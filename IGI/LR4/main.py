from gto_handler import GTOHandler
from text_handler import TextHandler
from row_handler import RowHandler
import geometric_shapes
from numpy_handler import NumpyHandler


while True:
    func_number = input("""
                        
Please enter the command number
Command's set:
    1. GTOHandeler demonstration
    2. TextHandeler demonstration 
    3. RowHandler demonstration
    4. Geometric shapes classes demonstration
    5. NumpyHandler demonstration
""")
    
    if(func_number == '1'):
        print("\nTask №1 is running\n")
        GTOHandler.demonstrate()

    elif(func_number == '2'):
        print("\nTask №2 is running\n")
        TextHandler.demonstrate()
    
    elif(func_number == '3'):
        print("\nTask №3 is running\n")
        RowHandler.demonstrate()

    elif(func_number == '4'):    
        print("\nTask №4 is running\n")
        geometric_shapes.demonstrate()

    elif(func_number == '5'):
        print("\nTask №5 is running\n")
        NumpyHandler.demonstrate()

    else:
        print("Incorrect input!\nPlease, try again\n")