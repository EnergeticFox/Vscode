#Python 入門教學課程
#https://www.youtube.com/watch?v=JLU5oc4_VtA&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=4&ab_channel=%E5%BD%AD%E5%BD%AD%E7%9A%84%E8%AA%B2%E7%A8%8B
#CLASS1
#程式中的註解: 寫給人看的，用來記錄，說明
#撰寫程式檔案:副檔名用 py
# 執行程式:Python 檔案名稱
 
# print("Hello world")

# #CLASS2

# #資料: 程式的基本單位
# #數字
# 3456
# #字串
# "HI"
# #布林值
# True
# False
# #有順序、可動的列表 List 
# [3,4,5]
# Y=["Hello","World"]
# #有順序、不可動的列表Tuple
# (3,4,5)
# ("Hello","World")
# #集合 Set 沒有順序的概念
# {3,4,5}
# {"Hello","World"}
# #字典 Dictionary
# {"apple":"蘋果","dats":"資料"}
# #變數:用來處存資料的自訂名稱
# #變數名稱=資料
# X=3
# print(X)
# X=True
# print(X)
# print(Y)
# #CLASS3

# X=3**3
# print(X)
# X=10/3
# print(X)
# X=10//3
# print(X)
# X=10%3
# print(X)


# S="Hello"*3+"World"
# print(S)

# S="Hello \n World"
# print(S)

# S="""Hello 


# World"""
# print(S)

# print(S[1:4])


# # Class 4
# #有序可動列表List
# grades=[12,62,15,70,90]
# grades[3] =100
# print(grades[3])
# print(grades[1:4])

# grades[1:4] = []
# print(grades)

# length=len(grades)
# print(length)

# grades=grades+[12,33]
# print(grades) 

# data=[[3,4,5],[6,7,8]]
# print(data[0][1])

# print(data)

# data[0][0:2]=[5,5,5]
# print(data)

# #有序不可變動列表
# data=(3,4,5)
# data[0]=5 錯誤: Tuple 的資料不可變動
# print(data)
 
# #class5 集合、字典的基本運算
 
# #集合的運算
# s1={3,4,5}
# print(3 in s1)
# print(10 in s1)
# print(10 not in s1)

# s2={4,5,6,7,9}
# s3=s1&s2 #交集: 取兩個集合中相同的資料
# print(s3)

# s3=s1|s2 #聯集:取兩個集合中的所有資料，但不重複取
# print(s3)

# s3=s1-s2 #差集:從S1中，減去和S2重疊的部分
# print(s3)

# s3=s2-s1 #差集:從S2中，減去和S1重疊的部分
# print(s3)

# s3=s1^s2 #反交集: 取兩個集合中，不重疊的部分
# print(s3)


# s=set("HELLO") #set(字串) 沒有順序 把字串中的字母拆解成集合
# print("H" in s)

# #字典的運算: key-value配對
# dic={"apple":"蘋果","dats":"資料"}
# dic["apple"]="小蘋果"
# print(dic["apple"])

# print("test" not in dic) #判斷 key是否存在

# print(dic)

# del dic["apple"]# 刪除字典中的鍵值對 (key-value pair)
# print(dic)

# dic={x:x*2 for x in [3,4,5]}#從列表的資料產生字典
# print(dic)
 


# #class 6 if 判斷式

# #判斷式
 
# x=input("請輸入數字: ") #取得字串形式的使用者輸入訊息

# x=int(x)
# if x>200:
#     print("大於200")
# elif x>100:
#     print("大於100，小於200")
# else:
#     print("小於等於100")
 
 
# #四則運算
# n1=int(input("請輸入數字一: "))
# n2=int(input("請輸入數字二: "))
# op=input("請輸入運算: +,-,*,/:")

# if op=="+":
#     print(n1+n2)
# elif op=="-":
#     print(n1-n2)
# elif op=="*":
#     print(n1*n2)
# elif op=="/":
#     print(n1/n2)
# else:
#     print("不支援的運算")
 

# #class7 迴圈

# #while 迴圈
 
