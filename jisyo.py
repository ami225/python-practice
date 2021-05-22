# coding: utf-8
# Your code here!



# 辞書の基本操作
enemies = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
print(enemies)
print(enemies["ザコ"])
print(len(enemies))

#追加
enemies["ザコ２"] = "メタルモンスター"
print(enemies) # {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王", "ザコ2":"メタルモンスター"}
print(len(enemies)) #４

#上書き
enemies["中ボス"] = "レッドドラゴン"
print(enemies) #{"ザコ":"スライム", "中ボス":"レッドドラゴン", "ラスボス":"魔王", "ザコ2":"メタルモンスター"}
print(len(enemies)) #4

#削除
del enemies["ザコ"]
print(enemies) #{"中ボス":"ドラゴン", "ラスボス":"魔王", "ザコ2":"メタルモンスター"}
print(len(enemies)) #3




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



# 辞書をループで処理する

# 辞書のおさらい
enemies = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
print(enemies)
print(enemies["ザコ"])

#ループ処理で表示
for rank in enemies:
    print(enemies[rank] + "が現れた!")
    
# スライムが現れた!
# ドラゴンが現れた!
# 魔王が現れた!


#複数取り出すにはitems()メソッドを使う
#最初のキーをrankで取り出して、enemyで値を取り出す
for (rank, enemy) in enemies.items():
    print(rank + "の" + enemy + "が、現れた！")
    
# ザコのスライムが、現れた！
# 中ボスのドラゴンが、現れた！
# ラスボスの魔王が、現れた！


# 練習問題
points = {"国語":50, "理科":70, "算数":60, "英語":90}
#合計点数を表示
sum = 0
for num in points:
    sum += points[num]
    
print(sum)


# リストの整列
weapons = ["イージスソード", "ウィンドスピア", "アースブレイカー", "イナズマハンマー"]
print(weapons)

#アイウエオ順で表示
print(sorted(weapons))
# 'アースブレイカー', 'イナズマハンマー', 'イージスソード', 'ウィンドスピア']

#アイウエオ順を反転
print(sorted(weapons, reverse=True))
# ['ウィンドスピア', 'イージスソード', 'イナズマハンマー', 'アースブレイカー']

#数字順に表示
weapons2 = ["4.イージスソード", "1.ウィンドスピア", "3.アースブレイカー", "2.イナズマハンマー"]
print(sorted(weapons2))
# ['1.ウィンドスピア', '2.イナズマハンマー', '3.アースブレイカー', '4.イージスソード']


name = ["あみ", "まる", "けんと", "じゅんき", "ヤマト", "みさき"]
print(sorted(name))
# ['あみ', 'けんと', 'じゅんき', 'まる', 'みさき', 'ヤマト']


#アイテム画像を表示させる
# 画像用辞書
items_imges = {
    "剣" : "http://paiza.jp/learning/images/sword.png",
    "盾" : "http://paiza.jp/learning/images/shield.png",
    "回復薬" : "http://paiza.jp/learning/images/potion.png",
    "クリスタル" : "http://paiza.jp/learning/images/crystal.png"
}

# アイテムの並び順リスト
items_orders = ["剣", "盾", "回復薬", "クリスタル"]


for item_name in items_orders:
    #アイテム画像
    print("<img src='" + items_imges[item_name] + "'>""<br>")
    

#練習問題

# 画像用辞書
items_imges = {
    "剣" : "http://paiza.jp/learning/images/sword.png",
    "盾" : "http://paiza.jp/learning/images/shield.png",
    "回復薬" : "http://paiza.jp/learning/images/potion.png",
    "クリスタル" : "http://paiza.jp/learning/images/crystal.png"
}


#出力するアイテム数を変数に代入
item_cnt = int(input())

#標準入力にあるアイテムを出力する
while item_cnt > 0: #0になるまで繰り返す
    item = input()
    print("<img src = '" + items_imges[item] + "'>")
    item_cnt = item_cnt - 1