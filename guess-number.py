# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
#猜對的話 印出 "出於猜對了!"
#猜錯的話 要告訴他 比答案大/小
import random
start = input('請輸入隨機數字開始範圍值')
end = input('請輸入隨機數字結束範圍值')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:

	num = input('請猜數字:')
	num = int(num)
	count = count +1
	print('你已經猜:',count,'次')

	if num == r:
		print('你猜中了')
		break

	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')