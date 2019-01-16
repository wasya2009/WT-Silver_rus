label luna_reversion_event:
    m "{size=-4}(Я просто попрошу по-быстрому...){/size}"
    if luna_corruption <= 10: #FIRST TIME
        if luna_corruption <= 9:
            $ luna_corruption += 1
        call play_music("chipper_doodle") 
        if luna_sub > luna_dom: #Sub intro
            m "[luna_name]..."
            call luna_main("Да, [l_genie_name]...", 6, 3, 4, 2) 
            m "Ты знаешь, что такое мастурбировать?"
            call luna_main("Что?", 1, 1, 3, 3) 
            m "Ты тихонечко гладишь ее руку--"
            call luna_main("Я знаю, что это такое!", 4, 1, 2, 4) 
            m "Фантастика!"
            call luna_main("...", 7, 2, 2, 3) 

        else: #Dom intro
            m "[luna_name]?"
            call luna_main("Да, [l_genie_name]...", 1, 2, 2, 2) 
            m "Ты случайно не знаешь, что такое мастурбировать?"
            call luna_main("...", 7, 1, 2, 2) 
            m "..."
            m "Ну, если это не слишком сложно..."
            call luna_main("...", 7, 2, 2, 2) 
            call luna_main("Продолжайте...", 7, 2, 2, 2) 
        menu:
            "-Сказать ей, чтобы она мне подрочила-" if luna_sub >= 7:
                $ current_payout = 80
                if luna_sub <= 8:
                    $ luna_sub += 1
                $ luna_choice = 1
                m "Хорошо вижу, что ты знакома с концепцией, как насчет практической демонстрации."
                call luna_main("...", 6, 2, 2, 3) 
                call luna_main("Правда? Вы ожидаете, что я {size=+5}коснусь{/size} вашего грязного члена?", 4, 1, 5, 3) 
                call luna_main("Это очень плохо, что я должна стоять здесь, пока вы касаетесь себя...", 8, 1, 2, 2) 
                call luna_main("Вот здесь я рисую ограничительную линию, [l_genie_name]!", 9, 1, 3, 3) 
                m "Хммм...{p}, ну хорошо, я не собираюсь заставлять тебя."
                call luna_main("Спасибо...", 6, 2, 4, 3) 
                m "На сегодня все, [luna_name], ты можешь идти."
                call luna_main("Хорошо, [l_genie_name]...", 6, 1, 4, 2) 
                call luna_main("(Хорошая работа, наконец, мне удалось противостоять ему!)", 2, 2, 4, 1) 
                ">Полумна поворачивается, чтобы покинуть твой кабинет."
                m "О, и напоследок еще кое-что..."
                call luna_main("...", 7, 1, 4, 2) 
                m "Не могла бы ты отправить ко мне одну \'Слизеринскую\' девочку?"
                call luna_main("Что? Зачем?", 4, 1, 2, 4) 
                m "Ну, видя, как ты не в состоянии дать мне немного внимания, я полагаю, что одна из тех \'Слизеринских\' шлюх будет готова."
                m "Они, вероятно, даже сделают это за половину цены..." 
                call luna_main("...", 7, 1, 2, 3) 
                call luna_main("......", 6, 3, 4, 2) 
                $ luna_tears = 1 
                call luna_main(".........", 5, 1, 4, 3) 
                call luna_main("{size=-5}Отлично{/size}...", 5, 3, 4, 2) 
                m "Что, [luna_name]?"
                call luna_main("{size=+5}Отлично!{/size} Я буду дрочить ваш отвратительный, грязный, морщинистый старый член!", 4, 1, 4, 6) 
                m "Фантастика! Позволь мне просто встать."
                call luna_main("Вы отвратительны...", 8, 1, 2, 3) 

            "-Попросить мастурбировать-" if luna_sub > luna_dom:
                $ current_payout = 120
                if luna_sub <= 8:
                    $ luna_sub += 1
                $ luna_choice = 2
                m "Хорошо, вижу, ты знакома с концепцией ..."
                call luna_main("...", 7, 1, 3, 3) 
                call luna_main("В самом деле? Вы ожидаете, что я буду {size=+5}трогать{/size} этот грязный член?", 4, 1, 5, 3) 
                call luna_main("Это достаточно плохо, что я должна стоять здесь, пока вы касаетесь себя ...", 8, 8, 4, 2) 
                m "Будет хорошая награда..."
                call luna_main("...", 6, 3, 4, 3) 
                call luna_main("......", 6, 2, 4, 1) 
                call luna_main("Я ожидаю, что также и журнал моего отца продастся еще в несколько копий...", 7, 1, 4, 2) 
                m "Конечно..."
                call luna_main("Отлично...", 6, 3, 4, 3) 
                m "Фантастика! Позволь мне просто встать."
                call luna_main("*Хмммф* Не ждите, что будете кончать где-нибудь рядом со мной!", 8, 1, 3, 3) 
            "-Попросить мастурбировать, вежливо-" if luna_sub < luna_dom:
                $ current_payout = 160
                if luna_dom <= 8:
                    $ luna_dom += 1
                $ luna_choice = 3
                m "Ну, видя, как ты так искусна во всем, к чему прикасаешься руками..."
                call luna_main("Мхммм...", 6, 2, 2, 3) 
                m "Я надеялся, что ты коснешься рукой и моего члена."
                call luna_main("...", 8, 2, 1, 2) 
                m "Пожалуйста..."
                call luna_main("Правда? Хотите, чтобы я погладила ваш грязный стручок?", 8, 1, 2, 3) 
                call luna_main("Разве недостаточно того, что я позволяю вам трогать себя?..", 9, 2, 3, 3) 
                m "Будет огромное вознаграждение..."
                call luna_main("...", 8, 2, 3, 3) 
                call luna_main("......", 8, 1, 2, 2) 
                call luna_main("Хорошо, что вы так вежливо попросили...", 8, 1, 1, 1) 
                m "..."
                call luna_main("Давайте сюда...", 7, 1, 3, 1) 
                m "Фантастика! Позволь мне просто встать."
                call luna_main("(Это,вроде так просто)", 8, 2, 2, 1) 
            "-Умолять мастурбировать-" if luna_dom >= 7:
                $ current_payout = 200
                if luna_dom <= 8:
                    $ luna_dom += 1
                $ luna_choice = 4
                m "Ну, если это не слишком сложно..."
                call luna_main("Мхммм...", 6, 2, 2, 3) 
                m "Я надеялся, что ты сможешь..."
                call luna_main("...", 8, 2, 1, 2) 
                m "Дай мне разок..."
                call luna_main("Правда? Хотите, чтобы я погладила ваш грязный стручок?", 8, 1, 2, 3) 
                m "Если это не слишком большая проблема..."
                call luna_main("Ну, я полагаю, что я, вероятно, могу.", 5, 2, 1, 1) 
                call luna_main("Кто знает, кому вы позвоните, если я этого не сделаю...", 8, 1, 3, 1) 
                m "Спасибо..."
                call luna_main("...", 8, 2, 3, 3) 
                call luna_main("......", 8, 1, 2, 2) 
                call luna_main("Однако, я ожидаю справедливой компенсации...", 8, 1, 1, 1) 
                m "Конечно."
                call luna_main("Хорошо. А теперь подойдите сюда...", 7, 1, 3, 1) 
                m "Фантастика! Позволь мне просто встать."
                call luna_main("(Это, вроде так, просто...)", 8, 2, 2, 1) 
                call luna_main("(Я буду единственным человеком в его завещании к концу месяца с такой скоростью...)", 9, 1, 3, 1) 

        if luna_choice <= 2: #Sub choices
            jump luna_revert_1
        else:
            jump luna_revert_2


