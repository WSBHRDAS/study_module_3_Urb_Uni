def point_addr_proverka (sender_or_recipient, *point_adresses):

    point_addresses = [".com", ".ru", ".net"] #проверка адреса на корректность
    rezult_1 = False
    for point_address in point_addresses:
        if point_address in sender_or_recipient and "@" in sender_or_recipient:
            rezult_1 = True
            return rezult_1
            break
    return rezult_1

def send_email(message,recipient, sender = "university.help@gmail.net") :
    if point_addr_proverka(sender) == False or point_addr_proverka(recipient) == False:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    else:
        if recipient == sender :
            print ("Нельзя отправить письмо самому себе!")
        else:
            if sender == "university.help@gmail.net" :
                print ("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
            else :
                print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!","Письмо отправлено с адреса", sender, "на адрес", recipient)

send_email("PREVED MEDVED!!!", "orlovsky@gmail.ru","AdminVasya@mail.ru")
send_email("PREVED MEDVED!!!", "orlovsky@gmail.ru", "orlovsky@gmail.ru")
send_email("PREVED MEDVED!!!", "prived@gmail.tw", "orlovsky@gmail.ru")
send_email("PREVED MEDVED!!!", "orlovskygmail.ru", "orlovsky@gmail.ru")
send_email("PREVED MEDVED!!!", "orlovsky@gmail.ru")
