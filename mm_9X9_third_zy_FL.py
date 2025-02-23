import tkinter as tk
import os,sys
import random as rd
from functools import partial
from PIL import Image, ImageTk
import mm_random_shuffle_zy_FL as mm_rdsf_zy


wiN=None #預設 None

# 函式來處理圖片路徑
def get_image_path(image_name):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, "images", image_name)

def set_main_window(window):
    global wiN
    wiN=window

   
def _hitwiN_zy():
    global wiN_ch   
    if wiN is None:
        raise ValueError("主視窗尚未初始化")
        
    wiN_zy = tk.Toplevel(wiN)
    wiN_zy.title("乘法魔法師：點亮數字魔法")
    wiN_zy.configure(bg="black") 
    wiN_zy.geometry("450x370+600+300") 
    
    
    framewiN=tk.Frame(wiN_zy,bg="black")
    framewiN.pack(expand=True)
    
    
    #btN1(主視窗，第1個按鈕)
    #加載圖片（使用PIL）
    #調整圖片大小
    '''1-9排排隊'''
    img_btN1=Image.open(get_image_path("1-9Line up_zy-remove bg.png")).resize((150,50))  
    wiNzy_btN1=ImageTk.PhotoImage(img_btN1)
    
    # 建立按鈕，將圖片作為背景  
    btN1=tk.Button(framewiN,
                   image=wiNzy_btN1,
                   bg="DeepSkyBlue",
                   width=150, height=50,
                   command=_zy_hit1B) 
    
    btN1.grid(pady=5)
    btN1.image=wiNzy_btN1
    
    #btN2(主視窗，第2個按鈕)
    '''1-9大風吹'''
    img_btN2=Image.open(get_image_path("1-9The Wind Blows_zy-remove bg.png")).resize((150,50))  
    wiNzy_btN2=ImageTk.PhotoImage(img_btN2)
    
    #建立按鈕，將圖片作為背景
    btN2=tk.Button(framewiN,
                   image=wiNzy_btN2,
                   bg="DodgerBlue",
                   width=150, height=50,
                   command=mm_rdsf_zy._hitsizes) 
    
    btN2.grid(pady=5)
    btN2.image=wiNzy_btN2
    
    
    #btN3(主視窗，第3個按鈕)
    '''圖片：說明'''
    img_btN3=Image.open(get_image_path("Explanation_zy-remove bg.png")).resize((70,50))  
    wiNzy_btN3=ImageTk.PhotoImage(img_btN3)
    
    #建立按鈕，將圖片作為背景
    btN3=tk.Button(wiN_zy,
                   image=wiNzy_btN3,
                   bg="MistyRose",
                   width=70, height=50,
                   command=_zy_hitDr) 
    
    btN3.place(relx=1.0, rely=0.0, 
               anchor="ne", x=-30, y=30)
    btN3.image=wiNzy_btN3
    
    '''圖片：流星'''
    img1=Image.open(get_image_path("shooting star_Remove bg.png")).resize((100,100))       # 開啟圖片
    wiNzy_img1 = ImageTk.PhotoImage(img1)
    lbLimg1 = tk.Label(wiN_zy,image=wiNzy_img1,
                       bg="black")
    '''
    #anchor	擺放位置，可以設定 
    n、s、w、e、ne、nw、sw、se、center 
    ( e 右，w 左，s 下，n 上 )，預設 center。                  
    '''
    lbLimg1.place(relx=0.0, rely=0.0, 
               anchor="nw", x=15, y=18)
    lbLimg1.image=wiNzy_img1
    
    '''圖片：魔法帽變兔子'''
    img2 = Image.open(get_image_path("magician_2_Remove bg.png")).resize((100,100))       # 開啟圖片
    wiNzy_img2 = ImageTk.PhotoImage(img2)
    lbLimg2 = tk.Label(wiN_zy,image=wiNzy_img2,
                       bg="black")
                      
    lbLimg2.place(relx=1.0, rely=1.0, 
               anchor="se",
               x=-20, y=-20)
    
    lbLimg2.image = wiNzy_img2
    
    
'''注音版子視窗命名，zy_wiN11開始，frame11開始'''
'''注音版第11個子視窗的def，所以命名「11」'''
'''1x-9x的def'''
'''
第 "1" 個子視窗，所有 "B" utton子視窗，命名 1B
'''

def _zy_hit1B():
    global zy_wiNb
    zy_wiNb = tk.Toplevel(wiN)
    zy_wiNb.title("")
    zy_wiNb.geometry("350x580+300+80")
    zy_wiNb.configure(bg="white")
    
    zy_frame1xA9x = tk.Frame(zy_wiNb,bg="white")
    zy_frame1xA9x.pack(expand=True)
    
    '''圖片："挑戰/練習1-9"'''
    #檔名：3_Challenge and Practice_1-9_remove bg.png
    #命名「cAp」
    img_zyw1cAp = Image.open(get_image_path("3_Challenge and Practice_1-9_remove bg.png")).resize((160, 40))  
    zyw1cAp = ImageTk.PhotoImage(img_zyw1cAp)
    lbL_img_zyw1cAp = tk.Label(zy_frame1xA9x,
                                image=zyw1cAp,
                                bg="#FFFACD",
                                relief="ridge", 
                                borderwidth=4,
                                width=160, height=40)
    lbL_img_zyw1cAp.grid(pady=4, ipadx=10, ipady=8)
    lbL_img_zyw1cAp.image = zyw1cAp
    
    # Button set
    '''1 X 1-9的 Button'''
    zy_btN1x = tk.Button(zy_frame1xA9x, 
                     text="1 X 1-9", 
                     font=("Arial", 12), 
                     width=10, height=2,
                     command= _hit1B111x)    
    zy_btN1x.grid(pady=2)
    
    '''2 X 1-9的 Button'''
    zy_btN2x = tk.Button(zy_frame1xA9x, 
                     text="2 X 1-9", 
                     font=("Arial", 12), 
                     width=10, height=2,
                     command= _hit1B212x)    
    zy_btN2x.grid(pady=2)
    
    '''3 X 1-9的 Button'''
    zy_btN3x = tk.Button(zy_frame1xA9x, 
                     text="3 X 1-9", 
                     font=("Arial", 12), 
                     width=10, height=2,
                     command= _hit1B313x)    
    zy_btN3x.grid(pady=2)
    
    '''4 X 1-9的 Button'''
    zy_btN4x = tk.Button(zy_frame1xA9x, 
                     text="4 X 1-9", 
                     font=("Arial", 12), 
                     width=10, height=2,
                     command= _hit1B414x)    
    zy_btN4x.grid(pady=2)
    
    '''5 X 1-9的 Button'''
    zy_btN5x = tk.Button(zy_frame1xA9x, 
                     text="5 X 1-9", 
                     font=("Arial", 12), 
                     width=10, height=2,
                     command= _hit1B515x)    
    zy_btN5x.grid(pady=2)
    
    '''6 X 1-9的 Button'''
    zy_btN6x = tk.Button(zy_frame1xA9x, 
                     text="6 X 1-9", 
                     font=("Arial", 12), 
                     width=10, height=2,
                     command= _hit1B616x)    
    zy_btN6x.grid(pady=2)
    
    '''7 X 1-9的 Button'''
    zy_btN7x = tk.Button(zy_frame1xA9x, 
                     text="7 X 1-9", 
                     font=("Arial", 12), 
                     width=10, height=2,
                     command= _hit1B717x)    
    zy_btN7x.grid(pady=2)
    
    '''8 X 1-9的 Button'''
    zy_btN8x = tk.Button(zy_frame1xA9x, 
                     text="8 X 1-9", 
                     font=("Arial", 12), 
                     width=10, height=2,
                     command= _hit1B818x)    
    zy_btN8x.grid(pady=2)
    
    '''9 X 1-9的 Button'''
    zy_btN9x = tk.Button(zy_frame1xA9x, 
                     text="9 X 1-9", 
                     font=("Arial", 12), 
                     width=10, height=2,
                     command= _hit1B919x)    
    zy_btN9x.grid(pady=2)
    
'''1x的def'''
'''1x-9x的def'''
'''
第 "1" 個子視窗，所有 "B" utton子視窗，
乘法 1 X1-9的子視窗，從wiN"11"，1的乘法→ "1x" ，命名 1B111x
'''
def _hit1B111x():
    global zy_entrIes1x,zy_answErs1x,zy_btN1xs,zy_wiN11
    zy_wiN11=tk.Toplevel(wiN)
    zy_wiN11.title("1 X 1-9")
    zy_wiN11.geometry("225x525+200+200")
    
    zy_frame1B111x=tk.Frame(zy_wiN11)
    zy_frame1B111x.pack()
    
    zy_entrIes1x=[]
    zy_answErs1x=[1,2,3,4,5,6,7,8,9]
    
    for n1x in range(1,10):
        zy_lbL_1x=tk.Label(zy_frame1B111x,text=f"1 X {n1x} =",
                           fg="black",bg="Salmon",
                           font=("Arial",12),
                           width=10,height=2)
        zy_lbL_1x.grid(row=n1x-1,column=0)
        
        zy_entrY_1x=tk.Entry(zy_frame1B111x,
                             font=("Arial",14),
                             width=3,bd=2,
                             justify="center")
        zy_entrY_1x.grid(row=n1x-1,column=1,
                         padx=3,pady=3,
                         ipadx=6,ipady=8)
        zy_entrIes1x.append((zy_entrY_1x,zy_answErs1x[n1x-1]))
        
        
    '''Check answers Button 1X1-9'''
    '''圖片：對答案'''
    img_btN1xs=Image.open(get_image_path("1_Check answers_2_remove bg.png")).resize((125,30))  
    zyf11_btN1xs=ImageTk.PhotoImage(img_btN1xs)
    
    zy_btN1xs = tk.Button(zy_frame1B111x, 
                     image=zyf11_btN1xs,
                     relief="raised", 
                     borderwidth=3,
                     width=125, height=30,
                     command=partial(_hit1xs, zy_wiN11))    
    zy_btN1xs.grid(row=9,column=0,columnspan=2,pady=6,ipadx=5,ipady=5)
    zy_btN1xs.image=zyf11_btN1xs
    
