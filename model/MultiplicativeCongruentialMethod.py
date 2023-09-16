class MultiplicativeCongruentialMethod:
    """
        Esta clase implementa el método multiplicativo congruencial para generar números pseudoaleatorios.
    """

    def __init__(self, xo, t, g, min, max, iterations):
        """
            Este es el método constructor de la clase MultiplicativeCongruentialMethod.
            Inicializa la clase con los parámetros dados.
        """
        self.xi_values = []  # Lista para almacenar los valores de Xi
        self.ri_values = []  # Lista para almacenar los valores de Ri
        self.ni_values = []  # Lista para almacenar los valores de Ni
        self.xo = xo  # Valor inicial semilla
        self.t = t  # Parametro multiplicador
        self.g = g  # Parametro del modulo
        self.min = min  # Valor minimo para el rango
        self.max = max  # Valor maximo para el rango
        self.iterations = iterations  # Numero de iteraciones

    def generateAValue(self):
        """
            Este método genera el valor 'a' utilizado en la fórmula congruente multiplicativa.
        """
        return (8 * self.t) + 3

    def determinateNumberAmount(self):
        """
            Este método determina el número de posibles valores únicos.
        """
        return 2 ** self.g

    def fillFirstXiValue(self):
        """
            Este método calcula y almacena el primer valor Xi.
        """
        a = self.generateAValue()
        amount = self.determinateNumberAmount()
        value = ((a * self.xo)) % amount
        self.xi_values.append(round(value, 5))

    def fillXiValues(self):
        """
            Este método calcula y almacena todos los valores Xi posteriores.
        """
        a = self.generateAValue()
        amount = self.determinateNumberAmount()
        for i in range(self.iterations - 1):
            value = ((a * self.xi_values[i])) % amount
            self.xi_values.append(round(value, 5))

    def fillRiAndNiValues(self):
        """
            Este método calcula y almacena todos los valores de Ri y Ni.
        """
        num_amount = self.determinateNumberAmount()
        for i in range(self.iterations):
            ri_value = float(self.xi_values[i]) / (num_amount - 1)
            self.ri_values.append(round(ri_value, 5))

            ni_value = self.min + (self.max - self.min) * ri_value
            self.ni_values.append(round(ni_value, 5))

    def get_xi_values_array(self):
        """
            Este método devuelve el arreglo de valores Xi.
        """
        return self.xi_values

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
