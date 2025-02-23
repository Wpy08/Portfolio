'''
2X2、3X3、4X4、5X5_zy版
'''

import tkinter as tk
import os,sys
import random as rd
from functools import partial
from PIL import Image, ImageTk


wiN=None #預設 None

def get_image_path(image_name):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, "images", image_name)

def set_main_window(window):
    global wiN
    wiN=window

def _hitsizes():
    global wiN11    
    if wiN is None:
        raise ValueError("主視窗尚未初始化")
    
    wiN11=tk.Toplevel(wiN)
    wiN11.title("")
    wiN11.geometry("500x200+380+130")

    sizes = [3, 4, 5, 6]
    
    frame3A6=tk.Frame(wiN11)
    frame3A6.pack(expand=True)  
    
    img_choose=Image.open(get_image_path("4_Select a button_remove bg_2.png")).resize((400,45))
    frame3A6_lbL3A6_2=ImageTk.PhotoImage(img_choose)
    lbL3A6_2=tk.Label(frame3A6,image=frame3A6_lbL3A6_2,
                       bg="Azure",
                       relief="ridge", 
                       borderwidth=4,
                       width=400, height=50)
    lbL3A6_2.grid(row=0,columnspan=len(sizes),
                     pady=8,
                     ipadx=3,ipady=1)
    lbL3A6_2.image=frame3A6_lbL3A6_2
     
    
    for ss, sizeS in enumerate(sizes):
        #ss 是索引，表示當前元素在 sizes 列表中的位置（從 0 開始）。size 是當前元素的值，對應 sizes 列表中的每個元素。
        btN2A6 = tk.Button(frame3A6, 
                            text=f"{sizeS-1} x {sizeS-1}",
                            font=("Arial",14),
                            bg="LightGreen",
                            width=8, height=3,
                            command=lambda S=sizeS,s=sizes:_hits(S,s))
        btN2A6.grid(column=ss,row=1,
                     padx=5, pady=5)
        
def _hits(sizeS,sizes):
    global wiN12,entrIes    
    wiN12=tk.Toplevel(wiN)
    wiN12.title("")
    
    wiN12.geometry(f"{sizeS*100}x{sizeS*115}+200+50")

    frameW12=tk.Frame(wiN12)
    frameW12.pack(expand=True)
    
    image_files = {
    3: "2X2_no chinese_remove bg.png",
    4: "3X3_no chinese_remove bg.png",
    5: "4X4_no chinese_remove bg.png",
    6: "5X5_no chinese_remove bg.png"}

    image_file=image_files[sizeS] 
    
    img2A5=Image.open(get_image_path(image_file)).resize((210, 30))
    frameW12_img2A5=ImageTk.PhotoImage(img2A5)

    lbL_img2A5=tk.Label(
        frameW12, image=frameW12_img2A5,
        bg="HoneyDew",
        relief="ridge",
        borderwidth=4,
        width=225, height=40)
    
    lbL_img2A5.grid(row=0, columnspan=sizeS, pady=8, ipadx=3, ipady=1)
    lbL_img2A5.image=frameW12_img2A5 # 防止垃圾回收

    
    '''結果不會重複'''
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


    #存儲輸入框和正確答案
    entrIes = []
    answErs = []
        
    #動態生成表格
    for i in range(sizeS):
        for j in range(sizeS):
            if i == 0 and j == 0:  # 左上角空格
                tk.Label(frameW12, text="", 
                         width=8, height=2, 
                         bg=frameW12["bg"]).grid(
                             row=i+1, column=j)
            elif i == 0:  # 第一列
                tk.Label(frameW12, 
                         text=str(roW1[j-1]),
                         font=("Arial",14), 
                         width=5, height=2, 
                         bg="LightSkyBlue").grid(
                             row=i+1, column=j,
                             padx=2)
            elif j == 0:  # 第一欄
                tk.Label(frameW12, 
                         text=str(coL1[i-1]),
                         font=("Arial",14), 
                         width=5, height=2, 
                         bg="lightgreen").grid(
                             row=i+1, column=j,
                             pady=2)
            else:  # 其他格子為輸入框                
                entry = tk.Entry(frameW12, 
                                 width=4,bd=2, 
                                 font=("Arial", 14), 
                                 justify="center")
                entry.grid(row=i+1,column=j, 
                           padx=1, pady=1,
                           ipadx=4,ipady=9)
                entrIes.append(entry)
                # 計算正確答案並存入
                answErs.append(
                    roW1[j-1] * coL1[i-1])
    
        img_btN=Image.open(get_image_path("1_Check answers_2_remove bg.png")).resize((125,30))
        photo_btN=ImageTk.PhotoImage(img_btN)
        
        btN = tk.Button(frameW12, 
                         image=photo_btN,
                         relief="raised", 
                         borderwidth=3,
                         width=125, height=30,
                         bg="orange",
                         command=partial(_hitcheck,wiN12,answErs,entrIes,sizeS))    
        btN.grid(row=sizeS+1,columnspan=sizeS,
                 pady=6,ipadx=5,ipady=5)
                 
        btN.image=photo_btN
        
       
        img_btN1=Image.open(get_image_path("2_Eraser_remove bg.png")).resize((130,40))
        photo_btN1=ImageTk.PhotoImage(img_btN1)
        
        btN1 = tk.Button(frameW12, 
                         image=photo_btN1,
                         relief="raised", 
                         borderwidth=3,
                         width=130, height=40,
                         bg="LightYellow",
                         command=partial(_hitclean,entrIes))    
        btN1.grid(row=sizeS+2,columnspan=sizeS,
                  pady=2,ipadx=2,ipady=2,)
                  
        btN1.image=photo_btN1
        
        
