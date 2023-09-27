# This is a program that can encrypt or decrypt messages
# of a Vigenère cipher when given the correct keyword.
def main():
    print("Enter 'E' for encryption, or 'D' for decryption:")
    mode = input()
    if mode not in ['E', 'e', 'D', 'd']:
        print("Incorrect input, try again.")
    elif mode in ['E', 'e']:
        encryption = True
    else:
        encryption = False

    if encryption:
        print("Enter message to be encrypted:")
        message = input()
        print("Enter keyword for encryption")
        key = input()
        new_message = Vigenère_encrypt(message.upper(), key.upper())
        print("Encrypted message:", new_message)
    else:
        print("Enter message to be decrypted:")
        message = input()
        print("Enter keyword for decryption")
        key = input()
        new_message = Vigenère_decrypt(message.upper(), key.upper())
        print("Decrypted message:", new_message)

# 65 = 'A' I want 'A' to be 1, so subtract 64
# 90 = 'Z' I want 'Z' to be 26, so subtract 64

def Vigenère_encrypt(msg, key):
    char_list = []
    key_list = []
    msg_list = []

    # ASCII value list
    for i in msg:
        char_list.append(ord(i))

    # creating the key list
    iter = 0 #iterables
    key_iter = 0
    while iter < len(char_list):
        if key_iter == len(key):
            key_iter = 0
        if chr(char_list[iter]).isalpha():
            key_list.append(ord(key[key_iter])-64)
        else:
            key_list.append(0)
        iter += 1
        key_iter += 1
    
    # encrypting the message
    for i in range(len(char_list)):
        if char_list[i] + key_list[i] > ord('Z') and chr(char_list[i]).isalpha():
            char_list[i] -= 26
        msg_list.append(chr(char_list[i]+key_list[i]))

    # return the message
    return "".join(msg_list)

def Vigenère_decrypt(msg, key):
    char_list = []
    key_list = []
    msg_list = []

    # ASCII value list
    for i in msg:
        char_list.append(ord(i))

    # creating the key list
    iter = 0 #iterables
    key_iter = 0
    while iter < len(char_list):
        if key_iter == len(key):
            key_iter = 0
        if chr(char_list[iter]).isalpha():
            key_list.append(ord(key[key_iter])-64)
        else:
            key_list.append(0)
            print("The character:", char_list[iter], "or", chr(char_list[iter]))
        iter += 1
        key_iter += 1
    
    # decrypting the message
    for i in range(len(char_list)):
        if char_list[i] - key_list[i] < ord('A') and chr(char_list[i]).isalpha():
            char_list[i] += 26
        msg_list.append(chr(char_list[i]-key_list[i]))

    # return the message
    return "".join(msg_list)

if __name__ == "__main__":
    main()