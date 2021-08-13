# 멀쩡한 사각형

def solution(w, h):
    if w == h: return w * h - w

    if w < h:
        w, h = h, w

    def gcd(w, h):
        if h == 0:
            return w
        else:
            return gcd(h, w % h)

    return w * h - (w + h - gcd(w, h))