import requests
from bs4 import BeautifulSoup
def get_dollar_course():
    return soup.find("Valute", ID="RO1235"). Value.text    #Ищем значение Доллара value text возвращает только текст
response =requests.get("http://www.cbr.ru/scripts/XML_daily.asp")  #get парсинг сайта
if response.status_code ==200:

    soup = BeautifulSoup(response.content, features= 'xml' )
