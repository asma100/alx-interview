#!/usr/bin/python3
"""module"""
def canUnlockAll(boxes):
    """
    if all the boxes can be op. 
    """
    n = len(boxes)
    op = [False] * n
    op[0] = True
    ks = [0] 
    while ks:
        k = ks.pop()
        for new_k in boxes[k]:
            if new_k < n and not op[new_k]:
                op[new_k] = True
                ks.append(new_k)

    return all(op)
