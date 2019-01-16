

### HERMIONE PERSONAL FAVOUR 3 ###

### BREAST MOLESTER (while wearing clothes!) ###

label hg_pf_BreastMolester:
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    m "{size=-4}(Я хочу немного помять ее сиськи. Даже не стану просить их оголить. Безобидная просьба.){/size}"

    if hg_pf_BreastMolester_OBJ.points < 1:
        menu:
            "\"(Да, сделаем это!)\"":
                pass
            "\"(Не сейчас.)\"":
                jump silver_requests

    if hg_msMarvel_OBJ.purchased:
        m "\"(Попросить ее переодеться?)\""
        menu:
            "\"(Да, сделаем это!)\"":
                m "[hermione_name], Прежде чем я скажу о своей просьбе, не могла бы ты переодеться в..."
                call her_main("Во что?","open","worriedL")
                m "Мисс Марвел."
                if whoring >= 7:
                    m "Это ведь не сложно?"
                    call her_main("...","angry","worriedCl",emote="05")
                    call her_main("Хорошо, скоро вернусь.","normal","worriedCl")
                    call play_sound("door") #Sound of a door opening.
                    call set_hermione_outfit(hg_msMarvel_OBJ)
                    pass
                else:
                    jump too_much
            "\"(В другой раз.)\"":
                pass

    if whoring < 3: #Hermione refuses.
        m "[hermione_name], Как вы относитесь к тому чтобы я немного поиграл с твоей грудью?"
        call her_main("Поиграть с...?","shock","wide")
        call her_main("Моими сиськами?!","angry","wide_stare")
        jump too_much

    #First time event
    elif whoring >= 3 and whoring <= 5:

        $ new_request_04_heart = 1 #Event hearts level (0-3)
        $ hg_pf_BreastMolester_OBJ.hearts_level = 1 #Event hearts level (0-3)

        m "Подойди ближе, [hermione_name]..."
        call her_head("Эмм... ладно...","annoyed","angryL",xpos="base",ypos="base")
        hide screen bld1
        hide screen hermione_blink
        with d3

        call her_walk_desk_blkfade

        call her_head("[genie_name].....?","annoyed","angryL")

        menu:
            m "..."
            "\"Я собираюсь поиграть с твоей грудью.\"":
                call her_head("Что? Что вы имеете в виду, [genie_name]--?","soft","wide")
                ">Гермиона на шаг отходит от тебя..."
                ">Ты подходишь и хватаешь ее за грудь обеими руками..."
            "-Просто взять ее за сиськи.-":
                ">Ты подходишь и хватаешь за сиськи Гермиону обеими руками!"

        stop music fadeout 1.0
        with hpunch
        call her_head("?!!!","mad","wide",cheeks="blush")
        call her_head("[genie_name]?!","base","ahegao_raised",cheeks="blush")

        ">Гермиона пытается отойти от тебя, но ты крепко держишь ее за сиськи..."
        call play_music("playful_tension") #SEX THEME.

        call her_head("[genie_name], что вы себе позволяе--?","angry","worriedCl",cheeks="blush",emote="05")
        ">Она снова пытается отойти."
        ">Ты сжимаешь ее сиськи сильнее."

        call her_head("[genie_name], вы делаете мне больно!","angry","suspicious",cheeks="blush")
        g4 "Тогда хватит вырываться, [hermione_name]!"
        call her_head("Н-но.....","soft","wide")
        m "Все что я хочу, это немного помять твою грудь, тогда ты получишь свои очки!"
        call her_head("Н-но... это...","disgust","down_raised",cheeks="blush")
        m "Просто не сопротивляйся..."
        m "Встань на свое место и все..."
        call her_head("М-мое место...?","angry","wink")
        ">Ты чувствуешь красивую грудь девочки в своих ладонях..."

        hide screen genie
        call her_chibi("hide")
        show screen chair_left #Genie's chair.
        show screen groping_03
        with d1
        hide screen bld1
        call hide_blkfade
        call ctc

        call bld
        call her_head("............................","shock","worriedCl")

        $ menu_x = 0.5 #Menu is moved to the left side.
        $ menu_y = 0.3 #Menu is moved to the left side.

        menu:
            "-Сжать ее сиськи со всей силы-":
                call nar(">Ты сжимаешь их сильнее...")
                call her_head("Мои...........","disgust","down_raised",cheeks="blush")
                call nar(">Ты сжимаешь еще сильнее...")
                call her_head("[genie_name], вы делаете мне больно...","shock","worriedCl")
                m "Тише, [hermione_name]..."
                call her_head("Ай..............","disgust","down_raised",cheeks="blush")
                call nar(">Ты сжимаешь со всей силы.")
                call her_head("Ай! Мне больно!","angry","suspicious",cheeks="blush")
                call her_head("Вы их раздавите! Остановитесь, пожалуйста!","angry","suspicious",cheeks="blush")
                m "Я не раздавлю их, глупая девочка..."
                call nar(">Ты немного ослабляешь хватку...")
                call her_head("Мне очень больно...","shock","worriedCl")
                m "Все будет хорошо..."
                call her_head(".........","annoyed","angryL",cheeks="blush")

            "-Нежно помассировать-":
                call nar(">Ты начинаешь немного сжимать грудь Гермионы через ее одежду...")
                call her_head("[genie_name]...?","shock","worriedCl")
                m "Твои очки, [hermione_name]... тебе нужны очки, сконцентрируйся на этом."
                call her_head("Верно...","annoyed","angryL",cheeks="blush")
                call her_head("Да, все ради чести \"Гриффиндора\"...","angry","worriedCl",cheeks="blush")
                "*Жмяк-жмяк!*"
                call nar(">Ты продолжаешь массировать ее сиськи...","start")
                call nar(">Ты пытаешься на ощупь определить где ее соски...","end")
                call her_head("[genie_name]... вы сжимаете их... ?","shock","worriedCl")
                call nar(">Однако это не дает результата, ткань слишком плотная...")
                call her_head("\"Гриффиндор\" ............","angry","worriedCl",cheeks="blush")

            "-Позволить ей уйти-":
                m "Отлично, если ты не передумала делать из этого драму, то можешь уходить..."
                call nar(">Ты отпускаешь грудь девочки...")
                call her_head("Серьезно?","base","baseL",cheeks="blush")
                m "Да, да... я даже дам тебе твои очки..."
                call her_head("Арр... спасибо, [genie_name]...","base","baseL",cheeks="blush")
                m "Хотя ты и не заработала их сегодня..."
                call her_head(".........","disgust","down_raised",cheeks="blush")

    #Second Event
    if whoring >= 6:
        if whoring >= 6 and whoring <= 8:
            $ new_request_04_heart = 2
            $ hg_pf_BreastMolester_OBJ.hearts_level = 2 #Event hearts level (0-3)
        else:
            $ new_request_04_heart = 3
            $ hg_pf_BreastMolester_OBJ.hearts_level = 3 #Event hearts level (0-3)

        stop music fadeout 2.0
        m "Подойди ближе, [hermione_name]... Я хожу сделать массаж твоим сиськами..."
        call her_main("Как скажете, [genie_name]...","base","baseL",cheeks="blush")

        hide screen bld1
        hide screen hermione_main
        with d3

        call her_walk_desk_blkfade

        call play_music("playful_tension") # SEX THEME.
        ">Гермиона начинает стягивать униформу..."

        m "Нет, не раздевайся, я хочу их потрогать пока ты будешь одетой..."
        call her_head("Ох, я поняла...","base","baseL",cheeks="blush",xpos="base",ypos="base")
        ">Гермиона стоит перед тобой в ожидании..."
        ">Ты тянешься руками к ее полной груди..."
        ">Ты начинаешь массировать ее сиськи..."

        hide screen genie
        call her_chibi("hide")
        show screen chair_left #Genie's chair.
        show screen groping_03
        with d1

        hide screen bld1
        call hide_blkfade
        call ctc

        "*Жим-жим-жим*"
        call bld
        call her_head("................","base","ahegao_raised",cheeks="blush")

        $ menu_x = 0.5 #Menu is moved to the left side.
        $ menu_y = 0.3 #Menu is moved to the left side.

        menu:
            "\"Тебе нравится, [hermione_name]?\"":
                call her_head("Что...?","base","baseL",cheeks="blush")
                call her_head("О, ну, я не имею ничего против...","base","baseL",cheeks="blush")
                "*Жим-жим-жим*"
                call nar(">Ты продолжаешь мять ее мягкие сиськи...")

                if whoring <= 12:
                    call her_head("Я имею в виду, это допустимо, пока я получаю за это очки...","base","ahegao_raised",cheeks="blush")
                    call nar(">Ты продолжаешь сжимать ее грудь через одежду...")
                    call her_head("Небольшая цена за честь моего факультета, правда......{image=textheart}","soft","baseL",cheeks="blush")
                else:
                    m "Правда? А мне кажется, что ты полюбила наши занятия."
                    call her_head("Я бы не сказала что люблю это...","base","ahegao_raised",cheeks="blush")
                    call nar(">Ты продолжаешь массировать ее сиськи через униформу...")
                    m "Тогда что бы ты сказала, [hermione_name]?"
                    call her_head("Ну, мне начинает это нравиться, {size=-4} немного {image=textheart}{/size}","base","ahegao_raised",cheeks="blush")

            "-Сильно потянуть за них-":
                call nar(">Ты резко тянешь за сиськи Гермиону...","start")
                with vpunch
                hide screen blktone8
                with d3
                call her_head("Ауч....","angry","worriedCl",cheeks="blush",emote="05")
                call nar(">Ты снова тянешь за них. Заметно сильнее чем в прошлый раз.","start")
                with vpunch
                hide screen blktone8
                with d3
                call her_head("Ауч! [genie_name], чего вы добиваетесь...?","angry","worriedCl",cheeks="blush",emote="05")
                call nar(">Ты дергаешь девочку за сиськи со всей силы...","start")
                with vpunch
                with vpunch
                call nar(">Гермиона едва не теряет равновесие...","end")
                call her_head("*Тяжело дышит* Что вы делаете, [genie_name]...?","open","baseL",cheeks="blush")
                call her_head("Вы не должны быть таким грубым....{image=textheart}","base","baseL",cheeks="blush")

    call blkfade

    hide screen ctc
    hide screen bld1
    hide screen blktone
    hide screen blktone8
    hide screen hermione_blink
    hide screen hermione_main
    hide screen groping_03
    hide screen chair_left #Genie's chair.
    show screen genie
    call her_chibi("stand","desk","base")

    stop music fadeout 1.0
    ">Ты отпускаешь грудь Гермионы..."
    m "Закончим на этом."
    call her_head("................","annoyed","angryL",cheeks="blush")

    call hide_blkfade


    if whoring < 6: #Adds points till 6.
        $ whoring +=1

    if whoring <= 12:
        $ gryffindor +=15
        m " \"Гриффиндор\" получает 15 очков!"
    else:
        m "Теперь можешь идти, [hermione_name]."

    call bld
    call her_main("..................","annoyed","worriedL",xpos="base",ypos="base")
    her "Спасибо, [genie_name]..."

    if daytime:
        her "Я пойду, если вы не возражаете, скоро начнутся занятия."
    else:
        her "Я должна идти. Уже довольно поздно..."

    hide screen bld1
    hide screen hermione_main
    with d3

    if whoring >= 13:

        call her_walk("desk","door",3)

        call her_head("(Что насчет моих очков?)","disgust","down_raised",cheeks="blush")
        if whoring >= 20:
            call her_head("(Ай, да кого это волнует...)","base","ahegao_raised",cheeks="blush")
        else:
            call her_head("(Спрошу об этом в другой раз...)","annoyed","angryL")

        pause.5
        call her_chibi("leave","door","base")

    else:
        call her_walk("desk","leave",3)

    $ hg_pf_BreastMolester_OBJ.points += 1

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
