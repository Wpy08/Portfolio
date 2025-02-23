import tkinter as tk
import os  
import sys  
from tkinter import messagebox
from functools import partial
from PIL import Image, ImageTk
import mm_random_shuffle_CH_second_FL as mm_rdsf_ch


wiN=None #預設 None

# 函式來處理圖片路徑  
def get_image_path(image_name):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, "images", image_name)


def set_main_window(window):
    global wiN
    wiN=window

def _hitwiN_CH():
    global wiN_ch   
    if wiN is None:
        raise ValueError("主視窗尚未初始化")
     
    wiN_ch =tk.Toplevel(wiN)
    wiN_ch.title("乘法魔法師：點亮數字魔法")
    wiN_ch.configure(bg="black") #設背景顏色
    wiN_ch.geometry("450x370+600+300")
        
   
    framewiN=tk.Frame(wiN_ch,bg="black")
    framewiN.pack(expand=True)
    
    #btN1(主視窗，第1個按鈕)
    btN1_ch = tk.Button(framewiN, text="排 序 固 定", 
                     font=("標楷體", 18),
                     bg="DeepSkyBlue", 
                     width=12, height=2,
                     command=_hit11) 
    
    btN1_ch.grid(pady=5)
    
    #btN2(主視窗，第2個按鈕)
    btN2_ch = tk.Button(framewiN, text="排 序 隨 機", 
                     font=("標楷體", 18),
                     bg="DodgerBlue", 
                     width=12, height=2,
                     command=mm_rdsf_ch._hitsizes)
                     
    btN2_ch.grid(pady=5)
    
    btN3_ch=tk.Button(wiN_ch,text="說明",
                   font=("標楷體", 16),
                   bg="MistyRose",
                   width=6, height=1,
                   command=_hitDr)
    
    btN3_ch.place(relx=1.0, rely=0.0, 
               anchor="ne", x=-30, y=30)
    '''圖片：星星'''   
    img1 = Image.open(get_image_path("3 stars_Remove bg.png")).resize((100,100))       # 開啟圖片
    wiN_img = ImageTk.PhotoImage(img1)
    lbLimg1 = tk.Label(wiN_ch,
                       image=wiN_img,
                       bg="black")
    
    lbLimg1.place(relx=0.0, rely=0.0, 
               anchor="nw", x=15, y=18)

    '''圖片：魔術帽'''
    img2 = Image.open(get_image_path("magic-trick_Remove bg.png")).resize((100,100))       # 開啟圖片
    wiN_img2 = ImageTk.PhotoImage(img2)
    lbLimg2 = tk.Label(wiN_ch,image=wiN_img2,
                       bg="black")
                      
    lbLimg2.place(relx=1.0, rely=1.0, 
               anchor="se",
               x=-20, y=-10)
    
    lbLimg1.image = wiN_img
    
    lbLimg2.image = wiN_img2