def _hitclean(entrIes):
    for entry in entrIes:
        entry.delete(0,"end")        
      
        
        
def _hitcheck(wiN12,answErs,entrIes,sizeS):
    global roW2,coL2
    errors=[] # 用於收集錯誤訊息
       
    try:
        for cc,entry in enumerate(entrIes):
            user_input=int(entry.get()) #取得使用者輸入
            
            #動態計算行列
            roW2 = cc // (sizeS-1)  #計算行索引 (0-based)
            coL2 = cc % (sizeS-1)   #計算列索引 (0-based)
            
            if user_input != answErs[cc]:
                errors.append(f"   ㄉ一ˋ {roW2+1} ㄌㄧㄝˋ ， ㄉㄧˋ {coL2 +1 } ㄍㄜˊ ㄉㄚˊ ㄢˋ ㄘㄨㄛˋ ㄨˋ !")
               
    except ValueError:
        zy_wiN1=tk.Toplevel(wiN)
        zy_wiN1.title("")
        zy_wiN1.geometry("550x250+600+200")
        zy_wiN1.configure(bg="white")
        
        zy_frameW1=tk.Frame(zy_wiN1,bg="white")
        zy_frameW1.pack(expand=True)
        
        '''圖片：請勿空白或輸入不是數字的內容喔!'''
        imgdonot_empty=Image.open(get_image_path("don't empty_img_remove bg.png")).resize((430,50)) 
        zyfW1_imgdonot_empty=ImageTk.PhotoImage(imgdonot_empty)
        lbLimgdonot_empty=tk.Label(zy_frameW1,
                                   image=zyfW1_imgdonot_empty,
                                   borderwidth=4,
                                   width=450, height=75)
        
        lbLimgdonot_empty.grid(row=0,column=2,
                               columnspan=2,
                               pady=8,
                               ipadx=3,ipady=1)
        lbLimgdonot_empty.image=zyfW1_imgdonot_empty

        
        '''製作check Button'''
        '''btNcB無法執行，問題是「#command=zy_wiN1.destroy()」'''
        '''command=zy_wiN1.destroy←不要"()"就可以執行了'''
        
        img_cB=Image.open(get_image_path("ok_remove bg.png")).resize((50,50))  
        img_btNcB=ImageTk.PhotoImage(img_cB)

        btNcB=tk.Button(zy_frameW1,
                       image=img_btNcB,
                       bg="white",
                       relief="groove", 
                       borderwidth=5,
                       width=50, height=50,
                       command=zy_wiN1.destroy)
                    

        btNcB.grid(row=1,
                   columnspan=4,
                   pady=15,ipadx=3,ipady=1)
        
        btNcB.image=img_btNcB       
        return

    #根據檢查結果顯示提示
    if errors:       
        '''視窗：第幾列第幾格錯誤!'''
        
        zy_wiN2=tk.Toplevel(wiN)
        zy_wiN2.title("")
        zy_wiN2.geometry("700x400+300+200")
        zy_wiN2.configure(bg="white")
        zy_wiN2.resizable(width=False, height=False)
        zy_frameW3=tk.Frame(zy_wiN2,bg="MediumTurquoise",
                            width=700, height=140)
        zy_frameW3.pack(fill="x")
        
        '''圖片：Cue_remove bg'''
        imgCue = Image.open(get_image_path("Cue_remove bg.png")).resize((105,35))
        zy_frameW3_imgCue = ImageTk.PhotoImage(imgCue)
        lbL_imgCue = tk.Label(zy_frameW3,
                              image=zy_frameW3_imgCue,
                              bg="MintCream",
                              relief="solid",
                              borderwidth=2,
                              width=120,height=40)
                          
        lbL_imgCue.place(relx=0.1, rely=0.3, 
                   anchor="center",
                   x=20, y=2)
        
        lbL_imgCue.image=zy_frameW3_imgCue
        
        '''圖片：Count from top to bottom_remove bg'''
        imgLtoR = Image.open(get_image_path("Count from top to bottom_remove bg.png")).resize((200,40))
        zy_frameW3_imgLtoR = ImageTk.PhotoImage(imgLtoR)
        lbL_imgLtoR = tk.Label(zy_frameW3,
                              image=zy_frameW3_imgLtoR,
                              bg="MintCream",
                              relief="groove",
                              borderwidth=2,
                              width=210,height=40)
                          
        lbL_imgLtoR.place(relx=0.09, rely=0.3,
                          anchor="center",
                          x=60, y=68)
        
        lbL_imgLtoR.image=zy_frameW3_imgLtoR

        '''圖片：Count from left to right_remove bg'''
        imgTtoB = Image.open(get_image_path("Count from left to right_remove bg.png")).resize((200,40))
        zy_frameW3_imgTtoB = ImageTk.PhotoImage(imgTtoB)
        lbL_imgTtoB = tk.Label(zy_frameW3,
                              image=zy_frameW3_imgTtoB,
                              bg="MintCream",
                              relief="groove",
                              borderwidth=2,
                              width=210,height=40)
                          
        lbL_imgTtoB.place(relx=0.43, rely=0.3,
                          anchor="center",
                          x=50, y=68)
        
        lbL_imgTtoB.image=zy_frameW3_imgTtoB

        '''OK=離開鈕'''
        img_OK=Image.open(get_image_path("ok_remove bg.png")).resize((50,50))  
        img_btNOK=ImageTk.PhotoImage(img_OK)

        btNOK=tk.Button(zy_frameW3,
                       image=img_btNOK,
                       bg="white",
                       relief="groove", 
                       borderwidth=5,
                       width=50, height=50,
                       command=zy_wiN2.destroy)
                   

        btNOK.place(relx=0.8, rely=0.5,
                    anchor="center")
        
        btNOK.image=img_btNOK

        
        zy_frameW2=tk.Frame(zy_wiN2,bg="MediumTurquoise")
        zy_frameW2.pack(expand=True,
                        fill="both")
        
        # 滾動條，用於文字框 # Scrollbar for the text box
        sBar_zyw2 = tk.Scrollbar(zy_frameW2, orient="vertical") # 建立垂直滾動條
        sBar_zyw2.pack(side=tk.RIGHT, fill="y")  # 將滾動條附加在右側 # Attach scrollbar to the right side
                    
        # zy_frameW2 裡面的文字框 # Text box inside zy_frameW2
        texT_zy_frameW2= tk.Text(zy_frameW2,
                                    bg="#F0FFF0",
                                    wrap=tk.WORD, # 自動換行以單字為單位
                                    font=("標楷體", 14), 
                                    yscrollcommand=sBar_zyw2.set)  
                                    # 將文字框與滾動條連結 # Link Text box to scrollbar)
                               
        texT_zy_frameW2.pack()
                              
        
        # 將滾動條連結到文字框 # Link scrollbar to Text box
        sBar_zyw2.config(command=texT_zy_frameW2.yview)
        
        # 將錯誤訊息組合成單一字串，並以分隔線區隔
        errors_text="\n  -----------------------------------------------------------------\n".join(errors)
        texT_zy_frameW2.insert(tk.END,f"\n{errors_text}\n")
        texT_zy_frameW2.config(state="disabled")
        
        
    else:
        '''視窗：全部正確顯示'''
        global zy_wiN4
        zy_wiN4=tk.Toplevel(wiN)
        zy_wiN4.title("")
        zy_wiN4.geometry("550x270+550+200")
        zy_wiN4.configure(bg="OldLace")
        
        zy_frameW4=tk.Frame(zy_wiN4,
                            bg="OldLace")
        zy_frameW4.pack(expand=True)


        image_files2 = {
            1: "V1_remove bg.png",
            2: "V2_remove bg.png",
            3: "V3_remove bg.png",
            4: "V4_remove bg.png",
            5: "V5_remove bg.png",
            6: "V6_remove bg.png",
            7: "V7_remove bg.png",
            8: "V8_remove bg.png",
            9: "V9_remove bg.png",
            10: "V10_remove bg.png",
            11: "V11_remove bg.png",
            12: "V12_remove bg.png",
            13: "V13_remove bg.png",
            14: "V14_remove bg.png",
            15: "V15_remove bg.png",
            16: "V16_remove bg.png",
            17: "V17_remove bg.png",
            18: "V18_remove bg.png",
            19: "V19_remove bg.png",
            20: "V20_remove bg.png",
            21: "V21_remove bg.png",
            22: "V22_remove bg.png",
            23: "V23_remove bg.png",
            24: "V24_remove bg.png",
            25: "V25_remove bg.png",
            26: "V26_remove bg.png"}
        
        random_key=rd.randint(1,len(image_files2))
        image_file2=image_files2[random_key]
     
        img_good=Image.open(get_image_path(image_file2)).resize((70,70))
        zy_frameW4_img_good=ImageTk.PhotoImage(img_good)

        lbL_img_good=tk.Label(
            zy_frameW4, image=zy_frameW4_img_good,
            bg="OldLace",
            width=70, height=70)
        
        lbL_img_good.grid(row=0,
                          column=0,
                          pady=8,
                          ipadx=3,
                          ipady=1)
        lbL_img_good.image=zy_frameW4_img_good # 防止垃圾回收
        
        
        image_files3 = {
        1: "good1_All correct_remove bg.png",
        2: "good2_All answers are correct_remove bg.png",
        3: "good3_En_Bingo_remove bg.png",
        4: "good4_You are excellent!_remove bg.png",
        5: "good5_Completely correct_remove bg.png",
        6: "good6_You got it right!_remove bg.png"}
        
        random_key1=rd.randint(1,len(image_files3))
        image_file3=image_files3[random_key1]
        
        img_good1=Image.open(get_image_path(image_file3)).resize((180,40))
        zy_frameW4_img_good1=ImageTk.PhotoImage(img_good1)

        lbL_img_good1=tk.Label(
            zy_frameW4, image=zy_frameW4_img_good1,
            bg="OldLace",
            width=200, height=50)
        
        lbL_img_good1.grid(row=0,
                           column=1,
                           pady=8,
                           ipady=1)
        lbL_img_good1.image=zy_frameW4_img_good1 # 防止垃圾回收
        
        image_files4 = {
        1: "good71_Awesome!_remove bg.png",
        2: "good71_You are amazing!_remove bg.png",
        3: "good71_So impressive_remove bg.png",
        4: "good71_So smart!_remove bg.png",
        5: "good71_Super amazing!_remove bg.png",
        6: "good71_You are a genius!_remove bg.png"}
        
        random_key2=rd.randint(1,len(image_files4))
        image_file4=image_files4[random_key2]
 
        img_good2=Image.open(get_image_path(image_file4)).resize((180,40))
        zy_frameW4_img_good2=ImageTk.PhotoImage(img_good2)

        lbL_img_good2=tk.Label(
            zy_frameW4, image=zy_frameW4_img_good2,
            bg="OldLace",
            width=200, height=50)
        
        lbL_img_good2.grid(row=0,
                           column=2,
                           pady=8,
                           ipady=1)
        lbL_img_good2.image=zy_frameW4_img_good2 # 防止垃圾回收
        
        
        
        '''稱讚的OK鈕'''
                
        img_cB=Image.open(get_image_path("ok_remove bg.png")).resize((50,50))  
        img_btNcB=ImageTk.PhotoImage(img_cB)

        btNcB=tk.Button(zy_frameW4,
                       image=img_btNcB,
                       bg="white",
                       relief="groove", 
                       borderwidth=5,
                       width=50, height=50,
                       command=partial(_hit_clearnAclose,zy_wiN4))
                

        btNcB.grid(row=1,
                   columnspan=4,
                   pady=15,ipadx=3,ipady=1)
        
        btNcB.image=img_btNcB  
        
