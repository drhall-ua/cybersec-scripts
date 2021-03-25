# Password cracker from Violent Python

from crypt import crypt


def test_pw(crypt_pass):
    salt = crypt_pass[:2]
    dict_file = open('dictionary.txt', 'r')

    for word in dict_file.readlines():
        crypt_word = crypt(word.strip('\n'), salt)
        if crypt_word == crypt_pass:
            print(f'[+] Found Password: {word}\n')
            return

    print('[-] Password Not Found.\n')
    return


if __name__ == '__main__':
    pw_file = open('passwords.txt')
    for line in pw_file.readlines():
        if ':' in line:
            user = line.split(':')[0]
            _crypt_pass = line.split(':')[1].strip()
            print(f'[*] Cracking Password For: {user}')
            test_pw(_crypt_pass)