def main():
    option = 0

    print(f"""
Menu
-------------
1. Encode
2. Decode
3. Quit""")
    while option != "3":
        option = input("Please enter an option: ")
        passw = input("Please enter your password to encode: ")
        if option == "1":
            passw = encode(passw)
            print("Your password has been encoded and stored!")


def encode(stri):
    x = list(stri)
    res = []
    for digit in x:
        digit = int(digit) + 3
        i = str(digit)
        res.append(i)
    final = "".join(res)
    return final



if __name__ == "__main__":
    main()