label luna_revert_1: #Reversion event
    hide screen bld1
    hide screen genie
    show screen chair_left
    show screen desk
    $ genie_chibi_xpos = -20
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "jerking_off_02_ani"
    show screen g_c_u
    with fade
    hide screen blktone
    hide screen blkfade
    with d5
    pause
    ">Ты встаешь и обходишь свой стол, встав перед Полумной."
    ">Ты открываешь плащ и вытаскиваешь свой член."
    m "Ну..."
    $ luna_tears = 0
    call luna_main("...", 5, 3, 1, 2) 
    ">Полумна нерешительно смотрит на твой член."
    call luna_main("......", 3, 3, 4, 2) 
    ">Она медленно берет его правой рукой."
    $ luna_r_arm = 3
    $ genie_sprite_xpos = 300
    $ luna_xpos = 390
    call gen_main("!!!", 4, 4) 

    call luna_main("Он такой большой...", 5, 3, 4, 1) 
    call luna_main("(Я даже не могу обхватить его рукой.)", 5, 2, 4, 1) 
    m "Почему бы тебе не попробовать схватить его обеими руками, [luna_name]..."
    call luna_main("Хорошо...", 6, 3, 4, 1) 
    ">Полумна медленно обхватывает обеими руками твой член."
    m "Мммм, вот так. А теперь начни двигать руками вперед и назад."
    call luna_main("......", 5, 3, 1, 2) 
    ">Полумна начинает двигать руками взад и вперед вдоль твоего члена."
    m "Да, вот так..."
    call luna_main("...", 6, 3, 4, 1) 
    m "Мммм, да... неплохо, [luna_name], ты практиковалась?"
    call luna_main("Что? Конечно, нет!", 4, 1, 2, 2) 
    m "Ну, я ожидаю, что ты начнешь практиковаться с этого момента!"
    call luna_main("На чем?", 7, 1, 5, 2) 
    m "На моем члене, разумеется!"
    call luna_main("[l_genie_name]!", 8, 1, 2, 6) 
    m "Я пошутил, [luna_name]."
    call luna_main("Ох...", 7, 2, 4, 14) 
    m "Но я надеюсь, что ты улучшишь свои навыки..."
    call luna_main("Разве вам, не хорошо?...", 8, 1, 5, 4) 
    m "Все в порядке..."
    call luna_main("Хорошо, что мне нужно сделать по-другому?", 6, 2, 4, 2) 
    menu:
        "\"Сними рубашку.\"":
            $ luna_choice = 1
            call luna_main("Моя рубашка? Правда?", 8, 1, 2, 14) 
            m "Это сделает все намного быстрее."
            call luna_main("...", 6, 3, 4, 3) 
            call luna_main("Прекрасно...", 8, 1, 4, 2) 
            call luna_main("Но я рассчитываю на дополнительную оплату!", 3, 3, 2, 3) 
            $ current_payout += 20
            m "Договорились."
            call luna_main("...", 6, 3, 4, 3) 
            ">Полумна медленно снимает верхнюю часть, ложа ее на пол."
            $ luna_wear_top = False
            call luna_main("Так...", 5, 1, 4, 2) 
            call luna_main("Этого достаточно, [l_genie_name]?", 7, 2, 2, 3) 
            m "Почти... руки на член, [luna_name]..."
            call luna_main("...", 5, 3, 4, 1) 
            ">Полумна медленно обхватывает руками твой член и начинает дрочить."
        "\"Быстрее\"":
            $ luna_choice = 2
            call luna_main("Вот так?", 7, 8, 4, 1) 
            ">Полумна начинает двигать руками вверх и вниз по члену немного быстрее."
            m "Мммм..."
            call luna_main("Это достаточно быстро [l_genie_name]?", 5, 2, 4, 1) 
            m "Почти..."
            call luna_main("...", 6, 3, 4, 3) 
            ">Она ускоряет темп."
            call gen_main("Ах!", 2) 
            call luna_main("Что?", 4, 1, 1, 2) 
            m "Ну, когда ты делаешь так быстро, у меня начинает немного болеть..."
            call luna_main("Правда? Мне тогда притормозить... ?", 6, 3, 4, 3) 
            m "В этом нет необходимости [luna_name], немного слюны должно решить проблему."
            call luna_main("...", 8, 1, 2, 2) 
            call luna_main("Хотите, чтобы я плюнула на ваш член?", 9, 2, 4, 3) 
            m "Только чуть-чуть."
            call luna_main("...", 8, 1, 4, 3) 
            call luna_main("......", 7, 2, 4, 3) 
            call luna_main("*Ptew*", 6, 3, 4, 16) 
            ">Полумна плюет на руку, прежде чем положить ее обратно на член."
    call gen_main("Мммм... да вот так, [luna_name]...", 4) 
    call luna_main("...", 5, 1, 1, 1) 
    g9 "Просто двигай рукой вверх и вниз."
    call luna_main("......", 5, 2, 4, 1) 
    if luna_choice == 1:
        g9 "Почему бы тебе не встряхнуть свои наливные сиськи?"
        call luna_main("[l_genie_name]...", 5, 2, 1, 1) 
        call luna_main("(Небольшая встряска не повредит...)", 3, 3, 1, 1) 
        ">Полумна нежно начинает трясти грудью, в то время пока рукой дрочит твой член."
    else:
        g9 "Мммм, да... как насчет еще немного плюнуть, [luna_name]?"
        g9 "Просто, чтобы убедиться, что все хорошо и смазать..."
        call luna_main("...", 5, 2, 1, 1) 
        call luna_main("Хорошо...", 5, 3, 1, 1) 
        call luna_main("*Ptew*", 6, 3, 4, 16) 
        ">Полумна снова плюет на руку и кладет ее обратно на член."
    ">Она начинает дрочить твой член еще быстрее."
    g9 "Боги да..."
    g9 "(Вот и момент, куда мне кончить?)"
    menu:
        "-На ее лицо-":
            ">Ты помещаешь руку на макушку головы Полумны и медленно давишь на нее, чтобы она опустилась на один уровень с твоим членом"
            ">Ее тонкие руки не перестают скользить вверх и вниз по всей длине члена."
            call luna_main("[l_genie_name]!!!", 4, 1, 4, 6) 
            g9  "Тсс, [luna_name], я просто показываю его ближе."
            call luna_main("...", 8, 3, 4, 2) 
            $ luna_tears = 2
            call luna_main("{size=-5}Пожалуйста, сэр...{/size}", 5, 2, 4, 3) 
            g9  "Что [luna_name]?"
            call luna_main("Пожалуйста, не надо...", 6, 3, 4, 3) 
            g9  "Мммм..."
            call luna_main("Кончать на мое-", 5, 3, 4, 3) 
            hide screen luna
            with d3
            $ luna_wear_cum = True
            $ luna_cum = 7
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white 
            pause .1
            hide screen white
            with hpunch
            call luna_main("!!!!!!", 4, 1, 4, 8) 
            g9  "Ох! Боги {size=+10}ДА!{/size}"
            g9  "{size=+10}ВОЗЬМИ ВСЕ!{/size}"

        "-На ее блузку-":
            ">Ты помещаешь руку на плечо Полумны."
            ">Ее тонкие руки не перестают скользить вверх и вниз по всей длине члена."
            call luna_main("[l_genie_name]...", 4, 1, 4, 6) 
            g9  "Тсс, [luna_name], продолжай гладить."
            call luna_main("...", 8, 3, 4, 2) 
            $ luna_tears = 2
            call luna_main("{size=-5}Пожалуйста, сэр...{/size}", 5, 2, 4, 3) 
            g9  "Что, [luna_name]?"
            call luna_main("Пожалуйста, не надо...", 6, 3, 4, 3) 
            g9  "Мммм"
            call luna_main("Кончать мне на-", 5, 3, 4, 3) 
            hide screen luna
            with d3
            $ luna_wear_cum = True
            $ luna_cum = 3
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white 
            pause .1
            hide screen white
            with hpunch
            call luna_main("!!!!!!", 4, 1, 4, 8) 
            g9  "Ох! Боги {size=+10}ДА!{/size}"
            g9  "{size=+10}ЛОВИ ВСЕ, ШЛЮХА!{/size}"
    g9  "Мммм....."
    m "Это пришлось по вкусу..."
    call luna_main("[l_genie_name]!", 8, 1, 2, 9) 
    call luna_main("Как вы могли!", 7, 1, 3, 6) 
    m "Ах... это было фантастически, шлюха..."
    $ g_c_u_pic = "images/animation/06_groping_01.png"
    call luna_main("[l_genie_name]!!!", 8, 1, 3, 15) 
    call play_sound("door") #Sound of a door opening.
    $ hermione_SC.chibi.xpos = 600 #Near the desk.
    show screen hermione_blink #Hermione stands still.
    pause
    hide screen luna
    with d3
    $ luna_flip = -1
    $ luna_r_arm = 2
    hide screen genie_sprite
    with d3
    call her_main("[genie_name], надеюсь, вы не против, что я пришла без предупреждения...","angry","wink") 
    $ changeLuna(4, 1, 4, 3, 400)
    call her_main("Но мне действительно нужно хорошее-.","angry","down_raised") 
    call her_main("...","shock","wide") 
    call luna_main("...", 4, 2, 4, 3) 
    m "..."
    pause
    call her_main("{size=+5}ЧТО{/size}","annoyed","annoyed") 
    $ changeLuna(4, 3, 4, 3)
    call her_main("{size=+10}ЗА{/size}","angry","angry") 
    $ changeLuna(4, 2, 4, 3)
    call her_main("{size=+15}ЧЕРТ!{/size}","scream","angry",emote="01") 
    call luna_main("Это совсем не то, что ты подумала-", 5, 2, 4, 6) 
    show screen white 
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    call her_main("{size=+15}petrificus totalus!{/size}","scream","angry",emote="01") 
    ">Гермиона с удивительной скоростью вытаскивает палочку и парализует Полумну."
    call luna_main("!!!", 4, 1, 4, 6) 
    m "(Вау...)"
    call her_main("Честно говоря, сэр, о чем вы думаете!","annoyed","annoyed") 
    call her_main("Если вам так нужно потеребонькать ваш грязный старый член, вы должны просто позвать меня!","annoyed","angryL") 
    call luna_main("???", 4, 2, 4, 3) 
    call her_main("Но делать это, с Полумной Лавгуд...","annoyed","annoyed") 
    call her_main("Она даже не {size=+5}\"Гриффиндорка\"!{/size}","angry","angry") 
    m "Я не платил-"
    call her_main("Заткнитесь!","scream","angry",emote="01") 
    call her_main("Как вы вообще договорились с Полумной, сэр?","annoyed","annoyed") 
    call her_main("Я даже не думаю, что она знает, в каком факультете она учится.","angry","angry") 
    call her_main("Я не могу представить, что ее чувство гордости за факультет достаточно велико, чтобы оправдать это...","annoyed","annoyed") 
    $ changeLuna(4, 3, 4, 2)
    m "Я могу это объяснить..."
    call her_main("Правда? {p}Продолжайте...","angry","angry") 
    m "Ну, я сидел здесь один в своем кабинете."
    m "(Что еще я могу делать...)"
    m "Когда вдруг эта странная шляпа на полке позади меня заговорила!"
    call her_main("...","annoyed","suspicious") 
    call her_main("Вы это серьезно, сэр?","annoyed","angry") 
    m "Я знал, что ты не поверишь-"
    call her_main("Конечно, я вам верю! Это же сортировочная шляпа!","angry","angry") 
    m "(Я все время забываю, что это место волшебное...)"
    m "Да, хорошо... эта \"сортировочная\" шляпа отметила, что она, возможно, сделала ошибку с сортировкой некоторых студентов."
    hat "..."
    m "Поэтому она предложила использовать \"Legitimancy\" и что-то исправить-"
    call her_main("Вы выполнили Legilimency?","angry","wide") 
    call her_main("На {size=+5}студентах{/size}?!","scream","angry",emote="01") 
    m "Это не так уж плохо, конечно..."
    call her_main("Сэр, это достаточно плохо, чтобы использовать Legilimency для чтения чьих-то мыслей...","annoyed","annoyed") 
    call her_main("Но использовать ее, чтобы изменить мнение...","annoyed","annoyed") 
    call her_main("Я даже не думаю, что это возможно...","angry","angry") 
    m "Значит, все в порядке?"
    call her_main("Это довольно чертовски далеко от \"в порядке\"...","scream","angry",emote="01") 
    call her_main("Вы должны изменить ее обратно!","annoyed","annoyed") 
    m "Правда? Но это было довольно забавно."
    call her_main("Я даже не могу поверить, что должна говорить вам, как это неправильно, сэр!","angry","angry") 
    call her_main("Верните ее обратно сейчас же или я все сообщу в Министерство.","scream","angryCl") 
    m "Как насчет твоего факультета-"
    call her_main("{size=+10}СЕЙЧАС ЖЕ!{/size}","scream","angry",emote="01") 
    m "Хорошо, хорошо. Блин...."
    m "{size=-5}(Эти сучки просто сумасшедшие!){/size}"
    m "Давай я только возьму шляпу."
    ">Ты протягиваешь руку и вытаскиваешь старую кожистую шляпу из пыльного шкафа."
    hat "Ухх... Нежнее Виктор, еще нежнее."
    call her_main("Положите шляпу ей на голову.","annoyed","annoyed") 
    hat "Хорошо, если это не мисс Грейнджер..."
    call her_main("...","annoyed","angryL") 
    ">Ты аккуратно одел сортировочную шляпу на голову Полумны."
    m "Так."
    call her_main("Хорошо, измените ее обратно!","annoyed","annoyed") 
    hat "Ты уверена? Она оказалась гораздо более забавной..."
    call her_main("Сделайте {size=+5}это {size=+5}НЕМЕДЛЕННО!{/size}","angry","angry") 
    hat "Хорошо, хорошо. Блин."
    hat "Ты не такая властная, когда обычно бываешь здесь..."
    call luna_main("!!!", 4, 1, 4, 3) 
    call her_main("{size=+5}Заткнись!{/size}","scream","angryCl") 
    hat "Так... Одна скучная старая Лавгуд, сейчас снова будет."
    call luna_main("???", 4, 2, 4, 3) 
    call luna_main("......", 4, 3, 4, 2) 
    call luna_main(".....", 4, 1, 4, 2) 
    call luna_main("....", 4, 6, 4, 3) 
    call luna_main("...", 4, 6, 4, 2) 
    $ luna_reverted = True
    call luna_main("...", 4, 6, 4, 2) 
    hat "Вот, она вернулась к нормальной жизни... {size=-8}печально{/size}"
    call her_main("Вы уверены?","annoyed","annoyed") 
    hat "Да, я в этом абсолютно уверена. Могу я теперь вернуться на полку?"
    call her_main("Отлично...","annoyed","annoyed") 
    call her_main("Но если вы захотите попробовать что-то подобное снова...","annoyed","angryL") 
    call her_main("...","annoyed","annoyed") 
    ">Ты поместил шляпу на верхней части шкафа."
    m "Так теперь лучше? Теперь мы можем забыть обо всем этом?"
    call her_main("Вы же это не серьезно, не так ли?","annoyed","annoyed") 
    m "Что? Мисс Лавгуд вернулась к нормальной жизни..."
    call her_main("Вам это не сойдет с рук, сэр.","annoyed","annoyed") 
    m "Я не совсем понимаю, о чем ты говоришь?"
    call her_main("О чем я вообще говорю?","angry","angry") 
    call her_main("Полумна Лавгуд в {size=+10}ГЛАЗУРИ{/size} из вашей спермы!","angry","angry",emote="01") 
    m "Оу..."
    call her_main("А что более важно, сколько очков вы ей заплатили?","annoyed","annoyed") 
    menu:
        "\"Нисколько\"":
            call her_main("Что?","disgust","glance") 
            call her_main("Я должна поверить, что она пришла к вам в кабинет...","annoyed","annoyed") 
            call her_main("И вы дрочили свой отвратительный старый член перед ней...","angry","angry") 
            call her_main("Бесплатно?","annoyed","annoyed") 
            ">Ты поднимаешь руку в воздух."
            m "Честно Пионерское!"
            call her_main("...","disgust","glance") 
            m "Кроме того, наверняка ты заметила бы скачок очков \"Когтеврана\"?"
            call her_main("Я полагаю, что вы правы...","annoyed","angryL") 
            call her_main("Если Сортировочная шляпа манипулировала ею, то это не исключено.","annoyed","angryL") 
            call her_main("{size=-5}(Но для нее сделать это так охотно...){/size}","annoyed","angryL") 
        "\"Я платил ей золотом.\"":
            call her_main("Золотом?","disgust","glance") 
            m "Да золотом, галлеонами."
            call her_main("Значит, не очками?","annoyed","annoyed") 
            m "Ни одного не дал."
            call her_main("Полагаю, тогда все в порядке...","annoyed","angryL") 
            call her_main("{size=-5}(Почему мне никогда не платят золотом...){/size}","annoyed","annoyed") 
            call her_main("{size=-5}(Нет, Гермиона! Если бы я сделал это, ты бы была проституткой...){/size}","normal","worriedCl") 
            call her_main("{size=-5}{image=textheart}{image=textheart}{image=textheart}{/size}","grin","ahegao") 

    call her_main("Несмотря ни на что, она должна быть наказана.","annoyed","annoyed") 
    m "Подожди, она наказана?"
    call her_main("Ну конечно!","annoyed","angryL") 
    call her_main("Вижу, что, раз вы не дали \"Когтеврану\" никаких очков вы не сделали ничего плохого.","annoyed","suspicious") 
    call her_main("Но она...","annoyed","frown") 
    ">Гермиона уставилась на все еще замерзшую Полумну Лавгуд."
    call her_main("...","annoyed","frown") 
    call her_main("Она нуждается в наказании.","smile","angry") 
    m "О чем ты только думаешь?"
    call her_main("Хммм...","annoyed","angryL") 
    call her_main("Сортировочная шляпа!","annoyed","annoyed") 
    hat "Ч-ч-что? Я пытаюсь заснуть..."
    call her_main("Когда Полумна придет в норму?","soft","angry") 
    hat "Я не совсем в этом уверена... Наверное, минут через двадцать."
    hat "До тех пор она будет в довольно ясном и внушаемом состоянии."
    call her_main("Хорошо...","smile","angry") 
    show screen white 
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    call her_main("liquescimus corporis!","scream","angryCl") 
    ">Еще одна вспышка света, когда Полумна становится не окаменевшей."
    call luna_main("Тьфу... где я?", 6, 2, 4, 2) 
    call her_main("Тссс, все в порядке.","base","glance") 
    call luna_main("Гермиона? Что происходит?", 6, 1, 4, 2) 
    call her_main("Ничего... Профессор Дамблдор и я, просто нуждались в твоей помощи.","base","down") 
    call luna_main("В чем?", 7, 1, 4, 3) 
    call luna_main("А что это у-", 8, 2, 4, 2) 
    call her_main("Тихо, сейчас это не имеет значения.","soft","squintL") 
    call her_main("Возвращайся в свою комнату отдыха...","open","baseL") 
    m "Это правда-"
    ">Гермиона уставилась на тебя."
    call her_main("...","annoyed","annoyed") 
    call luna_main("Хорошо, я вернусь в свою комнату отдыха...", 6, 1, 4, 3) 
    call her_main("Вот именно...","soft","squintL") 
    ">Полумна тихо выходит из комнаты."
    hide screen luna_chibi
    hide screen luna 
    with d3
    call play_sound("door") #Sound of a door opening.
    call her_main("Что ж, теперь все кончено...","annoyed","angryL") 
    call her_main("Думаю, мне тоже пора уходить...","annoyed","angry") 
    m "Не хочешь остаться еще ненадолго?"
    call her_main("Мне так не кажется, сэр...","disgust","glance") 

    ">Гермиона поворачивается, чтобы уйти."
    $ hermione_busy = True
    if daytime:
        $ hermione_takes_classes = True
    else:
        $ hermione_sleeping = True
    hide screen hermione_main
    with d3
    show screen genie
    hide screen chair_left
    hide screen desk
    $ genie_chibi_xpos = -20
    $ genie_chibi_ypos = 10
    hide screen g_c_u
    call luna_reset 
    jump end_hg_pf

    #result of this event:
        #Ability to redo all luna's favours with the real luna


