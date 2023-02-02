categories = []
item_cat1={}
item_cat1["id"]= 1
item_cat1["name"]= "Хобби"
item_cat1["desc"]= "Ваши увлечения"
categories.append(item_cat1)

item_cat2={}
item_cat2["id"]= 2
item_cat2["name"]= "Домашние животные"
item_cat2["desc"]= "Увлечения c вашими любимцами"
categories.append(item_cat2)

item_cat3={}
item_cat3["id"]= 3
item_cat3["name"]= "Спортивные игры"
item_cat3["desc"]= "Спорт и все что с ним связано"
categories.append(item_cat3)

item_cat4={}
item_cat4["id"]= 4
item_cat4["name"]= "Философия"
item_cat4["desc"]= "Об этом можно разговаривать вечно"
categories.append(item_cat4)

item_cat5={}
item_cat5["id"]= 5
item_cat5["name"]= "Музыка"
item_cat5["desc"]= "То, что вы любите больше всего"
categories.append(item_cat5)

item_cat6={}
item_cat6["id"]= 6
item_cat6["name"]= "Книги"
item_cat6["desc"]= "Без чтения не живут"
categories.append(item_cat6)

item_cat7={}
item_cat7["id"]= 7
item_cat7["name"]= "Семья"
item_cat7["desc"]= "Главное"
categories.append(item_cat7)

item_cat8={}
item_cat8["id"]= 8
item_cat8["name"]= "Душевные темы"
item_cat8["desc"]= "Обо всем"
categories.append(item_cat8)

item_cat9={}
item_cat9["id"]= 9
item_cat9["name"]= "Игры"
item_cat9["desc"]= "Для совместного досуга в сети"
categories.append(item_cat9)

item_cat10={}
item_cat10["id"]= 10
item_cat10["name"]= "Будущее"
item_cat10["desc"]= "Планы и цели"
categories.append(item_cat10)

import json
jsonstring = json.dumps(categories, ensure_ascii=False)
with open('categories.json', 'w+', encoding='utf-8') as f:
    f.write(jsonstring)
    
sub_categories = []
item_sub_cat1={}
item_sub_cat1["id"]= 1
item_sub_cat1["parent_id"]= 1
item_sub_cat1["name"]= "Коллекционирование марок"
item_sub_cat1["desc"]= "История и оценки марок"
sub_categories.append(item_sub_cat1)

item_sub_cat2={}
item_sub_cat2["id"]= 2
item_sub_cat2["parent_id"]= 1
item_sub_cat2["name"]= "Рисование"
item_sub_cat2["desc"]= "Обсуждение работ собеседника(ов)"
sub_categories.append(item_sub_cat2)

item_sub_cat3={}
item_sub_cat3["id"]= 3
item_sub_cat3["parent_id"]= 1
item_sub_cat3["name"]= "Тенис"
item_sub_cat3["desc"]= "Стаж игры в тенис"
sub_categories.append(item_sub_cat3)

item_sub_cat4={}
item_sub_cat4["id"]= 4
item_sub_cat4["parent_id"]= 2
item_sub_cat4["name"]= "Питомцы"
item_sub_cat4["desc"]= "Есть ли они у собеседника?"
sub_categories.append(item_sub_cat4)

item_sub_cat5={}
item_sub_cat5["id"]= 5
item_sub_cat5["parent_id"]= 2
item_sub_cat5["name"]= "Прогулки"
item_sub_cat5["desc"]= "Игры во время прогулок"
sub_categories.append(item_sub_cat5)

item_sub_cat6={}
item_sub_cat6["id"]= 6
item_sub_cat6["parent_id"]= 2
item_sub_cat6["name"]= "Имя"
item_sub_cat6["desc"]= "Как зовут маленького друга?"
sub_categories.append(item_sub_cat6)

item_sub_cat7={}
item_sub_cat7["id"]= 7
item_sub_cat7["parent_id"]= 3
item_sub_cat7["name"]= "Любимый вид спорта"
item_sub_cat7["desc"]= "А почему?"
sub_categories.append(item_sub_cat7)

item_sub_cat8={}
item_sub_cat8["id"]= 8
item_sub_cat8["parent_id"]= 3
item_sub_cat8["name"]= "Усердие"
item_sub_cat8["desc"]= "Сколько времени спорт занимает в вашей жизни?"
sub_categories.append(item_sub_cat8)

item_sub_cat9={}
item_sub_cat9["id"]= 9
item_sub_cat9["parent_id"]= 3
item_sub_cat9["name"]= "Мировые достижения"
item_sub_cat9["desc"]= "Последние спортивные новости"
sub_categories.append(item_sub_cat9)

item_sub_cat10={}
item_sub_cat10["id"]= 10
item_sub_cat10["parent_id"]= 4
item_sub_cat10["name"]= "Выбор каждый делает сам"
item_sub_cat10["desc"]= "Существует ли судьба?"
sub_categories.append(item_sub_cat10)

item_sub_cat11={}
item_sub_cat11["id"]= 11
item_sub_cat11["parent_id"]= 4
item_sub_cat11["name"]= "Почему мы стремимся к совершенству?"
item_sub_cat11["desc"]= "Оно ведь недостижимо"
sub_categories.append(item_sub_cat11)

item_sub_cat12={}
item_sub_cat12["id"]= 12
item_sub_cat12["parent_id"]= 4
item_sub_cat12["name"]= "Что такое свобода?"
item_sub_cat12["desc"]= "Возможна ли настоящая свобода?"
sub_categories.append(item_sub_cat12)

