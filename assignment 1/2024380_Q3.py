def ones(number):
    if number == 0:
         return "zero"
    elif number == 1: 
        return "one"
    elif number == 2: 
        return "two"
    elif number == 3: 
        return "three"
    elif number == 4: 
        return "four"
    elif number == 5: 
        return "five"
    elif number == 6: 
        return "six"
    elif number == 7: 
        return "seven"
    elif number == 8: 
        return "eight"
    elif number == 9: 
        return "nine"

def unique(number):
    if number == 10: 
        return "ten"
    elif number == 11: 
        return "eleven"
    elif number == 12: 
        return "twelve"
    elif number == 13: 
        return "thirteen"
    elif number == 14: 
        return "fourteen"
    elif number == 15: 
        return "fifteen"
    elif number == 16: 
        return "sixteen"
    elif number == 17: 
        return "seventeen"
    elif number == 18: 
        return "eighteen"
    elif number == 19: 
        return "nineteen"

def tens(number):
    if number == 20: 
        return "twenty"
    elif number == 30: 
        return "thirty"
    elif number == 40: 
        return "forty"
    elif number == 50: 
        return "fifty"
    elif number == 60: 
        return "sixty"
    elif number == 70: 
        return "seventy"
    elif number == 80: 
        return "eighty"
    elif number == 90: 
        return "ninety"

def twos(number):
    if number < 10:
        return ones(number)
    elif number < 20:
        return unique(number)
    else:
        if number % 10 != 0:
            return str(tens(number // 10 * 10)) + " " + str(ones(number % 10)) #added string as it was giving me some unknown error.
        else:
            return tens(number)

def threes(number):
    if number < 100:
        return twos(number)
    else:
        if number % 100 != 0:
            return str(ones(number // 100)) + " hundred" + "  " + str(twos(number % 100))
        else:
            return str(ones(number // 100)) + " hundred"

def number_to_words(number):
    if number == 0:
        return "zero"
    
    crores = number // 10000000
    lakhs = (number // 100000) % 100
    thousands = (number // 1000) % 100
    hundreds = (number // 100) % 10
    remainder = number % 100

    result = ""
    if crores > 0:
        result += str(threes(crores)) + " crore"
    if lakhs > 0:
        if result:
            result += " " + str(twos(lakhs)) + " lakh"
        else:
            result += str(twos(lakhs)) + " lakh" 
    if thousands > 0:
        if result:
            result += " " + str(twos(thousands)) + " thousand"
        else:
            result += str(twos(thousands)) + " thousand"
    if hundreds > 0:
        if result:
            result += " " + str(ones(hundreds)) + " hundred"   
        else:
            result += str(ones(hundreds)) + " hundred"
    if remainder > 0:
        if result:
            result += " " + str(twos(remainder))
        else:
            result += str(twos(remainder))

    return result

def test():
    assert number_to_words(0) == "zero"
    assert number_to_words(1) == "one"
    assert number_to_words(10) == "ten"
    assert number_to_words(11036) == "eleven thousand thirty six"
test()

x = int(input("Enter a number up to 100 crore: "))
print(number_to_words(x))