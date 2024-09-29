def calculate(s):
    stack = []
    s = s.replace(" ", "")
    Z = []
    polish = ""
    c1 = 0
    c2 = 0
    znaki = "+-*/"
    D = {"-": 1, "+": 1, "*": 2, "/": 2}
    contrl = len(s)
    i = 0
    while i < contrl:
        if s[i] == "(":
            Z.append(s[i])
            c2 += 1
        elif s[i] == ")":
            while Z[c2 - 1] != "(":
                polish += " "
                polish += Z[c2 - 1]
                polish += " "
                Z.pop()
                c2 -= 1
            Z.pop()
            c2 -= 1
        elif s[i] in znaki:
            c2 += 1
            if Z:
                fopr = Z[-1]
                while (Z[-1] != "(") and D[fopr] <= D[s[i]]:
                    kost2 = Z.pop()
                    c2 -= 1
                    polish += " "
                    polish += kost2
                    polish += " "
                    if not Z:
                        break
            Z.append(s[i])
            polish += " "
            print(polish)
            c1 += 1
        else:
            polish += s[i]
        i += 1
    if Z:
        polish = polish + " " + Z[-1] + " "
    else:
        polish += " "
    print(polish)
    ps = ""
    for i in range(len(polish)):
        if polish[i] == " ":
            if ps != "":
                stack.append(ps)
                ps = ""
        else:
            ps += polish[i]
    print(stack)
    res = []
    for i in range(len(stack)):
        a = 0
        b = 0
        if not (stack[i] in znaki):
            res.append(int(stack[i]))
        else:
            if res:
                a = res.pop()
            if res:
                b = res.pop()
            if stack[i] == "-":
                res.append(b - a)
            elif stack[i] == "*":
                res.append(b * a)
            elif stack[i] == "/":
                res.append(b / a)
            elif stack[i] == "+":
                res.append(b + a)
        print(res)
    return res[0]
