

label hg_pf_TimeForAnal: #LV.8 (Whoring = 21 - 23)
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_TimeForAnal_OBJ.points == 0:
        m "{size=-4}(Должен ли я попросить ее заняться анальным сексом со мной?){/size}"
        menu:
            "\"(Да, давай!)\"":
                pass
            "\"(Не сейчас.)\"":
                jump silver_requests

    if hg_ballDress_OBJ.purchased:
        m "\"(Попросить ее переодеться?)\""
        menu:
            "\"(Да, давай!)\"":
                m "[hermione_name], прежде чем я попрошу об услуге, переоденься."
                call her_main("Во что?","open","worriedL")
                m "В свое бальное платье."
                if whoring >= 22:
                    call her_main("Что?","scream","wide")
                    her "Вы подарите мне бальное платье?"
                    m "Да, но тебе придется его заслужить."
                    call her_main("Конечно!","angry","wide")
                    call her_main("Я пошла переодеваться!","base","baseL",cheeks="blush")
                    call play_sound("door") #Sound of a door opening.
                    call set_hermione_outfit(hg_ballDress_OBJ)
                    pass
                else:
                    jump too_much
            "\"(Не сейчас.)\"":
                pass

    $ genie_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "sex_slow_ani"

    #Intro
    if hg_pf_TimeForAnal_OBJ.points == 0:
        m "[hermione_name]..."
        call her_main("[genie_name]..?","annoyed","suspicious")
        m "Насколько ты знакома с термином \"Анальный секс\"?"

        if whoring < 21:
            jump too_much

        call her_main("90 очков...","annoyed","annoyed")
        m "Что?"
        call her_main(".............................","disgust","glance")
        m "Ну, а за 90 очков?"
        hide screen hermione_main

        label lucky_guess:

        call blkfade
        stop music fadeout 1.0

        call her_head("...........","annoyed","worriedL")
        m "Давай посмотрим..."
        call her_head(".................","angry","worriedCl",emote="05")
        m "Хм..."
        call her_head("!!!","angry","wide")
        g4 "Ох, не входит!"
        call her_head("Ай!","mad","worriedCl",tears="soft_blink")
        m "Просто постарайся немного расслабиться, хорошо?"
        call her_head("Я пытаюсь!","angry","base",tears="soft")
        m "Хорошо, что если я сделаю так..?"
        call her_head("Ай! Что вы делаете, [genie_name]?","mad","worriedCl",tears="soft_blink")
        m "Это тоже не работает..."
        m "Хм..."
        m "Хорошо, я знаю, что мы должны сделать."

        menu:
            m "..."
            "\"Я плюну на него и засуну!\"":
                call play_music("playful_tension") # SEX THEME.
                call her_head("Засунете, [genie_name]?!","angry","wide")
                $ renpy.play('sounds/spit.mp3') #Sound of spiting.
                g4 "*ПЛЕВОК!*"
                call her_head("Eeeeeew!","scream","worriedCl")
                call her_head("Нет, [genie_name], подождите! Может быть, если я просто расслаблю--","open","base")
                m "Уже не нужно!"
                with hpunch
                call her_head("АХ!","angry","base",tears="soft")
                call her_head("Ай! Ай! Ай!","mad","worriedCl",tears="soft_blink")
                g4 "Почти!"
                call her_head("Нет, вы делаете мне больно! Вы делаете мне больно!","scream","worriedCl")
                g4 "Почти! Ну же, почти!"
                call her_head("Aх! Это же больно!","scream","worriedCl")
                g4 "Заткнись, [hermione_name]! Я купил услугу!"
                g4 "Твой анус такой тугой, что его невозможно трахать!"
                call her_head("Тогда остановитесь, пожалуйста!","mad","worriedCl",tears="soft_blink")
                m "Нет! Нужно чтобы ты немного расслабила свою попку!"
                call her_head("Но я не хочу!","mad","worriedCl",tears="soft_blink")
                m "Серьезно? И как ты видишь, чтобы люди трахали тебя в задницу?"
                call her_head("Какие люди?","shock","worriedCl")
                g4 "Ты знаешь... Люди."
                g4 "Ах, черт... Моему члену тоже больно."
                call her_head("Остановитесь тогда! Остановитесь, [genie_name]!","open","worriedCl")
                call her_head("Я передумала! Мне не нужно 90 очков!")
                g4 "Я думаю, что уже почти..."

                $ renpy.play('sounds/gltch.mp3')
                with hpunch
                with kissiris
                call her_head("{size=+5}ААААХХХ!!!{/size}","scream","wide")
                g4 "ДА!!!"
                call her_head("ААААААААААААААХХХ!","scream","wide")
                g4 "Тогда давай накачаем тебе полную попку спермы, не так ли?"
                call her_head("Да... Пожалуста, я хочу побыстрее закончить это...","scream","worriedCl",cheeks="blush",tears="crying")


                call her_chibi("hide") #HERMIONE
                hide screen genie
                show screen chair_left

                $ genie_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "sex_slow_ani"
                show screen g_c_u

                if use_cgs:
                    hide screen candlefire
                    $ face_on_cg = True
                    $ ccg_folder = "herm_sex"
                    $ ccg1 = "blank"
                    $ ccg2 = "blank"
                    $ ccg3 = "blank"
                    call her_head("","shock","baseL",cheeks="blush",tears="soft")
                    show screen ccg

                hide screen blktone
                hide screen bld1
                hide screen blkfade
                with fade
                call ctc


                #SCHUSH!
                g4 "Ах... Ты хочешь, чтобы это закончилось быстрее?"
                g4 "Тогда помоги мне!"
                call her_head("*Всхлип!* Как?","shock","baseL",cheeks="blush",tears="soft")
                g4 "Ты знаешь..."
                call her_head("ОХ...","shock","baseL",cheeks="blush",tears="soft")
                #$ ccg2 = 6
                call her_head("Я шлюха?","clench","worried",cheeks="blush",tears="soft")
                g9 "Да, ты шлюха!"
                call her_head("*Всхлип!*  Я шлюха...","angry","suspicious",cheeks="blush")
                call her_head("Я люблю сосать член...")
                call her_head("И теперь меня разрывают изнутри на куски... *Всхлип!*","angry","dead",cheeks="blush",tears="crying")
                g4 "Да! Да!"
                g4 "Ах! Да!"
                call her_head("Нет! Он становится только больше?! Мне страшно!","open","surprised",cheeks="blush",tears="messy")
                g4 "АХ!"

            "\"Сначала пососи его. Смажь его слюной!\"":
                call her_head("Ох... Хорошо...","open","base")
                call play_music("playful_tension") # SEX THEME.

                #SUCKING
                call her_chibi("hide")
                hide screen genie
                show screen chair_left

                $ genie_chibi_xpos = -10 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "blowjob_ani"
                show screen g_c_u

                hide screen blktone
                hide screen bld1
                call hide_blkfade
                call ctc

                call her_head("*Slurp!* *Slurp!* *Slurp!*")
                m "Да... хорошо..."
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Отлично, думаю, этого достаточно. Теперь на стол."
                call blkfade

                #ON THE DESK
                call her_head(".............","open","base")
                g4 "Да! Почти!"
                call her_head("Ouch!","scream","worriedCl")
                m "Расслабься. Уже почти."

                $ renpy.play('sounds/gltch.mp3')
                with hpunch
                with kissiris
                call her_head("{size=+5}ААААХХХ!!!{/size}","scream","wide")
                g4 "ДА!!!"
                call her_head("Моя... моя...","scream","wide")
                call her_head("Больно!","shock","worriedCl")
                g4 "Тогда давай накачаем тебе полную попку спермы, не так ли?"
                call her_head(".....................","angry","suspicious",cheeks="blush")

                # SEX
                call her_chibi("hide") #HERMIONE
                hide screen genie
                show screen chair_left

                $ genie_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "sex_slow_ani"
                show screen g_c_u

                if use_cgs:
                    hide screen candlefire
                    $ face_on_cg = True
                    $ ccg_folder = "herm_sex"
                    $ ccg1 = "blank"
                    $ ccg2 = "blank"
                    $ ccg3 = "blank"
                    call her_head("","shock","baseL",cheeks="blush",tears="soft")
                    show screen ccg

                hide screen blktone
                hide screen bld1
                hide screen blkfade
                with fade
                call ctc

                call her_head(".....................","shock","baseL",cheeks="blush",tears="soft")
                m "Ты в порядке, шлюха?"
                call her_head("Aх... Вы... расстягиваете мне все изнутри... [genie_name].","clench","worried",cheeks="blush",tears="soft")
                call her_head("И мне все равно больно...","angry","suspicious",cheeks="blush")
                m "Хм..."
                m "Возможно, не достаточно смазки...?"
                m "Давай, [hermione_name]. Пососи мой член еще раз."
                call her_head("Что? Но...","clench","worried",cheeks="blush",tears="soft")
                call her_head("Но он грязный... Он только что побывал там...","shock","baseL",cheeks="blush",tears="soft")
                m "Да, он был внутри, но это не значит, что он стал грязный."
                m "Давай, [hermione_name]. Пососи же мой член еще раз."
                call her_head("...........","shock","baseL",cheeks="blush",tears="soft")
                call blkfade

                #SUCKING
                hide screen ccg
                $ face_on_cg = False
                hide screen hermione_face
                call h_update_hair
                call her_chibi("hide")
                hide screen genie
                show screen chair_left

                $ genie_chibi_xpos = -10 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "blowjob_ani"
                show screen g_c_u

                hide screen blktone
                hide screen bld1
                call hide_blkfade
                call ctc

                call her_head("*Slurp!* *Slurp!* *Slurp!*",xpos="base",ypos="base")
                m "Да... хорошо..."
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Может ты попробуешь свою задницу на вкус на моем члене?"
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Хорошо, этого достаточно."
                call blkfade

                # SEX
                call her_chibi("hide") #HERMIONE
                hide screen genie
                show screen chair_left

                $ genie_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "sex_slow_ani"
                show screen g_c_u

                if use_cgs:
                    hide screen candlefire
                    $ face_on_cg = True
                    $ ccg_folder = "herm_sex"
                    $ ccg1 = "blank"
                    $ ccg2 = "blank"
                    $ ccg3 = "blank"
                    call her_head("","shock","baseL",cheeks="blush",tears="soft")
                    show screen ccg

                hide screen blktone
                hide screen bld1
                hide screen blkfade
                with fade
                call ctc

                call her_head("Aх...","shock","baseL",cheeks="blush",tears="soft")
                m "Уже лучше?"
                call her_head("Все еще больно...","clench","worried",cheeks="blush",tears="soft")
                call her_head("Но я думаю, что все будет хорошо...")
                m "Я пока не буду торопиться...."
                call her_head("Aх... Спасибо, [genie_name].","angry","suspicious",cheeks="blush")
                m "Oх... да... это здорово..."
                call her_head("...........","shock","baseL",cheeks="blush",tears="soft")
                m "Oх... Такая тугая..."
                call her_head("................","shock","down_raised",cheeks="blush",tears="crying")
                m "Почему ты молчишь? [hermione_name]?"
                call her_head("Потому что очень больно...","clench","worried",cheeks="blush",tears="soft")
                call her_head("И я просто хочу, чтобы вы кончили быстрее, [genie_name]...")
                m "Так ты подавляешь свои крики боли?"
                call her_head("Да [genie_name]. *Всхлип!*","angry","dead",cheeks="blush",tears="crying")
                m "Не делай этого."
                m "Рыдай, кричи и плачь столько, сколько хочешь!"
                call her_head("Н-но--","clench","worried",cheeks="blush",tears="soft")
                m "Это заставит меня кончить быстрее."
                call her_head("Серьезно? *Всхлип!*","angry","dead",cheeks="blush",tears="crying")
                call her_head("*Всхлип!* Это больно! *всхлип!* Это очень больно! *Вхлип!*","shock","baseL",cheeks="blush",tears="soft")
                m "Да, да..."
                call her_head("*Всхлип!*","angry","suspicious",cheeks="blush",tears="messy")
                m "Бедный маленький ребенок..."
                m "Большой, злой дяденька насилует твою задницу!"
                call her_head("*Всхлип!* Да! *Всхлип!*","scream","suspicious",cheeks="blush",tears="messy")
                g4 "Ах!"
                call her_head("Нет, мне страшно! *Всхлип!*","scream","worriedCl",cheeks="blush",tears="messy")

        menu:
            "-Кончить в Гермиону-":
                g4 "Ах!"
                call her_head("Нет! AХ!","scream","wide")
                call cum_block
                g4 "{size=+15}АХ!!!!!!!!!!!!!!!!{/size}"

                $ g_c_u_pic = "sex_cum_in_ani"
                hide screen bld1
                with d3

                call cum_block
                call ctc

                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"

                call her_head("AХ! ОН НАПОЛНЯЕТ МЕНЯ!{image=textheart}{image=textheart}{image=textheart}","open","surprised",cheeks="blush",tears="messy")
                g4 "Да, ты шлюха! Да!"
                call her_head("Это больно, больно!","angry","suspicious",cheeks="blush",tears="messy")
                g4 "Заткнись!"
                with hpunch
                call her_head("Нет, я уже полная! Хватит кончать, чертов ублюдок!","scream","surprised",cheeks="blush",tears="messy")
                g4 "Заткнись нахер, шлюха! Я еще не закончил!"
                call her_head("Нет! Пожалуйста! Мой живот! Я лопну!","scream","suspicious",cheeks="blush",tears="messy")
                g4 "АХ!"
                call her_head("Нет, думаю, меня сейчас стошнит....","open","surprised",cheeks="blush",tears="messy")
                with hpunch
                play sound "sounds/burp.mp3"
                call her_head("{size=+7}*ОТРЫЖКА!*!!!!!{/size}","full","surprised",tears="messy")
                call her_head(".......................","full","base",tears="messy")
                call her_head(".............")
                $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                call her_head("{size=+7}*ГЛОТОК!*{/size}","cum","worriedCl")
                call her_head("*Всхлип!* Я НЕНАВИЖУ ВАС...","angry","suspicious",cheeks="blush",tears="messy")
                call her_head("{size=+5}Я НЕНАВИЖУ ВАС И ВАШ ПРОТИВНЫЙ СТАРЫЙ ЧЛЕН!{/size}","scream","angry",cheeks="blush",tears="messy")
                call her_head("{size=+5}НЕНАВИЖУ ВАС! ВЫ СЛЫШИТЕ МЕНЯ?!{/size}")
                g4 "Ах... Заткнись, шлюха!"
                call her_head("*Всхлип!* *Всхлип!*...","angry","suspicious",cheeks="blush",tears="messy")

                # AFTER CUM INSIDE
                hide screen bld1
                with d3
                call ctc

                $ g_c_u_pic = "ani_her_sex_cum_inside_blink"

                call her_head("*Всхлип!*...","angry","dead",cheeks="blush",tears="crying")
                m "Фух!... Я думаю, что я закончил."
                m "Ты в порядке?"
                call her_head("Да... *Всхлип!*","angry","dead",cheeks="blush",tears="crying")
                m "Ты плачешь?"
                call her_head("Моя попка болит, но я в порядке, [genie_name]...","angry","dead",cheeks="blush",tears="crying")
                m "Ты упорно взяла мой член..."
                call her_head("Спасибо [genie_name]...","angry","dead",cheeks="blush",tears="crying")
                hide screen bld1
                with d3
                call ctc

                call blkfade
                $ face_on_cg = False
                hide screen hermione_face
                call h_update
                call h_update_hair

                call her_head("Прошу прощения за то, что я сказала, что ненавижу вас, [genie_name]...","base","baseL",cheeks="blush",tears="mascara",xpos="base",ypos="base")
                call her_head("И ваш член не противен...",cheeks="blush",tears="mascara")
                call her_head("Я не знаю, что нашло на меня...","grin","concerned",cheeks="blush",tears="mascara")
                g9 "Мой член!"
                call her_head("Я полагаю, что, когда вы называете меня \"шлюхой\". На самом деле я знаю, что это не так...","grin","concerned",cheeks="blush",tears="mascara")
                m "Да, конечно..."
                m "Все еще болит?"
                call her_head("Немного...","open","concerned",cheeks="blush",tears="mascara")
                call her_head("Я также чувствую полноту и тепло внутри...","grin","closed",cheeks="blush",tears="mascara")
                m "Ты планируешь удержать все внутри? Все что я накончал."
                call her_head("Да...","grin","glance",cheeks="blush",tears="mascara")

                if daytime:
                    call her_head("Надеюсь, моя попа не начнет протекать во время занятий...",cheeks="blush",tears="mascara")
                else:
                    call her_head("Я надеюсь, моя попа не начнет протекать прежде, чем я доберусь до своей комнаты...",cheeks="blush",tears="mascara")

                m "Что ж, удачи тебе."
                call her_head("Могу я получить очки?","grin","closed",cheeks="blush",tears="mascara")

            "-Вытащить и кончить на нее-":
                $ g_c_u_pic = "sex_cum_out_ani"
                hide screen bld1
                with d3

                call cum_block
                call ctc

                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"

                call her_head("Aх...{image=textheart}{image=textheart}{image=textheart}","silly","dead")
                g4 "Да!!! Твоя попка!"
                call her_head("Aх... Горячо!","silly","ahegao")
                hide screen bld1
                with d3
                call ctc

                call blkfade

                call blkfade
                $ face_on_cg = False
                hide screen hermione_face
                call h_update
                call h_update_hair

                m "Что ж, я закончил... Можешь убраться с моего стола.."
                call her_head("Да, [genie_name]...","silly","worried",cheeks="blush",tears="soft",xpos="base",ypos="base")
                m "Ты хорошо себя чувствуешь?"
                call her_head("Да, [genie_name]. Все еще немного больно, но...","shock","baseL",cheeks="blush",tears="soft")
                m "Что но?"
                call her_head("Но в хорошем смысле... [genie_name].","silly","worried",cheeks="blush",tears="soft")
                m "В хорошем смысле?"
                g9 "Хех... Ты милая, маленькая шлюшка."
                call her_head("Могу я получить очки, [genie_name]?","silly","worried",cheeks="blush",tears="soft")

    #Second time event.
    elif hg_pf_TimeForAnal_OBJ.points == 1:
        m "[hermione_name]?"
        call her_main("[genie_name]?","soft","base")
        m "Сегодня я куплю у тебя одну услугу...."
        call her_main(".............","open","suspicious")
        m "Угадай, какая будет услуга?"
        m "У тебя три попытки."
        call her_main("...........","annoyed","frown")
        call her_main("Анальный секс?","disgust","glance")
        g4 "Чт..........?!"
        g4 "Как ты...?"
        call her_main("Просто повезло, [genie_name]...","angry","angry")
        m "Иногда ты меня пугаешь, [hermione_name]..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        jump lucky_guess

    #Third time event.
    elif hg_pf_TimeForAnal_OBJ.points >= 2:
        m "Как насчет анального секса, [hermione_name]?"
        call her_main("Конечно, [genie_name].","base","ahegao_raised")
        g9 "Иди ко мне, маленькая шлюха!"

        hide screen hermione_main
        call blkfade

        stop music fadeout 1.0

        call her_head("........","annoyed","worriedL")
        m "Хм..."
        call her_head("...........","open","base")
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        call her_head("Ааааааххх....{image=textheart}","scream","wide")
        g4 "Oх, да-а!"
        call her_head("Aх...","soft","ahegao")
        m "Похоже, твоя попка стала более приветливой, [hermione_name]."
        call her_head("Aх... До сих пор болит.","base","glance")
        call her_head("И, пожалуйста, называйте меня \"шлюхой\", [genie_name].","base","suspicious")
        g4 "Ах! ты шлюха! У тебя всегда получается сказать то, что я хочу услышать!"

        call her_chibi("hide")
        hide screen genie
        show screen chair_left

        $ genie_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "sex_ani"
        show screen g_c_u

        if use_cgs:
            hide screen candlefire
            $ face_on_cg = True
            $ ccg_folder = "herm_sex"
            $ ccg1 = "blank"
            $ ccg2 = "blank"
            $ ccg3 = "blank"
            call her_head("","open","closed")
            show screen ccg

        hide screen blktone
        hide screen bld1
        call hide_blkfade
        call ctc

        call play_music("playful_tension") # SEX THEME.

        #INSERTION
        call her_head("Aх... AХ...","open","closed")
        call her_head("Aх...")
        call her_head("[genie_name]?","base","glance")
        m "Да, шлюха?"
        call her_head("Эм...","angry","base")
        call her_head("Вы возьмете меня за муж, [genie_name]?","angry","down_raised")
        with hpunch
        g4 "{size=+9} ЧТО?!{/size}"
        g4 "Не говори мне, что ты беременна, [hermione_name]!"
        call her_head("Я не могла забеременеть через анальный секс, [genie_name]...","angry","wink")
        m "Тогда что это за разговоры о браке?"
        call her_head("Вы меня не поняли [genie_name].","angry","base")
        call her_head("Я хотела сказать, вы бы женились на девушке {size=+5}вроде меня{/size}?","angry","down_raised")
        call her_head("Я бы никогда не спрашивала о предложении мужчину с его членом в моей попке, [genie_name]...","angry","worriedCl",emote="05")
        m "Хорошо. Потому что в этом случае не возможно сказать \"нет\"."
        call her_head("Aх{image=textheart}...","open","closed")
        call her_head("Что я хотела... Ах{image=textheart} {w} ...Сказать... Ах{image=textheart}... {w}...Вы думаете, кто-нибудь, когда-нибудь захочет... ах{image=textheart}... {w} ...Взять в жены такую девушку как я?","angry","down_raised")
        m "А?"
        call her_head("Я имею в виду, что все, что со мной происходило в последнее время... aх{image=textheart}...","angry","down_raised")
        call her_head("Я не могу не чувствовать, что стала более развратной... даже очень развратной.")
        call her_head("И ни сколечки целомудрия...")
        call her_head("Кому будет нужна такая жена?","angry","base")

        menu:
            m "..."
            "\"Я бы запросто на тебе женился!\"":
                call her_head("Что?","open","base")
                m "Ну, конечно, чисто гипотетически, ..."
                call her_head("...Конечно...{image=textheart}","base","baseL")
                call her_head("..............","base","squint")
                call her_head("Но почему вы так говорите?, [genie_name]?","soft","base")
                m "А?"
                m "Что ты имеешь под словом \"почему\", шлюха?"
                m "Ты молодая и привлекательная..."
                m "Большие сиськи и мокрая киска..."
                call her_head("Aх...{image=textheart}","open","closed")
                m "Однажды, ты сделаешь очень счастливым кого-то, шлюха.."
                m "Эм, я имел в виду не шлюха, [hermione_name]."
                call her_head("Нет, \"шлюха\" - хорошо. Называйте меня так, [genie_name].","silly","ahegao")
                m "Вот, видишь? Ты отличная невеста, говорю тебе, шлюха..."
                call her_head("Aх...{image=textheart} Спасибо, [genie_name].","angry","dead",cheeks="blush",tears="crying")
                m "А?"
                m "Ты плачешь?"
                label among_other_things:
                call her_head("Вообще-то, [genie_name]...{image=textheart}{image=textheart}{image=textheart}","silly","dead")
                m "Вообще-то?"
                call her_head("Я кончаю [genie_name]...{image=textheart}{image=textheart}{image=textheart}","open_wide_tongue","ahegao")
                g4 "Ах! Мой член!"
                g4 "Расслабься немного, хорошо?"
                call her_head("НО Я КОНЧАЮ!{image=textheart}{image=textheart}{image=textheart}","open","worriedCl")
                g4 "Отлично! Шлюха!"
                with hpunch
                call her_head("{size=+7}Aх-aх-aхa!!! Я кончаю!!!{/size}","scream","wide")
                g4 "{size=+7}Ах!{/size}"

            "\"Брак для тебя не подходит..\"":
                call her_head("Я так и думала...","shock","down_raised",cheeks="blush",tears="crying")
                m "Oх... Я просто обожаю твой узенький анус!!"
                call her_head(".....................","angry","dead",cheeks="blush",tears="crying")
                call her_head("Да... После всего, что мне пришлось сделать для своего факультета...")
                call her_head("...никто никогда не захочет меня...","angry","suspicious",cheeks="blush",tears="messy")
                m "Ох, все очень будут хотеть тебя!"
                call her_head("Что? Но вы сказали...","open","surprised",cheeks="blush",tears="messy")
                m "Брак, [hermione_name]. Брак не для тебя."
                m "Но как шлюха, удовлетворяющая мужчин - ты шикарна!"
                call her_head("Правда?","open","surprised",cheeks="blush",tears="messy")
                m "Ты сомневаешься во мне?!"
                m "Молодая, горячая и распутная. Ты можешь заполучить любого мужчину, какого захочешь!"
                m "Или волшебника...."
                call her_head("Я думаю, что вы можете быть правы, [genie_name].","base","concerned",cheeks="blush",tears="soft")
                m "Я знаю, что я прав, шлюха."
                m "Пошевели задницей немного."
                call her_head("Вам нравится?","silly","worried",cheeks="blush",tears="soft")
                m  "Да, хорошая шлюха."
                call her_head("Я шлюха, да?","silly","dead")
                m "Ты только что продала мне свою попку за 90 очков. Как бы ты это назвала?"
                call her_head("Да, да...{image=textheart} Я шлюха...{image=textheart}","silly","worried",cheeks="blush",tears="soft")
                m "Ты плачешь?"
                jump among_other_things

        menu:
            g4 "!!!"
            "-Кончить в нее-":
                hide screen bld1
                with d3
                $ g_c_u_pic = "sex_cum_in_ani"

                call cum_block
                call ctc

                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"

                call her_head("!!!","scream","wide")
                m "Да! Ах!"
                call her_head("Aх!{image=textheart} Вы меня наполняете!{image=textheart} Я чувствую это!{image=textheart}","silly","ahegao")
                m "Заткнись, шлюха!"
                call her_head("Aх! Я ШЛЮХА!!!!{image=textheart}{image=textheart}{image=textheart}","scream","worriedCl",cheeks="blush",tears="crying")
                m "Ах!"
                call her_head("Aх...{image=textheart} ваша сперма, [genie_name]...{image=textheart}","open","surprised",cheeks="blush",tears="messy")
                m "Да, да..."
                call her_head("Aх...{image=textheart}","angry","suspicious",cheeks="blush",tears="messy")
                m "......"
                hide screen bld1
                with d3
                call ctc

                call blkfade

            "-Кончить на нее-":
                hide screen bld1
                with d3
                $ g_c_u_pic = "sex_cum_out_ani"

                call cum_block
                call ctc

                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"

                call her_head("Aх-aхa! Вы кончаете! {image=textheart}{image=textheart}{image=textheart}","silly","dead")
                g4 "{size=+7}Да, шлюха!{/size}"
                call her_head("Aх, я тоже! Я тоже!","scream","worriedCl",cheeks="blush",tears="messy")
                g4 "{size=+7}Ебаная шлюшка!{/size}"
                call her_head("Aх...{image=textheart} ваша сперма...{image=textheart}","angry","dead",cheeks="blush",tears="crying")
                call her_head("Я ей сыта...{image=textheart}{image=textheart}{image=textheart}")
                g4 "Да!!!"
                call her_head("Aх... Горячо!","silly","ahegao")
                hide screen bld1
                with d3
                call ctc

                call blkfade

        #Ending
        $ face_on_cg = False
        call h_update_hair

        m "Что ж, это было здорово..."
        call her_head("Aх-хa...{image=textheart} aх...{image=textheart}","grin","dead",cheeks="blush",tears="messy",xpos="base",ypos="base")
        m "Ты в порядке, [hermione_name]?"
        call her_head("Я думаю... Я не уверена...","grin","dead",cheeks="blush",tears="messy")
        call her_head("Я думаю, что все еще могу кончить, [genie_name].","grin","dead",cheeks="blush",tears="messy")
        call her_head("Или нет...","grin","dead",cheeks="blush",tears="messy")
        call her_head("Все как в тумане... Я почти не чувствую ног...")
        if whoring < 24:
            her "Могу я получить очки, [genie_name]?"
        stop music fadeout 1.0


    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    $ gryffindor += current_payout #35

    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen chair_left
    hide screen desk
    hide screen ccg
    if not daytime:
        show screen candlefire

    call her_chibi("stand","desk","base")
    show screen genie
    call hide_blkfade

    if whoring < 24:
        m "Да, [hermione_name]. 90 очков \"Гриффиндору\"."
        $ gryffindor +=90

    call her_main("Спасибо, [genie_name]...","angry","suspicious",cheeks="blush",xpos="right",ypos="base")

    if whoring < 24: #Adds points till 24.
        $ whoring +=1

    if hg_pf_TimeForAnal_OBJ.points == 0:
        $ new_request_31_heart = 1
        $ hg_pf_TimeForAnal_OBJ.hearts_level = 1 #Event hearts level (0-3)
    if hg_pf_TimeForAnal_OBJ.points == 1:
        $ new_request_31_heart = 2
        $ hg_pf_TimeForAnal_OBJ.hearts_level = 2 #Event hearts level (0-3)
    if hg_pf_TimeForAnal_OBJ.points >= 2:
        $ new_request_31_heart = 3
        $ hg_pf_TimeForAnal_OBJ.hearts_level = 3 #Event hearts level (0-3)

    $ hg_pf_TimeForAnal_OBJ.points += 1

    $ aftersperm = False #Show cum stains on Hermione's uniform.

    $ custom_outfit_old = temp_outfit

    jump end_hg_pf  #Resets screens. Hermione walks out. Resets Hermione.
