🔐 Cipher Implementations

This project implements two classical cryptographic techniques:

Substitution Cipher (Caesar Cipher)

Transposition Cipher (Rail Fence – 2 Rails)

1️⃣ Substitution Cipher (Caesar Cipher)
📌 Description

The substitution cipher replaces each character in the plaintext with another character by shifting it using a numeric key.
The same logic is used for encryption and decryption.

⚙️ Implementation Steps

Take the input text from the user.

Take a numeric key from the user.

Traverse each character of the input text one by one.

Check the character type:

If it is a lowercase letter (a–z), shift it within the lowercase range.

If it is an uppercase letter (A–Z), shift it within the uppercase range.

If it is a digit (0–9), shift it within the digit range.

Use modulo operation to handle wrap-around (e.g., z → a).

Append the shifted character to the result.

If the character is not alphanumeric, keep it unchanged.

Display the final encrypted or decrypted output.

For decryption, use the negative value of the key.

🔁 Encryption & Decryption Rule

Encryption → shift using + key

Decryption → shift using - key

2️⃣ Transposition Cipher (Rail Fence Cipher – 2 Rails)
📌 Description

The transposition cipher rearranges the position of characters without changing them.
In the 2-rail rail fence cipher, characters are written alternately on two rows and read row-by-row.

⚙️ Implementation Steps (Encryption)

Take the input text from the user.

Remove all spaces from the text.

Initialize two empty strings:

top_rail

bottom_rail

Use a flag variable to alternate between rails.

Traverse each character in the text:

If flag is 0, add character to the top rail.

Else, add character to the bottom rail.

Toggle the flag after each character.

Concatenate top_rail + bottom_rail.

Display the ciphertext.

⚙️ Implementation Steps (Decryption)

Take the ciphertext as input.

Find the midpoint of the text.

Split the ciphertext into:

First half → top rail

Second half → bottom rail

Reconstruct the plaintext by alternately taking characters from:

top rail

bottom rail

Append any remaining character if text length is odd.

Display the decrypted plaintext.

📝 Summary
Cipher Type	Technique Used	Key Type
Substitution	Character shifting	Numeric key
Transposition	Character rearrangement	Fixed rail pattern

These implementations are simple, terminal-based, and suitable for academic and lab use.

If you want this in shorter form or formatted exactly for GitHub, I can refine it 👍