# #無窮迴圈
# n=1
# while True:
#     print(n)
#     n+=1
 
 
# n=1
# sum=0 #紀錄累加的成果
# while n<=10:
#     sum=sum+n
#     n+=1
# print(sum)
 
 
# for x in[3,5,1]:
#     print(x)
 
 
# for x in'hello':
#     print(x)

# for x in range(5):
#     print(x)

# for x in range(5,10):
#     print(x)
 
# #class 8
 
# sum=0
# for x in range(11):
#     sum=sum+x
# print(sum)
 
 
# n=0
# while n<=5:
#   if n==3:
#     break
#   n+=1
#   print(n)


# n=0
# for x in [0,1,2,3,4]:
#   if x%2==0:
#     continue
#   n+=1
#   print(n)
   
   
# n=1
# while n<5:
#   print('變數n的資料是:',n)
#   n+=1
# else:
#   print(n)
  
  
# for c in 'Hello':
#   print('逐一取得字串中的字元',c)
# else:
#   print(c)
  
# sum=0

# for n in range(11):
#   sum+=n
# else:
#   print(sum)
 

#綜合例題: 找出整數平方根
#輸入9得3
#輸入11得到沒有[整數]平方根

# n=input('輸入一個整數: ')
# n=int(n)

# for i in range(n):
#   if i*i==n:
#     print('整數平方根: ',i)
#     break
# else:
#   print('沒有整數平方根')
  
#class 9 定義並呼叫函式

# #定義函式
# def multiply(n1,n2):
#   print(n1*n2)
# #呼叫函式
# multiply(3,4)
# multiply(9,4)


#定義函式
# def multiply(n1,n2):
#   print(n1*n2)
#   return n1*n2
# #呼叫函式
# value=multiply(5,8)
# print(value)

#函式可用來做程式的包裝:同樣的邏輯可重複利用
# def calculate(n1,n2):
#   sum=0
#   for n in range(n1,n2):
#     sum+=n
#   print(sum)

# calculate(5,9)


#class 10 函式參數詳解

#參數的預設資料
# def power(base,exp=0):#=0預設值為0
#   print(base**exp)
# power(3,2)
# power(9)

#使用參數名稱對應
# def divide(n1,n2):
#   print(n1/n2)
# divide(2,4)
# divide(n2=2,n1=4)

#無限/不定 參數資料

# def avg(*ns): #將參數的資料已Touple的方式處存(不限資料長度)
#   print(ns)
# avg(6,8,10)
# avg(1,4,-1,18)

#算平均數

# def avg(*ns): #將參數的資料已Touple的方式處存(不限資料長度)
#   sum=0
#   for n in ns:
#     sum+=n
#   ans=sum/len(ns)
#   print(ans)
# avg(6,8,10)
# avg(1,4,-1,18)

#class11 python model模組的使用

# #載入sys模組
# import sys

# #使用sys模組
# print(sys.platform)#印出作業系統
# print(sys.maxsize)#印出整數型態的最大值
# print(sys.path)#印出搜尋模組的路徑

# #載入sys模組
# import sys as s

# #使用sys模組
# print(s.platform)#印出作業系統
# print(s.maxsize)#印出整數型態的最大值
# print(s.path)#印出搜尋模組的路徑

#建立geometry  模組載入並使用

# #在geometry  模組中定義幾何運算功能
# def distance(x1,y1,x2,y2):
#   return ((x2-x1)**2+(y2-y1)**2)**0.5
# def slope(x1,y1,x2,y2)
#   return (y2-y1/(x2-x1)):


# import geometry
# result=geometry.distance(1,1,5,5)
# print(result)

# result=geometry.slope(1,2,5,6)
# print(result)

#調整搜尋模組的路徑
# import sys
# print(sys.path) #python 會按照以下路徑搜尋模組，若不再這些路徑中則無法取得

# #新增模組的搜尋路徑

# import sys
# sys.path.append("modules")
# print(sys.path)
# import geometry
# result=geometry.distance(1,1,5,5)
# print(result)

# result=geometry.slope(1,2,5,6)
# print(result)

#class12 封包的使用:  用來整理分類模組程式(在資料夾中建立一__init__.py)
#主程式
#import modules.point
# result =modules.point.slope(1,5)
# print('斜率',result)

