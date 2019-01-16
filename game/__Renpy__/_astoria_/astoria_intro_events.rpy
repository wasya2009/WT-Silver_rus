#LETTER FROM THE MINISTRY OF MAGIC
#Dear Albus Dubmbledore, as we are sure you are aware,
#an unforgivable curse has been detected within the grounds of Hogwarts.
#While the punishment for such a curse is usually lifetime incarceration in the
#prison, Azkaban, we are allowing you to address this matter at your own discretion.
#This is due to the possible nature of the spell being cast by a minor who has not
#fully grasped the serious nature of the curse. If this is the case we expect no further communication from
#you regarding this unfortunate event. If, however, you believe the curse has been cast by someone other than a student,
#or if any other complications arise we expect direct communication. Lastly, the detection of any further curses will
#result in the immediate dispatchment of an auror to Hogwarts.

#Cornelius Fudge,
#Department Head: Improper Use of Magic Office

#m "That doesn't sound good..."
#m "Perhaps I should tell Snape about this."
#m "Or maybe miss granger?"


#TELL HERMIONE ABOUT THE LETTER #Done
label letter_intro_hermione:
    m "Я недавно, получил письмо."
    call her_main("Оно из Министерства магии, не так ли?!","shock","wide") #No xpos change.
    call her_main("Они пронюхали о моих темных делишках? Пожалуйста, не говорите мне, что они--","disgust","worriedCl")
    m "Нет, нет, письмо не о тебе..."
    m "Однако \'оно\' из Министерства магии."
    m "По-видимому, они обнаружили в школе что-то, называемое \'непростительным\' проклятием."
    call her_main("Непростительное проклятие!!!","scream","wide",trans="hpunch")
    call her_main("В нашей школе?!","shock","wide_stare")
    call her_main("КОГО-ТО МОЖЕТ УБИЛИ!","scream","wideL")
    call her_main("ИЛИ ПЫТАЛИ!!","disgust","worriedCl")
    call her_main("ИЛИ ХУЖЕ!!!","disgust","worriedL")
    m "Правда?"
    call her_main("Только из-за этих причин может образоваться непростительное проклятие, [genie_name]!","angry","worried")
    m "Конечно... Я просто хочу убедиться, знала ли ты об этом..."
    call her_main("Это первый урок, который мы получили на \"защите от темных искусств\".","open","closed")
    m "Хорошо, значит кто-то наложил проклятье где-то в школе."
    m "И мне нужна твоя помощь, чтобы выяснить, кто это сделал..."
    call her_main("Почему вам нужна моя помощь?","soft","wink")
    call her_main("Вы же в состоянии обнаружить его?","base","base")
    m "К сожалению, нет... Я, должно быть, спал... когда это случилось..."
    m "Я упустил свой шанс, так сказать ..."
    call her_main("Итак, как вы ожидаете, что я узнаю, кто это сделал?","soft","baseL")
    m "Я уверен, что это работа другого студента.."
    m "(или Снейп, наконец сорвался...)"
    m "Так что мне нужно, чтобы ты, под прикрытием узнала, кто это сделал."
    call her_main("Серьезно? Вы рассчитываете, что я найду студента-преступника в нашей школе?","soft","down_raised",cheeks="blush")
    m "Если тебе не трудно--"
    call her_main("Для меня, это будет честью, [genie_name]!","scream","closed")
    call her_main("Это, несомненно, работа одного из тех презренных \'слизеринцев\'...","open","angryCl")
    call her_main("Ничто не доставит мне большего удовольствия, чем видеть, как такая мразь отправится в \'Азбакан\'...","angry","angryL")
    m "А что такое Азкабан?"
    call her_main("...Это еще одно испытание, сэр?","open","wink")
    m "А как же..."
    call her_main("Ну конечно! Я все об этом знаю!","smile","happy")
    call her_main("Это тюрьма для проклятых... Непроходимый скалистый выход, окруженный суровым северным морем не дает сбежать оттуда...","open","happyCl")
    call her_main("Охраняют ее смертоносные пожиратели всех счастливых мыслей и эмоций, известные как Дементоры...","open","angryL")
    call her_main("Они бесконечно патрулируют тюрьму, пожирая всю надежду из заключенных, сводя их с ума в течение нескольких дней ...","open","angry")
    call her_main("Они мучают их безжалостно всю оставшуюся жизнь...","grin","happyCL")
    call her_main("И идеальное место для размещения всех этих \'слизеринских\' мразей!","angry","angry")

    menu:
        "(...)"
        "-Просто найди ученика.-":
            m "Хватит..."
            m "Просто найди его, чтобы мы могли отправить его в Акабур..."
            call her_main("Азкабан, сэр...","open","wink")
            m "Иди уже."
        "-Скажи ей, что не собираешься отправлять виновника в Азкабан.-":
            m "Господи, [hermione_name], что с тобой?"
            call her_main("О чем вы говорите, [genie_name]?","open","baseL",cheeks="blush")
            call her_main("Всем известно, что жизнь в Азкабане - наказание за наложение непростительного проклятия...","open","closed")
            m "Мне дали специальное разрешение наказывать их по своему усмотрению."
            call her_main("О...","annoyed","base")
            call her_main("Значит, не Азкабан?","soft","baseL")
            m "Только если он кого-то убил..."
            call her_main("Правда? Значит, все еще есть шанс?","base","glance")
            m "Только, если ты найдешь мертвое тело"
            call her_main("Да!","smile","happyCl")

    call her_main("Считайте, что уже сделано, [genie_name]!","open","closed")

    call her_walk("mid","leave",2)

    if snape_on_the_lookout:
        m "Интересно, найдет ли она его раньше Снейпа..."
    else:
        m "Наверное, мне стоит рассказать Снейпу..."

    jump day_main_menu


#TELL SNAPE ABOUT THE LETTER #Done
label letter_intro_snape:
    m "Я получил письмо из Министерства магии..."
    call sna_main("Серьезно?","snape_03") #No xpos change.
    call sna_main("Зачем ты мне это рассказываешь?","snape_04")
    m "По-видимому, они обнаружили в школе нечто, называемое \'непростительным\' проклятием..."
    call play_sound("scratch")
    call sna_main("","snape_11")
    with hpunch
    pause.2
    call sna_main("Дерьмо... в этом нет ничего хорошего...","snape_08")
    m "И если они обнаружат еще одно, то  они пришлют \'мракоборца\' или своего представителя."
    call sna_main("Это действительно нехорошо...","snape_07")
    m "Почему, проклятия настолько плохие?"
    call sna_main("Забудь о проклятиях, если они пришлют сюда Мракоборца, они могут узнать, что мы делаем.","snape_10")
    m "Что?"
    call sna_main("Торговля услугами! Трахать своих студентов, это не то, что преподаватели должны делать, Джинни!","snape_25")
    call sna_main("Если Мракоборец узнает, что здесь происходит, мы оба отправимся в Азкабан!","snape_16")
    m "Так что же мы будем делать?"
    call sna_main("Мы просто должны убедиться, что больше не будет проклятий...","snape_01")
    m "Как нам с этим справиться?"
    call sna_main("Мы должны выяснить, кто проводил обряд.","snape_24")
    call sna_main("Настоящий Дамбдор смог бы обнаружить, кто это сделал, но, теперь ты здесь, вместо него...","snape_06")
    call sna_main("Мы должны найти его по старинке.","snape_10")
    m "Так ты хочешь, чтобы я начал охоту?"
    call sna_main("Ты с ума сошел? Мы не можем никому рассказать, что случилось. Все студенты будут паниковать, думая, что кто-то был убит...","snape_16")
    call sna_main("Наверное, это просто Imperio или Crucio.","snape_24")
    call sna_main("Я начну поиски немедленно. А пока оставайся здесь и занимайся делом.","snape_10")
    m "Тебе не нужна моя помощь?"
    call sna_main("Нет... С тем, насколько сильна твоя магия, ты просто привлечешь больше внимания со стороны министерства, а затем они определенно пришлют мракоборца.","snape_03")
    call sna_main("Не волнуйся, Джинни, я найду этого студента в мгновение ока.","snape_02")

    call sna_walk("mid","leave",2)

    m "Королевская драма..."

    jump day_main_menu


