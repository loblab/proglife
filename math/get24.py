#!/usr/bin/env python3
import sys

OP_ADD = lambda a, b: [a[0]*b[1]+a[1]*b[0], a[1]*b[1]]
OP_SUB = lambda a, b: [a[0]*b[1]-a[1]*b[0], a[1]*b[1]]
OP_BUS = lambda a, b: [a[1]*b[0]-a[0]*b[1], a[1]*b[1]]
OP_MUL = lambda a, b: [a[0]*b[0], a[1]*b[1]]
OP_DIV = lambda a, b: [a[0]*b[1], a[1]*b[0]]
OP_VID = lambda a, b: [a[1]*b[0], a[0]*b[1]]
solid = lambda x: x.isnumeric() or x[0]=='(' and x[-1]==')'
TEXT_ADD = lambda a, b: f"({a} + {b})"
TEXT_SUB = lambda a, b: f"({a} - {b})" if solid(b) else f"({a} - ({b}))"
TEXT_BUS = lambda a, b: f"({b} - {a})" if solid(a) else f"({b} - ({a}))"
TEXT_MUL = lambda a, b: f"{a} * {b}"
TEXT_DIV = lambda a, b: f"{a} / {b}" if solid(b) else f"{a} / ({b})"
TEXT_VID = lambda a, b: f"{b} / {a}" if solid(a) else f"{b} / ({a})"
OPS_OP = [OP_ADD, OP_SUB, OP_BUS, OP_MUL, OP_DIV, OP_VID]
OPS_TEXT = [TEXT_ADD, TEXT_SUB, TEXT_BUS, TEXT_MUL, TEXT_DIV, TEXT_VID]
OPS_CODE = range(len(OPS_OP))

def solve(a):
    if len(a) == 1:
        check_24(a[0])
        return
    for op in OPS_CODE:
        for i in range(len(a) - 1):
            if i > 0 and a[i] == a[i-1]:
                continue
            for j in range(i+1, len(a)):
                if j > i+1 and a[j] == a[j-1]:
                    continue
                b = a[:]
                i1, i2 = b[i], b[j]
                del b[j]
                del b[i]
                b.append([op, i1, i2])
                solve(b)

def calc(expr):
    if type(expr) is int:
        return [expr, 1]
    return OPS_OP[expr[0]](calc(expr[1]), calc(expr[2]))

def text(expr):
    if type(expr) is int:
        return str(expr)
    return OPS_TEXT[expr[0]](text(expr[1]), text(expr[2]))

def check_24(expr):
    global count
    val = calc(expr)
    if val[1] > 0 and val[0] == val[1] * 24:
        count += 1
        print(f"{count:2d}: {text(expr)} = 24")

count = 0
nums = list(map(int, sys.argv[1:]))
nums.sort()
print(f" Q: {nums}")
solve(nums)

