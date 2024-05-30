from ultralytics import YOLO
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
from functools import partial
import time

# 柚子todo-------------------------------------------------------------------------

# 驗收訓練結果
model = YOLO(
    "C:\C++\yolov8\\runs\detect\\train2\weights\\best.pt"
)  # 套上訓練好的模組中最好的
results = model.predict(source="C:\C++\yolov8\malu1_1.jpg", save=True)  # 預測多少人

persons = 0
# 算有幾個框框(上面標示好人的照片)，才能轉成數字
for result in results:
    persons = result.boxes


# 取得有幾個人的函示
def get_person():
    return str(len(persons))


# 柚子todo-------------------------------------------------------------------------end
currentState = ""


# 秒數調整系統
def get_second():
    # to do--------------------------------------------------------------
    if currentState == "red":
        return "5"
    elif currentState == "green":
        return "10"


second = 0
count = 0


def add():
    global second, currentState, label1, count
    test["state"] = "disable"
    label2 = tk.Label(text="預測人數:" + get_person(), fg="red", font=("Helvetica", 30))
    label2.place(x=100, y=350)
    second = int(get_second())
    update_image_with_countdown(second)
    window.after(6000, add)


def update_image_with_countdown(i):
    print(i)
    global currentState, second, label1, tk_img2, count
    count += 1
    font_path = "C:\C++\yolov8\Seven Segment.ttf"

    if currentState == "red":
        img2 = Image.open("C:\C++\yolov8\photo\\rd light_2.png")

    else:
        img2 = Image.open("C:\C++\yolov8\photo\\rd light_1.png")

    draw = ImageDraw.Draw(img2)
    font = ImageFont.truetype(font_path, 50)
    draw.text((138, 190), str(i), font=font, fill="green")
    tk_img2 = ImageTk.PhotoImage(img2)
    label1.config(image=tk_img2)

    if i > 0:
        window.after(1000, update_image_with_countdown, i - 1)  # 1000ms
        print("X")

    if i == 0:
        currentState = "red" if currentState == "green" else "green"
        second = 7
        # print(currentState)
        img2 = Image.open("C:\C++\yolov8\photo\\rd light_1.png")
        tk_img2 = ImageTk.PhotoImage(img2)
        label1.config(image=tk_img2)
        test["state"] = "normal"  # 恢復按鈕,不讓使用者一直按


def show_page(frame):
    frame.tkraise()


# ----main------
# 創建主窗口
window = tk.Tk()
window.title("AI")
window.geometry("900x500")
window.resizable(False, False)

# 創建兩個頁面
page1 = tk.Frame(window)
page2 = tk.Frame(window)

for frame in (page1, page2):
    frame.place(x=0, y=0, width=900, height=500)

# 頁面1內容
Button_img = Image.open("C:\C++\yolov8\photo\\button.jpg")
button_img = ImageTk.PhotoImage(Button_img)
test = tk.Button(
    page1, image=button_img, command=add, borderwidth=0, highlightthickness=0
)
test.place(x=600, y=350)

img = Image.open("C:\C++\yolov8\\runs\detect\predict3\malu1_1.jpg")  # 開啟圖片
tk_img = ImageTk.PhotoImage(img)  # 轉換為 tk 圖片物件
label = tk.Label(page1, image=tk_img)  # 在 Label 中放入圖片
label.place(x=50, y=40)

img1 = Image.open("C:\C++\yolov8\photo\\rd light_1.png")  # 開啟圖片
tk_img1 = ImageTk.PhotoImage(img1)
label1 = tk.Label(page1, image=tk_img1)  # 在 Label 中放入圖片
label1.place(x=550, y=30)

# 添加頁面切換按鈕
switch_to_page2_btn = tk.Button(
    page1, text="警示系統", command=lambda: show_page(page2)
)
switch_to_page2_btn.place(x=1, y=1)

# 頁面2內容
label_hello = tk.Label(page2, text="有人！減速慢行！", font=("Helvetica", 50))
label_hello.place(x=200, y=200)

# 添加頁面切換按鈕
switch_to_page1_btn = tk.Button(
    page2, text="紅綠燈系統", command=lambda: show_page(page1)
)
switch_to_page1_btn.place(x=1, y=1)

# 顯示初始頁面
show_page(page1)

currentState = "red"
# second = 10
# window.after(1000, update_image_with_countdown, 10 - 1)#1000ms
# 開始主循環
window.mainloop()
