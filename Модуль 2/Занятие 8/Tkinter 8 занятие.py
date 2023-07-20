from Lesson 8 import get_course,today
from tkinter import *

 #Виджет Label представляет текстовую метку. Этот элемент позволяет выводить статический текст без возможности редактирования.
window = Tk()   # 
window.geometry("500,500")  # Размер окна
window.title("Банк")   # Название Окна

image = PhotoImage(file=r"C:\Users\Andre\PycharmProjects\pythonProject2\Занятие 8\logo.png")
#image: ссылка на изображение, которое отображается на метке

label_img = Label(window, image=image)  #
label_img.place(x=0,y=0)   #Координаты фотографии

label_title = Label(window,text= "Банк 2035", font= "Arial 32")   #Добавляет текст в окно
label_title.place(x=200, y=50)   #Координаты текста

label_currency = Label(window,text=f"Курсы на {today}:", font= "Arial 22")  #font-шрифт текста
label_currency.place(x=20, y=180)  #Координаты текста

dollar_info = f"{get_course("R01235").get("name")} {get_course("R01235").get("value")}"  #Выводим информацию о долларе

dollar_label = Label(window,text=dollar_info, font ="Arial 18")   #Выводим текст о долларе в окно Label
dollar_label.place(x=40, y=220)  #Координаты текста

euro_info  = f"{get_course("R01235").get("name")} {get_course("R01235").get("value")}"  #Выводим информацию о долларе

euro_label = Label(window,text=euro_info, font ="Arial 18")
euro_label.place(x=40, y=260)  #Координаты текста

cny_info  = f"{get_course("R01375").get("name")} {get_course("R01375").get("value")}"  #Выводим информацию о долларе

cny_label = Label(window,text=cny_info, font ="Arial 18")
cny_label.place(x=40, y=300)  #Координаты текста


entry = Entry(font="Arial 22")  #Ввод, где вводит свой текст пользователь
entry.place(x=40,y=400)

y = 40

def search():
    global y #
    #Функция, чтобы повторять вводы
    text = entry.get()   #Сюда пользователь вводит команды
    currrency_info =get_course(currency_id)
    currency_name =currrency_info.get("name")
    currency_value =currrency_info.get("value")

    currency_str =f"{currency_name} {currency_value}"
    currency_label =Label(window,text=currency_str, font = "Arial 18")  #Arial-название шрифта 18-размер шрифта
    currency_label.place(x=40, y=260+y)



    y += 40  #Заставляет следующую валюту отпускаться на 40 пунктов от предыдущей

button = Button(text ="Найти", command=search())  #Кнопка на окне
button.place(x=400, y=400)



window.mainloop()   #Чтобы окно не закрывалось