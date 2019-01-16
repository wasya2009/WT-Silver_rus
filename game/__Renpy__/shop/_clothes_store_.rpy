#477-478
label __init_variables:
    if not hasattr(renpy.store,'clothes_intro_done'): #important!
        $ clothes_intro_done = False
    if not hasattr(renpy.store,'outfit_order_placed'): #important!
        $ outfit_order_placed = False
    if not hasattr(renpy.store,'outfit_ready'): #important!
        $ outfit_ready = False
    if not hasattr(renpy.store,'outfit_wait_time'): #important!
        $ outfit_wait_time = 0
    if not hasattr(renpy.store,'outfit_order'): #important!
        $ outfit_order = None
    
    $ clothes_store_order_choice = None
    $ clothes_store_selection = None
    
    if not hasattr(renpy.store,'cs_stock_inventory'): #important!
        $ cs_stock_inventory = []
    if not hasattr(renpy.store,'micro_skirt'): #important!
        $ micro_skirt = False
    if not hasattr(renpy.store,'glasses'): #important!
        $ glasses = False
    if not hasattr(renpy.store,'wear_shirts'): #important!
        $ wear_shirts = True
    if not hasattr(renpy.store,'wear_skirts'): #important!
        $ wear_skirts = True
    if not hasattr(renpy.store,'gave_tinyminiskirt'): #important!
        $ gave_tinyminiskirt = False
    if not hasattr(renpy.store,'cs_accessories'): #important!
        $ cs_accessories = [False,False,False]
    if not hasattr(renpy.store,'cs_existing_stock'): #important!
        $ cs_existing_stock = [False,False,False,False,False]
    if not hasattr(renpy.store,'cs_existing_stock_gifted'): #important!
        $ cs_existing_stock_gifted = []
    
    
    return
    
label clothes_store:
    if outfit_ready:
        maf "Пришли забрать свой заказ?"
        m "Да."
        maf "Один момент, я за ним схожу."
        maf "..."
        maf "Вот ты где."
        call pickup_outfit 
        if clothes_intro_done == False:
            ">Ты входишь, и видишь старушку, занятую сшиванием двух кусков длинной темной ткани."
            ">Женщина одета почти полностью в розовый и теплый немного розово воздушный цвет."
            m "Здравствуйте."
            maf "Здравствуйте, Профессор Дамблдор."
            maf "Что я могу для вас сделать? Вы хотите новый плащ, или вам нужны изменения существующего элемента?"
            m "Не, благодарю вас, я просто здесь, чтобы сделать несколько заказов."
            maf "Конечно, сэр, чем я могу вам помочь?"
            m "Во-первых, что у вас в ассортименте?"
            maf "Ну, я портниха. Я шью униформу для персонала и студентов."
            maf "А также измененяю существующие детали гардероба. В основном, когда студент вырастает из своей одежды или проделывает дырку в своей форме."
            m "А, понятно. Вы когда-нибудь делали одежду на заказ?"
            maf "Не совсем, хотя это моя страсть. Но большая часть того, что меня попросили сделать, это стандартные черные мантии."
            m "Так вы заинтересованы в создании уникальных нарядов?"
            maf "Конечно, хотя мне придется заказать ткань. На данный момент у меня нет обширной цветовой гаммы."
            maf "А что вы хотите?"
            m "Некоторые вещи. Я еще не решил, ничего конкретного."
            maf "Ну... пока вы решаете, не стесняйтесь осмотреть в магазине ассортимент."
            $ clothes_intro_done = True
            jump clothes_menu
    maf "Что я могу предложить вам сегодня?"
    jump clothes_menu
    
label clothes_menu:
    menu:
        "{color=#858585}-Индивидуальный Заказ-{/color}"if outfit_order_placed:
            call cust_excuse("Одновременно можно разместить только один заказ.") 
            jump clothes_menu
        "-Индивидуальный Заказ-"if not outfit_order_placed:
            jump custom_orders
        "-Одежда-":
            jump existing_stock
        "-Уйти-":
            m "На сегодня все. Спасибо."
            maf "Не стоит благодарности, сэр. Возвращайтесь в любое удобное время."
            jump day_main_menu
   
