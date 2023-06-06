# Select the Functionality
En = input("Encryption(E)/ Decryption(D): ")


# Algorithm
def algorithm(combined, asc):
    # Conversion of Simple Letters
    if 97 <= asc <= 122:
        combined -= 97
        asc_rem = (combined % 26) + 97

    # Conversion of Capital Letters
    elif 65 <= asc <= 90:
        combined -= 65
        asc_rem = (combined % 26) + 65

    # Conversion of Numbers
    elif 48 <= asc <= 57:
        combined -= 48
        asc_rem = (combined % 10) + 48

    # Other Characters (will not be ciphered)
    else:
        asc_rem = asc

    return chr(asc_rem)


def main():
    result = ""

    # Encryption Process
    if 'e' == str.lower(En):
        txt = input("Enter the plain text: ")
        key = input("Enter the key: ")
        for t in txt:
            combined = ord(t) + int(key)
            result += algorithm(combined, ord(t))

    # Decryption Process
    elif 'd' == str.lower(En):
        txt = input("Enter the cipher text: ")
        key = input("Enter the key: ")

        for t in txt:
            combined = ord(t) - int(key)
            result += algorithm(combined, ord(t))

    # Input Validation
    else:
        print("Invalid Input!")

    return result


print(main())
