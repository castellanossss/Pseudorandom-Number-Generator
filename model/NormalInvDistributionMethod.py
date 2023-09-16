import numpy as np
from scipy.stats import norm

class NormalInvDistributionMethod:
    """
        Esta clase implementa el método de distribución inversa normal para generar números pseudoaleatorios.
    """

    def __init__(self, num_amount_xi, min, max, iterations):
        """
            Este es el método constructor de la clase NormalInvDistributionMethod.
            Inicializa la clase con los parámetros dados.
        """
        self.num_amount_xi = num_amount_xi  # Cantidad de numeros Xi a generar
        self.min = min  # Valor minimo para el rango de numeros aleatorios a crear
        self.max = max  # Valor maximo para el rango de numeros aleatorios a crear
        self.iterations = iterations  # Numero de iteraciones
        self.ri_values = []  # Lista para almacenar los valores de Ri
        self.ni_values = []  # Lista para almacenar los valores de Ni
        self.random_values_1 = []  # Lista para almacenar el primer arreglo de numeros aleatorios
        self.random_values_2 = []  # Lista para almacenar el segundo arreglo de numeros aleatorios
        self.xi_values = []  # Lista para almacenar los valores de Xi

    def fillRandomValues1(self):
        """
            Este método genera y almacena el primer conjunto de valores aleatorios utilizando una distribución uniforme.
        """
        for i in range(self.num_amount_xi):
            random_number = np.random.uniform(self.min, self.max)
            self.random_values_1.append(round(random_number, 5))

    def fillRandomValues2(self):
        """
            Este método genera y almacena el segundo conjunto de valores aleatorios utilizando una distribución uniforme.
        """
        for i in range(self.num_amount_xi):
            random_value = np.random.uniform()
            self.random_values_2.append(round(random_value, 5))

    def fillXiValues(self):
        """
            Este método calcula y almacena valores Xi en función de los dos conjuntos de valores aleatorios.
        """
        for i in range(len(self.random_values_1)):
            for j in range(len(self.random_values_2)):
                self.xi_values.append(self.random_values_1[i] + self.random_values_2[j])

    def findXiValuesAverage(self):
        """
            Este método calcula y devuelve el promedio de los valores Xi.
        """
        return np.mean(self.xi_values)

    def findXiValuesSDeviation(self):
        """
            Este método calcula y devuelve la desviación estándar de los valores Xi.
        """
        return np.std(self.xi_values)

    def fillRiValues(self):
        """
            Este método genera y almacena valores de Ri utilizando una distribución uniforme.
        """
        for i in range(self.iterations):
            random_number = np.random.uniform()
            self.ri_values.append(round(random_number, 5))

    def fillNiValues(self):
        """
            Este método calcula y almacena los valores de Ni basándose en los valores de Ri utilizando la distribución inversa de la normal.
        """
        average = self.findXiValuesAverage()
        standard_deviation = self.findXiValuesSDeviation()

        for i in range(len(self.ri_values)):
            self.ni_values.append(round(norm.ppf(self.ri_values[i], loc=average, scale=standard_deviation), 5))

    def get_ri_values_array(self):
        """
            Este método devuelve el arreglo de valores Ri.
        """
        return self.ri_values

    def get_ni_values_array(self):
        """
            Este método devuelve el arreglo de valores Ni.
        """
        return self.ni_values
