# String_Functions

N, Q = map(int, input().split())
S = list(input())   # IMPORTANT: list for mutability

for _ in range(Q):
    q = input().split()

    if q[0] == "pop_back":
         if S:
            S.pop()

    elif q[0] == "front":
        print(S[0])

    elif q[0] == "back":
        print(S[-1])

    elif q[0] == "sort":
        l = int(q[1]) - 1
        r = int(q[2]) - 1
        S[l:r+1] = sorted(S[l:r+1])

    elif q[0] == "reverse":
        l = int(q[1]) - 1
        r = int(q[2]) - 1
        S[l:r+1] = S[l:r+1][::-1]

    elif q[0] == "print":
        pos = int(q[1]) - 1
        print(S[pos])

    elif q[0] == "substr":
        l = int(q[1]) - 1
        r = int(q[2]) - 1
        print(''.join(S[l:r+1]))

    elif q[0] == "push_back":
        S.append(q[1][0])

