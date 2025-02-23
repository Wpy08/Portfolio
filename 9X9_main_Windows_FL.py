import os
import sys
import tkinter as tk
from PIL import Image, ImageTk
import mm_9X9_third_CH_FL as mm_sort_CH
import mm_random_shuffle_CH_second_FL as mm_rdsf_CH
import mm_9X9_third_zy_FL as mm_sort_zy
import mm_random_shuffle_zy_FL as mm_rdsf_zy

# 函式來處理圖片路徑
def get_image_path(image_name):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, "images", image_name)

# 使用tkinter建立一個叫做[wiN]的視窗
wiN = tk.Tk()

# 設定視窗[標題]
wiN.title("~ 數字魔法森林 ~")

# 設背景顏色
wiN.configure(bg="Azure") 

# (2)
# 設定視窗顯示位置的方法:100是X軸，200是Y軸
wiN.geometry("450x380+600+300")  # 600X300→視窗大小 #700+400→700(X軸)、400(Y軸) 

mm_sort_CH.set_main_window(wiN)
mm_rdsf_CH.set_main_window(wiN)
mm_sort_zy.set_main_window(wiN)
mm_rdsf_zy.set_main_window(wiN)  # 初始化模組內的全域變數wiN


'''圖片：山和河流'''
# 使用 get_image_path 取得圖片路徑  #此處有更動
maiN_img = Image.open(get_image_path("forest_10_Remove bg.png")).resize((400, 400))  # 開啟圖片
wiN_maiN_img = ImageTk.PhotoImage(maiN_img)
lbL_maiN_img = tk.Label(wiN,image=wiN_maiN_img,
                        bg="Azure")
                  
lbL_maiN_img.place(relx=0.5,rely=0.5,
                   anchor="center")

lbL_maiN_img.image = wiN_maiN_img

# btN1(主視窗，第1個按鈕)
# 加載圖片（使用PIL）
# 調整圖片大小
'''圖片：國字版'''
# 使用 get_image_path 取得圖片路徑
img_btN1 = Image.open(get_image_path("CH version_remove bg.png")).resize((120, 30))
mainwiN_btN1 = ImageTk.PhotoImage(img_btN1)

wiN_btN1 = tk.Button(wiN,
                     image=mainwiN_btN1,
                     bg="DeepSkyBlue",
                     width=150, height=50,
                     command=mm_sort_CH._hitwiN_CH)

wiN_btN1.place(relx=0.5, rely=0.5,
               anchor="n",
               x=10, y=-25)

wiN_btN1.image = mainwiN_btN1

'''圖片：注音版'''
# 使用 get_image_path 取得圖片路徑
img_btN2 = Image.open(get_image_path("ZY version_remove bg.png")).resize((120, 30))
mainwiN_btN2 = ImageTk.PhotoImage(img_btN2)

# 建立按鈕，將圖片作為背景
wiN_btN2 = tk.Button(wiN,
                     image=mainwiN_btN2,
                     bg="DodgerBlue",
                     width=150, height=50,
                     command=mm_sort_zy._hitwiN_zy)

wiN_btN2.place(relx=0.5, rely=0.5,
               anchor="n",
               x=10, y=45)


wiN_btN2.image = mainwiN_btN2

# 5.顯示視窗
wiN.mainloop()
