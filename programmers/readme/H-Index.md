# H-Index
> lv2
>
> 2020-12-08
>
> https://programmers.co.kr/learn/courses/30/lessons/42747

### Sol
> 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
>
>제한사항
>
>과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
>논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

1,000 * 10,000 = 10,000,000가지의 경우의 수로 제한 시간 내 통과가 되기 때문에 그냥 브루트포스를 이용하였다.
H-Index는 citations의 최댓값을 넘길 수 없기 때문에 범위를 지정해주었고
해당 범위 내에서 인용 횟수와의 대소관계를 통해 인용 횟수가 h이상이라면 answer에 저장한다.
(h는 0부터 citations 배열의 최대 인용횟수까지 for문을 돌게 되기 때문에 answer는 항상 최댓값을 유지하게 된다.)

```python
def solution(citations):
    answer = 0
    for h in range(0,max(citations)+1):
        num = 0
        for i in citations:
            if i >= h :
                num += 1
        if num >= h:
            answer = h

    return answer
```

### Other's Code
```python
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
```