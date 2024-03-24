import json

def sign_up_process(username, password):
    f = open('data\\sign.json')
    d = json.load(f)

    if (username not in d['User']) and (password not in d["Password"]):
        d['User'].append(username)
        d['Password'].append(password)
        f = open('data\\sign.json', 'w')
        json.dump(d,f, indent=2)
        return True
    else:
        return False


def login_up_process(l_username, l_password):
    
    f = open('data\\sign.json')
    d = json.load(f)
    length = len(d["User"])
    flag = False
    data = {
                "Session" : True,
                "Session_Id": l_username
            }
    for i in range(length):
        if(l_username == d["User"][i] and l_password == d["Password"][i]):
            f = open('data\\session.json', 'w')
            json.dump(data, f, indent=2)
            flag = True
            break
    if flag:
        return True
    else:
        return False

     