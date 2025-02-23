'''
國字版
'''

import tkinter as tk
import os,sys
import random as rd
from tkinter import messagebox
from functools import partial
from PIL import Image, ImageTk
import mm_saying_random_CH_FL as mm_sayrd


wiN=None #預設 None

def get_image_path(image_name):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, "images", image_name)


def set_main_window(window):
    global wiN
    wiN=window

def _hitsizes():
    
    if wiN is None:
        raise ValueError("主視窗尚未初始化")
    
    wiN11=tk.Toplevel(wiN) #子視窗要用「.Toplevel(Win)」，括弧的(Win)是指主視窗，依據主視窗產生↓↓↓
    #「tk.Toplevel(wiN)」指定給wiN1，也就是子視窗，後續第1個子視窗就是「wiN1」，第二個就是「wiN2」，以此類推
    wiN11.title("")
    wiN11.geometry("800x200+380+130")
    
    #frame4A10_2=tk.Frame(wiN11)
    #frame4A10_2.pack(expand=True)        

    sizes = [4, 5, 6, 7, 8, 9, 10]
    
    
    frame4A10=tk.Frame(wiN11)
    frame4A10.pack(expand=True)      
    
    '''圖片：探索(人)'''
    img=Image.open(get_image_path("explorer_remove bg.png")).resize((60,60))       # 開啟圖片
    frame4A10_img = ImageTk.PhotoImage(img)
    lbLimg = tk.Label(frame4A10,image=frame4A10_img,)
                      #bg="black")
    
    lbLimg.place(relx=0.3, rely=0.2,
                 anchor="e", x=-8, y=0)
    lbLimg.image=frame4A10_img
    
    '''圖片：探索(放大鏡)'''
    img1=Image.open(get_image_path("explorer_1_remove bg.png")).resize((50,50))       # 開啟圖片
    frame4A10_img1 = ImageTk.PhotoImage(img1)
    lbLimg1 = tk.Label(frame4A10,image=frame4A10_img1,)
                       #bg="black")
    
    lbLimg1.place(relx=0.7, rely=0.2,
                 anchor="w", x=7, y=0)
    lbLimg1.image=frame4A10_img1
    
    
    
    lbL4A10_2=tk.Label(frame4A10,
                     text="點擊一個按鈕，探索乘法樂趣！",
                     fg="black",
                     bg="Azure",
                     font=("標楷體",14),
                     relief="ridge", 
                     borderwidth=2,
                     width=30,height=2)
    
    lbL4A10_2.grid(row=0,columnspan=len(sizes),
                   pady=8,
                   ipadx=3,ipady=1)

    for ss, sizeS in enumerate(sizes):
        #ss 是索引，表示當前元素在 sizes 列表中的位置（從 0 開始）。size 是當前元素的值，對應 sizes 列表中的每個元素。
        btN4A10 = tk.Button(frame4A10, 
                            text=f"{sizeS-1} x {sizeS-1}",
                            font=("Arial",14),
                            bg="LightGreen",
                            width=8, height=3,
                            command=lambda S=sizeS,s=sizes:_hits(S,s))
        btN4A10.grid(row=1, column=ss, 
                     padx=5, pady=5)
        
def _hits(sizeS,sizes):
    #global roW1,coL1,entrIes,answErs,btN
    #print(f"選擇了 {sizeS}x{sizeS}")
    wiN12=tk.Toplevel(wiN) # 建立子視窗
    wiN12.title(f"{sizeS-1}格x{sizeS-1}格乘法練習")
    #子視窗標題
    wiN12.geometry(f"{sizeS*100}x{sizeS*75}+200+100") #子視窗尺寸以及每次出現位置
    #wiN12.resizable(width=False, height=False)
