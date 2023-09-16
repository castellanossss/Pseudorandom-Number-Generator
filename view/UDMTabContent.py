import numpy as np
import matplotlib.pyplot as plt
import pyqtgraph as pg
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QWidget, QLabel, QSpinBox, QPushButton, QFrame, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtGui import QFont

class UDMTabContent(QWidget):
    """
        Esta es la clase de contenido de la pestaña Método de distribución uniforme.
        Hereda de QWidget, una clase base para todos los objetos de la interfaz de usuario en PyQt.
    """

    # Definir una señal PyQt que se emitirá cuando se haga clic en el botón generar.
    generate_button_clicked = pyqtSignal()

    def __init__(self):
        """
            Este es el método constructor de la clase UDMTabContent.
            Inicializa la pestaña y sus componentes.
        """
        super().__init__()

        # Inicializa y posiciona la etiqueta de rango mínimo para los Xi y el cuadro de giro.
        self.min_val_label = QLabel("Minimum Value", self)
        self.min_val_label.move(360, 21)
        self.min_val_spinbox = QSpinBox(self)
        self.min_val_spinbox.setRange(int(-1e+9), int(1e+9))
        self.min_val_spinbox.move(455, 20)

        # Inicializa y posiciona la etiqueta de rango máximo para los Xi y el cuadro de giro.
        self.max_val_label = QLabel("Maximum Value", self)
        self.max_val_label.move(560, 21)
        self.max_val_spinbox = QSpinBox(self)
        self.max_val_spinbox.setRange(int(-1e+9), int(1e+9))
        self.max_val_spinbox.move(655, 20)

        # Inicializa y posiciona la etiqueta de cantidad de iteraciones y el cuadro de giro.
        self.iterations_amount_label = QLabel("Number of Iterations", self)
        self.iterations_amount_label.move(760, 21)
        self.iterations_amount_spinbox = QSpinBox(self)
        self.iterations_amount_spinbox.setRange(0, int(1e+9))
        self.iterations_amount_spinbox.move(880, 20)

        # Inicializa y posiciona el boton de generar.
        self.generate_button = QPushButton("Generate", self)
        self.generate_button.move(600, 61)

        # Inicializa una línea horizontal como separador.
        self.line = QFrame(self)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.setGeometry(10, 100, 1280, 3)

        # Inicializa las variables de datos en None. Estos contendrán los datos para la tabla y el gráfico.
        self.data1 = None
        self.data2 = None

        # Inicializa un QTableWidget. Esto se utilizará para mostrar los datos.
        self.table = QTableWidget(self)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Establece el estilo de la tabla.
        self.table.setStyleSheet("""
                                    QTableWidget {
                                        gridline-color: black;
                                        color: black;
                                    }
                                    QHeaderView::section {
                                        background-color: #29005f;
                                        color: white;
                                        font-weight: bold;
                                        border: 1px solid black;
                                    }
                                    QScrollBar:vertical {
                                        border: none;
                                        background: white;
                                        width: 14px;
                                        margin: 15px 0 15px 0;
                                    }
                                    QScrollBar::handle:vertical {        
                                        background: gray;
                                        min-height: 30px;
                                    }
                                    QScrollBar::add-line:vertical {
                                        border: none;
                                        background: none;
                                    }
                                    QScrollBar::sub-line:vertical {
                                        border: none;
                                        background: none;
                                    }
                                """)

        # Posiciona y cambia el tamaño de la tabla.
        self.table.move(10, 110)
        self.table.resize(640, 460)

        # Deshabilitar la edición del contenido de la tabla.
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        # Ocultar el encabezado vertical de la tabla.
        self.table.verticalHeader().setVisible(False)

        # Inicializa un PlotWidget. Esto se utilizará para mostrar el gráfico.
        self.graphWidget = pg.PlotWidget(self)

        # Posiciona y cambia el tamaño del widget gráfico.
        self.graphWidget.move(655, 110)
        self.graphWidget.resize(640, 440)

        # Establece etiquetas para los ejes y un título para el gráfico.
        self.graphWidget.setLabel('left', 'Frequencies')
        self.graphWidget.setLabel('bottom', 'Intervals')
        self.graphWidget.setTitle('Histogram')

        # Establece el color de fondo del gráfico en blanco.
        self.graphWidget.setBackground('w')
        self.graphWidget.getAxis('bottom').setPen(pg.mkPen(color='k', width=1))
        self.graphWidget.getAxis('left').setPen(pg.mkPen(color='k', width=1))
        self.graphWidget.getAxis('bottom').setTextPen(pg.mkPen(color='k', width=1))
        self.graphWidget.getAxis('left').setTextPen(pg.mkPen(color='k', width=1))

        # Establece el color del título del gráfico en negro.
        self.graphWidget.setTitle('Histogram', color='k')

        # Conecta la señal del boton cuando se da click sobre el.
        self.generate_button.clicked.connect(self.generate_button_clicked)

    def set_data(self, data1, data2):
        """
            Este método establece los datos para la tabla y el gráfico.
            Se necesitan dos argumentos: data1 y data2, que son listas de puntos de datos.
        """
        self.data1 = data1  # Ri
        self.data2 = data2  # Ni

    def generateTable(self):
        """
            Este método genera la tabla y el histograma para la pestaña.
            Primero verifica si los datos no son None, luego borra la tabla y el gráfico.
            Llena la tabla con datos y crea un histograma.
        """

        # Comprobar si los datos son None.
        if self.data1 is None or self.data2 is None:
            return

        # Borra la tabla y el gráfico antes de agregar nuevos datos.
        self.table.clearContents()
        self.graphWidget.clear()

        # Establece el número de filas y columnas de la tabla.
        self.table.setRowCount(len(self.data1))
        self.table.setColumnCount(3)

        # Establece las etiquetas del encabezado de la tabla.
        header_labels = ['Iteration', 'Ri', 'Ni']
        self.table.setHorizontalHeaderLabels(header_labels)

        # Llenar la tabla con datos.
        for i in range(len(self.data1)):
            item_i = QTableWidgetItem(str(i + 1))
            item_i.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(i, 0, item_i)

            item1 = QTableWidgetItem(str(self.data1[i]))  # Ri
            item1.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(i, 1, item1)

            item2 = QTableWidgetItem(str(self.data2[i]))  # Ni
            item2.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(i, 2, item2)

        # Establece los encabezados de las columnas en negrita.
        font = QFont()
        font.setBold(True)
        self.table.horizontalHeader().setFont(font)

        # Crea un histograma con los datos.
        num_bins = 51  # O cualquier otro número que prefieras
        y, x = np.histogram(self.data1, bins=np.linspace(0, 1, num_bins + 1))  # Ri
        curve = pg.PlotCurveItem(x, y, stepMode=True, fillLevel=0, brush=(0, 0, 255, 80))

        # Agrega el histograma al widget de gráfico.
        self.graphWidget.addItem(curve)

        # Ajustar el rango del gráfico para que se ajuste a los datos.
        self.graphWidget.getViewBox().autoRange()

        # Crea un histograma con matplotlib
        plt.hist(self.data1, bins=51, range=(0, 1), edgecolor='black')

        # Etiquetar los ejes
        plt.title('Histogram')
        plt.xlabel('Intervals')
        plt.ylabel('Frequencies')

        # Mostrar la grafico
        plt.show()

    def get_min_spin_box_value(self):
        """
            Este método devuelve el valor del cuadro de giro de rango mínimo.
        """
        return self.min_val_spinbox.value()

    def get_max_spin_box_value(self):
        """
            Este método devuelve el valor del cuadro de giro de rango máximo.
        """
        return self.max_val_spinbox.value()

    def get_iterations_spin_box_value(self):
        """
            Este método devuelve el valor del cuadro de número de cantidad de iteraciones.
        """
        return self.iterations_amount_spinbox.value()