label custom_orders:
    
    call clothes_store_gui 
    
    if isinstance(clothes_store_order_choice,hermione_outfit):
        if clothes_store_order_choice.purchased:
            call cust_excuse("У тебя уже куплен этот наряд.") 
            jump custom_orders
        else:
            if clothes_store_order_choice == hg_gryffCheer_OBJ:
                m "Я бы хотел заказать наряд группы поддержки."
                maf "Костюм болельщицы? Эти ужасно грубые вещи популярны в Америке?"
                maf "Зачем он вам?"
                m "Ну, я разговаривал с Роладной Хуч, и она практически умоляла меня создать команду поддержки для каждого факультета."
                maf "Мадам Хуч так сказала?"
                m "Да, конечно. Я сказал нет, но согласился на одну студентку-испытателя из Гриффиндора."
                maf "Ну, это кажется достаточно справедливым. У вас есть какие-то предпочтения по дизайну?"
                m "Не совсем, просто сделайте его спортивным."
                maf "Хорошо, приходите ко мне через несколько дней, я думаю будет готово."
                m "Спасибо."
                call place_outfit_order 
                jump clothes_menu
            
            if clothes_store_order_choice == hg_slythCheer_OBJ:
                m "Я бы хотел заказать еще один наряд болельщицы."
                maf "Другой болельщицы? Я думала, вы сказали, что это был эксперимент только на одного человека?"
                m "Конечно, но с успехом болельщицы Гриффиндора, и Слизеринцы себе тоже потребовали."
                maf "Ах эти Слизеринцы, никогда не хотят быть вторыми."
                maf "Итак, вы хотите, тот же базовый дизайн или будут пожелания его как-то изменить?"
                m "Может быть, сделать его немного более спортивным, если вы понимаете, что я имею в виду."
                maf "Что ж, вы сможете забрать его через несколько дней."
                m "Спасибо."
                call place_outfit_order 
                jump clothes_menu
            
            if clothes_store_order_choice == hg_maid_OBJ:
                m "Я бы хотел заказать костюм горничной."
                maf "Костюм горничной, зачем он вам нужен? Конечно, эльфы и так держат вашу башню в чистоте."
                m "Это будет подарок."
                maf "Для кого?"
                m "Боюсь, я не могу сказать."
                maf "Ну, если это не для студента..."
                maf "Вы придерживаетесь какого-то стиля?"
                m "Желательно, французская горничная."
                maf "..."
                maf "Ну, я смогу сделать его, через пару дней, как получу материалы."
                m "Спасибо."
                call place_outfit_order 
                jump clothes_menu
            
            if clothes_store_order_choice == hg_silkNightgown_OBJ:
                m "Я хотел бы сегодня заказать другой наряд."
                maf "Конечно, Сэр. Эти наряды стали изюминкой моей работы. Все остальное уже кажется сравнительно консервативным."
                m "Ну, я могу заверить вас, что этот наряд не консервативен."
                maf "Хммм?"
                m "Я бы хотел заказать ночную женскую сорочку."
                maf "А, это не кажется вам уже чрезмерн-"
                m "Из шелка."
                maf "Ах. Я предполагаю, вы также хотите, чтобы она была прозрачной?"
                m "Если это, вообще возможно."
                maf "Конечно возможно, за кого вы меня принимаете?"
                maf "Приходится ткань заказывать с простыми материалами, хотя шелк стоит не дешево."
                m "Не беспокойтесь о стоимости."
                maf "Как пожелаете, сэр, будет готово через пару дней."
                m "Спасибо."
                call place_outfit_order 
                jump clothes_menu
            
            if clothes_store_order_choice == hg_ballDress_OBJ and not sorry_for_hesterics:
                call cust_excuse("Ты еще не можешь купить этот наряд...") 
                jump custom_orders
            if clothes_store_order_choice == hg_ballDress_OBJ and sorry_for_hesterics:
                m "Вы продаете бальные платья?"
                maf "Хммм, мы продаем, хотя они вполне посредственны. Зачем оно вам?"
                m "Одна 'девочка' обратилась ко мне с проблемой. По-видимому, она неспособна купить платье для ежегодного осеннего бала."
                maf "Как трагично, я уверена, что одного из этих простого покроя будет достаточно."
                m "Я подумал, что мог бы сделать его на заказ. Она очень хорошая девочка."
                maf "Я поняла. Буду ли я права, предполагая, что размеры у девочки такие же, как и у других нарядов, которые вы у меня заказывали?"
                m "Да, примерно."
                maf "Тогда я сделаю ей лучшее платье, которое когда-либо видела эта школа. Насколько я слышала, она заслужила это..."
                maf "Оно будет готово примерно через неделю."
                m "Неделю? Почему так долго?"
                maf "Бальное платье-это вам не просто, сложил вместе куски ткани и пришил. Оно требует любви и внимания. И еще это не дешево."
                m "Что ж, благодарю вас."
                maf "Всегда пожалуйста."
                call place_outfit_order 
                jump clothes_menu
            
            if clothes_store_order_choice == hg_msMarvel_OBJ:
                m "Скажите мне, мадам Мафкин, вы когда-нибудь слышали о супер-героях?"
                maf "А, да, это такие люди в комиксах. Мой внук очень их любит."
                m "Фантастика. Я хотел спросить, не могли бы вы сделать мне костюм."
                maf "Конечно, есть что-то на примете?"
                m "Вы знаете кого-нибудь из вселенной Marvel?"
                maf "Боюсь, что нет..."
                maf "Но я уверена, что у моего внука есть такой комикс. Я собираюсь навестить его в эти выходные, чтобы изучить."
                m "Большое спасибо."
                maf "Не нужно благодарить меня, сэр. Оплаты будет достаточно."
                call place_outfit_order 
                jump clothes_menu
            
            if clothes_store_order_choice == hg_heartDancer_OBJ:
                m "Вы когда-нибудь видели пародийное шоу, мадам?"
                maf "И даже больше, я разрабатывала несколько нарядов для них!"
                m "Великолепно, я хотел спросить, могу ли я сделать заказ."
                maf "Какой-то определенный цвет?"
                m "Идеально будет красный."
                maf "Как пожелаете."
                m "Большое спасибо."
                maf "Всегда пожалуйста, сэр."
                call place_outfit_order 
                jump clothes_menu
            
            if clothes_store_order_choice == hg_powerGirl_OBJ:
                m "Мне было интересно, сможете ли вы сделать мне костюм супергероя."
                maf "Конечно, есть что-то на примете?"
                m "Вы знаете о Power Girl?"
                maf "Боюсь, что нет..."
                maf "Но я уверена, что у моего внука есть о ней комикс. Я собираюсь навестить его в эти выходные, чтобы изучить."
                m "Большое спасибо."
                maf "Не нужно благодарить меня, сэр. Оплаты будет достаточно."
                call place_outfit_order 
                jump clothes_menu
            
            if clothes_store_order_choice == hg_harleyQuinn_OBJ:
                m "Я хотел спросить, не могли бы вы сделать мне костюм суперзлодея."
                maf "Конечно, есть что-то на примете?"
                m "Вы знаете о Harley Quinn?"
                maf "Боюсь, что нет..."
                maf "Но я уверена, что у моего внука есть подобный комикс. Мне придется вырвать комикс с ней из его грязных рук."
                m "Большое спасибо."
                maf "Вы всегда желанный покупатель."
                call place_outfit_order 
                jump clothes_menu
            
            if clothes_store_order_choice == hg_laraCroft_OBJ:
                m "Мне было интересно, можно ли сделать мне другой костюм."
                maf "Конечно, есть что-то на примете?"
                m "Я не думаю, что вы знаете про Lara Croft?"
                maf "Боюсь, что нет..."
                m "Это персонаж видеоигр..."
                maf "Мой внучок маленький магл, очень любит видеоигры. Уверена, он сможет показать мне, как она выглядит."
                m "Большое спасибо."
                maf "Пожалуйста. Я увижусь с ним сегодня вечером, так, что, я думаю смогу закончить костюм немного быстрее чем обычно."
                m "Фантастика."
                call place_outfit_order 
                jump clothes_menu
            
            if clothes_store_order_choice == hg_christmas_OBJ:
                m "Я хотел спросить, не могли бы вы сделать мне праздничный костюм."
                maf "Конечно, какой праздник вы хотите \"праздновать\"?"
                m "Рождество."
                maf "В это время года?"
                m "Никогда не рано начинать праздник..."
                maf "Видимо, нет. Я его сделаю, как только смогу. "
                m "Большое спасибо."
                maf "Пожалуйста. Я даже сделаю для вас, специальную цену. Считайте, что это мой рождественский подарок для вас..."
                m "Спасибо."
                call place_outfit_order 
                jump clothes_menu
            
            if clothes_store_order_choice == hg_pirate_OBJ:
                m "Я хочу пиратский наряд"
                maf "Хорошо"
                call place_outfit_order 
                jump clothes_menu

            if clothes_store_order_choice == hg_bio_OBJ:
                m "Вы когда-нибудь слышали о BioShock Infinite?"
                maf "Био что?"
                m "..."
                m "Может быть, об этом вы спросите своего внука..."
                maf "Полагаю, вам нужен костюм из этого Био, чего бы это ни значило?"
                m "Если это не слишком много..."
                maf "Считайте, что сделано!"
                m "Большое спасибо."
                maf "Пожалуйста."
                call place_outfit_order 
                jump clothes_menu

            if clothes_store_order_choice == hg_yenn_OBJ:
                m "Вы когда-нибудь слышали о волшебнице Yennefer?"
                maf "Конечно! Про мать схлопывания вселенной, не быстро забудешь..."
                m "Как думаете, сможете сделать копию ее наряда?"
                maf "Конечно."
                m "Большое спасибо."
                maf "Вы можете отблагодарить меня монетой!"
                call place_outfit_order 
                jump clothes_menu
    else:
        jump clothes_menu
        
        