#HERMIONE CAPTURED ASTORIA    #Done
label astoria_captured_intro:
    call play_sound("knocking")
    "*тук* *тук* *тук*"

    m "Кто там?"
    her "Это Гермиона Грейнджер, сэр, хотя,... Я не одна"
    m "Заходите."

    call her_walk("door","desk",2.7)

    call her_main("Здравствуйте, сэр.","normal","happy",xpos="mid",ypos="base")
    m "Я думал, ты сказала, что не одна?"
    call her_main("Не одна.","annoyed","glanceL")
    hide screen hermione_main
    hide screen bld1
    with d3
    pause.2

    call her_chibi("stand","desk",flip=True)
    pause.5

    call her_main("Сюда Астория!","annoyed","angryL",xpos="base",ypos="base")
    ast "{size=+2}{b}Нет!{/b}{/size}"
    call her_main("Ты хочешь сделать все еще хуже?","scream","closed",trans="hpunch")
    ast "Нет..."
    call nar(">Маленькая девочка медленно входит в твой кабинет.")

    call her_chibi("stand","desk",flip=False)
    call her_main("","normal","angry")
    pause.2

    call play_sound("door")
    call ast_main("...","pout","base","worried","R")
    m "..."
    m "Ты кто??"
    call ast_main("Меня зовут Астория Гринграсс, сэр.","disgust","base","worried","mid",xpos="mid",ypos="base")
    m "И почему мы здесь собрались?"
    call her_main("Вы просили меня привести вам человека, который наложил непростительное проклятие, сэр.","soft","annoyed",xpos="close",ypos="base")
    call her_main("А вот и она.","grin","angry")
    m "Я думал, что это будет какой-то подросток, который слушает death-метал или что-то вроде того..."
    m "А не какая-то маленькая девочка..."
    call ast_main("Я не маленькая девочка!","scream","angry","angry","angry")
    m "Тогда кто ты, 600-летний вампир?"
    call ast_main("Вампиры не существуют!","pout","angry","angry","R")
    m "..."
    m "Тогда почему ты не маленькая девочка?"
    call ast_main("Я старше, чем кажусь!","pout","angry","angry","angry")
    m "Я уже слышал это раньше..."
    call her_main("Это действительно так, сэр. Она была проклятым ребенком, рожденная с генным дефектом, влияющим на ее рост.","normal","concerned")
    call ast_main("Я это уже сказала!","smile","angry","angry","R")
    m "Ладно... это все равно не избавит тебя от наказания."
    call ast_main("Наказания? за что?","pout","wide","wide","wide")
    call her_main("Ты знаешь за что!","angry","angryCl")
    call ast_main("Я никогда не колдовала Imperio ни на кого! Я клянусь, сэр! Гермиона всего лишь всезнайка!","pout","wide","worried","R")
    m "Мисс Грейнджер..."
    call her_main("Я слышала, как она хвасталась этим группе слизеринцев в библиотеке.","annoyed","concerned")
    call her_main("Судя по звукам, она использовала Imperio, чтобы контролировать другого студента.","annoyed","base")
    call ast_main("Нет!","worried","angry","worried","angry")
    m "Ну, учитывая серьезность ситуации, я уверен, что есть что-то, что мы можем использовать, чтобы получить от вас четкий ответ..."
    call her_main("Мне принести флакон Правдариума от профессора Снейпа, сэр?","grin","base")
    call ast_main("П-правдариума? Разве это не против правил?","scream","wide","worried","wide")
    call her_main("Не тогда, когда ты накладываешь непростительные проклятия, маленькая злая ведьма!","grin","angry")
    call ast_main("Ладно... Я расскажу вам, что случилось, сэр...","pout","closed","base","mid")
    call ast_main("Но только если Гермиона уйдет!","pout","narrow","base","mid")
    call her_main("Только через мой труп","scream","angryCl")
    m "Мисс Грейнджер..."
    call her_main("Профессор! Я думаю, это несправедливо, учитывая, что я была той, кто поймала ее!","upset","annoyed")
    m "Мы поговорим о твоем вознаграждении позже..."
    call her_main("*hmph*","annoyed","angryL")
    call her_main("Хорошо...","open","angryCl")
    call her_main("Тогда я вернусь в свою комнату...","annoyed","angryL")
    call her_main("До свидания, сэр...","open","angry")
    call her_main("Прощай, Астория...","angry","closed")


    call her_walk("desk","leave",2.7)

    call bld
    m "Хорошо, теперь, когда Гермиона ушла, почему бы тебе не сказать мне точно, что--"

    #magic sound effect and screen shake
    call cast_spell("imperio") #Different effects for different spells.
    call ast_main("{size=+10}{b}IMPERIO{/b}{/size}","scream","angry","angry","angry")

    call blktone
    m "..."
    m "Что это было?"
    call hide_blktone

    call ast_main("Я только что направила Imperio на вас, профессор! Теперь вы должны делать все, что я скажу!","grin","narrow","base","mid")
    g4 "Ты, только что сделала это снова? Еще одно проклятье... на мне?"
    call ast_main("Да... но это должно было... почему ты этого не делаешь?..","worried","narrow","worried","mid")
    m "Ugh..."
    m "Я лучше приведу сюда Снейпа."
    call ast_main("Профессор Снейп? Я приказываю тебе этого не делать!","scream","angry","angry","angry")
    m "Да, нет. Я приведу его сюда, потому что теперь нам, вероятно, придется иметь дело с кем-то, называемым мракоборцем, направляющимся в школу."
    call ast_main("Мракоборцем?!","worried","wide","wide","wide")
    call ast_main("Но они отправят меня в Азкабан!","scream","wide","worried","wide")
    m "Я уверен, они будут снисходительны, ведь ты всего лишь ребенок."
    call ast_main("Я не ребенок!","scream","angry","angry","angry")
    m "Тьфу... Мне лучше позвать Снейпа."

    call play_sound("door")
    call sna_walk("door","mid",2)

    call play_music("snape_theme")
    call sna_main("Джи-о, вижу, к тебе уже пришел посетитель...","snape_03",xpos="base",ypos="base")
    call ast_main("...","pout","base","worried","R")
    call sna_main("Она слишком молода, не так ли? Даже для тебя...","snape_09")
    m "Это не такого рода визит."
    call sna_main("Правда? Тогда что она здесь делает?","snape_05")
    m "Это она кидает эти проклятия."
    call sna_main("Честно? Слизерин?","snape_05")
    call sna_main("Я ожидал большего от своих студентов, мисс Гринграсс...","snape_10")
    call sna_main("Самый первый урок я вам не--","snape_08")
    call sna_main("мог--","snape_08",trans="hpunch")
    call sna_main("дать--!","snape_15",trans="hpunch")
    pause.5
    call sna_main("У вас есть что сказать в свое оправдание?","snape_10")
    call ast_main("Мне... Мне очень жаль, сэр... Это больше не повторится.","disgust","closed","base","mid")
    call sna_main("Ну, если ты накладывала проклятие только один раз...","snape_09")
    call ast_main("Дважды...","disgust","base","worried","R")

    stop music fadeout 1.0
    call play_sound("scratch")
    call sna_main("","snape_11",trans="hpunch")
    pause.5

    call sna_main("Дважды...?!!","snape_15")
    call sna_main("Но это значит...","snape_08")
    call sna_main("Мракоборец уже в пути!","snape_07")
    call sna_main("Мы в полной заднице!","snape_29")
    call sna_main("Кого ты контролировала, маленькая идиотка?","snape_30")
    call sna_main("Кого ты прокляла?","snape_16")
    call ast_main("Ну, в первый раз я просто проверяла это на Сьюзан Боунс...","disgust","closed","base","mid")
    call ast_main("Она была груба со мной, так что я... ..использовала Imperio... чтобы немного смягчить ее...","smile","narrow","worried","mid")
    call sna_main("А второй раз?","snape_01")
    call ast_main("Я просто пыталась использовать Imperio против профессора Дамблдора, чтобы он не втянул меня в неприятности...","disgust","base","base","R")
    call ast_main("Но это не сработало!","pout","base","base","wide")
    call sna_main("Правда? Это должно быть потому, что он Джи-","snape_05")
    call sna_main("Гениальный маг!","snape_17",trans="hpunch")
    call sna_main("Но в этом нет ничего хорошего... Если они пришлют сюда мракоборца, они захотят поговорить с тобой... Дамблдор...","snape_16")
    m "Со мной??"
    call sna_main("Боюсь, что да...","snape_06")
    m "Как скоро он будет здесь?"
    call sna_main("Я не знаю, и я не собираюсь это выяснять!","snape_16")

    call sna_walk("mid","leave",1.5)

    g4 "Трус!"
    call play_music("night_theme")
    call ast_main("Значит, действительно приближается мракоборец?","worried","closed","worried","mid")
    call ast_main("Я слышала, что их всех тренирует \"Mad-Eye\ Moody (прим. Алистер \"Злой-глаз\" Грюм)...","worried","closed","worried","mid")
    call ast_main("ПОЖАЛУЙСТА, СЭР!","worried","wide","wide","wide",tears="crying")
    call ast_main("Вы не можете позволить им, отправить меня в Азкабан!",tears="crying")
    call ast_main("Обещаю, все будет хорошо! Я больше не буду накладывать проклятия!","scream","closed","base","mid")
    call ast_main("Я сделаю все, что вы захотите!","scream","base","worried","R",tears="crying")
    m "Успокойся..."
    call ast_main("Н-Н-но... Я не хочу... в Азкабан...","worried","closed","worried","mid")
    m "Я не позволю им забрать тебя в Азкабан."
    call ast_main("С-С-С-Серьезно? Даже после того, как я пыталась контролировать вас?","smile","wink","worried","mid")
    m "(Нет ни одного существа, которое может контролировать меня!)" #4th wall break, lololol
    m "Мы поговорим о твоем наказании позже. А пока, я думаю, тебе лучше вернуться в свою комнату."
    call ast_main("A-a-хорошо... но что насчет мракоборца?","worried","wink","base","mid")
    m "Я просто объясню им, что это было простое недоразумение."
    call ast_main("С-спасибо, сэр...","smile","narrow","base","mid")
    m "Тем не менее, я ожидаю, что ты будешь приходить ко мне в кабинет каждый раз, когда я буду вызвать тебя."
    call ast_main("Ч-что? Зачем?","pout","wide","worried","wide")
    m "Возможно, мне придется позвать тебя сюда, чтобы увидеть мракоборца. Не говоря уже о том, что у нас все еще есть вопрос о твоем наказании."
    call ast_main("Но я думала, что это просто недоразумение?","pout","base","narrow","R")
    m "Ты совершила очень серьезное преступление, девочка. То, что ты не собираешься в Азкабан, не значит, что ты избежишь наказания."
    call ast_main("Хорошо, сэр...","pout","base","worried","R")
    m "Славно. А теперь возвращайся в свою комнату, пока я тебя не позову."
    g4 "И прекрати это проклятие, немедленно!"
    call ast_main("Да, сэр...","pout","closed","base","mid")
    hide screen astoria_main
    with d3

    call nar(">Астория поворачивается к выходу из кабинета, слегка удрученно глядя на перспективу будущего наказания.")
    m "(Я чувствую, что начинаю управлять этой чертовой школой.)"
    m "(Это не то, на что я подписывался...)"

    call give_reward(">Ты открыл возможность вызывать Асторию в свой кабинет.","images/store/astoria_unlock_01.png")

    $ astoria_busy = True
    $ hermione_takes_classes = True
    $ snape_busy = True

    jump day_main_menu



