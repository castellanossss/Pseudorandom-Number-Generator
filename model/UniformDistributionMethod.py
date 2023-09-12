import numpy as np

class UniformDistributionMethod:
    """
        This class implements the Uniform Distribution Method for generating pseudo-random numbers.
    """

    def __init__(self, min, max, num_amount):
        """
            This is the constructor method for the UniformDistributionMethod class.
            It initializes the class with the given parameters.
        """
        self.min = min  # Minimum value for Ni
        self.max = max  # Maximum value for Ni
        self.num_amount = num_amount  # Number of random numbers to generate
        self.ri_values = []  # List to hold Ri values
        self.ni_values = []  # List to hold Ni values

    def fillRiValues(self):
        """
            This method generates and stores Ri values using a uniform distribution.
        """
        for i in range(self.num_amount):
            value = round(np.random.uniform(), 5)
            self.ri_values.append(round(value, 5))

    def obtainMinValue(self):
        """
            This method returns the minimum value for Ni.
        """
        return self.min

    def obtainMaxValue(self):
        """
            This method returns the maximum value for Ni.
        """
        return self.max

    def fillNiValues(self):
        """
            This method calculates and stores Ni values based on the Ri values.
        """
        min_value = self.obtainMinValue()
        max_value = self.obtainMaxValue()

        for i in range(len(self.ri_values)):
            value = min_value + (max_value - min_value) * self.ri_values[i]
            self.ni_values.append(round(value, 5))

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
