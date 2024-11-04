if __name__ == '__main__':
    CURRENT_YEAR = 2024
    METTER_TO_FEET = 3.281

    firstname = input("your firstname:")
    lastname = input("Your lastname:")
    year_born= int(input("when you were born:"))
    height_metter = input("Your height (metter):")

    Age = CURRENT_YEAR - year_born
    height_metter = float(height_metter)
    height_feet = height_metter * METTER_TO_FEET
    height_feet = round(height_feet,1)

    print("\n---")
    print("Your name is " + firstname + " " + lastname )
    print("You are" + " " +  str(height_feet) + " " + "feet tall")
    print("You are {0} year old in {1}".format(Age,CURRENT_YEAR))
