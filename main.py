from SmartRefrigerator import *
'''
    Testing SmartRefrigerator object
'''

if __name__ == '__main__':
    check_dict = SmartRefrigerator()
    check_dict.show_dictionary_refrigerator()
    print("In the refrigerator, we have: ", check_dict.check_how_many_groceries(), " groceries")
    check_dict.add_new_groceries("Bananas", 10)
    check_dict.add_new_groceries("Apples", 9)
    check_dict.add_new_groceries("Slices of bread", 20)
    check_dict.add_existing_groceries("Eggs", 12)
    check_dict.add_existing_groceries("Slices of bread", 7)
    print("In the refrigerator, we have:")
    check_dict.show_dictionary_refrigerator()
    check_dict.take_groceries("Slices of bread", 20)
    print("In the refrigerator, we have:")
    check_dict.show_dictionary_refrigerator()
    check_dict.take_groceries("Slices of bread", 20)
    print("In the refrigerator, we have:")
    check_dict.show_dictionary_refrigerator()
    print("In the refrigerator, we have: ", check_dict.check_how_many_groceries(), "groceries")
