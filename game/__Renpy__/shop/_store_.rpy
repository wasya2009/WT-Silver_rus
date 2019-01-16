label __init_variables:
    if not hasattr(renpy.store,'gift_item_inv'): #important! Gift_Item.ID == Index in this array
        $ gift_item_inv = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if not hasattr(renpy.store,'shop_found'): #important!
        $ shop_found = False
    if not hasattr(renpy.store,'bought_glasses'): #important!
        $ bought_glasses = False
    if not hasattr(renpy.store,'sscroll_'): #important!
        $ sscroll_ = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    if not hasattr(renpy.store,'fiction_books_intro'): #important!
        $ fiction_books_intro = False


    $ sacred_scrolls = [
        silver_scroll(id=0 , name="None",               cost=0,     comments=[]),
        silver_scroll(id=1 , name="Комната",           cost=10,    comments=["Это первый проект кабинета Дамблдора.", "Не очень захватывающая вещь, чтобы смотреть, конечно. Но имеет большую историческую ценность."]),
        silver_scroll(id=2 , name="Календарь",       cost=30,    comments=["Календарь...","На ранних этапах разработки я поигрался с идеей внедрить в игровой процесс актуальный внутриигровой календарь...","Вскоре я понял, насколько сложнее было бы создать такую игру...","И поскольку я лично считаю, что любые временные ограничения в любой игре всегда работают против фактора удовольствия, я решил отказаться от этой идеи...","Позже я использовал этот рисунок в качестве пергамента для написания писем..."]),
        silver_scroll(id=3 , name="Девушка",           cost=40,    comments=["Пара очень ранних рисунков Гермионы..."]),
        silver_scroll(id=4 , name="Глубокий минет",       cost=70,    comments=["Сцена глубоко минета...","Моя первая попытка.","Была признана плохой и оказалась здесь."]),
        silver_scroll(id=5 , name="Плакат №1",          cost=80,    comments=["Плакат игры...","Гермиона - работа Дахра. Остальное мое..."]),
        silver_scroll(id=6 , name="Плакат №2",          cost=80,    comments=["Другой плакат игры.","Никогда не был выпущен."]),
        silver_scroll(id=7 , name="Чиби-танец",      cost=90,    comments=["Некоторые чиби крупным планом.","Тот, что слева, не попал в финальную игру..."]),
        silver_scroll(id=8 , name="Игровые предметы",         cost=50,    comments=["Куча предметов, которые я не использовал...","Я виню Дахра и его потрясающие работы."]),
        silver_scroll(id=9 , name="С трусиками, без трусиков", cost=90,    comments=["Рисунок Гермионы с плакат. (от Дахра)","Мне нравится правый, когда трусики все еще на ней."]),
        silver_scroll(id=10, name="Много прищепок",      cost=50,    comments=["Еще одна вещь, которая так и не попала в финальную игру...","Идея заключалась в том, что чем больше вы развращаете Гермиону, тем больше прищепок она позволяла бы вам надеть на нее...","И цепь на сосках она должна была носить в классе под униформой."]),
        silver_scroll(id=11, name="Бордель домашних эльфов",  cost=110,   comments=["Бордель домашних эльфов... Просто еще одна вещь, которая никогда не случится."]),
        silver_scroll(id=12, name="Я и Лола",        cost=110,   comments=["Рисунок, изображающий вас как маг Дурмстранга и Лолы, как студентки...","Сам рисунок, конечно, принадлежит Дахру."]),
        silver_scroll(id=13, name="Тяжелая тренировка",      cost=100,   comments=["Еще один побочный квест, которого никогда не будет...","Он был о--","Нет, лучше не надо. Кто знает, возможно, мы в конце концов добавим эти квесты."]),
        silver_scroll(id=14, name="Волшебные шахматы",     cost=80,    comments=["Другой побочный квест...","Он был связан с волшебным клубом по шахматам."]),
        silver_scroll(id=15, name="Книга репетиторства",     cost=40,    comments=["Есть больше способов носить красивой девушки с собой свои книги, чем один.","Я подумал, что было бы здорово изменить то, как Гермиона несет книги, когда она прогрессирует с обучением.","Поскольку вся ветка репетиторства была отменена, я показываю ее здесь..."]),
        silver_scroll(id=16, name="Особый подарок №1",     cost=30,    comments=["Несколько предметов, которые не попали в финальную игру...","Слева - настоящий живой домашний эльф, который дается в подарок.","Справа - портрет первого, но мудрого волшебника. Должен помогать с учебой..."]),
        silver_scroll(id=17, name="Особый подарок №2",     cost=30,    comments=["Еще несколько предметов...","Газета, флакон духов и Волшебная шляпа, говорящая то, что вы хотите услышать..."]),
        silver_scroll(id=18, name="Художественная книга",      cost=90,    comments=["Художественные книги...","Верхний ряд - мои эскизы, нижний ряд - завершенные рисунки Дахра."]),
        silver_scroll(id=19, name="Шлюха певица",       cost=50,    comments=["Рисунок известной певицы.","Не имеет никакого отношения к этой игре и здесь без причины."]),
        silver_scroll(id=20, name="Кастинг",            cost=70,    comments=["Мне потребовалось некоторое время, чтобы придумать правильный взгляд на Гермиону...","Версия \"A\" была моей первой попыткой. И мне это нравилось до того момента, пока я не начал ее ненавидеть...","Версия \"B\" была второй попыткой. И она хороша. Но ее уверенные и полуагрессивные черты лица не очень подходили персонажу...","Версия \"C\" была выбрана. Гермиона, на которой, я уверен, мы все росли до настоящего момента."]),
        silver_scroll(id=21, name="Мантия ведьмы №1",      cost=90,    comments=["Побочный квест которого никогда не будет.","Вам позволено чувствовать себя плохо после того, как торопили меня.","Если вы не торопили меня, вы можете злиться на людей, которые это делали."]),
        silver_scroll(id=22, name="Мантия ведьмы №2",      cost=90,    comments=["Гермиона представляет свое тело Джинни...","Это была бы довольно запоминающаяся сцена..."]),
        silver_scroll(id=23, name="Мантия ведьмы №3",      cost=150,   comments=["Не ожидали такого, не правда ли?","Если вам интересно, это все еще Гермиона."]),
        silver_scroll(id=24, name="Мантия ведьмы №4",      cost=150,   comments=[".................................","Побочный квест, конечно-же..."]),
        silver_scroll(id=25, name="Прогулка",           cost=100,   comments=["Другой побочный квест...","У нас была довольно продолжительная дискуссия с Дахром об этом...","Я был против, но потом Дахр прислал мне это изображение, и я заткнулся."]),
        silver_scroll(id=26, name="Дурмстранг",         cost=80,    comments=["На первых этапах развития у меня возникла идея представить результаты ваших неудачных или успешно завершенных побочных квестов с помощью упрощенных пластинок или фотографий...","Сначала многие из побочных квестов включали решения о том, как потратить бюджет Хогвартса...","Потратьте деньги на финансирование школьной команды по квиддичу или наймите новых учителей и тому подобное..."]),
        silver_scroll(id=27, name="Кляп с шариком",           cost=200,   comments=["Разве она не прелестна?"]),
        silver_scroll(id=28, name="Новая одежда №1",     cost=150,   comments=["Еще один (довольно длинный) побочный квест..."]),
        silver_scroll(id=29, name="Новая одежда №2",     cost=200,   comments=[".........."]),
        silver_scroll(id=30, name="Команда",           cost=70,    comments=["Один из самых ранних эскизов, связанный с побочными квестами квиддича..."]) ]

    return
    
