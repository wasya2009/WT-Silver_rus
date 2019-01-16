
init python:

    class main_quest(object):
        id = 0
        name = ""
        objective = ""
        hint_text = ""
        hint_text2 = ""
        hint_text3 = ""
        hint_text4 = ""
        hint_text5 = ""
        full_text = ""
        full_text2 = ""
        full_text3 = ""
        full_text4 = ""
        full_text5 = ""
        counter = 0
        completed = False

    class side_quest(object):
        id = 0
        name = ""
        objective = ""
        hint_text = ""
        hint_text2 = ""
        hint_text3 = ""
        hint_text4 = ""
        hint_text5 = ""
        full_text = ""
        full_text2 = ""
        full_text3 = ""
        full_text4 = ""
        full_text5 = ""
        counter = 0
        completed = False

label __init_variables:
    #Guide
    if not hasattr(renpy.store,'guide_active'): #important!
        $ guide_active = False
    if not hasattr(renpy.store,'guide_page'): #important!
        $ guide_page = 0
    if not hasattr(renpy.store,'guide_show_hint'): #important!
        $ guide_show_hint = False
    if not hasattr(renpy.store,'guide_show_next_step'): #important!
        $ guide_show_next_step = False
    if not hasattr(renpy.store,'guide_add_tip'): #important!
        $ guide_add_tip = False

    #Main Quests

    if not hasattr(renpy.store,'mQuest_0'): #important!
        $ mQuest_0 = main_quest()
    $ mQuest_0.id = 0
    $ mQuest_0.name = ""
    $ mQuest_0.objective = "Больше квестов добавлено не было."
    $ mQuest_0.hint_text = "Пока ты сам по себе. Удачи!"
    $ mQuest_0.hint_text2 = ""
    $ mQuest_0.hint_text3 = ""
    $ mQuest_0.hint_text4 = ""
    $ mQuest_0.hint_text5 = ""
    $ mQuest_0.full_text = "Пока ты сам по себе. Удачи!"
    $ mQuest_0.full_text2 = ""
    $ mQuest_0.full_text3 = ""
    $ mQuest_0.full_text4 = ""
    $ mQuest_0.full_text5 = ""

    if not hasattr(renpy.store,'mQuest_A'): #important!
        $ mQuest_A = main_quest()
    $ mQuest_A.id = 1
    $ mQuest_A.name = "Начало"
    $ mQuest_A.objective = "Найди способ вернуться домой!"
    $ mQuest_A.hint_text = ""
    $ mQuest_A.hint_text2 = ""
    $ mQuest_A.hint_text3 = ""
    $ mQuest_A.hint_text4 = ""
    $ mQuest_A.hint_text5 = ""
    $ mQuest_A.full_text = ""
    $ mQuest_A.full_text2 = ""
    $ mQuest_A.full_text3 = ""
    $ mQuest_A.full_text4 = ""
    $ mQuest_A.full_text5 = ""
    $ mQuest_A.counter = 0 #counter
    $ mQuest_A.completed = False
        
    if not hasattr(renpy.store,'mQuest_B'): #important!
        $ mQuest_B = main_quest()
    $ mQuest_B.id = 2
    $ mQuest_B.name = "Лев и Змей"
    $ mQuest_B.objective = "Найди способ справиться со скукой."
    $ mQuest_B.hint_text = ""
    $ mQuest_B.hint_text2 = ""
    $ mQuest_B.hint_text3 = ""
    $ mQuest_B.hint_text4 = ""
    $ mQuest_B.hint_text5 = ""
    $ mQuest_B.full_text = ""
    $ mQuest_B.full_text2 = ""
    $ mQuest_B.full_text3 = ""
    $ mQuest_B.full_text4 = ""
    $ mQuest_B.full_text5 = ""
    $ mQuest_B.counter = 0 #counter
    $ mQuest_B.completed = False


    #Side Quests

    if not hasattr(renpy.store,'sQuest_get_map'): #important!
        $ sQuest_get_map = side_quest()
    $ sQuest_get_map.id = 0
    $ sQuest_get_map.name = "Карта Мародеров"
    $ sQuest_get_map.objective = "Найди карту и используй ее."
    $ sQuest_get_map.hint_text = "Тест 1"
    $ sQuest_get_map.full_text = "Тест 2"
    $ sQuest_get_map.counter = 0
    $ sQuest_get_map.completed = False

    if not hasattr(renpy.store,'sQuest_buy_at_shop'): #important!
        $ sQuest_buy_at_shop = side_quest()
    $ sQuest_buy_at_shop.id = 1
    $ sQuest_buy_at_shop.name = "Всевозможные волшебные вредилки"
    $ sQuest_buy_at_shop.objective = "Купи товар в лавке Уизли."
    $ sQuest_buy_at_shop.hint_text = ""
    $ sQuest_buy_at_shop.full_text = ""
    $ sQuest_buy_at_shop.counter = 0
    $ sQuest_buy_at_shop.completed = False


    if not hasattr(renpy.store,'current_main_quest'): #important!
        $ current_main_quest = mQuest_0
    if not hasattr(renpy.store,'current_side_quests'): #important!
        $ current_side_quests = []

    #Quest Rewards
    if not hasattr(renpy.store,'quest_reward_image'): #important!
        $ quest_reward_image = "images/store/01.png" #default image is the gift box
    if not hasattr(renpy.store,'quest_reward_text'): #important!
        $ quest_reward_text = ""

    #Tips and Facts
    if not hasattr(renpy.store,'daily_rndm_tip_or_fact'): #important!
        $ daily_rndm_tip_or_fact = 0
    if not hasattr(renpy.store,'guide_tip_text'): #important!
        $ guide_tip_text = ""
    if not hasattr(renpy.store,'guide_tip_text2'): #important!
        $ guide_tip_text2 = ""
    if not hasattr(renpy.store,'guide_tip_text3'): #important!
        $ guide_tip_text3 = ""
    if not hasattr(renpy.store,'guide_tip_text4'): #important!
        $ guide_tip_text4 = ""

    return