label luna_revert_2: #Non-Reversion event
    show screen blkfade
    ">Ты встаешь и обходишь свой стол, встав перед Полумной."
    ">Ты открываешь плащ и вытаскиваешь свой член."
    hide screen bld1
    hide screen genie
    show screen chair_left
    show screen desk
    $ genie_chibi_xpos = -20
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "jerking_off_02_ani"
    show screen g_c_u
    with fade
    hide screen blktone
    hide screen blkfade
    with d5
    pause
    m "Ну..."
    call luna_main("...", 7, 8, 2, 3) 
    ">Полумна смотрит на твой член."
    call luna_main("Отвратительный...", 9, 8, 3, 1) 
    ">Она крепко держит его правой рукой"
    $ luna_r_arm = 3
    $ genie_sprite_xpos = 300
    $ luna_xpos = 390
    call gen_main("!!!", 4, 4) 
    call luna_main("*Хммф* По крайней мере, он не маленький...", 5, 8, 2, 1) 
    call luna_main("(Я даже не могу обхватить его рукой.)", 5, 3, 3, 1) 
    ">Полумна, грубыми и неопытными движениями, медленно надрачивает рукой твой член."
    m "Почему бы тебе не попробовать схватить его обоими руками [luna_name]..."
    call luna_main("Хмф... Вы хотите?!", 8, 1, 2, 1) 
    m "..."
    ">Полумна начинает двигать руками вперед и назад, по всей длине твоего члена."
    m "Да, вот так..."
    call luna_main("(Мужчины действительно самые худшие)", 6, 3, 3, 3) 
    m "Мммм, да... Вот так [luna_name]..."
    call luna_main("Вам хорошо [l_genie_name]?", 6, 1, 4, 14) 
    m "Да, да, это удивительно..."
    call luna_main("Хорошо...", 6, 1, 4, 1) 
    call luna_main("Но...", 6, 2, 4, 2) 
    call luna_main("Вам нужно больше стимула?", 8, 1, 4, 1) 
    m "А как ты думаешь?"
    call luna_main("... ...", 9, 8, 3, 1) 
    menu:
        "-Полумна, оголяй верх-":
            ">Полумна медленно снимает жилет и начинает расстегивать топ."
            m "Мммм"
            $ luna_wear_top = False
            $ luna_choice = 1
            ">Она снимает рубашку и кладет ее на пол."
            call luna_main("Вот...", 8, 2, 4, 1) 
            m "Симпатично, [luna_name]!"
            call luna_main("...", 7, 8, 4, 2) 
            call luna_main("Спасибо, сэр...", 7, 1, 4, 1) 
            ">Она кладет обратно руки на твой член."
            call luna_main("Ммм, намного лучше...", 5, 8, 2, 1) 
            m "Боги, о да."
            call luna_main("...", 5, 1, 2, 1) 
            call luna_main("Я бы сняла и лифчик...", 5, 2, 4, 2) 
            call luna_main("Но я не думаю, что вы сможете остановиться и не кончить, не так ли?", 8, 1, 3, 1) 
            g4 "Скорее всего нет!"
            call luna_main("...", 9, 8, 2, 1) 
            ">Полумна начинает дрочить твой член еще быстрее."
        "-Полумна дразнит тебя-":
            $ luna_choice = 2
            call luna_main("Давайте, профессор...", 8, 2, 4, 1) 
            ">Полумна начинает двигать руками вверх и вниз по члену немного быстрее."
            m "Мммм..."
            call luna_main("Приготовьте для меня побольше спермы...", 7, 8, 4, 2) 
            m "О да..."
            call luna_main("Будьте готовы кончить на все места своего студента.", 7, 1, 4, 1) 
            ">Она ускоряет темп."
            call gen_main("Ах...", 2) 
            call luna_main("Что случилось?", 7, 1, 5, 2) 
            m "Ну, если дрочить так быстро, будет немного болеть."
            call luna_main("Правда?...", 8, 1, 2, 1) 
            ">Полумна не замедляется. Даже немного ускоряет темп."
            g4 "Ах!"
            call luna_main("...", 9, 1, 3, 1) 
            g4 "[luna_name]..."
            call luna_main("Тогда вы хотите, чтобы я поплевала на ваш член?", 5, 1, 5, 1) 
            g4 "Только чуть-чуть..."
            call luna_main("...", 5, 1, 2, 1) 
            call luna_main("......", 5, 1, 3, 1) 
            g4 "Пожалуйста..."
            call luna_main("Хороший мальчик.", 7, 1, 2, 1) 
            call luna_main("*Ptew*", 5, 8, 2, 16) 
            ">Полумна плюет на руку, прежде чем положить ее обратно на член."
    call gen_main("Мммм, да, вот так [luna_name]...", 4) 
    call luna_main("...", 7, 8, 2, 1) 
    g9  "Просто продолжай двигать рукой вверх и вниз."
    call luna_main("......", 8, 1, 3, 1) 
    if luna_choice == 1:
        ">Полумна нежно начинает трясти сиськами, в то время пока тебе дрочит."
    else:
        call luna_main("*Ptew*", 8, 8, 3, 16) 
        ">Полумна снова плюет на руку и кладет ее обратно на член."
    ">После она начинает дрочить твой член еще быстрее."
    g9  "Боги, о да..."
    g9  "(Вот-вот кончу, только куда?)"
    menu:
        "-На ее лицо-":
            ">Ты кладешь ладонь на макушку головы Полумны и медленно пытаешься заставить ее присесть на уровень с твоим членом."

        "-На ее сиськи-":
            ">Ты кладешь ладонь на голову Полумне и медленно пытаешься заставить ее присесть на уровень с твоим членом."

    call luna_main("[l_genie_name]!!!", 7, 1, 3, 6) 
    call luna_main("Вы же не пытаетесь кончить на меня, правда?", 8, 1, 3, 3) 
    g9  "Ах, [luna_name], я уже почти."
    call luna_main("Ну...", 9, 8, 3, 3) 
    $ luna_wear_skirt = False
    ">Полумна быстро стягивает юбку."
    g9  "!!!"
    call luna_main("Вы кончаете...", 8, 1, 3, 3) 
    g9  "Ах..."
    ">Полумна медленно стягивает трусики в сторону, выставляя свою киску напоказ."
    ">Ее правая рука все еще обхватывает твой член, и дрочит его с ослепительной скоростью."
    call luna_main("Ну же...", 9, 1, 3, 3) 
    g9  "Мммм"
    call luna_main("Теперь...", 8, 1, 3, 2) 
    call luna_main("Кончайте!", 5, 1, 2, 1) 
    $ g_c_c_u_pic = "jerking_off_cum_ani"
    show screen g_c_c_u
    $ luna_wear_cum_under = True
    $ luna_cum = 10
    show screen white 
    pause.1
    hide screen white
    pause.2
    show screen white 
    pause .1
    hide screen white
    with hpunch
    ">Ты начинаешь кончать прямо в трусики Полумны, покрывая ее киску спермой."
    g9  "Ох! Боги, о {size=+10}ДА!{/size}"
    call luna_main("...", 5, 3, 1, 1) 
    call luna_main("(Она такая теплая...)", 5, 2, 4, 1) 
    g9  "{size=+10}ПОЛУЧАЙ ЕЕ ВСЮ, ШЛЮХА!{/size}"
    g9  "Мммм....."
    hide screen g_c_c_u
    $ g_c_u_pic = "images/animation/06_jerking_01.png"
    m "Тебе понравилось? Ух..."
    call luna_main("({image=textheart}{image=textheart}{image=textheart})", 5, 8, 4, 1) 
    call luna_main("[l_genie_name]!", 8, 1, 3, 1) 
    call luna_main("Как вы могли! Кончить на {size=-10}киску{/size} своего студента...", 7, 8, 2, 1) 
    m "Ах... это было просто фантастично, шлюха..."
    $ g_c_u_pic = "images/animation/06_groping_01.png"
    call luna_main("[l_genie_name]...", 6, 2, 2, 1) 
    call play_sound("door") #Sound of a door opening.
    $ hermione_SC.chibi.xpos = 600 #Near the desk.
    show screen hermione_blink #Hermione stands still.
    hide screen luna 
    with d3
    $ luna_flip = -1
    $ luna_r_arm = 2
    hide screen genie_sprite
    with d3
    call her_main("[genie_name], надеюсь, вы не против, что я вошла без стука...","angry","wink", xpos=600) 
    call her_main("Но мне действительно нужно хорошее-.","angry","down_raised") 
    $ changeLuna(4, 1, 4, 3, 400)
    call luna_main("...", 7, 1, 3, 3) 
    call her_main("...","scream","wide_stare") 
    m "..."
    pause
    call her_main("{size=+5}ЧТО{/size}","annoyed","annoyed") 
    $ changeLuna(8, 1, 3, 3)
    call her_main("{size=+10}ЗА{/size}","angry","angry") 
    $ changeLuna(9, 1, 3, 3)
    call her_main("{size=+15}ЧЕРТ!{/size}","scream","angry",emote="01") 
    call her_main("Что тут происходит-","angry","angry") 
    call luna_main("{size=+15}petrificus totalus!{/size}", 8, 1, 3, 15) 
    show screen white 
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    ">Полумна с удивительной скоростью вытаскивает палочку и парализует Гермиону."
    call her_main("!!!","soft","shocked") 
    m "(Вау...)"
    hide screen luna
    with d3
    $ luna_flip = 1
    $ changeLuna(9, 1, 3, 7, 400)
    ">Полумна поворачивается к вам лицом, оставляя Гермиону парализованной посреди комнаты."
    call luna_main("{size=+15}Что все это значит?{/size}", 7, 1, 3, 7) 
    m "Я не знаю, мисс Грейнджер, должно быть, пришла сюда, чтобы попросить что-нибудь."
    call luna_main("Дверь была заперта!", 9, 1, 2, 6) 
    call luna_main("И все знают, что ваша дверь зачарована против всех возможных заклинаний!", 8, 1, 3, 4) 
    m "(Так и есть?)"
    call luna_main("Значит, у нее должен был быть ключ...", 5, 3, 3, 4) 
    m "..."
    call luna_main("Почему у нее есть ключ, [l_genie_name]?", 9, 1, 3, 3) 
    m "Эм... чтобы..."
    menu:
        "\"Продавать услуги\"":
            pass

        "\"Я не знаю\"":
            call luna_main("...", 9, 1, 3, 4) 
            call luna_main("Действительно? Вы не знаете...", 8, 1, 3, 6) 
            m "Без понятия..."
            call luna_main("Ну тогда, мы просто должны спросить Гермиону...", 7, 2, 3, 4) 
            call her_main("...","open","wide") 
            call luna_main("Я уверена, что несколько капель Veritaserum прояснят ситуацию...", 7, 1, 3, 6) 
            call her_main("!!!","angry","wide") 
            m "(Это плохо?)"
            ">Гермиона смотрит на тебя умоляющими глазами."
            call her_main("...","angry","worriedCl", tears="crying") 
            m "(Наверное...)"
            m "Чтобы..."
            call luna_main("Давай, старина...", 9, 1, 3, 2) 
            m "Она здесь, чтобы продать услугу..."



    call luna_main("{size=+5}ЧТО{/size}", 4, 1, 3, 7) 
    call luna_main("Подумать только, я пришла сюда и позволила вам смотреть на свое тело...", 9, 1, 3, 6) 
    call luna_main("Пока вы гладили свой грязный член...", 8, 8, 3, 6) 
    call luna_main("и все это время вы выбрасывали свои галлеоны какой-то \"Гриффин-{size=+5}ШЛЮХЕ{/size}\"!", 7, 1, 3, 3) 
    call luna_main("Хорошо, сколько вы ей заплатили?", 9, 1, 2, 2) 
    hide screen luna
    with d3
    $ luna_flip = -1
    call luna_main("Сколько вы потратили на эту жирную шлюху?", 8, 1, 3, 3) 

    $ point_estimate = (gryffindor-200)
    m "Все в порядке? Вероятно, [point_estimate] очков..."
    hide screen luna
    with d3
    $ luna_flip = 1
    call luna_main("[point_estimate]... {p}очков?", 7, 1, 5, 2) 
    m "Ну знаешь, для \"Графиньдур\"..."
    call luna_main("...", 5, 1, 5, 2) 
    call luna_main("Хахахаха!", 2, 1, 1, 11) 
    call her_main("...","annoyed","angryL") 
    m "..."
    hide screen luna
    with d3
    $ luna_flip = -1
    ">Полумна оборачивается к Гермионе."
    call luna_main("Правда? Ты продаешь свое тело за очки факультету?", 5, 2, 1, 5) 
    call her_main("...","annoyed","annoyed") 
    call luna_main("Ну да, наверное, мне стоит это отменить.", 7, 1, 2, 4) 
    show screen white 
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    call luna_main("liquescimus corporis!", 5, 1, 2, 15) 
    ">Еще одна вспышка света, и с Гермионы, заклинание обездвиживания отменяется."
    $ changeLuna(5, 2, 1, 1, 400)
    call her_main("Профессор! Что все это значит?","scream","angryCl") 
    call her_main("И что вы двое делали до того, как я пришла сюда?","angry","angry") 
    call luna_main("О... Я просто помогала профессору Дамблдору...", 5, 3, 1, 2) 
    call her_main("Как помогала?","annoyed","annoyed") 
    call luna_main("Просто немного снимала... напряжение. {p}Не волнуйся, он не заплатил мне очками... *tssk*", 7, 2, 1, 1) 
    call her_main("Что?","angry","angry",emote="01") 
    call her_main("[genie_name]! Что вы здесь делали?","scream","angryCl") 
    m "Ах...."
    call luna_main("Не вини его. Это не его вина, что ты его не удовлетворяешь...", 8, 1, 2, 1) 
    call her_main("Ты... ты...","annoyed","annoyed") 
    call her_main("{size=+10}Тупая шлюха!{/size}","angry","angry") 
    call her_main("{size=+15}Ты всего лишь проститут-{/size}","angry","angry",emote="01") 
    call luna_main("{size=+15}petrificus totalus!{/size}", 9, 1, 3, 15) 
    show screen white 
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    ">Полумна парализует Гермиону во второй раз."
    $ changeLuna(9, 1, 3, 2, 400)
    call her_main("!!!","angry","wide") 
    call her_main("...","angry","angry") 
    ">Гермиона в слепой ярости смотрит на Полумну."
    m "Ты действительно должна это делать?"
    hide screen luna
    with d3
    $ luna_flip = 1
    call luna_main("*Hmmmph*", 5, 2, 2, 3) 
    ">Полумна хохочет, игнорируя вопрос."
    call luna_main("Честно, [l_genie_name], я не знаю, что вы в ней нашли...", 7, 1, 2, 2) 
    pause
    call luna_main("Итак, как мы должны наказать ее?", 5, 2, 1, 5) 
    call her_main("!!!","angry","wide") 
    m "Наказать ее?"
    call luna_main("Ну конечно! За то, что она сказала.", 5, 1, 2, 11) 
    call her_main("...","clench","down_raised") 
    call luna_main("Вы же не позволите ей уйти безнаказанной?", 7, 1, 3, 3) 
    menu:
        "-Сказать ей, чтоб отпустила Гермиону.-" if False:
            m "Разморозить мисс Грейнджер."
            call luna_main("Что? Вы принимаете ее сторону?", 5, 3, 1, 1) 
            m "(Тьфу... Сучки...)"
            m "Я не беру ничью сторону. Я накажу мисс Грейнджер соответственно позже."
            call luna_main("...", 5, 3, 1, 1) 
            call luna_main("Без разницы...", 5, 3, 1, 1) 
            show screen white 
            pause .1
            hide screen white
            $ renpy.play('sounds/magic4.ogg')   #Not loud.
            call luna_main("liquescimus corporis!", 5, 3, 1, 1) 
            call her_main("...","angry","wink") 
            m "На сегодня все, мисс Лавгуд."
            call luna_main("...", 5, 3, 1, 1) 
            call luna_main("Вам лучше наказать ее...", 5, 3, 1, 1) 
            jump luna_away
            call her_main("...","angry","wink") 

        "-Пусть Полумна решит-":
            pass
    m "Я оставлю решение о наказании на тебе."
    call luna_main("Да, вы, вероятно, правы.", 5, 3, 1, 1) 
    hide screen luna
    with d3
    $ luna_flip = -1
    ">Полумна поворачивается к Гермионе."
    call luna_main("Хммм, что же мне сделать...", 8, 1, 3, 1) 
    call luna_main("...", 5, 1, 2, 1) 
    call her_main("...","open","wide") 
    call luna_main("Я поняла!", 4, 1, 2, 5) 
    hide screen hermione_main 
    with d3
    ">Полумна кладет руки на плечи Гермионы и мягко заставляет ее парализованное тело встать на колени."
    $ hermione_SC.chibi.xpos = 40 #40 = Near Luna
    $ hermione_SC.chibi.ypos = 60
    $ h_c_u_pic = "characters/hermione/chibis/dance/08_sits.png"
    call luna_main("Это вероятно правильно...", 5, 8, 2, 1) 
    call luna_main("Подождите...", 5, 8, 1, 2) 
    if luna_wear_top:
        $ luna_wear_top = False
        ">Полумна быстро снимает верх."
    ">Полумна кладет руку на подбородок Гермионы и мягко поворачивает голову вверх."
    call luna_main("Отлично...", 5, 8, 1, 5) 
    call her_kneel("...","annoyed","worriedL") 
    call luna_main("Теперь, прежде чем ты так грубо решила прервать нас, профессор Дамблдор сделал неприятный беспорядок...", 5, 3, 1, 1) 
    call her_kneel("...","angry","worried") 
    call luna_main("Я собиралась вернуться в свою комнату и привести себя в порядок перед уроком, но, учитывая, что твое вмешательство заняло так много времени, тебе придется сделать это.", 5, 2, 2, 1) 
    call her_kneel("...","normal","worriedCl") 
    hide screen luna 
    with d3
    $ luna_wear_panties = False 
    show screen luna
    with d3
    ">Полумна медленно стягивает трусики, показывая свою пропитанную спермой киску."
    call her_kneel("!!!","disgust","narrow") 
    call luna_main("Ну... {p}приступай к работе!", 8, 8, 1, 5) 
    ">Гермиона свирепо смотрит на Полумну."
    call her_kneel("...","annoyed","annoyed") 
    call luna_main("*Вздох* Тогда, наверное, мне придется все делать!", 7, 8, 2, 1) 
    show screen blkfade
    hide screen hermione_kneel
    $ luna_l_arm = 3
    $ luna_xpos=635
    $ hermione_head_ypos=390
    $ hermione_kneel_leg = True
    ">Полумна подходит к Гермионе и подносит свою киску к ее носу."
    hide screen blkfade
    call her_kneel("!!!","angry","worriedCl") 
    m "!!!"
    call luna_main("Мммм, вот и все...", 5, 3, 1, 1) 
    call luna_main("Кто хорошая девочка... ?", 5, 8, 1, 5) 
    call her_kneel("!!!","normal","worriedCl") 
    call luna_main("Мммм ... Хорошо пахнет, не так ли, шлюха?", 5, 3, 1, 1) 
    call luna_main("Мммм... Ты выглядишь так, как будто хочешь еще...", 5, 3, 2, 5) 
    $ luna_xpos = 550
    $ luna_l_arm = 1
    $ hermione_kneel_leg = False
    ">Полумна делает шаг назад от лица Гермионы."
    call luna_main("Такое красивое личико...", 5, 8, 4, 1) 
    ">Полумна помещает большой палец в парализованный рот Гермионы, медленно открывая его."
    call her_kneel("...","open_tongue","angryL") 
    ">Она хватает ее за язык и медленно вытаскивает его, пока он не начинает свисать изо рта."
    call her_kneel("Уууаааа йййааааяяя!!!","open_wide_tongue","angryCl") 
    m "(...)"
    call luna_main("Тсс... ...", 5, 3, 4, 2) 
    $ luna_xpos=635
    $ luna_l_arm = 3
    $ hermione_kneel_leg = True
    ">Полумна подошла к ней, подставив киску со спермой в ротик Гермионы."
    call her_kneel("!!!","open_wide_tongue","angry") 
    call luna_main("Тссс.... Мммм, не плохо...", 5, 8, 1, 5) 
    call her_kneel("...","open_wide_tongue","base") 
    call her_kneel("...","open_wide_tongue","squintL") 
    call her_kneel("......","open_wide_tongue","down_raised") 
    call her_kneel(".........","open_wide_tongue","ahegao_mad",cheeks="blush") 
    call luna_main("Хорошая девочка...", 5, 8, 2, 5) 
    call luna_main("Просто наслаждайся...", 5, 8, 2, 1) 
    call luna_main("Мы оба знаем, кто настоящая шлюха, не так ли?...", 7, 8, 3, 3) 
    call her_kneel("...","open_wide_tongue","ahegao_mad",cheeks="blush") 
    call luna_main("Не так ли?", 9, 8, 3, 5) 
    call her_kneel("ууааааа...","open_wide_tongue","ahegao") 
    ">Гермиона едва ли может говорить."
    g9  "(Это уже слишком!)"
    menu:
        "-Присоединиться-" if False: #Have sex with hermione while luna grinds on her face. Needs chibi work
            show screen blkfade
            ">Ты подходишь к Гермионе и поднимаешь ее."
            call luna_main("Эй! Я не закончила с ней!", 5, 3, 1, 1) 
            m "Не волнуйся, я просто перенесу ее. Ты все еще сможешь повеселиться."
            ">Ты несешь парализованную Гермиону на свой стол, и нежно кладешь на него."
            hide screen blkfade
            call luna_main("...", 5, 3, 1, 1) 
            m "Хммм... Интересно, если..."
            ">Ты начинаешь сгибать конечности Гермионы, обнаруживая, что они легко двигаются, но фиксируются на месте."
            m "Да, она просто как кукла Барби!"
            call her_kneel("хрохехо!","angry","wink") 
            ">Ты наклоняешь ее над столом, лицом к Полумне."
            m "Надеюсь, ты все еще в состоянии исполнить свое наказание, [luna_name]?"
            call luna_main("Мммм, я думаю да...", 5, 3, 1, 1) 
            ">Полумна подходит к Гермионе и прижимает ее язык к своему клитору."
            call luna_main("Ах... {image=textheart}", 5, 3, 1, 1) 
            call her_kneel("...","angry","wink") 
            ">Ты медленно поднимаешь юбку Гермионы."
            call her_kneel("!!!","angry","wink") 
            ">Освобождая от всего ее мокрую киску."
            m "Мммм..."
            m "Давай, Барби..."
            ">Ты воткнул свой вставший член во влагалище Гермионы!"
            g9  "Начнем вечеринку!"
            call her_kneel("{image=textheart}{image=textheart}{image=textheart}","angry","wink") 
            g9  "Да! Боги!"
            call luna_main("Мммм {image=textheart}", 5, 3, 1, 1) 
            ">Ты начинаешь трахать Гермиону жестче."
            call luna_main("Так [l_genie_name]...", 5, 3, 1, 1) 
            call luna_main("Как долго это будет продолжатся?", 5, 3, 1, 1) 
            m "С мисс Грейнджер? Некоторое время..."
            call luna_main("Цифры...", 5, 3, 1, 1) 
            call luna_main("Ты всегда была любимчиком учителя, не так ли..?", 5, 3, 1, 1) 
            call her_kneel("{image=textheart}{image=textheart}{image=textheart}","angry","wink") 
            call luna_main("Бьюсь об заклад, ты пришла сюда одна...", 5, 3, 1, 1) 
            call luna_main("Хочешь продавать свое тело за несколько паршивых очков...", 5, 3, 1, 1) 
            g9  "Да..."
            call her_kneel("...","angry","wink") 
            call luna_main("Чтобы твой факультет мог выиграть Кубок в этом году...", 5, 3, 1, 1) 
            call luna_main("Ты знаешь, что никого не волнует эта домашняя чашка, не так ли?", 5, 3, 1, 1) 
            ">Ты начинаешь засовывать еще глубже в капающую киску Гермионы."
            call her_kneel("Ааааа эээйййй ооооо!!!","angry","wink") 
            call luna_main("Посмотрим...", 5, 3, 1, 1) 
            call luna_main("Профессор...", 5, 3, 1, 1) 
            m "А... Да?"
            call luna_main("Кто выиграл Кубок, когда вы учились в школе...", 5, 3, 1, 1) 
            m "(Черт! Я понятия не имею, кто выиграл паршивый Кубок, когда Думбодур был ребенком.)"
            m "Хм... Ах..."
            ">Гермиона сжимает твой член."
            m "Кажется, так и есть... Ах... Вылетело из головы."
            call luna_main("Видишь...", 5, 3, 1, 1) 
            call luna_main("Даже Дамблдор не помнит, кто получал кубок, когда он был студентом...", 5, 3, 1, 1) 
            call her_kneel("...","angry","wink") 
            #hermione tears
            call luna_main("Это означает, что все твои старания прошли зря...", 5, 3, 1, 1) 
            call luna_main("Все это время ты продавала свое тело...", 5, 3, 1, 1) 
            call luna_main("Все это время ты унижала себя...", 5, 3, 1, 1) 
            call luna_main("Даже сейчас лежа здесь, и вылизывая мне, пока твой драгоценный Дамблдор трахает тебя...", 5, 3, 1, 1) 
            g9  "Да..."
            call her_kneel("...","angry","wink") 
            g9  "Ох!"
            call luna_main("Ты сделала все это, только потому, что ты этого хотела...", 5, 3, 1, 1) 
            call her_kneel("...","angry","wink") 
            g9  "{size=+5}Да!!!!{/size}"
            call luna_main("Ты...", 5, 3, 1, 1) 
            call luna_main("Мерзкая...", 5, 3, 1, 1) 
            call luna_main("Шлюха...", 5, 3, 1, 1) 
            with hpunch
            g9  "{size=+7}Аааа, ДЕРЖИ!!!{/size}"
            call cum_block 
            g9  "{size=+15}АРГХ!!!!!!!!!!!!!!!!{/size}"
            $ g_c_u_pic = "sex_cum_in_ani"
            call cum_block 
            show screen ctc
            pause
            hide screen ctc
            $ uni_sperm = True
            $ u_sperm = "characters/hermione/face/auto_08.png"
            hide screen bld1
            with d3
            show screen ctc
            pause
            hide screen ctc
            show screen bld1
            with d3
            $ g_c_u_pic = "images/animation/23_cum_19.png"


        "-Начать дрочить-": #Jerk off and cum on hermione
            show screen blkfade
            hide screen hermione_kneel
            ">Ты подходишь к Гермионе, стоящей на коленях, и вытаскиваешь свой твердый член из-под мантии."
            lun "Мммм, пришло время, когда вы начали дисциплинировать своих учеников должным образом."
            $ genie_sprite_xpos = 450
            hide screen blkfade
            show screen hermione_kneel
            call gen_main("Может быть, ты права.", 4, 3) 
            $ genie_chibi_xpos = 50
            $ genie_cum_chibi_xpos = 50
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "jerking_off_02_ani"
            ">Ты начинаешь дрочить свой член, направляя его прямо на лицо Гермионы"
            call luna_main("Я всегда оказываюсь права...", 8, 2, 1, 5) 
            hide screen genie_sprite 
            with d3
            call her_kneel("...","open_wide_tongue","down_raised") 
            m "Да... вот так шлюха."
            call luna_main("Мммм, я вижу, что вам в ней нравится...", 5, 8, 1, 1) 
            ">Полумна с трудом закрывает рот Гермионе."
            call her_kneel("...","open_wide_tongue","ahegao") 
            call luna_main("Она гораздо более сексуальная с полным ртом...", 8, 8, 1, 5) 
            g9  "Кому ты рассказываешь!"
            call luna_main("Итак, как долго это продолжается [l_genie_name]?", 8, 2, 2, 1) 
            m "Уже давно..."
            call luna_main("Меня это не удивляет...", 5, 8, 1, 3) 
            call luna_main("Я всегда полагала, что Гермиона подавляемая шлюха...", 5, 8, 2, 1) 
            call luna_main("Бьюсь об заклад, она даже приходила к вам, не так ли?", 5, 2, 2, 1) 
            call her_kneel("...","open_wide_tongue","ahegao_mad",cheeks="blush") 
            m "Ах... Да, так."
            call luna_main("Так и знала...", 7, 8, 2, 3) 
            call luna_main("Она показывает, что глава \"ДПМ\" - шлюха...", 8, 8, 3, 1) 
            call her_kneel("...","open_wide_tongue","ahegao") 
            call luna_main("Отчаянно хочет продать свое тело...", 9, 8, 2, 5) 
            call luna_main("Все ради нескольких очков...", 5, 8, 1, 1) 
            m "Да... Продолжай..."
            call luna_main("Оо, вам нравится, когда я унижаю ее [l_genie_name]?", 7, 2, 4, 1) 
            g9  "Боги, да!"
            call luna_main("Хорошо...", 5, 2, 2, 1) 
            call luna_main("Потому что я ожидаю, что вы покроете эту шлюшку результатом своего \"наслаждения\"...", 7, 8, 2, 5) 
            g9  "Не стоит беспокоиться!"
            g9  "Я скоро буду готов!"
            call luna_main("Слышала, Гермиона?", 8, 8, 3, 5) 
            call her_kneel("...","open_wide_tongue","down_raised") 
            call luna_main("Для тебя у директора заготовлено большое количество спермы...", 9, 8, 2, 1) 
            call luna_main("Если тебе повезет, он может даже дать \"Гриффиндору\" несколько очков...", 5, 3, 1, 11) 
            g9  "Да..."
            call her_kneel("...","open_wide_tongue","angryCl") 
            call luna_main("Ой, ты выглядишь такой расстроеной...", 5, 3, 4, 2) 
            call luna_main("Не расстраивайся... Для этого ты и была рождена...", 5, 8, 4, 5) 
            call her_kneel("...","open_wide_tongue","ahegao") 
            ">Ты начинаешь дрочить еще решительнее!"
            call luna_main("Ты должна гордится, что примешь сперму от своего учителя...", 7, 3, 4, 1) 
            call luna_main("Кстати говоря... Вы готовы, [l_genie_name]?", 5, 2, 2, 1) 
            g9  "Ох! Клянусь девятью богами, да!"
            call luna_main("Тогда кончайте!", 9, 2, 2, 5) 
            $ g_c_c_u_pic = "jerking_off_cum_ani"
            show screen g_c_c_u
            g9  "{size=+7}Аааа, ПОЛУЧАЙ!!!{/size}"
            call luna_main("Покройте эту шлюху глазурью!", 8, 3, 2, 1) 
            g9  "{size=+15}АРГХ!!!!!!!!!!!!!!!!{/size}"
            $ uni_sperm = True
            $ u_sperm = "characters/hermione/face/auto_15.png"
            $ luna_xpos = 550
            $ luna_l_arm = 1
            $ hermione_kneel_leg = False
            call her_kneel("!!!","grin","ahegao") 

            ">Полумна делает шаг назад, когда ты извергаешься над окаменевшим выражением Гермионы."
            g9  "Возьми все, сучка!"
            g9  "{size=+15}АРГХ!!!!!!!!!!!!!!!!{/size}"
            call her_kneel("!!!","silly","dead") 
            ">Ты чувствуешь, что кончаешь больше чем когда-либо прежде кончал в своей жизни"
            g9  "Держи все!"
            hide screen g_c_c_u
            $ g_c_u_pic = "images/animation/06_jerking_01.png"
            $ u_sperm = "characters/hermione/face/auto_16.png"
            pause 
            call her_kneel("...","open_wide_tongue","ahegao") 
            ">Гермиона стоит перед тобой на коленях, не в силах пошевелиться на ее лице слой спермы настолько толстый, что подобного ты еще никогда не видел."
            ">Ты едва можешь разглядеть ее черты через слой белого крема."

    m "Боги да... Это было потрясающе..."
    hide screen luna
    with d3
    $ luna_flip = 1
    $ luna_xpos = 400
    $ hermione_kneel_leg = False
    call luna_main("Я рада, что вам понравилось, [l_genie_name]...", 5, 2, 1, 1) 
    $ luna_wear_skirt = True 
    $ luna_wear_panties = True 
    $ luna_wear_cum_under = False 
    $ luna_wear_top = True
    show screen genie
    hide screen chair_left
    hide screen desk
    $ genie_chibi_xpos = -20
    $ genie_chibi_ypos = 10
    hide screen g_c_u
    $ luna_chibi("stand")
    ">Полумна быстро надевает трусики и одежду."
    call her_kneel("...","silly","dead") 
    call luna_main("На сколько вы бы оценили, то, что вам понравилось?", 7, 1, 2, 1) 
    m "На много..."
    call luna_main("А если бы вам пришлось поставить оценку вашему удовольствию?", 8, 1, 2, 3) 
    m "О... Я бы сказал, примерно 250?"
    call luna_main("Фантастика!", 2, 1, 1, 1) 
    m "..."
    m "Вот твоя оплата, [luna_name]."
    $ gold -= 250
    $ luna_gold += 250
    call luna_main("Спасибо, [l_genie_name].", 5, 2, 1, 1) 
    call luna_main("Что ж, тогда мне лучше уйти. Я опаздываю на занятия.", 5, 2, 2, 2) 
    m "Ты не собираешься сначала привести в порядок Гермиону?"
    call her_kneel("...","silly","ahegao") 
    call luna_main("Правда? Вы слишком ленивы, чтобы произнести несколько простых заклинаний?", 7, 1, 2, 2) 
    m "Ах... Я немного устал после всего этого..."
    m "Думаю, будет лучше, если ты это сделаешь."
    call luna_main("Отлично... Полагаю, вы хотите, чтобы я стерла и ее воспоминания?", 5, 2, 1, 2) 
    m "Стереть ее воспоминания?"
    call her_kneel("???","angry","worriedCl") 
    call luna_main("Конечно. Я имею в виду, то, что мы с ней сделали, было немного сомнительно...", 7, 1, 2, 2) 
    call luna_main("Стереть часть памяти, было бы уместным.", 8, 2, 1, 1) 
    call her_kneel("!!!","annoyed","annoyed") 
    m "(Думаю, я недооценил магию этой школы...)"
    m "Ну конечно... Почему нет..."
    hide screen luna
    with d3
    $ luna_flip = -1
    call luna_main("Я думаю, что уберу ее, а также...", 6, 8, 2, 2) 
    show screen white 
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    call luna_main("scourgify!", 7, 1, 2, 15) 
    $ uni_sperm = False
    ">Вся сперма исчезает из тела Гермионы."
    call her_kneel("...","annoyed","base") 
    m "Вау..."
    show screen white 
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    call luna_main("obliviate!", 8, 1, 2, 15) 
    ">Еще одна вспышка света, которое приводит ее в порядок."
    call her_kneel("...","soft","dead") 
    m "..."
    show screen white 
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    call luna_main("liquescimus corporis!", 7, 1, 3, 15) 
    ">Гермиона падает на пол безвольным манекеном."
    call her_kneel("Ах...","shock","dead") 
    hide screen hermione_kneel
    with d3
    m "(Все кончено?)"
    show screen white 
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    call luna_main("vestimenta lacus!", 9, 1, 2, 15) 
    ">Вся одежда Гермионы извивается, как черви на ее теле."
    hide screen luna
    with d3
    $ luna_flip = 1
    call luna_main("Там...", 7, 2, 2, 2) 
    call luna_main("Это все, [l_genie_name]?", 6, 1, 2, 1) 
    m "На сегодня достаточно, [luna_name]."
    ">Полумна поворачивается, чтобы покинуть твой кабинет с Гермионой."
    call luna_main("Увидимся в следующий раз...", 9, 1, 3, 1) 

    hide screen luna_chibi
    hide screen luna
    with d3

    ">Ты поворачиваешься к Гермионе."
    m "[hermione_name]? Ты в порядке?"
    call her_main("Ах... что случилось?","open","down") 
    call her_main("Полумна Лавгуд была здесь?","upset","wink") 
    m "Кто?"
    call her_main("Неважно...","normal","worriedCl") 
    call her_main("Думаю, мне пора уходить, [genie_name]...","angry","worriedCl",emote="05") 
    m "Хорошо, хорошего тебе дня."
    call her_main("Тьфу...","disgust","down_raised") 
    call her_main("(Могу поклясться, Полумна была здесь...)","annoyed","worriedL") 
    call her_main("(Подождите, что я здесь делаю...)","annoyed","suspicious") 
    call luna_reset 
    jump end_hg_pf
    #result of this event:
        #Ability to get Luna to summon hermione for threesome (Planned future event)