label shop_intro:
    show screen shop_screen
    if shop_found:
        twi "Здравствуйте, профессор! Вы \nхотели что-то приобрести?"
        jump shop_menu
    else:
        $ show_clothes_store = True
        $ shop_found = True
        fre "Профессор Дамблдор? Что вы здесь делаете? Мы думали, что вы больше не выходите из своей башни."
        ger "Вы здесь для того, чтобы нас прикрыть?"
        m "Прикрыть вас? Зачем мне это?"
        fre "Да так!"
        ger "Мы точно не продаем зелья, которое не крали у профессора Снейпа."
        fre "Нет, сэр! Запрещенных товаров здесь нет."
        ger "Вообще нет никаких!"
        fre "Но если бы мы их продавали..."
        ger "Но их у нас, совсем нет."
        fre "Они бы продавались по самым лучшим ценам в школе."
        ger "Непревзойденно."
        m "Хммм. И какие зелья ты \'не\' продаешь?"
        fre "Мы не продаем оборотное зелье."
        ger "Даже и не мечтаем о таком."
        m "А другие ништячки у вас имеются?"
        ger "У нас есть книги, угощения и безделушки на продажу."
        fre "Посмотрите."
        jump shop_menu
    
label shop_menu:
    show screen shop_screen
    call screen shop_screen
    
    
