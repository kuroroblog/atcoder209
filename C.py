# 標準入力を受け付ける。
N = int(input())

C = list(map(int, input().split()))

# 1 ≤ Ai ≤ Ciを満たすAiを取得するだけで、Aiを並べて生成される整数列Aに順序は必要ない。 ⏩ Cの整数列の順番をソートしても問題ない。
C.sort()

ans = 1
for i in range(len(C)):
    # ソートしたCの整数列の値が大きくなるにつれて、その分Aの整数列が生成できることを利用する。
    ans = (ans * (C[i] - i)) % (10 ** 9 + 7)

print(ans)
