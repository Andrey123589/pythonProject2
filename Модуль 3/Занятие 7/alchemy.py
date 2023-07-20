from tkinter import *
import random

window = Tk()
window.geometry("600x600")
window.title("Алхимия")

class Steam:
    image = PhotoImage(file=r'C:\Users\Andre\PycharmProjects\pythonProject2\Модуль 3\Занятие 7\aroma.png').subsample(4,4)


class Water:
    image =PhotoImage(file=r'C:\Users\Andre\PycharmProjects\pythonProject2\Модуль 3\Занятие 7\water.png').subsample(4,4)

    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam




class Fire:
    image =PhotoImage(file=r'C:\Users\Andre\PycharmProjects\pythonProject2\Модуль 3\Занятие 7\fire.png').subsample(4,4)

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam


class Wind:
    image =PhotoImage(file=r'C:\Users\Andre\PycharmProjects\pythonProject2\Модуль 3\Занятие 7\wind.png').subsample(4,4)





class Ground:
    image =PhotoImage(file=r'C:\Users\Andre\PycharmProjects\pythonProject2\Модуль 3\Занятие 7\ground.png').subsample(4,4)







canvas =Canvas(width=600, height=600)
canvas.pack()

elements = [Wind(), Fire(), Water(), Ground()]

for elem in elements:
    canvas.create_image(random.randint(50,550), random.randint(50,550), image=elem.image)

def move(event):
    images_ids= canvas.find_overlapping(event.x, event.y, event.x+10, event.y +10)
    if len(images_ids) == 2:
        elem_id_1, elem_id_2 images_ids[0], images_ids[1]
        elem_1 = elements[elem_id_1-1]
        elem_2 = elements[elem_id+2-1]
        new_elem = elem_1+elem_2
        
        print(images_ids)
    canvas.coords(images_ids,event.x, event.y)





window.bind("B1-Motion", move)


window.mainloop()