label sscrolls:
    show screen shop_screen
    $ scrolls_range = range(1,16)
    jump store_scrolls
label sscrolls2:
    show screen shop_screen
    $ scrolls_range = range(16,31)
    jump store_scrolls

label store_scrolls:
    python:
        scrolls_menu = []
        for scroll in scrolls_range:
            sc = sacred_scrolls[scroll]
            if not sscroll_[sc.id]:
                scrolls_menu.append( ("-Свиток №"+str(sc.id)+": "+sc.name+"-", sc) )
        scrolls_menu.append(("-Назад-", "nvm"))
        result = renpy.display_menu(scrolls_menu)

    if result == "nvm":
        jump shop_menu
    else:
        $ the_gift = "images/store/31.png" # SACRED SCROLL.
        show screen gift
        with d3
        dahr "Свиток, содержащий священные знания.\n(Может также содержать спойлеры)."
        menu:
            "-Купить свиток за ([result.cost] галлеонов)-":
                if gold >= result.cost:
                    $ gold -= result.cost
                    $ sscroll_[result.id] = True # Turns TRUE if the scroll had been bought.
                    $ renpy.play('sounds/win_04.mp3')   #Not loud.
                    ">Новый свиток был добавлен в твою коллекцию, священных свитков."
                    hide screen gift
                    with d3
                    call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                    call screen shop_screen
                else:
                    call no_gold #Massage: m "I don't have enough gold".
                    hide screen gift
                    jump store_scrolls
            "-Назад-":
                hide screen gift
        jump store_scrolls
    
    
label shop_books:
    show screen shop_screen
    twi "Какой тип книги вы предпочитаете?"
    label shop_book_menu:
    menu:
        "-Образовательные книги-":
            label education_menu:
            $ books_menu_list = []
            $ books_menu_list.extend(Books_OBJ.read_books)
            $ books_menu_list.extend(Books_OBJ.write_books)
        "-Художественная литература-":
            if not fiction_books_intro:
                twi "Эти книги - в основном легкая \nэротика..." 
                ger "Некоторые девушки настаивали на том, чтобы мы их заказали."
                $ fiction_books_intro = True
            label fiction_menu:
            $ books_menu_list = []
            $ books_menu_list.extend(Books_OBJ.fiction_books)
        "-Назад-":
            call screen shop_screen 
    python:
        books_menu = []
        for book in books_menu_list:
            if book.purchased:
                books_menu.append((book.getMenuTextPurchased(),book))
            else:
                books_menu.append((book.getStoreMenuText(),book))
        books_menu.append(("-Назад-", "nvm"))
        BookOBJ = renpy.display_menu(books_menu)
    if BookOBJ == "nvm":
        jump shop_book_menu
    elif BookOBJ.purchased:
        call do_have_book #Message that says that you already bought this book.
    else:
        call purchase_book 
    if BookOBJ in Books_OBJ.get_edu():
        jump education_menu
    if BookOBJ in Books_OBJ.get_fic():
        jump fiction_menu
    
