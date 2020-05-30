from enchant import Dict
import sys
import string

dictionnary_english = Dict("en_US")

list_text = list(map(int, input().split(",")))
#list_decrypted_text = []

def base2_convertor(number):
    number = bin(number)
    list_number = [c for c in number]
    number = ""
    for i in range(2,len(list_number)):
        number += list_number[i]
    return number

def XOR(a, b):
    crypted_number = ""
    a_binar = base2_convertor(a)
    b_binar = base2_convertor(b)
    
    len_a = len(a_binar)
    len_b = len(b_binar)

    if len_a > len_b:
        while len(b_binar) != len_a:
            b_binar = "0" + b_binar
    elif len_b > len_a:
        while len(a_binar) != len_b:
            a_binar = "0" + a_binar

    for digit in range(len(a_binar)):
        if a_binar[digit] == b_binar[digit]:
            crypted_number += "0"
        else:
            crypted_number += "1"
    
    return int(crypted_number, 2)



list_alphabet_lowercase = list(string.ascii_lowercase)
list_alphabet_uppercase = list(string.ascii_uppercase)
set_alphabet_lowercase = set(list_alphabet_lowercase)
set_alphabet_uppercase = set(list_alphabet_uppercase)



for a in range(26):
    print(a, file=sys.stderr)
    for b in range(26):
        for c in range(26):
            text = ""
            code = list_alphabet_lowercase[a] + list_alphabet_lowercase[b] + list_alphabet_lowercase[c]
            for i in range(len(list_text)):
                key = code[i % 3]
                text += chr(XOR(list_text[i], ord(key)))
        

            
            print("-----------------------------------------------")
            


            new_special_index = -1

            for index in range(len(text)):

                if text[index] not in set_alphabet_lowercase and text[index] not in set_alphabet_uppercase:
                    old_special_index = new_special_index
                    new_special_index = index
                    word = text[old_special_index + 1 : new_special_index]
                    if len(word)== 0:
                        print(text[index], end = "")
                    else: 
                        if dictionnary_english.check(word):
                            print("{}{}".format(word, text[index]), end = "")
            print()
            print(code)





#key : "exp"
#solution : 129448




