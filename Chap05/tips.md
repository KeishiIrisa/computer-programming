# 理解

- 5.1.2 12 行目 return n って？
  - このコードでは、\_insert_by_recursion メソッドが再帰的に呼び出されています。つまり、メソッドが自分自身を呼び出しています。新しいノード（キーが 6）が作成されて return されると、その return 文は最も深くネストされた\_insert_by_recursion の呼び出しを終了します。しかし、その呼び出し元である一つ上のレベルの\_insert_by_recursion の実行はまだ続いています。
  - n.left = self.\_insert_by_recursion(n.left, key, value)これらの行では、\_insert_by_recursion メソッドが新しいノードを返し（return Node(key, value)）、その新しいノードが現在のノード（n）の left または right に設定されます。
  - return n は、現在のノード（n）を返しますが、この n はその直前に n.left または n.right が更新された可能性があります。つまり、新しいノードが n の左子または右子として追加された場合、その情報が n に含まれます。
    そして、この return n によって返されたノード（とその下のサブツリー）は、一つ上のレベルの\_insert_by_recursion メソッドの呼び出し元に伝えられます。つまり、n.left = self.\_insert_by_recursion(n.left, key, value)または n.right = self.\_insert_by_recursion(n.right, key, value)の行で、一つ上のレベルのノードの左子または右子として設定されます。
- 5.1.319 行目の right_min_node の処理
  - node.right = self.\_delete_by_recursion(node.right, node.key)：この行では、右部分木から right_min_node（つまり、削除するノードのキーと同じキーを持つノード）を削除しています。これは、right_min_node の情報が削除するノードにコピーされた後で行われます。この操作により、right_min_node が二度出現することを防ぎます。
  - 右側の最も小さいノードを見つけて、対象のノードを上書きする。そして、上書きのもととなる右側の最も小さいノードであったものを、node.right から消す。その処理は現在の node は元々右側で最も小さいノードだったので、現在のノードの右側スタートで、key が現在の node.key のものを削除する
- 演習 5-3
  - input()に関して
    - Python の input()関数はユーザーからの入力を一行ずつ読み込みます。したがって、一行目だけを出力したい場合は、一度だけ input()を呼び出すことで実現できます。
