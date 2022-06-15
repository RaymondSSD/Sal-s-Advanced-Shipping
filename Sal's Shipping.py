#This program calculates the costs of shipping for items based on weight and shipping method.


#Regular Shipping
def regular_shipping():
    while True:
        try:
            item_weight = float(input('Please enter item weight in pounds'))
            if item_weight > 0:
                break
            else:
                print('Please use positive numbers!')
        except ValueError:
            print('''This isn't even any kind of number! :O''')
    if item_weight > 0 and item_weight <= 2:
        print('$' + str(item_weight * 1.50 + 20))
    elif item_weight >2 and item_weight <= 6:
        print('$' + str(item_weight * 3 + 20))
    elif item_weight >6 and item_weight <10:
        print('$' + str(item_weight * 4 + 20))
    elif item_weight >=10:
        print('$' + str(item_weight * 4.75 + 20))
    

#Premium Ground Shipping
premium_shipping = '$125'

#Drone Shipping
def drone_shipping():
    while True:
        try:
            item_weight = float(input('Please enter item weight in pounds'))
            if item_weight > 0:
                break
            else:
                print('Please use positive numbers!')
        except ValueError:
            print('''This isn't even any kind of number! :O''')
    if item_weight > 0 and item_weight <= 2:
        print('$' + str(item_weight * 4.50))
    elif item_weight >2 and item_weight <= 6:
        print('$' + str(item_weight * 9))
    elif item_weight >6 and item_weight <10:
        print('$' + str(item_weight * 12))
    elif item_weight >=10:
        print('$' + str(item_weight * 14.25))

#Shipping method
def shipping_method():
    while True:
        try:
            question = input('Would you like to use regular, premium, or drone shipping?')
            if question == 'regular':
                break
            elif question == 'premium':
                break
            elif question == 'drone':
                break
            else:
                print('Input 1 of these 3 words to continue: regular, premium, drone')
        except ValueError:
            int
    if question == 'regular':
        regular_shipping()
    elif question == 'premium':
        print(premium_shipping)
    elif question == 'drone':
        drone_shipping()
shipping_method()