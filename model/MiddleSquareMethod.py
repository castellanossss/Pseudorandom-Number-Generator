class MiddleSquareMethod:
    """
        This class implements the Middle Square Method for generating pseudo-random numbers.
    """

    def __init__(self, seed, min, max, numAmount):
        """
            This is the constructor method for the MiddleSquareMethod class.
            It initializes the class with the given parameters.
        """
        self.seed = seed  # Initial seed value
        self.niValues = []  # List to hold Ni values
        self.riValues = []  # List to hold Ri values
        self.xiValues = []  # List to hold Xi values
        self.centers = []  # List to hold center values
        self.min = min  # Minimum value for Ni
        self.max = max  # Maximum value for Ni
        self.numAmount = numAmount  # Number of random numbers to generate

    def generateRandoms(self):
        """
            This method generates the pseudorandom numbers using the middle square method.
        """
        seed = self.seed
        len_seed = len(str(self.seed))
        for i in range(self.numAmount):
            self.xiValues.append(seed)
            xi2 = seed * seed
            center = self.getCenter(str(xi2))
            self.centers.append(center)
            ri = center / self.getDivNum(len_seed)
            self.riValues.append(ri)
            ni = self.genNiNumber(ri)
            self.niValues.append(ni)
            seed = center

    def genNiNumber(self, ri):
        """
            This method generates a Ni value from a given Ri value.
        """
        return self.min + ((self.max - self.min) * ri)

    def getCenter(self, num):
        """
            This method extracts the center digits from a given number.
        """
        len_seed = len(str(self.seed))
        len_num = len(str(num))
        padded = ""

        if len_num == (len_seed * 2):
            padded = num
        elif len(num) < len_seed * 2:
            while len(padded) < len_seed * 2 - len_num:
                padded = "0" + padded
            padded += num

        startIndex = int(len_seed / 2)
        endIndex = startIndex + len_seed
        center = padded[startIndex:endIndex]

        return int(center)

    def getDivNum(self, length):
        """
            This method generates a divisor number based on the length of the seed.
            It is used to calculate the Ri values.
        """
        num = ""
        for i in range(length):
            num += "0"
        num = "1" + num
        return float(num)

    def get_xi_values_array(self):
        """
            This method returns the array of Xi values.
        """
        return self.xiValues

    def get_ri_values_array(self):
        """
            This method returns the array of Ri values.
        """
        return self.riValues

    def get_ni_values_array(self):
        """
            This method returns the array of Ni values.
        """
        return self.niValues
