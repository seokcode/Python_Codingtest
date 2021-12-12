import re

pattern = r'\b(100+1+|01)+\b'
sound = input()

if re.match(pattern, sound):
  print("SUBMARINE")
else:
  print("NOISE")