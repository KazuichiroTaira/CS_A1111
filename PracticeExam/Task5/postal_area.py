class PostalArea:

    def __init__(self, area_code, number_of_people):
        self.__code = str(area_code)
        self.__people = number_of_people
        self.__positive = 0
        self.__negative = 0
        self.__dead = 0

    def get_code(self):
        return self.__code

    def get_positives(self):
        return self.__positive

    def get_negatives(self):
        return self.__negative

    def get_dead(self):
        return self.__dead

    def change_statistics(self, positive_test, negative_test, deads):
        """
        The method changes the number of positive and negative test results.
        If the given parameter is greater than zero, increase the value of
        the corresponding field. If the given parameter is less than zero,
        it reduces the value of the corresponding field for positive and
        negative test results,but does nothing for the number of dead.
        However, the number of positive or negative test results must
        never go below zero. In this case, be sure to set the number to zero.
        """

        # positives
        self.__positive += positive_test

        if self.__positive < 0:
            self.__positive = 0

        # negatives
        self.__negative += negative_test

        if self.__negative < 0:
            self.__negative = 0

        # deads
        if deads > 0:
            self.__dead += deads


    def calculate_ratio_of_sick(self):
        """
        The method returns the proportion of people living in
        the area who tested positive. The proportion is zero if
        the number of people living in the area is zero.
        """

        covid_positives = self.get_positives()
        population_of_ara = self.__people

        if population_of_ara > 0:

            ratio_of_sick = covid_positives / population_of_ara

        else:
            ratio_of_sick = 0

        return ratio_of_sick

    def compare_areas(self, other_area):
        """
        The method returns True if there are relatively more
        people in the area who have tested positive for the
        corona test in this area than in the other_area area,
        and otherwise returns False.

        Note: it can be like below...But cleaner is the one implimented
        greater = True
        first_area = self.calculate_ratio_of_sick()
        second_area = other_area.calculate_ratio_of_sick()
        if first_area < second_area:
             greater = False
        """

        greater = self.calculate_ratio_of_sick() > other_area.calculate_ratio_of_sick()

        return greater

    def __str__(self):
        # The method returns a string that looks like this:
        # area code: 02150, people: 22696, positive: 42, negative: 3496, dead: 0

        info = f"area code: {self.__code}, people: {self.__people}, positive: {self.__positive}, " \
               f"negative: {self.__negative}, dead: {self.__dead}"

        return info
