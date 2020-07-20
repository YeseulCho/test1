#! /usr/bin/env python

import sys

if len(sys.argv) != 2 :
    print(f"#usage: python {sys.argv[0]} [fasta]") # 오류 안나게
    sys.exit()

f = sys.argv[1]
d = {}

with open(f, 'r') as handle :
    for line in handle :
        if line.startswith(">") :
            continue
        for s in line.strip() :
            if s in d :
                d[s] += 1
            else :
                d[s] = 1

print(d)

total = 0
for k, v in d.items() : # dic
    total += v

# covid dic 나온거 출력하기
with open("result.txt", 'w') as handle :
    handle.write(f"A: {d['A']}\n")
    handle.write(f"C: {d['C']}\n")
    handle.write(f"G: {d['G']}\n")
    handle.write(f"T: {d['T']}\n")
