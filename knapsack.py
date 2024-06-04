"""
ナップサック問題(Knapsack Problem)は、与えられた制限付きの容量を持つナップサックに、価値や重みの異なるアイテムを詰め込む際の最適な組み合わせを求める問題です。

具体的な例として、容量が10のナップサックに、価値が6のアイテムAと価値が8のアイテムBがあります。アイテムの重さがそれぞれ4と6である場合、この問題ではどのアイテムを選ぶべきかが求められます。

ナップサックの容量とアイテムの数を定義します。
動的計画法のテーブル（配列）を用意し、初期値を設定します。
テーブルを更新していきます。
最終的な結果をテーブルから読み取り、最適な組み合わせが得られます。
"""

def knapsack_problem(capacity, weights, values):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if j >= weights[i - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][capacity]

# ナップサックの容量が10で、アイテムAの重さが4、価値が6、アイテムBの重さが6、価値が8の場合
weights = [4, 6]
values = [6, 8]
capacity = 10

print(knapsack_problem(capacity, weights, values))  # 結果: 8
