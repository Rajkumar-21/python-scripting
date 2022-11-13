import startup_font
print(startup_font.cipher)
print(startup_font.Author)
alphabet= ['a','b','c','d','e','f','g','h','i','j',
'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j',
'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input('Enter "encode" to Encrypt the plain_text or enter "decode" to Decrypt the encoded text: ')
text = input("Enter the text: ").lower()
shift= int(input("Enter the shift value: "))

def encrypt(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position+shift_amount
        cipher_text += alphabet[new_position]
    print(f"Ecrypted text is {cipher_text}")

def decrypt(cipher_text,shift_amount):
    plain_text=""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position-shift_amount
        plain_text += alphabet[new_position]
    print(f"Decrypted text is {plain_text}")

if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
  decrypt(cipher_text=text, shift_amount=shift ) 