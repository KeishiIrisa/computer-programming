# 有用なコード

- 平方根を取るための math モジュールの sqrt メソッド

  ```
  math.sqrt(s*(s-a)*(s-b)*(s-c))
  ```

- global glb

  - 関数の中で`global 変数`を実行すると、大域変数(グローバル変数)に代入できるようになる
  - 関数の中でグローバル変数と同じ関数名で代入すると、グローバル変数には代入できずに、関数内で新しく変数が宣言される。
  - 実引数でリストを渡し、グローバル変数のリストを関数内で変更した場合、グローバル変数も変更される

- swap 関数の宣言
  ```
  def swap(a,i,j):
      a[i], a[j] = a[j], a[i]
  ```
- recursion(再帰)

  ```
  def recursion_example(i):
      if i == 0:
          print("recursion_finished.")
      else:
          print("This is", i, "th recursion.") recursion_example(i-1)
          recursion_example(4)
  ```

  - 再帰関数ないでは必ず、`if / else`で分岐を作る(漸化式の`n = 1`の時の宣言と同じ意味)

- クラスの宣言

  ```
  class Date:
      def __init__(self,y,m,d):
          self.year = y self.month = m self.day = d
      def is_new_year_day(self):
          return (self.month == 1) and (self.day == 1)
      def print(self):
          print(" 今 日 は "+str(self.year)+" 年 "+str(self.month)+" 月 "+str(self.day)+" 日 で す 。 ") return
  ```

- クラスの継承のオーバーライド

  - スーパークラスを継承した子クラスで`def __init__():`メソッドを記すと、親クラスの**init**メソッドは使用できない

- exec 関数
  - exec 関数は文字列を受け取るとその文字列を Python のプログラムの式または文として評価を行う。すなわち、exec(X)がある場所にあたかも X がプログラム中に書かれているかのように振る舞う
