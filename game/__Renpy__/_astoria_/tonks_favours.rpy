
label astoria_tonks_event: #send astoria to go see tonks

    $ spells_locked = False
    $ tonks_busy = True
    $ astoria_tonks_event_in_progress = False
    if astoria_tonks_3_completed and not astoria_wardrobe_unlocked: #Unlocks Astoria's Wardrobe.
        jump astoria_tonks_wardrobe_unlock

    if astoria_affection == 1 and not astoria_tonks_1_completed:
        jump astoria_tonks_1
    elif astoria_affection == 2 and not astoria_tonks_2_completed:
        jump astoria_tonks_2
    elif astoria_affection == 3 and not astoria_tonks_3_completed:
        jump astoria_tonks_3
    else: #Repeatable events.
        jump astoria_tonks_random


### TONKS EVENTS ###
label astoria_tonks_1: #First time astoria sent to tonks.
    call play_music("fun")
    call play_sound("door")
    call ast_main("","smile","base","base","mid",xpos="right",ypos="base")
    pause.5
    call nar(">Твоя дверь широко распахнулась, когда вошла Астория.")

    m "О, ты вернулась!"
    call ast_main("Вы удивлены, [ast_genie_name]?","smile","base","base","mid")
    m "Немного... (Она кажется немного странной)."
    call ast_main("Тогда зачем ты отправил меня туда?!","open","base","worried","R")
    m "Эм..."
    call ast_main("...","pout","narrow","narrow","mid")
    call ast_main("Ну это не так уж плохо...","open","base","base","mid")
    call ast_main("Она всего лишь хотела задать несколько вопросов.","upset","base","base","R")
    m "Какого рода вопросы?"
    call ast_main("Мои любимые предметы, что мне нравится, сколько мне лет, и все в таком духе.","open","base","base","down")
    m "И это все? Она не просила тебя сделать что-нибудь странное?"
    call ast_main("На самом деле, нет...","pout","base","base","R")
    call ast_main("Хотя у нее был такой взгляд в глазах... Как будто она хотела съесть меня...","open","narrow","worried","mid")
    call ast_main("Она ведь не оборотень, [ast_genie_name]?","open","wide","wide","wide")
    m "Срань господня! Здесь настоящие оборотни?"
    call ast_main("Что вы имеете в виду под, здесь? Конечно, оборотни реальны... Мы все учимся этому в детстве.","open","closed","base","mid")
    m "Просто проверка..."
    m "Ой, и я уверен, что она не оборотень..."
    m "(Я надеюсь...)"
    call ast_main("Лучше бы ей им не быть, [ast_genie_name]!","disgust","base","worried","down")
    m "Уверен, ты к ней привыкнешь."
    call ast_main("Привыкнуть к ней????","open","wide","wide","mid")
    call ast_main("Мне не нужно ее снова видеть?","disgust","base","worried","down")
    m "Ну... Если хочешь продолжать изучать новые заклинания, тебе придется..."
    call ast_main("*хм* Вы еще ничему меня не научили!","clench","angry","angry","mid")
    call ast_main("Они, наверное, даже скучные...","pout","angry","angry","R")
    m "Почему бы тебе тогда не подойти сюда, и мы начнем первое занятие."
    call ast_main("Хорошо...","grin","base","base","mid")

    $ astoria_tonks_1_completed = True

    jump astoria_requests


