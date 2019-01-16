

### HERMIONE PERSONAL FAVOUR 6 ###

### DANCE FOR ME ###

label hg_pf_DanceForMe:
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_DanceForMe_OBJ.points < 1:
        m "{size=-4}(Попросить ее станцевать для меня?){/size}"
        menu:
            "\"(Да, давай!)\"":
                pass
            "\"(Нет, не сейчас.)\"":
                jump silver_requests

    if hg_heartDancer_OBJ.purchased:
        m "\"(Попросить ее переодеться?)\""
        menu:
            "\"(Да, давай!)\"":
                m "[hermione_name], прежде чем я попрошу об услуге, я хочу, чтобы ты переоделась."
                call her_main("Во что?","open","worriedL")
                m "В танцовщицу."
                if whoring >= 15:
                    call her_main("В танцовщицу?","scream","angryCl")
                    m "Не волнуйся, твои соски будут прикрыты."
                    call her_main("...","angry","worriedCl",emote="05")
                    call her_main("Ладно, пойду переоденусь.","normal","worriedCl")
                    call play_sound("door") #Sound of a door opening.
                    call set_hermione_outfit(hg_heartDancer_OBJ)
                    pass
                else:
                    jump too_much
            "\"(Нет, не сейчас.)\"":
                pass

    $ current_payout = 35 #Because will have option to pay extra.

    #First Time Event.
    if hg_pf_DanceForMe_OBJ.points == 0:

        call bld
        m "[hermione_name], я хочу, чтоб ты станцевала для меня."
        call her_main("Вы хотите, чтобы я...","open","worried")

        if whoring < 9:
            call her_main("...станцевала для вас, [genie_name]?","open","worriedL")
            jump too_much
        else:
            call her_main("...станцевала для вас, [genie_name]?","open","wink")

        $ new_request_11_heart = 1
        $ hg_pf_DanceForMe_OBJ.hearts_level = 1 #Event hearts level (0-3)

        m "Да... Думаешь, что справишься с этим?"
        call her_main("Эм... Я думую, да...","soft","baseL")
        her "Вы заплатите за это?"
        m "Конечно, [hermione_name]!"
        call her_main("Так... Тогда немного потанцуем...","annoyed","worriedL")
        m "Начинай когда будешь готова..."
        her "................."
        hide screen hermione_main
        with d3

        call nar(">Гермиона начала танцевать...","start")
        stop music fadeout 1.0

        hide screen blktone8
        call her_chibi("dance","mid","base")
        with fade
        pause.2

        m "Хм..."
        call her_head("{size=-5}(...........................................){/size}","disgust","down_raised",cheeks="blush")
        call her_head( "{size=-5}(Это глупо...){/size}","annoyed","angryL",cheeks="blush")
        call nar(">Гермиона смущенно выглядит, но она продолжает \"танцевать\"...")
        m "..................."
        call her_head( "{size=-5}(...........................................){/size}","annoyed","angryL",cheeks="blush")
        m "Хорошо, теперь можешь раздеваться."

        call her_chibi("stand","mid","base") #Hermione stands still.
        with hpunch

        show screen blktone
        call her_head("??!","mad","wide",cheeks="blush")
        call her_head("Я думала, что все, что мне нужно сделать, это танцевать?","angry","angry")
        call play_music("playful_tension") # SEX THEME.
        m "Правда? Вот незадача."
        m "Теперь начни снимать свою одежду."

        show screen blktone
        call her_head("Вы хотите, чтобы я... станцевала стриптиз для вас?","disgust","down_raised",cheeks="blush")
        m "Да. Я жду, что сегодня ты это сделаешь, [hermione_name]."
        call her_head("[genie_name]!","angry","worriedCl",cheeks="blush")
        m "Не повышай на меня голос, [hermione_name]!"
        call her_head("... ... ?!!","mad","wide",cheeks="blush")
        m "Никто не заставляет тебя это делать."
        m "Я делаю тебе одолжение!"
        m "Если тебе не нужны очки, пожалуйста, не задерживайся в моем кабинете."
        call her_head(".....................","angry","angry")
        call her_head(".......................................","disgust","down_raised",cheeks="blush")

        hide screen blktone
        call nar(">Гермиона снова начинает танцевать...")

        call her_chibi("dance","mid","base")
        with d5

        call her_head("{size=-5}(...........................................){/size}","angry","worriedCl",cheeks="blush")
        m "Чего же ты ждешь?"

        if hermione_wear_top and (h_top == "uni_top_1" or h_top == "uni_top_6"):
            m "Начни с жилета."

            call her_head(".............................................................","disgust","down_raised",cheeks="blush")
            call nar(">Гермиона сконфуженно смотрит на тебя и снимает жилет...")
        else:
            call nar(">Гермиона сконфуженно смотрит на тебя...")

        if hermione_wear_top and (h_top == "uni_top_1" or h_top == "uni_top_6"):
            if h_top == "uni_top_1":
                $ h_top = "uni_top_2"
            else:
                $ h_top = "uni_top_4"
            call update_her_uniform
            pause.2

        pause.5
        show screen blktone
        call her_main("{size=-5}(Я действительно собираюсь это сделать?){/size}","angry","worriedCl",cheeks="blush",trans="fade",xpos="base",ypos="base")
        call ctc

        menu:
            m "......................."
            "\"Теперь избавься от юбки!\"":
                call her_main(".................................","angry","worriedCl",cheeks="blush")

                hide screen blktone
                call nar(">Гермиона начинает расстегивать юбку...","start")
                ">Она кажется очень нерешительной..."
                call nar(">Наконец молния расстегнута, и у нее нет выбора, кроме как снять ее...","end")

                call her_main("{size=-5}(Ох, была не была...){/size}","angry","worriedCl",cheeks="blush")
                call her_main("{size=-5}(За честь \"Гриффиндора\"....){/size}","angry","worriedCl",cheeks="blush")

                call nar(">Гермиона снимает юбку...")
                pause.2

                $ hermione_wear_panties = True
                call set_hermione_action("lift_skirt")
                pause.5

                $ hermione_wear_bottom = False
                call set_hermione_action("None","skip_update")
                pause.5


                m "..............."
                call her_main("{size=-5}(.........................................){/size}","angry","worriedCl",cheeks="blush")
                call nar(">Гермиона продолжает танцевать...")
                m "Хорошо, теперь рубашка!"
                call her_main("Моя рубашка... ... ?","disgust","down",cheeks="blush")
                hide screen hermione_main
                with d3

                hide screen blktone
                call nar(">Гермиона выглядит смущенной....","start")
                call nar(">Она неуклюже перебирает пуговицы своей рубашки...","end")

            "\"Теперь сними рубашку!\"":
                call her_main(".................................","angry","worriedCl",cheeks="blush")

                hide screen blktone
                call nar(">Гермиона начинает расстегивать рубашку...","start")
                ">Она кажется очень нерешительной..."
                call nar(">Наконец, последняя пуговица расстегнута, теперь у нее нет выбора, кроме как снять ее...","end")

                call her_main("{size=-5}(Ладно, будь, что будет...){/size}","angry","worriedCl",cheeks="blush")
                call her_main("{size=-5}(За честь \"Гриффиндора\"!){/size}","angry","worriedCl",cheeks="blush")

                call nar(">Гермиона снимает рубашку...")
                pause.2

                call set_hermione_action("lift_top")
                pause.5

                $ hermione_wear_top = False
                call set_hermione_action("None","skip_update")
                pause.5

                call her_main("{size=-5}(Я это сделала...){/size}","angry","worriedCl",cheeks="blush")
                call her_main("{size=-5}([genie_name] может увидеть мою грудь, пока я танцую...){/size}","angry","worriedCl",cheeks="blush")
                call her_main("{size=-5}(Это так унизительно...){/size}","angry","worriedCl",cheeks="blush")
                call her_main("{size=-5}(Но я делаю это для своего факультета...){/size}","angry","worriedCl",cheeks="blush")

                m "Неплохо...."
                call her_main("{size=-5}(.........................................){/size}","angry","worriedCl",cheeks="blush")

                call nar(">Гермиона стоит с обнаженной грудью...","start")
                ">Она продолжает танцевать, но, кажется, она очень стеснена в движениях. Даже больше, чем раньше..."
                call nar(">Похоже, она пытается предотвратить, чтобы ее грудь не покачивалась и не подпрыгивала...","end")

                m "Ладно, теперь юбка!"
                call her_main("....................","angry","worriedCl",cheeks="blush")
                hide screen hermione_main
                with d3

                hide screen blktone
                call nar(">Гермиона выглядит смущенной....","start")
                call nar(">Она нащупывает застежку юбки...","end")

        stop music fadeout 1.0
        m "В чем проблема, [hermione_name]?"
        call play_music("sad") # HERMIONE'S THEME.

        call her_head("Простите, [genie_name]...","angry","worriedCl",cheeks="blush")
        call her_head("Она застряла...","angry","worriedCl",cheeks="blush")
        call her_head("Она не сдвигается с места...","angry","worriedCl",cheeks="blush")
        call her_head("Почему она не сдвигается с места?! *всхлип*","angry","worriedCl",cheeks="blush")
        call her_head("Нет, я не могу этого сделать, [genie_name]! *всхлип*","open","surprised",cheeks="blush",tears="messy")
        m "Что?"
        call her_main("Я думала, что смогу, но...","angry","suspicious",cheeks="blush",trans="fade")
        call her_main("Обнажиться ради очков, [genie_name]?","angry","suspicious",cheeks="blush")
        call her_main("Люди смотрят на меня в этой школе!","angry","suspicious",cheeks="blush")
        call her_main("У меня есть репутация...*всхлип*","angry","suspicious",cheeks="blush")
        call her_main("И если я это сделаю...","scream","angry",cheeks="blush",tears="messy")
        call blkfade

        ">Гермиона быстро надевает форму..."

        call h_action("None")
        call her_chibi("stand","desk","base")

        hide screen blkfade
        call her_main("[genie_name], Думаю, мне лучше сейчас уйти... *Всхлип!*","angry","suspicious",cheeks="blush",tears="messy",trans="fade")

        menu:
            "\"Хорошо. Мне было весело. Вот твои очки.\"":
                call her_main("Правда? Разве я все не испортила?","soft","baseL",tears="soft")
            "\"Конечно. Ты не получишь никаких очков.\"":
                call her_main("[genie_name]... Возможно, я не очень хороша в этом...","open","base",tears="mascara_crying")
                call her_main("Но я сделала все возможное... Думаю, я заслужила немного--",tears="mascara_crying")
                m "Просто постарайся в следующий раз, [hermione_name]."
                call her_main("Следующий раз?!","open","base",tears="mascara_crying")
                call her_main("Уверяю вас, [genie_name], следующего раза не будет...","angry","angry",cheeks="blush",tears="mascara")
                m "Посмотрим..."
                call her_main("Пф!","disgust","glance",tears="mascara")
                $ mad += 35
                call music_block
                jump could_not_flirt

    #Second Event
    if hg_pf_DanceForMe_OBJ.points == 1:

        $ new_request_11_heart = 2
        $ hg_pf_DanceForMe_OBJ.hearts_level = 2 #Event hearts level (0-3)

        call bld
        m "[hermione_name], Я хочу, чтоб ты станцевала для меня."
        call her_main("Еще раз, [genie_name]... ?","disgust","glance")
        m "Ты разумеется получишь свои очки..."
        call her_main("............................","annoyed","angryL")
        call her_main("И вы ожидаете, что я... эм...","annoyed","angryL")
        m "Обязательно снимешь свою одежду."
        stop music fadeout 1.0

        show screen blktone
        call her_main("......................","annoyed","angryL")
        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("Ну, почему бы и нет?","disgust","glance")
        call her_main("Да, не понимаю, почему бы и нет!","scream","angry",emote="01")
        m "Хм... {size=-4}(Посмотрика на нее, такая нетерпеливая...){/size}"
        call her_main("В конце концов, как ученица, я должна подчиняться всем вашим приказам, не так ли, [genie_name]?!","scream","angryCl")
        m "...................."
        call her_main("Если директор говорит мне раздеться, то, значит, я должна раздеться!!!","scream","angryCl")
        call her_main("Считаю ли я это крайне неуместным, позорным и унизительным?","angry","angry")
        call her_main("Конечно же, нет! Какой вздор!","scream","angryCl")
        m ".............."
        call her_main("Ха! Все ведь так, как и должно быть!","angry","angry")

        hide screen bld1
        hide screen blktone
        hide screen hermione_main
        with d3
        pause.2

        m "??!"

        call her_walk_desk_blkfade

        $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking.
        pause 3
        g4 "!!!!!!"
        ">К твоему удивлению, Гермиона взбирается на твой стол и начинает безумно танцевать..."
        call her_chibi("dance","on_desk","on_desk")
        hide screen blkfade
        with fade
        pause.5

        show screen blktone
        call her_main("Если я должна унижаться, чтобы защитить честь моего факультета...","scream","angryCl",xpos="mid",ypos="base")

        if hermione_wear_top and (h_top == "uni_top_1" or h_top == "uni_top_6"):
            call nar(">Гермиона начинает снимать свой жилет...")
        call her_main("Так и будет!","scream","angry",emote="01")
        call her_main("Просто...","open","down")
        call her_main("*стон*","clench","down_raised")

        if hermione_wear_top and (h_top == "uni_top_1" or h_top == "uni_top_6"):
            call nar(">У жилета, кажется, застряла застежка. Но она рьяно пытается сорвать его с себя...")
            call her_main("Почему он не... .?!")
            call her_main("Вот!","annoyed","annoyed")
            call nar(">Гермиона, наконец-то, сняла с себя жилет и кидает его в дальний угол кабинета...")

            if h_top == "uni_top_1":
                $ h_top = "uni_top_2"
            else:
                $ h_top = "uni_top_4"
            call update_her_uniform
            pause.2

            call her_main("","","")
            pause.1

        else:
            call nar(">Девушка, кажется, размышляет о том, что ей снять в первую очередь...")
            pause.1

        call her_main("Юбка следующая, верно?","scream","angryCl")

        menu:
            m "..."
            "\"Да, верно. Снимай ее!\"":
                call her_main("Конечно!")
                call her_main("А вот и она!","open","down")
                pause.1
            "\"Тебе нужно успокоиться, [hermione_name]. \"":
                call her_main("Что ж, {size=+7}ПРОСТИТЕ МЕНЯ{/size}, [genie_name]!")
                call her_main("Вы сказали мне раздеться для вас, но вы не говорили мне ваши предпочтения!")
                m "Что ж, я скажу тебе сейчас, [hermione_name]!"
                call her_main("Слишком поздно!","angry","angry")
                pause.1

        $ hermione_wear_panties = True
        call set_hermione_action("lift_skirt")
        pause.5

        $ hermione_wear_bottom = False
        call set_hermione_action("None","skip_update")
        pause.2

        call nar(">Гермиона кидает свою юбку через весь кабинет, как она сделала с жилетом мгновение назад...")

        m "{size=-4}(Вау, она видимо тренировалась...){/size}"
        m "{size=-4}(Может быть, еще слишком рано--{/size}"
        call her_main("Моя рубашка?!!","disgust","glance")

        $ hermione_wear_bra = True
        call set_hermione_action("lift_top")
        pause.2

        call her_main("{size=+9}Она мне не нужна!{/size}","scream","angry",emote="01")
        pause.2

        $ hermione_wear_top = False
        call set_hermione_action("None","skip_update")
        pause.2

        call nar(">Рубашка Гермионы внезапно падает на пол.")
        call her_main("","angry","angry")
        pause.2
        g4 "{size=-4}(Когда она успела??!){/size}"
        call ctc

        call her_main("Вам нравится, [genie_name]?")
        call her_main("","angry","angry")

        call set_hermione_action("lift_breasts")

        call her_main("Должна ли я трясти для вас своей грудью, как те шлюхи?","scream","angryCl")
        m "Ну---"
        call her_main("Конечно! Почему бы мне не унизиться для вашего удовольствия?!")
        call her_main("Это вполне {size=+7}приемлемо!{/size}","scream","angry",emote="01")
        call her_main("","angry","angry")

        call set_hermione_action("None","skip_update")
        pause.2

        call nar(">Гермиона начинает неуклюже трясти обнаженной грудью...","start")
        call nar(">Пока ты смотришь, как сиськи этой девочки расскачиваются влево-вправо перед твоим лицом, тебе приходится бороться с сильным желанием...","end")

        menu:
            m "..."
            "-Схватить их!-":
                g9 "{size=-4}(Да, именно просто положить свои руки на эти милые сиськи!){/size}"
                g9 "{size=-4}(Может, чуть подергать их...){/size}"
                call slap_her #Calls slapping sound and visual.
                call her_main("","disgust","wide")
                pause.2
                call slap_her #Calls slapping sound and visual.
                call her_main("","shock","shocked")
                pause.2

            "-Отшлепать их!-":
                m "{size=-4}(Я хочу выбить дерьмо из ее веселых сисек.){/size}"
                call slap_her #Calls slapping sound and visual.
                call her_main("","disgust","wide")
                pause.2
                g9 "{size=-4}(Да, просто шлепну их немного...){/size}"
                call slap_her #Calls slapping sound and visual.
                call her_main("","shock","shocked")
                pause.2

            "-Укусить их!":
                m "{size=-4}(Это странно, что я хочу впиться в них зубами?){/size}"
                m "{size=-4}(Нет, это не странно!){/size}"
                m "{size=-4}(Просто пара нежных укусов с любовью!){/size}"
                call kiss_her
                call her_main("","shock","wide",tears="soft")
                pause.2
                g9 "{size=-4}(Да... Может быть, больше чем пара укусов...){/size}"
                call her_main("","disgust","worriedCl",tears="soft_blink")
                pause.2
                call kiss_her
                call kiss_her
                pause.2

            "-Зарыться в них лицом!-":
                m "{size=-4}(Я просто хочу зарыться в них лицом!){/size}"
                call kiss_her
                call her_main("","shock","worriedCl")
                pause.2
                g9 "{size=-4}(Да, зарыться в них лицом - это лучшее, что можно сделать!){/size}"
                call her_main("","shock","shocked")
                pause.2

        call nar(">Пока ты решаешь, Гермиона продолжает танцевать...")


        call her_main("(Танцую голой перед директором...)","soft","shocked")
        call her_main("(Позволяю трогать ему свою грудь...)","disgust","shocked")
        call her_main("(Если мои родители узнают об этом, они сойдут с ума...)","soft","shocked")
        call her_main("(Особенно мой отец...)","annoyed","closed")
        call nar(">Гермиона снова начинает трясти сиськами...")
        call her_main("(Гермиона Грейнджер - стриптизерша...)")
        call her_main("(Прости меня, папочка...)","annoyed","dead")
        pause.1

        call nar(">Гермиона кладет руки на сиськи и начинает сжимать их...","start")
        ">Вы можешь только предполагать, что у нее на уме, но выглядит она очень подавленно и смущенно."
        call her_main("(Раньше я была лучшей ученицей... Примером для других...)")
        ">Гермиона сильнее хватается за сиськи и скручивает их пару раз..."
        ">Выглядит так, будто она зла на них и пытается наказать..."
        call nar(">Выглядит странно, но возбуждающе...","end")

        call her_chibi("image","on_desk","on_desk","dance/05_panties_01")
        call ctc

        call her_main("Ну, я надеюсь, вы наслаждаетесь, [genie_name]!","open","annoyed")
        m "Что?"
        call her_main("Мне бы хотелось получить очки прямо сейчас...","open","angryCl")
        m "Разве ты ничего не забыла, [hermione_name]?"
        call her_main("[genie_name]... ?","open","annoyed")
        m "А трусики?"
        call her_main("Мои трусики?","open","wide")
        call her_main("Но, они их не снимают!")
        m "Кто именно \"они\"?"
        m "Стриптизерши в детских мультфильмах?"
        m "Стриптиз-это раздевание, [hermione_name]!"
        m "А теперь снимай трусики!"
        call her_main("................","angry","wide")

        call nar(">Гермиона выглядит испуганно. Весь ее гнев ушел...","start")
        call her_main(".................","annoyed","closed")
        ">Молчание..."
        call nar(">Она начинает снимать трусики...","end")

        $ hermione_wear_panties = False
        call update_her_uniform
        call her_chibi("image","on_desk","on_desk","dance/07_dance_01")
        call her_main("","annoyed","worriedCl",cheeks="blush")
        pause.2

        g9 "......................................."

        hide screen blktone
        hide screen bld1
        hide screen hermione_main
        with d1

        stop music
        call play_sound("door") #Sound of a door opening.

        call sna_walk("door","mid",2)


        call sna_main("Послушай, Джини. Я подумал--","snape_01",xpos="base",ypos="base")

        hide screen snape_01 #Chibi
        show screen hermione_main
        with d3

        $ renpy.play('sounds/scratch.wav')
        with hpunch

        call sna_main("............................................","snape_11")
        with hpunch

        call her_main("(Профессор Снейп???????!)","angry","wide")
        call sna_main("Мисс Грейнджер?","snape_12")

        call h_action("covering")
        show screen bld1
        call her_main("(Нет, нет... Этого не может быть... Пожалуйста...)","shock","worriedCl",cheeks="blush",trans="d5")
        call play_music("playful_tension") # SEX THEME.
        m "...................................."

        menu:
            m "..."
            "\"Северус, я сейчас немного занят.\"":
                call sna_main("Да... Я вижу, что...","snape_13")
                call her_main("{size=-7}(Я хочу умереть!){/size}","angry","worriedCl")
            "\"Северус! Пожалуйста, присоединяйся к нам.\"":
                $ mad += 20
                #$ snape_invated_to_watch = True #Removed. Turns true on a new Snape event instead. (label special_date_with_snape_03)
                call sna_main("Серьезно?","snape_14")
                call her_main("([genie_name], нет, пожалуйста.............................)","angry","worriedCl")
                call sna_main("Действитель, очень заманчивое предложение...","snape_13")
                call her_main("!!!!!!.......","angry","wide")
                call sna_main("Ну, может быть, в другой раз...","snape_13")
                call her_main("{size=-5}(Другого раза не будет!){/size}","angry","worriedCl")
                call her_main("{size=-5}(Я прекращу продавать услуги с этого момента, клянусь!){/size}")

        call sna_main("Я отложу наш разговор, Джи-- *кхм!* Альбус.","snape_12")
        call sna_main("Мисс Грейнджер...","snape_13")
        call her_main(".................................","angry","worriedCl")

        hide screen bld1
        show screen snape_01
        hide screen snape_main
        hide screen hermione_main
        with fade
        pause.2

        call sna_walk("mid","leave",3)

        call blkfade
        ">Гермиона поспешно спрыгивает со стола."
        ">Она начинает отчаянно одеваться..."

        call her_chibi("stand","desk","base")
        call hide_blkfade

        call her_main("Моя рубашка! Где моя рубашка?!","scream","worriedCl",xpos="mid",ypos="base")
        m "Там, у камина..."

        hide screen hermione_main
        with d3
        pause.2

        call her_walk("desk","mid",1.5)

        call her_head("................................","disgust","down_raised",xpos="base",ypos="base")
        pause.2

        $ hermione_wear_panties = True
        $ hermione_wear_top = True
        $ hermione_wear_bottom = True

        call h_action("none")

        call her_chibi("stand","mid","base",flip=True)
        pause.2
        call her_walk("mid","desk",2)

        show screen bld1
        call her_main("........................","normal","worriedCl",xpos="base",ypos="base")
        stop music fadeout 2.0
        call her_main("Могу ли я просто получить свои очки, пожалуйста?","angry","worriedCl",emote="05")
        pause.2
        call blkfade
        pause.5


    #Third Event.
    if hg_pf_DanceForMe_OBJ.points >= 2:

        $ new_request_11_heart = 3
        $ hg_pf_DanceForMe_OBJ.hearts_level = 3 #Event hearts level (0-3)

        call blktone

        if snape_invated_to_watch: #Turns TRUE after Dance Event 2 and the next Date with Snape.
            m "(Хм ... Я может пригласить Снейпа?)"

            menu:
                "-\"Да! Гермионе нужна аудитория!\"-":
                    if not invited_snape_once_already:
                        $ invited_snape_once_already = True #Makes sure this event takes place only once.
                        hide screen blktone
                        hide screen hermione_main
                        with d3

                        m "Мисс, Грейнджер, я куплю у тебя сегодня еще одну услугу."

                        call her_main("Конечно, [genie_name].","open","closed",xpos="base",ypos="base")
                        m "Но для этого, как ты думаешь, ты могла бы пойти и пригласить сюда профессора Снейпа?"
                        call her_main("...профессора Снейпа?","annoyed","suspicious")
                        her "Могу я спросить, зачем, [genie_name]?"
                        m "Ну, я думаю, для подобных танцев нужно немного больше зрителей."
                        call her_main("Подобных танцев... ?!!","shock","wide")
                        call her_main("При всем моем уважении, [genie_name]...","angry","angry")
                        call her_main("{size=-5}(Которого у меня так мало осталось к вам...){/size}","normal","frown")
                        call her_main("Я отказываюсь деградировать для развлечения профессора Снейпа!","scream","angryCl")
                        m "Нет, нет, ты неправильно поняла , [hermione_name]."
                        call her_main("Хм..?","soft","base")
                        m "Я хочу проверить профессора Снейпа на причастность к \"грязным\" делишкам, и ты должна мне помочь"
                        call her_main("!!!","shock","wide")
                        m "Да, я хочу поймать его с поличным!"
                        call her_main("[genie_name], я не понимаю...","open","worried")
                        call her_main("Хм... хотя.... теперь ясно...","base","base")
                        her "Простите, что сомневалась в вас [genie_name]..."
                        m "Ничего страшного. Теперь найди профессора Снейпа и приведи его сюда.."
                        call her_main("Я пошла [genie_name]!","smile","angry")

                    else:
                        hide screen blktone
                        hide screen hermione_main
                        with d3

                        m "Мисс, Грейнджер, сегодня я куплю у тебя еще одну услугу.."

                        call her_main("Конечно, [genie_name].","open","closed",xpos="base",ypos="base")
                        m "Но для этого, как ты думаешь, ты могла бы пойти и пригласить сюда профессора Снейпа?"
                        call her_main("...профессора Снейпа?","annoyed","suspicious")
                        her "Могу я спросить, зачем, [genie_name]?"
                        m "Ох, я просто хочу, чтоб ты станцевала для нас."
                        call her_main("!!!","open","base")
                        m "Я хочу доказать, что профессор Снейп замешан в \"грязных\" делишках, и мне нужна твоя помощь."
                        call her_main("Но, разве мы в прошлый раз не узнали?","annoyed","worriedL")
                        m "Ну, эм... Конечно..."
                        m "Но мне нужно будет больше доказательств, если я буду поднимать этот вопрос в Министерстве магии!"
                        call her_main(".....","angry","angry")
                        m "Итак, что ты скажешь [hermione_name]?"
                        m "Еще один танец для всеобщего блага?"
                        call her_main("Ну, хорошо...","disgust","glance")
                        m "Хорошо. Иди и найди профессора Снейпа..."

                    hide screen bld1
                    hide screen hermione_main
                    with d3

                    call her_walk("mid","leave",2.5,loiter=False)
                    call blkfade

                    stop music fadeout 1.0
                    ">..............{w}..................{w}...................."
                    call play_sound("door") #Sound of a door opening.
                    with d3
                    call her_chibi("stand","desk","base")
                    call sna_chibi("stand","mid","base")
                    call hide_blkfade
                    pause.5

                    call play_music("dark_fog")

                    show screen blktone
                    call sna_main("Джи... *кхм*, я имел в виду Альбус, ты хотел меня видеть?","snape_01",xpos="base",ypos="base")
                    m "Да. Ты в настроении для небольшого стриптиза?"
                    call sna_main("Ох..?","snape_05")
                    sna "Я полагаю, Мисс Грейнджер будет выступать?"
                    call her_main("..............","angry","worriedCl",emote="05",xpos="mid",ypos="base")
                    m "Да, наша маленькая мокрощелка более чем счастлива снять одежду для нашего развлечения."
                    call her_main("............","angry","worriedCl",emote="05")
                    m "Не так ли [hermione_name]?"
                    hide screen blktone
                    hide screen hermione_main
                    hide screen snape_main
                    with d3
                    pause.5

                    call her_chibi("stand","desk","base",flip=True)
                    with d1
                    pause.8

                    call her_chibi("stand","desk","base")
                    with d1
                    pause.5

                    show screen blktone
                    show screen snape_main
                    call her_main("Да, [genie_name].","angry","worriedCl",emote="05")
                    m "В таком случае, приступай!"
                    hide screen hermione_main
                    with d3
                    pause.2
                    call sna_main("","snape_13")
                    pause.8

                    hide screen snape_main
                    call blkfade

                    $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking.
                    pause 3
                    call her_chibi("dance","on_desk","on_desk")
                    call sna_chibi("stand","desk_close","base")

                    call her_head(".............","open","closed")

                    call sna_head("......................","snape_05")

                    m ".........................."

                    hide screen blktone
                    call hide_blkfade
                    pause.8

                    call blktone
                    m "Так... Северус... Как жизнь?"

                    call sna_main("Ну, ты же знаешь... все по старому... все по старому...","snape_09")
                    call sna_main("Из-за студентов у меня стресс...","snape_06")
                    call sna_main("На самом деле мисс Грейнджер вызывала у меня больше стресса, чем любой другой студент...","snape_03")
                    pause.2
                    call her_main("...............................","grin","baseL")
                    m "Ох, я уверен, что она немного сожалеет об этом..."
                    call her_main("{size=-4}(Ни капельки!!){/size}","base","happyCl")
                    m "И сделает что угодно для тебя сегодня. Да, [hermione_name]?"
                    pause.2

                    call her_main("Хм... Да, [genie_name].","base","squint")
                    pause.2

                    if hermione_wear_top and (h_top == "uni_top_1" or h_top == "uni_top_6"):
                        call nar(">Гермиона снимает свою одежду и начинает соблазнительно покачивать своими бедрами.")

                        if h_top == "uni_top_1":
                            $ h_top = "uni_top_2"
                        else:
                            $ h_top = "uni_top_4"
                        call update_her_uniform
                        pause.2

                        call her_main("","","")
                        pause.1

                    else:
                        call nar(">Гермиона соблазнительно взмахивает руками.")
                        pause.1

                    call ctc

                    call her_main("...................","open","down")
                    call sna_main("Хм... Вы подозрительно спокойны, мисс Грейнджер.","snape_05")
                    call her_main("{size=-4}(Ох нет! Он следит за нами?){/size}","shock","wide")
                    call her_main("Я просто делаю то, что сказал мне директор школы, профессор Снейп...","grin","worriedCl",emote="05")
                    call sna_main("Сегодня вы не собираетесь выговаривать мне о \"разврате, в котором погряз Хогвартс\"?","snape_03")
                    m "Северус..."
                    call sna_main("Нет, Альбус, я хочу услышать ответ  маленькой мисс совершенство.","snape_03")
                    call her_main("Я просто хочу, чтобы вы хорошо провели время, профессор Снейп...","grin","worriedCl",emote="05")
                    call sna_main("Ой! Это \"Профессор Снейп\" это ведь ты не ко мне обращаешься?","snape_03")
                    call sna_main("Что стало со \"Снейпдиотом\" и профессором \"Лицемериусом\"??!","snape_10")
                    g9 "{size=-5}( \"Снейпдиотом\", хех... это забавно.){/size}"
                    call her_main(".............","grin","worriedCl",emote="05")
                    call sna_main("Да, я знаю, что ты называешь меня так за моей спиной, девочка!","snape_08")
                    call her_main("Ну, может быть, это потому, что вы этого заслуживаете... Снивеллус .","scream","angry",emote="01")
                    call sna_main("Что?!","snape_10")
                    call sna_main("Как ты смеешь... ..?")
                    call sna_main("Кто ты, по-твоему, такая? Ты грязно--","snape_15")
                    call her_main("[genie_name], один из ваших сотрудников пытается оскорбить меня!","scream","angryCl")
                    call her_main("Вы это допустите?")
                    call sna_main("Оскорбить... ?! У тебя хватает наглости, девочка!","snape_08")
                    call sna_main("Альбус, ты позволишь ей так говорить с преподавателем?","snape_10")
                    call her_main("[genie_name]!","scream","angryCl")
                    call sna_main("Альбус!","snape_10")

                    menu:
                        m "..."
                        "\"[hermione_name], прояви немного уважения!\"":
                            $ mad += 9
                            call her_main("Что?","annoyed","angry")
                            call her_main("Но [genie_name]!")
                            m "Юная леди, ты {size=+4}должна{/size} успокоиться."
                            call her_main("Пф!","disgust","glance")
                            m "И снимай уже свою юбку, хорошо?"
                            call her_main(".......","annoyed","angryL")
                            call sna_main("...........","snape_13")
                        "\"Северус, ты это начал.\"":
                            call sna_main("Что? Я?!","snape_10")
                            call her_main("Спасибо, [genie_name].","base","base")
                            call sna_main("Альбус, ты балуешь девку! Ей нужно преподать урок!","snape_08")
                            m "...............Северус."
                            g4 "Ты головой ударился?!"
                            call sna_main("Прошу прощения?","snape_03")
                            g4 "Девочка уже раздевается для нас!"
                            g4 "О каком наказании ты говоришь?"
                            call sna_main("Пф... Как насчет порки?","snape_16")
                            g4 "Северус!"
                            call sna_main("Хорошо, хорошо, я тебя понял...","snape_17")
                            m "[hermione_name], ты собираешься раздеваться дальше или нам придется заглядывать тебе под юбку?"
                            call her_main("Эм...","open","down")
                            m "Снимай юбку, [hermione_name]!"
                            call her_main("Да, [genie_name]...","soft","base")
                        "\"Вы оба, успокойтесь, мать вашу...\"":
                            m "Ты, высокий-парень в черном, успокойся немного, хорошо?"
                            call sna_main("Прошу прощения?","snape_03")
                            call her_main("Да, так ему, профес--","annoyed","angryL")
                            m "Ты тоже, маленькая извращенка!"
                            m "Успокойся и снимай уже с себя юбку."
                            call her_main("Я не извращенка...","annoyed","annoyed")
                            m "Юбка, [hermione_name]!"
                            call her_main("......","annoyed","angryL")
                            call sna_main(".............","snape_13")
                        "-HARDCORE-" if hardcore_difficulty_active: #Hardcore difficulty dialogue.
                            $ mad += 18
                            m "Оба..."
                            stop music
                            with hpunch
                            g4 "Заткнитесь в жопу!!!"
                            g4 "Ты!... Ты ни на что не годный, уродливый, кривоногий волшебник!"
                            with hpunch
                            call sna_main("(...)","snape_11")
                            call her_main("(... жесть!)","angry","wink")
                            call sna_main("(Что ты, только что, сказал мне?!)","snape_08")
                            g4 "Закрой свой дурацкий рот или я выкину тебя из этого чертового окна!"
                            g4 "Эта сучка стриптиз для тебя танцует, что ты еще хочешь?!"
                            call her_main("(С-Су--","shock","wide")
                            g4 "А ты,... стриптизерша-шлюха!"
                            g4 "Делайте то, за что тебе платят и начинай уже раздеваться!!!"
                            call her_main("......","angry","angryCl",emote="01")
                            call sna_main(".............","snape_05")
                            call her_main("...","mad","frown")
                    pause.2

                    $ hermione_wear_panties = True
                    call set_hermione_action("lift_skirt")
                    pause.5

                    $ hermione_wear_bottom = False
                    call set_hermione_action("None","skip_update")
                    pause.2

                    call nar(">Гермиона быстро снимает юбку \"Хогвартса\"...")
                    call ctc

                    sna "Хм..."
                    call her_main("........................","open","down")
                    m "Да, так намного лучше!"

                    call nar(">Гермиона продолжает танцевать, пока на ней ничего не остается, кроме рубашки...")

                    menu:
                        m "..."
                        "\"Северус, что с мальчиком Поттером ?\"":
                            call her_main("(... ..?)","soft","base")
                            call sna_main("А что с ним?","snape_09")
                            m "Он все еще причиняет тебе беспокойства?"
                            call sna_main("Ох...","snape_09")
                            call sna_main("Не совсем, нет...")
                            call sna_main("Честно говоря, у меня никогда не было с ним особых проблем...","snape_06")
                            sna "Хотя я планировал сделать его жизнь здесь несчастной из-за его отца...."
                            call sna_main("Но в последнее время у меня есть гораздо более интересные проекты, которыми я занимаюсь...","snape_02")
                            call her_main("...................","soft","base")
                        "\"Северус, а что насчет Уизли?\"":
                            call sna_main("А с ними что?","snape_09")
                            m "Они все еще создают проблемы?"
                            call sna_main("Да... Больше чем когда-либо.","snape_09")
                            m "Хм..?"
                            m "Похоже, тебя это не сильно волнует?"
                            call sna_main("Это потому, что я знаю, что они получат то, что они заслуживают...","snape_05")
                            m "Месть? Круто! Что у тебя на уме?"
                            call her_main("!!!","soft","base")
                            call sna_main("Хм... не могу обсуждать это, пока \"лазутчик\" рядом.","snape_06")
                            call her_main("Пф!","annoyed","angryL")
                            call sna_main("Все, что я могу сказать, что это связано с их любимой младшей сестрой Джинни...","snape_13")
                            m "Джинни? Хм... Какое любопытное имя для девочки..."
                            m "............."
                            m "Так, ты планируешь выебать ее?"
                            call sna_main("?!!","snape_08")
                            call sna_main("Альбус, пожалуйста, не перед девочкой!","snape_17")
                            m "Хорошо, хорошо..."

                            #if not snapes_plan_for_ginny:
                            #    call nar(>Your curiosity about Ginny grows!)
                            #$ snapes_plan_for_ginny = True

                            call her_main("{size=-5}(Джини...){/size}","open","down")
                        "\"Как бы ты оценил задницу Гермионы?\"":
                            call sna_main("Ягодицы мисс Грейнджер?","snape_05")
                            call her_main("!!!............","annoyed","angryL")
                            m "Конечно! Как ты оцениваешь ее работу."
                            call sna_main("Хм...","snape_13")
                            pause.1
                            call nar(">Профессор Снейп оценивающе смотрит на попку Гермионы...")
                            call her_main("... ... ..?","upset","wink")
                            call sna_main("Я бы сказал...","snape_13")
                            call her_main("... ... ... ... .?!","base","down")
                            call sna_main("Да... \"{size=+5}Два с минусом-{/size}\".","snape_09")
                            call her_main("(Что?!)","shock","wide")
                            call sna_main("Неудовлетворительно...","snape_09")
                            sna "Посмотри на нее! Такая маленькая и ущипнуть не за что... Да это определенно задница мальчика!"
                            call her_main("!!!!!!!!!!","angry","annoyed",emote="01")

                    call nar(">Гермиона, одна за другой, расстегивает пуговицы на блузке...")
                    pause.2

                    $ hermione_wear_bra = False
                    call set_hermione_action("lift_top")
                    pause.5

                    $ hermione_wear_top = False
                    call set_hermione_action("None","skip_update")
                    pause.2

                    call nar(">Затем снимает ее...")

                    m "Все в порядке! Мы наконец добрались до хорошего финала!"
                    call sna_main("Хм...","snape_13")

                    call her_main("........","annoyed","closed")

                    menu:
                        m "..."
                        "-Начать дрочить-":
                            call play_music("playful_tension") # SEX THEME
                            pause.2

                            call blkfade
                            hide screen hermione_main
                            hide screen snape_main
                            pause.2

                            call her_head("[genie_name]?!","open","wide")
                            m "Все хорошо, [hermione_name]. Не обращай на меня внимания..."
                            call sna_head("Ох, это входит в программу выступления?","snape_12",xpos="base",ypos="base")
                            call sna_head("Ну, тогда я не против присоединится...","snape_12")
                            call her_head("!!!")

                            hide screen genie
                            show screen chair_left
                            call gen_chibi("jerking_off","behind_desk","base")
                            hide screen desk
                            show screen desk
                            call her_chibi("stand","on_desk","on_desk")
                            call sna_chibi("jerking_off","desk","base")
                            hide screen blktone
                            call hide_blkfade
                            call ctc

                            show screen bld1
                            call her_main("Нет, ребята ... Я имею в виду, сэры... Эм, профессора!","angry","wide")
                            m "Не обращай внимание [hermione_name], просто продолжай делать свое дело."
                            call her_main("Но...")
                            call her_main("Нет! Я отказываюсь танцевать с этими штуками, направленными на меня!","angry","worriedCl")
                            call her_main("Вы должны убрать их или танцы закончатся!")
                            m "Ты не в том положении, чтобы нам приказывать, [hermione_name]."
                            call her_main("Это был не приказ, [genie_name]. Это был ультиматум.","clench","angry",emote="01")

                            menu:
                                m "..."
                                "\"Ладно, Северус, будем цивилизованны...\"":
                                    hide screen hermione_main
                                    with d3
                                    pause.2
                                    call sna_head("Я вижу, мисс Грейнджер удается оставаться упрямой в любой ситуации...","snape_03")
                                    call blkfade

                                    hide screen chair_left
                                    hide screen desk
                                    show screen genie
                                    call her_chibi("stand","on_desk","on_desk")
                                    call sna_chibi("stand","desk","base")
                                    pause.3
                                    hide screen snape_main
                                    hide screen hermione_main
                                    hide screen bld1
                                    hide screen blktone
                                    call hide_blkfade
                                    jump civil_with_snape

                                "\"(Псс! Помнишь, почему мы это делаем!)\"":

                                    #Hermione is ok with it.
                                    if whoring >= 15:

                                        call her_main("Ох, хорошо...","shock","wide")
                                        call sna_head("Что это было?","snape_05")
                                        call her_main("Пожалуйста, не обращайте внимания на то, что я только что сказала...","silly","worriedCl",emote="05")
                                        call sna_head("Хм... ?","snape_05")
                                        call her_main("Я не против, что вы трогаете свои штуки передо мной....","silly","worriedCl",emote="05")
                                        call her_main("Да, я совсем не против этого...")
                                        call her_main("И я продолжу танцевать...")

                                        call nar(">Пока смотришь, как танцует Гермиона, ты продолжаешь дрочить...","start")
                                        call nar(">Гермиона сжимает грудь и слегка трясет бедрами...","end")

                                        m "Да, [hermione_name]. Очень хорошо."
                                        call sna_head("*Кхем!* Неплохое выступление, мисс Грейнджер.","snape_12")
                                        call her_main("....................","angry","worriedCl")
                                        m "Хех..."
                                        m "Итак, как бы ты оценил ее грудь?"
                                        call her_main("......","open","wide")
                                        call sna_head("Хм......","snape_13")
                                        call her_main("........","annoyed","angryL")
                                        call sna_head("\"4+\"!","snape_12")
                                        call her_main("!!!","open","wide")
                                        m "Серьезно?"
                                        call sna_head("Да. Я всегда отдаю должное хорошей груди.","snape_12")
                                        call her_main("(Профессор...)","annoyed","closed")
                                        call her_main("(Время для моего заключительного акта!)","open","closed")
                                        pause.1

                                        $ hermione_wear_panties = False
                                        call set_hermione_action("pinch")
                                        pause.5

                                        call nar(">Гермиона наклоняется и снимает трусики.","start")
                                        ">Ее изящные движения..."
                                        ">Но красивая киска всегда было желанным зрелищем, тем не менее..."
                                        hide screen blktone
                                        call nar(">Вы показываете свою признательность, дроча еще быстрее...","end")
                                        call ctc

                                        show screen blktone
                                        call sna_head("Да... Да!!!","snape_18")
                                        call sna_head("Теперь потряси своими \"четыре с плюсом\" для меня, шлюха!")
                                        call her_main(".......","angry","worriedCl")

                                        call set_hermione_action("none","skip_update")
                                        pause.5

                                        call nar(">Гермиона неожиданно врывается в серию довольно сложных пируэтов.")
                                        call sna_head("Да, так изящно...","snape_19")
                                        call sna_head("Это гибкое, молодое тело!","snape_20")
                                        call her_main(".........","grin","ahegao")
                                        call sna_head("Ох, да!","snape_20")
                                        call her_main("{size=-5}(три-два-один... три-два-один... и шаг!){/size}","grin","ahegao")
                                        call nar(">Гермиона, кажется, очень сосредоточена на своем танце...")
                                        call sna_head("Да, а теперь еще один пируэт!","snape_19")
                                        call sna_head("Великолепно!")
                                        call sna_head("Я бы поаплодировал тебе, но одна моя рука сейчас очень занята.","snape_13")
                                        m "{size=-4}(Это была попытка пошутить?){/size}"
                                        m "{size=-4}(Хм, возбужденный Снейп такой странный...){/size}"
                                        call blkfade

                                        ">Гермиона выполняет еще один набор движений и пируэтов..."
                                        ">Делает небольшой реверанс воображаемой публике..."
                                        ">И после этого устало шлепается на задницу."

                                        call her_chibi("sit_naked","on_desk","on_desk")

                                        hide screen snape_main
                                        hide screen hermione_main
                                        hide screen blktone
                                        hide screen bld1
                                        call hide_blkfade
                                        call ctc

                                        show screen bld1
                                        call her_main("Ух... Это было--","open","closed")
                                        with hpunch

                                        g4 "АХ! ЧЕРТОВА ШЛЮХА!"

                                        hide screen bld1
                                        with d3

                                        call cum_block

                                        call gen_chibi("cumming","behind_desk","base")
                                        pause.2

                                        $ uni_sperm = True #Triggers universal sperm to show on hermione_main screen.
                                        $ u_sperm = "characters/hermione/face/auto_04.png"

                                        call her_main("??!!!","shock","wide")
                                        call her_main("","angry","worriedCl")
                                        call ctc

                                        call sna_head("Хорошая работа, шлюшка!","snape_18")
                                        call sna_head("Вот твоя награда!","snape_21")

                                        call cum_block

                                        call sna_chibi("cumming","desk","base")
                                        pause.2

                                        $ uni_sperm = True #Triggers universal sperm to show on hermione_main screen.
                                        $ u_sperm = "characters/hermione/face/auto_05.png"

                                        call her_main("!!!!!!!!!!!","shock","wide")
                                        call ctc

                                        call sna_head("Ох... Да...","snape_21")
                                        g4 "Маленькая шлюха!"
                                        call her_main("...............................","grin","ahegao")

                                        $ s_c_c_u_pic = "images/animation/11_cum_18.png"
                                        $ g_c_c_u_pic = "images/animation/09_cum_18.png"

                                        call sna_head("Ха-ха-ха! Это было превосходно!","snape_21")
                                        g9 "Я знаю!"

                                        call gen_chibi("hold_dick","behind_desk","base")
                                        call sna_chibi("hold_dick","desk","base")
                                        pause.2

                                        call bld
                                        call sna_head("Да... Мы должны делать это почаще.","snape_22")
                                        call her_main(".................","grin","ahegao")

                                        call sna_head("Ваше выступление было приемлемым, мисс Грейнджер...","snape_20")
                                        call her_main("Спасибо................","annoyed","dead")
                                        call sna_head("Но я оценил бы его на...","snape_19")
                                        call her_main("...........","annoyed","dead")
                                        call sna_head("Хм....","snape_22")
                                        call her_main("............","annoyed","dead")
                                        call sna_head("\"{size=+5}2+{/size}\"!","snape_10")
                                        stop music

                                        hide screen bld1
                                        show screen blktone
                                        call her_main("{size=+5}Что?!!!{/size}","shock","wide")
                                        call sna_head("Да... Довольно много над чем стоит поработать.","snape_09")
                                        call play_music("chipper_doodle") # HERMIONE'S THEME.
                                        call her_main("Не могу в это поверить!","clench","angry",emote="01")
                                        call ctc
                                        call blkfade

                                        ">Гермиона в ярости спрыгивает со стола."
                                        pause 2
                                        hide screen hermione_main
                                        hide screen chair_left
                                        hide screen desk
                                        show screen genie
                                        call sna_chibi("hold_dick","mid","base")
                                        call her_chibi("stand","desk","base",flip=True)
                                        hide screen bld1
                                        hide screen blktone
                                        call hide_blkfade
                                        call ctc

                                        $ flip = True # Flips hermione_main screen.
                                        $ u_sperm = "characters/hermione/face/auto_05.png"

                                        show screen bld1
                                        call her_main("Я требую более высокую оценку!","soft","angry",xpos="right",ypos="base")
                                        call sna_head("Вы не требуете оценку мисс Грейнджер, вы ее зарабатываете.","snape_09")
                                        call her_main("Я действительно заслужила!","open","baseL")
                                        call her_main("И не могли бы вы, по крайней мере, быть цивилизованнее, перестать трогать себя, профессор!","annoyed","angryL")
                                        call sna_head("Пф...","snape_12")
                                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        with d3
                                        m "(Они по-настоящему?)"
                                        hide screen bld1
                                        with d3
                                        pause.2
                                        call blkfade

                                        ">Ты видишь, как Снейп, со все еще стоящим членом и заляпанная спермой Гермиона громко спорят о неправильной воображаемой оценке."
                                        ">Через некоторое время профессор Снейп соглашается изменить оценку Гермионы с \"2+\" на \"3-\"."
                                        ">После чего поспешно уходит, пока Гермиона снова не начала спорить..."
                                        pause 2

                                        $ flip = False # Flips hermione_main
                                        $ aftersperm = True #Show cum stains.
                                        $ uni_sperm = False #Don't show cum.
                                        call sna_chibi("stand","mid","base",flip=True)
                                        call hide_blkfade

                                        call sna_walk("mid","leave",2)
                                        pause.5

                                        call her_chibi("stand","desk","base")
                                        pause.2

                                        show screen bld1
                                        call her_main("Что ж...","annoyed","worriedL",xpos="mid",ypos="base")
                                        her "Наша миссия успешна, [genie_name]?"

                                        menu:
                                            m "..."
                                            "\"А? Какая миссия?\"":
                                                $ mad += 7
                                                call her_main("Я согласилась на это только для того, чтобы вы могли поймать профессора Снейпа с поличным, [genie_name]!","scream","worriedCl")
                                                call her_main("Чтобы у нас были доказательства, что он замешан в \"Грязных\" делишках!","normal","worriedCl")
                                                m "Ах, эта миссия..."
                                                m "Да. Миссия выполнена!"
                                            "\"Да! Спасибо тебе!\"":
                                                pass

                                        m "Хорошая работа, [hermione_name]."
                                        call her_main("Я рада была помочь, [genie_name]!","normal","worriedCl")
                                        pause.5
                                        call blkfade

                                        call her_head("...Могу ли я получить очки, пожалуйста?","angry","worriedCl",emote="05")
                                        jump done_with_dancing #Blkfade needs to be active!

                                    #Hermione is ok with it.
                                    else:

                                        call her_head("Ох...","open","wide")
                                        call her_head("Нет, не могу! Это просто того не стоит!","angry","worriedCl")
                                        call blkfade

                                        ">Гермиона спрыгивает со стола и начинает надевать одежду."
                                        call sna_head("Ну, это было ужасно...","snape_03")
                                        g4 "И не говори..."
                                        call sna_head("Я полагаю, теперь можно идти. Я поговорю с тобой позже, Альбус.","snape_03")
                                        m "Да, поговорим позже, Северус."
                                        call sna_head("Мисс Грейнджер...","snape_04")
                                        call her_head("Профессор...","angry","worriedCl")

                                        call sna_chibi("hide")
                                        call her_chibi("stand","desk","base")
                                        call play_sound("door")
                                        ">Профессор Снейп уходит..."
                                        stop music fadeout 1.0

                                        call her_head("....................","annoyed","dead")
                                        pause.5
                                        ">..............{w}..................{w}...................."

                                        call her_head("...Могу ли я получить очки... [genie_name]... ?","normal","worriedCl")
                                        jump done_with_dancing #Blkfade needs to be active!


                        "-Продолжать смотреть-":
                            label civil_with_snape:
                                call play_music("dark_fog")

                            call her_chibi("dance","on_desk","on_desk")
                            pause.5

                            show screen blktone
                            call her_main("Тогда я продолжу танцевать....","open","closed")
                            call ctc

                            call nar(">Гермиона сжимает грудь и слегка трясет бедрами...")

                            m "Да, [hermione_name]. Очень хорошо."
                            call sna_main("*Кхем!* Неплохое выступление, мисс Грейнджер.","snape_12")
                            call her_main("....","open","closed")
                            m "Хех..."
                            m "Так... Как бы ты оценил ее сиськи?"
                            call her_main("......","annoyed","closed")
                            call sna_main("Хм......","snape_20")
                            call her_main("........","annoyed","closed")
                            call sna_main("\"4+\"!","snape_12")
                            call her_main("!!!","open","wide")
                            m "Серьезно?"
                            call sna_main("Да. Я всегда отдаю должное хорошей груди.","snape_12")
                            call her_main("(Профессор...)","angry","wide")
                            call her_main("(Тогда время для моего заключительного акта!)","open","closed")
                            pause.1

                            $ hermione_wear_panties = False
                            call set_hermione_action("pinch")
                            pause.5

                            call nar(">Гермиона наклоняется и снимает трусики.","start")
                            ">Ее изящные движения..."
                            hide screen blktone
                            call nar(">Но красивая киска всегда была, тем не менее желанным зрелищем...","end")
                            call ctc

                            show screen blktone
                            call sna_main("Да... Да...","snape_20")
                            sna "Потряси этими сиськами для меня, шлюха!"
                            call her_main(".......","angry","worriedCl")

                            call set_hermione_action("none","skip_update")
                            pause.5

                            call nar(">Гермиона неожиданно врывается в серию довольно сложных пируэтов.")
                            call sna_main("Да, так изящно...","snape_19")
                            call sna_main("Это гибкое, молодое тело!","snape_20")
                            call her_main("{size=-5}(три-два-один... три-два-один... и шаг!){/size}","open","closed")
                            call nar(">Гермиона, кажется, очень сосредоточена на своем танце...")
                            call sna_main("Да, а теперь еще один пируэт!","snape_19")
                            call sna_main("Великолепно!")
                            call blkfade

                            ">Гермиона выполняет еще один набор движений и пируэтов..."
                            ">Делает небольшой реверанс воображаемой публике..."
                            ">И после этого измученно падает на задницу"

                            call her_chibi("sit_naked","on_desk","on_desk")

                            hide screen snape_main
                            hide screen hermione_main
                            hide screen blktone
                            hide screen bld1
                            call hide_blkfade
                            call ctc

                            show screen bld1
                            call sna_main("Молодец, проститутка!","snape_22")
                            call her_main(".............","soft","squintL")

                            if daytime:
                                call sna_main("Вот-вот начнутся занятия, я ухожу.","snape_22")
                                sna "Разве у тебя нет сегодня урока по зельям со мной, мисс Грейнджер?"
                                call her_main("Есть, [genie_name]...","annoyed","dead")
                                call sna_main("Ну, тогда не опаздывай, девочка...","snape_22")
                            else:
                                call sna_main("Сейчас довольно поздно. Я пойду.","snape_22")
                                sna "Доброй ночи, Альбус."
                                m "Северус."
                                call sna_main("Шлюха.","snape_22")
                                call her_main("Профессор...","annoyed","dead")

                            call ctc

                            hide screen hermione_main
                            hide screen snape_main
                            call blkfade

                            ">Профессор Снейп уходит..."
                            stop music fadeout 1.0
                            call her_head("....................","annoyed","dead")
                            pause.5
                            ">..............{w}..................{w}...................."

                            call her_head("Могу ли я... получить очки [genie_name]... ?","normal","worriedCl")
                            jump done_with_dancing #Blkfade needs to be active!

                ### SNAPE NOT INVITED ###
                "-\"Нет... Это не очень хорошая идея...\"-":
                    label no_snape_watching:
                    hide screen blktone
                    hide screen hermione_main
                    with d3

                    m "[hermione_name], как насчет другого стриптиза?"
                    call her_main("..............","disgust","glance",xpos="base",ypos="base")
                    her "Я скорее откажусь, [genie_name]..."
                    m "Почему? С каждым разом у тебя получается все лучше и лучше."
                    call her_main(".........................","annoyed","annoyed")
                    call her_main("Тридцать пять очков?","open","down")
                    m "Конечно! Обычная ставка."
                    call her_main("...................","annoyed","angryL")
                    hide screen hermione_main
                    hide screen bld1
                    with d3
                    pause.5


                    #Walks to the door
                    call her_walk("mid","door",2)
                    pause.2
                    $ tt_xpos=670
                    $ tt_ypos=200
                    show screen thought
                    with d3
                    pause.5
                    $ renpy.play('sounds/09_lock.wav') #Sound of a door opening.
                    hide screen thought
                    with d3
                    pause.2

                    #Returns from the door
                    m "??!"
                    pause.2

                    call her_chibi("stand","door","base")
                    pause.1

                    call her_walk("door","mid",3)
                    pause.2

                    show screen bld1
                    call her_main("На всякий случай...","annoyed","angryL")
                    stop music fadeout 1.0

                    hide screen bld1
                    with d3

                    call her_walk("mid","desk",3, redux_pause = 2,loiter=False)
                    call blkfade
                    pause.5

                    $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking.
                    pause 3
                    call her_chibi("dance","on_desk","on_desk")

                    call her_head("Просто для протокола...","open","closed")
                    call her_head("Я все еще считаю, что это совершенно недопустимо - покупать одну из своих студенток, [genie_name].","annoyed","suspicious")
                    m "Правильно. И еще более неуместно продавать себя своему директору. Согласна?"
                    call her_head("..........","annoyed","angryL")

                    call hide_blkfade
                    call ctc

                    call play_music("playful_tension") # SEX THEME.
                    show screen blktone
                    call her_main("..............","open","down",xpos="mid",ypos="base")
                    call her_main("Что если мои родители узнают об этом, [genie_name]?","disgust","down_raised")
                    call her_main("Мама никогда не поймет...")
                    call her_main("Что касается моего отца...","upset","wink")

                    menu:
                        m "..."
                        "{size=-3}\"Твой отец гордился бы тобой!\"{/size}":
                            call her_main("Я сомневаюсь...")
                            call her_main("Да, я делаю это по веским причинам, но...")
                            call her_main("Он бы никогда не увидел это с такого ракурса...","annoyed","angry")
                            call her_main("Он не должен узнать об этом...")
                        "{size=-3}\"Твой отец отшлепает тебя!\"{/size}":
                            call her_main("Он не будет!","shock","wide")
                            call her_main("И я, все равно, уже взрослая для этого...","upset","wink")
                            g9 "Я бы сказал, что ты находишься в идеальном возрасте для этого..."
                            call her_main("А?")
                            call her_main("Я не понимаю, что вы имеете в виду, [genie_name].","grin","worriedCl",emote="05")
                        "{size=-3}\"Твой отец отрекся бы от тебя!\"{/size}":
                            call her_main("Вы, наверное, правы, [genie_name]...","angry","worriedCl",emote="05")
                            call her_main("(Ох, папочка, мне очень жаль....)","angry","base",tears="soft")
                            call her_main("Он не должен узнать...","angry","base",tears="soft")
                        "{size=-3}\"Твой отец хотел бы посмотреть, как ты раздеваешься!\"{/size}":
                            call her_main("Он бы не стал! Ему было бы стыдно за меня!","normal","worriedCl")
                            m "Ты уверена?"
                            call her_main("Безусловно! Мой отец-честный человек!","scream","worriedCl")
                            m "Но он {size=+4}муж{/size}чи{size=+4}на{/size}, Верно?"
                            call her_main(".....................","annoyed","annoyed")
                            call her_main("Мой отец не должен узнать об этом...","annoyed","worriedL")

                    call nar(">Гермиона начинает соблазнительно покачивать бедрами...")

                    $ hermione_wear_panties = True
                    call set_hermione_action("lift_skirt")
                    pause.5

                    $ hermione_wear_bottom = False
                    call set_hermione_action("None","skip_update")
                    pause.2

                    call nar(">Ее юбка сползает...")
                    call ctc

                    call her_main("[genie_name]?","open","base")
                    m "А?"
                    call her_main("Могу я задать вам вопрос?","upset","wink")
                    m "Давай..."
                    call her_main("...............","normal","worriedCl")
                    call her_main("Вы когда-нибудь были влюблены... ?","grin","worriedCl",emote="05")

                    menu:
                        m "..."
                        "\"Не смеши! Любовь-это ложь!\"":
                            call her_main("Мне жаль, что вы так думаете, [genie_name]!","annoyed","worriedL")
                            call her_main("Но вы же можете ошибаться!","annoyed","annoyed")
                            call her_main("Я верю, что истинная любовь-это то, что заставляет землю вращаться!","base","baseL")
                            m "Собственно, за это отвечает angular momentum, сохранение импульса."
                            call her_main("А?","upset","wink")
                            m "Неважно. Просто сними уже рубашку?"
                            call her_main("............","annoyed","annoyed")
                        "\"Продолжай молча танцевать!\"":
                            call her_main("Но вы сказали, что я могу задать вам вопрос...","annoyed","annoyed")
                            m "И?"
                            call her_main("!!!............","open","base")
                            call her_main("....................................","annoyed","annoyed")
                            m "Теперь молча сними рубашку."
                            call her_main("........","annoyed","angryL")
                        "\"Да... очень давно...\"":
                            m "Да... очень давно..."
                            call her_main("??! !!! ..............................","open","base")
                            m "Ее зовут Эден..."
                            call her_main("Она была красива?","base","base")
                            m "Более чем..."
                            m "Она была умна, зелена и совершенна..."
                            call her_main("Она была...{w} \"зелена\"... ?","open","down")
                            call her_main("Вы издеваетесь, [genie_name]?","angry","angry")
                            m "Ох, вы, люди, ничего не знаете о настоящей любви..."
                            call her_main("..................................... ?","soft","base")
                            m "Эмм... Я имею в виду, сними рубашку, [hermione_name]!"
                            call her_main(".................","annoyed","angryL")
                        "\"Я чувствую, что я влюблен прямо сейчас!\"":
                            call her_main("Вам не обязательно быть таким вульгарным, [genie_name].","annoyed","angryL")
                            m "Ох, но мне кажется, что это так!"
                            call her_main("[genie_name], пожалуйста!","disgust","glance")
                            call her_main("Я одна из ваших учениц!","soft","base")
                            call her_main("И вы старше моего отца!","grin","worriedCl",emote="05")
                            m "{size=-4}(Даже не представляешь, насколько, девочка.){/size}"
                            call her_main("Хотя некоторые ученые считают, что \"любовь\" - это не что иное, как химическая реакция...","soft","base")
                            call her_main("И когда человек испытывает сексуальное возбуждение, тот же самый тип гормонов--","open","closed")
                            m "[hermione_name]!"
                            call her_main("Да, [genie_name]?","soft","base")
                            m "Ты забыла, где находишься??"
                            call her_main("Ой, простите, [genie_name]... Иногда я отвлекаюсь.","grin","worriedCl",emote="05")
                            m "Сними уже рубашку, наконец?!"
                            call her_main("Точно...","annoyed","worriedL")

                    call nar(">Гермиона расстегивает последнюю пуговицу рубашки...")

                    $ hermione_wear_bra = False
                    call set_hermione_action("lift_top")
                    pause.5

                    $ hermione_wear_top = False
                    call set_hermione_action("None","skip_update")
                    pause.2

                    call nar(">Нежно снимает рубашку и изящно скидывает ее...")
                    call ctc

                    g9 "Да! Сиськи!"

                    call her_main("Вам обязательно быть настолько пошлым, [genie_name]?","annoyed","closed")

                    menu:
                        "-Начать дрочить-":
                            call blkfade

                            call her_head("[genie_name]?!","open","wide")
                            m "Все в порядке, [hermione_name]. Не обращай внимание..."


                            hide screen genie
                            hide screen no_shirt_no_skirt_dance
                            show screen chair_left
                            call gen_chibi("jerking_off","behind_desk","base")
                            hide screen desk
                            show screen desk
                            call her_chibi("dance","on_desk","on_desk")
                            hide screen blktone
                            call hide_blkfade
                            call ctc

                            call bld
                            call her_head("Н-но...","angry","wide")
                            call her_head("Ваш...")
                            m "Да... Ах, да, потрясающе..."
                            call her_head("[genie_name]!!!","scream","worriedCl")
                            call her_head("Я настаиваю, чтобы вы убрали свою...","angry","worriedCl")
                            call her_head("...штуковину.")

                            menu:
                                m "..."
                                "\"Я сказал, продолжай танцевать, [hermione_name]!\"":
                                    if whoring >= 15: #LEVEL 06. You jerk off your cock and Hermione is OK with it.
                                        call her_head("Но...","angry","worriedCl")
                                        call her_head(".............................")
                                        call her_head("Ну, ладно, но только если вы пообещаете не кончать, [genie_name].","soft","angry")
                                        menu:
                                            m "..."
                                            "-Пообещать ей-":
                                                    $ d_flag_07 = True #Promised to hold it.
                                                    call her_head("Ну, тогда, ладно...","open","closed")
                                            "-Не давать обещание-":
                                                $ d_flag_07 = False #Did not promise to hold it.
                                                m "\"Не кончать\"? Это похоже на пытку!"
                                                m "Пожалуйста, держи свои садистские мысли при себе, [hermione_name]."
                                                call her_head("У меня нет ни каких... садистских мыслей, [genie_name]!","annoyed","angryL")
                                                call her_head("Я просто не хочу...")
                                                g9 "Да... Какие красивые у тебя сиськи..."
                                                call her_head("............","angry","worriedCl")
                                                g9 "А-ах... Да..."
                                                call her_head("..........","angry","worriedCl")
                                                call her_head("Ладно! Будь по-вашему, [genie_name]!","angry","worriedCl")
                                                call her_head("{size=-5}(Как обычно...){/size}","annoyed","angryL")

                                        hide screen bld1
                                        show screen blktone
                                        call nar(">Ты продолжаешь дрочить, наблюдая за Гермионой...")
                                        call her_main("Время для заключительного акта...","annoyed","closed")
                                        m "Да, [hermione_name]! Сними их!"
                                        call her_main("........","annoyed","dead")
                                        if h_request_wear_panties or hermione_wear_panties:
                                            call nar(">Гермиона слегка наклоняется и снимает трусики...")

                                            $ hermione_wear_panties = False
                                            call set_hermione_action("pinch")
                                            pause.5

                                            call set_hermione_action("None","skip_update")
                                            pause.2

                                        call nar(">Ты замечаешь, что она делает все возможное, чтобы быть грациозной...","start")
                                        call nar(">Но она выглядит довольно нелепо в своих попытках вести себя как профессиональная стриптизерша...","end")
                                        call ctc

                                        call nar(">Тем не менее, ты делаешь вид, что у нее получается весьма неплохо...","start")
                                        call nar(">Начиная дрочить еще быстрее!","end")
                                        call her_main("..........","annoyed","dead")
                                        call nar(">Вдруг Гермиона начинает выдавать целую серию довольно сложных пируэтов...")
                                        m "{size=-4}(Это выглядит довольно впечатляюще...){/size}"

                                        call set_hermione_action("fingering")
                                        pause.5

                                        call nar(">Гермиона сжимает грудь, а затем еще одна серия довольно сложных движений...")
                                        call ctc

                                        m "{size=-4}(Она практиковалась в этом?){/size}"
                                        g9 "Ох, какое мне дело?"
                                        call nar(">Ты начинаешь еще сильнее надрачивать свой твердый, как камень, член.")
                                        call her_main("{size=-5}(Три-два-один... три-два-один... шаг!){/size}","open","closed")

                                        call set_hermione_action("none","skip_update")
                                        pause.5

                                        call nar(">Гермиона выполняет еще одну серию довольно изящных движений...","start")
                                        call nar(">Ее упругие сиськи подпрыгивают в такт...","end")

                                        g9 "Да, да, маленькая шлюха!"
                                        call nar(">Еще несколько движений, пара жестов и небольшой поклон воображаемой публике...")
                                        call blkfade

                                        call her_chibi("sit_naked","on_desk","on_desk")

                                        ">И под конец она падает на свою попку."

                                        hide screen hermione_main
                                        hide screen blktone
                                        call hide_blkfade
                                        call ctc

                                        call her_head("Фиу... Это было--","open","closed")
                                        with hpunch
                                        g4 "ДААА! ЕБАНАЯ ДЫРКА!"

                                        call cum_block

                                        call gen_chibi("cumming","behind_desk","base")
                                        call ctc

                                        $ uni_sperm = True #Triggers universal sperm to show on hermione_main screen.
                                        $ u_sperm = "characters/hermione/face/auto_04.png"

                                        call her_chibi("sit_naked_shocked","on_desk","on_desk")

                                        call her_head("??!!!","shock","wide")

                                        call bld
                                        call her_head("[genie_name]!!!","angry","worriedCl")

                                        call gen_chibi("hold_dick","behind_desk","base")

                                        $ g_c_c_u_pic = "images/animation/09_cum_18.png"
                                        $ genie_cum_chibi_xpos = -45
                                        $ genie_cum_chibi_ypos = 5
                                        show screen g_c_c_u

                                        if d_flag_07: #Promised to hold it.
                                            call her_head("Нет, [genie_name]! Вы же обещали!","angry","worriedCl")
                                            g4 "Ох, детка... Это было довольно круто..."
                                            call her_head("Вы нарушили свое слово, [genie_name]!","scream","worriedCl")
                                            m "А? О чем ты говоришь?"
                                            call her_head("Как вы могли поступить так со мной, [genie_name]?","shock","angry",tears="crying_blink")
                                            m "Ох, успокойся, [hermione_name]."
                                            m "Ты заработала свои очки."
                                            m "Теперь просто одевайся и уходи, пока кто-нибудь не застукал нас..."
                                            call her_head("*всхлип!*........................","shock","angryL",tears="messy")
                                            $ mad += 30
                                            call blkfade

                                            $ uni_sperm = False #Sperm layer is not displayed.
                                            $ aftersperm = True #Aftersperm layer is displayed.
                                            stop music fadeout 5.0
                                            ">..............{w}..................{w}...................."
                                            call her_head("...Могу ли я получить свои очки, [genie_name]... пожалуйста?","annoyed","angryL")
                                            jump done_with_dancing

                                        else:
                                            call her_head("Она такая горячая...","angry","worriedCl")
                                            call gen_chibi("hold_dick","behind_desk","base")
                                            m "А-ах... Да... Это великолепно..."
                                            call her_head("Вы всю меня обкончали...","soft","squintL")
                                            call her_head("Я же ваша ученица...")
                                            call her_head("Вы просто кончили на меня...","grin","ahegao")
                                            g9 "Я знаю! Довольно круто, да?!"
                                            call her_head("Ничего подобного!","open","baseL")
                                            #her "You should not have done this, [genie_name]!"
                                            call her_head("Вам следовало сдерживать себя, как подобает директору!")
                                            m "Правда? Что ты ожидала от меня?"
                                            m "Чтоб я направил на стену или просто положил его обратно в брюки и кончил?"
                                            call her_head("........","soft","squintL")
                                            call her_head("Тем не менее, вы не должны были...","soft","angry")
                                            call her_head("Я согласилась исполнить для вас стриптиз...","open","closed")
                                            call her_head("Но я не соглашалась на такое.")
                                            m "Думаю, я знаю, к чему все идет..."
                                            call her_head("Я требую доплаты!","base","angry")
                                            m "Конечно..."

                                            menu:
                                                m "..."
                                                "\"Ты получишь 1 очко.\"":
                                                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                                                    call her_head("Одно дополнительное очко?","soft","angry")
                                                    call her_head("Одно жалкое очко за все здесь произошедшее?","scream","worriedCl")
                                                    call her_head("Это просто оскорбительно, [genie_name]!","soft","angry")
                                                    m "Одно очко, [hermione_name]. Бери и уходи."
                                                    hide screen g_c_c_u
                                                    call her_chibi("sit_naked","on_desk","on_desk")
                                                    show screen g_c_c_u

                                                    call her_head(".............","annoyed","angryL")
                                                    call her_head("Я возьму.","soft","angry")
                                                    $ mad += 30
                                                    $ current_payout = 36
                                                    hide screen bld1
                                                    call ctc

                                                    call blkfade
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing

                                                "\"Десять дополнительных очков.\"":
                                                    $ current_payout = 45
                                                    call her_head("10 очков [genie_name]?","soft","angry")
                                                    call her_head("Но это слишком мало!")
                                                    m "10 очков. Берешь и уходищь, [hermione_name]."
                                                    hide screen g_c_c_u
                                                    call her_chibi("sit_naked","on_desk","on_desk")
                                                    show screen g_c_c_u

                                                    call her_head("...............","annoyed","angryL")
                                                    call her_head("Ну, хорошо... Это лучше, чем ничего...","soft","angry")
                                                    $ mad += 11
                                                    hide screen bld1
                                                    call ctc

                                                    call blkfade
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing

                                                "\"Ты получишь 25 дополнительных очков.\"":
                                                    $ current_payout = 60
                                                    hide screen g_c_c_u
                                                    call her_chibi("sit_naked","on_desk","on_desk")
                                                    show screen g_c_c_u

                                                    call her_head("Да, я считаю, что это будет вполне достаточно.","open","closed")
                                                    m "Теперь ты счастлива?"
                                                    call her_head("Да, [genie_name]. Спасибо [genie_name].","open","closed")
                                                    hide screen bld1
                                                    with d3
                                                    call ctc
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing

                                                "\"Ты получишь 50 дополнительных очков.\"":
                                                    $ current_payout = 85
                                                    call her_head("Серьезно?!","angry","wide")
                                                    hide screen g_c_c_u
                                                    call her_chibi("sit_naked","on_desk","on_desk")
                                                    show screen g_c_c_u

                                                    call her_head("Ох, я не знаю, что и сказать...","open","wide")
                                                    m "Мне понравилось твое выступление [hermione_name]."
                                                    call her_head("Спасибо [genie_name]...","base","glance")
                                                    m "А еще мне понравилось поливать твое гибкое тело своей спермой..."
                                                    call her_head("[genie_name]......","silly","worriedCl",emote="05")
                                                    m "Так что позволь мне выразить свою признательность."
                                                    m "50 очков. Заслуженных, [hermione_name]."
                                                    call her_head("Огромное спасибо, [genie_name].","silly","worriedCl",emote="05")
                                                    hide screen bld1
                                                    call ctc

                                                    call blkfade
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing

                                                "\"Ты ничего не получишь!\"":
                                                    stop music fadeout 1.0
                                                    call her_head("Что? Даже за танец?","shock","wide")
                                                    menu:
                                                        m "..."
                                                        "\"Ох, нет, за танец получишь.\"":
                                                            $ mad += 30
                                                            call her_head("Как щедро с вашей стороны, [genie_name].","soft","angry")
                                                            hide screen bld1
                                                            call ctc

                                                            call blkfade
                                                            $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                            jump done_with_dancing

                                                        "\"Нет, даже этого нет!\"":
                                                            call play_music("chipper_doodle") # HERMIONE'S THEME.
                                                            call her_head("?! !!","shock","wide")
                                                            call her_head("Я танцевала для вас, [genie_name]...")
                                                            call her_head("Я унижалась ради вашего развлечения...","soft","squintL")
                                                            call her_head("Позволила кончить на себя...","open","baseL")
                                                            with hpunch
                                                            call her_head("И я ничего не получу?!","clench","angry",emote="01")
                                                            m "Ты провалилась, [hermione_name]!"
                                                            call her_head("Ох, это низко даже для вас, [genie_name]!","soft","angry")
                                                            m "Я сказал, ты свободна."
                                                            call her_head("*Агрх!*","clench","angry",emote="01")
                                                            $ mad += 50
                                                            hide screen bld1
                                                            call ctc

                                                            call blkfade
                                                            call gen_chibi("hide")
                                                            hide screen g_c_c_u # Genie's sperm. Universal.
                                                            hide screen chair_left
                                                            hide screen desk
                                                            show screen genie
                                                            show screen bld1
                                                            call her_chibi("stand","desk","base")
                                                            pause.1
                                                            call hide_blkfade
                                                            call music_block
                                                            jump could_not_flirt #Leaves without getting any points.


                                    else: # You jerk off your cock and Hermione is NOT OK with it.
                                        stop music fadeout 1.0

                                        call her_head("Нет, [genie_name]!","annoyed","angryL")
                                        m "А?"
                                        call blkfade

                                        ">Гермиона спрыгивает со стола и начинает спешно одеваться, посматривая на тебя..."
                                        m "Ох, да ладно! Не оставляй меня так!"

                                        call her_head("Танцы закончились, [genie_name]!","soft","angry")
                                        pause 1
                                        call her_head("Я хотела бы получить очки!","annoyed","annoyed")
                                        m "Упрямая [hermione_name]..."
                                        ">Ты неохотно убираешь свой член..."
                                        call her_head("Я хотела бы получить очки.","annoyed","annoyed")
                                        jump done_with_dancing

                                "\"Ладно. Не драматизируй ты так!\"":
                                    call her_head("......................","annoyed","angryL")
                                    pause.1

                                    hide screen chair_left
                                    hide screen g_c_u
                                    hide screen desk
                                    call gen_chibi("hide")
                                    show screen genie
                                    call her_chibi("dance","on_desk","on_desk")
                                    hide screen blktone
                                    hide screen bld1
                                    with fade
                                    pause.5

                                    pass

                        "-Просто смотреть-":
                            pass


                    # JUST WATCHING.
                    call blktone
                    call nar(">Ты смотришь на танец Гермионы...")
                    call her_main("(Время для заключительного акта...)","angry","worriedCl")
                    if h_request_wear_panties or hermione_wear_panties:
                        m "Да, [hermione_name]! Снимай их!"
                        call her_main("........","annoyed","closed")

                        $ hermione_wear_panties = False
                        call set_hermione_action("pinch")
                        pause.5

                        call set_hermione_action("None","skip_update")
                        pause.2

                        call nar(">Гермиона слегка наклоняется и снимает трусики...")

                    call nar(">Ты видишь, что она делает все возможное, чтобы быть грациозной...","start")
                    call nar(">Но она выглядит довольно нелепо в своих попытках вести себя как профессиональная стриптизерша...","end")
                    call ctc

                    call her_main("..........","base","glance")

                    call nar(">Вдруг Гермиона врывается в целую серию довольно сложных пируэтов...")
                    m "{size=-4}(Это выглядит довольно впечатляюще...){/size}"

                    call set_hermione_action("fingering")
                    pause.5

                    call nar(">Гермиона сжимает грудь, а затем следует еще одна серия довольно сложных движений...")
                    call ctc

                    m "{size=-4}(Она практиковалась в этом?){/size}"
                    g9 "Почему меня это волнует?"
                    call her_main("{size=-5}(Три-два-раз... и шаг, три-два-раз... поворот!){/size}","open","closed")

                    call set_hermione_action("none","skip_update")
                    pause.5

                    call nar(">Гермиона выполняет довольно сложные движения, которые были бы весьма изящными...","start")
                    call nar("Если бы не ее прыгающие в разные стороны, сиськи...","end")

                    g9 "Да, да, маленькая шлюха!"

                    call nar(">Еще несколько движений, пара жестов и небольшой поклон воображаемой публике...")
                    call blkfade

                    call her_chibi("sit_naked","on_desk","on_desk")

                    ">И тогда Гермиона падает на свою задницу, полностью истощенная."

                    hide screen hermione_main
                    hide screen blktone
                    call hide_blkfade
                    call ctc

                    call her_head("Фух... Это было довольно захватывающе...","silly","worriedCl",emote="05")
                    menu:

                        m "..."
                        "{size=-3}\"Хорошая работа, [hermione_name]! Ты умеешь танцевать!\"{/size}":
                            m "Хорошая работа [hermione_name]!"
                            call her_head("Правда?","base","glance")
                            m "Да! У тебя большой талант к этому!"
                            call her_head("Спасибо [genie_name].","silly","worriedCl",emote="05")
                        "{size=-3}\"Хм... Это было довольно ужасно...\"{/size}":
                            call her_head("Ох... Простите...","soft","squintL")
                            m "Все хорошо... Тебе просто нужно больше практики..."
                            call her_head(" Эм... я буду иметь в виду, [genie_name]...","open","baseL")
                        "{size=-3}\".................................................\"{/size}":
                            call her_head(".......................","silly","worriedCl",emote="05")
                            call her_chibi("sit_naked_shocked","on_desk","on_desk")

                    hide screen bld1
                    call ctc

                    call blkfade


        else: #Stripping only for Genie.
            jump no_snape_watching



    label done_with_dancing:
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    $ gryffindor += current_payout #35
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen s_c_c_u # Snape's sperm. Universal.
    hide screen chair_left
    hide screen desk
    call gen_chibi("hide")
    call sna_chibi("hide")
    show screen genie
    call her_chibi("stand","desk","base")

    call h_action("none")

    show screen bld1
    call hide_blkfade

    m "Да, [hermione_name]. [current_payout] очков \"Гриффиндору\" ."

    call her_main("Спасибо, [genie_name]...","soft","baseL",xpos="base",ypos="base")
    hide screen hermione_main
    hide screen bld1
    with d3

    $ sperm_on_tits = False
    $ uni_sperm = False

    pause.2
    call her_walk("desk","leave",3)

    call reset_hermione_main

    if whoring < 12: #Adds points till 12.
        $ whoring +=1

    $ hg_pf_DanceForMe_OBJ.points += 1

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if daytime:
        call play_music("day_theme")
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        call play_music("night_theme")
        $ hermione_sleeping = True
        jump night_main_menu
