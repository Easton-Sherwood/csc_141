def build_profile(first, last, **user_info):
   user_info['first_name'] = first
   user_info['last_name'] = last
   return user_info

user_profile_Easton = build_profile('Easton', 'Sherwood',
                             location='Albright College',
                             field='Computer Science',
                             hobby='Painting' )

print(user_profile_Easton)