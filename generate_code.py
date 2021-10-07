
cod_baza = "0dfz62fwtrvv"

index1 = 11

def change_value(string):
    index = 11
    string = list(string)
    while True:
        if string[index] == 'z' :
            string[index] = '1'
            #print(f'Index: {index}, new_value: {string[index]}')
            index -= 1
        elif string[index] == '9' :
            string[index] = 'a'
            #print(f'Index: {index}, new_value: {string[index]}')
            break
        else:
            string[index] = chr(ord(string[index])+1)
            #print(f'Index: {index}, new_value: {string[index]}')
            break
    string1 = ''.join(string)
    return string1

def get_codes(string, amount):
    codes = []
    for i in range(amount):
        string = change_value(string)
        codes.append(string)
    return codes

