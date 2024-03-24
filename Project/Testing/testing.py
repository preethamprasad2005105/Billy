import json

def sign():

    username = input('enter username: ')
    password = input('enter password')

    f = open('data\\sign.json')
    d = json.load(f)
    print(username in d['User'] and password in d["Password"])

    if (username not in d['User']) and (password not in d["Password"]):
        d['User'].append(username)
        d['Password'].append(password)
        f = open('data\\sign.json', 'w')
        json.dump(d,f, indent=2)
        return True
    else:
        return False
        

sign()