### Quest System ###

#Play Intro
#Skip Intro
### Start of Game ###
### Activate Quest Guide and Icon after Dialogue ###

label update_quests:

    #Side Quests
    $ side_quests = [] #list of your side quests

    #Get Marauder's Map
    if sQuest_get_map.counter >=1 and sQuest_get_map.counter <= 3 and sQuest_get_map not in side_quests:
        $ side_quests.append(sQuest_get_map)

    #Buy something at the shop
    if sQuest_buy_at_shop.counter >=1 and sQuest_buy_at_shop.counter <= 3 and sQuest_buy_at_shop not in side_quests:
        $ side_quests.append(sQuest_buy_at_shop)


    #Main Quest A #Start of game till Snape unlock

    if mQuest_A.counter == 1: #Examine room
        $ mQuest_A.hint_text = "Почему бы тебе не осмотреться?"
        $ mQuest_A.full_text = "Осмотри комнату!"
        $ mQuest_A.full_text2 = "Взаимодействуй со всем, что видишь!"
    if mQuest_A.counter == 2: #Read owl's letter. Snape enters room
        # if looked at door: Side quest map activates here!
        $ mQuest_A.hint_text = "Что это за странная птица?"
        $ mQuest_A.full_text = "Нажми на сову и прочитай письмо!"
        $ mQuest_A.full_text2 = ""
        $ mQuest_A.full_text3 = "Сразу после этого появится Снейп."
        $ mQuest_A.full_text4 = "Поговори с ним!-Выбери любой вариант диалога!"
    if mQuest_A.counter == 3: #Skip to night
        #rummaging through cupboard unlocked!
        # if clicked on cupboard. Add quest "" #get healing potions
        $ mQuest_A.hint_text = "Время для сна!"
        $ mQuest_A.full_text = "Нажми на свой стол и вздремни!"
        $ mQuest_A.full_text2 = "Снейп появится на следующее утро!"
        $ mQuest_A.full_text3 = "Поговори с ним!-Выбери любой вариант диалога!"
    if mQuest_A.counter == 4: #Read owl's 2nd letter
        $ mQuest_A.hint_text = "Разве они не знают, что такое Электронная почта?"
        $ mQuest_A.full_text = "Прочитай письмо у совы!"
    if mQuest_A.counter == 5: #Get healing potions
        $ mQuest_A.hint_text = "Ты заглядывал в свой шкаф, в последнее время?"
        $ mQuest_A.full_text = "Получи три зелья из своего шкафа!"
        $ mQuest_A.full_text2 = "Ты будешь нуждаться в них позже!"
    if mQuest_A.counter == 6: # Duel # ADD custom duel guide screen
        $ mQuest_A.hint_text = "Он нападает на тебя!"
        $ mQuest_A.hint_text2 = "Ничего страшного!"
        $ mQuest_A.hint_text3 = "У него есть только эта маленькая деревянная палка для борьбы!"
        $ mQuest_A.hint_text3 = "Ты сможешь легко его победить!"
        $ mQuest_A.full_text = "Бей Снейпа!"
        $ mQuest_A.full_text2 = "Атакуй его, когда он не защищается!"
        $ mQuest_A.full_text3 = "Защищайся, когда он собирается атаковать!"
    if mQuest_A.counter == 7: # Duel # ADD custom duel guide screen
        $ mQuest_A.hint_text = ""
        $ mQuest_A.hint_text2 = ""
        $ mQuest_A.hint_text3 = ""
        $ mQuest_A.hint_text3 = ""
        $ mQuest_A.full_text = "Бей Снейпа!"
        $ mQuest_A.full_text2 = ""
        $ mQuest_A.full_text3 = ""

    #Main Quest B #Till Hermione unlock

    if mQuest_B.counter == 1: #wait for Hermione
        $ mQuest_B.hint_text = "Лучше устроиться здесь поудобнее. Видимо не скоро, я смогу покинуть это место"
        $ mQuest_B.full_text = "Подождите пару дней, пока Гермиона не появится! Тогда поговорите с Гермионой и выберите любой вариант диалога!"
    if mQuest_B.counter == 2: #Hang with Snape
        #Side quests map could complete here. Rummage through cupboard.
        $ mQuest_B.hint_text = "Может, Снейп знает, что случилось с той девушкой?"
        $ mQuest_B.full_text = "Пообщайся со Снейпом вечером и обсуди с ним ваши новые знакомства! На следующий день Гермиона постучит в твою дверь! Пригласи ее или выгоняй. В конце концов, тебе придется поговорить с ней! Нет никакого способа обойти это!"
    if mQuest_B.counter == 3: #Hermione knocks on door #If send her away, else skip to 4
        $ mQuest_B.hint_text = "Тук-Тук!"
        $ mQuest_B.full_text = "Пригласи ее или выгоняй. В конце концов тебе придется поговорить с ней! Нет никакого способа обойти это!"
    if mQuest_B.counter == 4: #Hang with Snape
        $ mQuest_B.hint_text = "Снейп? Снейп?! СНЕЕЕЙП!"
        $ mQuest_B.full_text = "Вечером пообщайтесь со Снейпом и поговорите еще раз!"
    if mQuest_B.counter == 5: #Wait for Hermione
        $ mQuest_B.hint_text = "Наблюдайте, как ваш зловещий план запустится!"
        $ mQuest_B.full_text = "Подожди Гермиону! - Поговори с ней, пока она не будет готова стать твоей ученицей!"
    if mQuest_B.counter == 6: #Wait for Hermione
        $ mQuest_B.hint_text = ""
        $ mQuest_B.full_text = ""

    #Call Reward
    if mQuest_A.counter >= 7 and not mQuest_A.completed:
        $ mQuest_A.completed = True
        call give_reward(">Ты разблокировал возможность вызывать Северуса Снейпа в свой кабинет.","images/store/snape_unlock_01.png") 

    if mQuest_B.counter == 6 and not mQuest_B.completed:
        call give_reward(">Ты открыл возможность вызывать Гермиону в свой кабинет.","images/store/hermione_unlock_01.png") 
        $ mQuest_B.counter = 7 #Makes sure it only triggers once!
    if mQuest_B.counter == 8 and not mQuest_B.completed:
        $ mQuest_B.completed = True
        call give_reward(">Ты открыл возможность покупать сексуальные услуги у Гермионы.","images/store/hermione_unlock_02.png") 

    #Set Main Quest
    if mQuest_A.counter >= 1:
        if not mQuest_A.completed:
            $ current_main_quest = mQuest_A
    if mQuest_B.counter >= 1:
        if not mQuest_B.completed:
            $ current_main_quest = mQuest_B

    #end of quest.
    #hide star icon and call main_quest_reward = ability to summon Hermione

    return






