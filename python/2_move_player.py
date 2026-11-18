print("================== 문제 2 ==================")
def move_player(pos, direction, walls):
    first_pos = pos
    cm_pos = list(pos)

    if direction == "U":
        cm_pos[1] -= 1
        s_pos = tuple(cm_pos)
        if (s_pos in walls) or (cm_pos[1]<0):
            return first_pos
        return s_pos

    elif direction == "D":
        cm_pos[1] += 1
        s_pos = tuple(cm_pos)
        if (s_pos in walls) or (cm_pos[1]>4):
            return first_pos
        return s_pos

    elif direction == "L":
        cm_pos[0] -= 1
        s_pos = tuple(cm_pos)
        if (s_pos in walls) or (cm_pos[0]<0):
            return first_pos
        return s_pos

    elif direction == "R":
        cm_pos[0] += 1
        s_pos = tuple(cm_pos)
        if (s_pos in walls) or (cm_pos[0]>4):
            return first_pos
        return s_pos

    else:
        return first_pos

    
walls = {(2, 1), (3, 3)}

print(move_player((1, 1), "R", walls))  # (1, 1)
print(move_player((1, 1), "D", walls))  # (1, 2)
print(move_player((0, 0), "L", walls))  # (0, 0)
print(move_player((4, 4), "D", walls))  # (4, 4)
print(move_player((2, 2), "X", walls))  # (2, 2)