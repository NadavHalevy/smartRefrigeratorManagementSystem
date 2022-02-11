class SmartRefrigerator(dict):
    dictionary_refrigerator = {}
    '''
        The SmartRefrigerator object contains a dictionary groceries for a smart refrigerator.
    '''

    # init method or constructor
    def __init__(self, *args, **kwargs):
        """
        Construct a new 'SmartRefrigerator' object.
        Parameters:
            args: The args in dictionary refrigerator
            kwargs: The kwargs in dictionary refrigerator

        Returns:
            returns nothing
        """
        super().__init__(*args, **kwargs)
        self.__dict__ = self

    def check_how_many_groceries(self):
        """
        Check how many groceries in a dictionary refrigerator.
        Parameters:
             No parameters

        Returns:
            int:Returning the number of all groceries.
        """
        if len(self.dictionary_refrigerator) == 0:
            return 0
        count_list = []
        for i in self.dictionary_refrigerator:
            count_list.append(self.dictionary_refrigerator[i])
        final_number = sum(count_list)
        return final_number

    def take_groceries(self, name_of_groceries, number_of_groceries):
        """
        Check if name_of_groceries in a dictionary refrigerator,
        and if the product exists, check if the number_of_groceries can be taken from it.

        Parameters:
            name_of_groceries: The name of key in a dictionary refrigerator
            number_of_groceries: The name of value in a dictionary refrigerator

        Returns:
            returns nothing
        """
        if name_of_groceries in self.dictionary_refrigerator:
            if self.dictionary_refrigerator[name_of_groceries] > 0:
                self.dictionary_refrigerator[name_of_groceries] -= number_of_groceries
                if self.dictionary_refrigerator[name_of_groceries] < 0:
                    print("You can't take the",  name_of_groceries, "from the refrigerator")
                    self.dictionary_refrigerator[name_of_groceries] += number_of_groceries
                else:
                    print("You can't take the",  name_of_groceries, "from the refrigerator")
        else:
            print("The groceries do not exist")

    def add_existing_groceries(self, name_of_groceries, number_of_groceries):
        """
        Check if groceries in a dictionary refrigerator,
        and if the groceries exists you will add the value to it.

        Parameters:
            name_of_groceries: The name of key in a dictionary refrigerator
            number_of_groceries: The name of value in a dictionary refrigerator

        Returns:
            returns nothing
        """
        if name_of_groceries in self.dictionary_refrigerator:
            self.dictionary_refrigerator[name_of_groceries] += number_of_groceries
        else:
            print("The groceries", name_of_groceries, " do not exist")

    def add_new_groceries(self, name_of_groceries, number_of_groceries):
        """
        Add new groceries to dictionary refrigerator.
        Parameters:
            name_of_groceries: The name of key in a dictionary refrigerator
            number_of_groceries: The name of value in a dictionary refrigerator

        Returns:
            returns nothing
        """
        self.dictionary_refrigerator[name_of_groceries] = number_of_groceries

    def show_dictionary_refrigerator(self):
        """
        Prints dictionary refrigerator to the display.
        """
        print(self.dictionary_refrigerator)