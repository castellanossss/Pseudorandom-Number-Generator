import pyqtgraph as pg
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QWidget, QLabel, QSpinBox, QPushButton, QFrame, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtGui import QFont

class MCMTabContent(QWidget):
    """
        This is the Multiplicative Congruential Method tab content class.
        It inherits from QWidget, a base class for all user interface objects in PyQt.
    """

    # Define a PyQt signal to be emitted when the generate button is clicked
    generate_button_clicked = pyqtSignal()

    def __init__(self):
        """
            This is the constructor method for the MCMTabContent class.
            It initializes the tab and its components.
        """
        super().__init__()

        # Initialize and position the xo param label and spinbox
        self.xo_label = QLabel("Parameter Xo", self)
        self.xo_label.move(20, 21)
        self.xo_spinbox = QSpinBox(self)
        self.xo_spinbox.setRange(int(-1e+9), int(1e+9))
        self.xo_spinbox.move(100, 20)

        # Initialize and position the t param label and spinbox
        self.t_label = QLabel("Parameter t", self)
        self.t_label.move(230, 21)
        self.t_spinbox = QSpinBox(self)
        self.t_spinbox.setRange(int(-1e+9), int(1e+9))
        self.t_spinbox.move(300, 20)

        # Initialize and position the g param label and spinbox
        self.g_label = QLabel("Parameter g", self)
        self.g_label.move(420, 21)
        self.g_spinbox = QSpinBox(self)
        self.g_spinbox.setRange(int(-1e+9), int(1e+9))
        self.g_spinbox.move(490, 20)

        # Initialize and position the range minimum label and spinbox
        self.min_val_label = QLabel("Minimum Value", self)
        self.min_val_label.move(620, 21)
        self.min_val_spinbox = QSpinBox(self)
        self.min_val_spinbox.setRange(int(-1e+9), int(1e+9))
        self.min_val_spinbox.move(715, 20)

        # Initialize and position the range maximum label and spinbox
        self.max_val_label = QLabel("Maximum Value", self)
        self.max_val_label.move(845, 21)
        self.max_val_spinbox = QSpinBox(self)
        self.max_val_spinbox.setRange(int(-1e+9), int(1e+9))
        self.max_val_spinbox.move(940, 20)

        # Initialize and position the iterations amount label and spinbox
        self.iterations_amount_label = QLabel("Number of Iterations", self)
        self.iterations_amount_label.move(1070, 21)
        self.iterations_amount_spinbox = QSpinBox(self)
        self.iterations_amount_spinbox.setRange(0, int(1e+9))
        self.iterations_amount_spinbox.move(1190, 20)

        # Initialize and position the generate button
        self.generate_button = QPushButton("Generate", self)

        # Center the button in the bottom row
        self.generate_button.move(600, 61)

        # Initialize a horizontal line as a separator
        self.line = QFrame(self)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.setGeometry(10, 100, 1280, 3)

        # Initialize data variables to None. These will hold the data for the table and graph.
        self.data1 = None
        self.data2 = None
        self.data3 = None

        # Initialize a QTableWidget. This will be used to display the data.
        self.table = QTableWidget(self)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Set the style of the table
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

        # Position and resize the table
        self.table.move(10, 110)
        self.table.resize(640, 460)

        # Disable editing of the table contents
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        # Hide the vertical header of the table
        self.table.verticalHeader().setVisible(False)

        # Initialize a PlotWidget. This will be used to display the graph.
        self.graphWidget = pg.PlotWidget(self)

        # Position and resize the graph widget
        self.graphWidget.move(655, 110)
        self.graphWidget.resize(640, 440)

        # Set labels for the axes and a title for the graph
        self.graphWidget.setLabel('left', 'Ri')
        self.graphWidget.setLabel('bottom', 'Iteration')
        self.graphWidget.setTitle('Scatter Plot')

        # Set the background color of the graph to white
        self.graphWidget.setBackground('w')
        self.graphWidget.getAxis('bottom').setPen(pg.mkPen(color='k', width=1))
        self.graphWidget.getAxis('left').setPen(pg.mkPen(color='k', width=1))
        self.graphWidget.getAxis('bottom').setTextPen(pg.mkPen(color='k', width=1))
        self.graphWidget.getAxis('left').setTextPen(pg.mkPen(color='k', width=1))

        # Set the title color of the graph to black
        self.graphWidget.setTitle('Scatter Plot', color='k')

        # Connect the generate button's clicked signal to its slot
        self.generate_button.clicked.connect(self.generate_button_clicked)

    def set_data(self, data1, data2, data3):
        """
            This method sets the data for the table and graph.
            It takes three arguments: data1, data2, and data3, which are lists of data points.
        """
        self.data1 = data1
        self.data2 = data2
        self.data3 = data3

    def generateTable(self):
        """
            This method generates the table and scatter plot for the tab.
            It first checks if the data is not None, then clears the table and graph,
            fills the table with data, and creates a scatter plot.
        """

        # Check if data is None
        if self.data1 is None or self.data2 is None or self.data3 is None:
            return

        # Clear the table and graph before adding new data
        self.table.clearContents()
        self.graphWidget.clear()

        # Set the number of rows and columns in the table
        self.table.setRowCount(self.iterations_amount_spinbox.value())
        self.table.setColumnCount(4)

        # Set the header labels for the table
        header_labels = ['Iteration', 'Xi', 'Ri', 'Ni']
        self.table.setHorizontalHeaderLabels(header_labels)

        # Fill the table with data
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

        # Set the column headers to bold
        font = QFont()
        font.setBold(True)
        self.table.horizontalHeader().setFont(font)

        # Create a scatter plot with the data
        scatter = pg.ScatterPlotItem(size=10)
        scatter.setBrush(pg.mkBrush('r'))

        for i in range(1, self.iterations_amount_spinbox.value() + 1):
            scatter.addPoints([i], [self.data2[i - 1]])

        # Add the scatter plot to the graph widget
        self.graphWidget.addItem(scatter)

        # Adjust the graph's range to fit the data
        self.graphWidget.getViewBox().autoRange()

    def get_xo_spin_box_value(self):
        """
            This method returns the value of the xo param spin box.
        """
        return self.xo_spinbox.value()

    def get_t_spin_box_value(self):
        """
            This method returns the value of the t param spin box.
        """
        return self.t_spinbox.value()

    def get_g_spin_box_value(self):
        """
            This method returns the value of the g param spin box.
        """
        return self.g_spinbox.value()

    def get_min_spin_box_value(self):
        """
            This method returns the value of the minimum range spin box.
        """
        return self.min_val_spinbox.value()

    def get_max_spin_box_value(self):
        """
            This method returns the value of the maximum range spin box.
        """
        return self.max_val_spinbox.value()

    def get_iterations_spin_box_value(self):
        """
            This method returns the value of the iterations amount spin box.
        """
        return self.iterations_amount_spinbox.value()
