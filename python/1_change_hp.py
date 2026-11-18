print("================== 문제 1 ==================")
def change_hp(hp, amount, max_hp=100):
    if hp > max_hp or hp < 0 or max_hp <= 0:
        return None

    hp += amount

    if hp >= max_hp:
        hp = max_hp
    elif hp <= 0:
        hp = 0
    
    return hp

print(change_hp(90, 25))       # 100
print(change_hp(15, -30))      # 0
print(change_hp(30, 0))        # 30
print(change_hp(70, -20, 80))  # 50
print(change_hp(130, -20))
print(change_hp(50.5, -20.5))