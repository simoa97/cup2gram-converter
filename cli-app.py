# Simple application that converts food value in cups to grams

# conversion values
from database import food_list

# loop for keeping the program running
print('===== Cups to grams conventer =====')
converter_status = True
while converter_status == True:

    # name of the food and validate
    while True:
        user_input = input('Name of the food (singular): ')
        if user_input.lower() in food_list:
            break
        else:
            print(
                'Sorry, name of food you entered is not in the list,',
                  'please try entering different food.')
            continue 
    
    # number of cups and validate
    while True:
        cups_value = input('How many cups(number): ')
        try:
            val = int(cups_value)
            break
        except ValueError:
            try:
                val = float(cups_value)
                break
            except ValueError:
                print(cups_value, 'is not a number')
                continue
        
    # conversion
    if user_input.lower() in food_list:
        gram_value = float(cups_value) * food_list[user_input]
        print(
            str(cups_value) + ' cups of ' + user_input + ' is ' + 
            str(gram_value) +'g.')
    else:
        ('Wrong input')

    # continue converting?
    while True:
        convert_again = input('Convert again? (enter yes or no): ')
        if convert_again.lower() == 'no':
            converter_status = False
            break
        elif convert_again.lower() == 'yes':
            break
        else:
            continue