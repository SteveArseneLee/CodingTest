def solution(name, yearning, photo):
    name_yearning = {name[i]: yearning[i] for i in range(len(name))}
    # print(name_yearning)
    answer = []
    for tmp in photo:
        score = 0
        for i in tmp:
            if i not in name: continue
            score += name_yearning[i]
            
        answer.append(score)
    
    return answer