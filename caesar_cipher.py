def has_keyword(message, keywords):
    message = " " + message

    for word in keywords:
        word = " " + word
        if word in message:
            return True

    return False        

def find_shift(message, lisd):
    for i in lisd:
        count = 0
        if count < len(lisd):
            bah = decrypt(message, i)
            if has_keyword(bah, common):
                return decrypt(bah, i)
        count += 1

def shift(letter, shift_amount):
    unicode_value = ord(letter) + shift_amount

    if unicode_value > 126:
        unicode_value += - 95
    elif unicode_value < 32:
        unicode_value += 95

    new_letter = chr(unicode_value)

    return new_letter

def encrypt(message, shift_amount):
    result = ""
    for letter in message:
        result += shift(letter, shift_amount)

    return result

def decrypt(message, shift_amount):
    result = ""
    return encrypt(message, (-1) * shift_amount)

#unencrypted_message = "ABCD. I hate eels!!! These are the last 4 ascii characters: {|}~"
#encrypted_message = encrypt(unencrypted_message, 3)
#decrypted_message = decrypt(encrypted_message, 3)

common = ["and" , "the"]
onetwothree = [1, 2, 3]
unencrypted_message = "hey howdy hey"
encrypted_message = encrypt(unencrypted_message, 2)
decrypted_message = find_shift(encrypted_message, onetwothree)

print(unencrypted_message)
print(encrypted_message)
print(decrypted_message)


#print(find_shift(123))


      
