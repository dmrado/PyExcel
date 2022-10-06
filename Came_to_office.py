import re

print("Здравствуйте, как я могу к Вам обращаться?")
user = input()
print(f"Рад Вас видеть уважаемый(ая) {user}, вы пришли в офис, что будете делать?")

while True:
    answer = input().lower()
    if re.fullmatch(".*(ча.*|кофе|вод.*|сок.*).*", answer):
        print("Горячие и холодные напитки это хорошо, а работать собираемся?")
    elif re.fullmatch(".*(болта.*|говор.*|обща.*).*", answer):
        print("общение конечно необходимо, а работать собираемся?")
    elif re.fullmatch(".*(кур.*|магаз.*|газет.*|журнал.*|ларек.*|ем.*|куша.*).*", answer):
        print(f"{user}, Вы работать-то собираетесь?")
    elif re.fullmatch(".*комп.*", answer):
        print(f"Прекрасный выбор! {user}, cразу видно хорошего сотрудника! Что делаете? Есть ли проблема?")
        while True:
            answer = input().lower()
            if re.fullmatch("(прист.*|начин.*|старт.*)", answer):
                print(f"{user}, Хорошего рабочего дня!")
                break
            elif re.fullmatch(".*(проблем.*)+(\s+?\w*)?|(не.*)(\s+?\w*)?(раб.*|вкл.*).*", answer):
                print(f"{user}, что не работает выбери: компьютер, телефон или свет?")
                while True:
                    answer = input().lower()
                    match = re.search("(комп.*|телефон.*|свет.*)+", answer)
                    if not match:
                        print(f"О прекрасный работник, {user}, я не знаю чем Вам помочь, простите!")
                        break
                    else:
                        if re.fullmatch(".*комп.*", match[0]):
                            print(f"{user}, обратитесь в техподдержку")
                        elif re.fullmatch(".*телефон.*", match[0]):
                            print(f"{user}, позвоните в сотовую компанию")
                        elif re.fullmatch(".*свет.*", match[0]):
                            print(f"{user}, вызовите специалиста АХЧ")




