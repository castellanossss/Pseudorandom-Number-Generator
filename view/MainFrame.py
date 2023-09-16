import os

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QTabWidget
from view.LCMTabContent import LCMTabContent
from view.MCMTabContent import MCMTabContent
from view.MSMTabContent import MSMTabContent
from view.NIDMTabContent import NIDMTabContent
from view.UDMTabContent import UDMTabContent


class MainFrame(QMainWindow):
    """
        Esta es la clase de ventana principal de la aplicación Generador de números.
         Hereda de QMainWindow, un tipo de ventana principal de la aplicación en PyQt.
    """

    def __init__(self):
        """
            Este es el método constructor de la clase MainFrame.
            Inicializa la ventana principal y sus componentes.
        """

        super().__init__()
        # Establece el título de la ventana.
        self.setWindowTitle("Number Generator")

        # Obtiene la ruta absoluta del proyecto
        project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Define la ruta para el icono
        icon_path = os.path.join(project_dir, 'icons', '7.png')

        # Establece el icono de la ventana
        self.setWindowIcon(QIcon(icon_path))

        # Inicializa un QTabWidget. Esto contendrá todas las pestañas de la ventana principal.
        self.tab_widget = QTabWidget()

        # Inicializa el contenido de cada pestaña.
        self.tab1 = MSMTabContent()  # Middle Square Method tab
        self.tab2 = LCMTabContent()  # Linear Congruential Method tab
        self.tab3 = MCMTabContent()  # Multiplicative Congruential Method tab
        self.tab4 = UDMTabContent()  # Uniform Distribution Method tab
        self.tab5 = NIDMTabContent()  # Normal Distribution Method tab

        # Agrega cada pestaña al QTabWidget con una etiqueta,
        self.tab_widget.addTab(self.tab1, "Middle Square Method")
        self.tab_widget.addTab(self.tab2, "Linear Congruential Method")
        self.tab_widget.addTab(self.tab3, "Multiplicative Congruential Method")
        self.tab_widget.addTab(self.tab4, "Uniform Distribution Method")
        self.tab_widget.addTab(self.tab5, "Normal Distribution Method")

        # Establece QTabWidget como el widget central de la ventana principal.
        self.setCentralWidget(self.tab_widget)
