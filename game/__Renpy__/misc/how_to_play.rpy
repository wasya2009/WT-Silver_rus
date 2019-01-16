label howtoplay_ht:
    $ end_u_5_pic =  "title/title3.jpg" #<---- SCREEN
    $ interface_color = "gold"
    show screen end_u_5                                             #<---- SCREEN
    play music "music/silly_fun_loop.mp3" fadein 1 fadeout 1 # LOLA'S THEME.
    if not persistent.tut: #Turns TRUE after tutorial happened once already. EVENT_01
        
        
        
        $ interface_color = "gold"
        $ lola_face = "characters/misc/lola/01.png"
        $ lola_body = "characters/misc/lola/body_01.png"
        
        $ l_things = True
        #$ l_blush = True
        $ lx = 490
        $ ly = 190
        show screen l_head
        l "Привет интернет-извращугам!"
        hide screen l_head
        a5 "Следи за языком, сучка!"
        $ l_things = False
        $ lola_face = "characters/misc/lola/02.png"
        show screen l_head
        l "Хах...?"
        hide screen l_head
        a6 "Что я тебе говорил о слове на букву \"и\"?"
        $ l_question = True
        $ lola_face = "characters/misc/lola/03.png"
        show screen l_head
        l "Эм... Использовать его как можно чаще..?"
        hide screen l_head
        pause.01
        with hpunch
        a7 "{size=+7}Неверно!{/size}"
        $ l_question = False
        $ l_drop = True
        $ lola_face = "characters/misc/lola/04.png"
        show screen l_head
        l "Гх!"
        hide screen l_head
        pause.01
        with hpunch
        a7 "{size=+7}Мы не используем его! Никогда!{/size}"
        $ lola_face = "characters/misc/lola/01.png"
        $ l_drop = False
        show screen l_head
        l "Потому что папочка, самый большой \nизвращенец?"
        hide screen l_head
        a6 "Гх!"
        a6 "Тебе понравилось сниматься в \"Тренере Принцесс\"?"
        $ l_hearts = True
        $ lola_face = "characters/misc/lola/01.png"
        show screen l_head
        l "Это самое лучшее событие в моей жизни!"
        hide screen l_head
        a1 "Хочешь попасть в \"gold edition\"?"
        $ l_hearts = False
        $ lola_face = "characters/misc/lola/05.png"
        show screen l_head
        l "!!!"
        $ lola_face = "characters/misc/lola/06.png"
        show screen l_head
        l "Дамы и господа, добро пожаловать в \nрежим обучения \"Тренер Ведьм\"."
        hide screen l_head
        a1 "Умница, девочка."
        $ l_drop = True
    else: # EVENT_02
        $ lx = 490
        $ ly = 190
        $ lola_body = "characters/misc/lola/body_01.png"
        $ lola_face = "characters/misc/lola/05.png"
        show screen l_head
        l "Хм...?"
        l "Ты хочешь прослушать обучение снова?"
        $ lola_face = "characters/misc/lola/09.png"
        l "Хм...."
        $ lola_face = "characters/misc/lola/11.png"
        l "Ты не очень сообразительный, не так ли?"
        $ lola_face = "characters/misc/lola/10.png"
        l "Хм..."
        $ l_things = True
        $ lola_face = "characters/misc/lola/08.png"
        l "*Хихикает!*"
        $ l_things = False
        $ lola_face = "characters/misc/lola/01.png"
        l "Ты хочешь, чтобы я учила тебя топлесс?"
        hide screen l_head
        $ d_flag_01 = False
        menu:
            "\"Еще бы!\"":
                $ lola_face = "characters/misc/lola/01.png"
                show screen l_head
                
                $ d_flag_01 = True
                l "Чудненько!"
                hide screen l_head
                pause.1
                show screen blkfade 
                with d3
                $ lola_body = "characters/misc/lola/body_02.png"
                $ l_blush = True
                pause.5
                hide screen blkfade
                with d7
                
                
            "\"Не интересно.\"":
                $ lola_face = "characters/misc/lola/12.png"
                show screen l_head
                l "Ты скучный..."
                $ lola_face = "characters/misc/lola/09.png"
                l "Ладно, пофиг..."

                   
    ### THE TUTORIAL ###
    play music "music/Under-the-Radar by PhobyAk.mp3" fadein 1 fadeout 1 
    $ lola_face = "characters/misc/lola/06.png"
    show screen l_head
    l "Вот краткий перечень вещей, которые стоит помнить..."
    with hpunch
    $ end_u_1_pic =  "characters/misc/lola/tut_02.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3')   
    show screen end_u_1

    l "Гермиона захочет продавать сексуальные \nуслуги в обмен на очки факультета,\nкогда Гриффиндор отстает."
    
    with hpunch
    $ end_u_1_pic =  "characters/misc/lola/tut_01.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3')   
    l "Дружба с профессором Снейпом  увеличит количество очков, зарабатываемых \nСлизерином."
    with hpunch
    $ end_u_1_pic =  "characters/misc/lola/tut_03.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3') 
    if d_flag_01: # TOPLESS.
        $ lola_face = "characters/misc/lola/07.png"
    l "Чтение образовательных книг позволит тебе зарабатывать, но это по желанию."

    with hpunch
    $ end_u_1_pic =  "characters/misc/lola/tut_04.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3') 
    l "Покупка одной и той же сексуальной услуги может привести к разным последствиям,\nв зависимости от того, как далеко \nГермиона зашла в своих тренировках."
    $ lola_face = "characters/misc/lola/06.png"

    with hpunch
    $ end_u_1_pic =  "characters/misc/lola/tut_07.png" #<---- SCREEN
    l "Все услуги разделены на две группы: \n\"приватные\" и \"публичные\" услуги."
    l "Приватные услуги оказываются в кабинете \nи не сильно влияют на репутацию Гермионы."
    l "Публичные услуги оказываются во время \nуроков за пределами экрана."
    l "Каждая публичная услуга, не считая \nпоследней, имеет девять концовок."
    l "Кстати, несмотря на то, что покупка \nприватных услуг - необходима для\nтренировки Гермионы, публичные услуги\nне обязательны."

    with hpunch
    $ end_u_1_pic =  "characters/misc/lola/tut_05.png" #<---- SCREEN

    $ renpy.play('sounds/boing02.mp3') 
    l "Плохое обращение с Гермионой ухудшит ее настроение и может сделать очень несговорчивой..."
    l "Она остынет со временем, но ты можешь \nускорить процесс, купив ей что-нибудь \nприятное..."
    
    with hpunch
    $ end_u_1_pic =  "characters/misc/lola/tut_06.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3') 
    l "Здесь нет временных ограничений, так что \nможешь играть с ней столько дней, \nсколько захочешь."
 
    
    
    
    $ end_u_1_pic =  "characters/misc/lola/tut_00.png" #<---- SCREEN
    $ l_drop = False
    
    if not persistent.tut: # FIRST TIME TUTORIAL. Turns TRUE after tutorial happened once already. EVENT_01
        $ persistent.tut = True #Turns TRUE after tutorial happened once already.
        hide screen l_head
        a1 "Ладно, этого хватит..."
        $ l_question = True
        $ lola_face = "characters/misc/lola/05.png"
        show screen l_head
        l "Как я справилась?"
        hide screen l_head
        a1 "Ты хорошо поработала. Хорошая девочка."
        $ l_question = False
        $ l_things = True
        $ lola_face = "characters/misc/lola/08.png"
        show screen l_head
        l "Хе-хе-хе. Лола хорошая девочка!"
        $ l_things = False
        $ lola_face = "characters/misc/lola/01.png"
        show screen l_head
        l "А что я получу?"
        hide screen l_head
        a1 "А что ты хочешь?"
        $ lola_face = "characters/misc/lola/10.png"
        show screen l_head
        l "Хм..."
        $ l_exclamation = True
        $ lola_face = "characters/misc/lola/01.png"
        l "Мы можем сделать сцену изнасилования n\со мной в \"Gold Edition\"?"
        hide screen l_head
        a6 "Не испытывай мое терпения, девочка."
        $ l_exclamation = False
        $ l_drop = True
        $ lola_face = "characters/misc/lola/04.png"
        show screen l_head
        l "Извини, папочка."
        $ l_drop = False
        hide screen l_head
        a5 "............"

    else: ### NOT FIRST TUTORIAL. EVENT_02
        if d_flag_01: #TOPLESS.
            hide screen l_head
            stop music fadeout 1.0
            a1 "Что здесь происходит?"
            $ lola_face = "characters/misc/lola/14.png"
            $ l_drop = True
            show screen l_head
            l "Упс!"
            hide screen l_head
            a1 "Что я говорил тебе о раздевании перед незнакомцами?"
            $ lola_face = "characters/misc/lola/04.png"
            show screen l_head
            l "Это важная часть моего развития и \nвзросления?"
            hide screen l_head
            a6 "Неверно!"
            $ l_drop = False
            $ l_tears = True
            $ lola_body = "characters/misc/lola/body_01.png"
            $ lola_face = "characters/misc/lola/04.png"
            show screen l_head
            l "Папочка, мне так жаль!"
            l "Этот случайный чувак из интернета \nзаставил меня, я клянусь!"
            hide screen l_head
            a1 "Обучение закончено."
            $ l_blush = False
            $ l_tears = False
            $ lola_face = "characters/misc/lola/15.png"
            show screen l_head
            l "Хе-хе! Попался!"
        else:
            $ lola_face = "characters/misc/lola/09.png"
            l "И, это..."
            $ lola_face = "characters/misc/lola/13.png"
            l "Может быть в следующий раз."
            $ lola_face = "characters/misc/lola/10.png"
            l "Попробуем топлесс?"
            
        