#TONKS AUROR INTRO #Done
label tonks_intro_event: #occurs a day or two after the last event
    call play_sound("knocking")
    "*тук* *тук* *тук*"

    m "Ахх..."
    m "Кто это?"
    ton "Нимфадора Тонкс, сэр."
    ton "Я из Министерства Магии.."
    m "(Черт, еще одна женщина... Снейп, что единственный чувак на этой забытой планете?)"
    g9 "(Сыграю на своем обоянии...)"
    m "Да... входите."

    call play_sound("door")
    call ton_main("","base","base","base","mid",xpos="right",ypos="base")
    call ctc

    g4 "(Черт возьми!)"
    g9 "(Да она горячая!)"
    call ton_main("Спасибо, сэр... Полагаю, вы знаете, почему я здесь?","open","base","base","mid")
    m "Проклятие, я осведомлен."
    call ton_main("Да. Я уверена, вы знаете протокол министерства, по которому мракоборец расследует каждый случай непростительного проклятия.","open","base","raised","R")
    call ton_main("Министерство было готово игнорировать одно проклятие, учитывая вероятность того, что это был просто студент...","open","base","worried","down")
    call ton_main("Два проклятия нельзя игнорировать.","open","base","raised","mid")
    m "Я понимаю..."
    call ton_main("Хорошо, во-первых, вы знаете, кто произносил заклинания?","base","base","raised","mid")
    m "Знаю."
    call ton_main("Фантастика, это экономит мне большую часть усилий, связанных с поисками.","open","base","base","mid")
    call ton_main("Во-вторых, вы знаете, какое заклинание было наложено?","base","base","raised","mid")
    m "(Черт... Как же оно называется?)"

    menu:
        "\'Imperio\'":
            call ton_main("Я тоже об этом подумала.","base","base","worried","R")
        "\'Imperial\'":
            call ton_main("Вы имеете в виду Imperio, сэр?","base","base","raised","mid")
            m "Да,конечно, простите меня..."
        "\'Imp piy-piy?\'":
            call ton_main("...","base","base","raised","mid")
            call ton_main("Это серьезный вопрос, сэр, я бы предпочла, чтобы вы оставили шутки на потом.","open","base","angry","mid")
            m "Конечно..."

    call ton_main("Ну, я не удивлена, обычно это Imperio.","open","base","worried","R")
    call ton_main("У большинства студентов не хватает смелости бросить Crucio на другого человека...","open","base","worried","mid")
    call ton_main("Не говоря уже о Avada Cadavara...","open","wide","wide","wide")
    call ton_main("И, наконец, знаете ли вы, на кого наложено проклятие?","open","base","worried","mid")
    m "Да."
    call ton_main("Если вы не возражаете...","base","base","raised","mid")
    m "Сьюзан Боу-"
    call ton_main("Сьюзан Боунс!","open","wide","wide","wide",trans="hpunch")
    m "Что-то случилось?"

    show screen blktone
    call ton_main("Конечно, что-то случилось!","open","wide","angry","wide")
    call ton_main("Сьюзан - моя племянница!","open","base","angry","mid")
    call ton_main("И вы просто так, позволили наложить на нее непростительное проклятие?","open","base","angry","mid")
    call ton_main("Разве вы не должны защищать своих учеников от подобных вещей?","open","base","angry","mid")
    m "Их слишком много. Что я могу подела-"
    call ton_main("Типично! Ты такой же, как и министерство, никогда не желающие брать на себя ответственность за свои ошибки.","open","base","angry","R")
    call ton_main("По крайней мере, приведи сюда этого выродка, который проклял мою племянницу, чтобы я сопроводила его в Азкабан.","open","base","angry","mid")
    m "Азкабан? Я думал, что я был назначен ответственным за их наказание?"
    call ton_main("Это было до того, как я узнала, кто был проклят, Дамблдор!","open","base","base","mid")
    call ton_main("Теперь они будут наказаны по всей строгости закона.","open","wide","angry","wide")
    call ton_main("Только пожизненное заключение в Азкабане!","open","base","raised","mid")
    m "..."
    call ton_main("Ну ты собираешься привести его сюда или нет?","open","base","angry","mid")
    m "Я правда не думаю, что-"
    call ton_main("Мне плевать, хоть сам Гарри {b}чертов{/b} Поттер, это сделал, он уедет в Азкабан!","open","base","angry","mid")
    call ton_main("Ну... зови {size=+2}его {size=+2}. {size=+2}сюда!..","open","base","angry","mid")
    call ton_main("{size=+5}Сейчас же!{/size}","open","base","angry","mid",trans="hpunch")
    m "Хорошо..."
    call blkfade

    ">Ты вызываешь Асторию в свой кабинет.."
    pause.5
    hide screen tonks_main
    hide screen blktone
    hide screen blkfade
    call ast_main("","upset","base","worried","R",xpos="mid",ypos="base",trans="fade")
    pause.8

    call ast_main("Здравствуйте, профессор.","upset","closed","base","mid")
    call ton_main("...","base","base","raised","L",xpos="base",ypos="base")
    call ast_main("Здравствуйте, мэм.","pout","base","worried","R")
    call ton_main("З-здравствуй...","open","base","raised","L")
    call ast_main("Вы хотели меня видеть, сэр?","pout","narrow","base","down")
    m "Боюсь, что нет, вообще-то, это мисс Тонкс хотела, чтобы тебя сюда вызвали"
    call ast_main("Ох...","upset","base","worried","down")
    call ast_main("Все в порядке?","worried","wink","worried","R")
    call ton_main("Ты же не серьезен, Дамблдор... ?!","open","base","angry","mid")
    call ton_main("Приведите сюда настоящего заклинателя.","open","base","angry","mid")
    m "Он перед тобой."
    call ton_main("Серьезно?","base","base","wide","L")
    m "Серьезно."
    call ast_main("Это по поводу Imperio, которое я наложила... ?","pout","narrow","worried","down")
    call ast_main("Мне действительно очень жаль! Я обещаю, что больше такого не повторится","scream","closed","worried","mid")
    call ton_main("Правда? Это ты наложила заклинание?","open","base","worried","L")
    call ton_main("Но...","open","base","angry","down")
    call ton_main("Но.......","open","base","raised","L")
    call ton_main("Но ты же еще такая {size=+10}хорошенькая!{/size}","open","wide","wide","wide",trans="hpunch")
    call ast_main("...","disgust","wide","wide","wide")
    m "..."
    call ton_main("Это не мог быть кто-то вроде тебя!","open","base","wide","L")
    call ast_main("Прошу прощения, мисс... это была я...","open","closed","base","R")
    call ton_main("Правда?","base","base","raised","L")
    call ast_main("Пожалуйста, не отправляйте меня в Азкабан!","scream","wide","wide","wide")
    call ast_main("Я не хочу к дементорам!","scream","closed","worried","mid")
    call ton_main("Не волнуйся, до этого не дойдет...","base","base","base","L")
    call ast_main("П-п-п-правда?","upset","wink","base","R")
    call ton_main("Конечно, нет!","base","base","raised","mid")
    call ton_main("Министерство не собирается запирать такую милую маленькую девочку, как ты, на всю жизнь...","open","base","base","mid")
    call ton_main("{size=+2}Безобидная забава{/size} {image=textheart}","horny","base","wide","L")
    m "..."
    call ton_main("Так что ты заставила Сьюзан сделать?","base","base","raised","L")
    call ton_main("Бегать кругами, как цыпленок?","base","base","raised","mid")
    call ast_main("Не совсем...","upset","closed","base","mid")
    call ton_main("Давай тогда, рассказывай.","base","base","base","L")
    call ast_main("Я заставила ее показать сиськи на несколько секунд...","upset","wink","base","mid")
    call ton_main("Хахахаха!","base","base","wide","L")
    call ast_main("Всего лишь на несколько секунд!","pout","base","worried","R")
    m "(Что здесь происходит?)"
    call ton_main("И это все? Ты, вероятно, тогда сделала Сьюзен некоторую пользу, все знают, что она должна немного расслабиться.","base","base","wide","L")
    call ton_main("Она всегда была очень чувствительна к своему телу.","base","base","raised","mid")
    call ast_main("Значит, у меня не будет неприятностей?","upset","base","base","mid")
    call ton_main("Я этого не говорила... Ты совершила серьезный проступок наколдовав запрещеное заклинание.","open","base","base","L")
    call ton_main("Однако, учитывая обстоятельства, я оставлю твое наказание в руках профессора Дамблдора.","open","base","base","mid")
    m "Мне?"
    call ton_main("Это не проблема, сэр?","base","base","raised","mid")
    m "Нисколько!"
    call ton_main("Фантастика.","base","base","base","mid")
    call ton_main("Теперь, как часть стандартной процедуры Министерства, я собираюсь остаться в школе еще не на долго.","open","base","raised","mid")
    call ton_main("Просто чтобы убедиться, что не произойдет ничего страшного.","base","base","base","mid")
    call ton_main("С момента рекурсии Imperio в прошлом году в Beauxbatons(Шармбатоне)...","open","base","raised","mid")
    call ton_main("...они чуть не преступили черту к темным волшебникам этого рода заклинаний...","open","base","angry","R")
    m "Хорошо..."
    call ton_main("Можешь идти, малышка.","base","base","base","L")
    call ast_main("Хмм... Ок. Спасибо, сэр...","upset","closed","base","mid")
    call ast_main("Мэм...","upset","wink","base","R")
    hide screen astoria_main
    with d3
    pause.8

    call ton_main("Итак {size=+5}милая!{/size} {image=textheart}","base","base","wide","mid",xpos="right",ypos="base")
    call ton_main("В любом случае, я предполагаю, что мне разрешат спать в кабинете.","open","base","raised","mid")
    m "Конечно, я немедленно заправлю тебе постель."
    call ton_main("Спасибо, Дамблдор. Приятного вечера.","base","base","base","mid")
    m "И тебе..."
    hide screen tonks_main
    with d3
    pause.8

    m "(Я даже не знал, что здесь есть кровать, а я спал на этом стуле...)"
    m "(Мне очень нужно почистить эту штуку....)"
    m "asd"

    $ astoria_busy = True

    jump day_main_menu