'''第1個子視窗的def'''
#第1個主視窗，第1個子視窗，所以命名「11」
def _hit11():
    
    wiN1=tk.Toplevel(wiN) #子視窗要用「.Toplevel(Win)」，括弧的(Win)是指主視窗，依據主視窗產生↓↓↓
    #「tk.Toplevel(wiN)」指定給wiN1，也就是子視窗，後續第1個子視窗就是「wiN1」，第二個就是「wiN2」，以此類推
    wiN1.title("")
    wiN1.geometry("350x580+300+150")
    wiN1.configure(bg='white')
    
    frame1xA9x=tk.Frame(wiN1,bg='white')
    frame1xA9x.pack(expand=True)
     
    lbL11= tk.Label(frame1xA9x,
                    text="挑戰 / 練習 1-9",
                    fg="black",
                    bg="#FFFACD",                    
                    font=("Arial",14),
                    relief="ridge", 
                    borderwidth=5,
                    width=14, height=3)

    lbL11.grid(pady=4)
    
    
    '''1 X 1-9的 Button'''
    btN1x = tk.Button(frame1xA9x, 
                     text="1 X 1-9", 
                     font=("Arial", 12), 
                     width=10, height=2,
                     command= _hit1121x)    
    btN1x.grid(pady=2)
    
    '''2 X 1-9的 Button'''
    btN2x = tk.Button(frame1xA9x, 
                     text="2 X 1-9", 
                     font=("Arial", 12), 
                     width=10, height=2,
                     command= _hit1132x)    
    btN2x.grid(pady=2)
    
    '''3 X 1-9的 Button'''
    btN3x = tk.Button(frame1xA9x, 
                     text="3 X 1-9", 
                     font=("Arial", 12), 
                     width=10, height=2,
                     command= _hit1143x)    
    btN3x.grid(pady=2)
    
    '''4 X 1-9的 Button'''
    btN4x = tk.Button(frame1xA9x, 
                     text="4 X 1-9", 
                     font=("Arial", 12), 
                     width=10, height=2,
                     command= _hit1154x)    
    btN4x.grid(pady=2)
    
    '''5 X 1-9的 Button'''
    btN5x = tk.Button(frame1xA9x, 
                     text="5 X 1-9", 
                     font=("Arial", 12), 
                     width=10, height=2,
                     command= _hit1165x)    
    btN5x.grid(pady=2)
    
    '''6 X 1-9的 Button'''
    btN6x = tk.Button(frame1xA9x, 
                     text="6 X 1-9", 
                     font=("Arial", 12), 
                     width=10, height=2,
                     command= _hit1176x)    
    btN6x.grid(pady=2)
    
    '''7 X 1-9的 Button'''
    btN7x = tk.Button(frame1xA9x, 
                     text="7 X 1-9", 
                     font=("Arial", 12), 
                     width=10, height=2,
                     command= _hit1187x)    
    btN7x.grid(pady=2)
    
    '''8 X 1-9的 Button'''
    btN8x = tk.Button(frame1xA9x, 
                     text="8 X 1-9", 
                     font=("Arial", 12), 
                     width=10, height=2,
                     command= _hit1198x)    
    btN8x.grid(pady=2)
    
    '''9 X 1-9的 Button'''
    btN9x = tk.Button(frame1xA9x, 
                     text="9 X 1-9", 
                     font=("Arial", 12), 
                     width=10, height=2,
                     command= _hit11109x)    
    btN9x.grid(pady=2)
    
    
    
'''1x的def'''
'''第1個主視窗，第1個子視窗，第2個子視窗，1的乘法→1x，命名1121x'''

def _hit1121x():
    global entrIes1x,answErs1x,btN1xs
    wiN2=tk.Toplevel(wiN)
    wiN2.title("1 X 1-9")
    wiN2.geometry("225x525+200+200")
    
    frame1121x=tk.Frame(wiN2)
    frame1121x.pack()
    
    entrIes1x=[]
    answErs1x=[1,2,3,4,5,6,7,8,9]
    
    for n1x in range(1,10):
        lbL=tk.Label(frame1121x,text=f"1 X {n1x} =",
                     fg="black",bg="Salmon",
                     font=("Arial",12),
                     width=10,height=2)
        lbL.grid(row=n1x-1,column=0)
        
        entrY=tk.Entry(frame1121x,font=("Arial",14),
                       width=3,bd=2,justify="center")
        entrY.grid(row=n1x-1,column=1,padx=3,pady=3,
                   ipadx=6,ipady=8)
        entrIes1x.append((entrY,answErs1x[n1x-1]))
        
        
    '''comfirm Button 1X1-9'''
    btN1xs=tk.Button(frame1121x,text="送出",
                     font=("Arial",12),
                     width=8,height=2,
                     command=partial(_hit1xs, wiN2))
    btN1xs.grid(row=9,column=0,columnspan=2,pady=4)
    
    
def _hit1xs(wiN2):
    errorS1x=[]
    try:
        for n1x,(entry,answErs1x) in enumerate(entrIes1x):
            if int(entry.get()) != answErs1x:
                errorS1x.append(f" 1 X {n1x + 1} 答案錯誤!")
            
        if errorS1x:    
            messagebox.showerror("錯誤","\n".join(errorS1x))
            return
        messagebox.showinfo("提示","超厲害！都答對了")
        
        if messagebox.askokcancel("提示","確定關閉乘法 1 的視窗嗎？"):
            wiN2.destroy() #「wiN.destroy()」可以將視窗關掉
        
        else:
            messagebox.showinfo("","乘法 1 清除，重新挑戰？")
            for entry,_ in entrIes1x:
                entry.delete(0,"end")
        
            
    except ValueError:
        messagebox.showerror("提示","請勿輸入非數字 或 空白")


'''2x的def'''   
'''第1個主視窗，第1個子視窗，第3個子視窗，2的乘法→2x，命名1122x'''

