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
print(str(age) + "歳で")