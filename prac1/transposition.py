choice = input("Enter E for Encrypt or D for Decrypt: ").upper()
text = input("Enter text: ")
text = text.replace(" ", "")   # remove spaces
if choice == "E":
    top = ""
    bottom = ""
    flag = 0
    for ch in text:
        if flag == 0:
            top += ch
            flag = 1
        else:
            bottom += ch
            flag = 0
    print("Ciphertext:", top + bottom)
elif choice == "D":
    half = (len(text) + 1) // 2
    top = text[:half]
    bottom = text[half:]
    result = ""
    i = 0
    while i < len(bottom):
        result += top[i]
        result += bottom[i]
        i += 1
    if len(top) > len(bottom):
        result += top[-1]
    print("Plaintext:", result)
else:
    print("Invalid choice")
