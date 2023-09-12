import sys
import os

from PyQt6.QtWidgets import QApplication, QMessageBox
from model.LinearCongruentialMethod import LinearCongruentialMethod
from model.MiddleSquareMethod import MiddleSquareMethod
from model.MultiplicativeCongruentialMethod import MultiplicativeCongruentialMethod
from model.NormalInvDistributionMethod import NormalInvDistributionMethod
from model.UniformDistributionMethod import UniformDistributionMethod
from view.MainFrame import MainFrame

class Presenter:
    """
        The Presenter class is responsible for managing the main frame of the application and connecting
        the generate button clicks from each tab to their respective methods. It also sets up the output directory
        where the results from each tab will be stored.
    """

    def __init__(self):
        """
            Initializes a new instance of the Presenter class.

            The constructor connects the generate button click event from each tab in the main frame to its
            respective method. It also sets up the output directory where the results from each tab will be stored.
        """
        # Create a MainFrame instance
        self.main_frame = MainFrame()

        # Connect the generate button click event from each tab in the main frame to its respective method
        self.main_frame.tab1.generate_button_clicked.connect(self.manage_tab1_info)
        self.main_frame.tab2.generate_button_clicked.connect(self.manage_tab2_info)
        self.main_frame.tab3.generate_button_clicked.connect(self.manage_tab3_info)
        self.main_frame.tab4.generate_button_clicked.connect(self.manage_tab4_info)
        self.main_frame.tab5.generate_button_clicked.connect(self.manage_tab5_info)

        # Define the project directory and output directory paths
        self.project_dir = os.path.dirname(os.path.dirname(__file__))
        self.output_dir = os.path.join(self.project_dir, 'Numbers Generated')

        # Create the output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)

    def manage_tab1_info(self):
        """
            This method manages the information for tab 1 of the main frame.

            It retrieves the input values from the spin boxes in tab 1, checks if the inputs are valid,
            and then uses these values to generate pseudorandom numbers using the Middle Square Method.
            The generated numbers are then displayed in a table in tab 1 and written to a text file.
        """
        # Retrieve input values from the spin boxes in tab 1
        seed = self.main_frame.tab1.get_seed_spin_box_value()
        min_value = self.main_frame.tab1.get_min_spin_box_value()
        max_value = self.main_frame.tab1.get_max_spin_box_value()
        iterations = self.main_frame.tab1.get_iterations_spin_box_value()

        # Check if the minimum value is greater than the maximum value
        if min_value > max_value:
            QMessageBox.critical(self.main_frame, "Error", "The minimum value cannot be greater than the maximum value.")
            return

        # Check if there are blank spaces in the input fields
        if not seed or min_value is None or max_value is None or not iterations:
            QMessageBox.critical(self.main_frame, "Error", "You cannot leave blank spaces.")
            return

        # Create a MiddleSquareMethod object and generate pseudorandom numbers
        msm = MiddleSquareMethod(seed, min_value, max_value, iterations)
        msm.generateRandoms()

        # Display the generated numbers in a table in tab 1
        self.main_frame.tab1.set_data(msm.get_xi_values_array(), msm.get_ri_values_array(), msm.get_ni_values_array())
        self.main_frame.tab1.generateTable()

        # Define the path for the output file
        self.file_path = os.path.join(self.output_dir, 'MiddleSquareValues.txt')

        # Write the generated numbers to a text file
        with open(self.file_path, 'w') as f:
            for value in msm.get_ri_values_array():
                f.write(str(value) + '\n')

    def manage_tab2_info(self):
        """
            This method manages the information for tab 2 of the main frame.

            It retrieves the input values from the spin boxes in tab 2, checks if the inputs are valid,
            and then uses these values to generate pseudorandom numbers using the Linear Congruential Method.
            The generated numbers are then displayed in a table in tab 2 and written to a text file.
        """
        # Retrieve input values from the spin boxes in tab 2
        xo_param = self.main_frame.tab2.get_xo_spin_box_value()
        k_param = self.main_frame.tab2.get_k_spin_box_value()
        c_param = self.main_frame.tab2.get_c_spin_box_value()
        g_param = self.main_frame.tab2.get_g_spin_box_value()
        min_value = self.main_frame.tab2.get_min_spin_box_value()
        max_value = self.main_frame.tab2.get_max_spin_box_value()
        iterations = self.main_frame.tab2.get_iterations_spin_box_value()

        # Check if c param is not zero
        if c_param == 0:
            QMessageBox.critical(self.main_frame, "Error", "The value of c cannot be 0.")
            return

        # Check if g param is less than xo param, k param and c param
        if g_param <= max(xo_param, k_param, c_param):
            QMessageBox.critical(self.main_frame, "Error",
                                 "The value of g must be greater than the values of xo, k, and c.")
            return

        # Check if there are blank spaces in the input fields
        if not xo_param or not k_param or not c_param or not g_param or min_value is None or max_value is None or not iterations:
            QMessageBox.critical(self.main_frame, "Error", "You cannot leave blank spaces.")
            return

        # Check if the minimum value is greater than the maximum value
        if min_value > max_value:
            QMessageBox.critical(self.main_frame, "Error",
                                 "The minimum value cannot be greater than the maximum value.")
            return

        # Create a LinearCongruentialMethod object and generate pseudorandom numbers
        lcm = LinearCongruentialMethod(xo_param, k_param, c_param, g_param, min_value, max_value, iterations)
        lcm.fillFirstXiValue()
        lcm.fillXiValues()
        lcm.fillRiAndNiValues()

        # Display the generated numbers in a table in tab 2
        self.main_frame.tab2.set_data(lcm.get_xi_values_array(), lcm.get_ri_values_array(), lcm.get_ni_values_array())
        self.main_frame.tab2.generateTable()

        # Define the path for the output file
        self.file_path = os.path.join(self.output_dir, 'LinearCongruentialValues.txt')

        # Write the generated numbers to a text file
        with open(self.file_path, 'w') as f:
            for value in lcm.get_ri_values_array():
                f.write(str(value) + '\n')

    def manage_tab3_info(self):
        """
            This method manages the information for tab 3 of the main frame.

            It retrieves the input values from the spin boxes in tab 3, checks if the inputs are valid,
            and then uses these values to generate pseudorandom numbers using the Multiplicative Congruential Method.
            The generated numbers are then displayed in a table in tab 3 and written to a text file.
        """
        # Retrieve input values from the spin boxes in tab 3
        xo_param = self.main_frame.tab3.get_xo_spin_box_value()
        t_param = self.main_frame.tab3.get_t_spin_box_value()
        g_param = self.main_frame.tab3.get_g_spin_box_value()
        min_value = self.main_frame.tab3.get_min_spin_box_value()
        max_value = self.main_frame.tab3.get_max_spin_box_value()
        iterations = self.main_frame.tab3.get_iterations_spin_box_value()

        # Check if g param is less than xo param and t param
        if g_param <= max(xo_param, t_param):
            QMessageBox.critical(self.main_frame, "Error",
                                 "The value of g must be greater than the values of xo and t.")
            return

        # Check if there are blank spaces in the input fields
        if not xo_param or not t_param or not g_param or min_value is None or max_value is None or not iterations:
            QMessageBox.critical(self.main_frame, "Error", "You cannot leave blank spaces.")
            return

        # Check if the minimum value is greater than the maximum value
        if min_value > max_value:
            QMessageBox.critical(self.main_frame, "Error",
                                 "The minimum value cannot be greater than the maximum value.")
            return

        # Create a MultiplicativeCongruentialMethod object and generate pseudorandom numbers
        mcm = MultiplicativeCongruentialMethod(xo_param, t_param, g_param, min_value, max_value, iterations)
        mcm.fillFirstXiValue()
        mcm.fillXiValues()
        mcm.fillRiAndNiValues()

        # Display the generated numbers in a table in tab 3
        self.main_frame.tab3.set_data(mcm.get_xi_values_array(), mcm.get_ri_values_array(), mcm.get_ni_values_array())
        self.main_frame.tab3.generateTable()

        # Define the path for the output file
        self.file_path = os.path.join(self.output_dir, 'MultiplicativeCongruentialValues.txt')

        # Write the generated numbers to a text file
        with open(self.file_path, 'w') as f:
            for value in mcm.get_ri_values_array():
                f.write(str(value) + '\n')

    def manage_tab4_info(self):
        """
            This method manages the information for tab 4 of the main frame.

            It retrieves the input values from the spin boxes in tab 4, checks if the inputs are valid,
            and then uses these values to generate pseudorandom numbers using the Uniform Distribution Method.
            The generated numbers are then displayed in a table in tab 4 and written to a text file.
        """
        # Retrieve input values from the spin boxes in tab 4
        min_value = self.main_frame.tab4.get_min_spin_box_value()
        max_value = self.main_frame.tab4.get_max_spin_box_value()
        iterations = self.main_frame.tab4.get_iterations_spin_box_value()

        # Check if the minimum value is greater than the maximum value
        if min_value > max_value:
            QMessageBox.critical(self.main_frame, "Error",
                                 "The minimum value cannot be greater than the maximum value.")
            return

        # Check if there are blank spaces in the input fields
        if min_value is None or max_value is None or iterations is None:
            QMessageBox.critical(self.main_frame, "Error", "You cannot leave blank spaces.")
            return

        # Create a UniformDistributionMethod object and generate pseudorandom numbers
        udm = UniformDistributionMethod(min_value, max_value, iterations)
        udm.fillRiValues()
        udm.fillNiValues()

        # Display the generated numbers in a table in tab 4
        self.main_frame.tab4.set_data(udm.get_ri_values_array(), udm.get_ni_values_array())
        self.main_frame.tab4.generateTable()

        # Define the path for the output file
        self.file_path = os.path.join(self.output_dir, 'UniformDistributionValues.txt')

        # Write the generated numbers to a text file
        with open(self.file_path, 'w') as f:
            for value in udm.get_ri_values_array():
                f.write(str(value) + '\n')

    def manage_tab5_info(self):
        """
            This method manages the information for tab 5 of the main frame.

            It retrieves the input values from the spin boxes in tab 5, checks if the inputs are valid,
            and then uses these values to generate pseudorandom numbers using the Normal Inverse Distribution Method.
            The generated numbers are then displayed in a table in tab 5 and written to a text file.
        """
        # Retrieve input values from the spin boxes in tab 5
        xi_amount = self.main_frame.tab5.get_xi_spin_box_value()
        min_value = self.main_frame.tab5.get_min_spin_box_value()
        max_value = self.main_frame.tab5.get_max_spin_box_value()
        iterations = self.main_frame.tab5.get_iterations_spin_box_value()

        # Check if the minimum value is greater than the maximum value
        if min_value > max_value:
            QMessageBox.critical(self.main_frame, "Error",
                                 "The minimum value cannot be greater than the maximum value.")
            return

        # Check if there are blank spaces in the input fields
        if min_value is None or max_value is None or iterations is None:
            QMessageBox.critical(self.main_frame, "Error", "You cannot leave blank spaces.")
            return

        # Create a NormalInvDistributionMethod object and generate pseudorandom numbers
        nidm = NormalInvDistributionMethod(xi_amount, min_value, max_value, iterations)
        nidm.fillRandomValues1()
        nidm.fillRandomValues2()
        nidm.fillXiValues()
        nidm.fillRiValues()
        nidm.fillNiValues()

        # Display the generated numbers in a table in tab 5
        self.main_frame.tab5.set_data(nidm.get_ri_values_array(), nidm.get_ni_values_array())
        self.main_frame.tab5.generateTable()

        # Define the path for the output file
        self.file_path = os.path.join(self.output_dir, 'InverseNormalDistributionValues.txt')

        # Write the generated numbers to a text file
        with open(self.file_path, 'w') as f:
            for value in nidm.get_ri_values_array():
                f.write(str(value) + '\n')

if __name__ == "__main__":
    """
        This is the main entry point of the application. It creates a QApplication, sets up the main frame of the application,
        and starts the application's event loop.
    """

    # Set the application's style sheet
    app = QApplication(sys.argv)
    app.setStyleSheet("""
    QWidget {
      background-color: white;
    }
    QLabel {
      color: black;
    }
    QPushButton {
      background-color: #FF4500;
      color: white;
      border: none;
      padding: 5px;
      min-width: 100px;
    }
    QPushButton:hover {
      background-color: #FF6347;
    }
    """)

    # Create a Presenter instance
    presenter = Presenter()

    # Set up the main frame
    presenter.main_frame.setFixedSize(1300, 600)

    # Get the screen's geometry and set the main frame's geometry accordingly
    screen = QApplication.primaryScreen().geometry()
    presenter.main_frame.setGeometry(
        round((screen.width() - 1300) / 2),
        round((screen.height() - 600) / 2),
        885,
        600
    )

    # Show the main frame
    presenter.main_frame.show()

    # Start the application's event loop
    sys.exit(app.exec())