label luna_reverted_greeting_1: #reverted Luna explains the wrackspurt problem
    $ luna_corruption += 1
    $ luna_wear_glasses = True
    $ luna_wear_acc = True
    $ luna_l_arm = 1
    $ luna_r_arm = 2
    $ luna_hair = 2
    $ l_genie_name = "Сэр" #reset genie's name with Luna
    $ luna_name = "Мисс Лавгуд" #reset luna's name with genie
    "*Тук* *Тук* *Тук*"
    lun "Здравствуйте."
    m "(Вероятно Полумна...)"
    menu:
        "-Впустить ее.-":
            m "Войди!"
            call play_sound("door") #Sound of a door opening.
            $ luna_chibi("stand")
            ">Полумна стоит перед твоим столом."
            call luna_main("Здравствуйте, профессор...", 1, 1, 4, 1) 
            m "Мисс Лавгуд."
            pass


        "-Сказать ей, чтобы уходила.-":
            m "(Она, наверное, здесь из-за этой штуки со шляпой!)"
            m "Тьфу... меня здесь нет!"
            lun "..." 
            ">Твоя дверь открывается, входит Полумна."
            call play_sound("door") #Sound of a door opening.
            $ luna_chibi("stand")
            ">Полумна стоит перед твоим столом."
            call luna_main("Здравствуйте, профессор...", 1, 1, 4, 1) 
            m "Хм... Здравствуй, мисс Лавгуд."

    $ luna_l_arm = 1
    $ luna_r_arm = 1
    call luna_main("...", 1, 2, 4, 1) 
    call luna_main("......", 1, 3, 4, 2) 
    ">Полумна начинает осматривать твой кабинет."
    call luna_main("Здесь такая странная аура...", 6, 2, 2, 2) 
    call luna_main("Она как большое полое дерево...", 1, 2, 4, 2) 
    m "..."
    m "(Что?)"
    m "Могу я тебе чем-нибудь помочь?"
    call luna_main("Ох... Было кое-что, ради чего я пришла сюда...", 1, 3, 4, 3) 
    m "(Что здесь вообще происходит? Я думал, шляпа стерла ее разум!)"
    call luna_main("Я помню! Проклятие Wrackspurt!", 2, 2, 4, 1) 
    menu: 
        "\"Wrackspurt?... Это что, какой-то волшебник?\"":
            call luna_main("Хахаха, я думаю, только вы могли, это так сказать, профессор! ", 1, 2, 4, 1) 
            call luna_main("Wrackspurts, а по русски мозгошмыги - невидимые существа, которые влезают в ухо человека и делают мозг неясным.", 1, 1, 4, 2) 
            $ luna_l_arm = 2
            call luna_main("Вы можете увидеть их только в этих спектроскопах!", 1, 4, 1, 1) 
            $ luna_l_arm = 1
            m "Понятно... (Эта сучка действительно сумасшедшая!)"
            m "(Вероятно, шляпа перестаралась с ней...)"
            m "Так, мисс Лавгуд, что мы можем с этим поделать?"
            call luna_main("Я не уверена, профессор... Обычно достаточно мыслить позитивно, чтобы избавиться от них, но у меня с этим проблемы. Мой отец, Xenophilius-", 7, 2, 4, 2) 
            "*Ты прыгаешь со стола*"
            g4 "ТЫ ТОЛЬКО ЧТО КОЛДОВАЛА НА МЕНЯ?!"
            $ luna_l_arm = 2
            $ luna_r_arm = 2
            call luna_main("Профессор?", 4, 1, 4, 3) 
            g4 "ОБЪЯСНИСЬ!"
            $ luna_l_arm = 1
            $ luna_r_arm = 1
            call luna_main("Извините, профессор, я не уверена, что-", 4, 2, 4, 2) 
            g4 "XENOFIUS! Что оно делает?"
            call luna_main("Xenofius? Я не слышала об этом заклинании раньше, профессор.", 7, 1, 4, 2) 
            m "Заклинание... Ты же только, что..... А, ладно, проехали."
            call luna_main("(Секретное заклинание?) Профессор, ваша магия является самой сильной в Хогвартсе, а эти мозгошмыги теперь добрались и до меня.", 8, 2, 4, 3) 
            m "Я вижу... Продолжай дальше."
        "\"Боюсь, я не смогу помочь тебе, мисс Лавгуд.\"":
            call luna_main("Пожалуйста, профессор! Вы единственный, кто достаточно силен, чтобы помочь.", 4, 1, 4, 15) 
            "*Ты можешь видеть, что Полумна качает бедрами, в такт дыханию*"
            m "Мисс Лавгуд, боюсь, я не знаю, что такое мозгошмыги, не говоря уже о том, как их лечить."
            call luna_main("Но, профессор; мозгошмыги подробно описаны на странице 6, Придиры! Вот здесь!", 1, 1, 4, 2) 
            "*Полумна подает тебе Придиру*"
            m "*Чтение* “Rotfang заговор... 300 способов связать призрака... “ Ага! Мозгошмыги..."
            "\"Невидимые существа, которые вползают в уши человека, делая его/ее мозг туманным\""
            "*Полумна указывает на свои спектроскопы* "
            call luna_main("Я вижу их, профессор.", 2, 1, 1, 1) 
            m "Понятно... (Неудивительно, что Гермиона назвала ее чокнутой Лавгуд)."
        "\"Что, черт возьми, на тебе надето?\"":
            call luna_main("О! Это мои спектроскопы, профессор!", 1, 5, 4, 1) 
            m "(Пожалуйста, не читай мои мысли, пожалуйста, не читай мои мысли-)"
            call luna_main("Они помогают мне видеть мозгошмыгов.", 1, 1, 4, 2) 
            m "(Спасибо, великим пескам пустыни!)"
            call luna_main("А это мои серьги из сливы.", 1, 4, 4, 1) 
            m "Ах да, очень мило..."
            m "Так, что об этих, мозгошмыгах..."

    call luna_main("Да, профессор, они оказываются довольно болезненными.", 3, 1, 4, 2) 

    "*Полумна заметно виляет бедрами.*"
    m "(В самом деле?... Оооо). Мисс Лавгуд, как именно этих мозгошмыгов ты в себе чувствуешь?"
    call luna_main("Они такие, как описано в Придире, сэр, за одним исключением...", 5, 2, 4, 2) 
    m "Продолжай..."
    call luna_main("Ну, это, не мозг, они делают неясносным.", 5, 3, 4, 14) 
    m "Где точно неясность, мисс Лавгуд?"
    call luna_main("Умм... Я не уверена, могу ли я вам говорить...", 5, 2, 4, 2) 
    m "(ДА!)"
    m "А теперь, мисс Лавгуд, раз я твой директор, ты должна рассказать мне все, без утайки..."
    call luna_main("Ну ладно...", 5, 3, 4, 1) 
    call luna_main("Неясность у меня между ног, сэр...", 5, 1, 4, 1) 
    m "Правда? Это кажется довольно странно..."
    call luna_main("Это сэр! Я только слышала, что у людей мозги расплывались...", 1, 1, 4, 2) 
    call luna_main("Но это...", 7, 1, 4, 2) 
    call luna_main("Это как невыносимый зуд, который я не могу почесать...", 5, 3, 4, 3) 
    m "(Мне знакомо это чувство.)"
    call luna_main("И я чувствую, что не могу вспомнить, чем я занималась в последние несколько дней...", 6, 2, 4, 2) 
    m "О... Я бы не беспокоился об этом, вообще..."
    m "Давай сосредоточимся на твоей неясности."
    call luna_main("Хорошо, профессор...", 5, 3, 4, 2) 
    call luna_main("Как я уже говорила, эта неясность действительно беспокоит меня последние несколько дней...", 5, 1, 4, 2) 
    m "Хм, это как-то повлияло на твою учебу?"
    call luna_main("Да, сэр...", 5, 3, 4, 3) 
    m "Ну, мы не сможем проверить этого сейчас, не так ли?"
    call luna_main("Нет, сэр...", 5, 1, 4, 1) 
    m "Ты свободна в данный момент?"
    call luna_main("Эмм... Я собираюсь пойти на занятия по гаданию, сэр...", 5, 3, 4, 2) 
    m "В таком случае, мы будем решать, что делать с этим неприятным зудом позже."
    m "Приходи ко мне в кабинет сегодня вечером, и посмотрим, что мы сможем с ним сделать."
    call luna_main("О, спасибо, сэр!", 4, 1, 4, 1) 
    call luna_main("Я не могу ждать!", 5, 1, 4, 1) 
    call luna_main("Как вы думаете, вы могли бы остановить нарглов, которые воруют мою обувь, а?", 1, 3, 4, 1) 
    m "(Что, черт возьми, за нарглы, такие?)"
    m "Всему свое время, мисс Лавгуд."
    call luna_main("Да, вы правы... Нарглы не хотелось бы, распылятся на все сразу...", 3, 1, 4, 2) 
    m "..."
    call luna_main("Что ж, мне лучше уйти... До свидания, профессор!", 2, 1, 1, 1) 
    "*Полумна выпрыгивает из комнаты, скача, сжимая ноги вместе.*"
    m "(Это будет очень весело!)"
    $ luna_wear_glasses = True
    jump luna_away


