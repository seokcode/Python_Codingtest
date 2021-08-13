def sosu(num):
    t = 2
    if num < 2:
        return False

    while t * t <= num:
        if num % t == 0:
            return False
        t += 1
    return True

def saangn(num, visit):
  result = 0
  for i in list(str(num)):
    result += int(i)**2
  if result == 1:
    return True
  elif result in visit:
    return False
  else:
    visit.append(result)
    return saangn(result, visit)



number = int(input())
sosuArr,visit = [],[]
for i in range(2,number+1):
  if sosu(i): sosuArr.append(i)

for i in sosuArr:
  if saangn(i,visit):
    print(i)
  visit = []