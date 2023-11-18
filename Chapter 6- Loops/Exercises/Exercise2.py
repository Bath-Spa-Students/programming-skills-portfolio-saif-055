while True:
    
    age_input = input("Please enter your age (or 'quit' to exit): ")

   
    if age_input.lower() == 'quit':
        break  

    
    try:
        age = int(age_input)
    except ValueError:
        print("Invalid input. Please enter a valid age.")
        continue 

  
    if age < 3:
        ticket_price = 0  
    elif 3 <= age <= 12:
        ticket_price = 10  
    else:
        ticket_price = 15  

 
    print(f"The cost of your movie ticket is ${ticket_price}.")
