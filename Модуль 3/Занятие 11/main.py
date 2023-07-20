import sqlite3

# try:
#     connection = sqlite3.connect('sqlite.db')
# except sqlite3.DatabaseError:
#     print('Возникла ошибка при подключиении к БД')
# finally:
#     connection.close()

class User:  #Создаем класс пользователя с аттрибутами имя, фамилия, возраст, пол
    def __init__(self, name: str, surname: str, age: int, gender: str): # (name:str) обозначаем какой тип данных будет в этом аттрибуте)
        self.name = name
        self. surname = surname
        self. age = age
        self.gender = gender

def add_new_user(cur: sqlite3.Cursor, user: User): # Добавляем в таблицу значения к полям name, surname, age, gender
    # Чтобы добавить что-либо в таблицу используем INSERT INTO
        command = """
        INSERT INTO users (name, surname, age, gender) VALUES(?, ?, ?, ?)
        
        
        """
        cur.execute(command,(user.name, user.surname, user.age, user.gender)) # Вместо "?" добавляем "name", "surname", по порядку

def get_all_users(cur: sqlite3.Cursor):
    command = """
    SELECT * FROM users
    
    """

    result = cur.execute(command)
    return result.fetchall() # Команда, позволяющая вытащивать все данные из SQL


def get_user (cur: sqlite3.Cursor,user_id: int):
    command = """
    SELECT * FROM users WHERE id = ?;
    """
    result =cur.execute(command, (user_id,))
    return result.fetchone()
def create_user_table(cur: sqlite3.Cursor):  # Создаём таблицу  id, name, surname, age, gender
    #Чтобы создать таблицу используем (CREATE TABLE IF NOT EXISTS) users название таблицы
    command = """
    
    CREATE TABLE  IF NOT EXISTS users (       
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    age INTEGER,
    gender TEXT);
    """
    cur.execute(command)

def update_user_name(cur:sqlite3.Cursor, name: str, user_id: int):
    command = """
    UPDATE users SET name = ? WHERE id = ?
    """
    cur.execute(command,(name, user_id)) # параметр name поставляется вместо "?", где id это в какой строке находится имя


def clear_user_table(cur: sqlite3.Cursor):
    command = """
    DELETE FROM users;
    """
    cur.execute(command)

if __name__ ==  '__main__':
    with sqlite3.connect('sqlite.db') as connection:  #Открываем файл(ленивые вычисления)
        cursor = connection.cursor()  # Позволяет создавать команды  в SQL
        create_user_table(cursor) #Таблица (функция
        clear_user_table(cursor)

        user = User(name = 'Максим', surname = 'Максимов', age=16, gender='М')
        add_new_user(cursor, user=user)
        users = get_all_users(cursor)
        print(users)
        update_user_name(cursor, 'Евгений', 1)  # Мы через функцию update_user_name меняем имя на "Евгений", первого ID
        user = get_user(cursor, 1)
        print(user)


    
