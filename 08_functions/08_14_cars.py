def car_profile(manufacturer, model, **user_info):
   user_info['manufacturer'] = manufacturer
   user_info['model'] = model
   return user_info

vehicle_profile = car_profile('Ford', 'F-250',
                             color='Silver',
                             miles='137624',
                             package='Off Road')

print(vehicle_profile)