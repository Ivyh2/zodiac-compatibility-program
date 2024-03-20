"""
author: Ivy Huang
Compares the birthdays of two people to determine whether or not they 
are compatible based on their zodiac sign
"""

##Functions

def get_birthday():
    """Asks for the user's birthday and returns the month and day
    
    Returns:
        int: The month as a number 
        int: The day as a number 
    """
    
    try:
        month = int(input("Enter your birth month, as a number: "))
        while month < 1 or month > 12:
            print("You must enter a valid month!")
            month = int(input("Enter your birth month, as a number: "))
            
    except ValueError:
        print("You must enter a number!")
        month = int(input("Enter your birth month, as a number: "))
            
    try:
        day = int(input("Enter the day of your birthday: "))
        while day < 1 or day > 31:
            print("You must enter a valid day!")
            day = int(input("Enter the day of your birthday: "))
            
#Checks if the user entered a valid day according to the specific month
        while (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
            print("You must enter a valid day!")
            day = int(input("Enter the day of your birthday: "))
        while month == 2 and day > 29:
            print("You must enter a valid day!")
            day = int(input("Enter the day of your birthday: "))
            
    except ValueError:
        print("You must enter a number!")
        day = int(input("Enter the day of your birthday: "))
    
    return month, day
    
def get_zodiac_sign(month, day):
    """Gets the zodiac sign of the user according to their birthday
    
    Args:
        month(int): The month of the birthday
        day(int): The day of the birthday
    
    Returns:
        str: The zodiac sign according to the birthday
    """
    
    sign = ""
    ##Jan
    if (month == 1):
        if (day < 20):
            sign = "Capricorn"
        else:
            sign = "Aquarius"
    ##Feb
    if (month == 2):
        if (day < 19):
            sign = "Aquarius"
        else:
            sign = "Pisces"
    ##Mar
    if (month == 3):
        if (day < 21):
            sign = "Pisces"
        else:
            sign = "Aries"
    ##Apr
    if (month == 4):
        if (day < 20):
            sign = "Aries"
        else:
            sign = "Taurus"
    ##May
    if (month == 5):
        if (day < 21):
            sign = "Taurus"
        else:
            sign = "Gemini"
    ##Jun
    if (month == 6):
        if (day < 21):
            sign = "Gemini"
        else:
            sign = "Cancer"
    ##Jul
    if (month == 7):
        if (day < 23):
            sign = "Cancer"
        else:
            sign = "Leo"
    ##Aug
    if (month == 8):
        if (day < 23):
            sign = "Leo"
        else:
            sign = "Virgo"
    ##Sep
    if (month == 9):
        if (day < 23):
            sign = "Virgo"
        else:
            sign = "Libra"
    ##Oct
    if (month == 10):
        if (day < 23):
            sign = "Libra"
        else:
            sign = "Scorpio"
    ##Nov
    if (month == 11):
        if (day < 22):
            sign = "Scorpio"
        else:
            sign = "Sagittarius"
    ##Dec
    if (month == 12):
        if (day < 22):
            sign = "Sagittarius"
        else:
            sign = "Capricorn"
    
    return sign


def elemental_compatibility(element):
    """Checks whether or not the two zodiac signs are compatible based on their element
    
    Loops through each element list (fire, air, water, earth) and checks if
    both zodiac signs have the same element. Prints the result.
    
    Args:
        element(str): The element being checked
    """
    compatibility_1 = False
    compatibility_2 = False
    for i in element:
        if i == zodiac_sign:
            compatibility_1 = True
    for i in element:
        if i == zodiac_sign_2:
            compatibility_2 = True
    if compatibility_1 == True and compatibility_2 == True:
        print(zodiac_sign, "and", zodiac_sign_2, "are compatible by element.")
    
    elif (compatibility_1 == True and compatibility_2 == False):
        print(zodiac_sign, "and", zodiac_sign_2, "are incompatible by element.")


def power_couple(power_1, power_2):
    """Checks if the two zodiac signs are a power couple
    
    Args:
        power_1(str): The first zodiac sign which forms a power couple
        power_2(str): The second zodiac sign which forms a power couple
    """
    if (zodiac_sign == power_1 and zodiac_sign_2 == power_2) or (zodiac_sign == power_2 and zodiac_sign_2 == power_1):
        print(zodiac_sign, "and", zodiac_sign_2, "are a power couple!")
    
    
def danger_couple(danger_1, danger_2):
    """Checks if the two zodiac signs are a dangerous match
    
    Args:
        danger_1(str): The first zodiac sign which forms a dangerous match
        danger_2(str): The second zodiac sign which forms a dangerous match
    """
    if (zodiac_sign == danger_1 and zodiac_sign_2 == danger_2) or (zodiac_sign == danger_2 and zodiac_sign_2 == danger_1):
        print(zodiac_sign, "and", zodiac_sign_2, "are a dangerous match!")

##MAIN

#Asks the user to input the two people's birthdays
birth_month, birth_day = get_birthday()
print("")
birth_month_2, birth_day_2 = get_birthday()
print("")

#Prints the two zodiac signs
zodiac_sign = get_zodiac_sign(birth_month, birth_day)
zodiac_sign_2 = get_zodiac_sign(birth_month_2, birth_day_2)

print("Your sign is " + zodiac_sign + ".")
print("Your partner's zodiac sign is " + zodiac_sign_2 + ".")

##Compatibility by elements
#Groups the zodiac signs in lists by their corresponding element
fire = ["Aries", "Leo", "Sagittarius"]
earth = ["Taurus", "Virgo", "Capricorn"]
air = ["Gemini", "Libra", "Aquarius"]
water = ["Cancer", "Scorpio", "Pisces"]

elemental_compatibility(fire)
elemental_compatibility(air)
elemental_compatibility(water)
elemental_compatibility(earth)

##Complex compatibility
power_couple("Taurus", "Cancer")
power_couple("Gemini", "Aries")
power_couple("Leo", "Leo")
power_couple("Virgo", "Virgo")
power_couple("Libra", "Capricorn")
power_couple("Scorpio", "Sagittarius")
power_couple("Aquarius", "Pisces")

danger_couple("Aries", "Cancer")
danger_couple("Taurus", "Leo")
danger_couple("Cancer", "Aquarius")
danger_couple("Leo", "Capricorn")
danger_couple("Virgo", "Sagittarius")
danger_couple("Libra", "Virgo")
danger_couple("Scorpio", "Libra")
danger_couple("Pisces", "Pisces")