#SNAPE MASKING SPELL #Done
label snape_spell_intro: #Snape tells genie that he has adjusted the magic shield
    call play_sound("door")
    call sna_walk("door","mid",2)

    call play_music("snape_theme")
    call sna_main("У меня получилось, Джинни!","snape_02",xpos="base",ypos="base")
    m "Получилось что?"
    m "Ты никого не убивал?"
    m "Я не могу вернуть людей к жизни, Снейп! Не жди, что я помогу с этим..."
    call sna_main("Что? Нет...","snape_01")
    call sna_main("Я решил нашу проблему с Министерством!","snape_02")
    m "О... Правда? Как?"
    call sna_main("Честно говоря, это было гениально...","snape_23")
    call sna_main("Я изменил магловское маскирующее заклинание, чтобы включить непростительные проклятия!","snape_02")
    m "И это маскирующее заклинание...  Сработало?"
    call sna_main("Это огромное магическое силовое поле окружает нас, Джинни.","snape_24")
    call sna_main("Прячем замок и все что в нем находится от всех немагических существ. И все исчезнет от взора.","snape_24")
    call sna_main("Я могу изменить его, чтобы также окутать все непростительные проклятия, которые брошены в нем!","snape_23")
    call sna_main("За исключением смертельного, конечно. Остальные на мой взгляд вполне безобидны...!","snape_09")
    call sna_main("Ты должен знать, что магия в этом мире находится под пристальным наблюдением Министерства магии.","snape_01")
    m "И это должно остановить мракоборцев от прихода сюда?"
    call sna_main("Пока они не пронюхают про наши делишки, мы можем их не бояться!","snape_02")
    call sna_main("Ты можешь себе это представить? Совершенно новый мир пыток и подчинений этих грязных девчонок нашей воле!","snape_20")
    call sna_main("У меня есть целый набор слизеринских шалуний, которые охотно позволили бы мне попробовать эти проклятия на них!","snape_21")
    call sna_main("Разве ты не впечатлен, Джинни?","snape_22")
    m "(Это означает, что я мог бы заставить эту маленькую Асторию Гринграсс показать мне магическую силу...)"
    m "Я впечатлен..."
    call sna_main("Что? Ну, что самое впечатляющее ты сделал с магией?","snape_25")
    m "Однажды я превратил мир в пустынную Арабскую пустошь..."
    call sna_main("...","snape_09")
    if daytime:
        jump snape_ready
    else:
        call sna_main("Может выпьем?","snape_02")
        m "Я не против!"

        jump snape_dates #Snape Genie drinking. Jumps to next day.