#testing

    frameW12=tk.Frame(wiN12)
    frameW12.pack(expand=True) 
    # 隨機生成第 1 列和第 1 欄的數字
    #qq=rd.randint(1,9)
    #roW1 = [rd.sample(range(1,10),sizeS-1) for _ in range(sizeS-1)]
    #coL1 = [rd.sample(range(1,10),sizeS-1) for _ in range(sizeS-1)]
    #roW1 = [rd.randint(1,9) for _ in range(sizeS-1)]
    #coL1 = [rd.randint(1,9) for _ in range(sizeS-1)]
    
    roW1_rd = set()
    while len(roW1_rd)<sizeS-1:
        roW1_rd.add(rd.randint(1,9))        
        roW2=list(roW1_rd)
        rd.shuffle(roW2)
        roW1=roW2
        
    coL1_rd = set()
    while len(coL1_rd)<sizeS-1:
        coL1_rd.add(rd.randint(1,9))
        coL2=list(coL1_rd)
        rd.shuffle(coL2)
        coL1=coL2
    #roW1 = [rd.sample(range(1,10),sizeS-1)]
    #coL1 = [rd.sample(range(1,10),sizeS-1)]

    # 存儲輸入框和正確答案
    entrIes = []
    answErs = []
        
    # 動態生成表格
    for i in range(sizeS):
        for j in range(sizeS):
            if i == 0 and j == 0:  # 左上角空格
                tk.Label(frameW12, text="", 
                         width=8, height=2, 
                         bg=frameW12["bg"]).grid(
                             row=i, column=j)
            elif i == 0:  # 第一列
                tk.Label(frameW12, 
                         text=str(roW1[j-1]),
                         font=("Arial",14), 
                         width=5, height=2, 
                         bg="LightSkyBlue").grid(
                             row=i, column=j,
                             padx=2)
            elif j == 0:  # 第一欄
                tk.Label(frameW12, 
                         text=str(coL1[i-1]),
                         font=("Arial",14), 
                         width=5, height=2, 
                         bg="lightgreen").grid(
                             row=i, column=j,
                             pady=2)
            else:  # 其他格子為輸入框                
                entry = tk.Entry(frameW12, 
                                 width=4,bd=2, 
                                 font=("Arial", 14), 
                                 justify="center")
                entry.grid(row=i, column=j, 
                           padx=1, pady=1,
                           ipadx=4,ipady=9)
                entrIes.append(entry)
                # 計算正確答案並存入
                answErs.append(
                    roW1[j-1] * coL1[i-1])
    
                                
        btN = tk.Button(frameW12, text="送出", 
                        font=("Arial", 12), 
                        width=7,height=2,
                        bg="orange",
                        command=partial(_hitcheck,wiN12,answErs,entrIes,sizeS))
                        
        btN.grid(row=sizeS,columnspan=sizeS,          
                 padx=10,pady=20)
      
        btN1 = tk.Button(frameW12, text="清除", 
                        font=("Arial", 12), 
                        width=7,height=2,
                        bg="LightYellow",
                        command=partial(_hitclean,entrIes))
                      
        btN1.grid(row=sizeS,columnspan=sizeS,
                  padx=10,pady=20,
                  sticky="e")
       
        
def _hitclean(entrIes):
    for entry in entrIes:
        entry.delete(0,"end")        
      
        
        
def _hitcheck(wiN12,answErs,entrIes,sizeS):
    global roW2,coL2
    errors=[] # 用於收集錯誤訊息
       
    try:
        for cc,entry in enumerate(entrIes):
            user_input=int(entry.get()) #取得使用者輸入
            
            # 動態計算行列
            roW2 = cc // (sizeS-1)  # 計算行索引 (0-based)
            coL2 = cc % (sizeS-1)   # 計算列索引 (0-based)
            
            if user_input != answErs[cc]:
                errors.append(f"第 {roW2+1} 列的第 {coL2 +1 } 格答案錯誤!")
                #errors.append(f"第{cc+1}格答案錯誤!") #收集錯誤訊息
                
    except ValueError:
        messagebox.showerror("X","請勿空白，或輸入非數字！")
        return

    # 根據檢查結果顯示提示
    if errors:
        messagebox.showerror("錯誤","\n".join(errors)) # 一次性顯示所有錯誤
    else:
        messagebox.showinfo("",""+mm_sayrd._say())
        if messagebox.askokcancel("提示",f"確定關閉{sizeS-1}格x{sizeS-1}格乘法練習視窗嗎？"):
            wiN12.destroy()
            
        else:
            messagebox.showinfo("","清除答案，重新挑戰！")
            for entry in entrIes:
                entry.delete(0,"end")
    
    
    
    
        
        