label place_outfit_order:
    $ outfit_OBJ = clothes_store_order_choice
    if gold >= outfit_OBJ.cost:
        $ gold -= outfit_OBJ.cost
        $ outfit_wait_time = outfit_OBJ.wait_time
        $ outfit_order = clothes_store_order_choice
        $ outfit_order_placed = True
        maf "Я пришлю вам сову, когда закончу."
        jump clothes_menu
    else:
        m "У меня нет [outfit_OBJ.cost] галлеонов."
        m "Это удручает."
        jump clothes_menu
return

label outfit_purchase_check:
    if outfit_wait_time <= 0:
        $ outfit_ready = True
        $ letters += 1
    else:
       $ outfit_wait_time -= 1
return
    
label pickup_outfit:
    
    if outfit_order_placed: # OUTFIT
        $ outfit_order.purchased = True
        #$ outfit_inventory.append(outfit_order)
        call display_package("> "+outfit_order.name+R" наряд был добавлен к твоим вещам.") 
        call receive_package 
        call screen main_room_menu
        
return

label display_package(str1):
    $ the_gift = "images/store/07.png"
    show screen gift
    with d3
    "[str1]"
    hide screen gift
    with d3
return

label receive_package:
    if letters >= 1:
        $ letters -= 1
    $ outfit_order = None
    $ outfit_order_placed = False
    $ outfit_ready = False
return

label cust_excuse(text="Это, ты еще не можешь использовать"): #custom text option for other ideas
    show screen blktone8
    ">[text]"
    hide screen blktone8
    return