def _hit1132x():

    global entrIes2x,answErs2x,btN2xs
    wiN3=tk.Toplevel(wiN)
    wiN3.title("2 X 2-9")
    wiN3.geometry("225x525+200+200")
    
    frame1132x=tk.Frame(wiN3)
    frame1132x.pack()
    
    entrIes2x=[]
    answErs2x=[2,4,6,8,10,12,14,16,18]
    
    for n2x in range(1,10):
        lbL=tk.Label(frame1132x,text=f"2 X {n2x} =",
                     fg="black",bg="Salmon",
                     font=("Arial",12),
                     width=10,height=2)
        lbL.grid(row=n2x-1,column=0)
        
        entrY=tk.Entry(frame1132x,font=("Arial",14),
                       width=3,bd=2,justify="center")
        entrY.grid(row=n2x-1,column=1,padx=3,pady=3,
                   ipadx=6,ipady=8)
        entrIes2x.append((entrY,answErs2x[n2x-1]))
        
    '''comfirm Button 2X1-9'''

    btN2xs=tk.Button(frame1132x,text="送出",
                     font=("Arial",12),
                     width=8,height=2,
                     command=partial(_hit2xs, wiN3))
    btN2xs.grid(row=9,column=0,columnspan=2,pady=4)
    
    
def _hit2xs(wiN3):
    errorS2x=[]
    try:        
        for n2x,(entry,answErs2x) in enumerate(entrIes2x):
            if int(entry.get()) != answErs2x:            
                errorS2x.append(f" 2 X {n2x + 1} 答案錯誤!")
            
        if errorS2x:    
            messagebox.showerror("錯誤","\n".join(errorS2x))
            return        
        messagebox.showinfo("提示","太厲害了！回答完全正確！")
        
        if messagebox.askokcancel("提示","確定關閉乘法 2 的視窗嗎？"):
            wiN3.destroy() 
        
        else:
            messagebox.showinfo("","乘法 2 清除，重新挑戰？")
            for entry,_ in entrIes2x:
                entry.delete(0,"end")
                
    except ValueError:
        messagebox.showerror("提示","請勿輸入非數字 或 空白")

'''3x的def'''
'''第1個主視窗，第1個子視窗，第4個子視窗，3的乘法→3x，命名1143x'''
def _hit1143x():

    global entrIes3x,answErs3x,btN3xs
    wiN4=tk.Toplevel(wiN)
    wiN4.title("3 X 1-9")
    wiN4.geometry("225x525+200+200")
    
    frame1143x=tk.Frame(wiN4)
    frame1143x.pack()
    
    entrIes3x=[]
    answErs3x=[3,6,9,12,15,18,21,24,27]
    
    for n3x in range(1,10):
        lbL=tk.Label(frame1143x,text=f"3 X {n3x} =",
                     fg="black",bg="Salmon",
                     font=("Arial",12),
                     width=10,height=2)
        lbL.grid(row=n3x-1,column=0)
        
        entrY=tk.Entry(frame1143x,font=("Arial",14),
                       width=3,bd=2,justify="center")
        entrY.grid(row=n3x-1,column=1,padx=3,pady=3,
                   ipadx=6,ipady=8)
        entrIes3x.append((entrY,answErs3x[n3x-1]))
        
    '''comfirm Button 3 X 1-9'''

    btN3xs=tk.Button(frame1143x,text="送出",
                     font=("Arial",12),
                     width=8,height=2,
                     command=partial(_hit3xs, wiN4))
    btN3xs.grid(row=9,column=0,columnspan=2,pady=4)
    
    
def _hit3xs(wiN4):
    errorS3x=[]
    try:        
        for n3x,(entry,answErs3x) in enumerate(entrIes3x):
            if int(entry.get()) != answErs3x:
                errorS3x.append(f" 3 X {n3x + 1} 答案錯誤!")
            
        if errorS3x:    
            messagebox.showerror("錯誤","\n".join(errorS3x))
            return           
        messagebox.showinfo("提示","好棒！完全沒錯！")
        
        if messagebox.askokcancel("提示","確定關閉乘法 3 的視窗嗎？"):
            wiN4.destroy() 
        
        else:
            messagebox.showinfo("","乘法 3 清除，重新挑戰？")
            for entry,_ in entrIes3x:
                entry.delete(0,"end")
                
    except ValueError:
        messagebox.showerror("提示","請勿輸入非數字 或 空白")