return

### ABOUT GAME ####
label abouttrainer_ht:
    $ end_u_5_pic =  "title/title3.jpg" #<---- SCREEN
    $ interface_color = "gold"
    show screen end_u_5                                             #<---- SCREEN
    play music "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3" fadein 1 fadeout 1 
    
    a1 "Хм... Посмотрим..."
    a1 "Я начал работу над \"Тренером Гермионы\" сразу после релиза \"Тренера Принцессы\"."
    a1 "У меня была идея создать маленькую милую игру, на разработку которой уйдет не больше, чем пара месяцев."
    a1 "Как мы все знаем, это заняло у меня больше полугода..."
    a1 "И несмотря на бесконечные компромиссы, мне пришлось просто-напросто закончить разработку, чтобы эта чертовщина не убила у меня еще больше времени."
    a1 "Порой работать над игрой было весело..."
    a1 "Но также были и трудности..."
    a1 "Иногда мне приходилось бороться с некотрыми идеями и игровыми механиками, которые не хотели работать правильно..."
    a1 "Также работа над этой игрой рассказала мне много о моих способностях как разработчик игр и моих слабостях."
    a2 "Мне почти кажется, что я должен получить медаль или грамоту за это."
    a1 "Ладно, я сваливаю в мой следующий проект. {size=-4}(\"Тренер Принцессы Золотое Издание\"){/size}"
    a1 "Спасибо за поддержку, парни. И я надеюсь, что эта игра сделала ваши будни хоть чуточку светлее."
    a2 "До следующего раза..."

    return

