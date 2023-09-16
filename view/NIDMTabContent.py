import numpy as np
import matplotlib.pyplot as plt
import pyqtgraph as pg
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QWidget, QLabel, QSpinBox, QPushButton, QFrame, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtGui import QFont

class NIDMTabContent(QWidget):
    """
        Esta es la clase de contenido de la pestaña Método de distribución normal inversa.
        Hereda de QWidget, una clase base para todos los objetos de la interfaz de usuario en PyQt.
    """

    # Definir una señal PyQt que se emitirá cuando se haga clic en el botón generar.
    generate_button_clicked = pyqtSignal()

    def __init__(self):
        """
            Este es el método constructor de la clase NIDMTabContent.
            Inicializa la pestaña y sus componentes.
        """
        super().__init__()

        # Inicializa y posiciona la etiqueta de la cantidad de numeros Xi y el cuadro de giro.
        self.xi_amount_label = QLabel("Amount of Xi Numbers", self)
        self.xi_amount_label.move(220, 21)
        self.xi_amount_spinbox = QSpinBox(self)
        self.xi_amount_spinbox.setRange(0, int(1e+9))
        self.xi_amount_spinbox.move(350, 20)

        # Inicializa y posiciona la etiqueta de rango mínimo para los Xi y el cuadro de giro.
        self.min_val_label = QLabel("Minimum Xi Value", self)
        self.min_val_label.move(460, 21)
        self.min_val_spinbox = QSpinBox(self)
        self.min_val_spinbox.setRange(int(-1e+9), int(1e+9))
        self.min_val_spinbox.move(565, 20)

        # Inicializa y posiciona la etiqueta de rango máximo para los Xi y el cuadro de giro.
        self.max_val_label = QLabel("Maximum Xi Value", self)
        self.max_val_label.move(680, 21)
        self.max_val_spinbox = QSpinBox(self)
        self.max_val_spinbox.setRange(int(-1e+9), int(1e+9))
        self.max_val_spinbox.move(785, 20)

        # Inicializa y posiciona la etiqueta de cantidad de iteraciones y el cuadro de giro.
        self.iterations_amount_label = QLabel("Number of Iterations", self)
        self.iterations_amount_label.move(900, 21)
        self.iterations_amount_spinbox = QSpinBox(self)
        self.iterations_amount_spinbox.setRange(0, int(1e+9))
        self.iterations_amount_spinbox.move(1015, 20)

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

        # Establece el color de fondo del gráfico en blanco.
        self.graphWidget.setBackground('w')
        self.graphWidget.getAxis('bottom').setPen(pg.mkPen(color='k', width=1))
        self.graphWidget.getAxis('left').setPen(pg.mkPen(color='k', width=1))
        self.graphWidget.getAxis('bottom').setTextPen(pg.mkPen(color='k', width=1))
        self.graphWidget.getAxis('left').setTextPen(pg.mkPen(color='k', width=1))

        # Establece el color del título del gráfico en negro.
        self.graphWidget.setTitle('Gauss Bell', color='k')

        # Conecta la señal del boton cuando se da click sobre el.
        self.generate_button.clicked.connect(self.generate_button_clicked)

    def set_data(self, data1, data2):
        """
            Este método establece los datos para la tabla y el gráfico.
            Se necesitan dos argumentos: data1 y data2, que son listas de puntos de datos.
        """
        self.data1 = data1
        self.data2 = data2

    def generateTable(self):
        """
            Este método genera la tabla y un grafico que representa la Campana de Gauss para la pestaña.
            Primero verifique si los datos no son None, luego borre la tabla y el gráfico.
            Llene la tabla con datos y cree un gráfico de barras.
        """

        # Comprobar si los datos son None.
        if self.data1 is None or self.data2 is None:
            return

        # Borra la tabla y el gráfico antes de agregar nuevos datos.
        self.table.clearContents()
        self.graphWidget.clear()

        # Establece el número de filas y columnas de la tabla.
        self.table.setRowCount(self.iterations_amount_spinbox.value())
        self.table.setColumnCount(3)

        # Establece las etiquetas del encabezado de la tabla.
        header_labels = ['Iteration', 'Ri', 'Ni']
        self.table.setHorizontalHeaderLabels(header_labels)

        # Llenar la tabla con datos.
        for i in range(self.iterations_amount_spinbox.value()):
            item_i = QTableWidgetItem(str(i + 1))
            item_i.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(i, 0, item_i)

            item1 = QTableWidgetItem(str(self.data1[i]))
            item1.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(i, 1, item1)

            item2 = QTableWidgetItem(str(self.data2[i]))
            item2.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(i, 2, item2)

        # Establece los encabezados de las columnas en negrita.
        font = QFont()
        font.setBold(True)
        self.table.horizontalHeader().setFont(font)

        # Crea un histograma con los datos.
        counts, bins = np.histogram(self.data2, bins=121)  # Ni

        # Crea un gráfico de barras con los datos del histograma.
        bg1 = pg.BarGraphItem(x=np.arange(len(counts)), height=counts, width=0.6)

        # Agrega el gráfico de barras al widget de gráfico.
        self.graphWidget.addItem(bg1)

        # Ajustar el rango del gráfico para que se ajuste a los datos.
        self.graphWidget.getViewBox().autoRange()

        # Ahora vamos a crear el mismo gráfico con matplotlib, primero asignamos datos:
        data = self.data2

        # Calcular frecuencias y contenedores.
        counts, bins = np.histogram(data, bins=121)

        # Etiquetar los ejes
        plt.title('Gauss Bell')
        plt.xlabel('Intervals')
        plt.ylabel('Frequencies')

        # Gráfico de barras con datos
        plt.bar(range(1, len(bins)), counts)

        # Mostrar el gráfico
        plt.show()

    def get_xi_spin_box_value(self):
        """
            Este método devuelve el valor del cuadro de giro del parámetro xo.
        """
        return self.xi_amount_spinbox.value()

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