#SUSAN INTRO #
label astoria_susan_intro: #have astoria demonstrate the imperio spell for the first time on Susan
    call ast_main("Вы хотели меня видеть, сэр?","upset","wink","worried","mid",xpos="mid",ypos="base")
    m "Да. Думаю, пришло время обсудить вопрос о твоем наказании."
    call ast_main("Ох... Я надеялась, что вы забыли об этом.","pout","narrow","narrow","R")
    m "Конечно нет."
    call ast_main("Что мне нужно делать?","upset","base","base","mid")
    call ast_main("Мне не придется чистить туалеты, не так ли?!","scream","wide","wide","wide")
    m "Не волнуйся, ничего подобного."
    call ast_main("Ох...","disgust","narrow","narrow","R")
    call ast_main("Тогда что же это будет такое?","upset","wink","base","mid")
    m "Первым делом, я ожидаю, что ты будешь приходить в этот кабинет каждый раз, когда я буду вызывать тебя."
    call ast_main("Что? Разве мы не можем покончить с этим сразу?","scream","wide","wide","wide")
    m "Что-то вроде непростительного проклятия не так легко простить, Мисс Гринграсс.."
    m "Все записано в названии!"
    m "Ты знаешь, что такое обычное наказание..."
    call ast_main("Жизнь в Азкабане...","disgust","closed","worried","mid")
    m "Вот именно... Если ты не хочешь, чтобы я тебя отослал, думаю, тебе лучше согласиться на это."
    call ast_main("...","pout","narrow","narrow","R")
    call ast_main("Хорошо... Но вам лучше ничего не делать!","open","angry","worried","angry")
    g4 "Мне?"
    m "Ничего..."
    call ast_main("...","pout","base","base","R")
    call ast_main("Какова ваша вторая просьба.","upset","base","base","mid")
    m "Моя вторая и последняя просьба - наложить на меня непростительное проклятие."
    call ast_main("{size=+10}Что?{/size}","scream","wide","wide","wide")
    call ast_main("Но я не хочу в Азкабан! Вы слышали, что сказала та противная старушка!","scream","wide","wide","mid")
    m "Не волнуйся, ты не поедешь в Азкабан."
    call ast_main("Как вы можете быть таким уверенным? Она не простит, если я произнесу еще одно проклятье.","scream","narrow","narrow","mid")
    m "Не волнуйся, я уверен, что никто не узнает."
    call ast_main("...","disgust","wide","wide","down")
    call ast_main("Но почему вы хотите, чтобы на вас наколдовали непростительное проклятие?","open","wink","worried","mid")
    m "Скажем так, мне просто любопытно."
    m "(Я хочу, чтобы кто-нибудь контролировал мой разум!)"
    call ast_main("...","pout","angry","angry","angry")
    call ast_main("Это не проверка?","pout","angry","angry","R")
    call ast_main("Вы заставляете меня произнести еще одно заклятие, чтобы меня действительно отправили в Азкабан, не так ли?","disgust","narrow","narrow","mid")
    call ast_main("Я не стану этого делать!","scream","closed","base","mid")
    m "Думаю, ты забываешь, что я могу отправить тебя в Азкабан и так."
    call ast_main("Ох...","disgust","base","worried","down")
    call ast_main("Но я все еще не понимаю, почему вы хотите, чтобы я наложила проклятие?","open","base","worried","mid")
    m "(Ugh...)"
    m "Из-за твоего исключительного мастерства! Не каждый может наложить такое проклятие!"
    call ast_main("Скорее всего нет... Я была очень зла, когда я произносила его...","pout","base","base","R")
    call ast_main("Я не уверена, что смогу сделать его снова...","open","wink","base","mid")
    m "Считай это испытанием!"
    call ast_main("...","upset","base","worried","mid")
    call ast_main("Хорошо...","pout","base","worried","L")
    call ast_main("Но я точно не окажусь в Азкабане?","scream","closed","base","mid")
    m "Честное пионерское."
    call ast_main("Вы все еще хотите, чтобы я произнесла его?","worried","base","base","mid")
    call ast_main("Оно не сработало, когда я в последний раз колдовала его на вас..","worried","base","base","R")
    m "На кого, ты сказала, наложила его в прошлый раз?"
    call ast_main("Сьюзан Бонс, сэр.","smile","base","base","mid")
    m "Давай попробуем еще раз, посмотрим, как это работает."
    call ast_main("Что? Вы хотите, чтобы я наложила проклятие на другого ученика? Снова?","scream","wide","wide","wide")
    m "Они ведь не вспомнят, что мы это сделали?"
    call ast_main("Полагаю... нет.","pout","narrow","narrow","R")
    call ast_main("Я просто не ожидала, что вы сами будете настаивать на совершении чего-то подобного...","open","base","base","mid")
    m "Поверь мне, я делал вещи и похуже..."
    call ast_main("...","smile","base","base","down")
    call ast_main("Хорошо... I'll do it.","grin","base","base","mid")
    m "Фантастика!"
    call ctc

    call ast_main("...","pout","base","base","R")
    call ctc

    call ast_main("Вы не собираетесь вызвать ее??","open","wink","base","mid")
    m "Я не могу."
    call ast_main("Почему?","upset","narrow","narrow","mid")
    m "Потому что она еще не приходила ко мне в кабинет. Почему-то я могу вызывать только тех, кого встречал раньше."
    call ast_main("Это кажется глупым.","pout","narrow","narrow","R")
    m "Не мне это говори..."
    call ast_main("Тогда мне пойти и позвать ее?","smile","wink","worried","mid")
    m "Если ты не возражаешь."
    call ast_main("ЛАДНО... что я должна ей сказать?","grin","closed","base","mid")
    m "Ты о чем?"
    call ast_main("Чтобы заставить ее подняться сюда!","open","base","base","down")
    call ast_main("Мне нужно ей что-то сказать.","open","base","base","mid")
    m "Просто скажи ей, что я хочу с ней поговорить."
    call ast_main("Правда? Разве это не может быть что-то более веселое?","pout","angry","base","R")
    m "Веселое?"
    call ast_main("Знаете что-то, что заставит ее думать, что она в беде, так что она будет бояться и нервничать, когда придет сюда?","open","base","base","L")
    m "Ты можешь говорить ей все,что захочешь, чтобы она пришла сюда."
    call ast_main("Хорошо!","happy","base","base","mid")
    call ast_main("Я скоро вернусь.","grin","angry","angry","mid")
    hide screen astoria_main
    hide screen bld1
    call blkfade

    ">Астория покидает твой кабинет, напевая что-то."
    pause.5
    call hide_blkfade
    pause.5

    call bld
    m "..."
    pause.5
    m "Это может занять некоторое время..."
    pause.5
    g9 "Вполне возможно..."
    hide screen bld1
    with d3
    pause.1

    call gen_chibi("jerking_off_behind_desk")
    with d3
    pause.8

    call play_sound("knocking")
    "*Тук* *Тук* *Тук*"
    call bld
    m "(Черт...)"
    m "Обождите секунду..."

    call gen_chibi("hide")
    show screen genie
    with d3
    pause.2

    m "Войдите."
    call play_sound("door")
    call sus_main("","upset","base","worried","mid",xpos="mid",ypos="base")
    call ctc
    with hpunch
    g4 "!!!"
    g9 "(Посмотри кто стучится)"
    call ast_main("","pout","angry","angry","L",xpos="base",ypos="base")
    pause.8

    m "А это кто еще такая?!!"
    call sus_main("Меня зовут Сьюзан Боунс, сэр...","open","base","worried","L")
    call sus_main("Астория сказала, что вам нужно срочно меня увидеть.","open","narrow","worried","down")
    m "Да... Должен увидеть... их..."
    call sus_main("...","upset","base","worried","mid")
    call sus_main("Если вы не возражаете, я спрошу, сэр... что вы хотите этим сказать?","open","base","worried","mid")
    m "Хм... Астория тебе не говорила?"
    call sus_main("Н-Нет, сэр...","upset","base","worried","L")
    m "Ну, мисс Гринграсс и я обсуждали, как лучше продолжить образование.--"

    call ast_main("","grin","angry","angry","angry")
    call cast_spell("imperio")
    call sus_main("","upset","wide","base","wide")
    call ast_main("{size=+10}{b}IMPERIO{/b}{/size}","scream","angry","angry","angry")
    call ast_main("","smile","angry","angry","angry")

    call nar(">Перед лицом Сьюзан появляется клубы желтого дыма.","start")
    call sus_main("Что это--","open","narrow","worried","up")
    ">Быстро попав в нос Сьюзан, дым меняет выражение ее лица ."
    call sus_main("...","base","base","base","up")
    call nar(">Глаза Сьюзан становятся пустыми, ее тело расслабляется.","end")

    call ast_main("Ура! Это сработало!","grin","angry","angry","angry")
    m "Отлично!"
    call ast_main("Так что же нам теперь сделать?","grin","closed","base","mid")
    call ast_main("Хотите, я заставлю ее танцевать, как цыпленок?","grin","angry","angry","L")
    m "Не очень..."
    call ast_main("Что тогда?","open","wink","base","mid")
    m "Что ты сделала с ней в первый раз?"
    call ast_main("...","pout","angry","angry","R")
    call ast_main("Не могу сказать... Это слишком унизительно!","pout","narrow","narrow","R")
    g9 "Мне нужно это знать!"
    call ast_main("ЛАДНО... Но вы должны пообещать, что не будете злиться на меня!","pout","narrow","narrow","mid")
    m "Хорошо..."
    call ast_main("Ну, несколько девчонок говорили об этом...","open","base","base","mid")
    call ast_main("...","upset","base","worried","down")
    call ast_main("Они говорили о груди, сэр!","disgust","base","base","down",cheeks="blush")
    g9 "(ДЖЕКПОТ!)"
    m "Продолжай..."
    call ast_main("Они говорили о том, что мальчикам нравятся только большие...","open","narrow","narrow","down",cheeks="blush")
    call ast_main("И что, они только девушек с большими сиськами приглашали на осенний бал...","open","narrow","worried","down",cheeks="blush")
    m "Сьюзан была одной из этих девушек?"
    call ast_main("Нет, сэр. Это были несколько \'Слизеринских\' девушкек, которые разговаривали в общей комнате.","open","base","base","mid")
    m "Тогда как Сьюзан оказалась вовлечена во все это?"
    call ast_main("Это была ее собственная вина!","pout","angry","angry","R")
    m "..."
    call ast_main("А чего она ожидала, когда выставляла напоказ эти отвратительные сиськи на всю школу!","pout","angry","angry","L")
    call ast_main("Это справедливо, что кто-то поставил ее на место!","pout","angry","angry","mid")
    m "И этим кем-то была ты?"
    call ast_main("...","upset","narrow","narrow","mid")
    call ast_main("Да...","worried","narrow","narrow","down",cheeks="blush")
    m "Итак, что же ты сделала?"
    call ast_main("Я приказала... Снять...","worried","angry","angry","R")
    call ast_main("Я заставил ее ходить без рубашки...","pout","angry","angry","R")
    m "Что? Правда?"
    call ast_main("Прошу прощения, сэр! Это было в комнате отдыха.","open","base","worried","mid")
    call ast_main("Я была так зла, что она привлекла все внимание мальчиков.","worried","base","worried","down")
    call ast_main("Поэтому я уделила ей все внимание, о котором она только могла мечтать!","worried","base","base","L")
    call ast_main("Хотя это было только в комнате отдыха для девочек, так что ничего страшного...","open","closed","base","mid")
    call ast_main("И она все равно не сможет это вспомнить...","open","base","base","R")
    call ast_main("Это было {b}увлекательно{/b}, указать ей на ее место...","grin","angry","angry","R")
    m "И что сделали другие девушки, когда ты начала ее выставлять напоказ?"
    call ast_main("Сначала они все были шокированы...","grin","base","base","mid")
    call ast_main("Некоторые из них просто сказали ей перестать хвастаться и надеть верх...","open","angry","angry","R")
    call ast_main("Так что мне пришлось сделать все немного более неловким для нее...","grin","angry","angry","mid")
    m "И как?"
    call ast_main("Я заставила ее танцевать...","grin","base","base","mid")
    m "Танцевать?"
    call ast_main("Ну... Я просто заставила ее трясти сиськами перед ними...","smile","base","base","R")
    m "Ты можешь заставить ее сделать это снова?"
    call ast_main("ЧТО!","disgust","wide","wide","wide")
    call ast_main("Профессор! Я не могу сделать что-то подобное!","scream","closed","base","mid")

    menu:
        "\"Почему нет?\"":
            call ast_main("Потому что... Потому что это неправильно!","open","closed","worried","mid")
            call ast_main("Вы слишком стары для этого!","scream","wide","wide","mid")
            call ast_main("И вы учитель!","worried","wide","wide","wide")
            m "И что?"
        "\"Ну же...\"":
            call ast_main("...","pout","angry","angry","mid")
            call ast_main("Вы шутите, сэр?","pout","angry","angry","R")
            m "Возможно..."

    call ast_main("Даже не думайте, что я сделаю что-то подобное!","disgust","closed","worried","mid")
    call ast_main("За исключением...","open","wide","wide","wide")
    m "Исключением?"
    call ast_main("Возможно, если вы сделаете это стоящим моего времени...","grin","angry","angry","mid")
    call ast_main("Возможно, мне это понравится...","open","narrow","narrow","mid")
    call ast_main("Заставляя Сьюзан танцевать для вас...","open","narrow","narrow","R")
    m "И что это будет за вознаграждение?"
    call ast_main("Мне нужны очки!","scream","closed","angry","mid",trans="hpunch")
    m "(...Где-то я уже это слышал...)"
    m "С какого ты факультета?"
    call ast_main("Слизерин! Вы должны это знать!","pout","narrow","narrow","R")
    m "Как насчет вместо этого--"
    call ast_main("Это не все!","scream","closed","angry","mid",trans="hpunch")
    call ast_main("Я также ожидаю, что вы научите меня новым заклинаниям!","scream","angry","angry","mid")
    m "Что?"
    call ast_main("Все заклинания, которые я изучаю в классе, такие {b}скучные!{/b}","pout","angry","angry","R")
    call ast_main("Эти тупые учителя хотят, чтобы мы изучали только безопасные заклинания..","pout","angry","angry","L")
    call ast_main("Это одна из причин, почему я прокляла Сьюзан в первую очередь...","pout","angry","angry","mid")
    call ast_main("Непростительные проклятия были первыми забавными заклинаниями, о которых я узнала!","open","narrow","narrow","mid")
    call ast_main("Ну, может быть, не такое как Crucio или Avada Kadavra...","open","narrow","narrow","down")
    call ast_main("Но Imperio!","clench","angry","angry","angry")
    call ast_main("Это так весело!!!","grin","closed","base","mid")
    call ast_main("Я хочу выучить побольше подобных заклинаний!","grin","angry","angry","mid")
    call ast_main("Так что я жду, что ты научишь меня, я уверена, ты их все знаешь, старик.","open","closed","base","mid")
    m "(Я нихрена не понимаю.)"
    m "Хорошо..."
    call ast_main("Ура!","grin","closed","base","mid")
    call ast_main("Хорошо в таком случае...","smile","base","base","mid")

    #Susan Strips.
    call ast_main("Сьюзан, покажи профессору Дамблдору хороший танец...","scream","closed","base","mid")
    call sus_main("Да...","base","base","base","mid")
    call nar(">Сьюзан начинает медленно двигать бедрами в стороны, едва двигаясь.")
    call ast_main("Это ужасно!","scream","wide","wide","L")
    call sus_main("Ох...","upset","base","worried","mid")
    call ast_main("Сними хотя бы кофточку....","grin","angry","angry","L")
    call ast_main("Не волнуйся, Дамби, я позабочусь, чтобы ты получил хорошее шоу!","open","closed","base","mid")
    m "Дамби? (прим. Dumbledore, Dumby-Дурачек,Тупица)"
    call ast_main("Сокращенно от Дамблдора!","pout","narrow","narrow","mid")
    m "А... Ну хорошо..."

    #call set_sus_top("shirt_2") #ADD Shirt without vest.
    #pause.5

    #call nar(">As the two of you talk, Susan slowly removes her vest.")
    #call ast_main("That's it Susy, one piece at a time.","scream","narrow","base","L")
    call ast_main("Сьюзи, покажи нам свое вымя и сними жилет.","grin","narrow","base","L")
    m "Кажется, ты изменила свой тон..."
    call ast_main("Потому что теперь я знаю, что это не тест.","open","closed","base","mid")

    #call set_sus_top("shirt_3") #ADD Shirt without vest and tie.
    #pause.5

    #call nar(">Susan quietly removes her tie.")
    call ast_main("До этого, я была уверена, что ты меня исключишь, как только я наложу Imperio.","open","base","base","mid")
    call ast_main("Но после того, как ты попросил показать сиськи Сьюзи... Ну...","open","base","base","L")

    hide susan_main
    $ susan_wear_top = False
    call update_sus_uniform
    call sus_main("","base","base","base","mid")
    pause.5

    call nar(">Сьюзан снимает свою рубашку.")
    call ast_main("А теперь я научусь новым крутым заклинаниям!","grin","angry","angry","L")
    call ast_main("...","pout","narrow","narrow","L")
    call ast_main("Самым крутым, старик!","pout","angry","angry","mid")
    call ast_main("Я не хочу чего-то скучного, вроде фейерверка или чего-то подобного.","open","closed","base","mid")
    m "Что ты имеешь в виду?"
    call ast_main("Хммм--","pout","base","base","R")
    call ast_main("Что-то, что никто не знает!","grin","angry","angry","mid")
    m "Так тебе нужны тайные заклинания?"
    call ast_main("Да! И они должны быть веселыми! Я не хочу секретное заклинание по поиску лягушки!","open","closed","base","mid")


    call nar(">Сьюзан медленно двигает руками, чтобы расстегнуть лифчик...")
    m "Ах... Да... Конечно... Все, что ты сказала..."
    call ast_main("...","pout","narrow","narrow","mid")
    call ast_main("Ты рад видеть ее сиськи старик?","open","narrow","narrow","L")
    m "Да... Не каждый день можно увидеть такие..."
    call ast_main("Архх","pout","narrow","narrow","R")
    call ast_main("Типичные...","pout","narrow","base","R")
    m "Шшшш..."
    call ast_main("Они отвратительны...","pout","closed","angry","mid")
    call ast_main("Каждый {size=-2}знает {size=-2}что {size=-2}большие {size=-2}сиськи {size=-2}слишком {size=-2}отвратительные...{/size}","scream","closed","base","mid")
    call ast_main("Я думаю, ты достаточно насмотрелся, старик!","scream","angry","angry","mid",trans="hpunch")
    m "Ты можешь быть не такой серьезной!"
    call ast_main("[ast_susan_name], я приказываю тебе остановиться!!","open","base","base","L")
    call ast_main("Оденься, иди в свою комнату и ложись спать!","grin","base","base","L")
    call sus_main("Да...","base","base","base","up")
    pause.5

    call set_sus_top("shirt_1") #Normal top.
    with d3
    pause.8

    call play_sound("door")
    hide screen susan_main
    with d3
    pause.2

    call play_music("hermione_theme")
    call ast_main("","grin","angry","angry","mid",xpos="mid",ypos="base",trans="fade")
    pause.5

    m "О, но мы как раз добирались до самого лучшего!"
    call ast_main("Ты можешь приберечь это для следующего раза, старик, я думаю, ты уже достаточно повеселился сегодня.","open","closed","base","mid")
    call ast_main("Чуть дальше и ты начнешь забываться","grin","angry","angry","mid")
    call ast_main("В то же время, я хочу, чтобы ты нашел для меня забавные и секретные заклинания!","open","base","base","R")
    m "Ладно..."
    call ast_main("Договорились, только не зови меня сюда, пока они не будут у тебя!","smile","closed","base","mid")
    call ast_main("Пока, профессор!","open","base","base","mid")
    m "Прощай, дитя..."
    call ast_main("*архм*(Я не ребенок...)","pout","angry","angry","R")
    hide screen astoria_main
    hide screen bld1
    with d3

    call give_reward(">Ты открыл возможность вызывать Сьюзан в свой кабинет.","images/store/susan_unlock_01.png")

    $ astoria_busy = True
    $ susan_busy = True

    jump day_main_menu



