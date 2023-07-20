import vk_api
import random
import requests
from bs4 import BeautifulSoup


def get_dollar_course():
    return soup.find("Valute", ID="R01235").Value.text   #Ищем значение Доллара value text возвращает только текст


response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")  #requsts.get парсинг сайта
if response.status_code == 200:
    soup = BeautifulSoup(response.content, features="xml")


token ="vk1.a.O7EM4uJoOQ2wRpP0PwyDdz37-BTzKzcFeQvenUvrp8rTta4H5Lqg6ppXtcPO3Hg1oW8ckoInvNUYYIa20mZkefdQFYkJDAm8M3iVwNoA82IZzP0Ogkf_gBkxK4zXMrMHeCKPn7UX13n_bF_ccuONJIPpAFeGYN_HbcngnUfMM710NIK0_a5em5EGaw8aUjBXXGRg4p3avPaNjgYqR0Ni5w"

vk = vk_api.VkApi(token=token)  #Привязка токена

while True:
    messages = vk.method("messages.getConversations", {"count": 20, "filter": "unanswered"})
    if messages ['count'] >0:
         message_text =messages['items'][0]['last_message']['text']  #Возвращает текст, присланный от пользователя
         if message_text == "курс":
             ans = f"Курс доллара на сегодня составялет {get_dollar_course()} руб"
         else:
             ans ="Неизвестная команда"
         user_id = messages['items'][0]['last_message']['from_id']  #узнаём ID человека
         random_id = random.randint(-10 **7, 10**7) #Обязательный параметр randint генерирует число


         vk.method("messages.send", {
             "user_id": user_id,
              "random_id": random_id,
              "message": message_text,
    })