label astoria_tonks_2:
    call play_music("fun")
    call play_sound("door")
    call ast_main("","clench","angry","angry","mid",xpos="right",ypos="base")
    pause.5

    call nar(">Астория входит в твой кабинет, угрюмый взгляд нарисован на ее лице.")
    m "Как прошл--"
    call ast_main("Ужасно!","open","closed","angry","mid")
    call ast_main("Эта Тонкс настоящая уродина, [ast_genie_name]!","pout","base","worried","down")
    m "Правда? Что она сделала?"
    call ast_main("Она назвала мою униформу консервативной!","disgust","narrow","base","down")
    call ast_main("Как у униформы могут быть политические убеждения?","pout","base","base","R")
    call ast_main("Не говоря уже о консервативных!","open","base","worried","down")
    call ast_main("Она, наверное, одна из тех психов, которые жалуются на--","pout","angry","angry","L")
    m "Это не то, что означает консервативный."
    call ast_main("Так все и есть! Я чита--","scream","closed","base","mid")
    m "Это значит, что она думает, что твоя форма скрывает слишком много кожи..."
    call ast_main("О...","clench","narrow","narrow","down")
    call ast_main("Правда?","disgust","base","base","mid")
    call ast_main("Думаю, это объяснило бы размерную ленту...","open","base","base","L")
    m "Почему бы тебе не рассказать мне, что случилось с самого начала?"
    call ast_main("Хорошо...","upset","narrow","narrow","mid")
    call ast_main("Ну, сначала мы добрались до ее кабинета.","open","base","base","mid")
    call ast_main("Мы просто немного поболтали.","open","base","base","R")
    call ast_main("О конфетах, домашних животных, школьных вещах, и если есть, мальчики, которые мне нравятся...","worried","base","base","mid")
    call ast_main("Она даже показала мне секретный проход отсюда до кухонь, о которых я даже не знала!","grin","angry","angry","mid")
    call ast_main("В любом случае, когда мы добрались туда, Джинни Уизли внезапно выскочила из кабинета!","upset","base","worried","down")
    m "(Джинни Уизли? Я не слышал это имя раньше?)"
    m "(Это лесбиянка подруга Грейнджер? Я не могу вспомнить...)"
    call ast_main("Ее лицо было все красное, и она не хотела смотреть на меня...","worried","base","base","down")
    call ast_main("Я подумал, что она, вероятно, попала в неприятности из-за чего-то, поэтому я ничего не сказала...","open","base","base","R")
    call ast_main("Как только мы оказались внутри, она спросила, какое заклинание я наложу на этот раз...","upset","base","base","down")
    call ast_main("И на кого я его накладываю...","open","base","base","R")
    call ast_main("Но я не думаю, что она была очень заинтересована...","smile","base","base","down")
    call ast_main("Она была в восторге от моей униформы.","upset","base","base","mid")
    call ast_main("Она только, что узнала, как учителю ей разрешено выбирать форму, для своих учеников.","pout","angry","angry","R")
    m "(Мы можем это делать?... Эта Грейнджер солгала мне?!!)"
    call ast_main("И что она хотела внести некоторые изменения в мою униформу, потому что она была слишком консервативна!","upset","ahegao","ahegao","ahegao")
    call ast_main("Я сказал ей, что не связываюсь ни с одной политической партией, и убежала оттуда!","scream","angry","angry","R")
    call ast_main("Но если она имела в виду, что мой жилет слишком плотный, думаю, это не так уж плохо...","disgust","narrow","narrow","down")
    m "(Я уверен, что она это имела в виду...)"
    call ast_main("Мне обязательно туда возвращаться, сэр?","upset","base","worried","mid")
    m "Только если ты хочешь продолжать использовать новые заклинания..."
    call ast_main("Тьфу...","disgust","ahegao","ahegao","ahegao")
    call ast_main("Отлично...","pout","angry","angry","L")
    call ast_main("Просто убедиться, что она не лезет в политику!","pout","angry","angry","mid")
    m "Сделай это..."
    call ast_main("Хорошо! Теперь о новых заклинаниях...","pout","base","base","R")
    m "Мы можем начать читать сейчас, если хочешь."
    call ast_main("Уау!","grin","happyCl","base","mid")

    $ astoria_tonks_2_completed = True

    jump astoria_requests


