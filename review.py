#reviews_anaytics

data = [] #建立清單
count = 0
with open('reviews.txt', 'r') as f: #讀取 reviews 這個檔案到變數 f
	for line in f: # 從變數f 裡面一次讀取一行資料放到 line 裡面
		data.append(line) # 將讀出的每串資料放到 data 這個清單庫裡面
		count += 1
		if count % 10000 == 0: # %是用來求餘數的 exp: 10 % 6 = 4
			print(len(data))
#print(len(data)) # 印出 data 這個清單庫所有的資料筆數

print(data[0])
