import random


# 扩展欧几里得算法
def xgcd(a, b):
    if a % b == 0:
        return b
    else:
        c = a % b
        return xgcd(b, c)


# 求逆元算法
def inverse(m, N1, x1, y1, x2, y2):
    if m % N1 == 0:
        return x2
    else:
        (c, x3, y3) = ((m % N1), (x1 - (m // N1) * x2), (y1 - (m // N1) * y2))
        (m, x1, y1) = (N1, x2, y2)
        (N1, x2, y2) = (c, x3, y3)
        return inverse(m, N1, x1, y1, x2, y2)


# 快速模幂算法
def quickmod(m, e1, N2):
    list2 = [0] * len(bin(e1)[2:])
    temp = m
    re = 1
    for i in range(len(bin(e1)[2:])):
        list2[i] = temp
        temp = (temp * temp) % N2
    temp = e1
    for i in range(len(bin(e1)[2:])):
        if ((temp & 1) | 0) == 1:
            re = (re * list2[i]) % N2
        temp = temp >> 1
    return re


# 素性检验算法
def is_prime(n, times=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    k, q2 = 0, n - 1
    while q2 % 2 == 0:
        k += 1
        q2 = q2 // 2
    for i in range(times):
        a = random.randint(2, n - 2)
        x = quickmod(a, q2, n)
        if x == 1 or x == - 1 + n:
            continue
        for j in range(k - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # 寻找失败，则a为合数的米勒拉宾算证据 有一个就行
    return True  # 十个a都不为合数的米勒拉宾算证据


# 密钥生成函数
def getkey(bits):
    p2 = generate_prime(bits)
    q2 = generate_prime(bits)
    N3 = p2 * q2
    phi = (p2 - 1) * (q2 - 1)
    while True:
        e3 = random.randint(3, 100)
        if xgcd(e3, phi) == 1:
            break
    d3 = inverse(e3, phi, 1, 0, 0, 1)
    return N3, e3, d3, p2, q2


def generate_prime(bytes):
    while True:
        p1 = int.from_bytes(random.randbytes(bytes))
        if is_prime(p1):
            return p1


# 加解密函数
def solve(p4, q4, c, e4):
    N4 = p4 * q4
    phi = (p4 - 1) * (q4 - 1)
    d4 = (inverse(e4, phi, 1, 0, 0, 1) + phi) % phi
    flag1 = quickmod(c, d4, N4)
    return flag1


# 用中国剩余定理优化 RSA 的解密速度。
def CRT(c, p5, q5, e):
    d1 = (inverse(e, p5 - 1, 1, 0, 0, 1) + p5 - 1) % (p5 - 1)
    d2 = (inverse(e, q5 - 1, 1, 0, 0, 1) + q5 - 1) % (q5 - 1)
    red1 = (inverse(q5, p5, 1, 0, 0, 1) + p5) % p5
    red2 = (inverse(p5, q5, 1, 0, 0, 1) + q5) % q5
    return (q5 * red1 * quickmod(c, d1, p) + p5 * red2 * quickmod(c, d2, q) + p5 * q5) % (p5 * q5)


# 扩展要求a. 对消息进行数字编码，进而实现对消息进行加解密。
def s2n(msg2):
    encoded_msg = ""
    for char in msg2:
        ascii_val = str(ord(char))
        encoded_msg += ascii_val
    return int(encoded_msg)


def n2s(msg3):
    decoded_msg = ""
    i = 0
    while i < len(msg3):
        ascii_val = int(msg3[i:i + 3])
        if 128 > ascii_val > 99:
            decoded_msg += chr(ascii_val)
            i += 3
            continue
        else:
            ascii_val = int(msg3[i:i + 2])
            if 100 > ascii_val > 10:
                decoded_msg += chr(ascii_val)
                i += 2
                continue
            else:
                ascii_val = int(msg3[i:i + 1])
                decoded_msg += chr(ascii_val)
                i += 1
                continue
    return decoded_msg


# 加解密函数
msg = input()  # 输入要加密的明文
N, e, d, p, q = getkey(128)  # 得到密钥
msg = s2n(msg)  # 对消息进行数字编码，进而实现对消息进行加密
print(msg)  # 打印密文
msg = c3b8131a0ccc4df00f740b7eded9a2be4f8634ce9df6a13dd2edf184fc948d423fccd8b2afeebc664e053f3c2dd68671720bc01a00be7da3fff46c0f121eb1c152b6062a1b9e21f83a884c40d2b1f8beb4563a25b0219d88eba1f68d01be56cc8e04c8ecd92ada28d8cb2987a1beebf677d24e9ce73599516d370c906a85dcf92b6b3e779d71f7605a3fff29497b094d33887ad095d89b63fc8a422b689f663041eeb3d45b5798c7a7a15fb098085b5089a1d757ed46433a4eb2d9c26a52d5c2f83bd9c9765751054d59fb17782460a7d6d8ba5d4d6dad9b87cb5b053ca93195944d63c9ca827abc787f3985a831eefd3efd4db68e88cfb36893918f8c883907
# 普通求解
c1 = quickmod(msg, e, N)
flag = solve(p, q, c1, e)
flag = n2s(str(flag))
print(flag)
# 使用CRT算法进行加速求解
flag = CRT(c1, p, q, e)
flag = n2s(str(flag))
print(flag)
