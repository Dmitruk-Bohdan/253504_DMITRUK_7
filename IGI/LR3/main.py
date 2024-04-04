import row, loop_service, string_handler, text_parser, floats_list_handler


while True:
    func_number = input("""
                        
Please enter the command number
Command's set:
    1. Calculate  cos(x) row
    2. Loop function
    3. String handler function
    4. Text parsing function
    5. Floats list handling function
""")
    
    if(func_number == '1'):
        print("\nTask №1 is running\n")
        row.executable_function()

    elif(func_number == '2'):
        print("\nTask №2 is running\n")
        loop_service.executable_function()
    
    elif(func_number == '3'):
        print("\nTask №3 is running\n")
        string_handler.executable_function()

    elif(func_number == '4'):    
        print("\nTask №4 is running\n")
        text_parser.executable_function()

    elif(func_number == '5'):
        print("\nTask №5 is running\n")
        floats_list_handler.executable_function()

    else:
        print("Incorrect input!\nPlease, try again\n")