#SNAPE HANDS OVER HIS BOOK #Done
label snape_book_intro: #Have genie ask for a book of sex spells
    m "Итак, чтобы использовать магию, я должен сказать слова, дабы правильно наложить заклинания?"
    call sna_main("Ну конечно! Ты же не думаешь, что мы просто шевелим носами?","snape_05",xpos="base",ypos="base")
    m "Полагаю, нет..."
    m "У тебя случайно нет секретных заклинаний?"
    call sna_main("Секретные заклинания? Для чего?","snape_04")
    m "Для ме..."
    m "Для студента..."
    call sna_main("Что? Мисс Грейнджер?","snape_01")
    call sna_main("Ты можешь забывать обо мне, давая ей что угодно!","snape_10")
    m "Успокойся, Северус, это не Гермиона, это кое-кто другой..."
    call sna_main("О, ты наконец-то нашел себе другую, не так ли?","snape_02")
    m "В некотором смысле... Я все еще пытаюсь заставить ее плясать под мою дудку."
    m "Но взамен она хочет, чтобы я научил ее секретным заклинаниям или еще чему-нибудь."
    m "Я понятия не имею, связано ли это с твоей магией."
    call sna_main("Угу...","snape_24")
    m "Правда? Так у тебя есть какие-нибудь тайные заклинания?"
    call sna_main("Есть...","snape_23")
    m "Какого рода?"
    call sna_main("Возможно, в это трудно поверить, но у меня было тяжелое детство.","snape_29")
    m "(Опять...)"
    call sna_main("...","snape_12")
    call sna_main("Во всяком случае, я пробовал создавать заклинания как способ направлять свои эмоции в то время.","snape_24")
    call sna_main("В девять лет я изобрел одно из своих любимых заклинаний, {b}Septum Sempra{/b}.","snape_02")
    call sna_main("Проклятие такой ужасной силы... Даже по сей день я по-прежнему вижу все лиц-","snape_20")
    m "Да, да, да, у тебя есть что-нибудь веселое?"
    call sna_main("Мог бы хотя бы позволить мне закончить историю.","snape_29")
    m "Ближе к делу."
    call sna_main("Как я уже говорил, я использовал заклинания как способ направить свои эмоции. Поэтому, когда я достиг полового созревания, заклинаний стало немного больше...","snape_24")
    call sna_main("Сексуального характера...","snape_13")
    m "Правда? Что они делали?"
    call sna_main("Это слишком унизительно...","snape_14")
    m "Давай, мужик! Не скрывай от меня."
    call sna_main("Я не собираюсь стоять здесь и объяснять тебе все.","snape_12")
    call sna_main("Просто возьми эту книгу.","snape_13")

    call sna_walk("mid","desk",2)

    call nar(">Снейп вручает тебе розовую кожаную книгу.")
    call sna_main("Я написал заметки, объясняющие, что делают заклинания, а также как их использовать.","snape_24")
    call sna_main("Имей в виду, что эта магия не совсем такая, какую здесь преподаем студентам.","snape_01")
    call sna_main("Она основана на гораздо более первобытной магии, основанной на эмоциях, а не на словах.","snape_02")
    call sna_main("Это потребует немного практики, прежде чем они смогут обуздать ее.","snape_10")
    m "Спасибо, даже если она не сможет наколдовать, тот факт, что ты их сделал, должен привлечь ее ко мне."
    call sna_main("Это все, Джинни?","snape_09")
    if daytime:
        m "(...)"
        jump snape_ready
    else:
        m "Я думаю... Если только ты не хочешь выпить?"
        call sna_main("Я думал ты никогда не спросишь","snape_02")

        jump snape_dates #Snape Genie drinking. Jumps to next day.



