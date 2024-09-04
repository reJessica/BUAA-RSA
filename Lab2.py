from random import randrange

from AITMCLAB.libnum import s2n, n2s, invmod

# Use keyword 'import' to import other function from ctflab

'''
    「lzh们」非常喜欢用仿射密码分享密文涅，但是这次lzh（究竟是哪个lzh）不小心把一段密文摔成了两段，你们能帮lzh找到正确的明文汪？
'''

# assert, if the script works, it means the expression behind the 'assert' is true!
assert 1 + 1 == 2  # This is true.
# assert 1 + 1 == 1 不对～不对～!!

# Use s2n(acronym for 'string to number') to convert string to number,and use n2s to revert
s = 'You can guess which lzh set the question'
n = s2n(s)  # int
new_s = n2s(n)  # revert to string
assert new_s == s  # This is true.

a = invmod(3, 26)  #求逆元的方法
assert (a * 3) % 26 == 1


# invmod是求逆元函数，感兴趣的话可以尝试更多组数去验证一下,或者跳转去抓抓源码
# Want to know more about AITMCLab.libnum? https://github.com/hellman/libnum

# Welcome to LAB2 「Inverse Element」
# Here is an encoding procedure, try to understand
# what happened and find out the [flag]

def affine_encrypt(key, offset, msg):
    cipher = ''
    for c in msg:
        if 'a' <= c <= 'z':
            cipher += chr(((ord(c) - ord('a')) * key + offset) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            cipher += chr(((ord(c) - ord('A')) * key + offset) % 26 + ord('A'))
        else:
            cipher += c
    return cipher


def get_key():
    while True:
        key = randrange(1, 26)
        if key % 2 != 0 and key % 13 != 0:
            return key      返回非13的单数


def get_offset():
    offset = randrange(0, 26)
    return offset


flag1 = 'aitmc{xxxxxxxxxx'  # First piece!——
k = get_key()
b = get_offset()
cipher = affine_encrypt(k, b, flag1)  # Try to find the right k to get the flag2

k = get_key()
b = get_offset()
cipherl = affine_encrypt(k, b, cipher)

k = get_key()
b = get_offset()
cipherlz = affine_encrypt(k, b, cipherl)

k = get_key()
b = get_offset()
cipherlzh = affine_encrypt(k, b, cipherlz)
print(s2n(cipherlzh))  # s2n(cipherlzh)) = 2574992374550094956903337219165340952444495470

flag2 = 'xxxxxxxxxxxxxxx}'  # Second piece!——
cipher2 = affine_encrypt(2, 5, flag2)
cipher3 = affine_encrypt(13, 5, flag2)

print(s2n(cipher2))  # s2n(cipher2)) = 664527922255740620151790931196939524864799043709
print(s2n(cipher3))  # s2n(cipher3)) = 658818667412507809953389350319783663632206161533

# Try to find out the [flag]!
# This script is designed to show you the problem.So it can't be run!
# To solve the problem, you need to create a new python script file.
# Copy the key code and write the solution script!

'''
lzh(显然不是£，汪)看着被摔断的密文，大声喊出了那句话：“请帮帮我！可爱滴同学们！～”
（雾）
完成Lab2之后请根据README.md的要求上传解答
'''
