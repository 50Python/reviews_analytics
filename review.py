#reviews_anaytics

data = [] #建立清單庫
count = 0 #建立變數  count 且值為 0
with open('reviews.txt', 'r') as f: #讀取 reviews.txt 這個檔案到變數 f
	for line in f: # 從變數f 裡面一次讀取一行資料 (一筆) 放到 line 裡面, (line變數是隨便取的名字)
		data.append(line) # 將讀出的每串資料放到 data 這個清單庫裡面
		count += 1 # count += 1 == count = count + 1 的簡寫
		if count % 500000 == 0: # %是用來求餘數的 exp: 10 % 6 = 4
			print(len(data)) # len = lenth 長度的語法 , 印出 data 這個清單庫所有的資料筆數

print('檔案讀取完畢、總共有', len(data), '筆資料' ) # len(data) 為列出 data 這個清單庫裡面的資料筆數共有多少、 以後面的變數下去看的、如果是單一字串就會計算有幾個單獨的字

#print(data[1]) # 印出清單庫裡面第一筆資料的內容
#print(len(data[1])) # 印出清單庫裡面、第一筆資料的長度

sum_len = 0 # 定義 sum_len 這個變數、 順便宣告起始值為 0
for d in data: # 把 data 裡面的資料一筆一筆讀出來、放到 變數 d 裡面, data 有幾筆資料、就讀幾次
	sum_len += len(d) # sum_len +=  ==  sum_lem + len(d) , 用len 計算每一筆資料的長度、並加總道 sum_len裡面
print('每筆留言平均長度是: ', sum_len / len(data))

sum_len100 = 0 # 創立變數 sum_len100 並宣告值為 0
for d in data: # 把 data 裡面的資料一筆一筆讀出來、放到 變數 d 裡面, data 有幾筆資料、就讀幾次
	if len(d) == 50: # 假如讀取到 d 裡面的字串長度為 50
		sum_len100 += 1 # sum_lem100 這個變數就 +1
		print(d) # 印出字串長度為50的留言

print('留言字串等於50的總數為: ', sum_len100) # 印出字串長度為50的總留言數

#print('字串小於100: ',len(d) )



