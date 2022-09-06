#!/usr/bin/python3
import random

def one(round):
    freq = [0] * 45
    for i in range(round):
        n = random.randint(0, 44)
        freq[n] = 1
    s = sum(freq)
    return s

def more(round, total):
    result = []
    for i in range(total):
        s = one(round)
        result.append(s)
    #print(f'{round} round * {total}:')
    #print(result)
    avg = sum(result) / total
    #print(f"average: {avg}")
    print(f"{round}, {avg}")


def main():
    for r in range(0, 501, 5):
        more(r, 1000)

main()
