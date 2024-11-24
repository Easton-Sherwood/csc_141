from userpriv1 import User
from userpriv2 import Privileges, Administrator

person = Administrator('Jack', 'Smith', "11/5/1987", "5'11", "Kentucky")
person.describe_user()
person.greet_user()
person.privileges.show_privileges()