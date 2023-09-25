def main():
    # query the user for encryption or decryption
    print("Enter 'E' for Encryption, or 'D' for Decryption: ")
    mode = input().upper()

    # confirm a correct mode is chosen, and alert the user
    if mode != 'E' and mode != 'D':
        print("Incorrect value entered, please try again.")
        exit()

    # get the message from the user
    if mode == 'E':
        print("Enter the message to be encrypted:")
    else:
        print("Enter the message to be decrypted:")
    raw_message = input()
    message = []
    for ch in raw_message:
        message.append(ord(ch))

    # get the key from the user
    print("Enter shift key:")
    key = int(input())

    # encrypt/decrypt the message with the provided key
    if mode == 'E':
        raw_message = caesar_encrypt(message, key)
        print("Your encrypted message:", raw_message)
    else:
        raw_message = caesar_decrypt(message, key)
        print("Your decrypted message:", raw_message)

def caesar_encrypt(msg, key):
    encrypted_msg = [] # character list of the encrypted message
    for ch in msg:
        if chr(ch).isalpha(): # check to see if the character is a letter
            lowercase = chr(ch).islower() # check to see if this character is lowercase (changes ascii ranges)
            if lowercase:
                ch += key # encrypt
                while ch > ord('z'): # make sure the character is in the bounds of the alphabet
                    ch -= 26
                encrypted_msg.append(chr(ch)) # append the encrypted character to the encrypted list
            else: # same thing but for uppercase ASCII characters
                ch+=key
                while ch > ord('Z'):
                    ch -= 26
                encrypted_msg.append(chr(ch))
        else: #otherwise, don't change it
            encrypted_msg.append(chr(ch))
    encryption = "".join(encrypted_msg) # create a string from the encrypted list
    return encryption # Voilà 

def caesar_decrypt(msg, key): # basically identical documentation for the encryption function, except the key is subtracted from the encrypted message instead of added
    decrypted_msg = []
    for ch in msg:
        if chr(ch).isalpha():
            lowercase = chr(ch).islower()
            if lowercase:
                ch -= key
                while ch < ord('a'):
                    ch += 26
                decrypted_msg.append(chr(ch))
            else:
                ch -= key
                while ch < ord('A'):
                    ch += 26
                decrypted_msg.append(chr(ch))
        else:
            decrypted_msg.append(chr(ch))
    decryption = "".join(decrypted_msg)
    return decryption

if __name__ == "__main__":
    main()