label luna_reverted_greeting_2: #Explaining to Luna what will happen or something
    $ luna_corruption += 1
    "*тук* *тук* *тук*"
    m "Войди..."
    call play_sound("door") #Sound of a door opening.
    $ luna_chibi("stand")
    ">Полумна стоит перед твоим столом."
    call luna_main("Здравствуйте, профессор...", 2, 1, 1, 1) 
    m "Мисс Лавгуд. Итак, шарамыги оставили тебя в покое?"
    call luna_main("Вовсе нет! Сегодня было хуже, чем когда-либо!", 1, 2, 2, 3) 
    m "Правда?"
    call luna_main("Правда, сэр. И я не думаю, что они влияют только на меня.", 1, 1, 4, 2) 
    call luna_main("Боюсь, вся школа ими переполнена!", 4, 1, 4, 2) 
    m "Почему ты так думаешь?"
    call luna_main("Как люди ведут себя...", 7, 2, 4, 2) 
    call luna_main("Это очень странно, вам не кажется, сэр?", 7, 1, 4, 3) 
    m "(Как эта сумасшедшая сучка, может называть кого-то другого, странным!)"
    m "Как странно?"
    call luna_main("Их ауры, сэр!", 3, 2, 4, 2) 
    m "Ааа..."
    call luna_main("Они слишком сильно покраснели!", 7, 1, 4, 2) 
    m "Покраснели?"
    call luna_main("Боюсь, что да...", 7, 2, 4, 3) 
    m "И ты думаешь, что эти шарамыжники виноваты?"
    call luna_main("Я не уверена...", 5, 3, 4, 2) 
    call luna_main("Согласно каталогу существ моего отца, они должны только чуть-чуть давать серый оттенок ауре...", 5, 2, 4, 2) 
    call luna_main("Но у них, красные ауры...", 4, 3, 4, 3) 
    call luna_main("Это может быть, очень опасно!", 4, 1, 4, 2) 
    m "(Пфф... ауры...)"
    m "Да, я понимаю, как это может быть опасно..."
    "*Полумна начинает двигать бедрами.*"
    call luna_main("Да...", 5, 3, 4, 1) 
    call luna_main("Итак, насчет этого зуда, сэр...", 5, 1, 4, 1) 
    m "Да."
    call luna_main("Вы сказали, что у вас есть способ избавиться от него?", 5, 1, 4, 2) 
    m "Да."
    call luna_main("Хорошо...", 5, 2, 4, 3) 
    m "Ну, во-первых, мне нужно кое-что от тебя, мисс Лавгуд."
    call luna_main("Что-то от меня?", 4, 1, 4, 4) 
    m "Да, мне нужно обещание."
    call luna_main("О...", 1, 2, 4, 2) 
    call luna_main("Ладно!", 2, 1, 4, 1) 
    m "Я даже не сказал тебе, что за обещание."
    call luna_main("Не волнуйтесь, сэр, я вам доверяю!", 4, 1, 1, 1) 
    m "(Не думал, что это будет так легко!)"
    m "Да, методы, которые я собираюсь показать тебе, являются собственными, поэтому мне важно, чтобы ты пообещала не разговаривать ни с кем о том, что происходит в этом кабинете."
    call luna_main("Методы...", 5, 2, 4, 2) 
    call luna_main("Собственные...", 5, 3, 4, 3) 
    call luna_main("Я не уверена, что понимаю вас, сэр.", 5, 1, 4, 2) 
    m "Но, если то, что ты говоришь - верно, тогда если я использую мощную магию, чтобы справится с ними..."
    m "(Надеюсь, она купится на этот бред...)"
    m "Они могут в скором времени вернутся, и в гораздо большем количестве."
    call luna_main("...", 5, 2, 4, 2) 
    m "(Она на это купилась?)"
    call luna_main("Да, вы совершенно правы, сэр.", 3, 2, 4, 2) 
    m "(ДА!)"
    call luna_main("Но есть ли действенные методы, чтобы справится с ними?", 5, 1, 5, 2) 
    m "Есть, но, как я уже сказал, Если ты хочешь их изучить, ты должна пообещать никому не рассказывать, что здесь происходит."
    call luna_main("Полагаю, это справедливо, эта информация будет стоить даже больше, чем информация морщерогом кизляке!", 1, 1, 4, 1) 
    m "..."
    m "Дело не только в технике, мисс Лавгуд."
    m "Ты должна пообещать, что не расскажешь никому, что происходит в этом кабинете, несмотря ни на что."
    call luna_main("Что ж...", 5, 2, 4, 2) 
    "*Ты замечаешь, как Полумна неловко раскачивает тазом*"
    call luna_main("Тогда ладно...", 5, 1, 4, 1) 
    call luna_main("Я торжественно клянусь, что никому не расскажу, что происходит в этих священных стенах...", 3, 2, 1, 2) 
    m "Фантастика!"
    call luna_main("Не могли бы вы научить меня это секретной магической технике, сэр?", 4, 1, 4, 1) 
    ">Есть отчаянная потребность в глазах Полумны, которая возбуждает тебя."
    m "Да, да. Думаю, я заставил тебя ждать достаточно долго."
    call luna_main("Огромное спасибо!", 2, 2, 1, 1) 
    m "Не нужно благодарить меня, мисс Лавгуд, я просто делаю то, что должен делать любой хороший учитель."
    m "Теперь встань в середине комнаты."
    hide screen luna 
    with d3
    $ luna_xpos = 400
    call luna_main("Вот здесь?", 1, 1, 4, 4) 
    m "Идеально."
    m "Прежде чем мы начнем, я должен объяснить несколько вещей."
    ">Полумна пристально смотрит на тебя."
    call luna_main("...", 7, 1, 4, 2) 
    m "Из того, что я могу сказать, что эти шарашки, кажется, заразили необычную часть твоего тела."
    call luna_main("Да... Обычно они только голову заражают.", 7, 2, 4, 4) 
    m "И как ты избавляешься от них в этой ситуации?"
    call luna_main("Думаю о хорошем, сэр...", 2, 2, 4, 1) 
    m "Правильно."
    m "Таким образом, в твоей текущей ситуации тебе просто нужно сосредоточить позитивные мысли на затронутой области."
    call luna_main("...", 1, 2, 5, 2) 
    call luna_main("Как я могу это сделать?", 1, 1, 4, 3) 
    m "Для начала, мы попробуем немного массажа в зараженном районе."
    call luna_main("Так мне надо массировать область, которую они делают неясной?", 1, 1, 4, 14) 
    m "Правильно, я буду здесь, чтобы давать тебе некоторые указания."
    call luna_main("Благодарю вас, профессор!", 2, 2, 4, 1) 
    m "Всегда пожалуйста."
    call luna_main("...", 1, 3, 4, 1) 
    $ luna_l_arm = 4
    ">Полумна быстро опускает руку под юбку, едва осознавая природу своих действий."
    call luna_main("Ах...", 5, 3, 4, 2) 
    m "Все в порядке, мисс Лавгуд?"
    call luna_main("Ах... ну конечно!", 4, 1, 4, 1) 
    call luna_main("Это место просто немного чувствительно...", 5, 3, 4, 1) 
    m "Это ожидалось. Продолжай."
    call luna_main("Да, сэр...", 2, 2, 4, 2) 
    g4 "..."
    call luna_main("Ах... Я правильно это делаю?", 1, 8, 4, 4) 
    m "Я уверен, если ты чувствуешь себя хорошо, значит это работает. Продолжай и ты избавишься от этих смаугов."
    call luna_main("Это приятно...", 3, 2, 4, 1) 
    call luna_main("...", 1, 8, 4, 2) 
    call luna_main("Вы уверены, что это сработает, сэр?", 5, 1, 4, 14) 
    m "Конечно уверен! Ты осмеливаешься сомневаться в силе Бублегума?"
    call luna_main("Конечно, нет, сэр...", 4, 2, 4, 2) 
    call luna_main("Просто...", 5, 3, 4, 2) 
    call luna_main("Я не уверена, что это поможет от них избавиться...", 5, 1, 4, 4) 
    m "Что заставляет тебя так думать?"
    call luna_main("Вы помните, как я сказала, что мозгошмыги похожи на неприятный зуд, сэр?", 5, 2, 4, 2) 
    m "И..."
    call luna_main("Ну... Так же, как этот массаж...", 5, 3, 4, 2) 
    call luna_main("Сэр, это не совсем чесотка...", 7, 8, 4, 4) 
    call luna_main("... {p}Я делаю это неправильно, сэр?", 5, 1, 4, 2) 
    m "Конечно, нет, но дело хуже, чем я представлял."
    call luna_main("Правда?", 4, 1, 4, 2) 
    m "Да. Кажется, эти неприятные твари пытаются спрятаться."
    call luna_main("Спрятаться? Где?", 4, 3, 4, 2) 
    m "Ну, пока ты все еще чувствуешь зуд, они не могли уйти далеко."
    m "Но это означает, что тебе придется преследовать их."
    call luna_main("Преследовать их?", 5, 1, 5, 2) 
    m "Не волнуйся, я буду здесь, чтобы помочь тебе справится."
    call luna_main("Спасибо, сэр.", 1, 2, 4, 1) 
    m "Прежде всего, закрой глаза."
    call luna_main("...", 2, 2, 4, 2) #eyes closed
    m "Отлично. Теперь я хочу, чтобы ты изолировалась от всего остального."
    call luna_main("Хорошо, сэр...", 2, 2, 4, 3) 
    m "Представь, что ты одна в своей комнате."
    call luna_main("Да...", 2, 2, 4, 2) 
    m "Тебе хорошо и уютно, ничего постороннего тебя не отвлекает."
    call luna_main("...", 2, 2, 4, 1) #smile
    m "Теперь сосредоточься на том, где зудит сильнее."
    call luna_main("Ах... хорошо...", 2, 2, 1, 1) 
    m "Я хочу, чтобы ты погналась за этим чувством своими пальцами."
    call luna_main("...", 2, 2, 1, 2) 
    m "Сосредоточься на том, чтобы поймать его."
    call luna_main("Я не могу...", 2, 2, 4, 4) 
    call luna_main("Это как, пытаться поймать солнечные лучи...", 2, 2, 4, 2) 
    m "Не пытайся поймать, просто проведи по нему кончиками пальцев."
    call luna_main("...", 2, 2, 4, 1) 
    call luna_main("...", 2, 2, 1, 1) 
    ">Полумна начинает двигать пальцами под юбкой."
    call luna_main("Ах...", 2, 2, 4, 1) 
    call luna_main("Ммм...", 2, 2, 4, 5) 
    ">Полумна начинает тихо стонать."
    call luna_main("Я близко, сэр...", 2, 2, 4, 1) 
    m "Хорошо. Просто держи глаза закрытыми и сосредоточься на пальцах."
    call luna_main("{image=textheart}", 2, 2, 1, 5) 
    call luna_main("Ах... Я думаю, что это работает, сэр!", 2, 2, 4, 1) 
    call luna_main("Я думаю, что у меня получится поймать его!", 2, 2, 1, 1) 
    m "Тихо, не говори, просто сосредоточься..."
    call luna_main("Ладно...", 2, 2, 4, 2) 
    call luna_main("...", 2, 2, 4, 1) 
    call luna_main("Ах...", 2, 2, 4, 5) 
    call luna_main("{image=textheart}", 2, 2, 4, 1) 
    call luna_main("...", 2, 2, 4, 3) 
    call luna_main("Ах... сэр...", 5, 1, 4, 2) 
    call luna_main("Я думаю...", 5, 3, 4, 5) 
    call luna_main("Ах...", 5, 2, 4, 5) 
    call luna_main("Я думаю, что почти поймала...", 2, 2, 4, 5) 
    m "Тссс..."
    call luna_main("Ах...", 2, 1, 2, 5) 
    ">Пальцы Полумны начинают яростно двигаться под юбкой."
    call luna_main("Мммм...", 2, 1, 2, 1) 
    call luna_main("Ах...", 2, 1, 2, 5) 
    call luna_main("А-ах...", 5, 3, 4, 1) 
    call luna_main("Да...", 5, 8, 2, 1) 
    m "(Я думаю, что это оно и есть!)"
    call luna_main("Ах... ах...{image=textheart}", 5, 2, 4, 5) 
    call luna_main("{size=+4}Ммм... да...{image=textheart}{/size}", 5, 3, 4, 1) 
    call luna_main("{size=+8}Ах... ах...{/size}", 5, 8, 4, 5) 
    call luna_main("!!!", 4, 9, 1, 5) #orgasm face
    ">Под ногами Полумны образовалась лужица."
    call luna_main("Ах! Я думаю, они нападают на меня, сэр!", 4, 8, 4, 1) 
    call luna_main("!!!", 1, 9, 4, 1) #orgasm face
    m "Все в порядке?"
    call luna_main("Ах... Да, сэр...{image=textheart}", 5, 2, 4, 2) 
    call luna_main("Это, просто...", 5, 2, 4, 1) 
    m "..."
    call luna_main("Я... Я никогда...", 5, 2, 4, 2) 
    call luna_main("...", 5, 3, 4, 1) 
    call luna_main("{size=-5}Ах...{/size}", 5, 2, 4, 1) 
    m "Итак, шмары оставили тебя в покое?"
    call luna_main("Я думаю, что да, сэр...", 5, 1, 4, 2) 
    $ luna_l_arm = 1
    ">Полумна медленно вытаскивает руку из-под юбки."
    call luna_main("По крайней мере, этот неприятный зуд, кажется, исчез.", 1, 1, 4, 1) 
    m "Фантастика! На этом все, мисс Лавгуд."
    call luna_main("О... Вы хотели, чтобы я уже ушла, сэр?", 5, 3, 4, 2) 
    m "Если у тебя больше нет вопросов."
    call luna_main("Полагаю, нет... Но что, если это чувство вернется, сэр?", 5, 2, 4, 3) 
    call luna_main("Должна ли я попытаться избавиться от них самостоятельно?", 5, 3, 4, 2) 
    m "Конечно, нет!"
    call luna_main("Правда? Почему нет?", 4, 1, 4, 2) 
    m "Как я уже говорил, мисс Лавгуд, эта техника должна храниться в секрете."
    m "Не говоря уже о том, что рассеивание их в вашей общей комнате может привести к школьной вспышке."
    call luna_main("Так что мне делать, если они вернутся?", 1, 1, 4, 2) 
    m "Если ты когда-нибудь почувствуешь, что тебе снова нужно избавиться от этих надоедливых штуковин, моя дверь всегда открыта."
    call luna_main("Вы уверены в этом, сэр?", 5, 1, 4, 2) 
    call luna_main("Я бы не хотела вас беспокоить...", 5, 2, 4, 2) 
    m "Поверь, все нормально! Кроме того, я уже давно собирался протестировать эту технику."
    m "Если что, ты сможешь помочь мне с очень важными исследованиями."
    call luna_main("Правда? Спасибо вам большое, сэр.", 4, 1, 1, 1) 
    call luna_main("Надеюсь, они оставят меня в покое, но если нет, я приду к вам снова.", 1, 2, 4, 1) 
    m "С нетерпением жду этого момента."
    call luna_main("...", 5, 1, 4, 1) 
    ">Полумна дарит тебе последнюю улыбку перед выходом из кабинета."
    jump luna_away


