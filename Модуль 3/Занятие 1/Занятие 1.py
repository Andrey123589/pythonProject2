name = "давид"
salary = 200
age = 15

print("у " + name +"Зарплата составляет"+ str(salary) + "рублей.")
print(f"У {name}  зарплата составляет {salary} рублей")  #Форматирование текста {переменная }



employee = {
    'name': 'Вадим',
    'salary': 199,
    'age': 16,
}

print(f"Y {employee['name']} зарплата составляет {employee ['salary']} руб")

employees_list = [
    {
        'name': 'Вадим',
        'salary':199

    },

    {
        'name': 'Сева',
        'salary': 200
    },
    {
        "name": "Nikiton",
        'salary': 0
    }
]

for employee in employees_list:
    print(f"У {employee['name']} зарплата составляет {employee ['salary']}.")


class Employee:
    def __init__(self, name,salary,on_vacation):  # __init__  конструктор класса инициализация   self-ссылочка экземпляра к названию переменной
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation


employee = Employee(name = 'Я не знаю кто я',salary = 120, on_vacation=False)

print(f"У {employee.name} зарплата составляет {employee.salary} центов, он в отпуске?  {employee.on_vacation}")   # employee.name используем точку, чтобы обрашаться к параметрам name  и salary