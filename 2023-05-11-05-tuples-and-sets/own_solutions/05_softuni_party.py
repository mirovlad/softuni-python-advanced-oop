vips = set()
regs = set()

for _ in range(int(input())):
    code = input()
    if code[0].isdigit():
        vips.add(code)
    else:
        regs.add(code)

while True:
    line = input()

    if line == "END":
        break

    if line in vips:
        vips.remove(line)
    elif line in regs:
        regs.remove(line)
    else:
        pass
        # print("?? Guest not recognized")

print(len(vips) + len(regs))
if vips:
    print(*sorted(vips), sep="\n")
if regs:
    print(*sorted(regs), sep="\n")
