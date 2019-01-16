label inn_menu:
    show bld1
    if inn_first:
        jump inn_intro
    abe "Добро пожаловать трактир Кабанья Голова"
    menu:
        "-Представить Гермиону Аберфорту-":
            m "Я представляю, тебе твою новую барменшу."
            $ robeon = True
            $ stockings = 5
            $ custom_outfit_old = 5
            call her_main("","normal","frown") 
            pause
            abe "Ну давай, девочка, сними халат."
            her "Отлично..."
            $ robeon = False
            call her_main("","normal","worriedCl") 
            pause
            hide screen hermione_main
            jump inn_menu
        "-Поговорить с Аберфортом-":
            jump inn_talk
        "-Играть в кости с Аберфортом-":
            "Еще не добавлено (но вы держитесь)."
            jump inn_menu
        "-Уйти-":
            jump return_office


label inn_intro: 
    m "Привет."
    abe "Здравствуй, профессор..."
    ">В мужском голосе есть кислый тон."
    m "Так, что вы здесь продаете?"
    abe "Что ты хочешь, Альбус?"
    m "(Альбус? Он должен звать меня профессор.)"
    m "Просто выпить."
    abe "Ты пьешь? Я никогда бы не подумал, что этот день настанет."
    m "Чего так?"
    abe "Никогда не ожидал, что мой младший брат, оторвет взгляд от своих книг достаточно надолго, чтобы прийти ко мне выпить."
    m "(Брат?)"
    m "Все бывает в первый раз."
    abe "Хмммф. А начнем тогда со Сливочного пива. А затем выпьем чего-нибудь покрепче, и ты, вероятно, отрубишься."
    ">Аферфорт наливает вам большой Штейн золотистого, пенного пива."
    ">Ты делаешь глоток. Он сладковатый на вкус и сливочной консистенции."
    m "Не так уж плохо, так сколько я тебе должен?"
    abe "Просто скажи мне, кто ты."
    m "(Дерьмо)"
    m "Что ты имеешь в виду."
    abe "Я никогда в жизни не видел, чтобы мой брат пил сливочное пиво. Либо ты не Альбус, либо я bowtruckle."
    m "Хорошо, ты поймал меня, я не Альбус."
    abe "Тогда что ты делаешь в его теле?"
    m "Я всемогущий Джинн из волшебного мира, который случайно сделал зелье, которое поменяло мое сознание и твоего брата."
    abe "...."
    abe "Звучит запутанно."
    m "И не говорите."
    abe "Так как долго это будет продолжаться?"
    m "Без понятия."
    abe "Ну, насколько я понимаю, все не так плохо."
    m "Тебе так сильно не нравится твой брат?"
    abe "Это длинная история."
    abe "А как насчет по настоящему выпить, а не эту фигню для малолеток."
    m "Конечно."
    ">Ты пьешь всю ночь напролет, в конце концов, шатаясь возвращаешься обратно в замок"
    $ inn_first = False
    jump day_start
    
label inn_talk: #Responses to Genie asking Aberforth how he's doing
if day_random <= 2:
    "бла бла бла"
    jump inn_menu
elif day_random >= 3 and day_random <= 5:
    "бла бла бла"
    jump inn_menu
elif day_random >= 6 and day_random <= 8:
    "бла бла бла"
    jump inn_menu
elif day_random >=9:
    "бла бла бла"
    jump inn_menu