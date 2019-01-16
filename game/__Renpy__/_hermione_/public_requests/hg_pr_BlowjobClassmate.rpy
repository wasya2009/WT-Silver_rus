

### Give Classmate A Blowjob ###

##(Level 07) (65 pt.) (Blowjob to a boy). (Available during daytime only).
label hg_pr_BlowjobClassmate: #LV.7 (Whoring = 18 - 20)
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pr_BlowjobClassmate_OBJ.points < 1:
        m "{size=-4}(Сказать ей, чтоб сделала минет однокласснику?){/size}"
        menu:
            "\"(Да, давай!)\"":
                call nar("!!! Внимание !!!","start")
                ">При продолжении этого пути изменится концовка."
                call nar(">Ты можешь сохранить игру здесь.","end")

                menu:
                    "Продолжить?"
                    "\"(Да!)\"":
                        pass
                    "\"(Нет!)\"":
                        jump silver_requests

            "\"(Нет, не сейчас.)\"":
                jump silver_requests

    call bld

    #Intro.
    if hg_pr_BlowjobClassmate_OBJ.points == 0:
        m "[hermione_name], сегодня я куплю у тебя одну услугу."
        call her_main("Спасибо, [genie_name]. Я ценю это.","open","closed",xpos="right",ypos="base")
        m "Конечно, рад помочь."
        m "Я хочу, чтобы ты пошла и отсосала одному из своих одноклассников."
        stop music fadeout 1.0
        call her_main("!!!","shock","wide")
        her "...Своим ртом?"

        if whoring < 18 or hg_pr_HandjobClassmate_OBJ.points < 2:
            jump too_much

        call play_music("chipper_doodle") # HERMIONE'S THEME.
        m "Да, как обычно делается..."
        call her_main("[genie_name], я...","upset","closed")
        call her_main("Я отказываюсь продавать вам такую развратную услугу, [genie_name].","open","annoyed",cheeks="blush")
        call her_main("Разве я не могу просто поцеловать другую девушку?","open","worriedCl")
        her "Я не возражаю, но..."
        m "[hermione_name], пожалуйста, хватит тратить мое время..."
        m "Если ты не в настроении продавать услуги..."
        m "Вон там дверь."
        call her_main("Но мне нужны очки, [genie_name]. Вы знаете это.","upset","closed")
        m "Как говорится, [hermione_name]..."
        m "\"Если ты не будешь сосать член - очков не получишь.\""
        call her_main("Пф...","angry","angry",cheeks="blush")
        her "............................"
        m ".........................................."
        call her_main("...Хорошо.","annoyed","angryL")
        her "Я сделаю это..."
        m "Тогда иди и сделай!"
        m "Доложи мне после занятий."
        call her_main("...","angry","angry",cheeks="blush")
        her "....."
        her "......."
        m "Можешь идти, [hermione_name]."
        her "..."

    #First and second time event.
    else:

        #First time event.
        if whoring >= 18 and whoring < 21:
            m "Иди и сделай счастливому однокласснику минет, [hermione_name]."
            call her_main("......Опять?","disgust","glance",xpos="right",ypos="base")
            m "Да, опять."
            call her_main("..........","annoyed","annoyed")

        #Second time event.
        elif whoring >= 21:
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name]..."
            m "Ты веришь в гороскопы?"
            call her_main("Немного, [genie_name]...","annoyed","angryL",xpos="right",ypos="base")
            m "Ну, может тебе стоит..."
            call her_main("...?","open","base")
            m "Я прочитал гороскоп и там было написано..."
            m "\"Посвятите сегодня себя в то, что вы делаете хорошо\"..."
            call her_main("И что я делаю хорошо...?","soft","baseL")
            m "Сосешь член, [hermione_name]."
            call her_main(".....................","annoyed","annoyed") # :(
            m "Доложи мне после занятий, как обычно..."
            call her_main("Конечно...","annoyed","angryL")

    $ hg_pr_BlowjobClassmate_OBJ.inProgress = True

    jump hg_pr_transition_block