# import modules.line as line
# result = line.distance(1,1,3,3)
# print('距離',result)


 #class 13 文字檔案的讀取和儲存

 #儲存檔案
# cl1=open("data.txt",mode="w",encoding="utf-8") # 開啟
# cl1.write("Hellp File \n second line \n 測試中文 \n 好棒棒 \n 5 \n 3\n 9") # 操作
# cl1.close() # 關閉


# with open("data.txt",mode="w", encoding="utf-8") as cl1:
#     cl1.write("Hellp File \n second line \n 測試中文 \n 好棒棒 \n 5 \n 3\n 9 \n 9 \n 9")

#讀取檔案

# cl1=open("data.txt",mode="r",encoding="utf-8") # 開啟
# data=cl1.read()
# print(data)
# cl1.close() # 關閉

# with open("data.txt",mode="r",encoding="utf-8") as cl1:
#     data=cl1.read()
# print(data)

#把檔案中的數字資料，一行一行的讀取出來，並計算總合

# with open("data.txt",mode="w", encoding="utf-8") as cl1:
#     cl1.write("5 \n 3\n 9 \n 9 \n 9")

# sum=0
# with open("data.txt",mode="r",encoding="utf-8") as cl1:
#     for line in cl1: #一行一行的讀取
#         sum+=int(line)

# print(sum)


#使用 JSON 格式讀取、複寫檔案

# import json
# # 從檔案中讀取JSON資料，放入變數data裡面
# with open("config.json", mode="r") as cl1:
#     data=json.load(cl1) 
# print(data) # data 是一個字典資料
# print("name:",data["name"])
# print("version:",data["version"])

# data["name"]="New Name" # 修改變數中的資料
# #把最新的資料複寫回檔案中
# with open("config.json", mode="w") as cl1:
#     json.dump(data,cl1)

# class 14 亂數與統計模組 (數據分析很重要)
#隨機模組
import random
#隨機選取
# data = random.choice([1,5,6,10,20,50,6,40])
# print(data)

# data = random.sample([1,5,6,10,20,50,6,40],3)#隨機選取3筆
# print(data)

#n隨機調換順序
# data=[1,5,8,20]
# random.shuffle(data) #洗牌 
# print(data)

# 隨機取得亂數
# data=random.random() #0~1之間的隨機亂數
# print(data)

# data=random.uniform(5,9) #5~9之間的隨機亂數
# print(data)

#取得常態分配亂數
#平均數100,標準差10,得到的資料多數在90~110之間
# data=random.normalvariate(100,10)
# print(data)

#平均數0,標準差5,得到的資料多數在-5~5之間
# data=random.normalvariate(0,5)
# print(data)

# import random

# num_all = 0         #隨機點總計數器
# num_cir = 0         #隨機點在圓內的計數器
# num_halt = 10000000 #每產生這麼多個隨機點後，計算並打印一次目前的結果

# print("將進行無限計算，請用Ctrl_C或其他方式強制退出！ ！ ！")
# input("按回車(Enter)鍵開始...")
# print("開始計算...，退出請用Ctrl_C或其他強制退出方式...")
# print("\n實驗次數        計算結果")

# while True :
#     for i in range(num_halt): 
#         x = random.random()         #獲得隨機點的橫坐標
#         y = random.random()         #獲得隨機點的縱坐標
#         if x*x + y*y < 1 :          #隨機點(x,y)在圓內
#             num_cir = num_cir + 1   #圓內計數器+1
#         num_all = num_all + 1       #總計數器+1
#     pi = 4*num_cir/num_all
#     print(num_all,"   ", pi)



#統計模組 平均數、中位數、標準差、常態分配
# import statistics as stat
# data=stat.mean([1,2,3,4,5,8,100])#取得列表資料的平均數
# print(data)

# data=stat.median([1,2,3,4,5,8,100])#取得列表資料的中位數
# print(data)

# data=stat.stdev([1,2,3,4,5,8,100])#取得列表資料的標準差
# print(data)

#class 15 網路連線，公開資料串接

# import urllib.request as request
# src="http://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8") #取得台灣大學網站的原始碼 (HTML、CSS、JS)
# print(data)
 

 #前往台北市政府的開放式資料平台 data.taipei--> api(讓程式去連線) 

