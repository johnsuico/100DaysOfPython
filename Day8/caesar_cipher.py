alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def caesar(direction, text, shift):
    result = ""
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if direction == "encode":
                result += alphabet[(index + shift) % 26]
            elif direction == "decode":
                result += alphabet[(index - shift) % 26]
        else:
            result += letter
    
    print(f"The {direction}d text is: {result}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

if direction == "encode" or direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)

if direction != "encode" and direction != "decode" :
    print("You did not enter in a correct option.")