label purchase_book:
    $ the_gift = BookOBJ.picture
    show screen gift
    with d3
    "[BookOBJ.book_description]"
    menu:
        "-Купить книгу за [BookOBJ.cost] галлеонов -":
            if gold >= BookOBJ.cost:
                $ gold -= BookOBJ.cost
                $ BookOBJ.purchased = True
                "Книга [BookOBJ.name] была добавлена в твою коллекцию."
                hide screen gift
                with d3
            else:
                call no_gold #Massage: m "I don't have enough gold".
        "-Назад-":
            hide screen gift
    return
    
    
label shop_potion_menu:
    show screen shop_screen
    python:
        potion_menu = []
        potion_menu.append(("-Нахождение предметов-", "questions"))
        for potion in potion_lib.getBuyable():
            if whoring < potion.whoring_rec:
                potion_menu.append(("{color=#858585}-"+potion.name+"-{/color}","whoring"))
            else:
                potion_menu.append(("-"+potion.name+"-",potion))
        potion_menu.append(("-Назад-", "nvm"))
        PotionOBJ = renpy.display_menu(potion_menu)
    if isinstance(PotionOBJ, silver_potion):
        python:
            potion_menu = []
            potion_menu.append(("-Купить зелье за "+str(PotionOBJ.cost)+" Галлеонов-", PotionOBJ))
            potion_menu.append(("-Назад-", "nvm"))
            choice = renpy.display_menu(potion_menu)
        if isinstance(choice, silver_potion):
            if gold > PotionOBJ.cost:
                $ gold -= PotionOBJ.cost
                $ potion_inv.add(PotionOBJ.id)
                $ renpy.say(m, PotionOBJ.name+" Приобретен, хотя не хватает ключевого ингредиента...")
            else:
                $ renpy.say(m, "У меня недостаточно галлеонов.")
        call screen shop_screen
    if PotionOBJ == "questions":
        menu:
            "-Knotgrass-":
                m "Вы знаете, где я могу найти \"Knotgrass\"?"
                fre "Knotgrass, иногда можно найти в запретном лесу."
            "-Root of Aconite-":
                m "Вы знаете, где я могу найти \"Root of Aconite\"?"
                ger "Root of Aconite, можно найти на берегу озера."
            "-Wormwood-":
                m "Вы знаете, где я могу найти \"Wormwood\"?"
                ger "Wormwood, иногда встречается в запретном лесу."
            "-Niffler's Fancy-":
                m "Вы знаете, где я могу найти \"Niffler's Fancy\"?"
                fre "Хм ... Кажется, я слышал, что его находили у озера."
        jump shop_potion_menu
    if PotionOBJ == "whoring":
        call cust_excuse("У Гермионы статус -\"Обученная\" прежде, чем ты сможешь это купить.") 
    if PotionOBJ == "nvm":
        pass    
    call screen shop_screen
    
    
label gifts_menu:
    python:
        choices = []
        for i in gift_list:
            if whoring < i.whoringNeeded:
                choices.append( ("{color=#858585}-Товара нет в наличии-{/color}", "oos") )
            else:
                choices.append( ( ("-"+str(i.name)+"- ("+str(i.cost)+" Гал.)"), i) )
        choices.append(("-Назад-", "nvm"))
        result = renpy.display_menu(choices)
        
    if result == "nvm":
        jump shop_menu
    elif result == "oos":
        jump out
    else:
        call object_gift_block(result) 
        jump shop_menu
    
