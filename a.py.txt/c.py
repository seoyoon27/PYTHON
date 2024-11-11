if __name__ == '__main__':
    age = 5

    if age < 10:
        print("cậu", end=" ")
        # print rat 10 times using for
        for i in range(10):
            print("rất",end=" ")
        print(" là sửu nghé")



    elif age < 18:
        print("cậu là trẩu tre")
        if age >= 15 and age <= 18:
            print("cậu là chiu nhăn")
    if age == 24:
            print("cậu là ngừ eo của chớ >3")

    else:
        print("cậu là chục chức của chớ")