## О переводчиках
label devel:

    $ end_u_5_pic =  "title/title3.jpg"
    $ interface_color = "gold"
    
    show screen end_u_5                                             
    play music "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3" fadein 1 fadeout 1

    dev "{size=-4}Итак, вы уже обратили внимание, что это не оригинальная игра Акабура и уж тем более не версия 1.6f, в определенный кругах именуемая \"Russian Edition\" от команды Sad Crab...{/size}"
    menu:
        "Что???":
            dev "(facepalm)"
            dev "Я так и знал..."

        "Это же шутка ?":
            dev "..........."

        "А разве ты не Акабур ?":
            dev "В рот мне ноги..."

        "А разве 1.6f, делал не Акабур?":
            dev "Не-а, ее делали SadCrab team, которые нынче делают свою игру по вселенной Гарри Поттера."

        "А эту игру тогда, кто делает?":
            dev "MoCoder-Silver Game Studios"
            
    dev "{size=+3}Т.е. вы все по-прежнему считаете, что игру для вас продолжает делать Акабур?{/size}"

    dev "И это после того, как Акабур сообщил, что считает игру законченной?"

    dev "После того, как он решил никогда ее не переводить на русский? Интересно почему же без русского языка..."

    dev "И это после того, как Sad Crab сообщили, что считают свою модификацию 1.6f законченной? С недоделанной газетой..."

    dev "{size=+4}Аргх...{/size}"

    dev "......."

    dev "Простите, наболело."
    
    dev "Для вас над игрой трудилась команда \"Silver Game Studio\"."

    dev "А перевела ее для вас команда \"Red Machine\"."

    dev "Признаем, частично мы воспользовались переводом SadCrab team,- самую малость. Частично придумывали перевод сами, а частично оставили как есть."

    dev "Мы тоже человеки и где-то могли оставить непереведенные слова и фразы."
    dev "Что мы точно не переводили и вероятно не будем: \nЗаклинания \nИгредиенты зелий(не все-опционально)"

    dev "Некоторые слова, которые в переводе звучат жутко или плохо, но мы над ними еще поработаем."

    dev "Обо всех ошибках как орфографических, так и игрового кода этой локализованной игры, сообщите нам на {a=https://discord.gg/XasMKVc}Дискорд{/a} или в паблике в {a=https://vk.com/translators_rem}ВК{/a}"

    dev "А теперь подробнее о нашей команде с никнеймами, взятыми с дискорд-канала."

    dev "wasya2009 (перевод,редактирование,графика) - глава проекта по переводу, сперва пытался переводить в одну каску ;)."

    dev "администратор дискорд канала и по совместительству самый главный {w}лентяй!"

    dev "Copycat (перевод) - Помогала переводить игру на раннем этапе, фактически первый присоединившийся помошник,"

    dev "но в силу своих житейских проблем, не смогла продолжить над ним работу (P.S. Ух лентяка :>)."

    dev "RuGamerPRO (перевод,редактирование) - Присоединился к проекту случайно, решив посмотреть переведенные фразы на ошибки."

    dev "Затянулся в азарте, чем фактически и вдохнул в проект вторую жизнь и ускорил над ним работу."

    dev "Wentseeking (перевод,редактирование,графика) - присоединился к переводу, когда он зажил с новой силой."

    dev "lilpeep (перевод,редактирование) - выкраивал время, между домашними заданиями."

    dev "Heresy. А в определенных кругах, известный как NwNIHeretic (перевод) - по определенным непоняткам с обоих сторон,"

    dev "устроили с ним перепалку на одном сайте, после чего, помошников с переводом прибавилось."

    dev "palad1n (перевод) - внес и свои 5 копеек в перевод :З ."

    dev "Satna (перевод) - помогал переводить..."

    dev "DEAD_RaSe (перевод,редактирование) - присоединился, когда основная масса текстов уже была переведена,"

    dev "но тем не менее, тоже внес свой посильный вклад в работу над переводом."

    dev "KimseyGrowly (редактор) - присоединилась, на заключительном этапе и помогала редактировать фразы перевода."

    dev "На момент написания этих строк, во всю трудится. Как будет через пару дней - поживем увидим. Не перегорит ли у нее фитилек :З ."

    dev "zadroticus wise (ниасилил) - настойчиво стучался в личку, с просьбой практически переходящей в требование, дать ссылку на дискорд-канал и"

    dev "огроменным желанием помочь в переводе. Но жизненные обстоятельства сложились иначе. А после и просто в текст перегорел."

    dev "А с моего ракурса просто послал нас... {w} переводить,{w} пока сам рубился в РОБЛОКИ и другие игрушки... Но я же человек, поэтому могу и ошибаться."

    dev "ХоккеисТ (нишмагла) - постучался в дискорде, предложил помощь... А так, как я (плохой администратор) и плохо помнил, кто чего делает."

    dev " Предложил ему редактировать текст, и после, мы этого человека не видели... Даже думали, может файл несчастливый,"

    dev "от него люди пропадают {w}и долго его сами не редактировали."

    dev "Торин (я по прежнему был плохой руководитель см. пред.) - постучался в дискорде, файлы я не помнил, какие были свободны на перевод."

    dev "Предложил редактирование, на что получил его радостное одобрение."

    dev "Через три дня он скинул макет своих правок, был вроде немного поправлен {w}(отчитан, с его колокольни), ну да... кому понравится,"

    dev "Чтобы тебя отчитывали по {w}пустяку... :З Пропал на неделю и забил."

    dev "Вроде бы на этом все... всех, кто хоть чем-то помог, потратил сколько-то своего личного времени или сделали вид об этом - нашли здесь о себе пару строк."

    dev "Итак, приятной игры, друзья !"

    dev "А если хотите пообщаться с людьми, которые перевели эту игру, милости просим. {a=https://discord.gg/XasMKVc}НАШ ДИСКОРД-КАНАЛ{/a}"


