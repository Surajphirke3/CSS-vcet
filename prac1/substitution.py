def cipher(text, key):
    result = ""

    for ch in text:
        if 'a' <= ch <= 'z':
            result += chr((ord(ch) - 97 + key) % 26 + 97)

        elif 'A' <= ch <= 'Z':
            result += chr((ord(ch) - 65 + key) % 26 + 65)

        elif '0' <= ch <= '9':
            result += chr((ord(ch) - 48 + key) % 10 + 48)

        else:
            result += ch

    return result


text = input("Enter text: ") 

key = int(input("Enter key : "))

output = cipher(text, key)

print("Result is :", output)
