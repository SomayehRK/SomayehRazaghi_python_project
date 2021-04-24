from Users import Users
from login import login

print('                                                                                           ')
print('************************ welcome to our store *********************************************')
print('********************** enjoy from your purchase *******************************************')
print('                                                                                           ')
print('                                                                                           ')

select = int(input('1 - create an account | 2 - login :'))
if select == 1:
    user = Users.set_object()
    Users.create_account(user)
elif select == 2:
    acc_level = int(input('1 - admin | 2 - customer :'))
    if acc_level == 1:
        login('Admin_info_2.csv')
    elif acc_level == 2:
        login('Customer_info_2.csv')