return

label forum:

    $ end_u_5_pic =  "title/title3.jpg"
    $ interface_color = "gold"
    
    show screen end_u_5                                             

    dev "Итак, перед вами модификация игры, которая развивается независимо (от Акабура) командой разработчиков."

    dev "Добро пожаловать на {a=https://www.patreon.com/MoCoder}Патреон{/a} разработчиков англоязычной версии."

    dev "А вот наш {a=https://www.patreon.com/REdMachineteam}Патреон{/a}- Переводчиков этой игры. Так же у нас есть {a=https://discord.gg/XasMKVc}ДИСКОРД{/a} канал и группа во {a=https://vk.com/translators_rem}ВКонтакте{/a}."

return

label donate:

    $ end_u_5_pic =  "title/title3.jpg"
    $ interface_color = "gold"
    
    show screen end_u_5                                             

    dev "{size=-4}А спонсором данного перевода, выступил... {w}не магазин лутбоксов :) ...{w} а уйма убитого свободного времени примерно 12 человек...{/size}"

    dev "{size=-4}За время перевода файлов, у нас были жертвы и потери... Один учащийся общеобразовательного учреждения, не смог сопротивлятся животному инстинкту...{/size}"

    dev "{size=-4}От чего сорвался, и придумал отмазку в стиле мне надо к ЭГЕ готовиться, переводите без меня.{/size}"

    dev "Главный лентяй т.е. Я - сотый раз, забрызгал весь унитаз, сами понимаете чем... ;)"

    dev "А сколько раз срывались, остальные переводчики и редакторы - они не говорят..."

    dev "но у некоторых из них, жены и девушки, последний месяц ходят, со счастливыми лицами..."

    dev "{size=-4}На одном сайте настояли, что за подобный перевод игры, игроки, могут материально поощрить, поэтому...{/size}"

    dev "Вы можете отблагодарить нас - \"je ne mange pas six jours\","

    dev "{size=-4}пожертвовав некую сумму денег. это сугубо добровольно и необязательно, наш перевод {color=#19FF00}Асболютли фривейр!{/color}{/size}"

    dev "{size=-4}Но это подстегнет нас взяться за перевод обновления к игре, или же взятся за перевод какой-нибудь другой интересной игры. {a=https://www.patreon.com/REdMachineteam}Наш Патреон{/a}{/size}"

    dev "{size=-4}Здесь должны быть наши реквизиты, но мы такие занятые (не... скорее ленивые), что их просто пока не зарегистрировали,{/size}"

    dev "но можете зайти к нам в {a=https://discord.gg/XasMKVc}дискорд{/a}, и связаться с администрацией канала."

    dev "Видимо, нам и Яндекс Деньги лень регистрировать ;)"

    dev "А Qiwi-кошелек, уж тем более..."

    dev "У вас есть возможность помочь проекту."

    dev "Мы обязательно будем развивать его изо всех сил в любом случае, но найм дополнительных девок..."

    dev "Эээээээ. Художников. Найм художников очень поможет делу."

    dev "Спасибо за внимание."