label astoria_tonks_3:
    call play_music("fun")
    call play_sound("door")
    call ast_main("","smile","base","base","mid",xpos="right",ypos="base")
    pause.5

    call nar(">Астория радостно входит в твой кабинет, напевая мелодию и закрывая дверь.")
    call ast_main("Эй, [ast_genie_name]!","grin","happyCl","base","mid")
    m "Привет, [astoria_name]... Ты выглядишь бодрой сегодня."
    call ast_main("Угадайте, что?","grin","angry","angry","mid")
    m "Что это?"
    call ast_main("Тонкс хочет, чтобы я была моделью!","smile","angry","angry","down",cheeks="blush")
    m "Моделью?"
    call ast_main("Ага! Вы знали, что она на самом деле дизайнер костюмов в свободное время?","open","base","base","mid")
    m "Нет, не знал..."
    call ast_main("Так и есть! И она думает, что у меня есть все, чтобы стать моделью!","grin","angry","angry","mid")
    m "Правда..."
    call ast_main("Ага! Она даже провела весь день, снимая мои мерки, чтобы начать работать над некоторыми специальными нарядами для меня!","grin","happyCl","base","mid")
    call ast_main("Плюс она даже сказала, что начнет работать над новой, более крутой версией моей формы!","smile","base","base","mid")
    m "Ха..."
    call ast_main("Разве это не замечательно, сэр?","grin","happyCl","base","mid")
    m "Конечно."
    call ast_main("И подумать только, я думала, что она сделает что-нибудь гадкое...","open","base","base","R")
    m "Я бы не стал пока оставлять это в прошлом..."
    call ast_main("Пфф, кто бы говорил старик!","pout","angry","angry","mid")
    call ast_main("Бьюсь об заклад, ты весь день думал о том, что мы будем делать со Сьюзан в следующий раз, не так ли?","grin","angry","angry","mid")
    m "Эта мысль могла прийти мне в голову..."
    call ast_main("Ну, если вы хотите добраться до этого, мы должны сначала изучить новое заклинание, [ast_genie_name]!","open","base","base","L")
    call ast_main("Кстати говоря...","worried","base","base","R")

    $ astoria_tonks_3_completed = True

    jump astoria_requests


label astoria_tonks_wardrobe_unlock:
    #call play_music("fun")
    call play_sound("door")
    call ast_main("","upset","closed","base","mid",xpos="right",ypos="base")
    pause.5

    call nar(">Астория вошла в твой кабинет, надменно морща нос.")

    m "С возвращением, [astoria_name]. Как прошл--"
    call ast_main("Без лишних слов, [ast_genie_name]! У меня на это совершенно нет времени!","clench","closed","base","mid")
    call ast_main("Тонкс сказала, что вы можете помочь мне, с работой моделью!","open","base","base","mid")
    m "Она так сказала? Как я должен тебе помочь?"
    call ast_main("Она сделала мне новые классные наряды, которые она хочет, чтобы я надела.","open","base","base","down")
    call ast_main("Я еще не примеряла их, поэтому я не знаю, подойдут ли они мне вообще.... Они выглядят очень маленькими...","disgust","closed","worried","down")
    call ast_main("Все просто, я примерю их и посмотрю, как они мне подойдут...","open","base","base","down")
    call ast_main("Все, что вам нужно сделать, это сидеть и говорить мне, как здорово я выгляжу!","open","closed","base","mid")
    call ast_main("Как вы думаете, сможете справится с этим, [ast_genie_name]?","upset","narrow","narrow","mid")
    m "Я постараюсь..."
    call ast_main("Отлично! Теперь давайте начнем!","grin","angry","angry","mid")

    call give_reward(">Поздравляю! Теперь ты можешь получить доступ к гардеробу Астории и изменять ее внешний вид!","images/store/astoria_unlock_02.png")

    call give_reward(">Поздравляю! Шкаф Сьюзан также был разблокирован!","images/store/susan_unlock_02.png")

    "Примечание разработчика:" ">Сьюзан и гардероб Астории станет доступен.\nВся доступная одежда также была разблокирована."
    "Примечание разработчика:" ">Гардероб Сьюзан, а также одежда Астории откроются с будущими событиями, а не в более поздних патчах."

    "Примечание разработчика (Мерлина):" ">Это знаменует конец нынешнему контенту Астории и Сьюзан! Надеемся, вам понравилось!"

    $ astoria_wardrobe_unlocked = True
    $ susan_wardrobe_unlocked = True

    $ active_girl = "astoria"

    call load_astoria_clothing_saves

    call reset_wardrobe_vars
    call update_wr_color_list

    $ wardrobe_active = 1 #True
    call ast_main(xpos="wardrobe",ypos="base")
    call screen wardrobe