label luna_cum_addict_event:
    $ luna_addicted = True #luna is now a cum addict. I'm a bit undecided about the whole thing tbh, might ruin the dom path but idk, we can work it in, make her a dommy cumslut or whatever........
    ">Ты положил руки на плечи Полумны и поставил ее на колени."
    $ luna_l_arm = 2
    $ luna_r_arm = 2
    call gen_main("Давай, вниз!", 4, 4) 
    $ luna_ypos = 225
    $ luna_xpos = 350
    call luna_main("Остановитесь сейчас же! Это не вариант, [l_genie_name]!", 4, 1, 3, 15) 
    g4 "Аргх, слишком поздно шлюха!"
    call luna_main("!!!", 3, 1, 3, 3) 
    $ luna_cum = 11
    show screen white 
    pause.1
    hide screen white
    pause.2
    show screen white 
    pause .1
    hide screen white
    with hpunch
    $ luna_wear_cum = True
    ">Полумна смотрит на тебя с яростью в глазах в волне горячей спермы!"
    pause
    g4 "Ох! Боги {size=+10}ДА!{/size}"
    call luna_main("...", 5, 5, 1, 2) 
    call luna_main("(Что это за запах?)", 5, 7, 4, 4) 
    g4 "{size=+10}ВОЗЬМИ ВСЕ ЭТО, большегрудая ШЛЮХА!{/size}"
    g4 "Мммм....."
    hide screen g_c_c_u
    $ g_c_u_pic = "images/animation/06_jerking_01.png"
    $ luna_r_arm = 2
    hide screen genie_sprite
    $ genie_sprite_base = "characters/genie/base_2.png"
    with d3
    m "Это сразу бросилось в глаза..."
    call luna_main("...", 8, 4, 3, 4) 
    call luna_main("......", 7, 7, 2, 2) 
    call luna_main(".........", 5, 6, 4, 1) 
    m "Ах... ты была фантастической, шлюха..."
    $ g_c_u_pic = "images/animation/06_groping_01.png"
    call luna_main("Что {size=+4}это{size=+4} за  {size=+4}запах?{/size}", 4, 1, 4, 1) 
    m "Сперма?"
    ">Полумна встает с колен"
    $ luna_ypos = 0
    call luna_main("{size=+4}Они{/size}", 9, 4, 3, 3) 
    call luna_main("{size=+8}запахи{/size}", 8, 7, 2, 2) 
    call luna_main("{size=+12}Невероятно!!!{/size}", 4, 6, 4, 1) 
    m "..."
    m "Что?"
    call luna_main("Боже мой!!! В ней столько магической энергии!", 4, 8, 4, 1) 
    call luna_main("Я никогда не чувствовала ничего настолько мощного!", 4, 3, 4, 1) 
    m "Ах да, я ж великий Фамбелдор!"
    call luna_main("Тем не менее, сэр...", 7, 1, 2, 4) 
    call luna_main("Этот запах... Его слишком много, для простого смертного...", 7, 1, 1, 1) 
    m "(Дерьмо...)"
    call luna_main("Я могу...", 1, 1, 4, 2) 
    call luna_main("Ее попробовать?", 5, 2, 4, 2) 
    m "Что за вопрос?"
    call luna_main("Если ее так много...", 4, 1, 4, 2) 
    g9 "Конечно, ты можешь попробовать мою сперму девочка!"
    call luna_main("Спасибо, сэр...", 4, 1, 4, 1) 
    m "(Она кажется другой...)"
    $ luna_cum = 12
    ">Полумна собирает капли спермы в кучку на конце пальца, прежде чем положить ее в рот."
    call luna_main("{image=textheart}{image=textheart}{image=textheart}", 5, 6, 4, 13) 
    call luna_main("{size=+4}это {size=+4}удивительно!!!!!{image=textheart}{image=textheart}{/size}", 2, 8, 4, 1) 
    call luna_main("Могу я попробовать еще? Пожалуйста, сэр?", 4, 1, 4, 1) 
    m "Конечно..."
    ">Ты смотришь, как Полумна медленно собирает всю твою сперму в рот и проглатывает ее."
    $ luna_cum = 13
    call luna_main("...", 5, 6, 4, 13) 
    call luna_main("{image=textheart}{image=textheart}{image=textheart}", 2, 8, 4, 1) 
    pause
    $ luna_cum = 14
    call luna_main("...", 5, 6, 4, 13) 
    call luna_main("{image=textheart}{image=textheart}{image=textheart}", 2, 8, 4, 1) 
    $ luna_cum = 15
    call luna_main("...", 5, 6, 4, 13) 
    call luna_main("{image=textheart}{image=textheart}{image=textheart}", 2, 8, 4, 1) 
    $ luna_wear_cum = False
    call luna_main("Ах...", 2, 8, 4, 1) 
    call luna_main("Удивительно...", 5, 8, 4, 1) 
    m "Наслаждаешься?"
    call luna_main("Как я могла это сделать?", 7, 2, 2, 4) 
    m "(Что здесь вообще происходит? Она снова выглядит стервозной...)"
    call luna_main("Вы должны сказать мне, как вы это сделали!", 8, 1, 2, 2) 
    m "Кончил? Я уверен, что у тебя все получилось..."
    call luna_main("Не это, идиот!", 9, 1, 3, 2) 
    call luna_main("Почему это содержало так много волшебной энергии?", 7, 1, 2, 2) 
    call luna_main("Мы Лавгуды чувствительны к магии, но единственный раз я испытывала подобное, когда мне позволили немного попробовать спермы Джинна...", 7, 2, 3, 4) 
    call luna_main("Но все знают, что Джинов перебили тысячелетие назад...", 8, 1, 2, 2) 
    g4 "(!!!)"
    m "О, эм..."
    m "Коммерческая тайна..."
    call luna_main("Отлично! Пусть будет так, [l_genie_name]...", 6, 2, 2, 4) 
    ">Полумна одевается, смотря гневно на тебя."
    $ luna_wear_skirt = True
    $ luna_wear_bra = True
    $ luna_wear_panties = True
    $ luna_wear_top = True
    call luna_main("ТОлько не ждите, что я уйду, не получив оплату, [l_genie_name]!", 8, 1, 2, 2) 

    hide screen bld1
    m "Хорошо... Так или иначе, вот твоя оплата [luna_name]."
    $ gold -= current_payout
    $ luna_gold += current_payout
    ">Ты вручаешь Полумне [current_payout] галлеонов."
    call luna_main("Спасибо, [l_genie_name].", 5, 2, 1, 1) 
    ">Полумна покидает твой кабинет."  

    hide screen g_c_u
    show screen genie
    hide screen chair_left
    hide screen desk

    jump luna_away