label existing_stock:
    menu:
        "-Краска для волос-":
            label existing_stock_dyes:
            menu:
                "{color=#858585}-Светлая краска- (20 галлеонов)-{/color}"if "blonde_dye" in cs_existing_stock:
                    call cust_excuse(">У тебя уже она есть.") 
                    jump existing_stock_dyes
                "-Светлая краска- (20 галлеонов)" if "blonde_dye" not in cs_existing_stock:
                    maf "Очень приятный оттенок желтого."
                    if cheats_active or game_difficulty <= 2:
                        ">Требует уровня распутства 5 для использования.<"
                    menu:
                        "-Купить (20 галлеонов)-":
                            call cs_buy_stock("blonde_dye", 20) 
                            jump existing_stock_dyes
                        "-Назад-":
                            jump existing_stock_dyes

                "{color=#858585}-Красная краска- (20 галлеонов)-{/color}"if "red_dye" in cs_existing_stock:
                    call cust_excuse(">У тебя уже она есть.") 
                    jump existing_stock_dyes
                "-Красная краска- (20 галлеонов)" if "red_dye" not in cs_existing_stock:
                    maf "Очень приятный оттенок красного."
                    if cheats_active or game_difficulty <= 2:
                        ">Требует уровня распутства 5 для использования.<"
                    menu:
                        "-Купить (20 галлеонов)-":
                            call cs_buy_stock("red_dye", 20) 
                            jump existing_stock_dyes
                        "-Назад-":
                            jump existing_stock_dyes

                "{color=#858585}-Малиновый Краситель- (40 галлеонов)-{/color}"if "crimson_dye" in cs_existing_stock:
                    call cust_excuse(">У тебя уже он есть.") 
                    jump existing_stock_dyes
                "-Малиновый Краситель- (40 галлеонов)" if "crimson_dye" not in cs_existing_stock:
                    maf "Очень насыщенный оттенок красного."
                    if cheats_active or game_difficulty <= 2:
                        ">Требует уровня распутства 8 для использования.<"
                    menu:
                        "-Купить (40 галлеонов)-":
                            call cs_buy_stock("crimson_dye", 40) 
                            jump existing_stock_dyes
                        "-Назад-":
                            jump existing_stock_dyes

                "{color=#858585}-Черная краска- (200 галлеонов)-{/color}"if "black_dye" in cs_existing_stock:
                    call cust_excuse(">У тебя уже она есть.") 
                    jump existing_stock_dyes
                "-Черная краска- (200 галлеонов)" if "black_dye" not in cs_existing_stock:
                    maf "Черный как фестрал! Как я слышала."
                    if cheats_active or game_difficulty <= 2:
                        ">Требует уровня распутства 8 для использования.<"
                    menu:
                        "-Купить (200 галлеонов)-":
                            call cs_buy_stock("black_dye", 200) 
                            jump existing_stock_dyes
                        "-Назад-":
                            jump existing_stock_dyes

                "{color=#858585}-Зеленая краска- (60 галлеонов)-{/color}"if "green_dye" in cs_existing_stock:
                    call cust_excuse(">У тебя уже она есть.") 
                    jump existing_stock_dyes
                "-Зеленая краска- (60 галлеонов)" if "green_dye" not in cs_existing_stock:
                    maf "Яркий оттенок зеленого цвета."
                    if cheats_active or game_difficulty <= 2:
                        ">Требует уровня распутства 11 для использования.<"
                    menu:
                        "-Купить (60 галлеонов)-":
                            call cs_buy_stock("green_dye", 60) 
                            jump existing_stock_dyes
                        "-Назад-":
                            jump existing_stock_dyes

                "{color=#858585}-Голубая краска- (60 галлеонов)-{/color}"if "blue_dye" in cs_existing_stock:
                    call cust_excuse(">У тебя уже она есть.") 
                    jump existing_stock_dyes
                "-Голубая краска- (60 галлеонов)" if "blue_dye" not in cs_existing_stock:
                    maf "Яркий оттенок синего цвета."
                    if cheats_active or game_difficulty <= 2:
                        ">Требует уровня распутства 11 для использования.<"
                    menu:
                        "-Купить (60 галлеонов)-":
                            call cs_buy_stock("blue_dye", 60) 
                            jump existing_stock_dyes
                        "-Назад-":
                            jump existing_stock_dyes

                "{color=#858585}-Фиолетовая краска- (80 галлеонов)-{/color}"if "purple_dye" in cs_existing_stock:
                    call cust_excuse(">У тебя уже она есть.") 
                    jump existing_stock_dyes
                "-Фиолетовая краска- (80 галлеонов)" if "purple_dye" not in cs_existing_stock:
                    maf "Очень приятный фиолетовый оттенок."
                    if cheats_active or game_difficulty <= 2:
                        ">Требует уровня распутства 11 для использования.<"
                    menu:
                        "-Купить (80 галлеонов)-":
                            call cs_buy_stock("purple_dye", 80) 
                            jump existing_stock_dyes
                        "-Назад-":
                            jump existing_stock_dyes

                "{color=#858585}-Розовая Краска- (200 галлеонов)-{/color}"if "pink_dye" in cs_existing_stock:
                    call cust_excuse(">У тебя уже она есть.") 
                    jump existing_stock_dyes
                "-Розовая Краска- (200 галлеонов)" if "pink_dye" not in cs_existing_stock:
                    maf "Такой же яркий и розовый, как мой... Лучше больше ничего не говорить."
                    if cheats_active or game_difficulty <= 2:
                        ">Требует уровня распутства 14 для использования.<"
                    menu:
                        "-Купить (200 галлеонов)-":
                            call cs_buy_stock("pink_dye", 200) 
                            jump existing_stock_dyes
                        "-Назад-":
                            jump existing_stock_dyes

                "{color=#858585}-Белая краска- (400 галлеонов)-{/color}"if "white_dye" in cs_existing_stock:
                    call cust_excuse(">У тебя уже она есть.") 
                    jump existing_stock_dyes
                "-Белая краска- (400 галлеонов)" if "white_dye" not in cs_existing_stock:
                    maf "Белый, яркий и чистый, как кожа Единорога."
                    if cheats_active or game_difficulty <= 2:
                        ">Требует уровня распутства 17 для использования.<"
                    menu:
                        "-Купить (400 галлеонов)-":
                            call cs_buy_stock("white_dye", 400) 
                            jump existing_stock_dyes
                        "-Назад-":
                            jump existing_stock_dyes

                "-Назад-":
                    jump existing_stock



        "-Верх-":#Jeans#Stockings#Fishnet Stockings#Lace Bra and Panties#Cup-less Lace Bra#Silk Bra and Panties
            label existing_stock_tops:
            menu:
                "{color=#858585}-Пуловер маглов- (50 галлеонов)-{/color}"if "normal_pullover" in cs_existing_stock:
                    call cust_excuse(">У тебя уже он есть.") 
                    jump existing_stock_tops
                "-Пуловер маглов- (50 галлеонов)" if "normal_pullover" not in cs_existing_stock:
                    #maf "A cute pink pullover. Has a heart shaped hole for her cleavage that can magically appear if you want!"
                    maf "Милый розовый пуловер. Имеется декольте в форме сердечка, может волшебно преобразиться, если ты захочешь!"
                    if cheats_active or game_difficulty <= 2:
                        ">Требует уровня распутства 2 для ношения.<"
                    menu:
                        "-Купить (50 галлеонов)-":
                            call cs_buy_stock("normal_pullover", 50) 
                            jump existing_stock_tops
                        "-Назад-":
                            jump existing_stock_tops

                "{color=#858585}-Свитер маглов- (60 галлеонов)-{/color}"if "normal_sweater" in cs_existing_stock:
                    call cust_excuse(">У тебя уже он есть.") 
                    jump existing_stock_tops
                "-Свитер маглов- (60 галлеонов)" if "normal_sweater" not in cs_existing_stock:
                    maf "Свитер, который она носила в 3 фильме! Когда она ударила этого негодяя Малфоя в лицо! Мне понравилась эта сцена."
                    if cheats_active or game_difficulty <= 2:
                        ">Требует уровня распутства 2 для ношения.<"
                    menu:
                        "-Купить (60 галлеонов)-":
                            call cs_buy_stock("normal_sweater", 60) 
                            jump existing_stock_tops
                        "-Назад-":
                            jump existing_stock_tops

                #"{color=#858585}-Waitress Top- (100 Gold)-{/color}"if "normal_waitress_top" in cs_existing_stock:
                #    call cust_excuse(">You already own this.")
                #    jump existing_stock_tops
                #"-Waitress Top- (100 Gold)" if "normal_waitress_top" not in cs_existing_stock:
                #    maf "Very cute looking top if I may say so myself."
                #    if cheats_active or game_difficulty <= 2:
                #        ">Requires a whoring level of 8 to be worn.<"
                #    menu:
                #        "-Buy the item (100 gold)-":
                #            call cs_buy_stock("normal_waitress_top", 100)
                #            jump existing_stock_tops
                #        "-Never mind-":
                #            jump existing_stock_tops

                "{color=#858585}-Кожаная куртка с короткими рукавами- (200 галлеонов)-{/color}"if "wicked_leather_jacket_short_sleeves" in cs_existing_stock:
                    call cust_excuse(">У тебя уже она есть.") 
                    jump existing_stock_tops
                "-Кожаная куртка с короткими рукавами- (200 галлеонов)" if "wicked_leather_jacket_short_sleeves" not in cs_existing_stock:
                    maf "Черная кожаная куртка с короткими рукавами. Можно носить и расстегнутой."
                    if cheats_active or game_difficulty <= 2:
                        ">Требует уровня распутства 17 для ношения.<"
                    menu:
                        "-Купить (200 галлеонов)-":
                            call cs_buy_stock("wicked_leather_jacket_short_sleeves", 200) 
                            jump existing_stock_tops
                        "-Назад-":
                            jump existing_stock_tops

                "{color=#858585}-Кожаная куртка без рукавов- (200 галлеонов)-{/color}"if "wicked_leather_jacket_sleeveless" in cs_existing_stock:
                    call cust_excuse(">У тебя уже она есть.") 
                    jump existing_stock_tops
                "-Кожаная куртка  без рукавов- (200 галлеонов)" if "wicked_leather_jacket_sleeveless" not in cs_existing_stock:
                    maf "Черная кожаная куртка без рукавов. Можно носить и расстегнутой."
                    if cheats_active or game_difficulty <= 2:
                        ">Требует уровня распутства 17 для ношения.<"
                    menu:
                        "-Купить (200 галлеонов)-":
                            call cs_buy_stock("wicked_leather_jacket_sleeveless", 200) 
                            jump existing_stock_tops
                        "-Назад-":
                            jump existing_stock_tops

                "{color=#858585}-Кожаная куртка с длинными рукавами- (200 галлеонов)-{/color}"if "wicked_leather_jacket_sleeves" in cs_existing_stock:
                    call cust_excuse(">У тебя уже она есть.") 
                    jump existing_stock_tops
                "-Кожаная куртка с длинными рукавами- (200 галлеонов)" if "wicked_leather_jacket_sleeves" not in cs_existing_stock:
                    maf "Черная кожаная куртка с длинными рукавами. Можно также носить расстегнутой."
                    if cheats_active or game_difficulty <= 2:
                        ">Требует уровня распутства 17 для ношения.<"
                    menu:
                        "-Купить (200 галлеонов)-":
                            call cs_buy_stock("wicked_leather_jacket_sleeves", 200) 
                            jump existing_stock_tops
                        "-Назад-":
                            jump existing_stock_tops

                "{color=#858585}-Ажурный Топик- (60 галлеонов)-{/color}"if "top_fishnets" in cs_existing_stock:
                    call cust_excuse("У тебя уже он есть. - Требуется уровень распутства 20 для того, чтобы он появился в гардеробе.") 
                    jump existing_stock_tops
                "-Ажурный Топик- (60 галлеонов)" if "top_fishnets" not in cs_existing_stock:
                    maf "Этот ажурный топик ничего не скрывает! Какая девушка, захочет носить его на территории школы?"
                    if cheats_active or game_difficulty <= 2:
                        ">Требует уровня распутства 20 для ношения.<"
                    menu:
                        "-Купить (60 галлеонов)-":
                            call cs_buy_stock("top_fishnets", 60) 
                            jump existing_stock_tops
                        "-Назад-":
                            jump existing_stock_tops

                "-Назад-":
                    jump existing_stock


        "-Брюки и юбки-":#Jeans#Stockings#Fishnet Stockings#Lace Bra and Panties#Cup-less Lace Bra#Silk Bra and Panties
            label existing_stock_pants_skirts:
            menu:
                "{color=#858585}-Мини юбка с поясом- (75 галлеонов)-{/color}"if "skirt_belted_mini" in cs_existing_stock:
                    call cust_excuse(">У тебя уже она есть.") 
                    jump existing_stock_pants_skirts
                "-Мини юбка с поясом- (75 галлеонов)" if "skirt_belted_mini" not in cs_existing_stock:
                    maf "Мини юбка с поясом. Очень модная!"
                    if cheats_active or game_difficulty <= 2:
                        ">Требует уровня распутства 8 для ношения.<"
                    menu:
                        "-Купить (75 галлеонов)-":
                            call cs_buy_stock("skirt_belted_mini", 75) 
                            jump existing_stock_pants_skirts
                        "-Назад-":
                            jump existing_stock_pants_skirts

                "{color=#858585}-Микро юбка с поясом- (150 галлеонов)-{/color}"if "skirt_belted_micro" in cs_existing_stock:
                    call cust_excuse(">У тебя уже она есть.") 
                    jump existing_stock_pants_skirts
                "-Микро юбка с поясом- (150 галлеонов)" if "skirt_belted_micro" not in cs_existing_stock:
                    maf "Очень короткая юбка с поясом. Очень откровенная! Будем надеяться, что девушка носит нижнее белье!"
                    if cheats_active or game_difficulty <= 2:
                        ">Требует уровня распутства 17 для ношения.<"
                    menu:
                        "-Купить (150 галлеонов)-":
                            call cs_buy_stock("skirt_belted_micro", 150) 
                            jump existing_stock_pants_skirts
                        "-Назад-":
                            jump existing_stock_pants_skirts

                "{color=#858585}-Джинсы- (75 галлеонов)-{/color}"if "pants_jeans_long" in cs_existing_stock:
                    call cust_excuse(">У тебя уже они есть.") 
                    jump existing_stock_pants_skirts
                "-Джинсы- (75 галлеонов)" if "pants_jeans_long" not in cs_existing_stock:
                    maf "Стандартные джинсы маглов, хотя и немного длинные."
                    if cheats_active or game_difficulty <= 2:
                        ">Требует уровня распутства 2 для ношения.<"
                    menu:
                        "-Купить (75 галлеонов)-":
                            call cs_buy_stock("pants_jeans_long", 75) 
                            jump existing_stock_pants_skirts
                        "-Назад-":
                            jump existing_stock_pants_skirts

                "{color=#858585}-Короткие джинсы- (150 галлеонов)-{/color}"if "pants_jeans_short" in cs_existing_stock:
                    call cust_excuse(">У тебя уже они есть.") 
                    jump existing_stock_pants_skirts
                "-Короткие джинсы- (150 галлеонов)" if "pants_jeans_short" not in cs_existing_stock:
                    maf "Короткие джинсы daisy dukes."
                    if cheats_active or game_difficulty <= 2:
                        ">Требует уровня распутства 11 для ношения.<"
                    menu:
                        "-Купить (150 галлеонов)-":
                            call cs_buy_stock("pants_jeans_short", 150) 
                            jump existing_stock_pants_skirts
                        "-Назад-":
                            jump existing_stock_pants_skirts

                #"{color=#858585}-Retro Shorts- (170 Gold)-{/color}"if "pants_retro_shorts" in cs_existing_stock:
                #    call cust_excuse(">You already own this.")
                #    jump existing_stock_pants_skirts
                #"-Retro Shorts- (170 Gold)" if "pants_retro_shorts" not in cs_existing_stock:
                #    maf "A pair of skin tight retro shorts. Just the right thing to highlight a magnificent behind."
                #    if cheats_active or game_difficulty <= 2:
                #        ">Requires a whoring level of 17 to be worn.<"
                #    menu:
                #        "-Buy the item (170 gold)-":
                #            call cs_buy_stock("pants_retro_shorts", 170)
                #            jump existing_stock_pants_skirts
                #        "-Never mind-":
                #            jump existing_stock_pants_skirts

                "-Назад-":
                    jump existing_stock

        "-Чулки-":
            label existing_stock_stockings:
            menu:
                "{color=#858585}-Чулки Гриффиндор- (50 галлеонов)-{/color}"if "stockings_gryff" in cs_existing_stock:
                    call cust_excuse("У тебя уже они есть.") 
                    jump existing_stock_stockings
                "-Чулки Гриффиндор- (50 галлеонов)" if "stockings_gryff" not in cs_existing_stock:
                    maf "Пара веселых школьных чулок, цвета Гриффиндора."
                    menu:
                        "-Купить (50 галлеонов)-":
                            call cs_buy_stock("stockings_gryff", 50) 
                            jump existing_stock_stockings
                        "-Назад-":
                            jump existing_stock_stockings

                "{color=#858585}-Чулки Слизерин- (50 галлеонов)-{/color}"if "stockings_slyth" in cs_existing_stock:
                    call cust_excuse("У тебя уже они есть. - Требуется уровень распутства 9 для того, чтобы они появились в гардеробе.") 
                    jump existing_stock_stockings
                "-Чулки Слизерин- (50 галлеонов)" if "stockings_slyth" not in cs_existing_stock:
                    maf "Пара веселых школьных чулок, цвета Слизерина."
                    ">Требует уровня распутства 9 для ношения.<"
                    menu:
                        "-Купить (50 галлеонов)-":
                            call cs_buy_stock("stockings_slyth", 50) 
                            jump existing_stock_stockings
                        "-Назад-":
                            jump existing_stock_stockings

                "{color=#858585}-Ажурные чулки- (75 галлеонов)-{/color}"if "stockings_fishnet_black" in cs_existing_stock:
                    call cust_excuse("У тебя уже они есть.") 
                    jump existing_stock_stockings
                "-Ажурные чулки- (75 галлеонов)" if "stockings_fishnet_black" not in cs_existing_stock:
                    maf "Пара страстных чулок в сеточку."
                    menu:
                        "-Купить (75 галлеонов)-":
                            call cs_buy_stock("stockings_fishnet_black", 75) 
                            jump existing_stock_stockings
                        "-Назад-":
                            jump existing_stock_stockings

                "{color=#858585}-Кружевные чулки- (30 галлеонов)-{/color}"if "stockings_lace_black" in cs_existing_stock:
                    call cust_excuse("У тебя уже они есть.") 
                    jump existing_stock_stockings
                "-Кружевные чулки- (30 галлеонов)" if "stockings_lace_black" not in cs_existing_stock:
                    maf "Пара черных кружевных чулок."
                    menu:
                        "-Купить (30 галлеонов)-":
                            call cs_buy_stock("stockings_lace_black", 30) 
                            jump existing_stock_stockings
                        "-Назад-":
                            jump existing_stock_stockings


                "-Назад-":
                    jump existing_stock
        
        #"-Bras and Panties-":    ###Taken out as bra/panties not really needed
        #    label existing_stock_bras_panties:
        #    menu:
        #        "{color=#858585}-Lace Bra and Panties- (50 Gold){/color}"if "lace_set" in cs_existing_stock:
        #            call cust_excuse("You already own this.")
        #            jump existing_stock_bras_panties
        #        "-Lace Bra and Panties- (50 Gold)" if "lace_set" not in cs_existing_stock:
        #            "A lovely lace bra and panty set."
        #            menu:
        #                "-Buy the item (50 gold)-":
        #                    call cs_buy_stock("lace_set", 50)
        #                    jump existing_stock_bras_panties
        #                "-Never mind-":
        #                    jump existing_stock_bras_panties
        #        "{color=#858585}-Cup-less Lace Bra and panties- (125 Gold){/color}"if "cup_set" in cs_existing_stock:
        #            call cust_excuse("You already own this.")
        #            jump existing_stock_bras_panties
        #        "-Cup-less Lace Bra and panties- (125 Gold)" if "cup_set" not in cs_existing_stock:
        #            "A revealing piece of clothing that only serves to highlight the wearer's breasts."
        #            menu:
        #                "-Buy the item (125 gold)-":
        #                    call cs_buy_stock("cup_set", 125)
        #                    jump existing_stock_bras_panties
        #                "-Never mind-":
        #                    jump existing_stock_bras_panties
        #        "{color=#858585}-Silk Bra and Panties- (150 Gold){/color}"if "silk_set" in cs_existing_stock:
        #            call cust_excuse("You already own this.")
        #            jump existing_stock_bras_panties
        #        "-Silk Bra and Panties- (150 Gold)" if "silk_set" not in cs_existing_stock:
        #            "A smooth and comfortable lace bra and panty set."
        #            menu:
        #                "-Buy the item (150 gold)-":
        #                    call cs_buy_stock("silk_set", 150)
        #                    jump existing_stock_bras_panties
        #                "-Never mind-":
        #                    jump existing_stock_bras_panties
        #        "{color=#858585}-Latex Bra and Panties- (150 Gold){/color}"if "latex_set" in cs_existing_stock:
        #            call cust_excuse("You already own this.")
        #            jump existing_stock_bras_panties
        #        "-Latex Bra and Panties- (150 Gold)" if "latex_set" not in cs_existing_stock:
        #            "A tight and shiny lace bra and panty set."
        #            menu:
        #                "-Buy the item (150 gold)-":
        #                    call cs_buy_stock("latex_set", 150)
        #                    jump existing_stock_bras_panties
        #                "-Never mind-":
        #                    jump existing_stock_bras_panties
        #        "-Never Mind-":
        #            jump existing_stock
        


        "-Аксессуары-":
            label accessories:
            menu:
                "{color=#858585}-\"П.У.К.Н.И.\" значок-{/color}"if "SPEW_badge" in cs_existing_stock:
                    call cust_excuse("У тебя уже он есть.") 
                    jump accessories
                "-\"П.У.К.Н.И.\" значок-" if "SPEW_badge" not in cs_existing_stock:
                    maf "Значок, призванный показать твою позицию о рабстве эльфов.(Против Угнетения Колдовских Народов-Изгоев)"
                    menu:
                        "-Купить (100 галлеонов)-":
                            call cs_buy_stock("SPEW_badge",100) 
                            jump accessories
                        "-Назад-":
                            jump accessories
                "{color=#858585}-\"I <3 C.U.M.\" значок-{/color}"if "CUM_badge" in cs_existing_stock:
                    call cust_excuse("У тебя уже он есть.") 
                    jump accessories
                "-\"I <3 C.U.M.\" значок-" if "CUM_badge" not in cs_existing_stock:
                    maf "Значок, показывающий вкусовые предпочтения."
                    menu:
                        "-Купить (150 галлеонов)-":
                            call cs_buy_stock("CUM_badge",150) 
                            jump accessories
                        "-Назад-":
                            jump accessories
                "{color=#858585}-Веснушки-{/color}"if "freckles" in cs_existing_stock:
                    call cust_excuse("У тебя уже они есть.") 
                    jump accessories
                "-Веснушки-" if "freckles" not in cs_existing_stock:
                    maf "Прекрасная краска для веснушек. Теперь non-toxic!"
                    menu:
                        "-Купить (50 галлеонов)-":
                            call cs_buy_stock("freckles",50) 
                            jump accessories
                        "-Назад-":
                            jump accessories
                "{color=#858585}-Очки для чтения-{/color}"if "reading_glasses" in cs_existing_stock:
                    call cust_excuse("У тебя уже они есть.") 
                    jump accessories
                "-Очки для чтения-" if "reading_glasses" not in cs_existing_stock:
                    maf "Жаль, что мне не нужны фальшивые очки для чтения."
                    menu:
                        "-Купить (75 галлеонов)-":
                            call cs_buy_stock("reading_glasses",75) 
                            jump accessories
                        "-Назад-":
                            jump accessories
                "{color=#858585}-Винтажные очки-{/color}"if "vintage_glasses" in cs_existing_stock:
                    call cust_excuse("У тебя уже они есть.") 
                    jump accessories
                "-Винтажные очки-" if "vintage_glasses" not in cs_existing_stock:
                    maf "Эти старые очки когда-то были довольно модными."
                    menu:
                        "-Купить (60 галлеонов)-":
                            call cs_buy_stock("vintage_glasses",60) 
                            jump accessories
                        "-Назад-":
                            jump accessories
                "{color=#858585}-Псевдосперма-{/color}"if "fake_cum" in cs_existing_stock:
                    call cust_excuse("У тебя уже она есть.") 
                    jump accessories
                "-Псевдосперма-" if "fake_cum" not in cs_existing_stock:
                    maf "Это всего лишь коктейль - margarita mix..."
                    menu:
                        "-Купить (100 галлеонов)-":
                            call cs_buy_stock("fake_cum",100) 
                            jump accessories
                        "-Назад-":
                            jump accessories
                "{color=#858585}-Кошачьи ушки-{/color}"if "cat_ears" in cs_existing_stock:
                    call cust_excuse("У тебя уже они есть.") 
                    jump accessories
                "-Кошачьи ушки-" if "cat_ears" not in cs_existing_stock:
                    maf "Парочка кошачьих ушек..."
                    maf "Поставляется в комплекте с хвостиком на зажиме..."
                    menu:
                        "-Купить (70 галлеонов)-":
                            call cs_buy_stock("cat_ears",70) 
                            jump accessories
                        "-Назад-":
                            jump accessories
                "{color=#858585}-Зелье прозрачности-{/color}"if "transparency" in cs_existing_stock:
                    call cust_excuse("У тебя уже оно есть.") 
                    jump accessories
                "-Зелье прозрачности-" if "transparency" not in cs_existing_stock:
                    maf "Делает одежду немного прозрачнее при употреблении."
                    maf "На вашем месте, я бы приберегла парочку, про запас..."
                    menu:
                        "-Купить (130 галлеонов)-":
                            call cs_buy_stock("transparency",130) 
                            jump accessories
                        "-Назад-":
                            jump accessories
                "{color=#858585}-Эльфийские ушки-{/color}"if "elf_ears" in cs_existing_stock:
                    call cust_excuse("У тебя уже они есть.") 
                    jump accessories
                "-Эльфийские ушки-" if "elf_ears" not in cs_existing_stock:
                    maf "Парочка псевдо эльфийских ушек."
                    maf "Настоящие гораздо труднее достать..."
                    menu:
                        "-Купить (80 галлеонов)-":
                            call cs_buy_stock("elf_ears",80) 
                            jump accessories
                        "-Назад-":
                            jump accessories
                "-Назад-":
                    jump existing_stock
        "-Назад-":
            jump clothes_menu
    
