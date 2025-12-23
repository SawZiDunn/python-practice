def format(number, width):
    x = len(number)
    result = ""
    if x >= width:
        return number
    
    result += "0" * (width - x)
    return result + number

x = input("Enter an integer: ")
width = int(input("Enter width: "))
print("The formatted number is", format(x, width))