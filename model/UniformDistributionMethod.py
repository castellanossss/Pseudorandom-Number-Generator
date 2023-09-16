import numpy as np

class UniformDistributionMethod:
    """
        Esta clase implementa el método de distribución uniforme para generar números pseudoaleatorios.
    """

    def __init__(self, min, max, num_amount):
        """
            Este es el método constructor de la clase UniformDistributionMethod.
            Inicializa la clase con los parámetros dados.
        """
        self.min = min  # Valor minimo para el rango de numeros aleatorios a crear
        self.max = max  # Valor maximo para el rango de numeros aleatorios a crear
        self.num_amount = num_amount  # Cantidad de numeros a generar
        self.ri_values = []  # Lista para almacenar los valores de Ri
        self.ni_values = []  # Lista para almacenar los valores de Ni

    def fillRiValues(self):
        """
            Este método genera y almacena valores de Ri utilizando una distribución uniforme.
        """
        for i in range(self.num_amount):
            value = round(np.random.uniform(), 5)
            self.ri_values.append(round(value, 5))

    def obtainMinValue(self):
        """
            Este método devuelve el valor mínimo para el rango de los numeros Ni.
        """
        return self.min

    def obtainMaxValue(self):
        """
            Este método devuelve el valor máximo para el rango de los numeros Ni.
        """
        return self.max

    def fillNiValues(self):
        """
            Este método calcula y almacena los valores de Ni en función de los valores de Ri.
        """
        min_value = self.obtainMinValue()
        max_value = self.obtainMaxValue()

        for i in range(len(self.ri_values)):
            value = min_value + (max_value - min_value) * self.ri_values[i]
            self.ni_values.append(round(value, 5))

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