label cs_buy_stock(item_id = "", cost):
    if gold >= cost and item_id != "":
        if item_id in cs_existing_stock:
            m "У меня уже есть это."
            return
        else:
            $ gold -= cost
            $ cs_existing_stock.append(item_id)
            maf "Большое спасибо."
            return
    else:
        m "У меня недостаточно."
        return
    
label clothes_store_gui:
    $ cs_gui_OBJ = cs_gui_class()
    call screen cs_gui

label cs_select:
    if clothes_store_selection == "EXIT":
        jump clothes_menu
    #"You picked page [cs_gui_OBJ.current_page] item [clothes_store_selection.name]!"
    $ clothes_store_order_choice = clothes_store_selection
    return
    
screen cs_gui:
    
    tag clothes_menu
    zorder hermione_main_zorder-1
    
    imagemap:
        cache False
        ground "images/store/cs_gui/c_s_ground.png"
        idle "images/store/cs_gui/c_s_idle.png"
        hover "images/store/cs_gui/c_s_hover.png"
        
        $ page_list = cs_gui_OBJ.getListOfItems()
        
        $ index = 0
        for i in range(0,2):
            for j in range(0,4):
                if index < len(page_list):
                    hotspot((213+(175*j)),(78+(255*i)),125,190) clicked [SetVariable("clothes_store_selection",page_list[index]),Jump("cs_select")]
                    add page_list[index].getStoreImage() xpos 166+(175*j) ypos (31+(254*i)) zoom 0.40
                    $ index = index+1
        
        if cs_gui_OBJ.current_page > 0:
            hotspot (156, 552, 34, 34) clicked Jump("cs_gui_index_down")
        if cs_gui_OBJ.current_page < cs_gui_OBJ.getTotalPages():
            hotspot (885, 552, 34, 34) clicked Jump("cs_gui_index_up")
        hotspot (882, 11, 42, 41) clicked [SetVariable("clothes_store_selection","EXIT"),Jump("cs_select")]#exit
    
label cs_gui_index_up:
    $ cs_gui_OBJ.current_page = cs_gui_OBJ.current_page+1
    call screen cs_gui
label cs_gui_index_down:
    $ cs_gui_OBJ.current_page = cs_gui_OBJ.current_page-1
    call screen cs_gui
    
init python:
    class cs_gui_class(object):
        current_page = 0
        
        def getListOfItems(self):
            return hermione_outfits_list[(self.current_page*8):min((self.current_page*8)+8, len(hermione_outfits_list))]
        def getNamesOfItems(self):
            return [i.name for i in self.getListOfItems()]
        def getTotalPages(self):
            return len(hermione_outfits_list)/8
            
