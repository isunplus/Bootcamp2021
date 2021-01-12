#GUITranslator.py

#จาก library tkinter, * คือให้ดึงความสามารถหลักมาทั้งหมด
from tkinter import *

## ttk is theme of tk
from tkinter import ttk

###--------- Google Translate---------
from googletrans import Translator
translator = Translator() #สร้างฟังชั่นแปลภาษา
    
GUI = Tk() #สร้างหน้าต่างหลัก
GUI.geometry('500x300') #กำหนดขนาดหน้าจอ ก*ส
GUI.title('โปรแกรมแปลภาษา by imSuN')

#------Config-----
FONT = ('Angsana New',15)

#------Label------
L = ttk.Label(GUI,text='กรุณากรอกคำศัพท์ที่ต้องการแปล',font=FONT)
L.pack()

#------Entry (ช่องกรอกข้อความ)------
v_vocab = StringVar() #กล่องเก็บข้อความ

E1 = ttk.Entry(GUI,textvariable = v_vocab,font=FONT,width=40)
E1.pack(pady=20)

#------Button-----
def Translate():
    vocab = v_vocab.get() #.get คือให้แสดงผลออกมา
    meaning = translator.translate(vocab,dest='th')
    print(vocab + ':' + meaning.text)
    print(meaning.pronunciation)
    v_result.set(vocab + ' : ' + meaning.text)

B1 = ttk.Button(GUI, text='Translate',command=Translate) #สร้างปุ่มขึ้นมา
B1.pack(ipadx=20,ipady=10) #show ปุ่มขึ้นมาวางจากบนลงล่าง

#------Label------
L = ttk.Label(GUI,text='คำแปล',font=FONT)
L.pack()

#-----Result------
v_result  = StringVar() #กล่องสำหรับเก็บคำแปล
FONT2 = ('Angsana New',20)
R1 = ttk.Label(GUI,textvariable=v_result,font=FONT2, foreground='green')
R1.pack()

GUI.mainloop() #ทำให้โปรแกรมรันได้ตลอดเวลา จนกว่าจะปิด (บรรทัดสุดท้ายเท่านั่น)




