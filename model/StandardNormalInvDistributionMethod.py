import numpy as np
from scipy.stats import norm

class StandardNormalInvDistributionMethod:
    """
        This class implements the Standard Normal Inverse Distribution Method for generating pseudo-random numbers.
    """

    def __init__(self, num_amount_ri, num_amount_range):
        """
            This is the constructor method for the StandardNormalInvDistributionMethod class.
            It initializes the class with the given parameters.
        """
        self.num_amount_ri = num_amount_ri  # Number of Ri values to generate
        self.num_amount_range = num_amount_range  # Number of range values
        self.ri_values = []  # List to hold Ri values
        self.ni_values = []  # List to hold Ni values
        self.intervals_values = []  # List to hold interval values
        self.frequencies_values = []  # List to hold frequency values

    def fillRiValues(self):
        """
            This method generates and stores Ri values using a uniform distribution.
        """
        for i in range(self.num_amount_ri):
            random_number = np.random.uniform()
            self.ri_values.append(round(random_number, 5))

    def fillNiValues(self):
        """
            This method calculates and stores Ni values based on the Ri values using the inverse of the standard normal distribution.
        """
        for i in range(len(self.ri_values)):
            value = norm.ppf(self.ri_values[i])
            self.ni_values.append(value)

    def obtainMinNiValue(self):
        return min(self.ni_values)

    def obtainMaxNiValue(self):
        return max(self.ni_values)

    def fillIntervalsValues(self):
        min_value = self.obtainMinNiValue()
        max_value = self.obtainMaxNiValue()
        self.intervals_values.append(min_value)

        if self.num_amount_range > 1:
            step = (max_value - min_value) / (self.num_amount_range - 1)
            for i in range(1, self.num_amount_range + 1):
                value = self.intervals_values[i - 1] + step
                self.intervals_values.append(value)

    def fillFrequenciesValues(self):
        self.intervals_values.sort()
        counter = 0

        for i in range(len(self.intervals_values) - 1):
            for j in range(len(self.ni_values)):
                if (self.ni_values[j] >= self.intervals_values[i]) and (
                        self.ni_values[j] < self.intervals_values[i + 1]):
                    counter += 1
            self.frequencies_values.append(counter)
            counter = 0

    def cumulativeFrequencies(self):
        return sum(self.frequencies_values)

    def obtainIntervalsArray(self):
        return self.intervals_values

    def obtainFrequenciesArray(self):
        return self.frequencies_values

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


