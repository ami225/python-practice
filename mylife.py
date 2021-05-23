#自分が何日間いきているか計算

import datetime
import math

#今日
today = datetime.date.today()

#誕生日
birthday = datetime.date(1998,2,25)
life = today - birthday
print(str(life.days) + "日間生きています！")

#現在の年齢
age = math.floor(life.days / 365)
print(str(age) + "歳です")

#曜日ごとにメッセージを変える
#0は月曜日、6は日曜日

# 月曜日
if today.weekday() == 0:
    print("一週間の幕開け！！")
# 火曜 ~ 木曜日
elif today.weekday() < 4:
    print("がんばれ！！！")
# 金曜日
elif today.weekday() == 4:
    print("金曜日だ！！あとちょっと！")
# 土日
else:
    print("死ぬほど楽しめ！！！")
    
# 好きになる有名人の年齢平均

agelist = [37, 35, 40, 33, 39]

# 合計値を要素数でわる
ave = sum(agelist) / len(agelist)
# 平均値
print(str(math.floor(ave)) + "歳あたりの方を好きになる傾向があります")

# 平均値でメッセージ変える
if ave <= 30:
    print("若い男性がタイプです")
elif ave <= 40:
    print("イケオジがタイプです")
else:
    print("おじさんが可愛いと思うタイプです")