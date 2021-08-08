class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line, allLines = [], []
        curlen = 0
        for idx in range (len(words)):
            # 1. 현재 단어까지 더하면 최대치를 넘어갈 경우
            if curlen + len(words[idx]) + len(line) > maxWidth:
                # 문장 꾸리기
                self.addline(line, allLines, maxWidth-curlen)
                
                # 초기화
                line = []
                
                # 현재 단어는 문장꾸리기에 포함되지 않았기 때문에 다음 for문을 위해 추가
                line.append(words[idx])
                curlen = len(words[idx])
                
                # 근데 해당 단어가 words배열의 마지막 단어였을 경우 바로 문장 꾸리기로 넘겨
                # 이 경우는 단어가 하나만 존재하는 경우
                if idx == len(words)-1:
                    self.addline(line, allLines, maxWidth-curlen)
           
            # 2. 현재 단어까지 더해도 최대치 이하인 경우
            else:
                line.append(words[idx])
                curlen += len(words[idx])
                
                # 최대치는 이하이지만 그 단어가 words 배열의 마지막 단어였다면 문장 꾸리기로 넘겨야함
                # 이 경우는 단어가 여러개 존재하는 경우 -> 단어와 단어 사이는 한칸만 나머지는 끝나는 단어 우측에 삽입
                if idx == len(words)-1:
                    new = ''
                    for i in range (len(line)-1):
                        new += line[i] + ' '
                    new+=line[-1]
                    new+= ' '*((maxWidth)-len(new))
                    allLines.append(new)
        return allLines
                    
    # maxWidth에 맞춰서 문장을 꾸리는 메서드
    def addline(self, l, allLines, space):
        # divide by zero 처리
        left = space//(len(l)-1) if len(l)>1 else space//len(l)
        over = space%(len(l)-1)  if len(l)>1 else space%len(l)
        line = ''
        
        for i in range (len(l)):
            line += l[i]
            if len(l)==1 or i<len(l)-1:
                line += ' '*left
                
                # 나머지가 있다는 것은 왼쪽에 더 많은 space를 넣어야 하는 것
                # 5//3 = 1 && 5%3 = 2이다. 이 말은 모두 1칸씩 갖되 왼쪽부터 1칸씩 추가로 가져야 한다는 뜻이다.
                # 따라서 2, 2, 1 순으로 space가 분배된다. 아래는 그 로직이다.
                if over>0:
                    line+= ' '
                    over-=1
        allLines.append(line)