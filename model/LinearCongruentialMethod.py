class LinearCongruentialMethod:
    """
        This class implements the Linear Congruential Method for generating pseudo-random numbers.
    """

    def __init__(self, xo, k, c, g, min, max, iterations):
        """
            This is the constructor method for the LinearCongruentialMethod class.
            It initializes the class with the given parameters.
        """
        self.xi_values = []  # List to hold Xi values
        self.ri_values = []  # List to hold Ri values
        self.ni_values = []  # List to hold Ni values
        self.xo = xo  # Initial seed value
        self.k = k  # Multiplier
        self.c = c  # Increment
        self.g = g  # Modulus parameter
        self.min = min  # Minimum value for Ni
        self.max = max  # Maximum value for Ni
        self.iterations = iterations  # Number of iterations

    def generateAValue(self):
        """
            This method generates the 'a' value used in the linear congruential formula.
        """
        return 1 + (2 * self.k)

    def determinateNumberAmount(self):
        """
            This method determines the number of possible unique values.
        """
        return 2 ** self.g

    def fillFirstXiValue(self):
        """
            This method calculates and stores the first Xi value.
        """
        a = self.generateAValue()
        amount = self.determinateNumberAmount()
        value = ((a * self.xo) + self.c) % amount
        self.xi_values.append(round(value, 5))

    def fillXiValues(self):
        """
            This method calculates and stores all subsequent Xi values.
        """
        a = self.generateAValue()
        amount = self.determinateNumberAmount()
        for i in range(self.iterations - 1):
            value = ((a * self.xi_values[i]) + self.c) % amount
            self.xi_values.append(round(value, 5))

    def fillRiAndNiValues(self):
        """
            This method calculates and stores all Ri and Ni values.
        """
        num_amount = self.determinateNumberAmount()
        for i in range(self.iterations):
            ri_value = float(self.xi_values[i]) / (num_amount - 1)
            self.ri_values.append(round(ri_value, 5))

            ni_value = self.min + (self.max - self.min) * ri_value
            self.ni_values.append(round(ni_value, 5))

    def get_xi_values_array(self):
        """
            This method returns the array of Xi values.
        """
        return self.xi_values

    def get_ri_values_array(self):
        """
            This method returns the array of Ri values.
        """
        return self.ri_values

    def get_ni_values_array(self):
        """
            This method returns the array of Ni values.
        """
        return self.ni_values
