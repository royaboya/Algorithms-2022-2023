morse_code = {"a": "*-", "c": "-*-*", "e": "*", "t": "-", " ": " "}


def main():
    english = input("What would you like to convert to Morse code? ")
    encoded = ""
    for ch in english:
        if ch not in morse_code:
            new_code = input("What is Morse code for " + ch + "?")
            # Add the new key-value pair to the dictionary.
            morse_code[ch] = new_code
        # Write a statement to add to encoded.
        encoded += morse_code[ch] + " "
    print("Morse code for " + english + " is " + encoded)


if __name__ == "__main__":
    main()
