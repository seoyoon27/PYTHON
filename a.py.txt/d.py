if __name__ == '__main__':
#     age = 11
#     la_con_nit = False
#
#     if age < 10:
#         la_con_nit = True
#     if la_con_nit:
#         print("con nit")
#     elif age<18:
#         print("trau tre")
#     else:
#         print("nguoi lon")

    gender_input = input("Are you male (yes/no):")
    is_male = None
    height_feet = input("Are you feet?")

    if gender_input == 'yes' or gender_input == 'y' or gender_input == 'Yes' or gender_input == 'YES':
        is_male = True
    elif gender_input == 'no' or gender_input == 'n' or gender_input == 'No' or gender_input == 'NO':
        is_male = False
    else:
        is_male = None
    if is_male == None:
        print("Invalid Answer")
    elif is_male == True:
            if height_feet > 6.5:
                print("you are very tall as a man")
            elif height_feet > 6.0:
                print("you are tall as a man")
            else:
                print("you are short as a man")
    elif is_male == False:
            if height_feet > 5.7:
                print("you are tall as a girl")
            else:
                print("you are short as a girl")
    else:
        print("system error:Variable'is_male' is not correct")