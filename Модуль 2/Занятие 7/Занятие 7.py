import speech_recognition as sr # Библиотека для воспроизведения голоса sr-это сокращение, то есть speech_recognition=sr
recognizer = sr.Recognizer()  #Микрофон
while True:
    with sr.Microphone(device_index=2) as source:  # device index-микрофоны на устройстве(сам компьютер, от наушников)
        print(sr.Microphone.list_microphone_names())
        print("Скажите что-нибудь...")
        audio = recognizer.listen(source)  # Слушает наш микрофон

        speech = recognizer.recognize_google(audio, language="ru_Ru")   #Наша речь
        print(f"Вы сказали: {speech}")

        if speech.lower() == "Добрый день":
            print("И тебе привет!")
