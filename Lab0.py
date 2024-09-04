import math

from AITMCLAB import libnum

key = math.gcd(24249125136394344, 16156191447296618)
cipher = libnum.n2s(65722036292235302559481638183079634381922421508384374553067167612847784078042536639378200757956348168334378680716856243200381)
cipher1 = ''
string = str(cipher)
length = len(string)
for i in range(length):
    if 'a' <= string[i] <= 'z':
        now_cipher = chr((ord(string[i]) - ord('a') - key + 26) % 26 + ord('a'))
        cipher1 += now_cipher
    else:
        cipher1 += string[i]
print(cipher1)
