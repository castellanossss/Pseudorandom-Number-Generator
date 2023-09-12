import os
from PyQt6.QtWidgets import QMainWindow, QTabWidget
from PyQt6.QtGui import QIcon

from view.LCMTabContent import LCMTabContent
from view.MCMTabContent import MCMTabContent
from view.MSMTabContent import MSMTabContent
from view.NIDMTabContent import NIDMTabContent
from view.UDMTabContent import UDMTabContent


class MainFrame(QMainWindow):
    """
        This is the main window class for the Number Generator application.
        It inherits from QMainWindow, a type of main application window in PyQt.
    """

    def __init__(self):
        """
            This is the constructor method for the MainFrame class.
            It initializes the main window and its components.
        """

        super().__init__()
        # Set the window title
        self.setWindowTitle("Number Generator")

        # Get the absolute path of the project directory
        project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Define the path for the icon
        icon_path = os.path.join(project_dir, 'icons', '7.png')

        # Set the window icon
        self.setWindowIcon(QIcon(icon_path))

        # Initialize a QTabWidget. This will contain all the tabs in the main window.
        self.tab_widget = QTabWidget()

        # Initialize the content for each tab
        self.tab1 = MSMTabContent()  # Middle Square Method tab
        self.tab2 = LCMTabContent()  # Linear Congruential Method tab
        self.tab3 = MCMTabContent()  # Multiplicative Congruential Method tab
        self.tab4 = UDMTabContent()  # Uniform Distribution Method tab
        self.tab5 = NIDMTabContent()  # Normal Distribution Method tab

        # Add each tab to the QTabWidget with a label
        self.tab_widget.addTab(self.tab1, "Middle Square Method")
        self.tab_widget.addTab(self.tab2, "Linear Congruential Method")
        self.tab_widget.addTab(self.tab3, "Multiplicative Congruential Method")
        self.tab_widget.addTab(self.tab4, "Uniform Distribution Method")
        self.tab_widget.addTab(self.tab5, "Normal Distribution Method")

        # Set the QTabWidget as the central widget of the main window
        self.setCentralWidget(self.tab_widget)
