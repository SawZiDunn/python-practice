def main4():
    a = ["How", "are", "you?"]
    print(a)
    
    x = "*".join(a)
    print(x)

def string_reverse_recursive(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse_recursive(str[1:]) + str[0]
    # return str[::-1]



print(string_reverse_recursive("Hello World"))
main4()