# import urllib.request as request
# import json
# src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
# with request.urlopen(src) as response:
#     data=json.load(response)#利用json模組處理json資料格式
# print(data)
#將公司名稱列表出來
# clist=data["result"]["results"]
# for company in clist:
#     print(company["公司名稱"])
 

 #將公司名稱列表出來

# import urllib.request as request
# import json
# src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
# with request.urlopen(src) as response:
#     data=json.load(response)#利用json模組處理json資料格式
# clist=data["result"]["results"]
# with open("data.txt","w",encoding="utf-8") as file:
#     for company in clist:
#         file.write(company["公司名稱"]+"\n")


#class 16 類別的定義與使用

#定義類別、與類別屬性(封裝在類別中的變數和函式)
# 定義一個類別 IO， 有兩個屬性 supportedSrc 和read
# class IO:
#     supportedSrc=["console","file"]
#     def read(Src):
#         if Src not in IO.supportedSrc:
#             print("Not Supported")
#         else:
#             print("Read from",Src)
 
# #使用類別
# print(IO.supportedSrc)
# IO.read("file")
# IO.read("internet")

#Class 17 實體物件的建立與使用 上 實體屬性

# #Point 實體物件的設計:平面座標上的點
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
# #建立第一個實體物件
# P1=Point(3,4)
# print(P1.x,P1.y)
# #建立第二個實體物件
# P2=Point(5,6)
# print(P2.x,P2.y)

# Fullname 實體物件的設計:分開紀錄姓、名資料的全名
# class Fullname:
#     def __init__(self,first,last):
#         self.first=first
#         self.last=last

# name1=Fullname("C.J.","Chang")
# print(name1.first,name1.last)

# name2=Fullname("T.Y.","Ling")
# print(name2.first,name2.last)


#Class 18 實體物件的建立與使用 下 實體方法

#Point 實體物件的設計； 平面座標上的點
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     #定義實體方法
#     def show(self):
#         print(self.x,self.y)
#     def distance(self,targetX,targetY):
#         return(((self.x-targetX)**2)+((self.y-targetY)**2))**0.5
# P=Point(3,4)
# P.show() #呼叫實體方法/函式
# result=P.distance(0,0) # 計算座標3,4和座標0,0之間的距離
# print(result)
#File 實體物件的設計: 包裝檔案讀取的程式

# class File:
#     def __init__(self,name):
#         self.name=name
#         self.file=None # 尚未開啟檔案: 初期是None
#     def open(self):
#         self.file=open(self.name, mode="r",encoding="utf-8")
#     def read(self):
#         return self.file.read()
# #讀取第一個檔案
# f1=File("data1.txt")
# f1.open()
# data=f1.read()
# print(data)
# #讀取第二個檔案
# f2=File("data2.txt")
# f2.open()
# data=f2.read()
# print(data)

#class 19 網路爬蟲 Web Crawler
#關鍵心法:盡可能地，讓程式模仿一個普通使用者的樣子
#HTML格式資料:使用第三方套件 Beautiful Soup 來做解析
#安裝 Beautiful Soup --> pip install beautifulsoup4

# #抓取 PTT 電影版的網頁原始碼 (HTML)
# import urllib.request as req
# url="https://www.ptt.cc/man/movie/D647/D5E6/D96C/D97E/M.1230993855.A.AC1.html"
# #模仿一個普通使用者的樣子
# #chrom-->開發人員工具/Network/Response Headers
# #建立一個 Request 物件，附加 Request Headers 的資訊
# request=req.Request(url, headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
# })
# with req.urlopen(request) as response:
#     data=response.read().decode("utf-8")
# # print(data)

# #解析原始碼，取得每篇文章的標題
# import bs4
# root=bs4.BeautifulSoup(data, "html.parser")#讓 BeautifulSoup 協助我們解析HTML格式文件
# # print(root.title.string)
# titles=root.find_all("span", class_="f3 push-content")#尋找所有class="title"的div標籤
# # print(titles)

# for title in titles:
#    print(title.string)

#class 20 網路爬蟲 Web Crawler-Cookie
