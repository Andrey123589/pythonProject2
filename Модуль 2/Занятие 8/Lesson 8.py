import requests
from bs4 import  BeautifulSoup
from datetime import datetime

today =datetime.today().strftime("%d.%m.%Y")  #strftime-форматирование даты d=day m-month Y-Year

response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp?", params={"date_req": today})  #params-параметры
def get_course(currency_id: object) -> object:  #функция для принятия ID валюты
    soup = BeautifulSoup(response.content, features="xml")  #response-ответ   features-инструмент для парсинга
    valute = soup.find("Valute", ID= currency_id)    #Valute-валюта  ID-номер валюты
    valute_value = valute.Value.text   #Находим значение Валюты Азербайджанский манат "43,9463"
    valute_name = valute.Name.text  #Вывод данных Валюты  Name.text выводит название "Азербайджанский манат
    valute_info ={'name':valute_name, 'value': valute_value}   # Словарь для вывода валют

    return valute_info   # Возвращает информацию о валюте, а именно имя валюты и её значение

print(get_course("R01010")['value'])    #Value возвращает значение валюты, если написать вместо value name, то выведет имя валюты
