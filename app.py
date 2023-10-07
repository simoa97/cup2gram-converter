# Simple application that converts food value in cups to grams

# list of food, key is name, value is 1 cup in grams
food = {
    'flour':120,
    'carrot':122,
    'brocolli':175,
    'onion':52,
    'sugar':200,
    'powdered sugar':120,
    'butter':227,
    'rice':200,
    'oats':85,
    'almonds':145,
    'canned tomatoes':225,
    'yogurt':227,
    'celery':100,
    'cheddar':235,
    'bluberries':155,
    'mozzarella':113,
    'zucchini':130,
    'olives':142,
    'cranberries':105
}

# loop for keeping the program running
print('===== Cups to grams conventer =====')
converter_status = True
while converter_status == True:

    # name of the food and validate
    while True:
        user_input = input('Name of the food (singular): ')
        if user_input.lower() in food:
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
    if user_input.lower() in food:
        gram_value = float(cups_value) * food[user_input]
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