return


### F.A.Q. ###
label faq_ht:
    $ end_u_5_pic =  "title/title3.jpg" #<---- SCREEN
    $ interface_color = "gold"
    show screen end_u_5 
    with flashbb#<---- SCREEN
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 
    
    a1 "Привет. Меня зовут Акабур. Я ненавижу русскоязычных игроков, и одновременно являюсь создателем игры. Я здесь, чтобы ответить на твои вопросы." 
label faq_ht2:    
    menu:
        "Как я могу поддержать тебя?":
            a1 "Ну, есть несколько способов..."  
            a1 "Самый простой способов написать мне (akaburfake2@yahoo.com) и дать мне знать, что тебе понравилась игра."
            a1 "Также ты можешь поддержать меня лично на - ссылок не будет!"
            a1 "Еще один способ поддержать меня это перейти по этой ссылке:ссылок не будет!"
            a1 "У таких независимых художников как я, каждый бакс на счету..."
            a6 "Серьезно. Из-за моего стиля жизни, гребанный банк все еще не может выдать мне кредитную карту..."
            jump faq_ht2
            
        "Как оставаться в курсе?":
            a1 "Ну, перейти по этой ссылке: {a=http://akabur.hentaiunited.com}akabur.hentaiunited.com{/a} и подписаться. Или посетить мой сайт: {a=http://akabur.com}akabur.com{/a}."
            a1 "Еще, конечно есть Patreon {a=http://www.patreon.com/akabur}www.patreon.com/akabur{/a}.\nи {a=https://twitter.com/AKABUR}мой twitter{/a}."
            jump faq_ht2
        "У меня есть другой вопрос.":
            a1 "Если у тебя есть вопрос, что не входит в этот \"F.A.Q.\", не стесняйся и пиши: akaburfake2@yahoo.com"
            a1 "Или оставь вопрос здесь: {a=http://ask.fm/AKABUR}ask.fm/AKABUR{/a}"
            jump faq_ht2
        "Я хочу сообщить о баге/ошибке.":
            a1 "Эта игра тестировалась много много много раз, но лучшими тестерами всегда были и остаются игроки."
            a1 "Так что, если вы встретили баг - пишите мне (akaburfake2@yahoo.com) и я НЕисправлю проблему в следущей версии игры."
            jump faq_ht2
        "Кто помог тебе создавать игру?":
            a1 "Никто не помогал мне! Я сделал все сам!"
            a1 "Я сам написал все скрипты, нарисовал все арты, и сыграл всю музыку!"
            a7 "Я! {size=+3}Я! {size=+3}Я создал все! {size=+3}Я!{/size}"
            a2 "Хех..."
            a1 "Ну, по правде, я сделал большую часть работы. Но мне много помогали."
            a1 "Мой друг и коллега Dahr обеспечил меня благородно (и бесплатно) разными художествами (помимо всего прочего)."
            a1 "Не бойтись кинуть парню монетки или две на {a=http://www.patreon.com/DAHR}www.patreon.com/DAHR{/a}"
            a1 "Xaljio всегда был рядом, когда у меня были проблемы с коддингом. (частенько). Посетите его страничку - {a=http://www.patreon.com/xaljio}www.patreon.com/xaljio{/a}"
            a1 "И, конечно, сообщества на patreon и hentaiunited. Парни, вы шикарны."
            a1 "Спасибо вам за моральную и финансовую поддержку разработки этой игры. Вы, ребята, делаете этот мир чуточку лучше."
            jump faq_ht2
        "Можно взломать и перевести эту игру?":
            a1 "..."
            a1 "..."
            a5 "Нет, но Red Machine и Silver Studio - {b}можно!{/b}."
            define nyor = Character('Ибунхотеп', color="#9F42AB")
            nyor "Странный вопрос, не находишь?"
            nyor "И это после того, как я три гребанных часа, возился, чтобы перевести никому не нужные FAQ и обучалки!"
            nyor "Агрх!"
            nyor "А вообще, молодец, что заглянул."
            nyor "Минута славы."
            nyor "Перевод для вас пилил/и
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=23721488}wasya2009{/a}"

            nyor "Кого добавить в этот список, пишите в дискорде или в лс, на порнолабе"
            nyor "Извините, если кого-то забыл/и :3!"
            nyor "Не забывайте пользоваться салфетками, ребята, пока-пока!"
            a1 "..."
            jump faq_ht2

        "Неважно. Выпусти меня отсюда!":
            return

    
    return