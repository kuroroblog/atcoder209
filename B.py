# 標準入力を受け付ける。
N, X = map(int, input().split())

A = list(map(int, input().split()))

# セール中のN個の商品の合計金額を格納する。
a_sum_money = 0
for i in range(len(A)):
    # 偶数番目の商品に関しては、定価 - 1で購入する。
    if (i + 1) % 2 == 0:
        a_sum_money += (A[i] - 1)
    # 奇数番目の商品に関しては、定価で購入する。
    else:
        a_sum_money += A[i]

    # 途中でセール中のN個の商品の合計金額 > 所持金になった場合、`No`を出力する。
    if a_sum_money > X:
        print('No')
        exit()

print('Yes')