label object_gift_block(item):
    $ the_gift = item.image
    show screen gift
    with d3
    #$ tmp = item.description
    dahr "[item.description]"
    $ cost2 = item.cost * 2
    $ cost3 = item.cost * 4
    $ cost4 = item.cost * 8
    menu:
        "-Купить 1 за ([item.cost] галлеонов)-":
            call object_purchase_item(item, 1) 
        "-Купить 2 за ([cost2] галлеонов)-":
            call object_purchase_item(item, 2) 
        "-Купить 4 за ([cost3] галлеонов)-":
            call object_purchase_item(item, 4) 
        "-Купить 8 за ([cost4] галлеонов)-":
            call object_purchase_item(item, 8) 
        "-Назад-":
            hide screen gift
            pass
            
    return
            
label object_purchase_item(item, quantity):
    $ transit_time = renpy.random.randint(1, 5)
    $ order_cost = item.cost*quantity
    if gold >= (order_cost):
        menu:
            "-Добавить доставку на следующий день (15 галлеонов)-" if gold >= order_cost + 15:
                $ gold -= 15
                $ transit_time = 1
                # $ next_day = True
            "{color=#858585}-Добавить доставку на следующий день (15 галлеонов)-{/color}" if gold < order_cost + 15:
                pass
            "-Нет, спасибо-":
                pass
        $ gold -= order_cost
        $ deliveryQ.send(item,transit_time,quantity,'Gift')
        # $ gift_order = item
        # $ order_placed = True
        if transit_time ==  1:
            dahr "Благодарим за покупку во \"Всевозможных волшебных вредилках, братьев Уизли\". Ваш заказ будет доставлен завтра."
        else:
            dahr "Благодарим за покупку во \"Всевозможных волшебных вредилках, братьев Уизли\". Ваш заказ должен быть доставлен за 1 из [transit_time] дней."
        hide screen gift
        with d3
        
    else:
        call no_gold #Massage: m "I don't have enough gold".
    
    return
    
    
