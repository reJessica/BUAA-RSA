from AITMCLAB.libnum import s2n, xgcd

message = 'xxxxx{xxxxxxxxxxxxxxxxxxxxxxxxxxxx}'  # You can't see the [message] here!! hahaha
cipher = ''
key, _, _ = xgcd(24249125136394343, 16156191447296617)
key = key % 16156191447296617  # key is actually the inverse

for char in message:
    if 'a' <= char <= 'z':
        now_cipher = (ord(char) - ord('a') + key) % 26
        cipher += chr(now_cipher + ord('a'))
    else:
        cipher += char

numOfCipher = s2n(cipher)
bigPrime = 356591097085378373041406631775396675403608993465904761745667548546613469964055945893375233
output, _, _ = xgcd(numOfCipher, bigPrime)
output = output % bigPrime  # output is actually the inverse  逆元
print(output)
output=233238587670647787805028809001128036933176275182381815462045390514627843647184629262585311
# Try to find out the [message]!
# This script is designed to show you the problem.So it can't be run!
# To solve the problem, you need to create a new python script file.
# Copy the key code and write the solution script!