'''4x的def'''
'''第1個主視窗，第1個子視窗，第5個子視窗，4的乘法→4x，命名1154x'''
def _hit1154x():

    global entrIes4x,answErs4x,btN4xs
    wiN5=tk.Toplevel(wiN)
    wiN5.title("4 X 1-9")
    wiN5.geometry("225x525+200+200")
    
    frame1154x=tk.Frame(wiN5)
    frame1154x.pack()
    
    entrIes4x=[]
    answErs4x=[4,8,12,16,20,24,28,32,36]
    
    for n4x in range(1,10):
        lbL=tk.Label(frame1154x,text=f"4 X {n4x} =",
                     fg="black",bg="Salmon",
                     font=("Arial",12),
                     width=10,height=2)
        lbL.grid(row=n4x-1,column=0)
        
        entrY=tk.Entry(frame1154x,font=("Arial",14),
                       width=3,bd=2,justify="center")
        entrY.grid(row=n4x-1,column=1,padx=3,pady=3,
                   ipadx=6,ipady=8)
        entrIes4x.append((entrY,answErs4x[n4x-1]))
        
    '''comfirm Button 4 X 1-9'''

    btN4xs=tk.Button(frame1154x,text="送出",
                     font=("Arial",12),
                     width=8,height=2,
                     command=partial(_hit4xs, wiN5))
    btN4xs.grid(row=9,column=0,columnspan=2,pady=4)
    
    
def _hit4xs(wiN5):
    errorS4x=[]
    try:        
        for n4x,(entry,answErs4x) in enumerate(entrIes4x):
            if int(entry.get()) != answErs4x:
                errorS4x.append(f" 4 X {n4x + 1} 答案錯誤!")
            
        if errorS4x:    
            messagebox.showerror("錯誤","\n".join(errorS4x))
            return
        messagebox.showinfo("提示","答對了！你真是太聰明了！")
        
        if messagebox.askokcancel("提示","確定關閉乘法 4 的視窗嗎？"):
            wiN5.destroy() 
        
        else:
            messagebox.showinfo("","乘法 4 清除，重新挑戰？")
            for entry,_ in entrIes4x:
                entry.delete(0,"end")
                
    except ValueError:
        messagebox.showerror("提示","請勿輸入非數字 或 空白")

'''5x的def'''
'''第1個主視窗，第1個子視窗，第6個子視窗，5的乘法→5x，命名1165x'''
def _hit1165x():

    global entrIes5x,answErs5x,btN5xs
    wiN6=tk.Toplevel(wiN)
    wiN6.title("5 X 1-9")
    wiN6.geometry("225x525+200+200")
    
    frame1165x=tk.Frame(wiN6)
    frame1165x.pack()
    
    entrIes5x=[]
    answErs5x=[5,10,15,20,25,30,35,40,45]
    
    for n5x in range(1,10):
        lbL=tk.Label(frame1165x,text=f"5 X {n5x} =",
                     fg="black",bg="Salmon",
                     font=("Arial",12),
                     width=10,height=2)
        lbL.grid(row=n5x-1,column=0)
        
        entrY=tk.Entry(frame1165x,font=("Arial",14),
                       width=3,bd=2,justify="center")
        entrY.grid(row=n5x-1,column=1,padx=3,pady=3,
                   ipadx=6,ipady=8)
        entrIes5x.append((entrY,answErs5x[n5x-1]))
        
    '''comfirm Button 5 X 1-9'''

    btN5xs=tk.Button(frame1165x,text="送出",
                     font=("Arial",12),
                     width=8,height=2,
                     command=partial(_hit5xs, wiN6))
    btN5xs.grid(row=9,column=0,columnspan=2,pady=4)
    
    
def _hit5xs(wiN6):
    errorS5x=[]
    try:        
        for n5x,(entry,answErs5x) in enumerate(entrIes5x):
            if int(entry.get()) != answErs5x:
                errorS5x.append(f" 5 X {n5x + 1} 答案錯誤!")
            
        if errorS5x:    
            messagebox.showerror("錯誤","\n".join(errorS5x))
            return
        messagebox.showinfo("提示","完美的答案！做得好！")
        
        if messagebox.askokcancel("提示","確定關閉乘法 5 的視窗嗎？"):
            wiN6.destroy() 
        
        else:
            messagebox.showinfo("","乘法 5 清除，重新挑戰？")
            for entry,_ in entrIes5x:
                entry.delete(0,"end")
                
    except ValueError:
        messagebox.showerror("提示","請勿輸入非數字 或 空白")


