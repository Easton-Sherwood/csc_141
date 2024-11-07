from Restaurant import Restaurant, IceCreamStand

food = Restaurant('Subway', 'Sandwiches')
food.open()
food.describe_restaurant()

food.number_served = 46
food.served()