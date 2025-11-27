def solution(hp):
    answer = 0
    general, soldier, worker = 0,0,0
    
    # 1. 장군 개미
    general = hp // 5
    hp -= general * 5
    
    # 2. 병정 개미
    if hp <= 4 :
        soldier = hp // 3
        hp -= soldier * 3
    # 3. 일개미
    if hp > 0 :
        worker = hp
        
    answer = general + soldier + worker
    
    return answer