'''6x的def'''
'''第1個主視窗，第1個子視窗，第7個子視窗，6的乘法→6x，命名1176x'''
def _hit1176x():

    global entrIes6x,answErs6x,btN6xs
    wiN7=tk.Toplevel(wiN)
    wiN7.title("6 X 1-9")
    wiN7.geometry("225x525+200+200")
    
    frame1176x=tk.Frame(wiN7)
    frame1176x.pack()
    
    entrIes6x=[]
    answErs6x=[6,12,18,24,30,36,42,48,54]
    
    for n6x in range(1,10):
        lbL=tk.Label(frame1176x,text=f"6 X {n6x} =",
                     fg="black",bg="Salmon",
                     font=("Arial",12),
                     width=10,height=2)
        lbL.grid(row=n6x-1,column=0)
        
        entrY=tk.Entry(frame1176x,font=("Arial",14),
                       width=3,bd=2,justify="center")
        entrY.grid(row=n6x-1,column=1,padx=3,pady=3,
                   ipadx=6,ipady=8)
        entrIes6x.append((entrY,answErs6x[n6x-1]))
        
    '''comfirm Button 6 X 1-9'''

    btN6xs=tk.Button(frame1176x,text="送出",
                     font=("Arial",12),
                     width=8,height=2,
                     command=partial(_hit76xs, wiN7))
    btN6xs.grid(row=9,column=0,columnspan=2,pady=4)
    
    
def _hit76xs(wiN7):
    errorS6x=[]
    try:        
        for n6x,(entry,answErs6x) in enumerate(entrIes6x):
            if int(entry.get()) != answErs6x:
                errorS6x.append(f" 6 X {n6x + 1} 答案錯誤!")
            
        if errorS6x:    
            messagebox.showerror("錯誤","\n".join(errorS6x))
            return
        messagebox.showinfo("提示","很有幹勁！正確無誤！")
        
        if messagebox.askokcancel("提示","確定關閉乘法 6 的視窗嗎？"):
            wiN7.destroy() 
        
        else:
            messagebox.showinfo("","乘法 6 清除，重新挑戰？")
            for entry,_ in entrIes6x:
                entry.delete(0,"end")
                
    except ValueError:
        messagebox.showerror("提示","請勿輸入非數字 或 空白")
        
'''7x的def'''
'''第1個主視窗，第1個子視窗，第8個子視窗，7的乘法→7x，命名1187x'''
def _hit1187x():

    global entrIes7x,answErs7x,btN7xs
    wiN8=tk.Toplevel(wiN)
    wiN8.title("7 X 1-9")
    wiN8.geometry("225x525+200+200")
    
    frame1187x=tk.Frame(wiN8)
    frame1187x.pack()
    
    entrIes7x=[]
    answErs7x=[7,14,21,28,35,42,49,56,63]
    
    for n7x in range(1,10):
        lbL=tk.Label(frame1187x,text=f"7 X {n7x} =",
                     fg="black",bg="Salmon",
                     font=("Arial",12),
                     width=10,height=2)
        lbL.grid(row=n7x-1,column=0)
        
        entrY=tk.Entry(frame1187x,font=("Arial",14),
                       width=3,bd=2,justify="center")
        entrY.grid(row=n7x-1,column=1,padx=3,pady=3,
                   ipadx=6,ipady=8)
        entrIes7x.append((entrY,answErs7x[n7x-1]))
        
    '''comfirm Button 7 X 1-9'''

    btN7xs=tk.Button(frame1187x,text="送出",
                     font=("Arial",12),
                     width=8,height=2,
                     command=partial(_hit87xs, wiN8))
    btN7xs.grid(row=9,column=0,columnspan=2,pady=4)
    
    
def _hit87xs(wiN8):
    errorS7x=[]
    try:        
        for n7x,(entry,answErs7x) in enumerate(entrIes7x):
            if int(entry.get()) != answErs7x:
                errorS7x.append(f" 7 X {n7x + 1} 答案錯誤!")
            
        if errorS7x:    
            messagebox.showerror("錯誤","\n".join(errorS7x))
            return 
        messagebox.showinfo("提示","正確無誤！這個問題你輕鬆搞定了！")
        if messagebox.askokcancel("提示","確定關閉乘法 7 的視窗嗎？"):
            wiN8.destroy() 
        
        else:
            messagebox.showinfo("","乘法 7 清除，重新挑戰？")
            for entry,_ in entrIes7x:
                entry.delete(0,"end")
                
    except ValueError:
        messagebox.showerror("提示","請勿輸入非數字 或 空白")
             

