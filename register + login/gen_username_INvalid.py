import random
import json

# file to store registered accounts
# filename = "registeredAccounts.json"
filename = registeredAccounts_filepath

valid_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                    "W", "X", "Y", "Z", "_", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "@", ".", "+", "-"]

INvalid_characters = ["!", "#", "$", "%", "&",
                      "(", ")", "{", "}", "[", "]", "|", "*", ",", "<", ">", "=", "/", "\\", ":", ";", "~", "`", "'", '"', "^"]
# invalid characters -> not only alphanumeric
# 31 or more characters


# def generate_username_INvalid():
#     choice = random.randint(1, 3)
#     if choice == 1:
#         generate_username_INvalid_chars()
#     elif choice == 2:
#         generate_username_INvalid_length()
#     else:
#         generate_username_INvalid_taken()


def generate_username_INvalid_chars():
    invalid_length = random.randint(1, len(INvalid_characters))
    valid_length = random.randint(0, 30-invalid_length)
    character = []
    for i in range(invalid_length):
        index = random.randint(1, len(INvalid_characters))-1
        character.append(INvalid_characters[index])

    for j in range(valid_length):
        index = random.randint(1, len(valid_characters))-1
        character.append(valid_characters[index])

    g_username = ""
    while len(character) != 0:
        index = random.randint(1, len(character)) - 1
        g_username += character[index]
        del character[index]

    return g_username

# seems like it passes the testcase, but the account is not actually registered in the backend
# def generate_username_INvalid_length():
#     length = random.randint(256, 300)

#     g_username = ""

#     for i in range(length):
#         character_index = random.randint(1, len(valid_characters)-1)
#         g_username += valid_characters[character_index]

#     # print(generated_username)
#     return g_username


def generate_username_INvalid_taken():
    index = random.randint(1, usernameCount)-1
    g_username = arrayOfUsernames[index]
    return g_username


# looking thru json file to find already registered usernames
f = open(filename)
data = json.load(f)

arrayOfUsernames = []
for i in data['accounts']:
    username = i['username']
    arrayOfUsernames.append(username)

usernameCount = len(arrayOfUsernames)

f.close()

# test below ############################################################
# print(generate_username_INvalid_chars())


# for i in range(10):
#     user = generate_username_INvalid_length()
#     print(str(len(user)) + " :  " + user)


# generate_username_INvalid_taken()
