# N으로 표현
> lv3
>
> 2021-01-28
>
> https://programmers.co.kr/learn/courses/30/lessons/42895

### Sol


DP(동적계획법)을 이용하여 푸는 문제이다.

DP는 알다가도 모르겠다..ㅠㅠ  
먼저 규칙을 찾아야 한다.

N=1: [5]  
N=2: [55],[5+5],[5-5],[5*5],[5//5]  
N=3: [55+5],[55-5],[55*5],[55//5],[(5+5)+5],[(5+5)-5],[(5+5)*5],[(5+5)//5]...

이 정도만 쓰면 어느정도 규칙이 보인다.  
N=2인 경우는 같은 수가 2번 연속인 경우(55) 그리고 N=1인 경우와 N=1인 경우의 사칙연산이다.  
따라서 N=3인 경우는 N=1과 N=2인 경우의 사칙연산으로 구할 수 있다.  
이런식으로 N의 최솟값부터 시작하여 최초로 numbers가 나오는 N을 return해주는 알고리즘을 적용하여 풀면 된다.


단 주의해야할 점이 있다.  
N=6인 경우를 예로 들어보자, 6의 절반인 3까지만 체크해도 모든 경우를 볼 수 있다. 

> (`1`+5) (`2`+4) (`3`+3)  

그 이상이 되면 (4+2), (5+1)처럼 결과값에 있어서 중복되는 경우가 생긴다.


```python
def solution(N, number):
    possible_set = [0,[N]] # 조합으로 나올수 있는 가능한 숫자들, 여기에 계속 append하며 이후에 사용함
    
    if N == number: #숫자 N을 이용해서 number를 표현할 수 있는 방법은 1개 뿐
        return 1
    
    for i in range(2, 9): # N은 1이상, 9이하(N=1일 경우는 1개라서 2부터 시작)
        case_set = [] # 임시로 사용할 케이스 셋, 각 I 별로 셋을 만들어 possible set에 붙인다.
        basic_num = int(str(N)*i) # N=2부터는 같은 숫자가 반복되는게 한개씩 포함(55,555,5555...)
        case_set.append(basic_num)
        
        # 사용되는 숫자의 횟수를 구해야 하는데, 절반 이상으로 넘어가면 같은 결과만 나올 뿐이므로 절반까지만을 사용한다. 
        for i_half in range(1, i//2+1): 
            for x in possible_set[i_half]:
                for y in possible_set[i-i_half]: # x와 y를 더하면 i 가 되도록 만든 수다. 
                    case_set.append(x+y)# 각 사칙연산 결과를 더한다.
                    case_set.append(x-y)
                    case_set.append(y-x)
                    case_set.append(x*y)
                    if y !=0:
                        case_set.append(x/y)
                    if x !=0:
                        case_set.append(y/x)
            if number in case_set:
                return i
            possible_set.append(case_set) # 최종 결과물 set에 사칙 연산 결과를 더한다.
    return -1 #N 이 8까지 답이 없으면 -1을 출력한다.
```