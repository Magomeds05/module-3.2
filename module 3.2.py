def send_email(message, recipient,*, sender="university.help@gmail.com"):
    must = (".com"".ru"".net")
    for i in recipient, sender:
        if must not in i:
            print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
        if sender == recipient:
            print("Нельзя отправить письмо самому себе!")
            return must
        if sender == "university.help@gmail.com":
            print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
        if sender != "university.help@gmail.com":
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
            return must


send_email("Это сообщение для проверки связи", "vasyok1337@gmail.com", sender="university.help@gmail.com")
send_email("Вы видите это сообщение как лучший студент курса!", "urban.fan@mail.ru", sender="urban.info@gmail.com")
send_email("Пожалуйста, исправьте задание", "urban.student@mail.ru", sender="urban.teacher@mail.uk")
send_email("Напоминаю самому себе о вебинаре", "urban.teacher@mail.ru", sender="urban.teacher@mail.ru")