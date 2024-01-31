numeral, num = input().split()

num = int(num)

def number_to_numeral(number):
    alpha = {
        "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000
    }
    alphanum = [
        "I", "V", "X", "L", "C", "D", "M"
    ]
    string = ""
    alphaind = 6
    count = 0
    while number > 0:
        if number < alpha[alphanum[alphaind]]:
            alphaind -= 1
            count = 0
            continue
        number -= alpha[alphanum[alphaind]]
        string += alphanum[alphaind]
        count += 1
        if count > 3:
            if alphanum[alphaind] == "I":
                string = string[:-4]
                if len(string) > 0:
                    if string[-1] == "V":
                        string = string[:-1]
                        string += "IX"
                    else:
                        string += "IV"
                else:
                    string += "IV"
            if alphanum[alphaind] == "X":
                string = string[:-4]
                if len(string) > 0:
                    if string[-1] == "L":
                        string = string[:-1]
                        string += "XC"
                    else:
                        string += "XL"
                else:
                    string += "XL"
            if alphanum[alphaind] == "C":
                string = string[:-4]
                if len(string) > 0:
                    if string[-1] == "D":
                        string = string[:-1]
                        string += "CM"
                    else:
                        string += "CD"
                else:
                    string += "CD"

    return string

def numeral_to_lookandsay(numeral):
    string = ""
    lastNum = ""
    count = 0
    for i in numeral:
        if not lastNum:
            lastNum = i
            count = 1
            continue
        if i == lastNum:
            count += 1
        else:
            string += number_to_numeral(count)
            string += lastNum
            count = 1
            lastNum = i

    string += number_to_numeral(count)
    string += lastNum
    return string

# print(number_to_numeral(num))

for i in range(num):
    numeral = numeral_to_lookandsay(numeral)

print(numeral.count("I"), numeral.count("V"))
