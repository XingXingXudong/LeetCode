# coding: utf-8

from collections import deque

def open_lock(deadends, target):
    dead_set = set(deadends)
    queue = deque([('0000', 0)])
    visited = set('0000')

    while queue:
        print(queue)
        cur_state, step = queue.popleft()
        if cur_state == target:
            return step
        elif cur_state in dead_set:
            continue
        else:
            for i in range(4):
                d = int(cur_state[i])
                for move in [-1, 1]:
                    new_d = (d + move) % 10
                    new_state = cur_state[:i] + str(new_d) + cur_state[i+1:]
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, step + 1))
    return -1

if __name__ == '__main__':
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    output = 6
    assert open_lock(deadends, target) == output
    deadends = ["8888"]
    target = "0009"
    output = 1
    assert open_lock(deadends, target) == output
    deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    target = "8888"
    output = -1
    assert open_lock(deadends, target) == output
    deadends = ["0000"]
    target = "8888"
    output = -1
    assert open_lock(deadends, target) == output

