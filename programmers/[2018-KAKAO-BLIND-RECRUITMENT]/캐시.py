# 캐시

def solution(cacheSize, cities):
    answer = 0
    cache = []

    for city in cities:
        city = city.lower()  # 대,소문자 구분x
        if not city in cache:
            # cache miss
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city)
            elif cacheSize != 0:
                cache.pop(0)
                cache.append(city)
        else:
            # cache hit
            answer += 1
            cache.pop(cache.index(city))
            cache.append(city)

    return answer