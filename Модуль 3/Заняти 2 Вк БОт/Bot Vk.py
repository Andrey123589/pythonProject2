import vk_api
import random
import requests







token = "vk1.a.O7EM4uJoOQ2wRpP0PwyDdz37-BTzKzcFeQvenUvrp8rTta4H5Lqg6ppXtcPO3Hg1oW8ckoInvNUYYIa20mZkefdQFYkJDAm8M3iVwNoA82IZzP0Ogkf_gBkxK4zXMrMHeCKPn7UX13n_bF_ccuONJIPpAFeGYN_HbcngnUfMM710NIK0_a5em5EGaw8aUjBXXGRg4p3avPaNjgYqR0Ni5w"

vk = vk_api.VkApi(token=token)

while True:
    messages = vk.method("messages.getConversations", {"count": 20, "filter": "unanswered"})
    if messages['count'] > 0:
        message_text = messages['items'][0]['last_message']['text']
        if message_text == "планеты":
            ans = f"Планета с максимальным значением диаметра {(planets_list)} ."
        else:
            ans = "Неизвестная команда"
        user_id = messages['items'][0]['last_message']['from_id']
        random_id = random.randint(-10 ** 7, 10 ** 7)

        vk.method("messages.send", {
            "user_id": user_id,
            "random_id": random_id,
            "message": ans,
        })
