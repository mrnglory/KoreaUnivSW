def solution(n, lost, reserve):
    real_reserve = [i for i in reserve if i not in lost]
    real_lost = [i for i in lost if i not in reserve]

    for i in real_reserve:
        befo_i = i - 1
        next_i = i + 1

        if befo_i in real_lost:
            real_lost.remove(befo_i)

        elif next_i in real_lost:
            real_lost.remove(next_i)

    return n - len(real_lost)