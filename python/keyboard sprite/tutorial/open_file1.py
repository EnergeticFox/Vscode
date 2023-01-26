from tkinter import*
import tkinter.filedialog as fd

def openFloder():
    folder_path = fd.askdirectory() # 打開文件
    show_folderPath.delete(0,END) # 清空
    show_folderPath.insert(0,folder_path) # 寫入路徑

root = Tk()
root.title('Demo') # 窗口標題
root.geometry('300x80') # 窗口大小

show_folderPath = Entry(root)
show_folderPath.grid(row=1,column=2)

btn = Button(root,text = '選擇文件' ,command= openFloder) # 設置一個按鈕
btn.grid(row=1,column=1)

root.mainloop()

 