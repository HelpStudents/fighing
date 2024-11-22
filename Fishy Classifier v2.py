#!/usr/bin/env python3

import imaplib
import email
from email.header import decode_header

# Функция для получения писем
def get_emails(username, password):
    # Подключение к серверу
    mail = imaplib.IMAP4_SSL("imap.gmail.com")  # Используйте адрес IMAP вашего почтового провайдера
    mail.login(username, password)
    mail.select("inbox")

    # Поиск всех писем
    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()

    emails = []
    for email_id in email_ids:
        _, msg = mail.fetch(email_id, "(RFC822)")
        msg = email.message_from_bytes(msg[0][1])
        emails.append(msg)

    mail.logout()
    return emails

# Функция для простого анализа на наличие фишинга
def is_phishing_email(msg):
    phishing_keywords = ["urgent", "verify your account", "account suspended", "click here", "login", "password", "confirm"]

    subject, encoding = decode_header(msg['Subject'])[0]
    if isinstance(subject, bytes):
        subject = subject.decode(encoding if encoding else 'utf-8')

    # Приведение к нижнему регистру
    subject = subject.lower()

    # Проверка на наличие ключевых слов
    for keyword in phishing_keywords:
        if keyword in subject:
            return True

    return False

# Основная часть программы
if __name__ == "__main__":
    username = "your_email@gmail.com"  # Замените на ваш email
    password = "your_password"  # Замените на ваш пароль

    emails = get_emails(username, password)

    phishing_emails = []
    for msg in emails:
        if is_phishing_email(msg):
            phishing_emails.append(msg)
            print(f"Фишинговое письмо найдено: {msg['Subject']}")

    if not phishing_emails:
        print("Фишинговых писем не найдено.")