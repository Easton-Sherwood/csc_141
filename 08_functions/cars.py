def car_profile(manufacturer, model, **user_info):
   user_info['manufacturer'] = manufacturer
   user_info['model'] = model
   return user_info