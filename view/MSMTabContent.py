import pyqtgraph as pg
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QWidget, QLabel, QSpinBox, QPushButton, QFrame, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtGui import QFont

class MSMTabContent(QWidget):
    """
        Esta es la clase de contenido de la pestaña Método del cuadrado medio.
        Hereda de QWidget, una clase base para todos los objetos de la interfaz de usuario en PyQt.
    """

    # Definir una señal PyQt que se emitirá cuando se haga clic en el botón generar
    generate_button_clicked = pyqtSignal()

    def __init__(self):
        """
            Este es el método constructor de la clase MSMTabContent.
            Inicializa la pestaña y sus componentes.
        """
        super().__init__()

        # Inicializa y posiciona la etiqueta de la semilla y el cuadro de giro.
        self.seed_label = QLabel("Seed", self)
        self.seed_label.move(350, 21)
        self.seed_spinbox = QSpinBox(self)
        self.seed_spinbox.setRange(int(-1e+9), int(1e+9))
        self.seed_spinbox.move(390, 20)

        # Inicializa y posiciona la etiqueta de rango mínimo y el cuadro de giro.
        self.range_min_label = QLabel("Minimum Value", self)
        self.range_min_label.move(600, 21)
        self.range_min_spinbox = QSpinBox(self)
        self.range_min_spinbox.setRange(int(-1e+9), int(1e+9))
        self.range_min_spinbox.move(700, 20)

        # Inicializa y posiciona la etiqueta de rango máximo y el cuadro de giro.
        self.range_max_label = QLabel("Maximum Value", self)
        self.range_max_label.move(600, 61)
        self.range_max_spinbox = QSpinBox(self)
        self.range_max_spinbox.setRange(int(-1e+9), int(1e+9))
        self.range_max_spinbox.move(700, 60)

        # Inicializa y posiciona la etiqueta de cantidad de iteraciones y el cuadro de giro.
        self.iterations_amount_label = QLabel("Number of Iterations", self)
        self.iterations_amount_label.move(350, 61)
        self.iterations_amount_spinbox = QSpinBox(self)
        self.iterations_amount_spinbox.setRange(0, int(1e+9))
        self.iterations_amount_spinbox.move(475, 60)

        # Inicializa y posiciona el boton de generar.
        self.generate_button = QPushButton("Generate", self)
        self.generate_button.move(850, 38)

        # Inicializa una línea horizontal como separador.
        self.line = QFrame(self)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.setGeometry(10, 100, 1280, 3)

        # Inicializa las variables de datos en None. Estos contendrán los datos para la tabla y el gráfico.
        self.data1 = None
        self.data2 = None
        self.data3 = None

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
        self.graphWidget.setLabel('left', 'Ri')
        self.graphWidget.setLabel('bottom', 'Iteration')
        self.graphWidget.setTitle('Scatter Plot')

        # Establece el color de fondo del gráfico en blanco.
        self.graphWidget.setBackground('w')
        self.graphWidget.getAxis('bottom').setPen(pg.mkPen(color='k', width=1))
        self.graphWidget.getAxis('left').setPen(pg.mkPen(color='k', width=1))
        self.graphWidget.getAxis('bottom').setTextPen(pg.mkPen(color='k', width=1))
        self.graphWidget.getAxis('left').setTextPen(pg.mkPen(color='k', width=1))

        # Establece el color del título del gráfico en negro.
        self.graphWidget.setTitle('Scatter Plot', color='k')

        # Conecta la señal del boton cuando se da click sobre el.
        self.generate_button.clicked.connect(self.generate_button_clicked)

    def set_data(self, data1, data2, data3):
        """
            Este método establece los datos para la tabla y el gráfico.
            Se necesitan tres argumentos: data1, data2 y data3, que son listas de puntos de datos.
        """
        self.data1 = data1
        self.data2 = data2
        self.data3 = data3

    def generateTable(self):
        """
           Este método genera la tabla y el diagrama de dispersión para la pestaña.
            Primero verifica si los datos no son None, luego borra la tabla y el gráfico.
            Llena la tabla con datos y crea un diagrama de dispersión.
        """

        # Comprobar si los datos son None.
        if self.data1 is None or self.data2 is None or self.data3 is None:
            return

        # Borra la tabla y el gráfico antes de agregar nuevos datos.
        self.table.clearContents()
        self.graphWidget.clear()

        # Establece el número de filas y columnas de la tabla.
        self.table.setRowCount(self.iterations_amount_spinbox.value())
        self.table.setColumnCount(4)

        # Establece las etiquetas del encabezado de la tabla.
        header_labels = ['Iteration', 'Xi', 'Ri', 'Ni']
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

            item3 = QTableWidgetItem(str(self.data3[i]))
            item3.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(i, 3, item3)

        # Establece los encabezados de las columnas en negrita.
        font = QFont()
        font.setBold(True)
        self.table.horizontalHeader().setFont(font)

        # Crea un diagrama de dispersión con los datos.
        scatter = pg.ScatterPlotItem(size=10)
        scatter.setBrush(pg.mkBrush('r'))

        for i in range(1, self.iterations_amount_spinbox.value() + 1):
            scatter.addPoints([i], [self.data2[i - 1]])

        # Agregue el diagrama de dispersión al widget de gráfico.
        self.graphWidget.addItem(scatter)

        # Ajustar el rango del gráfico para que se ajuste a los datos.
        self.graphWidget.getViewBox().autoRange()

    def get_seed_spin_box_value(self):
        """
            Este método devuelve el valor del cuadro de giro del parámetro de la semilla.
        """
        return self.seed_spinbox.value()

    def get_min_spin_box_value(self):
        """
            Este método devuelve el valor del cuadro de giro de rango mínimo.
        """
        return self.range_min_spinbox.value()

    def get_max_spin_box_value(self):
        """
            Este método devuelve el valor del cuadro de giro de rango máximo.
        """
        return self.range_max_spinbox.value()

    def get_iterations_spin_box_value(self):
        """
            Este método devuelve el valor del cuadro de número de cantidad de iteraciones.
        """
        return self.iterations_amount_spinbox.value()