label app:
    menu:
        "-\"П.У.К.Н.И.\" значок (100 галлеонов)-" if not badge_01 == 7:
            $ the_gift = "images/store/29.png" # SPEW BADGE.
            show screen gift
            with d3
            dahr "значок \"П.У.К.Н.И.\" Проявите заботу..."
            menu:
                "-Купить (100 галлеонов)-":
                    if badge_01 == 7 or badge_01 == 1: # == 7 means "gifted already" # badge_01 == 1 because otherwise you could still buy it in the shop, even if you have 1 already.
                        call do_have_book # "I already own this one."
                        jump app
                    else:
                        if gold >= 100:
                            $ gold -=100
                            $ order_placed = True
                            $ bought_badge_01 = True #Affects 15_mail.rpy
                            call thx_4_shoping #Massage that says "Thank you for shopping here!".
                            call screen shop_screen
                        else:
                            call no_gold #Massage: m "I don't have enough gold".
                            hide screen gift
                            with d3
                            jump app
                "-Назад-":
                    hide screen gift
                    with d3
                    jump app
        "-Очки- (60 галлеонов)":
            $ the_gift = "images/store/glasses.png" # GLASSES
            show screen gift
            with d3
            call glasses_text 
            menu:
                "-Купить (60 галлеонов)-":
                    if gold >= 60:
                        $ gold -= 60
                        $ order_placed = True
                        $ bought_glasses = True #Affects 15_mail.rpy
                        call thx_4_shoping #Massage that says "Thank you for shopping here!".
                        call screen shop_screen
                    else:
                        call no_gold #Massage: m "I don't have enough gold".
                        jump app
                "-Назад-":
                    hide screen gift
                    jump app            
        "-Ажурные колготки (120 галлеонов)-" if not nets == 7:
            $ the_gift = "images/store/30.png" # FISHNETS.
            show screen gift
            with d3
            call nets_text 
            menu:
                "-Купить (120 галлеонов)-":
                    if nets == 7 or nets == 1: # == 7 means "gifted already"
                        call do_have_book # "I already own this one."
                        jump app
                    else:
                        if gold >= 120:
                            $ gold -= 120
                            $ order_placed = True
                            $ bought_nets = True #Affects 15_mail.rpy
                            call thx_4_shoping #Massage that says "Thank you for shopping here!".
                            call screen shop_screen
                        else:
                            call no_gold #Massage: m "I don't have enough gold".
                            hide screen gift
                            with d3
                            jump app
                "-Назад-":
                    hide screen gift
                    with d3
                    jump app
        "-Школьная Мини-Юбка- (---)" if not bought_skirt_already and not gave_miniskirt and whoring >= 3:
            $ the_gift = "images/store/07.png" # MINISKIRT
            show screen gift
            with d3
            dahr "Школьная мини-юбка. Резко улучшает оценки."
            menu:
                "-Купить юбку- (---)":
                    if vouchers >= 1: #Shows the amount of DAHR's vouchers in your possession.
                        $ vouchers -= 1 #Shows the amount of DAHR's vouchers in your possession.
                        $ order_placed = True
                        $ bought_miniskirt = True #Affects 15_mail.rpy
                        call thx_4_shoping #Massage that says "Thank you for shopping here!".
                        call screen shop_screen
                    else:
                        dahr "Этот предмет можно обменять только на \"ваучер ДАХРа\"."
                        hide screen gift
                        with d3
                        jump app
                "-Назад-":
                    hide screen gift
                    with d3
                    jump app
        "-Товар Продан-" if bought_dress_already:
            "Этот предмет распродан."
            jump app
        "{color=#858585}-Товара нет в наличии-{/color}" if not sorry_for_hesterics: # NIGHT DRESS.
            jump out # Message "Item us out of stock".
        "-Бальное платье- (1500 галлеонов)" if sorry_for_hesterics and not bought_dress_already:
            $ the_gift = "images/store/01.png" # DRESS.
            show screen gift
            with d3
            dahr "Ночная рубашка для особых случаев."
            menu:
                "-Купить платье (1500 галлеонов)-":
                    if gold >= 1500:
                        $ gold -=1500
                        $ order_placed = True
                        $ bought_ball_dress = True #Affects 15_mail.rpy
                        call thx_4_shoping #Massage that says "Thank you for shopping here!".
                        call screen shop_screen
                    else:
                        call no_gold #Massage: m "I don't have enough gold".
                        hide screen gift
                        with d3
                        jump app
                "-Назад-":
                    hide screen gift
                    with d3
                    jump app
        "-Назад-":
                jump shop_menu
    
    
    
### ALREADY HAVE THIS BOOK
label do_have_book:
    show screen bld1
    m "У меня уже есть этот экземпляр."
    hide screen bld1
    hide screen gift
    with d3
    return
    
### THANK YOU FOR shopping here.
label thx_4_shoping:
    # $ days_in_delivery2 = one_of_five  #Generating one number out of three for various porpoises.
    
    if one_of_five ==  1:
        dahr "Благодарим вас за покупку во \"Всевозможных волшебных вредилках, братьев Уизли\". Ваш заказ будет доставлен завтра."
        hide screen gift
        with d3
        return
    else:
        dahr "Благодарим вас за покупку во \"Всевозможных волшебных вредилках, братьев Уизли\". Ваш заказ должен быть доставлен за 1 из [transit_time] дней."
        hide screen gift
        with d3
        return
    
### THANK YOU FOR shopping here. IMMEDIATE DELIVERY.
label thx_4_shoping2:
    dahr "Благодарим вас за покупку во \"Всевозможных волшебных вредилках, братьев Уизли\"."
    hide screen gift
    with d3
    return
    
### NOT ENOUGH GOLD ###
label no_gold:
    m "У меня недостаточно галлеонов... Это удручает..."
    hide screen gift
    with d3
    return
    
### ITEM IS OUT OF STOCK ###
label out:
    show screen bld1
    with d3
    dahr "Этот товар в настоящее время отсутствует в наличии."
    hide screen bld1
    with d3
    jump gifts_menu
    