item_sub_cat13={}
item_sub_cat13["id"]= 13
item_sub_cat13["parent_id"]= 5
item_sub_cat13["name"]= "Любимый исполнитель собеседника"
item_sub_cat13["desc"]= "Почему он?"
sub_categories.append(item_sub_cat13)

item_sub_cat14={}
item_sub_cat14["id"]= 14
item_sub_cat14["parent_id"]= 5
item_sub_cat14["name"]= "Любимый трек собеседника"
item_sub_cat14["desc"]= "Какие ассоциации он вызывает?"
sub_categories.append(item_sub_cat14)

item_sub_cat15={}
item_sub_cat15["id"]= 15
item_sub_cat15["parent_id"]= 5
item_sub_cat15["name"]= "Какую роль играет музыка в жизни собеседника"
item_sub_cat15["desc"]= "Важна ли она для него?"
sub_categories.append(item_sub_cat15)

item_sub_cat16={}
item_sub_cat16["id"]= 16
item_sub_cat16["parent_id"]= 6
item_sub_cat16["name"]= "Какой жанр предпочитает собеседник"
item_sub_cat16["desc"]= "Почему?"
sub_categories.append(item_sub_cat16)

item_sub_cat17={}
item_sub_cat17["id"]= 17
item_sub_cat17["parent_id"]= 6
item_sub_cat17["name"]= "Нужно ли читать классику?"
item_sub_cat17["desc"]= "Чем она актуальна?"
sub_categories.append(item_sub_cat17)

item_sub_cat18={}
item_sub_cat18["id"]= 18
item_sub_cat18["parent_id"]= 6
item_sub_cat18["name"]= "Любимая книга"
item_sub_cat18["desc"]= "О чем она?"
sub_categories.append(item_sub_cat18)

item_sub_cat19={}
item_sub_cat19["id"]= 19
item_sub_cat19["parent_id"]= 7
item_sub_cat19["name"]= "Братья и сестры"
item_sub_cat19["desc"]= "Есть ли они у собеседника?"
sub_categories.append(item_sub_cat19)

item_sub_cat20={}
item_sub_cat20["id"]= 20
item_sub_cat20["parent_id"]= 7
item_sub_cat20["name"]= "Взаимоотношения"
item_sub_cat20["desc"]= "Есть ли поддержка в семье собеседника?"
sub_categories.append(item_sub_cat20)

item_sub_cat21={}
item_sub_cat21["id"]= 21
item_sub_cat21["parent_id"]= 7
item_sub_cat21["name"]= "Семейные традиции"
item_sub_cat21["desc"]= "Как они появились?"
sub_categories.append(item_sub_cat21)

item_sub_cat22={}
item_sub_cat22["id"]= 22
item_sub_cat22["parent_id"]= 8
item_sub_cat22["name"]= "Друзья"
item_sub_cat22["desc"]= "Какое окружение имеет собеседник?"
sub_categories.append(item_sub_cat22)

item_sub_cat23={}
item_sub_cat23["id"]= 23
item_sub_cat23["parent_id"]= 8
item_sub_cat23["name"]= "Праздники"
item_sub_cat23["desc"]= "Какой любимый праздник у собеседника?"
sub_categories.append(item_sub_cat23)

item_sub_cat24={}
item_sub_cat24["id"]= 24
item_sub_cat24["parent_id"]= 8
item_sub_cat24["name"]= "Питание"
item_sub_cat24["desc"]= "Какую пищу предпочитает собеседник? Любит ли он готовить?"
sub_categories.append(item_sub_cat24)

item_sub_cat25={}
item_sub_cat25["id"]= 25
item_sub_cat25["parent_id"]= 9
item_sub_cat25["name"]= "Игра в слова/города"
item_sub_cat25["desc"]= "Предложите собеседнику поиграть"
sub_categories.append(item_sub_cat25)

item_sub_cat26={}
item_sub_cat26["id"]= 26
item_sub_cat26["parent_id"]= 9
item_sub_cat26["name"]= "Шахматы онлайн"
item_sub_cat26["desc"]= "Предложите собеседнику поиграть"
sub_categories.append(item_sub_cat26)

item_sub_cat27={}
item_sub_cat27["id"]= 27
item_sub_cat27["parent_id"]= 9
item_sub_cat27["name"]= "Морскрй бой онлайн"
item_sub_cat27["desc"]= "Предложите собеседнику поиграть"
sub_categories.append(item_sub_cat27)

item_sub_cat28={}
item_sub_cat28["id"]= 28
item_sub_cat28["parent_id"]= 10
item_sub_cat28["name"]= "Мечты"
item_sub_cat28["desc"]= "Что самое непостижимое для собеседника?"
sub_categories.append(item_sub_cat28)

item_sub_cat29={}
item_sub_cat29["id"]= 29
item_sub_cat29["parent_id"]= 10
item_sub_cat29["name"]= "Желания"
item_sub_cat29["desc"]= "Что хочет освоить собеседник?"
sub_categories.append(item_sub_cat29)

item_sub_cat30={}
item_sub_cat30["id"]= 30
item_sub_cat30["parent_id"]= 10
item_sub_cat30["name"]= "Поездки"
item_sub_cat30["desc"]= "Собирается ли ваш собеседник куда-нибудь в ближайшее время?"
sub_categories.append(item_sub_cat30)

import json
jsonstring = json.dumps(sub_categories, ensure_ascii=False)
with open('sub_categories.json', 'w+', encoding='utf-8') as f:
    f.write(jsonstring)