#Start: There is a star icon at the top left corner of the screen. This is will open the player guide. 
#It will help you progress through the game, give you helpful tips, or even tell you what to do next entirely.

#28.gifts.rpy
#candy:          lvl 1-7= +5
#chocolate:      lvl 1-7= +10
#plush owl:      lvl 1-2= +7,  3-4= +10, 5-6= +15, 7+= +4
#butterbeer:     lvl 1-2= +3,  3-4= +10, 5-6= +15, 7+= 20
#edu-mags:       lvl 1-2= +15, 3-4= +10, 5-6= +3,  7+= +0
#girl-mags:      lvl 1-2= +0,  3-4= +5,  5-6= +15, 7+= +15
#adult-mags:     lvl 1-2= -7,  3-4= -3,  5-6= +8,  7+= +15
#porn-mags:      lvl 1-2= -15, 3-4= -8,  5-6= +0,  7+= +15
#krum poster:    lvl 1-2= +0,  3-4= +4,  5-6= +15, 7+= +25
#lingerie:       lvl 1-2= -10, 3-4= +0,  5-6= +7,  7+= +15
#condoms:        lvl 1-2= -6,  3-4= +0,  5-6= +3,  7+= +4
#vibrator:       lvl 1-2= -10, 3-4= -10, 5-6= +0,  7+= +10
#anal lube:      lvl 1-2= -6,  3-4= -2,  5-6= +0,  7+= +5
#gag and cuffs:  lvl 1-2= -10, 3-4= -5,  5-6= +9,  7+= +15
#anal plugs:     lvl 1-2= +8,  3-4= -15, 5-6= +0,  7+= +10
#strap on:       lvl 1-2= +20, 3-4= -15, 5-6= +10, 7+= +30
#speed stick:    lvl 1-2= +20, 3-4= +20, 5-6= +30, 7+= +30
#sex doll:       lvl 1-2= -20, 3-4= -20, 5-6= +10, 7+= +30
#ADD:            lvl 1-2= ,  3-4= ,  5-6= ,  7+= 

