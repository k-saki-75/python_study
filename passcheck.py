import re

def passcheck(password):
    if(re.match('\A(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)[a-zA-Z\d]{8,100}\Z', password)):
        print('強いパスワードです')
    else:
        print('弱いパスワードです')
    



print('パスワードの強さをチェックします。')
password = input()
passcheck(password)
