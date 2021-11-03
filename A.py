# 標準入力を受け付ける。
A, B = map(int, input().split())

# A > Bの時、A以上かつB以下の整数は存在しないので、0とする。
# A <= Bの時、B - A + 1の結果を出力する。
if A > B:
    print(0)
else:
    print(B - A + 1)
