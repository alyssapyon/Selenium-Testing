import random

valid_characters_domain = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                           "W", "X", "Y", "Z", "_", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ".", "+", "-"]

valid_characters_user = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                         "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ".", "+", "-"]


def generate_email_valid():
    # email length between [3,254] inclusive

    # max length for domain name labels is 63 characters per RFC 1034
    # 1 to 63 inclusive
    domain_length = random.randint(1, 63)
    user_length = random.randint(1, 253-domain_length)

    generated_user = ""
    generated_domain = ""
    generated_email = ""

    # generate domain
    for i in range(domain_length):
        character_index = random.randint(0, len(valid_characters_domain)-1)
        generated_domain += valid_characters_domain[character_index]

    while generated_domain[0] in [".", "_"]:
        generated_domain[1:]

    while generated_domain[-1] in [".", "_"]:
        generated_domain[:-2]

    # generated user
    for i in range(user_length):
        character_index = random.randint(0, len(valid_characters_user)-1)
        generated_user += valid_characters_user[character_index]

    while generated_user[0] in [".", "_"]:
        generated_user[1:]

    while generated_user[-1] in [".", "_"]:
        generated_user[:-1]

    generated_email = generated_user + "@" + generated_domain
    # print(generated_email)
    # print()
    return generated_email


generate_email_valid()
# generate_email_valid()
# generate_email_valid()
# generate_email_valid()
# generate_email_valid()
# generate_email_valid()
# generate_email_valid()
# generate_email_valid()
# generate_email_valid()
# generate_email_valid()
# print("done")
