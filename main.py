"""
Sebastian repo: https://github.com/dev-par/lab6
Devan repo: https://github.com/CakeCrusher/lab_6
Name: Devan Parekh
"""


def main():
    option = 0

    print(f"""
Menu
-------------
1. Encode
2. Decode
3. Quit""")
    stored_pass = ""
    while option != "3":
        option = input("Please enter an option: ")
        if option == "1":
            passw = input("Please enter your password to encode: ")
            passw = encode(passw)
            stored_pass = passw
            print("Your password has been encoded and stored!")
        if option == "2":
            print(f"The encoded password is {stored_pass}, and the original password is {decode(stored_pass)}.")


def encode(stri):
    x = list(stri)
    res = []
    for digit in x:
        digit = int(digit) + 3
        i = str(digit)
        res.append(i)
    final = "".join(res)
    return final

def decode(stri):
    x = list(stri)
    res = []
    for digit in x:
        digit = int(digit) - 3
        i = str(digit)
        res.append(i)
    final = "".join(res)
    return final



if __name__ == "__main__":
    main()