'''1xs→1的乘法(1x)，送出(send)→1xs'''    
def _hit1xs(zy_wiN11):
    zy_errorS1x=[]
    try:
        for n1x,(zy_entry1x,zy_answErs1x) in enumerate(zy_entrIes1x):
            if int(zy_entry1x.get()) != zy_answErs1x:
                zy_errorS1x.append(f"  1 X { n1x+1 }  ㄉㄚˊ ㄢˋ ㄘㄨㄛˋ ㄨˋ !")
                


    except ValueError:
        global zy_wiN12
        #messagebox.showerror("提示","請勿輸入非數字 或 空白")
        '''視窗：第幾列第幾格錯誤，'''
        zy_wiN12=tk.Toplevel(wiN)
        zy_wiN12.title("")
        zy_wiN12.geometry("550x250+550+200")
        zy_wiN12.configure(bg="white")
        
        zy_frameW12=tk.Frame(zy_wiN12,bg="white")
        zy_frameW12.pack(expand=True)
        
        '''圖片：請勿空白或輸入不是數字的內容喔!'''
        imgdonot_empty1x=Image.open(get_image_path("don't empty_img_remove bg.png")).resize((430,50)) 
        zyfW12_imgdonot_empty1x=ImageTk.PhotoImage(imgdonot_empty1x)
        lbLimgdonot_empty1x=tk.Label(zy_frameW12,
                                     image=zyfW12_imgdonot_empty1x,
                                     
                                     
                                     borderwidth=4,
                                     width=450, height=75)
        
        lbLimgdonot_empty1x.grid(row=0,column=2,
                                 columnspan=2,
                                 pady=8,
                                 ipadx=3,ipady=1)
        lbLimgdonot_empty1x.image=zyfW12_imgdonot_empty1x

        
        '''製作check Button'''
        '''btNcB無法執行，問題是「#command=zy_wiN1.destroy()」'''
        '''command=zy_wiN1.destroy←不要"()"就可以執行了'''
        
        img_cB_1x=Image.open(get_image_path("ok_remove bg.png")).resize((50,50))  
        zyW12_cB_1x=ImageTk.PhotoImage(img_cB_1x)

        btNcB_1x=tk.Button(zy_frameW12,
                            image=zyW12_cB_1x,
                            bg="white",
                            relief="groove",
                            borderwidth=5,
                            width=50, height=50,
                            command=zy_wiN12.destroy)
                    

        btNcB_1x.grid(row=1,
                       columnspan=4,
                       
                       pady=15,ipadx=3,ipady=1)
        
        btNcB_1x.image=zyW12_cB_1x
        return

    if zy_errorS1x:
        '''視窗：第幾列第幾格錯誤!'''
        zy_wiN13=tk.Toplevel(wiN)
        zy_wiN13.title("")
        zy_wiN13.geometry("400x350+450+200")
        zy_wiN13.configure(bg="white")
        zy_wiN13.resizable(width=False, height=False)
        zy_frameW13=tk.Frame(zy_wiN13,
                            bg="MediumTurquoise",
                            height=90)
        
        zy_frameW13.pack(fill="x")
        
        
        '''圖片：Cue1_remove bg'''
        zy_imgCue1x = Image.open(get_image_path("Cue1_remove bg.png")).resize((120,40))
        zy_frameW13_imgCue1x = ImageTk.PhotoImage(zy_imgCue1x)
        zy_lbL_imgCue1x = tk.Label(zy_frameW13,
                                image=zy_frameW13_imgCue1x,
                                bg="MintCream",
                                relief="solid",
                                borderwidth=2,
                                width=124,height=44)
                        
        zy_lbL_imgCue1x.place(relx=0.5, rely=0.5,
                              anchor="center")
        zy_lbL_imgCue1x.image=zy_frameW13_imgCue1x
        
        
        zy_frameW13_1=tk.Frame(zy_wiN13,
                            bg="MediumTurquoise")
        zy_frameW13_1.pack(expand=True,fill="both")
        
        # 滾動條，用於文字框 # Scrollbar for the text box
        sBar_zyw13 = tk.Scrollbar(zy_frameW13_1, orient="vertical") # 建立垂直滾動條
        sBar_zyw13.pack(side=tk.RIGHT, fill="y")  # 將滾動條附加在右側 # Attach scrollbar to the right side
                    
        # zy_frameW7_1 裡面的文字框 # Text box inside zy_frameW7_1
        texT_zy_frameW13_1 = tk.Text(zy_frameW13_1,
                                    bg="#F0FFF0",
                                    wrap=tk.WORD, # 自動換行以單字為單位
                                    font=("標楷體", 14), 
                                    yscrollcommand=sBar_zyw13.set)  
                                    # 將文字框與滾動條連結 # Link Text box to scrollbar)
        texT_zy_frameW13_1.pack()

        
        # 將滾動條連結到文字框 # Link scrollbar to Text box
        sBar_zyw13.config(command=texT_zy_frameW13_1.yview)
        
        # 將錯誤訊息組合成單一字串，並以分隔線區隔
        zy_errorS1x_text = "\n  ----------------------------------\n".join(zy_errorS1x)
        texT_zy_frameW13_1.insert(tk.END,f"\n{zy_errorS1x_text}\n")
        texT_zy_frameW13_1.config(state="disabled")
        # 設定文字框為不可編輯狀態 # Disable editing of the Text box
        
                     
    else:
        '''視窗：全部正確顯示'''
        global zy_wiN14
        zy_wiN14=tk.Toplevel(wiN)
        zy_wiN14.title("")
        zy_wiN14.geometry("550x270+450+200")
        zy_wiN14.configure(bg="SeaShell")
                                  
        zy_frameW14=tk.Frame(zy_wiN14,bg="SeaShell")
                            
        zy_frameW14.pack(expand=True)

        image_files_1x = {
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
        
        random_key_1x=rd.randint(1,len(image_files_1x))
        image_file_1x=image_files_1x[random_key_1x]
                
        img_good1x=Image.open(get_image_path(image_file_1x)).resize((70,70))
        zy_frameW14_img_good1x=ImageTk.PhotoImage(img_good1x)

        lbL_img_good1x=tk.Label(zy_frameW14,
                                image=zy_frameW14_img_good1x,
                                bg="SeaShell",
                                width=70, height=70)
        
        lbL_img_good1x.grid(row=0,
                            column=0,
                            pady=8,
                            ipadx=3,
                            ipady=1)
        lbL_img_good1x.image=zy_frameW14_img_good1x # 防止垃圾回收
        
        
        image_files2_1x = {
        1: "good1_All correct_remove bg.png",
        2: "good2_All answers are correct_remove bg.png",
        3: "good3_En_Bingo_remove bg.png",
        4: "good4_You are excellent!_remove bg.png",
        5: "good5_Completely correct_remove bg.png",
        6: "good6_You got it right!_remove bg.png"}
        
        random_key1_1x=rd.randint(1,len(image_files2_1x))
        image_file2_1x=image_files2_1x[random_key1_1x]
        
        img_good1_1x=Image.open(get_image_path(image_file2_1x)).resize((180,40))
        zy_frameW14_img_good1_1x=ImageTk.PhotoImage(img_good1_1x)

        lbL_img_good1_1x=tk.Label(zy_frameW14,
                                  image=zy_frameW14_img_good1_1x,
                                  bg="SeaShell",                                  
                                  width=200, height=50)
        
        lbL_img_good1_1x.grid(row=0,
                              column=1,                              
                              pady=8,
                              ipady=1)
        lbL_img_good1_1x.image=zy_frameW14_img_good1_1x # 防止垃圾回收
        
        image_files3_1x = {
        1: "good71_Awesome!_remove bg.png",
        2: "good71_You are amazing!_remove bg.png",
        3: "good71_So impressive_remove bg.png",
        4: "good71_So smart!_remove bg.png",
        5: "good71_Super amazing!_remove bg.png",
        6: "good71_You are a genius!_remove bg.png"}
        
        random_key2_1x=rd.randint(1,len(image_files3_1x))
        image_file3_1x=image_files3_1x[random_key2_1x]
                
        img_good2_1x=Image.open(get_image_path(image_file3_1x)).resize((180,40))
        zy_frameW14_img_good2_1x=ImageTk.PhotoImage(img_good2_1x)

        lbL_img_good2_1x=tk.Label(zy_frameW14,
                                  image=zy_frameW14_img_good2_1x,
                                  bg="SeaShell",                                  
                                  width=200, height=50)
        
        lbL_img_good2_1x.grid(row=0,
                              column=2,                              
                              pady=8,
                              ipady=1)
        lbL_img_good2_1x.image=zy_frameW14_img_good2_1x # 防止垃圾回收
        
        '''稱讚的OK鈕'''
                
        img_cB1_1x=Image.open(get_image_path("ok_remove bg.png")).resize((50,50))  
        img_btNcB1_1x=ImageTk.PhotoImage(img_cB1_1x)

        btNcB1_1x=tk.Button(zy_frameW14,
                          image=img_btNcB1_1x,
                          bg="white",
                          relief="groove",
                          borderwidth=5,
                          width=50, height=50,
                          command=partial(_hit_clearnAclose1x,zy_wiN14))

        btNcB1_1x.grid(row=1,
                     columnspan=4,
                     pady=15,
                     ipadx=3,ipady=1)
        btNcB1_1x.image=img_btNcB1_1x
   
        
def _hit_clearnAclose1x(zy_wiN14):   
        global zy_wiN15
        zy_wiN15=tk.Toplevel(wiN)
        zy_wiN15.title("")
        zy_wiN15.geometry("500x300+450+200")
        zy_wiN15.configure(bg="white")
        
        zy_frameW15=tk.Frame(zy_wiN15,bg="white")
        zy_frameW15.pack(expand=True)    
        
        '''視窗：關閉乘法練習的視窗嗎？'''
        imgclosE_1x = Image.open(get_image_path("Are you sure close window_remove bg.png")).resize((350,60))
        zy_frameW15_imgclosE_1x = ImageTk.PhotoImage(imgclosE_1x)
        lbL_imgclosE_1x = tk.Label(zy_frameW15,
                                   image=zy_frameW15_imgclosE_1x,
                                   bg="white",                                   
                                   width=400,height=60)
                          
        lbL_imgclosE_1x.grid(row=0,
                             columnspan=4,                             
                             pady=15,
                             ipadx=3,ipady=1)
        
        lbL_imgclosE_1x.image=zy_frameW15_imgclosE_1x

        '''確定鈕'''
        img_CB2_1x=Image.open(get_image_path("Confirm Button_1_remove bg.png")).resize((70,60))  
        zyfw15_CB2_1x=ImageTk.PhotoImage(img_CB2_1x)

        btNCB2_1x=tk.Button(zy_frameW15,
                            image=zyfw15_CB2_1x,
                            bg="white",
                            relief="groove",
                            borderwidth=3,
                            width=70, height=70,
                            command=lambda:(zy_wiN11.destroy(),
                                            zy_wiN14.destroy(),
                                            zy_wiN15.destroy()))
        
        btNCB2_1x.grid(row=1,
                       column=1,                       
                       padx=10,pady=15,
                       ipadx=1,ipady=1)
        
        btNCB2_1x.image=zyfw15_CB2_1x
        
        
        '''取消鈕'''
        img_canceL1x=Image.open(get_image_path("Cancel Button_remove bg.png")).resize((70,60))  
        zyfw15_canceL1x=ImageTk.PhotoImage(img_canceL1x)

        btNcanceL1x=tk.Button(zy_frameW15,
                            image=zyfw15_canceL1x,
                            bg="white",
                            relief="groove",
                            borderwidth=3,
                            width=70, height=70,
                            command=_hit_clAcl1x)
           
        btNcanceL1x.grid(row=1,
                       column=2,                       
                       padx=10,pady=15,
                       ipadx=1,ipady=1)
        
        btNcanceL1x.image=zyfw15_canceL1x

'''清除答案，在挑戰一次？'''
def _hit_clAcl1x(): #命名：Clear the answers and try the challenge again?
    
    zy_wiN16=tk.Toplevel(wiN)
    zy_wiN16.title("")
    zy_wiN16.geometry("500x300+450+200")
    zy_wiN16.configure(bg="white")
    
    zy_frameW16=tk.Frame(zy_wiN16,bg="white")
    zy_frameW16.pack(expand=True)    
    
    '''圖片：清除答案，在挑戰一次？'''
    imgclAcl_1x = Image.open(get_image_path("Clear answers and challenge again_remove bg.png")).resize((350,60))
    zy_frameW16_imgclAcl_1x = ImageTk.PhotoImage(imgclAcl_1x)
    lbL_imgclAcl_1x = tk.Label(zy_frameW16,
                               image=zy_frameW16_imgclAcl_1x,
                               bg="white",                               
                               width=400,height=60)
                      
    lbL_imgclAcl_1x.grid(row=0,
                         columnspan=4,                         
                         pady=15,
                         ipadx=3,ipady=1)
    
    lbL_imgclAcl_1x.image=zy_frameW16_imgclAcl_1x
    
    '''確定鈕'''
    img_CB3_1x=Image.open(get_image_path("Confirm Button_1_remove bg.png")).resize((70,60))  
    zyW16_CB3_1x=ImageTk.PhotoImage(img_CB3_1x)
    
    btNCB3_1x=tk.Button(zy_frameW16,
                        image=zyW16_CB3_1x,
                        bg="white",
                        relief="groove",
                        borderwidth=3,
                        width=70, height=70,
                        command=lambda:(
                            _hitclean1x(),
                            zy_wiN14.destroy(),
                            zy_wiN15.destroy(),                           
                            zy_wiN16.destroy()))

    btNCB3_1x.grid(row=1,                
                columnspan=5,                
                padx=10,pady=15,
                ipadx=1,ipady=1)
    
    btNCB3_1x.image=zyW16_CB3_1x


def _hitclean1x():
    for zy_entry1x,_ in zy_entrIes1x:
        zy_entry1x.delete(0,"end")    


'''2x的def'''   
'''
第 "1" 個子視窗，所有 "B" utton子視窗，
乘法 2 X1-9的子視窗，從wiN"21"，1的乘法→ "2x"，命名 1B212x
'''
def _hit1B212x():
    global zy_entrIes2x,zy_answErs2x,zy_btN2xs,zy_wiN21
    zy_wiN21=tk.Toplevel(wiN)
    zy_wiN21.title("2 X 1-9")
    zy_wiN21.geometry("225x525+200+200")
    
    zy_frame1B212x=tk.Frame(zy_wiN21)
    zy_frame1B212x.pack()
    
    zy_entrIes2x=[]
    zy_answErs2x=[2,4,6,8,10,12,14,16,18]
    
    for n2x in range(1,10):
        zy_lbL_2x=tk.Label(zy_frame1B212x,text=f"2 X {n2x} =",
                           fg="black",bg="Salmon",
                           font=("Arial",12),
                           width=10,height=2)
        zy_lbL_2x.grid(row=n2x-1,column=0)
        
        zy_entrY_2x=tk.Entry(zy_frame1B212x,
                             font=("Arial",14),
                             width=3,bd=2,
                             justify="center")
        zy_entrY_2x.grid(row=n2x-1,column=1,padx=3,pady=3,
                   ipadx=6,ipady=8)
        zy_entrIes2x.append((zy_entrY_2x,zy_answErs2x[n2x-1]))
        
        
    '''Check answers Button 2x1-9'''
    '''圖片：對答案'''
    img_btN2xs=Image.open(get_image_path("1_Check answers_2_remove bg.png")).resize((125,30))  
    zyf21_btN2xs=ImageTk.PhotoImage(img_btN2xs)
    
    zy_btN2xs = tk.Button(zy_frame1B212x, 
                     image=zyf21_btN2xs,
                     relief="raised", 
                     borderwidth=3,
                     width=125, height=30,
                     command=partial(_hit2xs, zy_wiN21))    
    zy_btN2xs.grid(row=9,column=0,columnspan=2,pady=6,ipadx=5,ipady=5)
    zy_btN2xs.image=zyf21_btN2xs
    
'''2xs→1的乘法(2x)，送出(send)→2xs'''    
def _hit2xs(zy_wiN21):
    zy_errorS2x=[]
    try:
        for n2x,(zy_entry2x,zy_answErs2x) in enumerate(zy_entrIes2x):
            if int(zy_entry2x.get()) != zy_answErs2x:
                zy_errorS2x.append(f"  2 X { n2x+1 }  ㄉㄚˊ ㄢˋ ㄘㄨㄛˋ ㄨˋ !")
                

    except ValueError:
        global zy_wiN22
        #messagebox.showerror("提示","請勿輸入非數字 或 空白")
        '''視窗：第幾列第幾格錯誤，'''
        zy_wiN22=tk.Toplevel(wiN)
        zy_wiN22.title("")
        zy_wiN22.geometry("550x250+550+200")
        zy_wiN22.configure(bg="white")
        
        zy_frameW12=tk.Frame(zy_wiN22,bg="white")
        zy_frameW12.pack(expand=True)
        
        '''圖片：請勿空白或輸入不是數字的內容喔!'''
        imgdonot_empty2x=Image.open(get_image_path("don't empty_img_remove bg.png")).resize((430,50)) 
        zyfW22_imgdonot_empty2x=ImageTk.PhotoImage(imgdonot_empty2x)
        lbLimgdonot_empty2x=tk.Label(zy_frameW12,
                                     image=zyfW22_imgdonot_empty2x,
                                     borderwidth=4,
                                     width=450, height=75)
        
        lbLimgdonot_empty2x.grid(row=0,column=2,
                                 columnspan=2,
                                 pady=8,
                                 ipadx=3,ipady=1)
        lbLimgdonot_empty2x.image=zyfW22_imgdonot_empty2x

        
        '''製作check Button'''
        '''btNcB無法執行，問題是「#command=zy_wiN1.destroy()」'''
        '''command=zy_wiN1.destroy←不要"()"就可以執行了'''
        
        img_cB_2x=Image.open(get_image_path("ok_remove bg.png")).resize((50,50))  
        zyfW22_cB_2x=ImageTk.PhotoImage(img_cB_2x)

        btNcB_2x=tk.Button(zy_frameW12,
                            image=zyfW22_cB_2x,
                            bg="white",
                            relief="groove",
                            borderwidth=5,
                            width=50, height=50,
                            command=zy_wiN22.destroy)
                    

        btNcB_2x.grid(row=1,
                      columnspan=4,
                      pady=15,ipadx=3,ipady=1)        
        btNcB_2x.image=zyfW22_cB_2x
        return

    if zy_errorS2x:
        '''視窗：第幾列第幾格錯誤!'''
        zy_wiN23=tk.Toplevel(wiN)
        zy_wiN23.title("")
        zy_wiN23.geometry("400x350+450+200")
        zy_wiN23.configure(bg="white")
        zy_wiN23.resizable(width=False, height=False)
        zy_frameW23=tk.Frame(zy_wiN23,
                            bg="MediumTurquoise",
                            height=90)
        
        zy_frameW23.pack(fill="x")
        
        
        '''圖片：Cue1_remove bg'''
        zy_imgCue2x = Image.open(get_image_path("Cue1_remove bg.png")).resize((120,40))
        zy_frameW23_imgCue2x = ImageTk.PhotoImage(zy_imgCue2x)
        zy_lbL_imgCue2x = tk.Label(zy_frameW23,
                                image=zy_frameW23_imgCue2x,
                                bg="MintCream",
                                relief="solid",
                                borderwidth=2,
                                width=124,height=44)
                        
        zy_lbL_imgCue2x.place(relx=0.5, rely=0.5,
                          anchor="center")
        zy_lbL_imgCue2x.image=zy_frameW23_imgCue2x
        
        
        zy_frameW23_1=tk.Frame(zy_wiN23,
                            bg="MediumTurquoise")
        zy_frameW23_1.pack(expand=True,fill="both")
        
        # 滾動條，用於文字框 # Scrollbar for the text box
        sBar_zyW23 = tk.Scrollbar(zy_frameW23_1, orient="vertical") # 建立垂直滾動條
        sBar_zyW23.pack(side=tk.RIGHT, fill="y")  # 將滾動條附加在右側 # Attach scrollbar to the right side
                    
        # zy_frameW7_1 裡面的文字框 # Text box inside zy_frameW7_1
        texT_zy_frameW23_1 = tk.Text(zy_frameW23_1,
                                    bg="#F0FFF0",
                                    wrap=tk.WORD, #自動換行以單字為單位
                                    font=("標楷體", 14), 
                                    yscrollcommand=sBar_zyW23.set)  
                                    # 將文字框與滾動條連結 # Link Text box to scrollbar)
        texT_zy_frameW23_1.pack()

        
        # 將滾動條連結到文字框 # Link scrollbar to Text box
        sBar_zyW23.config(command=texT_zy_frameW23_1.yview)
        
        # 將錯誤訊息組合成單一字串，並以分隔線區隔
        zy_errorS2x_text = "\n  ----------------------------------\n".join(zy_errorS2x)
        texT_zy_frameW23_1.insert(tk.END,f"\n{zy_errorS2x_text}\n")
        texT_zy_frameW23_1.config(state="disabled")
        # 設定文字框為不可編輯狀態 # Disable editing of the Text box
        
                     
    else:
        '''視窗：全部正確顯示'''
        global zy_wiN24
        zy_wiN24=tk.Toplevel(wiN)
        zy_wiN24.title("")
        zy_wiN24.geometry("550x270+450+200")
        zy_wiN24.configure(bg="SeaShell")
                          
        
        zy_frameW24=tk.Frame(zy_wiN24,
                            bg="SeaShell")
        zy_frameW24.pack(expand=True)

        image_files_2x = {
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
        
        random_key_2x=rd.randint(1,len(image_files_2x))
        image_file_2x=image_files_2x[random_key_2x]
     
        img_good2x=Image.open(get_image_path(image_file_2x)).resize((70,70))
        zy_frameW24_img_good2x=ImageTk.PhotoImage(img_good2x)

        lbL_img_good2x=tk.Label(zy_frameW24,
                                image=zy_frameW24_img_good2x,
                                bg="SeaShell",
                                
                                
                                
                                width=70, height=70)
        
        lbL_img_good2x.grid(row=0,
                            column=0,
                            
                            pady=8,
                            ipadx=3,
                            ipady=1)
        lbL_img_good2x.image=zy_frameW24_img_good2x # 防止垃圾回收
       
        image_files2_2x = {
        1: "good1_All correct_remove bg.png",
        2: "good2_All answers are correct_remove bg.png",
        3: "good3_En_Bingo_remove bg.png",
        4: "good4_You are excellent!_remove bg.png",
        5: "good5_Completely correct_remove bg.png",
        6: "good6_You got it right!_remove bg.png"}
        
        random_key1_2x=rd.randint(1,len(image_files2_2x))
        image_file2_2x=image_files2_2x[random_key1_2x]
       
        img_good1_2x=Image.open(get_image_path(image_file2_2x)).resize((180,40))
        zy_frameW24_img_good1_2x=ImageTk.PhotoImage(img_good1_2x)

        lbL_img_good1_2x=tk.Label(zy_frameW24,
                                  image=zy_frameW24_img_good1_2x,
                                  bg="SeaShell",
                                  
                                  
                                  
                                  width=200, height=50)
        
        lbL_img_good1_2x.grid(row=0,
                              column=1,
                              
                              pady=8,
                              ipady=1)
        lbL_img_good1_2x.image=zy_frameW24_img_good1_2x # 防止垃圾回收
        
        image_files3_2x = {
        1: "good71_Awesome!_remove bg.png",
        2: "good71_You are amazing!_remove bg.png",
        3: "good71_So impressive_remove bg.png",
        4: "good71_So smart!_remove bg.png",
        5: "good71_Super amazing!_remove bg.png",
        6: "good71_You are a genius!_remove bg.png"}
        
        random_key2_2x=rd.randint(1,len(image_files3_2x))
        image_file3_2x=image_files3_2x[random_key2_2x]
        
        img_good2_2x=Image.open(get_image_path(image_file3_2x)).resize((180,40))
        zy_frameW24_img_good2_2x=ImageTk.PhotoImage(img_good2_2x)

        lbL_img_good2_2x=tk.Label(zy_frameW24,
                                  image=zy_frameW24_img_good2_2x,
                                  bg="SeaShell",
                                  width=200, height=50)
        
        lbL_img_good2_2x.grid(row=0,
                              column=2,
                              
                              pady=8,
                              ipady=1)
        lbL_img_good2_2x.image=zy_frameW24_img_good2_2x # 防止垃圾回收
        
        '''稱讚的OK鈕'''
                
        img_cB1_2x=Image.open(get_image_path("ok_remove bg.png")).resize((50,50))  
        img_btNcB1_2x=ImageTk.PhotoImage(img_cB1_2x)

        btNcB1_2x=tk.Button(zy_frameW24,
                            image=img_btNcB1_2x,
                            bg="white",
                            relief="groove",
                            borderwidth=5,
                            width=50, height=50,
                            command=partial(
                                _hit_clearnAclose2x,
                                zy_wiN24))

        btNcB1_2x.grid(row=1,
                       columnspan=4,pady=15,
                       ipadx=3,ipady=1)
        
        btNcB1_2x.image=img_btNcB1_2x

    

        
def _hit_clearnAclose2x(zy_wiN24):   
        global zy_wiN25
        zy_wiN25=tk.Toplevel(wiN)
        zy_wiN25.title("")
        zy_wiN25.geometry("500x300+450+200")
        zy_wiN25.configure(bg="white")
        
        zy_frameW25=tk.Frame(zy_wiN25,bg="white")
        zy_frameW25.pack(expand=True)    
        
        '''視窗：關閉乘法練習的視窗嗎？'''
        imgclosE_2x = Image.open(get_image_path("Are you sure close window_remove bg.png")).resize((350,60))
        zy_frameW25_imgclosE_2x = ImageTk.PhotoImage(imgclosE_2x)
        lbL_imgclosE_2x = tk.Label(zy_frameW25,
                                   image=zy_frameW25_imgclosE_2x,
                                   bg="white",
                                   
                                   
                                   width=400,height=60)
                          
        lbL_imgclosE_2x.grid(row=0,
                             columnspan=4,
                             
                             pady=15,
                             ipadx=3,ipady=1)
        
        lbL_imgclosE_2x.image=zy_frameW25_imgclosE_2x

        '''確定鈕'''
        img_CB2_2x=Image.open(get_image_path("Confirm Button_1_remove bg.png")).resize((70,60))  
        zyfw25_CB2_2x=ImageTk.PhotoImage(img_CB2_2x)

        btNCB2_2x=tk.Button(zy_frameW25,
                            image=zyfw25_CB2_2x,
                            bg="white",
                            relief="groove",
                            borderwidth=3,
                            width=70, height=70,
                            command=lambda:(zy_wiN21.destroy(),
                                            zy_wiN24.destroy(),
                                            zy_wiN25.destroy()))
        
        btNCB2_2x.grid(row=1,
                       column=1,
                       
                       
                       padx=10,pady=15,
                       ipadx=1,ipady=1)
        
        btNCB2_2x.image=zyfw25_CB2_2x
        
        '''取消鈕'''
        img_canceL2x=Image.open(get_image_path("Cancel Button_remove bg.png")).resize((70,60))  
        zyfw25_canceL2x=ImageTk.PhotoImage(img_canceL2x)

        btNcanceL2x=tk.Button(zy_frameW25,
                            image=zyfw25_canceL2x,
                            bg="white",
                            relief="groove",
                            borderwidth=3,
                            width=70, height=70,
                            command=_hit_clAcl2x)
           
        btNcanceL2x.grid(row=1,
                       column=2,
                       
                       
                       padx=10,pady=15,
                       ipadx=1,ipady=1)
        
        btNcanceL2x.image=zyfw25_canceL2x

'''清除答案，在挑戰一次？'''
def _hit_clAcl2x(): #命名：Clear the answers and try the challenge again?
    
    zy_wiN26=tk.Toplevel(wiN)
    zy_wiN26.title("")
    zy_wiN26.geometry("500x300+450+200")
    zy_wiN26.configure(bg="white")
    
    zy_frameW26=tk.Frame(zy_wiN26,bg="white")
    zy_frameW26.pack(expand=True)    
    
    '''圖片：清除答案，在挑戰一次？'''
    imgclAcl_2x = Image.open(get_image_path("Clear answers and challenge again_remove bg.png")).resize((350,60))
    zy_frameW26_imgclAcl_2x = ImageTk.PhotoImage(imgclAcl_2x)
    lbL_imgclAcl_2x = tk.Label(zy_frameW26,
                               image=zy_frameW26_imgclAcl_2x,
                               bg="white",
                               
                               
                               width=400,height=60)
                      
    lbL_imgclAcl_2x.grid(row=0,
                         columnspan=4,
                         
                         pady=15,
                         ipadx=3,ipady=1)
    
    lbL_imgclAcl_2x.image=zy_frameW26_imgclAcl_2x
    
    '''確定鈕'''
    img_CB3_2x=Image.open(get_image_path("Confirm Button_1_remove bg.png")).resize((70,60))  
    zyW26_CB3_2x=ImageTk.PhotoImage(img_CB3_2x)
    
    btNCB3_2x=tk.Button(zy_frameW26,
                        image=zyW26_CB3_2x,
                        bg="white",
                        relief="groove",
                        borderwidth=3,
                        width=70, height=70,
                        command=lambda:(
                            _hitclean2x(),
                            zy_wiN24.destroy(),
                            zy_wiN25.destroy(),                           
                            zy_wiN26.destroy()))

    btNCB3_2x.grid(row=1,
                columnspan=5,
                padx=10,pady=15,
                ipadx=1,ipady=1)
    
    btNCB3_2x.image=zyW26_CB3_2x


def _hitclean2x():
    for zy_entry2x,_ in zy_entrIes2x:
        zy_entry2x.delete(0,"end")
       

'''3x的def'''   
'''
第 "1" 個子視窗，所有 "B" utton子視窗，
乘法 3 X1-9的子視窗，從wiN"31"，1的乘法→ "3x"，命名 1B313x
'''
def _hit1B313x():
    global zy_entrIes3x,zy_answErs3x,zy_btN3xs,zy_wiN31
    zy_wiN31=tk.Toplevel(wiN)
    zy_wiN31.title("3 X 1-9")
    zy_wiN31.geometry("225x525+200+200")
    
    zy_frame1B313x=tk.Frame(zy_wiN31)
    zy_frame1B313x.pack()
    
    zy_entrIes3x=[]
    zy_answErs3x=[3,6,9,12,15,18,21,24,27]
    
    for n3x in range(1,10):
        zy_lbL_3x=tk.Label(zy_frame1B313x,text=f"3 X {n3x} =",
                           fg="black",bg="Salmon",
                           font=("Arial",12),
                           width=10,height=2)
        zy_lbL_3x.grid(row=n3x-1,column=0)
        
        zy_entrY_3x=tk.Entry(zy_frame1B313x,
                             font=("Arial",14),
                             width=3,bd=2,
                             justify="center")
        zy_entrY_3x.grid(row=n3x-1,column=1,padx=3,pady=3,
                   ipadx=6,ipady=8)
        zy_entrIes3x.append((zy_entrY_3x,zy_answErs3x[n3x-1]))
        
        
    '''Check answers Button 3x1-9'''
    '''圖片：對答案'''
    img_btN3xs=Image.open(get_image_path("1_Check answers_2_remove bg.png")).resize((125,30))  
    zyf31_btN3xs=ImageTk.PhotoImage(img_btN3xs)
    
    zy_btN3xs = tk.Button(zy_frame1B313x, 
                     image=zyf31_btN3xs,
                     relief="raised", 
                     borderwidth=3,
                     width=125, height=30,
                     command=partial(_hit3xs, zy_wiN31))    
    zy_btN3xs.grid(row=9,column=0,columnspan=2,pady=6,ipadx=5,ipady=5)
    zy_btN3xs.image=zyf31_btN3xs
    
'''3xs→1的乘法(3x)，送出(send)→3xs'''    
def _hit3xs(zy_wiN31):
    zy_errorS3x=[]
    try:
        for n3x,(zy_entry3x,zy_answErs3x) in enumerate(zy_entrIes3x):
            if int(zy_entry3x.get()) != zy_answErs3x:
                zy_errorS3x.append(f"  3 X { n3x+1 }  ㄉㄚˊ ㄢˋ ㄘㄨㄛˋ ㄨˋ !")

    except ValueError:
        global zy_wiN32
        #messagebox.showerror("提示","請勿輸入非數字 或 空白")
        '''視窗：第幾列第幾格錯誤，'''
        zy_wiN32=tk.Toplevel(wiN)
        zy_wiN32.title("")
        zy_wiN32.geometry("550x250+550+200")
        zy_wiN32.configure(bg="white")
        
        zy_frameW32=tk.Frame(zy_wiN32,bg="white")
        zy_frameW32.pack(expand=True)
        
        '''圖片：請勿空白或輸入不是數字的內容喔!'''
        imgdonot_empty3x=Image.open(get_image_path("don't empty_img_remove bg.png")).resize((430,50)) 
        zyfW32_imgdonot_empty3x=ImageTk.PhotoImage(imgdonot_empty3x)
        lbLimgdonot_empty3x=tk.Label(zy_frameW32,
                                     image=zyfW32_imgdonot_empty3x,
                                     borderwidth=4,
                                     width=450, height=75)
        
        lbLimgdonot_empty3x.grid(row=0,column=2,
                                 columnspan=2,
                                 pady=8,
                                 ipadx=3,ipady=1)
        lbLimgdonot_empty3x.image=zyfW32_imgdonot_empty3x

        
        '''製作check Button'''
        '''btNcB無法執行，問題是「#command=zy_wiN1.destroy()」'''
        '''command=zy_wiN1.destroy←不要"()"就可以執行了'''
        
        img_cB_3x=Image.open(get_image_path("ok_remove bg.png")).resize((50,50))  
        zyfW32_cB_3x=ImageTk.PhotoImage(img_cB_3x)

        btNcB_3x=tk.Button(zy_frameW32,
                            image=zyfW32_cB_3x,
                            bg="white",
                            relief="groove",
                            borderwidth=5,
                            width=50, height=50,
                            command=zy_wiN32.destroy)
                    

        btNcB_3x.grid(row=1,
                       columnspan=4,                       
                       pady=15,ipadx=3,ipady=1)
        
        btNcB_3x.image=zyfW32_cB_3x
        return

    if zy_errorS3x:
        '''視窗：第幾列第幾格錯誤!'''
        zy_wiN33=tk.Toplevel(wiN)
        zy_wiN33.title("")
        zy_wiN33.geometry("400x350+450+200")
        zy_wiN33.configure(bg="white")
        zy_wiN33.resizable(width=False, height=False)
        
        zy_frameW33=tk.Frame(zy_wiN33,
                            bg="MediumTurquoise",
                            height=90)
        
        zy_frameW33.pack(fill="x")
        
        
        '''圖片：Cue1_remove bg'''
        zy_imgCue3x = Image.open(get_image_path("Cue1_remove bg.png")).resize((120,40))
        zy_frameW33_imgCue3x = ImageTk.PhotoImage(zy_imgCue3x)
        zy_lbL_imgCue3x = tk.Label(zy_frameW33,
                                image=zy_frameW33_imgCue3x,
                                bg="MintCream",
                                relief="solid",
                                borderwidth=2,
                                width=124,height=44)
                        
        zy_lbL_imgCue3x.place(relx=0.5, rely=0.5,
                          anchor="center")                   
        zy_lbL_imgCue3x.image=zy_frameW33_imgCue3x
        
        
        zy_frameW33_1=tk.Frame(zy_wiN33,
                            bg="MediumTurquoise")                            
        zy_frameW33_1.pack(expand=True,fill="both")
        
        
        # 滾動條，用於文字框 # Scrollbar for the text box
        sBar_zyW33 = tk.Scrollbar(zy_frameW33_1, orient="vertical") # 建立垂直滾動條
        sBar_zyW33.pack(side=tk.RIGHT, fill="y")  # 將滾動條附加在右側 # Attach scrollbar to the right side
                    
        # zy_frameW7_1 裡面的文字框 # Text box inside zy_frameW7_1
        texT_zy_frameW33_1 = tk.Text(zy_frameW33_1,
                                    bg="#F0FFF0",
                                    wrap=tk.WORD, # 自動換行以單字為單位
                                    font=("標楷體", 14), 
                                    yscrollcommand=sBar_zyW33.set)  
                                    # 將文字框與滾動條連結 # Link Text box to scrollbar)
        texT_zy_frameW33_1.pack()

        
        # 將滾動條連結到文字框 # Link scrollbar to Text box
        sBar_zyW33.config(command=texT_zy_frameW33_1.yview)
        
        # 將錯誤訊息組合成單一字串，並以分隔線區隔
        zy_errorS3x_text = "\n  ----------------------------------\n".join(zy_errorS3x)
        texT_zy_frameW33_1.insert(tk.END,f"\n{zy_errorS3x_text}\n")
        texT_zy_frameW33_1.config(state="disabled")
        # 設定文字框為不可編輯狀態 # Disable editing of the Text box    
                     
    else:
        '''視窗：全部正確顯示'''
        global zy_wiN34
        zy_wiN34=tk.Toplevel(wiN)
        zy_wiN34.title("")
        zy_wiN34.geometry("550x270+450+200")
        zy_wiN34.configure(bg="SeaShell")                          
        
        zy_frameW34=tk.Frame(zy_wiN34,bg="SeaShell")                            
        zy_frameW34.pack(expand=True)

        image_files_3x = {
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
        
        random_key_3x=rd.randint(1,len(image_files_3x))
        image_file_3x=image_files_3x[random_key_3x]
        
        img_good3x=Image.open(get_image_path(image_file_3x)).resize((70,70))
        zy_frameW34_img_good3x=ImageTk.PhotoImage(img_good3x)

        lbL_img_good3x=tk.Label(zy_frameW34,
                                image=zy_frameW34_img_good3x,
                                bg="SeaShell",
                                width=70, height=70)
        
        lbL_img_good3x.grid(row=0,
                            column=0,
                            pady=8,
                            ipadx=3,
                            ipady=1)
        lbL_img_good3x.image=zy_frameW34_img_good3x 
        
        image_files2_3x = {
        1: "good1_All correct_remove bg.png",
        2: "good2_All answers are correct_remove bg.png",
        3: "good3_En_Bingo_remove bg.png",
        4: "good4_You are excellent!_remove bg.png",
        5: "good5_Completely correct_remove bg.png",
        6: "good6_You got it right!_remove bg.png"}
        
        random_key1_3x=rd.randint(1,len(image_files2_3x))
        image_file2_3x=image_files2_3x[random_key1_3x]
        
        img_good1_3x=Image.open(get_image_path(image_file2_3x)).resize((180,40))
        zy_frameW34_img_good1_3x=ImageTk.PhotoImage(img_good1_3x)

        lbL_img_good1_3x=tk.Label(zy_frameW34,
                                  image=zy_frameW34_img_good1_3x,
                                  bg="SeaShell",
                                  width=200, height=50)
        
        lbL_img_good1_3x.grid(row=0,
                              column=1,
                              pady=8,
                              ipady=1)
        lbL_img_good1_3x.image=zy_frameW34_img_good1_3x 
        
        image_files3_3x = {
        1: "good71_Awesome!_remove bg.png",
        2: "good71_You are amazing!_remove bg.png",
        3: "good71_So impressive_remove bg.png",
        4: "good71_So smart!_remove bg.png",
        5: "good71_Super amazing!_remove bg.png",
        6: "good71_You are a genius!_remove bg.png"}
        
        random_key2_3x=rd.randint(1,len(image_files3_3x))
        image_file3_3x=image_files3_3x[random_key2_3x]
        
        img_good2_3x=Image.open(get_image_path(image_file3_3x)).resize((180,40))
        zy_frameW34_img_good2_3x=ImageTk.PhotoImage(img_good2_3x)

        lbL_img_good2_3x=tk.Label(zy_frameW34,
                                  image=zy_frameW34_img_good2_3x,
                                  bg="SeaShell",
                                  width=200, height=50)
        
        lbL_img_good2_3x.grid(row=0,
                              column=2,
                              pady=8,
                              ipady=1)
        lbL_img_good2_3x.image=zy_frameW34_img_good2_3x 
        
        '''稱讚的OK鈕'''
                
        img_cB1_3x=Image.open(get_image_path("ok_remove bg.png")).resize((50,50))  
        img_btNcB1_3x=ImageTk.PhotoImage(img_cB1_3x)

        btNcB1_3x=tk.Button(zy_frameW34,
                            image=img_btNcB1_3x,
                            bg="white",
                            relief="groove",
                            borderwidth=5,
                            width=50, height=50,
                            command=partial(
                                _hit_clearnAclose3x,
                                zy_wiN34))

        btNcB1_3x.grid(row=1,
                       columnspan=4,
                       pady=15,
                       ipadx=3,ipady=1)
        
        btNcB1_3x.image=img_btNcB1_3x
        
def _hit_clearnAclose3x(zy_wiN34):   
        global zy_wiN35
        '''
        ("提示",f"確定關閉{sizeS-1}格x{sizeS-1}格乘法練習視窗嗎？")
        '''
        
        zy_wiN35=tk.Toplevel(wiN)
        zy_wiN35.title("")
        zy_wiN35.geometry("500x300+450+200")
        zy_wiN35.configure(bg="white")
        
        zy_frameW35=tk.Frame(zy_wiN35,bg="white")
        zy_frameW35.pack(expand=True)    
        
        '''視窗：關閉乘法練習的視窗嗎？'''
        imgclosE_3x = Image.open(get_image_path("Are you sure close window_remove bg.png")).resize((350,60))
        zy_frameW35_imgclosE_3x = ImageTk.PhotoImage(imgclosE_3x)
        lbL_imgclosE_3x = tk.Label(zy_frameW35,
                                   image=zy_frameW35_imgclosE_3x,
                                   bg="white",
                                   width=400,height=60)
                          
        lbL_imgclosE_3x.grid(row=0,
                             columnspan=4,
                             pady=15,
                             ipadx=3,ipady=1)
        
        lbL_imgclosE_3x.image=zy_frameW35_imgclosE_3x

        '''確定鈕'''
        img_CB2_3x=Image.open(get_image_path("Confirm Button_1_remove bg.png")).resize((70,60))  
        zyfw35_CB2_3x=ImageTk.PhotoImage(img_CB2_3x)

        btNCB2_3x=tk.Button(zy_frameW35,
                            image=zyfw35_CB2_3x,
                            bg="white",
                            relief="groove",
                            borderwidth=3,
                            width=70, height=70,
                            command=lambda:(zy_wiN31.destroy(),
                                            zy_wiN34.destroy(),
                                            zy_wiN35.destroy()))
        
        btNCB2_3x.grid(row=1,
                       column=1,
                       padx=10,pady=15,
                       ipadx=1,ipady=1)
        
        btNCB2_3x.image=zyfw35_CB2_3x
        
        '''取消鈕'''
        img_canceL3x=Image.open(get_image_path("Cancel Button_remove bg.png")).resize((70,60))  
        zyfw35_canceL3x=ImageTk.PhotoImage(img_canceL3x)

        btNcanceL3x=tk.Button(zy_frameW35,
                              image=zyfw35_canceL3x,
                              bg="white",
                              relief="groove",
                              borderwidth=3,
                              width=70, height=70,
                              command=_hit_clAcl3x)
           
        btNcanceL3x.grid(row=1,
                       column=2,
                       padx=10,pady=15,
                       ipadx=1,ipady=1)
        
        btNcanceL3x.image=zyfw35_canceL3x

'''清除答案，在挑戰一次？'''
def _hit_clAcl3x(): #命名：Clear the answers and try the challenge again?
    
    zy_wiN36=tk.Toplevel(wiN)
    zy_wiN36.title("")
    zy_wiN36.geometry("500x300+450+200")
    zy_wiN36.configure(bg="white")
    
    zy_frameW36=tk.Frame(zy_wiN36,bg="white")
    zy_frameW36.pack(expand=True)    
    
    '''圖片：清除答案，在挑戰一次？'''
    imgclAcl_3x = Image.open(get_image_path("Clear answers and challenge again_remove bg.png")).resize((350,60))
    zy_frameW36_imgclAcl_3x = ImageTk.PhotoImage(imgclAcl_3x)
    lbL_imgclAcl_3x = tk.Label(zy_frameW36,
                               image=zy_frameW36_imgclAcl_3x,
                               bg="white",
                               width=400,height=60)
                      
    lbL_imgclAcl_3x.grid(row=0,
                         columnspan=4,
                         pady=15,
                         ipadx=3,ipady=1)
    
    lbL_imgclAcl_3x.image=zy_frameW36_imgclAcl_3x
    
    '''確定鈕'''
    img_CB3_3x=Image.open(get_image_path("Confirm Button_1_remove bg.png")).resize((70,60))  
    zyW36_CB3_3x=ImageTk.PhotoImage(img_CB3_3x)
    
    btNCB3_3x=tk.Button(zy_frameW36,
                        image=zyW36_CB3_3x,
                        bg="white",
                        relief="groove",
                        borderwidth=3,
                        width=70, height=70,
                        command=lambda:(
                            _hitclean3x(),
                            zy_wiN34.destroy(),
                            zy_wiN35.destroy(),                           
                            zy_wiN36.destroy()))

    btNCB3_3x.grid(row=1,
                columnspan=5,
                padx=10,pady=15,
                ipadx=1,ipady=1)
    
    btNCB3_3x.image=zyW36_CB3_3x


def _hitclean3x():
    for zy_entry3x,_ in zy_entrIes3x:
        zy_entry3x.delete(0,"end")


        
'''4x的def'''   
'''
第 "1" 個子視窗，所有 "B" utton子視窗，
乘法 4 X1-9的子視窗，從wiN"41"，1的乘法→ "4x"，命名 1B414x
'''
def _hit1B414x():
    global zy_entrIes4x,zy_answErs4x,zy_btN4xs,zy_wiN41
    zy_wiN41=tk.Toplevel(wiN)
    zy_wiN41.title("4 X 1-9")
    zy_wiN41.geometry("225x525+200+200")
    
    zy_frame1B414x=tk.Frame(zy_wiN41)
    zy_frame1B414x.pack()
    
    zy_entrIes4x=[]
    zy_answErs4x=[4,8,12,16,20,24,28,32,36]
    
    for n4x in range(1,10):
        zy_lbL_4x=tk.Label(zy_frame1B414x,text=f"4 X {n4x} =",
                           fg="black",bg="Salmon",
                           font=("Arial",12),
                           width=10,height=2)
        zy_lbL_4x.grid(row=n4x-1,column=0)
        
        zy_entrY_4x=tk.Entry(zy_frame1B414x,
                             font=("Arial",14),
                             width=3,bd=2,
                             justify="center")
        zy_entrY_4x.grid(row=n4x-1,column=1,padx=3,pady=3,
                   ipadx=6,ipady=8)
        zy_entrIes4x.append((zy_entrY_4x,zy_answErs4x[n4x-1]))
        
        
    '''Check answers Button 4x1-9'''
    '''圖片：對答案'''
    img_btN4xs=Image.open(get_image_path("1_Check answers_2_remove bg.png")).resize((125,30))  
    zyf41_btN4xs=ImageTk.PhotoImage(img_btN4xs)
    
    zy_btN4xs = tk.Button(zy_frame1B414x, 
                     image=zyf41_btN4xs,
                     relief="raised", 
                     borderwidth=3,
                     width=125, height=30,
                     command=partial(_hit4xs, zy_wiN41))    
    zy_btN4xs.grid(row=9,column=0,columnspan=2,pady=6,ipadx=5,ipady=5)
    zy_btN4xs.image=zyf41_btN4xs
    
'''4xs→1的乘法(4x)，送出(send)→4xs'''    
def _hit4xs(zy_wiN41):
    zy_errorS4x=[]
    try:
        for n4x,(zy_entry4x,zy_answErs4x) in enumerate(zy_entrIes4x):
            if int(zy_entry4x.get()) != zy_answErs4x:
                zy_errorS4x.append(f"  4 X { n4x+1 }  ㄉㄚˊ ㄢˋ ㄘㄨㄛˋ ㄨˋ !")

    except ValueError:
        global zy_wiN42
        #messagebox.showerror("提示","請勿輸入非數字 或 空白")
        '''視窗：第幾列第幾格錯誤，'''
        zy_wiN42=tk.Toplevel(wiN)
        zy_wiN42.title("")
        zy_wiN42.geometry("550x250+550+200")
        zy_wiN42.configure(bg="white")
        
        zy_frameW42=tk.Frame(zy_wiN42,bg="white")
        zy_frameW42.pack(expand=True)
        
        '''圖片：請勿空白或輸入不是數字的內容喔!'''
        imgdonot_empty4x=Image.open(get_image_path("don't empty_img_remove bg.png")).resize((430,50)) 
        zyfW42_imgdonot_empty4x=ImageTk.PhotoImage(imgdonot_empty4x)
        lbLimgdonot_empty4x=tk.Label(zy_frameW42,
                                     image=zyfW42_imgdonot_empty4x,
                                     borderwidth=4,
                                     width=450, height=75)
        
        lbLimgdonot_empty4x.grid(row=0,column=2,
                                 columnspan=2,
                                 pady=8,
                                 ipadx=3,ipady=1)
        lbLimgdonot_empty4x.image=zyfW42_imgdonot_empty4x

        
        '''製作check Button'''
        '''btNcB無法執行，問題是「#command=zy_wiN1.destroy()」'''
        '''command=zy_wiN1.destroy←不要"()"就可以執行了'''
        
        img_cB_4x=Image.open(get_image_path("ok_remove bg.png")).resize((50,50))  
        zyfW42_cB_4x=ImageTk.PhotoImage(img_cB_4x)

        btNcB_4x=tk.Button(zy_frameW42,
                            image=zyfW42_cB_4x,
                            bg="white",
                            relief="groove",
                            borderwidth=5,
                            width=50, height=50,
                            command=zy_wiN42.destroy)
                    

        btNcB_4x.grid(row=1,
                       columnspan=4,                       
                       pady=15,ipadx=3,ipady=1)
        
        btNcB_4x.image=zyfW42_cB_4x
        return

    if zy_errorS4x:
        '''視窗：第幾列第幾格錯誤!'''
        zy_wiN43=tk.Toplevel(wiN)
        zy_wiN43.title("")
        zy_wiN43.geometry("400x350+450+200")
        zy_wiN43.configure(bg="white")
        zy_wiN43.resizable(width=False, height=False)
        
        zy_frameW43=tk.Frame(zy_wiN43,
                            bg="MediumTurquoise",
                            height=90)
        
        zy_frameW43.pack(fill="x")
        
        
        '''圖片：Cue1_remove bg'''
        zy_imgCue4x = Image.open(get_image_path("Cue1_remove bg.png")).resize((120,40))
        zy_frameW43_imgCue4x = ImageTk.PhotoImage(zy_imgCue4x)
        zy_lbL_imgCue4x = tk.Label(zy_frameW43,
                                image=zy_frameW43_imgCue4x,
                                bg="MintCream",
                                relief="solid",
                                borderwidth=2,
                                width=124,height=44)
                        
        zy_lbL_imgCue4x.place(relx=0.5, rely=0.5,
                          anchor="center")                   
        zy_lbL_imgCue4x.image=zy_frameW43_imgCue4x
        
        
        zy_frameW43_1=tk.Frame(zy_wiN43,
                            bg="MediumTurquoise")                            
        zy_frameW43_1.pack(expand=True,fill="both")
        
        
        # 滾動條，用於文字框 # Scrollbar for the text box
        sBar_zyW43 = tk.Scrollbar(zy_frameW43_1, orient="vertical") # 建立垂直滾動條
        sBar_zyW43.pack(side=tk.RIGHT, fill="y")  # 將滾動條附加在右側 # Attach scrollbar to the right side
                    
        # zy_frameW7_1 裡面的文字框 # Text box inside zy_frameW7_1
        texT_zy_frameW43_1 = tk.Text(zy_frameW43_1,
                                    bg="#F0FFF0",
                                    wrap=tk.WORD, # 自動換行以單字為單位
                                    font=("標楷體", 14), 
                                    yscrollcommand=sBar_zyW43.set)  
                                    # 將文字框與滾動條連結 # Link Text box to scrollbar)
        texT_zy_frameW43_1.pack()

        
        # 將滾動條連結到文字框 # Link scrollbar to Text box
        sBar_zyW43.config(command=texT_zy_frameW43_1.yview)
        
        # 將錯誤訊息組合成單一字串，並以分隔線區隔
        zy_errorS4x_text = "\n  ----------------------------------\n".join(zy_errorS4x)
        texT_zy_frameW43_1.insert(tk.END,f"\n{zy_errorS4x_text}\n")
        texT_zy_frameW43_1.config(state="disabled")
        # 設定文字框為不可編輯狀態 # Disable editing of the Text box    
                     
    else:
        '''視窗：全部正確顯示'''
        global zy_wiN44
        zy_wiN44=tk.Toplevel(wiN)
        zy_wiN44.title("")
        zy_wiN44.geometry("550x270+450+200")
        zy_wiN44.configure(bg="SeaShell")                          
        
        zy_frameW44=tk.Frame(zy_wiN44,bg="SeaShell")                            
        zy_frameW44.pack(expand=True)

        image_files_4x = {
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
        
        random_key_4x=rd.randint(1,len(image_files_4x))
        image_file_4x=image_files_4x[random_key_4x]
        
        img_good4x=Image.open(get_image_path(image_file_4x)).resize((70,70))
        zy_frameW44_img_good4x=ImageTk.PhotoImage(img_good4x)

        lbL_img_good4x=tk.Label(zy_frameW44,
                                image=zy_frameW44_img_good4x,
                                bg="SeaShell",
                                width=70, height=70)
        
        lbL_img_good4x.grid(row=0,
                            column=0,
                            pady=8,
                            ipadx=3,
                            ipady=1)
        lbL_img_good4x.image=zy_frameW44_img_good4x 
        
        image_files2_4x = {
        1: "good1_All correct_remove bg.png",
        2: "good2_All answers are correct_remove bg.png",
        3: "good3_En_Bingo_remove bg.png",
        4: "good4_You are excellent!_remove bg.png",
        5: "good5_Completely correct_remove bg.png",
        6: "good6_You got it right!_remove bg.png"}
        
        random_key1_4x=rd.randint(1,len(image_files2_4x))
        image_file2_4x=image_files2_4x[random_key1_4x]
        
        img_good1_4x=Image.open(get_image_path(image_file2_4x)).resize((180,40))
        zy_frameW44_img_good1_4x=ImageTk.PhotoImage(img_good1_4x)

        lbL_img_good1_4x=tk.Label(zy_frameW44,
                                  image=zy_frameW44_img_good1_4x,
                                  bg="SeaShell",
                                  width=200, height=50)
        
        lbL_img_good1_4x.grid(row=0,
                              column=1,
                              pady=8,
                              ipady=1)
        lbL_img_good1_4x.image=zy_frameW44_img_good1_4x 
        
        image_files3_4x = {
        1: "good71_Awesome!_remove bg.png",
        2: "good71_You are amazing!_remove bg.png",
        3: "good71_So impressive_remove bg.png",
        4: "good71_So smart!_remove bg.png",
        5: "good71_Super amazing!_remove bg.png",
        6: "good71_You are a genius!_remove bg.png"}
        
        random_key2_4x=rd.randint(1,len(image_files3_4x))
        image_file3_4x=image_files3_4x[random_key2_4x]
        
        img_good2_4x=Image.open(get_image_path(image_file3_4x)).resize((180,40))
        zy_frameW44_img_good2_4x=ImageTk.PhotoImage(img_good2_4x)

        lbL_img_good2_4x=tk.Label(zy_frameW44,
                                  image=zy_frameW44_img_good2_4x,
                                  bg="SeaShell",
                                  width=200, height=50)
        
        lbL_img_good2_4x.grid(row=0,
                              column=2,
                              pady=8,
                              ipady=1)
        lbL_img_good2_4x.image=zy_frameW44_img_good2_4x 
        
        '''稱讚的OK鈕'''
                
        img_cB1_4x=Image.open(get_image_path("ok_remove bg.png")).resize((50,50))  
        img_btNcB1_4x=ImageTk.PhotoImage(img_cB1_4x)

        btNcB1_4x=tk.Button(zy_frameW44,
                            image=img_btNcB1_4x,
                            bg="white",
                            relief="groove",
                            borderwidth=5,
                            width=50, height=50,
                            command=partial(
                                _hit_clearnAclose4x,
                                zy_wiN44))

        btNcB1_4x.grid(row=1,
                       columnspan=4,
                       pady=15,
                       ipadx=3,ipady=1)
        
        btNcB1_4x.image=img_btNcB1_4x
        
def _hit_clearnAclose4x(zy_wiN44):   
        global zy_wiN45
        '''
        ("提示",f"確定關閉{sizeS-1}格x{sizeS-1}格乘法練習視窗嗎？")
        '''
        
        zy_wiN45=tk.Toplevel(wiN)
        zy_wiN45.title("")
        zy_wiN45.geometry("500x300+450+200")
        zy_wiN45.configure(bg="white")
        
        zy_frameW45=tk.Frame(zy_wiN45,bg="white")
        zy_frameW45.pack(expand=True)    
        
        '''視窗：關閉乘法練習的視窗嗎？'''
        imgclosE_4x = Image.open(get_image_path("Are you sure close window_remove bg.png")).resize((350,60))
        zy_frameW45_imgclosE_4x = ImageTk.PhotoImage(imgclosE_4x)
        lbL_imgclosE_4x = tk.Label(zy_frameW45,
                                   image=zy_frameW45_imgclosE_4x,
                                   bg="white",
                                   width=400,height=60)
                          
        lbL_imgclosE_4x.grid(row=0,
                             columnspan=4,
                             pady=15,
                             ipadx=3,ipady=1)
        
        lbL_imgclosE_4x.image=zy_frameW45_imgclosE_4x

        '''確定鈕'''
        img_CB2_4x=Image.open(get_image_path("Confirm Button_1_remove bg.png")).resize((70,60))  
        zyfw45_CB2_4x=ImageTk.PhotoImage(img_CB2_4x)

        btNCB2_4x=tk.Button(zy_frameW45,
                            image=zyfw45_CB2_4x,
                            bg="white",
                            relief="groove",
                            borderwidth=3,
                            width=70, height=70,
                            command=lambda:(zy_wiN41.destroy(),
                                            zy_wiN44.destroy(),
                                            zy_wiN45.destroy()))
        
        btNCB2_4x.grid(row=1,
                       column=1,
                       padx=10,pady=15,
                       ipadx=1,ipady=1)
        
        btNCB2_4x.image=zyfw45_CB2_4x
        
        '''取消鈕'''
        img_canceL4x=Image.open(get_image_path("Cancel Button_remove bg.png")).resize((70,60))  
        zyfw45_canceL4x=ImageTk.PhotoImage(img_canceL4x)

        btNcanceL4x=tk.Button(zy_frameW45,
                              image=zyfw45_canceL4x,
                              bg="white",
                              relief="groove",
                              borderwidth=3,
                              width=70, height=70,
                              command=_hit_clAcl4x)
           
        btNcanceL4x.grid(row=1,
                       column=2,
                       padx=10,pady=15,
                       ipadx=1,ipady=1)
        
        btNcanceL4x.image=zyfw45_canceL4x

'''清除答案，在挑戰一次？'''
def _hit_clAcl4x(): #命名：Clear the answers and try the challenge again?
    
    zy_wiN46=tk.Toplevel(wiN)
    zy_wiN46.title("")
    zy_wiN46.geometry("500x300+450+200")
    zy_wiN46.configure(bg="white")
    
    zy_frameW46=tk.Frame(zy_wiN46,bg="white")
    zy_frameW46.pack(expand=True)    
    
    '''圖片：清除答案，在挑戰一次？'''
    imgclAcl_4x = Image.open(get_image_path("Clear answers and challenge again_remove bg.png")).resize((350,60))
    zy_frameW46_imgclAcl_4x = ImageTk.PhotoImage(imgclAcl_4x)
    lbL_imgclAcl_4x = tk.Label(zy_frameW46,
                               image=zy_frameW46_imgclAcl_4x,
                               bg="white",
                               width=400,height=60)
                      
    lbL_imgclAcl_4x.grid(row=0,
                         columnspan=4,
                         pady=15,
                         ipadx=3,ipady=1)
    
    lbL_imgclAcl_4x.image=zy_frameW46_imgclAcl_4x
    
    '''確定鈕'''
    img_CB3_4x=Image.open(get_image_path("Confirm Button_1_remove bg.png")).resize((70,60))  
    zyW46_CB3_4x=ImageTk.PhotoImage(img_CB3_4x)
    
    btNCB3_4x=tk.Button(zy_frameW46,
                        image=zyW46_CB3_4x,
                        bg="white",
                        relief="groove",
                        borderwidth=3,
                        width=70, height=70,
                        command=lambda:(
                            _hitclean4x(),
                            zy_wiN44.destroy(),
                            zy_wiN45.destroy(),                           
                            zy_wiN46.destroy()))

    btNCB3_4x.grid(row=1,
                columnspan=5,
                padx=10,pady=15,
                ipadx=1,ipady=1)
    
    btNCB3_4x.image=zyW46_CB3_4x


def _hitclean4x():
    for zy_entry4x,_ in zy_entrIes4x:
        zy_entry4x.delete(0,"end")


        
'''5x的def'''   
'''
第 "1" 個子視窗，所有 "B" utton子視窗，
乘法 5 X1-9的子視窗，從wiN"51"，1的乘法→ "5x"，命名 1B515x
'''
def _hit1B515x():
    global zy_entrIes5x,zy_answErs5x,zy_btN5xs,zy_wiN51
    zy_wiN51=tk.Toplevel(wiN)
    zy_wiN51.title("5 X 1-9")
    zy_wiN51.geometry("225x525+200+200")
    
    zy_frame1B515x=tk.Frame(zy_wiN51)
    zy_frame1B515x.pack()
    
    zy_entrIes5x=[]
    zy_answErs5x=[5,10,15,20,25,30,35,40,45]
    
    for n5x in range(1,10):
        zy_lbL_5x=tk.Label(zy_frame1B515x,text=f"5 X {n5x} =",
                           fg="black",bg="Salmon",
                           font=("Arial",12),
                           width=10,height=2)
        zy_lbL_5x.grid(row=n5x-1,column=0)
        
        zy_entrY_5x=tk.Entry(zy_frame1B515x,
                             font=("Arial",14),
                             width=3,bd=2,
                             justify="center")
        zy_entrY_5x.grid(row=n5x-1,column=1,padx=3,pady=3,
                   ipadx=6,ipady=8)
        zy_entrIes5x.append((zy_entrY_5x,zy_answErs5x[n5x-1]))
        
        
    '''Check answers Button 5x1-9'''
    '''圖片：對答案'''
    img_btN5xs=Image.open(get_image_path("1_Check answers_2_remove bg.png")).resize((125,30))  
    zyf51_btN5xs=ImageTk.PhotoImage(img_btN5xs)
    
    zy_btN5xs = tk.Button(zy_frame1B515x, 
                     image=zyf51_btN5xs,
                     relief="raised", 
                     borderwidth=3,
                     width=125, height=30,
                     command=partial(_hit5xs, zy_wiN51))    
    zy_btN5xs.grid(row=9,column=0,columnspan=2,pady=6,ipadx=5,ipady=5)
    zy_btN5xs.image=zyf51_btN5xs
    
'''5xs→1的乘法(5x)，送出(send)→5xs'''    
def _hit5xs(zy_wiN51):
    zy_errorS5x=[]
    try:
        for n5x,(zy_entry5x,zy_answErs5x) in enumerate(zy_entrIes5x):
            if int(zy_entry5x.get()) != zy_answErs5x:
                zy_errorS5x.append(f"  5 X { n5x+1 }  ㄉㄚˊ ㄢˋ ㄘㄨㄛˋ ㄨˋ !")

    except ValueError:
        global zy_wiN52
        #messagebox.showerror("提示","請勿輸入非數字 或 空白")
        '''視窗：第幾列第幾格錯誤，'''
        zy_wiN52=tk.Toplevel(wiN)
        zy_wiN52.title("")
        zy_wiN52.geometry("550x250+550+200")
        zy_wiN52.configure(bg="white")
        
        zy_frameW52=tk.Frame(zy_wiN52,bg="white")
        zy_frameW52.pack(expand=True)
        
        '''圖片：請勿空白或輸入不是數字的內容喔!'''
        imgdonot_empty5x=Image.open(get_image_path("don't empty_img_remove bg.png")).resize((430,50)) 
        zyfW52_imgdonot_empty5x=ImageTk.PhotoImage(imgdonot_empty5x)
        lbLimgdonot_empty5x=tk.Label(zy_frameW52,
                                     image=zyfW52_imgdonot_empty5x,
                                     borderwidth=4,
                                     width=450, height=75)
        
        lbLimgdonot_empty5x.grid(row=0,column=2,
                                 columnspan=2,
                                 pady=8,
                                 ipadx=3,ipady=1)
        lbLimgdonot_empty5x.image=zyfW52_imgdonot_empty5x

        
        '''製作check Button'''
        '''btNcB無法執行，問題是「#command=zy_wiN1.destroy()」'''
        '''command=zy_wiN1.destroy←不要"()"就可以執行了'''
        
        img_cB_5x=Image.open(get_image_path("ok_remove bg.png")).resize((50,50))  
        zyfW52_cB_5x=ImageTk.PhotoImage(img_cB_5x)

        btNcB_5x=tk.Button(zy_frameW52,
                           image=zyfW52_cB_5x,
                           bg="white",
                           relief="groove",
                           borderwidth=5,
                           width=50, height=50,
                           command=zy_wiN52.destroy)
                    

        btNcB_5x.grid(row=1,
                       columnspan=4,                       
                       pady=15,ipadx=3,ipady=1)
        
        btNcB_5x.image=zyfW52_cB_5x
        return

    if zy_errorS5x:
        '''視窗：第幾列第幾格錯誤!'''
        zy_wiN53=tk.Toplevel(wiN)
        zy_wiN53.title("")
        zy_wiN53.geometry("400x350+450+200")
        zy_wiN53.configure(bg="white")
        zy_wiN53.resizable(width=False, height=False)
        
        zy_frameW53=tk.Frame(zy_wiN53,
                            bg="MediumTurquoise",
                            height=90)
        
        zy_frameW53.pack(fill="x")
        
        
        '''圖片：Cue1_remove bg'''
        zy_imgCue5x = Image.open(get_image_path("Cue1_remove bg.png")).resize((120,40))
        zy_frameW53_imgCue5x = ImageTk.PhotoImage(zy_imgCue5x)
        zy_lbL_imgCue5x = tk.Label(zy_frameW53,
                                image=zy_frameW53_imgCue5x,
                                bg="MintCream",
                                relief="solid",
                                borderwidth=2,
                                width=124,height=44)
                        
        zy_lbL_imgCue5x.place(relx=0.5, rely=0.5,
                          anchor="center")                   
        zy_lbL_imgCue5x.image=zy_frameW53_imgCue5x
        
        
        zy_frameW53_1=tk.Frame(zy_wiN53,
                            bg="MediumTurquoise")                            
        zy_frameW53_1.pack(expand=True,fill="both")
        
        
        # 滾動條，用於文字框 # Scrollbar for the text box
        sBar_zyW53 = tk.Scrollbar(zy_frameW53_1, orient="vertical") # 建立垂直滾動條
        sBar_zyW53.pack(side=tk.RIGHT, fill="y")  # 將滾動條附加在右側 # Attach scrollbar to the right side
                    
        # zy_frameW7_1 裡面的文字框 # Text box inside zy_frameW7_1
        texT_zy_frameW53_1 = tk.Text(zy_frameW53_1,
                                    bg="#F0FFF0",
                                    wrap=tk.WORD, # 自動換行以單字為單位
                                    font=("標楷體", 14), 
                                    yscrollcommand=sBar_zyW53.set)  
                                    # 將文字框與滾動條連結 # Link Text box to scrollbar)
        texT_zy_frameW53_1.pack()

        
        # 將滾動條連結到文字框 # Link scrollbar to Text box
        sBar_zyW53.config(command=texT_zy_frameW53_1.yview)
        
        # 將錯誤訊息組合成單一字串，並以分隔線區隔
        zy_errorS5x_text = "\n  ----------------------------------\n".join(zy_errorS5x)
        texT_zy_frameW53_1.insert(tk.END,f"\n{zy_errorS5x_text}\n")
        texT_zy_frameW53_1.config(state="disabled")
        # 設定文字框為不可編輯狀態 # Disable editing of the Text box    
                     
    else:
        '''視窗：全部正確顯示'''
        global zy_wiN54
        zy_wiN54=tk.Toplevel(wiN)
        zy_wiN54.title("")
        zy_wiN54.geometry("550x270+450+200")
        zy_wiN54.configure(bg="SeaShell")                          
        
        zy_frameW54=tk.Frame(zy_wiN54,bg="SeaShell")                            
        zy_frameW54.pack(expand=True)

        image_files_5x = {
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
        
        random_key_5x=rd.randint(1,len(image_files_5x))
        image_file_5x=image_files_5x[random_key_5x]
        
        img_good5x=Image.open(get_image_path(image_file_5x)).resize((70,70))
        zy_frameW54_img_good5x=ImageTk.PhotoImage(img_good5x)

        lbL_img_good5x=tk.Label(zy_frameW54,
                                image=zy_frameW54_img_good5x,
                                bg="SeaShell",
                                width=70, height=70)
        
        lbL_img_good5x.grid(row=0,
                            column=0,
                            pady=8,
                            ipadx=3,
                            ipady=1)
        lbL_img_good5x.image=zy_frameW54_img_good5x 
        
        image_files2_5x = {
        1: "good1_All correct_remove bg.png",
        2: "good2_All answers are correct_remove bg.png",
        3: "good3_En_Bingo_remove bg.png",
        4: "good4_You are excellent!_remove bg.png",
        5: "good5_Completely correct_remove bg.png",
        6: "good6_You got it right!_remove bg.png"}
        
        random_key1_5x=rd.randint(1,len(image_files2_5x))
        image_file2_5x=image_files2_5x[random_key1_5x]
        
        img_good1_5x=Image.open(get_image_path(image_file2_5x)).resize((180,40))
        zy_frameW54_img_good1_5x=ImageTk.PhotoImage(img_good1_5x)

        lbL_img_good1_5x=tk.Label(zy_frameW54,
                                  image=zy_frameW54_img_good1_5x,
                                  bg="SeaShell",
                                  width=200, height=50)
        
        lbL_img_good1_5x.grid(row=0,
                              column=1,
                              pady=8,
                              ipady=1)
        lbL_img_good1_5x.image=zy_frameW54_img_good1_5x 
        
        image_files3_5x = {
        1: "good71_Awesome!_remove bg.png",
        2: "good71_You are amazing!_remove bg.png",
        3: "good71_So impressive_remove bg.png",
        4: "good71_So smart!_remove bg.png",
        5: "good71_Super amazing!_remove bg.png",
        6: "good71_You are a genius!_remove bg.png"}
        
        random_key2_5x=rd.randint(1,len(image_files3_5x))
        image_file3_5x=image_files3_5x[random_key2_5x]
        
        img_good2_5x=Image.open(get_image_path(image_file3_5x)).resize((180,40))
        zy_frameW54_img_good2_5x=ImageTk.PhotoImage(img_good2_5x)

        lbL_img_good2_5x=tk.Label(zy_frameW54,
                                  image=zy_frameW54_img_good2_5x,
                                  bg="SeaShell",
                                  width=200, height=50)
        
        lbL_img_good2_5x.grid(row=0,
                              column=2,
                              pady=8,
                              ipady=1)
        lbL_img_good2_5x.image=zy_frameW54_img_good2_5x 
        
        '''稱讚的OK鈕'''
                
        img_cB1_5x=Image.open(get_image_path("ok_remove bg.png")).resize((50,50))  
        img_btNcB1_5x=ImageTk.PhotoImage(img_cB1_5x)

        btNcB1_5x=tk.Button(zy_frameW54,
                            image=img_btNcB1_5x,
                            bg="white",
                            relief="groove",
                            borderwidth=5,
                            width=50, height=50,
                            command=partial(
                                _hit_clearnAclose5x,
                                zy_wiN54))

        btNcB1_5x.grid(row=1,
                       columnspan=4,
                       pady=15,
                       ipadx=3,ipady=1)
        
        btNcB1_5x.image=img_btNcB1_5x
        
def _hit_clearnAclose5x(zy_wiN54):   
        global zy_wiN55
        '''
        ("提示",f"確定關閉{sizeS-1}格x{sizeS-1}格乘法練習視窗嗎？")
        '''
        
        zy_wiN55=tk.Toplevel(wiN)
        zy_wiN55.title("")
        zy_wiN55.geometry("500x300+450+200")
        zy_wiN55.configure(bg="white")
        
        zy_frameW55=tk.Frame(zy_wiN55,bg="white")
        zy_frameW55.pack(expand=True)    
        
        '''視窗：關閉乘法練習的視窗嗎？'''
        imgclosE_5x = Image.open(get_image_path("Are you sure close window_remove bg.png")).resize((350,60))
        zy_frameW55_imgclosE_5x = ImageTk.PhotoImage(imgclosE_5x)
        lbL_imgclosE_5x = tk.Label(zy_frameW55,
                                   image=zy_frameW55_imgclosE_5x,
                                   bg="white",
                                   width=400,height=60)
                          
        lbL_imgclosE_5x.grid(row=0,
                             columnspan=4,
                             pady=15,
                             ipadx=3,ipady=1)
        
        lbL_imgclosE_5x.image=zy_frameW55_imgclosE_5x

        '''確定鈕'''
        img_CB2_5x=Image.open(get_image_path("Confirm Button_1_remove bg.png")).resize((70,60))  
        zyfw55_CB2_5x=ImageTk.PhotoImage(img_CB2_5x)

        btNCB2_5x=tk.Button(zy_frameW55,
                            image=zyfw55_CB2_5x,
                            bg="white",
                            relief="groove",
                            borderwidth=3,
                            width=70, height=70,
                            command=lambda:(zy_wiN51.destroy(),
                                            zy_wiN54.destroy(),
                                            zy_wiN55.destroy()))
        
        btNCB2_5x.grid(row=1,
                       column=1,
                       padx=10,pady=15,
                       ipadx=1,ipady=1)
        
        btNCB2_5x.image=zyfw55_CB2_5x
        
        '''取消鈕'''
        img_canceL5x=Image.open(get_image_path("Cancel Button_remove bg.png")).resize((70,60))  
        zyfw55_canceL5x=ImageTk.PhotoImage(img_canceL5x)

        btNcanceL5x=tk.Button(zy_frameW55,
                              image=zyfw55_canceL5x,
                              bg="white",
                              relief="groove",
                              borderwidth=3,
                              width=70, height=70,
                              command=_hit_clAcl5x)
           
        btNcanceL5x.grid(row=1,
                       column=2,
                       padx=10,pady=15,
                       ipadx=1,ipady=1)
        
        btNcanceL5x.image=zyfw55_canceL5x

'''清除答案，在挑戰一次？'''
def _hit_clAcl5x(): #命名：Clear the answers and try the challenge again?
    
    zy_wiN56=tk.Toplevel(wiN)
    zy_wiN56.title("")
    zy_wiN56.geometry("500x300+450+200")
    zy_wiN56.configure(bg="white")
    
    zy_frameW56=tk.Frame(zy_wiN56,bg="white")
    zy_frameW56.pack(expand=True)    
    
    '''圖片：清除答案，在挑戰一次？'''
    imgclAcl_5x = Image.open(get_image_path("Clear answers and challenge again_remove bg.png")).resize((350,60))
    zy_frameW56_imgclAcl_5x = ImageTk.PhotoImage(imgclAcl_5x)
    lbL_imgclAcl_5x = tk.Label(zy_frameW56,
                               image=zy_frameW56_imgclAcl_5x,
                               bg="white",
                               width=400,height=60)
                      
    lbL_imgclAcl_5x.grid(row=0,
                         columnspan=4,
                         pady=15,
                         ipadx=3,ipady=1)
    
    lbL_imgclAcl_5x.image=zy_frameW56_imgclAcl_5x
    
    '''確定鈕'''
    img_CB3_5x=Image.open(get_image_path("Confirm Button_1_remove bg.png")).resize((70,60))  
    zyW56_CB3_5x=ImageTk.PhotoImage(img_CB3_5x)
    
    btNCB3_5x=tk.Button(zy_frameW56,
                        image=zyW56_CB3_5x,
                        bg="white",
                        relief="groove",
                        borderwidth=3,
                        width=70, height=70,
                        command=lambda:(
                            _hitclean5x(),
                            zy_wiN54.destroy(),
                            zy_wiN55.destroy(),                           
                            zy_wiN56.destroy()))

    btNCB3_5x.grid(row=1,
                columnspan=5,
                padx=10,pady=15,
                ipadx=1,ipady=1)
    
    btNCB3_5x.image=zyW56_CB3_5x


def _hitclean5x():
    for zy_entry5x,_ in zy_entrIes5x:
        zy_entry5x.delete(0,"end")


        
'''6x的def'''   
'''
第 "1" 個子視窗，所有 "B" utton子視窗，
乘法 6 X1-9的子視窗，從wiN"61"，1的乘法→ "6x"，命名 1B616x
'''
def _hit1B616x():
    global zy_entrIes6x,zy_answErs6x,zy_btN6xs,zy_wiN61
    zy_wiN61=tk.Toplevel(wiN)
    zy_wiN61.title("6 X 1-9")
    zy_wiN61.geometry("225x525+200+200")
    
    zy_frame1B616x=tk.Frame(zy_wiN61)
    zy_frame1B616x.pack()
    
    zy_entrIes6x=[]
    zy_answErs6x=[6,12,18,24,30,36,42,48,54]
    
    for n6x in range(1,10):
        zy_lbL_6x=tk.Label(zy_frame1B616x,text=f"6 X {n6x} =",
                           fg="black",bg="Salmon",
                           font=("Arial",12),
                           width=10,height=2)
        zy_lbL_6x.grid(row=n6x-1,column=0)
        
        zy_entrY_6x=tk.Entry(zy_frame1B616x,
                             font=("Arial",14),
                             width=3,bd=2,
                             justify="center")
        zy_entrY_6x.grid(row=n6x-1,column=1,padx=3,pady=3,
                   ipadx=6,ipady=8)
        zy_entrIes6x.append((zy_entrY_6x,zy_answErs6x[n6x-1]))
        
        
    '''Check answers Button 6x1-9'''
    '''圖片：對答案'''
    img_btN6xs=Image.open(get_image_path("1_Check answers_2_remove bg.png")).resize((125,30))  
    zyf61_btN6xs=ImageTk.PhotoImage(img_btN6xs)
    
    zy_btN6xs = tk.Button(zy_frame1B616x, 
                     image=zyf61_btN6xs,
                     relief="raised", 
                     borderwidth=3,
                     width=125, height=30,
                     command=partial(_hit6xs, zy_wiN61))    
    zy_btN6xs.grid(row=9,column=0,columnspan=2,pady=6,ipadx=5,ipady=5)
    zy_btN6xs.image=zyf61_btN6xs
    
'''6xs→1的乘法(6x)，送出(send)→6xs'''    
def _hit6xs(zy_wiN61):
    zy_errorS6x=[]
    try:
        for n6x,(zy_entry6x,zy_answErs6x) in enumerate(zy_entrIes6x):
            if int(zy_entry6x.get()) != zy_answErs6x:
                zy_errorS6x.append(f"  6 X { n6x+1 }  ㄉㄚˊ ㄢˋ ㄘㄨㄛˋ ㄨˋ !")

    except ValueError:
        global zy_wiN62
        #messagebox.showerror("提示","請勿輸入非數字 或 空白")
        '''視窗：第幾列第幾格錯誤，'''
        zy_wiN62=tk.Toplevel(wiN)
        zy_wiN62.title("")
        zy_wiN62.geometry("550x250+550+200")
        zy_wiN62.configure(bg="white")
        
        zy_frameW62=tk.Frame(zy_wiN62,bg="white")
        zy_frameW62.pack(expand=True)
        
        '''圖片：請勿空白或輸入不是數字的內容喔!'''
        imgdonot_empty6x=Image.open(get_image_path("don't empty_img_remove bg.png")).resize((430,50)) 
        zyfW62_imgdonot_empty6x=ImageTk.PhotoImage(imgdonot_empty6x)
        lbLimgdonot_empty6x=tk.Label(zy_frameW62,
                                     image=zyfW62_imgdonot_empty6x,
                                     borderwidth=4,
                                     width=450, height=75)
        
        lbLimgdonot_empty6x.grid(row=0,column=2,
                                 columnspan=2,
                                 pady=8,
                                 ipadx=3,ipady=1)
        lbLimgdonot_empty6x.image=zyfW62_imgdonot_empty6x

        
        '''製作check Button'''
        '''btNcB無法執行，問題是「#command=zy_wiN1.destroy()」'''
        '''command=zy_wiN1.destroy←不要"()"就可以執行了'''
        
        img_cB_6x=Image.open(get_image_path("ok_remove bg.png")).resize((50,50))  
        zyfW62_cB_6x=ImageTk.PhotoImage(img_cB_6x)

        btNcB_6x=tk.Button(zy_frameW62,
                           image=zyfW62_cB_6x,
                           bg="white",
                           relief="groove",
                           borderwidth=5,
                           width=50, height=50,
                           command=zy_wiN62.destroy)
                    

        btNcB_6x.grid(row=1,
                      columnspan=4,
                      pady=15,ipadx=3,ipady=1)
        
        btNcB_6x.image=zyfW62_cB_6x
        return

    if zy_errorS6x:
        '''視窗：第幾列第幾格錯誤!'''
        zy_wiN63=tk.Toplevel(wiN)
        zy_wiN63.title("")
        zy_wiN63.geometry("400x350+450+200")
        zy_wiN63.configure(bg="white")
        zy_wiN63.resizable(width=False, height=False)
        
        zy_frameW63=tk.Frame(zy_wiN63,
                            bg="MediumTurquoise",
                            height=90)
        
        zy_frameW63.pack(fill="x")
        
        
        '''圖片：Cue1_remove bg'''
        zy_imgCue6x = Image.open(get_image_path("Cue1_remove bg.png")).resize((120,40))
        zy_frameW63_imgCue6x = ImageTk.PhotoImage(zy_imgCue6x)
        zy_lbL_imgCue6x = tk.Label(zy_frameW63,
                                image=zy_frameW63_imgCue6x,
                                bg="MintCream",
                                relief="solid",
                                borderwidth=2,
                                width=124,height=44)
                        
        zy_lbL_imgCue6x.place(relx=0.5, rely=0.5,
                          anchor="center")                   
        zy_lbL_imgCue6x.image=zy_frameW63_imgCue6x
        
        
        zy_frameW63_1=tk.Frame(zy_wiN63,
                            bg="MediumTurquoise")                            
        zy_frameW63_1.pack(expand=True,fill="both")
        
        
        # 滾動條，用於文字框 # Scrollbar for the text box
        sBar_zyW63 = tk.Scrollbar(zy_frameW63_1, orient="vertical") # 建立垂直滾動條
        sBar_zyW63.pack(side=tk.RIGHT, fill="y")  # 將滾動條附加在右側 # Attach scrollbar to the right side
                    
        # zy_frameW7_1 裡面的文字框 # Text box inside zy_frameW7_1
        texT_zy_frameW63_1 = tk.Text(zy_frameW63_1,
                                    bg="#F0FFF0",
                                    wrap=tk.WORD, # 自動換行以單字為單位
                                    font=("標楷體", 14), 
                                    yscrollcommand=sBar_zyW63.set)  
                                    # 將文字框與滾動條連結 # Link Text box to scrollbar)
        texT_zy_frameW63_1.pack()

        
        # 將滾動條連結到文字框 # Link scrollbar to Text box
        sBar_zyW63.config(command=texT_zy_frameW63_1.yview)
        
        # 將錯誤訊息組合成單一字串，並以分隔線區隔
        zy_errorS6x_text = "\n  ----------------------------------\n".join(zy_errorS6x)
        texT_zy_frameW63_1.insert(tk.END,f"\n{zy_errorS6x_text}\n")
        texT_zy_frameW63_1.config(state="disabled")
        # 設定文字框為不可編輯狀態 # Disable editing of the Text box    
                     
    else:
        '''視窗：全部正確顯示'''
        global zy_wiN64
        zy_wiN64=tk.Toplevel(wiN)
        zy_wiN64.title("")
        zy_wiN64.geometry("550x270+450+200")
        zy_wiN64.configure(bg="SeaShell")                          
        
        zy_frameW64=tk.Frame(zy_wiN64,bg="SeaShell")                            
        zy_frameW64.pack(expand=True)

        image_files_6x = {
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
        
        random_key_6x=rd.randint(1,len(image_files_6x))
        image_file_6x=image_files_6x[random_key_6x]
        
        img_good6x=Image.open(get_image_path(image_file_6x)).resize((70,70))
        zy_frameW64_img_good6x=ImageTk.PhotoImage(img_good6x)

        lbL_img_good6x=tk.Label(zy_frameW64,
                                image=zy_frameW64_img_good6x,
                                bg="SeaShell",
                                width=70, height=70)
        
        lbL_img_good6x.grid(row=0,
                            column=0,
                            pady=8,
                            ipadx=3,
                            ipady=1)
        lbL_img_good6x.image=zy_frameW64_img_good6x 
        
        image_files2_6x = {
        1: "good1_All correct_remove bg.png",
        2: "good2_All answers are correct_remove bg.png",
        3: "good3_En_Bingo_remove bg.png",
        4: "good4_You are excellent!_remove bg.png",
        5: "good5_Completely correct_remove bg.png",
        6: "good6_You got it right!_remove bg.png"}
        
        random_key1_6x=rd.randint(1,len(image_files2_6x))
        image_file2_6x=image_files2_6x[random_key1_6x]
        
        img_good1_6x=Image.open(get_image_path(image_file2_6x)).resize((180,40))
        zy_frameW64_img_good1_6x=ImageTk.PhotoImage(img_good1_6x)

        lbL_img_good1_6x=tk.Label(zy_frameW64,
                                  image=zy_frameW64_img_good1_6x,
                                  bg="SeaShell",
                                  width=200, height=50)
        
        lbL_img_good1_6x.grid(row=0,
                              column=1,
                              pady=8,
                              ipady=1)
        lbL_img_good1_6x.image=zy_frameW64_img_good1_6x 
        
        image_files3_6x = {
        1: "good71_Awesome!_remove bg.png",
        2: "good71_You are amazing!_remove bg.png",
        3: "good71_So impressive_remove bg.png",
        4: "good71_So smart!_remove bg.png",
        5: "good71_Super amazing!_remove bg.png",
        6: "good71_You are a genius!_remove bg.png"}
        
        random_key2_6x=rd.randint(1,len(image_files3_6x))
        image_file3_6x=image_files3_6x[random_key2_6x]
        
        img_good2_6x=Image.open(get_image_path(image_file3_6x)).resize((180,40))
        zy_frameW64_img_good2_6x=ImageTk.PhotoImage(img_good2_6x)

        lbL_img_good2_6x=tk.Label(zy_frameW64,
                                  image=zy_frameW64_img_good2_6x,
                                  bg="SeaShell",
                                  width=200, height=50)
        
        lbL_img_good2_6x.grid(row=0,
                              column=2,
                              pady=8,
                              ipady=1)
        lbL_img_good2_6x.image=zy_frameW64_img_good2_6x 
        
        '''稱讚的OK鈕'''
                
        img_cB1_6x=Image.open(get_image_path("ok_remove bg.png")).resize((50,50))  
        img_btNcB1_6x=ImageTk.PhotoImage(img_cB1_6x)

        btNcB1_6x=tk.Button(zy_frameW64,
                            image=img_btNcB1_6x,
                            bg="white",
                            relief="groove",
                            borderwidth=5,
                            width=50, height=50,
                            command=partial(
                                _hit_clearnAclose6x,
                                zy_wiN64))

        btNcB1_6x.grid(row=1,
                       columnspan=4,
                       pady=15,
                       ipadx=3,ipady=1)
        
        btNcB1_6x.image=img_btNcB1_6x
        
def _hit_clearnAclose6x(zy_wiN64):   
        global zy_wiN65
        '''
        ("提示",f"確定關閉{sizeS-1}格x{sizeS-1}格乘法練習視窗嗎？")
        '''
        
        zy_wiN65=tk.Toplevel(wiN)
        zy_wiN65.title("")
        zy_wiN65.geometry("500x300+450+200")
        zy_wiN65.configure(bg="white")
        
        zy_frameW65=tk.Frame(zy_wiN65,bg="white")
        zy_frameW65.pack(expand=True)    
        
        '''視窗：關閉乘法練習的視窗嗎？'''
        imgclosE_6x = Image.open(get_image_path("Are you sure close window_remove bg.png")).resize((350,60))
        zy_frameW65_imgclosE_6x = ImageTk.PhotoImage(imgclosE_6x)
        lbL_imgclosE_6x = tk.Label(zy_frameW65,
                                   image=zy_frameW65_imgclosE_6x,
                                   bg="white",
                                   width=400,height=60)
                          
        lbL_imgclosE_6x.grid(row=0,
                             columnspan=4,
                             pady=15,
                             ipadx=3,ipady=1)
        
        lbL_imgclosE_6x.image=zy_frameW65_imgclosE_6x

        '''確定鈕'''
        img_CB2_6x=Image.open(get_image_path("Confirm Button_1_remove bg.png")).resize((70,60))  
        zyfw65_CB2_6x=ImageTk.PhotoImage(img_CB2_6x)

        btNCB2_6x=tk.Button(zy_frameW65,
                            image=zyfw65_CB2_6x,
                            bg="white",
                            relief="groove",
                            borderwidth=3,
                            width=70, height=70,
                            command=lambda:(zy_wiN61.destroy(),
                                            zy_wiN64.destroy(),
                                            zy_wiN65.destroy()))
        
        btNCB2_6x.grid(row=1,
                       column=1,
                       padx=10,pady=15,
                       ipadx=1,ipady=1)
        
        btNCB2_6x.image=zyfw65_CB2_6x
        
        '''取消鈕'''
        img_canceL6x=Image.open(get_image_path("Cancel Button_remove bg.png")).resize((70,60))  
        zyfw65_canceL6x=ImageTk.PhotoImage(img_canceL6x)

        btNcanceL6x=tk.Button(zy_frameW65,
                              image=zyfw65_canceL6x,
                              bg="white",
                              relief="groove",
                              borderwidth=3,
                              width=70, height=70,
                              command=_hit_clAcl6x)
           
        btNcanceL6x.grid(row=1,
                       column=2,
                       padx=10,pady=15,
                       ipadx=1,ipady=1)
        
        btNcanceL6x.image=zyfw65_canceL6x

'''清除答案，在挑戰一次？'''
def _hit_clAcl6x(): #命名：Clear the answers and try the challenge again?
    
    zy_wiN66=tk.Toplevel(wiN)
    zy_wiN66.title("")
    zy_wiN66.geometry("500x300+450+200")
    zy_wiN66.configure(bg="white")
    
    zy_frameW66=tk.Frame(zy_wiN66,bg="white")
    zy_frameW66.pack(expand=True)    
    
    '''圖片：清除答案，在挑戰一次？'''
    imgclAcl_6x = Image.open(get_image_path("Clear answers and challenge again_remove bg.png")).resize((350,60))
    zy_frameW66_imgclAcl_6x = ImageTk.PhotoImage(imgclAcl_6x)
    lbL_imgclAcl_6x = tk.Label(zy_frameW66,
                               image=zy_frameW66_imgclAcl_6x,
                               bg="white",
                               width=400,height=60)
                      
    lbL_imgclAcl_6x.grid(row=0,
                         columnspan=4,
                         pady=15,
                         ipadx=3,ipady=1)
    
    lbL_imgclAcl_6x.image=zy_frameW66_imgclAcl_6x
    
    '''確定鈕'''
    img_CB3_6x=Image.open(get_image_path("Confirm Button_1_remove bg.png")).resize((70,60))  
    zyW66_CB3_6x=ImageTk.PhotoImage(img_CB3_6x)
    
    btNCB3_6x=tk.Button(zy_frameW66,
                        image=zyW66_CB3_6x,
                        bg="white",
                        relief="groove",
                        borderwidth=3,
                        width=70, height=70,
                        command=lambda:(
                            _hitclean6x(),
                            zy_wiN64.destroy(),
                            zy_wiN65.destroy(),                           
                            zy_wiN66.destroy()))

    btNCB3_6x.grid(row=1,
                columnspan=5,
                padx=10,pady=15,
                ipadx=1,ipady=1)
    
    btNCB3_6x.image=zyW66_CB3_6x


def _hitclean6x():
    for zy_entry6x,_ in zy_entrIes6x:
        zy_entry6x.delete(0,"end")

        
        
'''7x的def'''   
'''
第 "1" 個子視窗，所有 "B" utton子視窗，
乘法 7 X1-9的子視窗，從wiN"71"，1的乘法→ "7x"，命名 1B717x
'''
def _hit1B717x():
    global zy_entrIes7x,zy_answErs7x,zy_btN7xs,zy_wiN71
    zy_wiN71=tk.Toplevel(wiN)
    zy_wiN71.title("7 X 1-9")
    zy_wiN71.geometry("225x525+200+200")
    
    zy_frame1B717x=tk.Frame(zy_wiN71)
    zy_frame1B717x.pack()
    
    zy_entrIes7x=[]
    zy_answErs7x=[7,14,21,28,35,42,49,56,63]
    
    for n7x in range(1,10):
        zy_lbL_7x=tk.Label(zy_frame1B717x,text=f"7 X {n7x} =",
                           fg="black",bg="Salmon",
                           font=("Arial",12),
                           width=10,height=2)
        zy_lbL_7x.grid(row=n7x-1,column=0)
        
        zy_entrY_7x=tk.Entry(zy_frame1B717x,
                             font=("Arial",14),
                             width=3,bd=2,
                             justify="center")
        zy_entrY_7x.grid(row=n7x-1,column=1,padx=3,pady=3,
                   ipadx=6,ipady=8)
        zy_entrIes7x.append((zy_entrY_7x,zy_answErs7x[n7x-1]))
        
        
    '''Check answers Button 7 x 1-9'''
    '''圖片：對答案'''
    img_btN7xs=Image.open(get_image_path("1_Check answers_2_remove bg.png")).resize((125,30))  
    zyf71_btN7xs=ImageTk.PhotoImage(img_btN7xs)
    
    zy_btN7xs = tk.Button(zy_frame1B717x, 
                     image=zyf71_btN7xs,
                     relief="raised", 
                     borderwidth=3,
                     width=125, height=30,
                     command=partial(_hit7xs, zy_wiN71))    
    zy_btN7xs.grid(row=9,column=0,columnspan=2,pady=6,ipadx=5,ipady=5)
    zy_btN7xs.image=zyf71_btN7xs
 
    
'''7xs→1的乘法(7x)，送出(send)→7xs'''    
def _hit7xs(zy_wiN71):
    zy_errorS7x=[]
    try:
        for n7x,(zy_entry7x,zy_answErs7x) in enumerate(zy_entrIes7x):
            if int(zy_entry7x.get()) != zy_answErs7x:
                zy_errorS7x.append(f"  7 X { n7x+1 }  ㄉㄚˊ ㄢˋ ㄘㄨㄛˋ ㄨˋ !")

    except ValueError:
        global zy_wiN72
        #messagebox.showerror("提示","請勿輸入非數字 或 空白")
        '''視窗：第幾列第幾格錯誤，'''
        zy_wiN72=tk.Toplevel(wiN)
        zy_wiN72.title("")
        zy_wiN72.geometry("550x250+550+200")
        zy_wiN72.configure(bg="white")
        
        zy_frameW72=tk.Frame(zy_wiN72,bg="white")
        zy_frameW72.pack(expand=True)
        
        '''圖片：請勿空白或輸入不是數字的內容喔!'''
        imgdonot_empty7x=Image.open(get_image_path("don't empty_img_remove bg.png")).resize((430,50)) 
        zyfW72_imgdonot_empty7x=ImageTk.PhotoImage(imgdonot_empty7x)
        lbLimgdonot_empty7x=tk.Label(zy_frameW72,
                                     image=zyfW72_imgdonot_empty7x,
                                     borderwidth=4,
                                     width=450, height=75)
        
        lbLimgdonot_empty7x.grid(row=0,column=2,
                                 columnspan=2,
                                 pady=8,
                                 ipadx=3,ipady=1)
        lbLimgdonot_empty7x.image=zyfW72_imgdonot_empty7x

        
        '''製作check Button'''
        '''btNcB無法執行，問題是「#command=zy_wiN1.destroy()」'''
        '''command=zy_wiN1.destroy←不要"()"就可以執行了'''
        
        img_cB_7x=Image.open(get_image_path("ok_remove bg.png")).resize((50,50))  
        zyfW72_cB_7x=ImageTk.PhotoImage(img_cB_7x)

        btNcB_7x=tk.Button(zy_frameW72,
                           image=zyfW72_cB_7x,
                           bg="white",
                           relief="groove",
                           borderwidth=5,
                           width=50, height=50,
                           command=zy_wiN72.destroy)
                    

        btNcB_7x.grid(row=1,
                      columnspan=4,
                      pady=15,ipadx=3,ipady=1)
        
        btNcB_7x.image=zyfW72_cB_7x
        return

    if zy_errorS7x:
        '''視窗：第幾列第幾格錯誤!'''
        zy_wiN73=tk.Toplevel(wiN)
        zy_wiN73.title("")
        zy_wiN73.geometry("400x350+450+200")
        zy_wiN73.configure(bg="white")
        zy_wiN73.resizable(width=False, height=False)
        
        zy_frameW73=tk.Frame(zy_wiN73,
                            bg="MediumTurquoise",
                            height=90)
        
        zy_frameW73.pack(fill="x")
        
        
        '''圖片：Cue1_remove bg'''
        zy_imgCue7x = Image.open(get_image_path("Cue1_remove bg.png")).resize((120,40))
        zy_frameW73_imgCue7x = ImageTk.PhotoImage(zy_imgCue7x)
        zy_lbL_imgCue7x = tk.Label(zy_frameW73,
                                image=zy_frameW73_imgCue7x,
                                bg="MintCream",
                                relief="solid",
                                borderwidth=2,
                                width=124,height=44)
                        
        zy_lbL_imgCue7x.place(relx=0.5, rely=0.5,
                          anchor="center")                   
        zy_lbL_imgCue7x.image=zy_frameW73_imgCue7x
        
        
        zy_frameW73_1=tk.Frame(zy_wiN73,
                            bg="MediumTurquoise")                            
        zy_frameW73_1.pack(expand=True,fill="both")
        
        
        # 滾動條，用於文字框 # Scrollbar for the text box
        sBar_zyW73 = tk.Scrollbar(zy_frameW73_1, orient="vertical") # 建立垂直滾動條
        sBar_zyW73.pack(side=tk.RIGHT, fill="y")  # 將滾動條附加在右側 # Attach scrollbar to the right side
                    
        # zy_frameW7_1 裡面的文字框 # Text box inside zy_frameW7_1
        texT_zy_frameW73_1 = tk.Text(zy_frameW73_1,
                                    bg="#F0FFF0",
                                    wrap=tk.WORD, # 自動換行以單字為單位
                                    font=("標楷體", 14), 
                                    yscrollcommand=sBar_zyW73.set)  
                                    # 將文字框與滾動條連結 # Link Text box to scrollbar)
        texT_zy_frameW73_1.pack()

        
        # 將滾動條連結到文字框 # Link scrollbar to Text box
        sBar_zyW73.config(command=texT_zy_frameW73_1.yview)
        
        # 將錯誤訊息組合成單一字串，並以分隔線區隔
        zy_errorS7x_text = "\n  ----------------------------------\n".join(zy_errorS7x)
        texT_zy_frameW73_1.insert(tk.END,f"\n{zy_errorS7x_text}\n")
        texT_zy_frameW73_1.config(state="disabled")
        # 設定文字框為不可編輯狀態 # Disable editing of the Text box    
                     
    else:
        '''視窗：全部正確顯示'''
        global zy_wiN74
        zy_wiN74=tk.Toplevel(wiN)
        zy_wiN74.title("")
        zy_wiN74.geometry("550x270+450+200")
        zy_wiN74.configure(bg="SeaShell")                          
        
        zy_frameW74=tk.Frame(zy_wiN74,bg="SeaShell")                            
        zy_frameW74.pack(expand=True)

        image_files_7x = {
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
        
        random_key_7x=rd.randint(1,len(image_files_7x))
        image_file_7x=image_files_7x[random_key_7x]
        
        img_good7x=Image.open(get_image_path(image_file_7x)).resize((70,70))
        zy_frameW74_img_good7x=ImageTk.PhotoImage(img_good7x)

        lbL_img_good7x=tk.Label(zy_frameW74,
                                image=zy_frameW74_img_good7x,
                                bg="SeaShell",
                                width=70, height=70)
        
        lbL_img_good7x.grid(row=0,
                            column=0,
                            pady=8,
                            ipadx=3,
                            ipady=1)
        lbL_img_good7x.image=zy_frameW74_img_good7x 
        
        image_files2_7x = {
        1: "good1_All correct_remove bg.png",
        2: "good2_All answers are correct_remove bg.png",
        3: "good3_En_Bingo_remove bg.png",
        4: "good4_You are excellent!_remove bg.png",
        5: "good5_Completely correct_remove bg.png",
        6: "good6_You got it right!_remove bg.png"}
        
        random_key1_7x=rd.randint(1,len(image_files2_7x))
        image_file2_7x=image_files2_7x[random_key1_7x]
        
        img_good1_7x=Image.open(get_image_path(image_file2_7x)).resize((180,40))
        zy_frameW74_img_good1_7x=ImageTk.PhotoImage(img_good1_7x)

        lbL_img_good1_7x=tk.Label(zy_frameW74,
                                  image=zy_frameW74_img_good1_7x,
                                  bg="SeaShell",
                                  width=200, height=50)
        
        lbL_img_good1_7x.grid(row=0,
                              column=1,
                              pady=8,
                              ipady=1)
        lbL_img_good1_7x.image=zy_frameW74_img_good1_7x 
        
        image_files3_7x = {
        1: "good71_Awesome!_remove bg.png",
        2: "good71_You are amazing!_remove bg.png",
        3: "good71_So impressive_remove bg.png",
        4: "good71_So smart!_remove bg.png",
        5: "good71_Super amazing!_remove bg.png",
        6: "good71_You are a genius!_remove bg.png"}
        
        random_key2_7x=rd.randint(1,len(image_files3_7x))
        image_file3_7x=image_files3_7x[random_key2_7x]
        
        img_good2_7x=Image.open(get_image_path(image_file3_7x)).resize((180,40))
        zy_frameW74_img_good2_7x=ImageTk.PhotoImage(img_good2_7x)

        lbL_img_good2_7x=tk.Label(zy_frameW74,
                                  image=zy_frameW74_img_good2_7x,
                                  bg="SeaShell",
                                  width=200, height=50)
        
        lbL_img_good2_7x.grid(row=0,
                              column=2,
                              pady=8,
                              ipady=1)
        lbL_img_good2_7x.image=zy_frameW74_img_good2_7x 
        
        '''稱讚的OK鈕'''
                
        img_cB1_7x=Image.open(get_image_path("ok_remove bg.png")).resize((50,50))  
        img_btNcB1_7x=ImageTk.PhotoImage(img_cB1_7x)

        btNcB1_7x=tk.Button(zy_frameW74,
                            image=img_btNcB1_7x,
                            bg="white",
                            relief="groove",
                            borderwidth=5,
                            width=50, height=50,
                            command=partial(
                                _hit_clearnAclose7x,
                                zy_wiN74))

        btNcB1_7x.grid(row=1,
                       columnspan=4,
                       pady=15,
                       ipadx=3,ipady=1)
        
        btNcB1_7x.image=img_btNcB1_7x
        
def _hit_clearnAclose7x(zy_wiN74):   
        global zy_wiN75
        '''
        ("提示",f"確定關閉{sizeS-1}格x{sizeS-1}格乘法練習視窗嗎？")
        '''
        
        zy_wiN75=tk.Toplevel(wiN)
        zy_wiN75.title("")
        zy_wiN75.geometry("500x300+450+200")
        zy_wiN75.configure(bg="white")
        
        zy_frameW75=tk.Frame(zy_wiN75,bg="white")
        zy_frameW75.pack(expand=True)    
        
        '''視窗：關閉乘法練習的視窗嗎？'''
        imgclosE_7x = Image.open(get_image_path("Are you sure close window_remove bg.png")).resize((350,60))
        zy_frameW75_imgclosE_7x = ImageTk.PhotoImage(imgclosE_7x)
        lbL_imgclosE_7x = tk.Label(zy_frameW75,
                                   image=zy_frameW75_imgclosE_7x,
                                   bg="white",
                                   width=400,height=60)
                          
        lbL_imgclosE_7x.grid(row=0,
                             columnspan=4,
                             pady=15,
                             ipadx=3,ipady=1)
        
        lbL_imgclosE_7x.image=zy_frameW75_imgclosE_7x

        '''確定鈕'''
        img_CB2_7x=Image.open(get_image_path("Confirm Button_1_remove bg.png")).resize((70,60))  
        zyfw75_CB2_7x=ImageTk.PhotoImage(img_CB2_7x)

        btNCB2_7x=tk.Button(zy_frameW75,
                            image=zyfw75_CB2_7x,
                            bg="white",
                            relief="groove",
                            borderwidth=3,
                            width=70, height=70,
                            command=lambda:(zy_wiN71.destroy(),
                                            zy_wiN74.destroy(),
                                            zy_wiN75.destroy()))
        
        btNCB2_7x.grid(row=1,
                       column=1,
                       padx=10,pady=15,
                       ipadx=1,ipady=1)
        
        btNCB2_7x.image=zyfw75_CB2_7x
        
        '''取消鈕'''
        img_canceL7x=Image.open(get_image_path("Cancel Button_remove bg.png")).resize((70,60))  
        zyfw75_canceL7x=ImageTk.PhotoImage(img_canceL7x)

        btNcanceL7x=tk.Button(zy_frameW75,
                              image=zyfw75_canceL7x,
                              bg="white",
                              relief="groove",
                              borderwidth=3,
                              width=70, height=70,
                              command=_hit_clAcl7x)
           
        btNcanceL7x.grid(row=1,
                       column=2,
                       padx=10,pady=15,
                       ipadx=1,ipady=1)
        
        btNcanceL7x.image=zyfw75_canceL7x

'''清除答案，在挑戰一次？'''
def _hit_clAcl7x(): #命名：Clear the answers and try the challenge again?
    
    zy_wiN76=tk.Toplevel(wiN)
    zy_wiN76.title("")
    zy_wiN76.geometry("500x300+450+200")
    zy_wiN76.configure(bg="white")
    
    zy_frameW76=tk.Frame(zy_wiN76,bg="white")
    zy_frameW76.pack(expand=True)    
    
    '''圖片：清除答案，在挑戰一次？'''
    imgclAcl_7x = Image.open(get_image_path("Clear answers and challenge again_remove bg.png")).resize((350,60))
    zy_frameW76_imgclAcl_7x = ImageTk.PhotoImage(imgclAcl_7x)
    lbL_imgclAcl_7x = tk.Label(zy_frameW76,
                               image=zy_frameW76_imgclAcl_7x,
                               bg="white",
                               width=400,height=60)
                      
    lbL_imgclAcl_7x.grid(row=0,
                         columnspan=4,
                         pady=15,
                         ipadx=3,ipady=1)
    
    lbL_imgclAcl_7x.image=zy_frameW76_imgclAcl_7x
    
    '''確定鈕'''
    img_CB3_7x=Image.open(get_image_path("Confirm Button_1_remove bg.png")).resize((70,60))  
    zyW76_CB3_7x=ImageTk.PhotoImage(img_CB3_7x)
    
    btNCB3_7x=tk.Button(zy_frameW76,
                        image=zyW76_CB3_7x,
                        bg="white",
                        relief="groove",
                        borderwidth=3,
                        width=70, height=70,
                        command=lambda:(
                            _hitclean7x(),
                            zy_wiN74.destroy(),
                            zy_wiN75.destroy(),                           
                            zy_wiN76.destroy()))

    btNCB3_7x.grid(row=1,
                columnspan=5,
                padx=10,pady=15,
                ipadx=1,ipady=1)
    
    btNCB3_7x.image=zyW76_CB3_7x


def _hitclean7x():
    for zy_entry7x,_ in zy_entrIes7x:
        zy_entry7x.delete(0,"end")
         

'''8x的def'''   
'''
第 "1" 個子視窗，所有 "B" utton子視窗，
乘法 8 X 1-9的子視窗，從wiN"81"，1的乘法→ "8x"，命名 1B818x
'''
def _hit1B818x():
    global zy_entrIes8x,zy_answErs8x,zy_btN8xs,zy_wiN81
    zy_wiN81=tk.Toplevel(wiN)
    zy_wiN81.title("8 X 1-9")
    zy_wiN81.geometry("225x525+200+200")
    
    zy_frame1B818x=tk.Frame(zy_wiN81)
    zy_frame1B818x.pack()
    
    zy_entrIes8x=[]
    zy_answErs8x=[8,16,24,32,40,48,56,64,72]
    
    for n8x in range(1,10):
        zy_lbL_8x=tk.Label(zy_frame1B818x,text=f"8 X {n8x} =",
                           fg="black",bg="Salmon",
                           font=("Arial",12),
                           width=10,height=2)
        zy_lbL_8x.grid(row=n8x-1,column=0)
        
        zy_entrY_8x=tk.Entry(zy_frame1B818x,
                             font=("Arial",14),
                             width=3,bd=2,
                             justify="center")
        zy_entrY_8x.grid(row=n8x-1,column=1,
                         padx=3,pady=3,
                         ipadx=6,ipady=8)
        zy_entrIes8x.append((zy_entrY_8x,zy_answErs8x[n8x-1]))
        
        
    '''Check answers Button 8x1-9'''
    '''圖片：對答案'''
    img_btN8xs=Image.open(get_image_path("1_Check answers_2_remove bg.png")).resize((125,30))  
    zyf81_btN8xs=ImageTk.PhotoImage(img_btN8xs)
    
    zy_btN8xs = tk.Button(zy_frame1B818x, 
                     image=zyf81_btN8xs,
                     relief="raised", 
                     borderwidth=3,
                     width=125, height=30,
                     command=partial(_hit8xs, zy_wiN81))    
    zy_btN8xs.grid(row=9,column=0,columnspan=2,pady=6,ipadx=5,ipady=5)
    zy_btN8xs.image=zyf81_btN8xs
    
'''8xs→1的乘法(8x)，送出(send)→8xs'''    
def _hit8xs(zy_wiN81):
    zy_errorS8x=[]
    try:
        for n8x,(zy_entry8x,zy_answErs8x) in enumerate(zy_entrIes8x):
            if int(zy_entry8x.get()) != zy_answErs8x:
                zy_errorS8x.append(f"  8 X { n8x+1 }  ㄉㄚˊ ㄢˋ ㄘㄨㄛˋ ㄨˋ !")

    except ValueError:
        global zy_wiN82
        #messagebox.showerror("提示","請勿輸入非數字 或 空白")
        '''視窗：第幾列第幾格錯誤，'''
        zy_wiN82=tk.Toplevel(wiN)
        zy_wiN82.title("")
        zy_wiN82.geometry("550x250+550+200")
        zy_wiN82.configure(bg="white")
        
        zy_frameW82=tk.Frame(zy_wiN82,bg="white")
        zy_frameW82.pack(expand=True)
        
        '''圖片：請勿空白或輸入不是數字的內容喔!'''
        imgdonot_empty8x=Image.open(get_image_path("don't empty_img_remove bg.png")).resize((430,50)) 
        zyfW82_imgdonot_empty8x=ImageTk.PhotoImage(imgdonot_empty8x)
        lbLimgdonot_empty8x=tk.Label(zy_frameW82,
                                     image=zyfW82_imgdonot_empty8x,
                                     borderwidth=4,
                                     width=450, height=75)
        
        lbLimgdonot_empty8x.grid(row=0,column=2,
                                 columnspan=2,
                                 pady=8,
                                 ipadx=3,ipady=1)
        lbLimgdonot_empty8x.image=zyfW82_imgdonot_empty8x

        
        '''製作check Button'''
        '''btNcB無法執行，問題是「#command=zy_wiN1.destroy()」'''
        '''command=zy_wiN1.destroy←不要"()"就可以執行了'''
        
        img_cB_8x=Image.open(get_image_path("ok_remove bg.png")).resize((50,50))  
        zyfW82_cB_8x=ImageTk.PhotoImage(img_cB_8x)

        btNcB_8x=tk.Button(zy_frameW82,
                            image=zyfW82_cB_8x,
                            bg="white",
                            relief="groove",
                            borderwidth=5,
                            width=50, height=50,
                            command=zy_wiN82.destroy)
                    

        btNcB_8x.grid(row=1,
                       columnspan=4,                       
                       pady=15,ipadx=3,ipady=1)
        
        btNcB_8x.image=zyfW82_cB_8x
        return

    if zy_errorS8x:
        '''視窗：第幾列第幾格錯誤!'''
        zy_wiN83=tk.Toplevel(wiN)
        zy_wiN83.title("")
        zy_wiN83.geometry("400x350+450+200")
        zy_wiN83.configure(bg="white")
        zy_wiN83.resizable(width=False, height=False)
        
        zy_frameW83=tk.Frame(zy_wiN83,
                            bg="MediumTurquoise",
                            height=90)
        
        zy_frameW83.pack(fill="x")
        
        
        '''圖片：Cue1_remove bg'''
        zy_imgCue8x = Image.open(get_image_path("Cue1_remove bg.png")).resize((120,40))
        zy_frameW83_imgCue8x = ImageTk.PhotoImage(zy_imgCue8x)
        zy_lbL_imgCue8x = tk.Label(zy_frameW83,
                                image=zy_frameW83_imgCue8x,
                                bg="MintCream",
                                relief="solid",
                                borderwidth=2,
                                width=124,height=44)
                        
        zy_lbL_imgCue8x.place(relx=0.5, rely=0.5,
                          anchor="center")                   
        zy_lbL_imgCue8x.image=zy_frameW83_imgCue8x
        
        
        zy_frameW83_1=tk.Frame(zy_wiN83,
                            bg="MediumTurquoise")                            
        zy_frameW83_1.pack(expand=True,fill="both")
        
        
        # 滾動條，用於文字框 # Scrollbar for the text box
        sBar_zyW83 = tk.Scrollbar(zy_frameW83_1, orient="vertical") # 建立垂直滾動條
        sBar_zyW83.pack(side=tk.RIGHT, fill="y")  # 將滾動條附加在右側 # Attach scrollbar to the right side
                    
        # zy_frameW7_1 裡面的文字框 # Text box inside zy_frameW7_1
        texT_zy_frameW83_1 = tk.Text(zy_frameW83_1,
                                    bg="#F0FFF0",
                                    wrap=tk.WORD, # 自動換行以單字為單位
                                    font=("標楷體", 14), 
                                    yscrollcommand=sBar_zyW83.set)  
                                    # 將文字框與滾動條連結 # Link Text box to scrollbar)
        texT_zy_frameW83_1.pack()

        
        # 將滾動條連結到文字框 # Link scrollbar to Text box
        sBar_zyW83.config(command=texT_zy_frameW83_1.yview)
        
        # 將錯誤訊息組合成單一字串，並以分隔線區隔
        zy_errorS8x_text = "\n  ----------------------------------\n".join(zy_errorS8x)
        texT_zy_frameW83_1.insert(tk.END,f"\n{zy_errorS8x_text}\n")
        texT_zy_frameW83_1.config(state="disabled")
        # 設定文字框為不可編輯狀態 # Disable editing of the Text box    
                     
    else:
        '''視窗：全部正確顯示'''
        global zy_wiN84
        zy_wiN84=tk.Toplevel(wiN)
        zy_wiN84.title("")
        zy_wiN84.geometry("550x270+450+200")
        zy_wiN84.configure(bg="SeaShell")                          
        
        zy_frameW84=tk.Frame(zy_wiN84,bg="SeaShell")                            
        zy_frameW84.pack(expand=True)

        image_files_8x = {
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
        
        random_key_8x=rd.randint(1,len(image_files_8x))
        image_file_8x=image_files_8x[random_key_8x]
        
        img_good8x=Image.open(get_image_path(image_file_8x)).resize((70,70))
        zy_frameW84_img_good8x=ImageTk.PhotoImage(img_good8x)

        lbL_img_good8x=tk.Label(zy_frameW84,
                                image=zy_frameW84_img_good8x,
                                bg="SeaShell",
                                width=70, height=70)
        
        lbL_img_good8x.grid(row=0,
                            column=0,
                            pady=8,
                            ipadx=3,
                            ipady=1)
        lbL_img_good8x.image=zy_frameW84_img_good8x 
        
        image_files2_8x = {
        1: "good1_All correct_remove bg.png",
        2: "good2_All answers are correct_remove bg.png",
        3: "good3_En_Bingo_remove bg.png",
        4: "good4_You are excellent!_remove bg.png",
        5: "good5_Completely correct_remove bg.png",
        6: "good6_You got it right!_remove bg.png"}
        
        random_key1_8x=rd.randint(1,len(image_files2_8x))
        image_file2_8x=image_files2_8x[random_key1_8x]
        
        img_good1_8x=Image.open(get_image_path(image_file2_8x)).resize((180,40))
        zy_frameW84_img_good1_8x=ImageTk.PhotoImage(img_good1_8x)

        lbL_img_good1_8x=tk.Label(zy_frameW84,
                                  image=zy_frameW84_img_good1_8x,
                                  bg="SeaShell",
                                  width=200, height=50)
        
        lbL_img_good1_8x.grid(row=0,
                              column=1,
                              pady=8,
                              ipady=1)
        lbL_img_good1_8x.image=zy_frameW84_img_good1_8x 
        
        image_files3_8x = {
        1: "good71_Awesome!_remove bg.png",
        2: "good71_You are amazing!_remove bg.png",
        3: "good71_So impressive_remove bg.png",
        4: "good71_So smart!_remove bg.png",
        5: "good71_Super amazing!_remove bg.png",
        6: "good71_You are a genius!_remove bg.png"}
        
        random_key2_8x=rd.randint(1,len(image_files3_8x))
        image_file3_8x=image_files3_8x[random_key2_8x]
        
        img_good2_8x=Image.open(get_image_path(image_file3_8x)).resize((180,40))
        zy_frameW84_img_good2_8x=ImageTk.PhotoImage(img_good2_8x)

        lbL_img_good2_8x=tk.Label(zy_frameW84,
                                  image=zy_frameW84_img_good2_8x,
                                  bg="SeaShell",
                                  width=200, height=50)
        
        lbL_img_good2_8x.grid(row=0,
                              column=2,
                              pady=8,
                              ipady=1)
        lbL_img_good2_8x.image=zy_frameW84_img_good2_8x 
        
        '''稱讚的OK鈕'''
                
        img_cB1_8x=Image.open(get_image_path("ok_remove bg.png")).resize((50,50))  
        img_btNcB1_8x=ImageTk.PhotoImage(img_cB1_8x)

        btNcB1_8x=tk.Button(zy_frameW84,
                            image=img_btNcB1_8x,
                            bg="white",
                            relief="groove",
                            borderwidth=5,
                            width=50, height=50,
                            command=partial(
                                _hit_clearnAclose8x,
                                zy_wiN84))

        btNcB1_8x.grid(row=1,
                       columnspan=4,
                       pady=15,
                       ipadx=3,ipady=1)
        
        btNcB1_8x.image=img_btNcB1_8x
        
def _hit_clearnAclose8x(zy_wiN84):   
        global zy_wiN85
        '''
        ("提示",f"確定關閉{sizeS-1}格x{sizeS-1}格乘法練習視窗嗎？")
        '''
        
        zy_wiN85=tk.Toplevel(wiN)
        zy_wiN85.title("")
        zy_wiN85.geometry("500x300+450+200")
        zy_wiN85.configure(bg="white")
        
        zy_frameW85=tk.Frame(zy_wiN85,bg="white")
        zy_frameW85.pack(expand=True)    
        
        '''視窗：關閉乘法練習的視窗嗎？'''
        imgclosE_8x = Image.open(get_image_path("Are you sure close window_remove bg.png")).resize((350,60))
        zy_frameW85_imgclosE_8x = ImageTk.PhotoImage(imgclosE_8x)
        lbL_imgclosE_8x = tk.Label(zy_frameW85,
                                   image=zy_frameW85_imgclosE_8x,
                                   bg="white",
                                   width=400,height=60)
                          
        lbL_imgclosE_8x.grid(row=0,
                             columnspan=4,
                             pady=15,
                             ipadx=3,ipady=1)
        
        lbL_imgclosE_8x.image=zy_frameW85_imgclosE_8x

        '''確定鈕'''
        img_CB2_8x=Image.open(get_image_path("Confirm Button_1_remove bg.png")).resize((70,60))  
        zyfw85_CB2_8x=ImageTk.PhotoImage(img_CB2_8x)

        btNCB2_8x=tk.Button(zy_frameW85,
                            image=zyfw85_CB2_8x,
                            bg="white",
                            relief="groove",
                            borderwidth=3,
                            width=70, height=70,
                            command=lambda:(zy_wiN81.destroy(),
                                            zy_wiN84.destroy(),
                                            zy_wiN85.destroy()))
        
        btNCB2_8x.grid(row=1,
                       column=1,
                       padx=10,pady=15,
                       ipadx=1,ipady=1)
        
        btNCB2_8x.image=zyfw85_CB2_8x
        
        '''取消鈕'''
        img_canceL8x=Image.open(get_image_path("Cancel Button_remove bg.png")).resize((70,60))  
        zyfw85_canceL8x=ImageTk.PhotoImage(img_canceL8x)

        btNcanceL8x=tk.Button(zy_frameW85,
                              image=zyfw85_canceL8x,
                              bg="white",
                              relief="groove",
                              borderwidth=3,
                              width=70, height=70,
                              command=_hit_clAcl8x)
           
        btNcanceL8x.grid(row=1,
                       column=2,
                       padx=10,pady=15,
                       ipadx=1,ipady=1)
        
        btNcanceL8x.image=zyfw85_canceL8x

'''清除答案，在挑戰一次？'''
def _hit_clAcl8x(): #命名：Clear the answers and try the challenge again?
    
    zy_wiN86=tk.Toplevel(wiN)
    zy_wiN86.title("")
    zy_wiN86.geometry("500x300+450+200")
    zy_wiN86.configure(bg="white")
    
    zy_frameW86=tk.Frame(zy_wiN86,bg="white")
    zy_frameW86.pack(expand=True)    
    
    '''圖片：清除答案，在挑戰一次？'''
    imgclAcl_8x = Image.open(get_image_path("Clear answers and challenge again_remove bg.png")).resize((350,60))
    zy_frameW86_imgclAcl_8x = ImageTk.PhotoImage(imgclAcl_8x)
    lbL_imgclAcl_8x = tk.Label(zy_frameW86,
                               image=zy_frameW86_imgclAcl_8x,
                               bg="white",
                               width=400,height=60)
                      
    lbL_imgclAcl_8x.grid(row=0,
                         columnspan=4,
                         pady=15,
                         ipadx=3,ipady=1)
    
    lbL_imgclAcl_8x.image=zy_frameW86_imgclAcl_8x
    
    '''確定鈕'''
    img_CB3_8x=Image.open(get_image_path("Confirm Button_1_remove bg.png")).resize((70,60))  
    zyW86_CB3_8x=ImageTk.PhotoImage(img_CB3_8x)
    
    btNCB3_8x=tk.Button(zy_frameW86,
                        image=zyW86_CB3_8x,
                        bg="white",
                        relief="groove",
                        borderwidth=3,
                        width=70, height=70,
                        command=lambda:(
                            _hitclean8x(),
                            zy_wiN84.destroy(),
                            zy_wiN85.destroy(),                           
                            zy_wiN86.destroy()))

    btNCB3_8x.grid(row=1,
                columnspan=5,
                padx=10,pady=15,
                ipadx=1,ipady=1)
    
    btNCB3_8x.image=zyW86_CB3_8x


def _hitclean8x():
    for zy_entry8x,_ in zy_entrIes8x:
        zy_entry8x.delete(0,"end")

        
             
'''9x的def'''   
'''
第 "1" 個子視窗，所有 "B" utton子視窗，
乘法 9 X 1-9的子視窗，從wiN"91"，1的乘法→ "9x"，命名 1B919x
'''
def _hit1B919x():
    global zy_entrIes9x,zy_answErs9x,zy_btN9xs,zy_wiN91
    zy_wiN91=tk.Toplevel(wiN)
    zy_wiN91.title("9 X 1-9")
    zy_wiN91.geometry("225x525+200+200")
    
    zy_frame1B919x=tk.Frame(zy_wiN91)
    zy_frame1B919x.pack()
    
    zy_entrIes9x=[]
    zy_answErs9x=[9,18,27,36,45,54,63,72,81]
    
    for n9x in range(1,10):
        zy_lbL_9x=tk.Label(zy_frame1B919x,text=f"9 X {n9x} =",
                           fg="black",bg="Salmon",
                           font=("Arial",12),
                           width=10,height=2)
        zy_lbL_9x.grid(row=n9x-1,column=0)
        
        zy_entrY_9x=tk.Entry(zy_frame1B919x,
                             font=("Arial",14),
                             width=3,bd=2,
                             justify="center")
        zy_entrY_9x.grid(row=n9x-1,column=1,
                         padx=3,pady=3,
                         ipadx=6,ipady=8)
        zy_entrIes9x.append((zy_entrY_9x,zy_answErs9x[n9x-1]))
        
        
    '''Check answers Button 9x1-9'''
    '''圖片：對答案'''
    img_btN9xs=Image.open(get_image_path("1_Check answers_2_remove bg.png")).resize((125,30))  
    zyf91_btN9xs=ImageTk.PhotoImage(img_btN9xs)
    
    zy_btN9xs = tk.Button(zy_frame1B919x, 
                     image=zyf91_btN9xs,
                     relief="raised", 
                     borderwidth=3,
                     width=125, height=30,
                     command=partial(_hit9xs, zy_wiN91))    
    zy_btN9xs.grid(row=9,column=0,columnspan=2,pady=6,ipadx=5,ipady=5)
    zy_btN9xs.image=zyf91_btN9xs
    
'''9xs→1的乘法(9x)，送出(send)→9xs'''    
def _hit9xs(zy_wiN91):
    zy_errorS9x=[]
    try:
        for n9x,(zy_entry9x,zy_answErs9x) in enumerate(zy_entrIes9x):
            if int(zy_entry9x.get()) != zy_answErs9x:
                zy_errorS9x.append(f"  9 X { n9x+1 }  ㄉㄚˊ ㄢˋ ㄘㄨㄛˋ ㄨˋ !")

    except ValueError:
        global zy_wiN92
        #messagebox.showerror("提示","請勿輸入非數字 或 空白")
        '''視窗：第幾列第幾格錯誤，'''
        zy_wiN92=tk.Toplevel(wiN)
        zy_wiN92.title("")
        zy_wiN92.geometry("550x250+550+200")
        zy_wiN92.configure(bg="white")
        
        zy_frameW92=tk.Frame(zy_wiN92,bg="white")
        zy_frameW92.pack(expand=True)
        
        '''圖片：請勿空白或輸入不是數字的內容喔!'''
        imgdonot_empty9x=Image.open(get_image_path("don't empty_img_remove bg.png")).resize((430,50)) 
        zyfW92_imgdonot_empty9x=ImageTk.PhotoImage(imgdonot_empty9x)
        lbLimgdonot_empty9x=tk.Label(zy_frameW92,
                                     image=zyfW92_imgdonot_empty9x,
                                     borderwidth=4,
                                     width=450, height=75)
        
        lbLimgdonot_empty9x.grid(row=0,column=2,
                                 columnspan=2,
                                 pady=8,
                                 ipadx=3,ipady=1)
        lbLimgdonot_empty9x.image=zyfW92_imgdonot_empty9x

        
        '''製作check Button'''
        '''btNcB無法執行，問題是「#command=zy_wiN1.destroy()」'''
        '''command=zy_wiN1.destroy←不要"()"就可以執行了'''
        
        img_cB_9x=Image.open(get_image_path("ok_remove bg.png")).resize((50,50))  
        zyfW92_cB_9x=ImageTk.PhotoImage(img_cB_9x)

        btNcB_9x=tk.Button(zy_frameW92,
                            image=zyfW92_cB_9x,
                            bg="white",
                            relief="groove",
                            borderwidth=5,
                            width=50, height=50,
                            command=zy_wiN92.destroy)
                    

        btNcB_9x.grid(row=1,
                       columnspan=4,                       
                       pady=15,ipadx=3,ipady=1)
        
        btNcB_9x.image=zyfW92_cB_9x
        return

    if zy_errorS9x:
        '''視窗：第幾列第幾格錯誤!'''
        zy_wiN93=tk.Toplevel(wiN)
        zy_wiN93.title("")
        zy_wiN93.geometry("400x350+450+200")
        zy_wiN93.configure(bg="white")
        zy_wiN93.resizable(width=False, height=False)
        
        zy_frameW93=tk.Frame(zy_wiN93,
                            bg="MediumTurquoise",
                            height=90)
        
        zy_frameW93.pack(fill="x")
        
        
        '''圖片：Cue1_remove bg'''
        zy_imgCue9x = Image.open(get_image_path("Cue1_remove bg.png")).resize((120,40))
        zy_frameW93_imgCue9x = ImageTk.PhotoImage(zy_imgCue9x)
        zy_lbL_imgCue9x = tk.Label(zy_frameW93,
                                image=zy_frameW93_imgCue9x,
                                bg="MintCream",
                                relief="solid",
                                borderwidth=2,
                                width=124,height=44)
                        
        zy_lbL_imgCue9x.place(relx=0.5, rely=0.5,
                          anchor="center")                   
        zy_lbL_imgCue9x.image=zy_frameW93_imgCue9x
        
        
        zy_frameW93_1=tk.Frame(zy_wiN93,
                            bg="MediumTurquoise")                            
        zy_frameW93_1.pack(expand=True,fill="both")
        
        
        # 滾動條，用於文字框 # Scrollbar for the text box
        sBar_zyW93 = tk.Scrollbar(zy_frameW93_1, orient="vertical") # 建立垂直滾動條
        sBar_zyW93.pack(side=tk.RIGHT, fill="y")  # 將滾動條附加在右側 # Attach scrollbar to the right side
                    
        # zy_frameW7_1 裡面的文字框 # Text box inside zy_frameW7_1
        texT_zy_frameW93_1 = tk.Text(zy_frameW93_1,
                                    bg="#F0FFF0",
                                    wrap=tk.WORD, # 自動換行以單字為單位
                                    font=("標楷體", 14), 
                                    yscrollcommand=sBar_zyW93.set)  
                                    # 將文字框與滾動條連結 # Link Text box to scrollbar)
        texT_zy_frameW93_1.pack()

        
        # 將滾動條連結到文字框 # Link scrollbar to Text box
        sBar_zyW93.config(command=texT_zy_frameW93_1.yview)
        
        # 將錯誤訊息組合成單一字串，並以分隔線區隔
        zy_errorS9x_text = "\n  ----------------------------------\n".join(zy_errorS9x)
        texT_zy_frameW93_1.insert(tk.END,f"\n{zy_errorS9x_text}\n")
        texT_zy_frameW93_1.config(state="disabled")
        # 設定文字框為不可編輯狀態 # Disable editing of the Text box    
                     
    else:
        '''視窗：全部正確顯示'''
        global zy_wiN94
        zy_wiN94=tk.Toplevel(wiN)
        zy_wiN94.title("")
        zy_wiN94.geometry("550x270+450+200")
        zy_wiN94.configure(bg="SeaShell")                          
        
        zy_frameW94=tk.Frame(zy_wiN94,bg="SeaShell")                            
        zy_frameW94.pack(expand=True)

        image_files_9x = {
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
        
        random_key_9x=rd.randint(1,len(image_files_9x))
        image_file_9x=image_files_9x[random_key_9x]
        
        img_good9x=Image.open(get_image_path(image_file_9x)).resize((70,70))
        zy_frameW94_img_good9x=ImageTk.PhotoImage(img_good9x)

        lbL_img_good9x=tk.Label(zy_frameW94,
                                image=zy_frameW94_img_good9x,
                                bg="SeaShell",
                                width=70, height=70)
        
        lbL_img_good9x.grid(row=0,
                            column=0,
                            pady=8,
                            ipadx=3,
                            ipady=1)
        lbL_img_good9x.image=zy_frameW94_img_good9x 
        
        image_files2_9x = {
        1: "good1_All correct_remove bg.png",
        2: "good2_All answers are correct_remove bg.png",
        3: "good3_En_Bingo_remove bg.png",
        4: "good4_You are excellent!_remove bg.png",
        5: "good5_Completely correct_remove bg.png",
        6: "good6_You got it right!_remove bg.png"}
        
        random_key1_9x=rd.randint(1,len(image_files2_9x))
        image_file2_9x=image_files2_9x[random_key1_9x]
        
        img_good1_9x=Image.open(get_image_path(image_file2_9x)).resize((180,40))
        zy_frameW94_img_good1_9x=ImageTk.PhotoImage(img_good1_9x)

        lbL_img_good1_9x=tk.Label(zy_frameW94,
                                  image=zy_frameW94_img_good1_9x,
                                  bg="SeaShell",
                                  width=200, height=50)
        
        lbL_img_good1_9x.grid(row=0,
                              column=1,
                              pady=8,
                              ipady=1)
        lbL_img_good1_9x.image=zy_frameW94_img_good1_9x 
        
        image_files3_9x = {
        1: "good71_Awesome!_remove bg.png",
        2: "good71_You are amazing!_remove bg.png",
        3: "good71_So impressive_remove bg.png",
        4: "good71_So smart!_remove bg.png",
        5: "good71_Super amazing!_remove bg.png",
        6: "good71_You are a genius!_remove bg.png"}
        
        random_key2_9x=rd.randint(1,len(image_files3_9x))
        image_file3_9x=image_files3_9x[random_key2_9x]
        
        img_good2_9x=Image.open(get_image_path(image_file3_9x)).resize((180,40))
        zy_frameW94_img_good2_9x=ImageTk.PhotoImage(img_good2_9x)

        lbL_img_good2_9x=tk.Label(zy_frameW94,
                                  image=zy_frameW94_img_good2_9x,
                                  bg="SeaShell",
                                  width=200, height=50)
        
        lbL_img_good2_9x.grid(row=0,
                              column=2,
                              pady=8,
                              ipady=1)
        lbL_img_good2_9x.image=zy_frameW94_img_good2_9x 
        
        '''稱讚的OK鈕'''
                
        img_cB1_9x=Image.open(get_image_path("ok_remove bg.png")).resize((50,50))  
        img_btNcB1_9x=ImageTk.PhotoImage(img_cB1_9x)

        btNcB1_9x=tk.Button(zy_frameW94,
                            image=img_btNcB1_9x,
                            bg="white",
                            relief="groove",
                            borderwidth=5,
                            width=50, height=50,
                            command=partial(
                                _hit_clearnAclose9x,
                                zy_wiN94))

        btNcB1_9x.grid(row=1,
                       columnspan=4,
                       pady=15,
                       ipadx=3,ipady=1)
        
        btNcB1_9x.image=img_btNcB1_9x
        
def _hit_clearnAclose9x(zy_wiN94):   
        global zy_wiN95
        '''
        ("提示",f"確定關閉{sizeS-1}格x{sizeS-1}格乘法練習視窗嗎？")
        '''
        
        zy_wiN95=tk.Toplevel(wiN)
        zy_wiN95.title("")
        zy_wiN95.geometry("500x300+450+200")
        zy_wiN95.configure(bg="white")
        
        zy_frameW95=tk.Frame(zy_wiN95,bg="white")
        zy_frameW95.pack(expand=True)    
        
        '''視窗：關閉乘法練習的視窗嗎？'''
        imgclosE_9x = Image.open(get_image_path("Are you sure close window_remove bg.png")).resize((350,60))
        zy_frameW95_imgclosE_9x = ImageTk.PhotoImage(imgclosE_9x)
        lbL_imgclosE_9x = tk.Label(zy_frameW95,
                                   image=zy_frameW95_imgclosE_9x,
                                   bg="white",
                                   width=400,height=60)
                          
        lbL_imgclosE_9x.grid(row=0,
                             columnspan=4,
                             pady=15,
                             ipadx=3,ipady=1)
        
        lbL_imgclosE_9x.image=zy_frameW95_imgclosE_9x

        '''確定鈕'''
        img_CB2_9x=Image.open(get_image_path("Confirm Button_1_remove bg.png")).resize((70,60))  
        zyfw95_CB2_9x=ImageTk.PhotoImage(img_CB2_9x)

        btNCB2_9x=tk.Button(zy_frameW95,
                            image=zyfw95_CB2_9x,
                            bg="white",
                            relief="groove",
                            borderwidth=3,
                            width=70, height=70,
                            command=lambda:(zy_wiN91.destroy(),
                                            zy_wiN94.destroy(),
                                            zy_wiN95.destroy()))
        
        btNCB2_9x.grid(row=1,
                       column=1,
                       padx=10,pady=15,
                       ipadx=1,ipady=1)
        
        btNCB2_9x.image=zyfw95_CB2_9x
        
        '''取消鈕'''
        img_canceL9x=Image.open(get_image_path("Cancel Button_remove bg.png")).resize((70,60))  
        zyfw95_canceL9x=ImageTk.PhotoImage(img_canceL9x)

        btNcanceL9x=tk.Button(zy_frameW95,
                              image=zyfw95_canceL9x,
                              bg="white",
                              relief="groove",
                              borderwidth=3,
                              width=70, height=70,
                              command=_hit_clAcl9x)
           
        btNcanceL9x.grid(row=1,
                       column=2,
                       padx=10,pady=15,
                       ipadx=1,ipady=1)
        
        btNcanceL9x.image=zyfw95_canceL9x

'''清除答案，在挑戰一次？'''
def _hit_clAcl9x(): #命名：Clear the answers and try the challenge again?
    
    zy_wiN96=tk.Toplevel(wiN)
    zy_wiN96.title("")
    zy_wiN96.geometry("500x300+450+200")
    zy_wiN96.configure(bg="white")
    
    zy_frameW96=tk.Frame(zy_wiN96,bg="white")
    zy_frameW96.pack(expand=True)    
    
    '''圖片：清除答案，在挑戰一次？'''
    imgclAcl_9x = Image.open(get_image_path("Clear answers and challenge again_remove bg.png")).resize((350,60))
    zy_frameW96_imgclAcl_9x = ImageTk.PhotoImage(imgclAcl_9x)
    lbL_imgclAcl_9x = tk.Label(zy_frameW96,
                               image=zy_frameW96_imgclAcl_9x,
                               bg="white",
                               width=400,height=60)
                      
    lbL_imgclAcl_9x.grid(row=0,
                         columnspan=4,
                         pady=15,
                         ipadx=3,ipady=1)
    
    lbL_imgclAcl_9x.image=zy_frameW96_imgclAcl_9x
    
    '''確定鈕'''
    img_CB3_9x=Image.open(get_image_path("Confirm Button_1_remove bg.png")).resize((70,60))  
    zyW96_CB3_9x=ImageTk.PhotoImage(img_CB3_9x)
    
    btNCB3_9x=tk.Button(zy_frameW96,
                        image=zyW96_CB3_9x,
                        bg="white",
                        relief="groove",
                        borderwidth=3,
                        width=70, height=70,
                        command=lambda:(
                            _hitclean9x(),
                            zy_wiN94.destroy(),
                            zy_wiN95.destroy(),                           
                            zy_wiN96.destroy()))

    btNCB3_9x.grid(row=1,
                columnspan=5,
                padx=10,pady=15,
                ipadx=1,ipady=1)
    
    btNCB3_9x.image=zyW96_CB3_9x


def _hitclean9x():
    for zy_entry9x,_ in zy_entrIes9x:
        zy_entry9x.delete(0,"end")


'''按鈕命名'''
'''
#Description of the rules：用於簡要描述規則的內容。            
按鈕命名："Z"hu"y"in Version→zy(小寫)、Description的"D"、rules的"r"，
→_zy_hitDr
'''
def _zy_hitDr():
    
    wiN13=tk.Toplevel(wiN)
    wiN13.title("~ 歡迎進入數字魔法森林 ~")
    wiN13.geometry("550x550+400+150")
    
    img_zyDrAll=Image.open(get_image_path("Description_zy All.png")).resize((500,500)) 
    wiN_img_zyDrAll = ImageTk.PhotoImage(img_zyDrAll)
    lbLimg_zyDrAll = tk.Label(wiN13,image=wiN_img_zyDrAll,bg="#F0FFF0")

    lbLimg_zyDrAll.place(relx=0.5, rely=0.5,
                         anchor="center")
    
    lbLimg_zyDrAll.image=wiN_img_zyDrAll