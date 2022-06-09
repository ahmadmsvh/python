ref = [[ "","one","two","three","four","five","six","seven","eight","nine"],
        [ "",["ten","eleven","twelve","thirteen","fourteen",
             "fifteen","sixteen","seventeen","eighteen","ninteen"],"twenty ",
        "thirty ","fourty ","fifty ","sixty ","seventy ","eighty ","ninty "],
        [ "","one hundred ","two hundred ","three hundred ","four hundred ",
            "five hundred ","six hundred ","sevent hundred ","eight hundred ","nine hundred "]]


number = int(input("enter a number:\t"))

number_reverse = [0,0,0]
number_literal = ""

quotient = number

i = 0
while quotient > 0 :
    digit = quotient % 10 
    quotient //= 10
    number_reverse[i] = digit
    i += 1
    
if number_reverse[1] != 1 :
    number_literal = ref[2][number_reverse[2]] + ref[1][number_reverse[1]] + ref[0][number_reverse[0]]
    
if number_reverse[1] == 1 :
    number_literal = ref[2][number_reverse[2]] + ref[1][1][number_reverse[0]]

print(number_literal)