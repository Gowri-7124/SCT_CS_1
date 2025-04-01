letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num_letters = len (letters)

def encrypt(plaintext,key):
  ciphertext =''
  for letter in plaintext:
    letter = letter.uppert()
    if not letter == ' ':
      index= letters.find(letter)
      if index == -1:
        ciphertext += letter
      else:
        new_index = index+key
        if new_index >= 26:
          newindex-=26
        ciphertext+=letters[new_index]
  return ciphertext

def decrypt(ciphertext,key):
  plaintext =''
  for letter in ciphertext:
    letter = letter.upper()
    if not letter == ' ':
      index= letters.find(letter)
      if index == -1:
        plaintext += letter
      else:
        new_index = index-key
        if new_index < 0:
          newindex+=num_letters
        plaintext+=letters[new_index]
  return plaintext

print()
print('***CEASER CIPER PROGRAM***')
print()
print('DO YOU WANT TO ENCRYPT OR DECRYPT?')
user_input= input('E/D:').upper()
print()
if user_input  == 'E':
  print('Encryption Mode Selected')
  print()
  key = int(input('Enter the key (1 through 26):'))
  text = input('Enter the text to encrypt:')
  ciphertext=encrypt(text,key)
  print(f'CIPERTEXT:{ciphertext}')
elif user_input == 'D':
  print('Decryption Mode Selected')
  print()
  key = int(input('Enter the key (1 through 26):'))
  text = input('Enter the text to decrypt:')
  plaintext = decrypt(text,key)
  print(f'PLAINTEXT:{plaintext}')
     