label hg_pr_BlowjobClassmate_complete:

    call play_sound("door") #Sound of a door opening.
    call her_walk("door","mid",2)
    call bld


    #First time event.
    if whoring >= 18 and whoring < 21:

        #Event A
        if one_out_of_three == 1: ### EVENT (A)
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "Ты знаешь правила, [hermione_name]. Начинай рассказывать."
            show screen blktone
            call her_main("Я выполнила ваше задание, [genie_name].","disgust","glance",xpos="right",ypos="base")
            m "Хорошо. Расскажи как все прошло."
            call her_main("Что тут рассказывать, [genie_name]?","annoyed","angryL")
            her "Я отсосала у одного из своих одноклассников..."
            her "И это все..."
            m "Хм... Понятно..."
            m "..............."
            call her_main("....................................","angry","down_raised")
            m "Ты проглотила?"
            call her_main("...........................","annoyed","annoyed")
            m "[hermione_name], ты все проглотила?"
            call her_main("Да, [genie_name].","angry","angry")
            m "Ну, на сегодня достаточно..."

        #Event B
        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], ты выполнила задание?"
            show screen blktone
            play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
            call her_main("[genie_name], я...","angry","down_raised",xpos="right",ypos="base")
            her "Я пыталась, но..."
            call her_main("Мальчик мне отказал, [genie_name]...","mad","worried",tears="soft")
            call her_main("Не могу поверить, что это произошло...","angry","base",tears="soft")
            her "Я одна из лучших учениц в этой школе!"
            her "Одна из самых популярных..."
            call her_main("И он мне отказывает?","angry","angry",tears="soft")
            her "Почему он меня так оскорбляет?!"
            m "Так, ты обиделась, потому, что парень отказался засунуть член тебе в рот?"
            call her_main("Разве вы не злитесь, [genie_name]?","angry","angry",tears="crying")
            m "Я думаю, что справлюсь с этим довольно быстро..."
            call her_main("Он отверг меня [genie_name]...","angry","angry",cheeks="blush")
            her "Кем он себя возомнил?!"
            call her_main("Со всем уважением, [genie_name], вы не поймете...","open","annoyed",cheeks="blush")
            m "Хорошо, в любом случае. Я не заплачу тебе за это."
            call her_main("Конечно... Я и не ожидала этого, [genie_name].","annoyed","annoyed",tears="soft")
            her "Я не выполнила свою задачу и не заслуживаю никакой похвалы..."
            her "И если вы заплатите мне из-за жалости..."
            call her_main("То меня оскорбит это еще сильнее...","annoyed","angryL")
            m "Хм... В таком случае, может быть, я все равно заплачу тебе..."
            call her_main("Нет, [genie_name]. Я не приму это...","annoyed","annoyed")
            m "Хм... Что ж, тогда еще все впереди."
            her "Доброй ночи, [genie_name]."
            hide screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3

            $ display_h_tears = False

            $ hg_pr_BlowjobClassmate_OBJ.inProgress = False
            jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).

        #Event C
        elif one_out_of_three == 3: ### EVENT (C)
            #play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
            m "[hermione_name], Как прошло?"
            show screen blktone
            call her_main("Я все еще думаю насчет этой идеи, она ужасная, [genie_name].","annoyed","angryL",xpos="right",ypos="base")
            call her_main("Но, кроме этого, она довольно сильно удивляет...","annoyed","annoyed")
            call play_music("playful_tension") # SEX THEME.
            her "Я сделал классный минет мальчику из \"Когтеврана\"..."
            call her_main("И он был таким джентльменом...","open","down")
            call her_main("Он даже предупредил меня, когда собирался кончить.","angry","down_raised")
            m "Настоящий джентльмен."
            m "Ты проглотила?"
            call her_main("Конечно, [genie_name].","upset","closed")
            her "Я же сказала, что сделала мальчику классный минет."
            call her_main("Это меньшее, что я могла сделать для него...","angry","down_raised")
            m "Ну, в таком случае."

    #Second Event.
    if whoring >= 21: # LEVEL 08 =+
        if one_out_of_three == 1: ### EVENT (A)
            stop music fadeout 1.0
            # HERMIONE ALL MESSED UP, WITH RUNNING MASCARA.
            $ u_tears_pic = "characters/hermione/face/tears_03.png"
            $ display_h_tears = True
            $ aftersperm = True
            $ uni_sperm = True
            $ u_sperm = "characters/hermione/face/auto_08.png"

            show screen blktone
            call her_main("","angry","angry",xpos="right",ypos="base")
            call ctc

            m "[hermione_name]..."
            m "Ты выглядишь ужасно..."
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("[genie_name], меня изнасиловали.","scream","angryCl")
            m "Серьезно?"
            call her_main("Да, [genie_name].","annoyed","annoyed")
            her "Этот противный мальчик из \"Слизерина\" изнасиловал..."
            call her_main("или изнасиловал мое лицо...","open","down")
            her "И--"
            play sound "sounds/burp.mp3"
            call her_main("*Burp!*...","shock","worriedCl")
            call her_main("Простите.","angry","down_raised")
            call her_main("Он спустил так много, что я едва могла проглотить все...","scream","angry",emote="01")
            her "Чертов ублюдок!"
            call her_main("Вы думаете, я могу подать жалобу, [genie_name]?","angry","angry",cheeks="blush")
            m "Хм... Я полагаю..."
            m "Но, имей в виду, если мы поднимем вопрос по этому..."
            m "Всю \"Продажу услуг\" придеться немедленно прекратить."
            call her_main("Ох...?","open","baseL",cheeks="blush")
            her ".................."
            call her_main("Пожалуйста, забудьте, что я сказала...","base","happyCl")
            m "Ты уверена? Ты выглядишь довольно потрепанной."
            her "Нет, нет. Это ничего не значит..."
            her "В конце концов, я же предложила ему минет..."
            her "Он просто был немного груб со мной ближе к концу, вот и все..."
            her "Думаю, я слишком бурно реагирую..."
            m "Понятно..."
            her "Могу я--"
            play sound "sounds/burp.mp3"
            call her_main("*Burp!*...","shock","wide")
            call her_main("Простите, [genie_name].","angry","down_raised")
            call her_main("{size=-3}(Он продолжал кончать... Мой желудок переполнен.){/size}","angry","worriedCl",emote="05")
            call her_main("Могу я получить очки?","open","base")

        elif one_out_of_three == 2: ### EVENT (B)
            # HERMIONE COVERED IN CUM
            label suked_off_them_both:
                pass

            stop music fadeout 1.0
            $ uni_sperm = True
            $ u_sperm = "characters/hermione/face/auto_10.png"

            show screen blktone
            call her_main("","base","ahegao_raised",xpos="right",ypos="base")
            call ctc

            her "Добрый вечер, [genie_name]..."
            g4 "[hermione_name]?!"
            g4 "Что случилось, [hermione_name]?"
            g4 "Все о чем я тебя попросил, это сделать минет однокласснику."
            call play_music("playful_tension") # SEX THEME.
            call her_main("Что... я это сделала, [genie_name].","angry","down_raised")
            m "[hermione_name], ты покрыта спермой с головы до ног."
            call her_main("Я?","soft","ahegao")
            her "Ох... Я забыла привести себя в порядок?"
            call her_main("Как неловко...","base","glance")
            her "Я поошибке зашла в туалет мальчиков..."
            her "Прежде, чем я это поняла, я была окружена членами..."
            call her_main("Ох... От одного разговора у меня мурашки по коже... рр...","silly","dead")
            call her_main("...Я имею в виду от страха... нет, не бойтесь...","grin","ahegao")
            call her_main("Вы смущаетесь?","base","baseL",cheeks="blush")
            m "Ты меня спрашиваешь?"
            call her_main("Ох, простите, [genie_name]... Я чувствую себя немного легкомысленной...","grin","dead")
            her "Я думаю, мне нужно немного полежать..."
            m "Не забудь сперва сходить в душ."
            call her_main("Душ? Зачем?","base","glance")
            m "Неважно..."
            show screen ctc
            pause
            hide screen ctc

        #Event C
        elif one_out_of_three == 3:
            if  suked_off_ron_and_har:
                jump suked_off_them_both
            else:
                 $ suked_off_ron_and_har = True #In public events. Give blowjob to a classmate. Event level 03. Event # 3. "Sukerd off Harrt and Ron". Turns True after that.

            m "[hermione_name], как прошло?"
            show screen blktone
            call her_main("Прекрасно, [genie_name]. Великолепно.","base","happyCl",xpos="right",ypos="base")
            m "Правда? Рассказывай."
            call play_music("playful_tension") # SEX THEME.
            call her_main("Сегодня я сделала то, что так давно хотела...","base","ahegao_raised")
            her "Но не могла набрать силу воли..."
            m "Хм..?"
            call her_main("Сегодня я отсосала двум своим лучшим друзьям во всем мире!","soft","ahegao")
            call her_main("Это было так же захватывающе как я и представляла.","base","down")
            call her_main("Я заслюнявила их члены...","grin","dead")
            her "Сосала и лизала их яйца..."
            call her_main("Но лучше всего было видеть их лица...","silly","ahegao")
            her "Мальчики не могли поверить, что это на самом деле происходит..."
            call her_main("Честно говоря, я тоже не могла...","silly","dead")
            her "Я, Гермиона Грейнджер-девочка, которую они знали уже не первый год..."
            call her_main("Сосательница их членов...","open_wide_tongue","ahegao")
            call her_main("Как какая-то маленькая, грязная шлюха...","shock","baseL",cheeks="blush",tears="soft")
            m "Ты влюблена в них, [hermione_name]?"
            call her_main("Я не знаю, [genie_name]... Может быть...","base","happyCl")
            her "Могу ли я получить очки?"
            m "Конечно..."

    $ gryffindor += 65 #65

    m "\"Гриффиндор\" получает 65 очков!"
    her "Спасибо, [genie_name]."

    $ display_h_tears = False
    $ aftersperm = False
    $ uni_sperm = False

    $ public_whore_ending = True #Activates "Public Whore" ending.

    $ hg_pr_BlowjobClassmate_OBJ.points += 1
    $ hg_pr_BlowjobClassmate_OBJ.inProgress = False

    if hg_pr_BlowjobClassmate_OBJ.points >= 2:
        $ hg_pr_BlowjobClassmate_OBJ.complete = True

    jump hg_pr_transition_block

    return
