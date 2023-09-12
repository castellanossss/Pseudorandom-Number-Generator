import numpy as np
from scipy.stats import norm

class NormalInvDistributionMethod:
    """
        This class implements the Normal Inverse Distribution Method for generating pseudo-random numbers.
    """

    def __init__(self, num_amount_xi, min, max, iterations):
        """
            This is the constructor method for the NormalInvDistributionMethod class.
            It initializes the class with the given parameters.
        """
        self.num_amount_xi = num_amount_xi  # Number of Xi values to generate
        self.min = min  # Minimum value for random number generation
        self.max = max  # Maximum value for random number generation
        self.iterations = iterations  # Number of iterations
        self.ri_values = []  # List to hold Ri values
        self.ni_values = []  # List to hold Ni values
        self.random_values_1 = []  # List to hold first set of random values
        self.random_values_2 = []  # List to hold second set of random values
        self.xi_values = []  # List to hold Xi values
        self.intervals_values = []  # List to hold interval values
        self.frequencies_values = []  # List to hold frequency values

    def fillRandomValues1(self):
        """
            This method generates and stores the first set of random values using a uniform distribution.
        """
        for i in range(self.num_amount_xi):
            random_number = np.random.uniform(self.min, self.max)
            self.random_values_1.append(round(random_number, 5))

    def fillRandomValues2(self):
        """
            This method generates and stores the second set of random values using a uniform distribution.
        """
        for i in range(self.num_amount_xi):
            random_value = np.random.uniform()
            self.random_values_2.append(round(random_value, 5))

    def fillXiValues(self):
        """
            This method calculates and stores Xi values based on the two sets of random values.
        """
        for i in range(len(self.random_values_1)):
            for j in range(len(self.random_values_2)):
                self.xi_values.append(self.random_values_1[i] + self.random_values_2[j])

    def findXiValuesAverage(self):
        """
            This method calculates and returns the average of the Xi values.
        """
        return np.mean(self.xi_values)

    def findXiValuesSDeviation(self):
        """
            This method calculates and returns the standard deviation of the Xi values.
        """
        return np.std(self.xi_values)

    def fillRiValues(self):
        """
            This method generates and stores Ri values using a uniform distribution.
        """
        for i in range(self.iterations):
            random_number = np.random.uniform()
            self.ri_values.append(round(random_number, 5))

    def fillNiValues(self):
        """
            This method calculates and stores Ni values based on the Ri values using the inverse of the normal distribution.
        """
        average = self.findXiValuesAverage()
        standard_deviation = self.findXiValuesSDeviation()

        for i in range(len(self.ri_values)):
            self.ni_values.append(round(norm.ppf(self.ri_values[i], loc=average, scale=standard_deviation), 5))

    def get_ri_values_array(self):
        """
            This method returns the array of Ri values.
        """
        return self.ri_values

    def get_ni_values_array(self):
        """
            This method returns the array of Ri values.
        """
        return self.ni_values