#TONKS TEACHER INTRO #Done
label astoria_tonks_intro: #occurs after you get the book from Snape
    call play_sound("knocking")
    "*тук* *Тук* *Свумп*"

    call play_sound("door")
    call ton_main("Сэр, у меня есть основания полагать, что на самом деле есть темный волшебник, действующий где-то на территории школы.","open","wide","wide","wide",xpos="right",ypos="base")
    m "Темный волшебник?"
    m "Конечно, ты вероятно хотела сказать негр-волшебник? (ох уж эта толерастия... афроамериканец-негр...)"
    call ton_main("Сейчас не время для твоих глупых шуток, профессор!","open","base","angry","mid")
    call ton_main("Недавно я обнаружила еще один случай непростительного проклятия, наложенного в моем районе.","open","base","raised","R")
    call ton_main("Но, что действительно меня беспокоит, так это то, что министерство не связалось со мной...","open","base","worried","down")
    call ton_main("Это должно означать, что волшебник скрывает себя в глобальной системе обнаружения заклинаний министерств.","open","base","raised","mid")
    call ton_main("Мы должны эвакуировать школу, пока их не поймают... Мы не можем рисковать жизнью студентов...","open","base","angry","mid")
    m "О... Я думаю, те заклинания, которые ты подхватила, могли быть связаны со мной.."

    stop music fadeout 1.0
    call ton_main("Не может быть...","base","wide","wide","wide")
    call ton_main("Вы темный волшебник???","open","wide","wide","wide")
    m "Говорю тебе, не думаю, что стоит так говорить..."

    call play_music("hitman")
    call ton_main("ЭТО НЕ ПОВОД ДЛЯ СМЕХА!","open","base","angry","mid")
    m "Я не \'темный\' волшебник! Заклинания происходят под моим строгим контролем."
    call ton_main("Вы хотите сказать, что позволяете студентам бросать непростительные проклятия? И скрываете это от Министерства?","open","wide","wide","wide")
    call ton_main("Вы в своем уме?","open","base","angry","mid")
    m "Как директор этой школы, я считаю, что обучение студентов - это мое дело, большое спасибо."
    call ton_main("Непростительные проклятия - мое дело, Дамблдор!","open","base","angry","mid")
    call ton_main("Я требую, чтобы вы объяснили, что происходит прежде, чем я вернусь в министерство и все им расскажу!","open","base","angry","R")
    m "(Дерьмо...)"
    m "Ладно..."
    m "Я обучал студентов..."
    call ton_main("Темным искусствам? Ты с ума сошел?","open","wide","wide","wide")
    m "Не волнуйся, я не позволю ей никого убить..."
    call ton_main("Ей? Кого именно ты тогда обучаешь?","open","base","angry","mid")
    m "Асторию Гринграсс. Я полагаю, вы встречались--"
    call ton_main("Астория? Вы имеете в виду, ту миленькую маленькую {p}леди...","base","base","raised","mid")
    call ton_main("Почему ты учишь ее проклятиям?","open","base","raised","R")
    m "Мисс Гринграсс обратилась ко мне с просьбой выучить несколько более продвинутых заклинаний."
    call ton_main("Так ты решил научить ее накладывать Imperio???","open","base","worried","mid")
    call ton_main("И если она накладывает Imperio под твоим руководством, кто тогда проклят?","open","base","raised","mid")
    call ton_main("Не думаю, что ты позволишь ей проклинать себя.","base","base","angry","mid")
    m "Помнишь свою племянницу?"
    call ton_main("{size=+2}СЬЮЗАН?{/size}","open","wide","wide","wide")
    call ton_main("Ты же не серьезно?!!! {p}В какой школе ты работаешь?","open","base","angry","mid")
    m "В магической?"
    call ton_main("...","base","base","angry","mid")
    call ton_main("Что вы с Асторией заставляете делать Сьюзан?","open","base","angry","mid")
    m "Ох... ну..."
    m "Танцевать как цыпленок"
    call ton_main("Ты правда думаешь, что я в это поверю?","open","base","angry","R")
    m "Стоило попробовать."
    call ton_main("Позволь мне прояснить ситуацию...","base","base","angry","R")
    call ton_main("Ты обучал студентов темным искусствам, скрывая свои действия от Министерства магии...","open","base","angry","mid")
    call ton_main("И управлял моей племянницей, чтобы кто-нибудь обучался?","open","base","angry","mid")
    call ton_main("Ты хоть представляешь, какие у тебя неприятности?","open","base","angry","mid")
    m "Это риторический вопрос?"
    call ton_main("Это означает, что те письма от мисс Грейнджер на самом деле говорили правду.","base","base","raised","R")
    m "Что за письма?"
    call ton_main("Несколько недель назад министерство получило официальную жалобу от мисс Грейнджер об оказании сексуальных услуг на территории Хогвартса.","open","base","raised","mid")
    call ton_main("Очевидно, что министерство проигнорировало ее. Я имею в виду, кто мог поверить, что знаменитый Альбус Дамблдор допустил подобное...","open","base","worried","R")
    call ton_main("Но теперь я в этом не уверена...","base","base","angry","mid")
    m "..."
    call ton_main("Значит, это действительно так?","open","base","raised","mid")
    call ton_main("Ты трахаешь своих студентов, Дамблдор?","open","base","angry","mid")
    call ton_main("Или ты просто покрываешь других учителей?","base","base","raised","mid")

    menu:
        "-Солгать-":
            m "Я никогда не позволю--"
        "-Сказать правду-":
            m "Все началось--"

    call ton_main("Мне все равно, в любом случае, ты попадешь в Азкабан на всю оставшуюся жизнь...","open","base","angry","mid")
    m "*gulp*"
    call ton_main("Если только...","open","base","raised","R")
    m "Что еще?"

    call play_music("hermione_theme")
    call ton_main("У вас есть свободная должность преподавателя, \"Защиты от Темных Искусств\"?","open","base","worried","mid")
    m "..."
    m "Что?"
    call ton_main("Тьфу... Ты же не думаешь, что мне нравится быть мракоборцем?","base","base","worried","R")
    call ton_main("Это просто постоянная напряженная работа...","open","base","angry","mid")
    call ton_main("Не говоря уже о часах.","open","base","base","up")
    call ton_main("И уровень смертности...","open","base","worried","down")
    call ton_main("Если бы я поняла преимущества работы учителем в Хогвартсе, я бы сразу записалась!","open","base","angry","mid")
    m "Преимущества?"
    m "Ты имеешь в виду торговлю услугами?"
    call ton_main("Нет, я имею в виду здравоохранение... Конечно, я имею в виду торговлю услугами, Дамблдор!","open","base","raised","mid")
    call ton_main("Я всегда предполагала, что вы со Снейпом не позволите держаться за руки в коридорах...","open","base","base","mid")
    call ton_main("Но если ты веселишься со своими студентами...","base","base","base","mid")
    call ton_main("Ну, скажем так, я хочу участвовать.","horny","base","raised","mid")
    m "(...)"

    g9 "Ты нанята!"
    m "Считай себя новым защитником-учителем древних или как там его..."
    call ton_main("Как насчет Квиррела?","open","base","raised","mid")
    m "Кого?"
    call ton_main("Нынешний профессор защиты от темных искусств...","open","base","base","R")
    m "О, хорошо... Я попрошу Снейпа разобраться с ним..."
    call ton_main("Значит, Снейп тоже в этом замешан?","open","base","raised","mid")
    m "Да..."
    call ton_main("Да... Я не думала, что этот унылый мешок знает, что такое веселье...","base","base","raised","R")
    call ton_main("Сколько платишь?","open","base","base","mid")
    m "Плачу?"
    call ton_main("Сколько ты платишь своим ученикам, чтобы они дурачились?","base","base","base","mid")
    m "О... Это зависит от того, что ты хочешь увидеть."
    call ton_main("Сколько стоит приватный танец?","horny","base","raised","mid")
    m "Опять же, это зависит от студента."
    call ton_main("...","base","base","base","mid")
    m "Даже не знаю, я бы сказал о 25 очках."
    call ton_main("Постой...","open","wide","wide","wide")
    call ton_main("Ты платишь очками?","open","base","raised","mid")
    m "В основном."
    call ton_main("Так тебе удалось убедить этих девушек предложить себя за кучу воображаемых очков, которые ничего не значат?","open","base","angry","mid")
    m "Прям как рулетки и лутбоксы в интернете..."
    call ton_main("Что?","base","base","angry","mid")
    m "В любом случае, ты не можешь просто попросить приватный танец прямо сейчас, ты должна сначала их подвести к этому."
    call ton_main("Это как?","base","base","raised","mid")
    m "Сначала большинство из них не собирается делать подобное, что ты их попросишь..."
    m "Ты должна медленно завоевать их доверие с течением времени и начинать с малого..."
    call ton_main("О, правда... Разве я не могу немного схитрить?","open","base","worried","L")
    m "..."
    m "Просто не торопись, хорошо? В любом случае я уверен, что ты найдешь милого мальчика, который будет готов сделать все, что ты захочешь."
    call ton_main("...А что если я захочу девушку?","horny","base","raised","mid")
    g4 "(...!)"
    m "Все, что захочешь..."
    call ton_main("А что если мне нужна конкретная девушка?","base","base","raised","mid")
    m "Конкретная?"
    call ton_main("Астория Гринграсс.","horny","base","angry","mid")
    m "Астория? Разве она не слишком--"
    call ton_main("Она идеальна! Она такая милая и невинная... Не могу дождаться, когда приласкаю ее!","horny","base","worried","mid")
    call ton_main("Мммм... Держу пари, она на вкус как абрикос...","tongue_wide","base","base","up")
    m "..."
    m "Я не уверен, что она будет готова к этому, если честно--"
    call ton_main("Тебе лучше загладить свою вину...","base","base","raised","mid")
    call ton_main("Или мне придется рассказать обо всем этом министерству...","open","base","angry","mid")
    m "Славненько..."
    call ton_main("Хорошо... Я ожидаю, что она прийдет ко мне в ближайшее время.","horny","base","raised","mid")
    m "..."
    call ton_main("Если это все, то я пойду.","base","base","base","mid")
    m "Хорошо..."
    hide screen tonks_main
    with d3
    call nar(">Тонкс поворачивается и покидает твой кабинет.")
    m "..."
    m "Я только что стал сутенером?"

    call give_reward(">Ты разблокировал возможность вызывать Тонкс в свой кабинет.","images/store/tonks_unlock_01.png")
    $ tonks_busy = True


    jump day_main_menu



