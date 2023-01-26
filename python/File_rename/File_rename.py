#功能:將檔案名稱批量轉換
import os #導進需要的套件包絕對是第一步
path='D:/書/Python x Excel VBA x JavaScript/截圖/' #這就是欲進行檔名更改的檔案路徑，路徑的斜線是為/，要留意下！
files=os.listdir(path) # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。它不包括 . 和 .. 即使它在文件夹中。只支持在 Unix, Windows 下使用。
print('files') #印出讀取到的檔名稱，用來確認自己是不是真的有讀到
n=0 #設定初始值

for i in files: #因為資料夾裡面的檔案都要重新更換名稱
	oldname=path+'螢幕擷取畫面 ('+str(346+n)+')'+'.png'#指出檔案現在的路徑名稱，[n]表示第n個檔案
	newname=path+str(n+1)+'.png' 
	print(oldname)
	os.rename(oldname,newname)
	print(oldname)
	print(oldname+'>>>'+newname) #印出原名與更名後的新名，可以進一步的確認每個檔案的新舊對應
	n=n+1 #當有不止一個檔案的時候，依次對每一個檔案進行上面的流程，直到更換完畢就會結束