def _hit_clearnAclose(zy_wiN4):   
        global zy_wiN5
                
        zy_wiN5=tk.Toplevel(wiN)
        zy_wiN5.title("")
        zy_wiN5.geometry("500x300+550+200")
        zy_wiN5.configure(bg="white")
        
        zy_frameW5=tk.Frame(zy_wiN5,bg="white")
        zy_frameW5.pack(expand=True)    
        
        '''視窗：關閉乘法練習的視窗嗎？'''
        imgclosE = Image.open(get_image_path("Are you sure close window_remove bg.png")).resize((350,60))
        zy_frameW5_imgclosE = ImageTk.PhotoImage(imgclosE)
        lbL_imgclosE = tk.Label(zy_frameW5,
                              image=zy_frameW5_imgclosE,
                              bg="white",
                              width=400,height=60)
                          
        lbL_imgclosE.grid(row=0,
                   columnspan=4, 
                   pady=15,ipadx=3,ipady=1)
        
        lbL_imgclosE.image=zy_frameW5_imgclosE

        '''確定鈕'''
        img_CB1=Image.open(get_image_path("Confirm Button_1_remove bg.png")).resize((70,60))  
        img_CB1=ImageTk.PhotoImage(img_CB1)

        btNCB1=tk.Button(zy_frameW5,
                       image=img_CB1,
                       bg="white",
                       relief="groove", 
                       borderwidth=3,
                       width=70, height=70,
                       command=lambda:(
                           wiN12.destroy(),
                           zy_wiN4.destroy(),
                           zy_wiN5.destroy()))
        
        btNCB1.grid(row=1,
                    column=1,
                    padx=10,pady=15,
                    ipadx=1,ipady=1)
        
        btNCB1.image=img_CB1
        
        '''取消鈕'''
        img_canceL=Image.open(get_image_path("Cancel Button_remove bg.png")).resize((70,60))  
        img_canceL=ImageTk.PhotoImage(img_canceL)

        btNcanceL=tk.Button(zy_frameW5,
                       image=img_canceL,
                       bg="white",
                       relief="groove", 
                       borderwidth=3,
                       width=70, height=70,
                       command=_hit_clAcl)
        
        
        btNcanceL.grid(row=1,
                       column=2,
                       padx=10,pady=15,
                       ipadx=1,ipady=1)
        
        btNcanceL.image=img_canceL