#ASTORIA TONKS FAVOUR INTRO. #Done
label astoria_book_intro: #Tell Astoria that you have a book of spells as well as the pimping with Tonks

    call ast_main("Итак, ты наконец-то вспомнил крутые заклинания?","grin","angry","angry","mid",xpos="mid",ypos="base",trans="fade")
    call ast_main("Или тебе сейчас тяжело вспоминать?","tongue_silly","angry","angry","mid")
    m "Я хочу, чтобы ты знала, что у меня есть целая книга, полная новых заклинаний для тебя."
    call ast_main("Правда?","happy","wide","wide","wide")
    call ast_main("Может, ты не такой уж и тупой, в конце концов!","grin","happyCl","base","mid")
    m "Ты хочешь их выучить или нет?"
    call ast_main("Конечно!","grin","base","base","mid")
    call ast_main("Мне пришлось провести весь день, слушая болтовню Макгонагалл о важности заклинания преображения.","pout","angry","angry","R")
    call ast_main("Все превращались в тупую желтую крысу!","upset","ahegao","ahegao","ahegao")
    call ast_main("Я хочу научиться чему-нибудь веселому!","pout","narrow","narrow","down")
    m "В таком случае, мне нужно, чтобы ты кое-что для меня сделала."
    call ast_main("Мне позвать Сьюзан сюда, чтобы ты снова пялился на ее тупое жирное вымя?","grin","angry","angry","mid")
    call ast_main("На этот раз я ее никуда не отправлю...","open","base","base","R")
    call ast_main("Пока ты нехорошо себя ведешь!","clench","angry","angry","angry")
    m "Как бы заманчиво это ни было, но не в этом дело."
    call ast_main("Хорошо, а в чем тогда?","open","base","base","L")
    call ast_main("Ты же не ждешь, что я стану танцевать для тебя?","upset","wink","worried","mid")
    m "(Всему свое время...)"
    m "Нет, это связано с Нимфоманкой Тонкс или как ее там звали..."
    call ast_main("Мракоборец!","disgust","wide","wide","wide")
    m "(Технически, она теперь твоя учительница...)"
    call ast_main("Ты же не собираешься отправить меня в Азкабан?","scream","closed","worried","mid")
    call ast_main("Ты обещал!","disgust","narrow","worried","down")
    m "Никто не посылает тебя в Азкабан."
    call ast_main("Тогда почему она хочет меня видеть?","pout","angry","angry","R")

    menu:
        "-Сказать правду-":
            m "Ну, ты же знаешь, как некоторые из учителей здесь любят присуждать бонусные очки студентам-"
            call ast_main("Ты имеешь в виду личные услуги?","upset","base","base","mid")
            m "Ты о них знаешь?"
            call ast_main("Конечно, мне известно. Половина девушек в Слизерине зарабатывают дополнительные очки у Снейпа.","pout","base","base","R")
            call ast_main("Некоторые из них даже заработали немного от эскорт услуг","disgust","narrow","base","down")
            with hpunch
            call nar("Астория дрожит при одной мысли об этом.")
            call ast_main("Но я никогда не делала ничего подобного, у меня мурашки по коже от Снейпа...","pout","angry","angry","L")
            call ast_main("(Плюс ему нравятся только девушки с большими сиськами...)","pout","angry","angry","R")
        "-Солгать-":
            m "Она просто хочет задать тебе несколько вопросов."
            call ast_main("Например?","upset","wink","worried","mid")
            m "Я не уверен, тебе придется подождать и увидеть..."
            call ast_main("Я не хочу!","pout","angry","angry","R")
            m "Ну давай же... Она может даже заплатить тебе несколько очков после этого..."
            call ast_main("Несколько очков? Вы имеете в виду...","scream","wide","wide","wide")
            call ast_main("Мне придется продаться за очки, [ast_genie_name]?!","disgust","wide","wide","mid")
            m "Продаться? Я понятия не имею, о чем ты говоришь..."
            call ast_main("[ast_genie_name]! Все знают о торговле услугами здесь, в школе.","open","angry","angry","mid")
            call ast_main("У меня есть три подруги, которые ублажают профессора Снейпа!","disgust","narrow","narrow","R")
            m "Правда?"
            call ast_main("Да, хотя все они шлюхи... Я бы никогда так не поступила.","pout","narrow","narrow","R")
            call ast_main("(Плюс Снейпу нравятся только девушки с большими сиськами...)","pout","ahegao","ahegao","ahegao")

    m "Ну, мы не сможем практиковать эти новые заклинания, пока ты не отправишься туда."
    call ast_main("Правда? Ты имеешь в виду, что я должна увидеться с этой жуткой старушкой...","pout","angry","angry","R")
    m "Она не настолько старая!"
    call ast_main("Возможно для тебя... !","pout","angry","angry","down")
    call ast_main("Она не выглядит древней!","pout","angry","angry","mid")
    m "Ты тоже будешь выглядеть древней после 30 лет в Алаказаме (прим. Алаказам - яндекс выдал, название Покемона), если не пойдешь туда!\nСЕЙЧАС ЖЕ!"
    call ast_main("Что? Но ты же обещал! [ast_genie_name]!!!","scream","wide","wide","mid")
    m "Я обещал тебе, что не отправлю! Я никогда не говорил, что Тонкс не посадит тебя в Алькатрас вместо меня!"
    call ast_main("Не думаю, что ее так зовут\n(И не правильная тюрьма...)","worried","narrow","narrow","L")
    m "Как бы там ни было, просто отправляйся туда!"
    m "Она не сделает с тобой ничего странного. Просто поговорит..."
    call ast_main("Ты уверен?","worried","closed","worried","mid")
    m "Что плохого может случиться на самом деле?"
    m "Боишься, что она заглянет тебе под юбку?"
    call ast_main("[ast_genie_name]!","scream","wide","wide","wide")
    m "Просто иди поздоровайся с ней."
    m "Потом вернешься сюда и расскажешь, что случилось."
    call ast_main("Мне обязательно?","disgust","closed","worried","mid")
    m "Только если ты хочешь попрактиковаться в новом крутом заклинании..."
    call ast_main("Арх... Ладно.","pout","angry","angry","R")
    call ast_main("Но ей лучше держать свои морщинистые старые руки при себе.","open","closed","base","mid")
    g9 "Я тебе покажу, морщинистые старые руки."
    call nar(">Ты протягиваешь руку, чтобы схватить ее.")
    call ast_main("ААА!-- Хорошо, уже иду!","scream","closed","worried","mid")
    hide screen astoria_main
    call play_sound("door")
    with d3
    pause.2

    $ astoria_busy = True
    $ tonks_busy = True

    call nar(">Астория выбегает за дверь, хихикая.")

    jump day_main_menu