'''8x的def'''
'''第1個主視窗，第1個子視窗，第9個子視窗，8的乘法→8x，命名1198x'''
def _hit1198x():

    global entrIes8x,answErs8x,btN8xs
    wiN9=tk.Toplevel(wiN)
    wiN9.title("8 X 1-9")
    wiN9.geometry("225x525+200+200")
    
    frame1198x=tk.Frame(wiN9)
    frame1198x.pack()
    
    entrIes8x=[]
    answErs8x=[8,16,24,32,40,48,56,64,72]
    
    for n8x in range(1,10):
        lbL=tk.Label(frame1198x,text=f"8 X {n8x} =",
                     fg="black",bg="Salmon",
                     font=("Arial",12),
                     width=10,height=2)
        lbL.grid(row=n8x-1,column=0)
        
        entrY=tk.Entry(frame1198x,font=("Arial",14),
                       width=3,bd=2,justify="center")
        entrY.grid(row=n8x-1,column=1,padx=3,pady=3,
                   ipadx=6,ipady=8)
        entrIes8x.append((entrY,answErs8x[n8x-1]))
        
    '''comfirm Button 8 X 1-9'''

    btN8xs=tk.Button(frame1198x,text="送出",
                     font=("Arial",12),
                     width=8,height=2,
                     command=partial(_hit98xs, wiN9))
    btN8xs.grid(row=9,column=0,columnspan=2,pady=4)
    
    
def _hit98xs(wiN9):
    errorS8x=[]
    try:        
        for n8x,(entry,answErs8x) in enumerate(entrIes8x):
            if int(entry.get()) != answErs8x:
                errorS8x.append(f" 8 X {n8x + 1} 答案錯誤!")
            
        if errorS8x:    
            messagebox.showerror("錯誤","\n".join(errorS8x))
            return
        messagebox.showinfo("提示","哇！答對了！你真是天才！")
        
        if messagebox.askokcancel("提示","確定關閉乘法 8 的視窗嗎？"):
            wiN9.destroy() 
        
        else:
            messagebox.showinfo("","乘法 8 清除，重新挑戰？")
            for entry,_ in entrIes8x:
                entry.delete(0,"end")
                
    except ValueError:
        messagebox.showerror("提示","請勿輸入非數字 或 空白")
             
'''9x的def'''
'''第1個主視窗，第1個子視窗，第10個子視窗，9的乘法→9x，命名11109x'''
def _hit11109x():

    global entrIes9x,answErs9x,btN9xs
    wiN10=tk.Toplevel(wiN)
    wiN10.title("9 X 1-9")
    wiN10.geometry("225x525+200+200")
    
    frame11109x=tk.Frame(wiN10)
    frame11109x.pack()
    
    entrIes9x=[]
    answErs9x=[9,18,27,36,45,54,63,72,81]
    
    for n9x in range(1,10):
        lbL=tk.Label(frame11109x,text=f"9 X {n9x} =",
                     fg="black",bg="Salmon",
                     font=("Arial",12),
                     width=10,height=2)
        lbL.grid(row=n9x-1,column=0)
        
        entrY=tk.Entry(frame11109x,font=("Arial",14),
                       width=3,bd=2,justify="center")
        entrY.grid(row=n9x-1,column=1,padx=3,pady=3,
                   ipadx=6,ipady=8)
        entrIes9x.append((entrY,answErs9x[n9x-1]))
        
    '''comfirm Button 9 X 1-9'''

    btN9xs=tk.Button(frame11109x,text="送出",
                     font=("Arial",12),
                     width=8,height=2,
                     command=partial(_hit109xs, wiN10))
    btN9xs.grid(row=9,column=0,columnspan=2,pady=4)
    
    
