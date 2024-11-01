# Рассылка писем

def send_email(message, recipient, *, sender="university.help@gmail.com"):

    if '@' not in recipient or '@' not in sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    recipient_parts = recipient.split('@')
    sender_parts = sender.split('@')
    val_domains = ('.com', '.ru', '.net')

    if not (recipient_parts[-1].endswith(val_domains) and sender_parts[-1].endswith(val_domains)):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')