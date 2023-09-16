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
        La clase Presenter es responsable de administrar el marco principal de la aplicación y conectar
        el botón generar hace clic en cada pestaña a sus respectivos métodos. También configura el directorio de salida.
        donde se almacenarán los resultados de cada pestaña.
    """

    def __init__(self):
        """
            Inicializa una nueva instancia de la clase Presenter.

             El constructor conecta el evento de clic del botón generar de cada pestaña en el marco principal a su
             método respectivo. También configura el directorio de salida donde se almacenarán los resultados de cada pestaña.
        """
        # Crear una instancia de MainFrame
        self.main_frame = MainFrame()

        # Conecta el evento de clic del botón generar de cada pestaña en el marco principal a su método respectivo
        self.main_frame.tab1.generate_button_clicked.connect(self.manage_tab1_info)
        self.main_frame.tab2.generate_button_clicked.connect(self.manage_tab2_info)
        self.main_frame.tab3.generate_button_clicked.connect(self.manage_tab3_info)
        self.main_frame.tab4.generate_button_clicked.connect(self.manage_tab4_info)
        self.main_frame.tab5.generate_button_clicked.connect(self.manage_tab5_info)

        # Define las rutas del directorio del proyecto y del directorio de salida
        self.project_dir = os.path.dirname(os.path.dirname(__file__))
        self.output_dir = os.path.join(self.project_dir, 'Numbers Generated')

        # Crea el directorio de salida si no existe
        os.makedirs(self.output_dir, exist_ok=True)

    def manage_tab1_info(self):
        """
            Este método gestiona la información de la pestaña 1 de la ventana principal MainFrame.

            Recupera los valores de entrada de los cuadros de giro en la pestaña 1, verifica si las entradas son válidas,
            y luego usa estos valores para generar números pseudoaleatorios usando el Método del Cuadrado Medio.
            Los números generados luego se muestran en una tabla en la pestaña 1 y se escriben en un archivo de texto.
        """
        # Recupera los valores de entrada de los cuadros de giro en la pestaña 1
        seed = self.main_frame.tab1.get_seed_spin_box_value()
        min_value = self.main_frame.tab1.get_min_spin_box_value()
        max_value = self.main_frame.tab1.get_max_spin_box_value()
        iterations = self.main_frame.tab1.get_iterations_spin_box_value()

        # Comprueba si el valor mínimo es mayor que el valor máximo
        if min_value > max_value:
            QMessageBox.critical(self.main_frame, "Error", "The minimum value cannot be greater than the maximum value.")
            return

        # Comprueba si hay espacios en blanco en los campos de entrada
        if not seed or min_value is None or max_value is None or not iterations:
            QMessageBox.critical(self.main_frame, "Error", "You cannot leave blank spaces.")
            return

        # Crea un objeto MiddleSquareMethod y genera números pseudoaleatorios
        msm = MiddleSquareMethod(seed, min_value, max_value, iterations)
        msm.generateRandoms()

        # Muestra los números generados en una tabla en la pestaña 1
        self.main_frame.tab1.set_data(msm.get_xi_values_array(), msm.get_ri_values_array(), msm.get_ni_values_array())
        self.main_frame.tab1.generateTable()

        # Define la ruta para el archivo de salida
        self.file_path = os.path.join(self.output_dir, 'MiddleSquareValues.txt')

        # Escribe los números generados en un archivo de texto
        with open(self.file_path, 'w') as f:
            for value in msm.get_ri_values_array():
                f.write(str(value) + '\n')

    def manage_tab2_info(self):
        """
            Este método gestiona la información de la pestaña 2 de la ventana principal MainFrame.

            Recupera los valores de entrada de los cuadros de giro en la pestaña 2, verifica si las entradas son válidas,
            y luego usa estos valores para generar números pseudoaleatorios usando el Método de Congruencial Lineal.
            Los números generados luego se muestran en una tabla en la pestaña 2 y se escriben en un archivo de texto.
        """
        # Recupera los valores de entrada de los cuadros de giro en la pestaña 2
        xo_param = self.main_frame.tab2.get_xo_spin_box_value()
        k_param = self.main_frame.tab2.get_k_spin_box_value()
        c_param = self.main_frame.tab2.get_c_spin_box_value()
        g_param = self.main_frame.tab2.get_g_spin_box_value()
        min_value = self.main_frame.tab2.get_min_spin_box_value()
        max_value = self.main_frame.tab2.get_max_spin_box_value()
        iterations = self.main_frame.tab2.get_iterations_spin_box_value()

        # Comprueba si el parámetro c no es cero
        if c_param == 0:
            QMessageBox.critical(self.main_frame, "Error", "The value of c cannot be 0.")
            return

        # Comprueba si g param es menor que xo param, k param y c param
        if g_param <= max(xo_param, k_param, c_param):
            QMessageBox.critical(self.main_frame, "Error",
                                 "The value of g must be greater than the values of xo, k, and c.")
            return

        # Comprueba si hay espacios en blanco en los campos de entrada
        if not xo_param or not k_param or not c_param or not g_param or min_value is None or max_value is None or not iterations:
            QMessageBox.critical(self.main_frame, "Error", "You cannot leave blank spaces.")
            return

        # Comprueba si el valor mínimo es mayor que el valor máximo
        if min_value > max_value:
            QMessageBox.critical(self.main_frame, "Error",
                                 "The minimum value cannot be greater than the maximum value.")
            return

        # Crea un objeto LinearCongruentialMethod y genera números pseudoaleatorios
        lcm = LinearCongruentialMethod(xo_param, k_param, c_param, g_param, min_value, max_value, iterations)
        lcm.fillFirstXiValue()
        lcm.fillXiValues()
        lcm.fillRiAndNiValues()

        # Muestra los números generados en una tabla en la pestaña 2
        self.main_frame.tab2.set_data(lcm.get_xi_values_array(), lcm.get_ri_values_array(), lcm.get_ni_values_array())
        self.main_frame.tab2.generateTable()

        # Define la ruta para el archivo de salida
        self.file_path = os.path.join(self.output_dir, 'LinearCongruentialValues.txt')

        # Escribe los números generados en un archivo de texto
        with open(self.file_path, 'w') as f:
            for value in lcm.get_ri_values_array():
                f.write(str(value) + '\n')

    def manage_tab3_info(self):
        """
            Este método gestiona la información de la pestaña 3 de la ventana principal MainFrame.

            Recupera los valores de entrada de los cuadros de giro en la pestaña 3, verifica si las entradas son válidas,
            y luego usa estos valores para generar números pseudoaleatorios usando el Método Multiplicativo Congruencial.
            Los números generados luego se muestran en una tabla en la pestaña 3 y se escriben en un archivo de texto.
        """
        # Recupera los valores de entrada de los cuadros de giro en la pestaña 3
        xo_param = self.main_frame.tab3.get_xo_spin_box_value()
        t_param = self.main_frame.tab3.get_t_spin_box_value()
        g_param = self.main_frame.tab3.get_g_spin_box_value()
        min_value = self.main_frame.tab3.get_min_spin_box_value()
        max_value = self.main_frame.tab3.get_max_spin_box_value()
        iterations = self.main_frame.tab3.get_iterations_spin_box_value()

        # Comprueba si g param es menor que xo param y t param
        if g_param <= max(xo_param, t_param):
            QMessageBox.critical(self.main_frame, "Error",
                                 "The value of g must be greater than the values of xo and t.")
            return

        # Comprueba si hay espacios en blanco en los campos de entrada
        if not xo_param or not t_param or not g_param or min_value is None or max_value is None or not iterations:
            QMessageBox.critical(self.main_frame, "Error", "You cannot leave blank spaces.")
            return

        # Comprueba si el valor mínimo es mayor que el valor máximo
        if min_value > max_value:
            QMessageBox.critical(self.main_frame, "Error",
                                 "The minimum value cannot be greater than the maximum value.")
            return

        # Crea un objeto MultiplicativeCongruentialMethod y genera números pseudoaleatorios
        mcm = MultiplicativeCongruentialMethod(xo_param, t_param, g_param, min_value, max_value, iterations)
        mcm.fillFirstXiValue()
        mcm.fillXiValues()
        mcm.fillRiAndNiValues()

        # Muestra los números generados en una tabla en la pestaña 3
        self.main_frame.tab3.set_data(mcm.get_xi_values_array(), mcm.get_ri_values_array(), mcm.get_ni_values_array())
        self.main_frame.tab3.generateTable()

        # Define la ruta para el archivo de salida
        self.file_path = os.path.join(self.output_dir, 'MultiplicativeCongruentialValues.txt')

        # Escribe los números generados en un archivo de texto
        with open(self.file_path, 'w') as f:
            for value in mcm.get_ri_values_array():
                f.write(str(value) + '\n')

    def manage_tab4_info(self):
        """
            Este método gestiona la información de la pestaña 4 de la ventana principal MainFrame.

            Recupera los valores de entrada de los cuadros de giro en la pestaña 4, verifica si las entradas son válidas,
            y luego usa estos valores para generar números pseudoaleatorios usando el Método de Distribución Uniforme.
            Los números generados luego se muestran en una tabla en la pestaña 4 y se escriben en un archivo de texto.
        """
        # Recupera los valores de entrada de los cuadros de giro en la pestaña 4
        min_value = self.main_frame.tab4.get_min_spin_box_value()
        max_value = self.main_frame.tab4.get_max_spin_box_value()
        iterations = self.main_frame.tab4.get_iterations_spin_box_value()

        # Comprueba si el valor mínimo es mayor que el valor máximo
        if min_value > max_value:
            QMessageBox.critical(self.main_frame, "Error",
                                 "The minimum value cannot be greater than the maximum value.")
            return

        # Comprueba si hay espacios en blanco en los campos de entrada
        if min_value is None or max_value is None or iterations is None:
            QMessageBox.critical(self.main_frame, "Error", "You cannot leave blank spaces.")
            return

        # Crea un objeto UniformDistributionMethod y genera números pseudoaleatorios
        udm = UniformDistributionMethod(min_value, max_value, iterations)
        udm.fillRiValues()
        udm.fillNiValues()

        # Muestra los números generados en una tabla en la pestaña 4
        self.main_frame.tab4.set_data(udm.get_ri_values_array(), udm.get_ni_values_array())
        self.main_frame.tab4.generateTable()

        # Define la ruta para el archivo de salida
        self.file_path = os.path.join(self.output_dir, 'UniformDistributionValues.txt')

        # Escribe los números generados en un archivo de texto
        with open(self.file_path, 'w') as f:
            for value in udm.get_ri_values_array():
                f.write(str(value) + '\n')

    def manage_tab5_info(self):
        """
            Este método gestiona la información de la pestaña 5 de la ventana principal MainFrame.

            Recupera los valores de entrada de los cuadros de giro en la pestaña 5, verifica si las entradas son válidas,
            y luego usa estos valores para generar números pseudoaleatorios usando el Método de Distribución Normal.
            Los números generados luego se muestran en una tabla en la pestaña 5 y se escriben en un archivo de texto.
        """
        # Recupera los valores de entrada de los cuadros de giro en la pestaña 4
        xi_amount = self.main_frame.tab5.get_xi_spin_box_value()
        min_value = self.main_frame.tab5.get_min_spin_box_value()
        max_value = self.main_frame.tab5.get_max_spin_box_value()
        iterations = self.main_frame.tab5.get_iterations_spin_box_value()

        # Comprueba si el valor mínimo es mayor que el valor máximo
        if min_value > max_value:
            QMessageBox.critical(self.main_frame, "Error",
                                 "The minimum value cannot be greater than the maximum value.")
            return

        # Comprueba si hay espacios en blanco en los campos de entrada
        if min_value is None or max_value is None or iterations is None:
            QMessageBox.critical(self.main_frame, "Error", "You cannot leave blank spaces.")
            return

        # Crear un objeto NormalInvDistributionMethod y genera números pseudoaleatorios
        nidm = NormalInvDistributionMethod(xi_amount, min_value, max_value, iterations)
        nidm.fillRandomValues1()
        nidm.fillRandomValues2()
        nidm.fillXiValues()
        nidm.fillRiValues()
        nidm.fillNiValues()

        # Muestra los números generados en una tabla en la pestaña 5
        self.main_frame.tab5.set_data(nidm.get_ri_values_array(), nidm.get_ni_values_array())
        self.main_frame.tab5.generateTable()

        # Define la ruta para el archivo de salida
        self.file_path = os.path.join(self.output_dir, 'InverseNormalDistributionValues.txt')

        # Escribe los números generados en un archivo de texto
        with open(self.file_path, 'w') as f:
            for value in nidm.get_ri_values_array():
                f.write(str(value) + '\n')

if __name__ == "__main__":
    """
        Este es el principal punto de entrada de la aplicación. Crea una QApplication, configura el marco principal de la aplicación,
        e inicia el bucle de eventos de la aplicación.
    """

    # Establece la hoja de estilo de la aplicación.
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

    # Crea una instancia de presentador
    presenter = Presenter()

    # Configura el marco principal
    presenter.main_frame.setFixedSize(1300, 600)

    # Obtiene la geometría de la pantalla y configura la geometría del marco principal en consecuencia
    screen = QApplication.primaryScreen().geometry()
    presenter.main_frame.setGeometry(
        round((screen.width() - 1300) / 2),
        round((screen.height() - 600) / 2),
        885,
        600
    )

    # Muestra la pantalla principal MainFrame
    presenter.main_frame.show()

    # Inicia el bucle de eventos de la aplicación.
    sys.exit(app.exec())
