def send_email(a, b, *, sender="university.help@gmail.com"):
    counter = 0
    if '@' not in b and sender:
        print("Невозможно отправить письмо с адреса ", sender, "на адрес ", b)
    elif not b.endswith(('.ru', '.com', '.net')):
        print("Невозможно отправить письмо с адреса ", sender, "на адрес ", b)
    elif not sender.endswith(('.ru', '.com', '.net')):
        print("Невозможно отправить письмо с адреса ", sender, "на адрес ", b)
    elif sender == b:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса ", sender, "на адрес ", b)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender, ' на адрес ', b)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