label astoria_tonks_4:

label astoria_tonks_5:

label astoria_tonks_6:






### REPEATABLE RANDOM EVENTS ###
label astoria_tonks_random:
    $ random_number = renpy.random.randint(1, 3)

    #Tonks is into beast stuff?!
    if random_number == 1:
        #call play_music("fun")
        call play_sound("door")
        call ast_main("","pout","base","base","R",xpos="right",ypos="base")
        pause.5

        call nar(">Астория небрежно входит в твой кабинет, бездумно оглядываясь.")
        m "Хорошо, как все прошло?"
        call ast_main("Ничего особенного, [ast_genie_name].","pout","base","base","L")
        call ast_main("Мы в основном пили чай и разговаривали...","pout","base","base","R")
        call ast_main("На ее полке была книга, которая привлекла мое внимание, и я хотела ее почитать...","open","base","base","mid")
        call ast_main("Я думаю, это было названо Бестиарием или Скотством или чем-то еще...","open","narrow","narrow","R")
        call ast_main("Она не позволила мне прочитать его... Интересно, почему...","pout","base","base","down")
        m "(...)"
        m "Хочешь, наложить несколько заклинаний, [astoria_name]?"
        call ast_main("Конечно, [ast_genie_name]!","grin","base","base","down")

    #Tonks is the best!
    if random_number == 2:
        call play_music("fun")
        call play_sound("door")
        call ast_main("","grin","base","base","mid",xpos="right",ypos="base")
        pause.5

        call nar(">Астория весело входит в твой кабинет, напевая мелодию, когда закрывает дверь.")
        m "Так... Как прошел твой день?"
        call ast_main("Это было потрясающе, [ast_genie_name]!!!","scream","wide","wide","wide")
        call ast_main("Тонкс показала мне свою книгу существ! Все магические существа, с которыми она столкнулась за годы службы Мракоборцем!","open","base","base","mid")
        call ast_main("Гигант, оборотень, даже вампир!","grin","angry","angry","mid")
        call ast_main("Она оооочень классная, [ast_genie_name]! Лучший учитель для нас в этой дурацкой школе!","grin","happyCl","base","mid")
        m "Я рад это слышать."
        m "Хотите наложить несколько заклинаний?"
        call ast_main("Хихихи-- конечно!","grin","base","base","mid")

    #Tonks sucks!
    if random_number == 3:
        #call play_music("fun")
        call play_sound("door")
        call ast_main("","pout","angry","angry","R",xpos="right",ypos="base")
        pause.8

        call ast_main("Я ненавижу ее, [ast_genie_name]!","scream","closed","angry","mid")
        m "Тонкс? В прошлый раз ты сказала, что любишь ее..."
        call ast_main("Это было до того, как она попросила, чтобы я убрала весь ее кабинет!","scream","angry","angry","mid")
        call ast_main("Не говоря уже об ужасном наряде, который она заставила меня надеть.","clench","angry","angry","R")
        m "Подожди, какой наряд?"
        call ast_main("Думаю, она назвала это девичьим нарядом или как-то так.","pout","angry","angry","L")
        call ast_main("Я выглядела такой глупой в нем...","pout","angry","angry","down")
        if astoria_tonks_3_completed:
            call ast_main("Она сказала, что если я действительно хочу быть моделью, мне нужно носить все, что мне говорят.","open","closed","base","mid")
            call ast_main("Даже если это означает ничего не носить, [ast_genie_name]! Вы можете в это поверить?!","scream","wide","wide","wide")
        m "Хм..."
        g9 "Я бы тоже хотел увидеть тебя в этом наряде!"
        call ast_main("Без шансов!","clench","angry","angry","mid")
        call ast_main("Спокойной ночи [ast_genie_name]!","open","closed","base","mid")
        m "Подожди, ты не хочешь--"
        hide screen astoria_main
        with d3
        pause.5

        call nar("Астория быстро выпрыгивает из твоего кабинета.")

        $ astoria_busy = True

        call play_music("night_theme")
        jump night_main_menu

    #ADD more random Tonks events.

    jump astoria_requests