### Run label every time before guide gets opened. ###
### Tip of the day ###

label update_tip_of_the_day:

    #Reset Text
    $ guide_tip_text = ""
    $ guide_tip_text2 = ""
    $ guide_tip_text3 = ""
    $ guide_tip_text4 = ""

    #Gift Items Tip
    if mad > 0: #Picks this first when she is mad.

        #Always relevant
        $ rndm_one_of_ten = renpy.random.randint(1, 10)

        if rndm_one_of_ten ==  1: #Broom
            $ guide_add_tip = True                                          #Max Characters
            $ guide_tip_text = "Новая метла - отличный подарок!"
            $ guide_tip_text2 = "Купить в магазине по дешевой цене"
            $ guide_tip_text3 = " только 500g!"
            $ guide_tip_text4 = "Получи ее сейчас! Возьми! ВОЗЬМИ!"
        if rndm_one_of_ten ==  2: #Condoms, Anal Lube
            $ guide_add_tip = False #False=Fact                             #Max Characters
            $ guide_tip_text = "Презервативы не могут быть лучшим подарком для"
            $ guide_tip_text2 = "молодой девушки..."
            $ guide_tip_text3 = "Как и анальная смазка!"
        if rndm_one_of_ten ==  3: #Butterbeer
            $ guide_add_tip = True                                          #Max Characters
            $ guide_tip_text = "Кажется, Гермиона злится на тебя!"
            $ guide_tip_text2 = "Подари ей немного сливочного пива!"
            $ guide_tip_text3 = "Все любят сливочное пиво!"
        if rndm_one_of_ten ==  4: #Candy
            $ guide_add_tip = True                                          #Max Characters
            $ guide_tip_text = "Кажется, Гермиона злится на тебя!"
            $ guide_tip_text2 = "Дай ей леденец, чтобы улучшить ее настроение!"
            $ guide_tip_text3 = "Ты также можешь смотреть, как она его лижет!"
        if rndm_one_of_ten ==  5: #Chocolate
            $ guide_add_tip = True                                          #Max Characters                                          
            $ guide_tip_text = "Кажется, Гермиона злится на тебя!"
            $ guide_tip_text2 = "Почему бы не дать ей немного шоколада, чтобы улучшить"
            $ guide_tip_text3 = " улучшить ее настроение!"

        #whoring specific gifts
        if rndm_one_of_ten >= 6 and rndm_one_of_ten <= 10:
            if whoring >= 0 and whoring <= 5:  #lvl 1-2    
                $ rndm_one_of_three = renpy.random.randint(1, 3)
                if rndm_one_of_three == 1:
                    $ guide_add_tip = True                                          #Max Characters
                    $ guide_tip_text = "Почему бы не купить ей Страпон?"
                    $ guide_tip_text2 = "Что может пойти не так!"
                elif rndm_one_of_three == 2:
                    $ guide_add_tip = True                                          #Max Characters
                    $ guide_tip_text = "Гермиона, кажется, очень любит"
                    $ guide_tip_text2 = " образовательные журналы!"
                    $ guide_tip_text3 = "Нет не сексуальное образование..."
                    $ guide_tip_text4 = "Да, выглядит скучно!"
                elif rndm_one_of_three == 3:
                    $ guide_add_tip = True                                          #Max Characters
                    $ guide_tip_text = "Кажется, Гермиона злится на тебя!"
                    $ guide_tip_text2 = "Может, она хочет подарок?"
                    $ guide_tip_text3 = "Просто... не покупай ей сексуальную куклу!"

            if whoring >= 6 and whoring <= 11: #lvl 3-4
                $ rndm_one_of_three = renpy.random.randint(1, 3)
                if rndm_one_of_three == 1:
                    $ guide_add_tip = True                                          #Max Characters
                    $ guide_tip_text = "Такая девушка как Гермиона может быть плюшевой"
                    $ guide_tip_text2 = "животное!"
                elif rndm_one_of_three == 2:
                    $ guide_add_tip = True                                          #Max Characters
                    $ guide_tip_text = "Ты слышал о Викторе Краме?"
                    $ guide_tip_text2 = "Все ведьмочки любят его!"
                    $ guide_tip_text3 = "Может быть, Гермиона хотела бы его постер!"
                elif rndm_one_of_three == 3:
                    $ guide_add_tip = True                                          #Max Characters
                    $ guide_tip_text = "Она по-прежнему предпочитает свои образовательные журналы,"
                    $ guide_tip_text2 = " но, возможно, ты сможешь заинтересовать ее"
                    $ guide_tip_text3 = " теми, которые специально для девочек!"

            if whoring >= 12 and whoring <= 17: #lvl 5-6
                $ rndm_one_of_three = renpy.random.randint(1, 3)
                if rndm_one_of_three == 1:
                    $ guide_add_tip = True
                    $ guide_tip_text = "Видимо они выпустили новый набор"
                    $ guide_tip_text2 = "новые и эксклюзивные плюшевые совы!"
                    $ guide_tip_text3 = "Надо поймать их всех!"
                elif rndm_one_of_three == 2:
                    $ guide_add_tip = True
                    $ guide_tip_text = "Ей действительно нравится этот Крам!"
                    $ guide_tip_text2 = "Может, тебе стоит купить ей его постер?"
                elif rndm_one_of_three == 3:
                    $ guide_add_tip = True
                    $ guide_tip_text = "Можно подумать, что Гермиона выросла"
                    $ guide_tip_text2 = "интересуется уже, секс-игрушками!"

            if whoring >= 18 and whoring <= 23: #7
                $ rndm_one_of_three = renpy.random.randint(1, 3)
                if rndm_one_of_three == 1:
                    $ guide_add_tip = False #False=Fact
                    $ guide_tip_text = "Образовательные Журналы? К черту их!"
                    $ guide_tip_text2 = "Кому они нужны!"
                elif rndm_one_of_three == 2:
                    $ guide_add_tip = True
                    $ guide_tip_text = "Я слышал, что есть новый плакат Крама"
                    $ guide_tip_text2 = "в магазине!"
                    $ guide_tip_text3 = "Гермиона будет целовать твои ноги,"
                    $ guide_tip_text4 = "если ты для нее, его купишь!"
                elif rndm_one_of_three == 3:
                    $ guide_add_tip = True
                    $ guide_tip_text = "Она сейчас очень любит секс."
                    $ guide_tip_text2 = "Ты действительно хорошо поработал!"
                    $ guide_tip_text3 = "Все равно ты облажался, а она"
                    $ guide_tip_text4 = "злится на тебя! Может, купишь ей что-нибудь!"



    else:
        
        

        ## Funny Tips ##
        if daily_rndm_tip_or_fact ==  0:                                     #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Никогда не щекочите спящего дракона."

        if daily_rndm_tip_or_fact ==  1:                                     #Max Characters
            $ guide_add_tip = False #False=Fact
            $ guide_tip_text = "Книга 3 всегда будет лучшей!"

        if daily_rndm_tip_or_fact ==  2:                                     #Max Characters
            $ guide_add_tip = False #False=Fact
            $ guide_tip_text = "Не волнуйся, директор, Снейп не собирается"
            $ guide_tip_text2 = " убивать тебя."
            $ guide_tip_text3 = "Разные сроки!"

        if daily_rndm_tip_or_fact ==  3:                                     #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Не ходите в запретный лес в одиночку!"
            $ guide_tip_text2 = "Есть существа, которые живут там,"
            $ guide_tip_text3 = " таких, которых вы никогда раньше "
            $ guide_tip_text4 = "не видели. Их называют автомобилями!"

        if daily_rndm_tip_or_fact ==  4:                                     #Max Characters
            $ guide_add_tip = False #False=Fact
            $ guide_tip_text = "Ковры-самолеты были удобным способом для,"
            $ guide_tip_text2 = "волшебных путешествий. Теперь это метлы."
            $ guide_tip_text3 = "Какой настоящий волшебник захочет сидеть на метле?"
            $ guide_tip_text4 = "По крайней мере ковры не повредят твою промежность!"

        if daily_rndm_tip_or_fact ==  5:                                     #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Маленькая звездочка в левом верхнем углу"
            $ guide_tip_text2 = "экрана открывает руководство для игрока!... "
            $ guide_tip_text3 = "О, ты уже это знал?"
            $ guide_tip_text4 = "Ну, не забывай тогда!"

        if daily_rndm_tip_or_fact ==  6:                                     #Max Characters
            $ guide_add_tip = False
            $ guide_tip_text = "Это плохая идея, использовать непростительное "
            $ guide_tip_text2 = "Черт! В то время, как Imperius Curse могло"
            $ guide_tip_text3 = "иметь некоторую полезность для тебя, но, к сожалению,"
            $ guide_tip_text4 = "придется развращать Гермиону по-старому!"

        if daily_rndm_tip_or_fact ==  7:                                     #Max Characters
            $ guide_add_tip = False
            $ guide_tip_text = "Мы заметили, что вы используете Ad-Block!"
            $ guide_tip_text2 = "Пожалуйста, отключите Ad-Block"
            $ guide_tip_text3 = "Поддержите этот квест-путеводитель! Спасибо."

        if daily_rndm_tip_or_fact ==  8:                                     #Max Characters
            $ guide_add_tip = False
            $ guide_tip_text = "Очевидно, Дамблдор пидарас."
            $ guide_tip_text2 = "Не то, чтобы я против этого,"
            $ guide_tip_text3 = "У меня просто не хватает полезных фактов."

        if daily_rndm_tip_or_fact ==  9:                                     #Max Characters
            $ guide_add_tip = False
            $ guide_tip_text = "Вы можете поддержать нас на Patreon!"
            $ guide_tip_text2 = "Вы можете найти нас ..."

        if daily_rndm_tip_or_fact ==  10:                                    #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Поддержать Или нет."
            $ guide_tip_text2 = "Выбор за вами!"


        ## Helpful Tips ##
        if daily_rndm_tip_or_fact ==  11:                                    #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Дождливый или пасмурный день?"
            $ guide_tip_text2 = "Читай книгу!"
            $ guide_tip_text3 = "Капризная погода поможет тебе сосредоточиться,"
            $ guide_tip_text4 = "и быть более продуктивным!"
        if daily_rndm_tip_or_fact ==  12:                                    #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Дождливый или пасмурный день?"
            $ guide_tip_text2 = "Лучшая погода, чтобы написать несколько"
            $ guide_tip_text3 = "отчетов! Капризная погода поможет "
            $ guide_tip_text4 = "тебе сосредоточиться, и быть более продуктивным!"
        if daily_rndm_tip_or_fact ==  13:                                    #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Включи камин во время дождя!"
            $ guide_tip_text2 = "Комфорт от света и тепла, пламени огня, греет и позволяет"
            $ guide_tip_text3 = "читать быстрее и писать больше!"
        if daily_rndm_tip_or_fact ==  14:                                    #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Выпивание вина со Снейпом, не только увеличивает"
            $ guide_tip_text2 = "узы вашей крепкой дружбы, он также"
            $ guide_tip_text3 = "с большей готовностью вознаграждает Слизерин"
            $ guide_tip_text4 = "очками факультета!"
        if daily_rndm_tip_or_fact ==  15:                                    #Max Characters
            $ guide_tip_text = "Продолжай рыться в своем шкафу."
            $ guide_tip_text2 = "Никогда не узнаешь, какие полезные вещи"
            $ guide_tip_text3 = "сможешь найти, пока не попробуешь!"
        if daily_rndm_tip_or_fact ==  16:                                    #Max Characters
            $ guide_add_tip = False #False=Fact
            $ guide_tip_text = "У Дамблдора был большой выбор вина."
            $ guide_tip_text2 = "У него может остаться вино в шкафу!"

        if daily_rndm_tip_or_fact ==  17:                                    #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Если Гермиона злится на тебя, это может"
            $ guide_tip_text2 = "занять -дни-, чтобы погасить злость!"
            $ guide_tip_text3 = "Лучше просто, купи ей подарок!"

        if daily_rndm_tip_or_fact ==  18:                                    #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Если Гермиона злится на тебя, ты можешь дать ей"
            $ guide_tip_text2 = "подарки, чтобы улучшить ее настроение! "
            $ guide_tip_text3 = "В зависимости от уровня ее развращенности она будет"
            $ guide_tip_text4 = "отдавать предпочтение разным подаркам!"



    return
