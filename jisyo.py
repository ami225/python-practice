# coding: utf-8
# Your code here!

# リストのおさらい
enemyArray = ["スライム", "モンスター", "ドラゴン"]
print(enemyArray)
print(enemyArray[0])

#辞書の具体例
#(値を取り出すためのキー) : (対応する値)
#辞書を取り出す順番はエントリーを登録した順番と異なる場合がある
enemyDictionary = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
print(enemyDictionary) # => {'ザコ': 'スライム', '中ボス': 'ドラゴン', 'ラスボス': '魔王'}
print(enemyDictionary["中ボス"]) # => ドラゴン

#変数で取り出す場合
level = "ザコ"
print(enemyDictionary[level]) # => スライム

print(enemyDictionary["敵"]) #辞書の中に敵という値はないとエラーが出る