def _hit109xs(wiN10):
    errorS9x=[]
    try:        
        for n9x,(entry,answErs9x) in enumerate(entrIes9x):
            if int(entry.get()) != answErs9x:
                errorS9x.append(f" 9 X {n9x + 1} 答案錯誤!")
            
        if errorS9x:    
            messagebox.showerror("錯誤","\n".join(errorS9x))
            return
        messagebox.showinfo("提示","優秀！完美解答！")
        if messagebox.askokcancel("提示","確定關閉乘法 9 的視窗嗎？"):
            wiN10.destroy() 
        
        else:
            messagebox.showinfo("","乘法 9 清除，重新挑戰？")
            for entry,_ in entrIes9x:
                entry.delete(0,"end")
                
    except ValueError:
        messagebox.showerror("提示","請勿輸入非數字 或 空白")

'''按鈕命名'''
'''
#Description of the rules：用於簡要描述規則的內容。            
按鈕命名：Description的"D"、rules的"r"，
→hitDr
'''
def _hitDr():
    
    wiN13=tk.Toplevel(wiN)
    wiN13.title("~ 歡迎進入數字魔法森林 ~")
    wiN13.geometry("420x400+400+150")
    
       
    sBar=tk.Scrollbar(wiN13)
    sBar.pack(side=tk.RIGHT,fill="y")
              #,ipadx=2, ipady=50)
    
    texTDr = tk.Text(wiN13,bg="#F0FFF0",
                     wrap=tk.WORD,
                     font=("標楷體", 14),
                     yscrollcommand=sBar.set) 
                     # 將 Text 的滾動指令傳給 Scrollbar
                     
    sBar.config(command=texTDr.yview) 
    # 將 Scrollbar 的控制指令傳回 Text
    
        
    texTDr.insert(tk.END,"\n親愛的小魔法師：\n\n"
                  "進入數字魔法森林之前，請先了解規則，\n"
                  "這將幫助你輕輕鬆鬆學好乘法！\n\n")
    texTDr.insert(tk.END,"按鈕")
    texTDr.insert(tk.END,"1:","bold")
    texTDr.insert(tk.END,"排序固定\n","bold")    
    texTDr.insert(tk.END,"指 1 到 9 照順序練習乘法。\n")
    texTDr.insert(tk.END,"點擊第一個按鈕，循序漸進挑戰每個數字，\n"                  
                  "隨著熟練度提升，逐一挑戰每一個數字，讓基礎更扎實！\n\n")
    texTDr.insert(tk.END,"按鈕")
    texTDr.insert(tk.END,"2:","bold")
    texTDr.insert(tk.END,"排序隨機\n","bold")
    texTDr.insert(tk.END,"數字順序會被打亂，挑戰會更有趣！\n")
    texTDr.insert(tk.END,"森林裡有")
    texTDr.insert(tk.END,"有 7 種","bold")
    texTDr.insert(tk.END,"挑戰難度，\n")
    texTDr.insert(tk.END,"從")
    texTDr.insert(tk.END," 3x3 ")
    texTDr.insert(tk.END,"到")
    texTDr.insert(tk.END," 9x9 ")
    texTDr.insert(tk.END,"，考驗你回答的正確度！\n\n")
    texTDr.insert(tk.END,"乘法高手挑戰！\n","bold")
    texTDr.insert(tk.END,"如果你已經很厲害了，\n")
    texTDr.insert(tk.END,"試試隨機排序的高難度模式，\n")
    texTDr.insert(tk.END,"看看你的實力有多強！\n\n\n")

    
    texTDr.insert(tk.END,"你的乘法冒險即將開始，\n")
    texTDr.insert(tk.END,"準備好了嗎？來挑戰吧！\n")
    
   
    texTDr.tag_configure("bold", font=("標楷體", 14, "bold"))
    texTDr.tag_configure("underline", font=("標楷體", 14, "underline"))
    texTDr.tag_configure("arial", font=("Arial", 14))
    texTDr.tag_configure("left_align", justify=tk.LEFT)
    
    texTDr.tag_add("arial", "7.3", "7.4")  # "1."的位置
    texTDr.tag_add("arial", "8.1", "8.3")  # "1"的位置
    texTDr.tag_add("arial", "8.5", "8.7")  # "9"的位置
        
    texTDr.tag_add("arial", "12.3", "12.4")  # "2."的位置
        
    texTDr.tag_add("arial", "14.4", "14.6")  # "7"的位置
    texTDr.tag_add("arial", "15.1", "15.5") # "3x3"的位置
    texTDr.tag_add("arial", "15.7", "15.11")  # "9x9"的位置
    
    texTDr.configure(state=tk.DISABLED)
    
    texTDr.pack(fill=tk.BOTH,expand=True)
    
    


