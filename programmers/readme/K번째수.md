# K번째수
> lv1
>
> 2020-12-08
>
> https://programmers.co.kr/learn/courses/30/lessons/42748

### Sol
commands가 2차원 배열로 주어지기 때문에 1차원 배열로서 나누어 주어야 했다.
for문을 이용하여 num에 저장된 일차원배열의 인덱스를 통해 배열을 자르고 newarray에 저장한다.
오름차순 정렬 후 num[2]번째 수를 answer에 넣어준다.

배열을 자를 때에 [2,5,3]이면 2번째 수부터 5번째 수까지 잘라야 한다.
때문에 `array[2:5]`로 하게 되면 3번째 수부터 5번째 수까지 잘리므로 `array[1:5]`여야 함을 주의한다.
```python
def solution(array, commands):
    answer = []

    for num in commands:
        newarray = array[num[0] - 1:num[1]]
        newarray.sort()
        answer.append(newarray[num[2] - 1])

    return answer
```

### 한줄 코드
`lambda`, `map`이 유용하게 많이 쓰이니 사용법을 항상 잘 숙지해두도록 하자
```python
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
```