'''清除答案，在挑戰一次？'''
def _hit_clAcl(): #命名：Clear the answers and try the challenge again?
    
    zy_wiN6=tk.Toplevel(wiN)
    zy_wiN6.title("")
    zy_wiN6.geometry("500x300+550+200")
    zy_wiN6.configure(bg="white")
    
    zy_frameW6=tk.Frame(zy_wiN6,bg="white")
    zy_frameW6.pack(expand=True)    
    
    '''視窗：清除答案，在挑戰一次？'''
    imgclAcl = Image.open(get_image_path("Clear answers and challenge again_remove bg.png")).resize((350,60))
    zy_frameW6_imgclAcl = ImageTk.PhotoImage(imgclAcl)
    lbL_imgclAcl = tk.Label(zy_frameW6,
                          image=zy_frameW6_imgclAcl,
                          bg="white",
                          width=400,height=60)
                      
    lbL_imgclAcl.grid(row=0,
               columnspan=4,
               pady=15,ipadx=3,ipady=1)
    
    lbL_imgclAcl.image=zy_frameW6_imgclAcl
    
    '''確定鈕'''
    img_CB2=Image.open(get_image_path("Confirm Button_1_remove bg.png")).resize((70,60))  
    img_CB2=ImageTk.PhotoImage(img_CB2)
    
    btNCB2=tk.Button(zy_frameW6,
                   image=img_CB2,
                   bg="white",
                   relief="groove", 
                   borderwidth=3,
                   width=70, height=70,
                   command=lambda:(
                       _hitclean(entrIes),
                       zy_wiN4.destroy(),
                       zy_wiN5.destroy(),
                       zy_wiN6.destroy()))

    btNCB2.grid(row=1,
                columnspan=5,
                padx=10,pady=15,
                ipadx=1,ipady=1)
    
    btNCB2.image=img_CB2
    
