# 나머지 # B_10430
A, B, C = map(int, input().split())

print((A + B) % C)
print(((A % C)+(B % C)) % C)
# (A + B) % C == ((A % C)+(B % C)) % C
print((A * B) % C)
print(((A % C) * (B % C)) % C)
# (A * B) % C == ((A % C) * (B % C)) % C
