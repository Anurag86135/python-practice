# Encrypt and Decrypt_Message

n=int(input())
s=input().strip()

original="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
key = "PgEfTYaWGHjDAmxQqFLRpCJBownyUKZXkbvzIdshurMilNSVOtec#@_!=.+-*/"

encrypt_map={}
decrypt_map={}

for i in range(len(original)):
    o_char =original[i]
    k_char=key[i]

    encrypt_map[o_char]=k_char
    decrypt_map[k_char]=o_char

result=[]
if n==1:
    for ch in s:
        result.append(encrypt_map[ch])
else:
    for ch in s:
        result.append(decrypt_map[ch])

print("".join(result))