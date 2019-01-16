

label equipping_failed:

    if mad >= 1 and mad <=5:
        if wardrobe_chitchat_active:
            hide screen hermione_main 
            with d3

            $ hermione_xpos = 665
            $ wardrobe_active = 0 #activates dissolve in her_main 

            m "[hermione_name]..."
            m "Ты будешь ходить в этом--"
            call her_main("Извините [genie_name],...","open","closed") 
            call her_main("Но мне не хочется наряжаться сегодня для вас.","open","worriedL") 
            m "Есть шанс убедить тебя в обратном?"
            call her_main("Хм...","annoyed","base") #very upset, default
            call her_main("Я хочу 5 очков факультету! И то, это не гарантирует, что я действительно буду это носить...","open","closed") 
            call her_main("Как бы то ни было, вы хотите, чтобы я это надела.","annoyed","annoyed") 

            $ menu_x = 0.2 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
            menu:
                "-Дать ей очки-":
                    m "Хорошо, [hermione_name],... вот твои очки..."
                    m "кхм--кхм..."
                    m "Пять очков Гриффиндору!"
                    m "Этого достаточно для тебя?"
                    call her_main("...","normal","base") 
                    call her_main("Спасибо, [genie_name].","soft","baseL") 
                    m "Отлично, теперь я забыл, что я хотел, чтобы ты надела..."
                    $ gryffindor += 5
                    $ mad = 0
                    call her_main("","","",xpos="wardrobe",trans="d3") 
                "-Не давать ей очков.-":
                    m "Я так не думаю, мисс!"
                    call her_main("...","annoyed","frown") 
                    call her_main("Отлично!","angry","angry") 
                    call her_main("Они мне все равно не нужны!","annoyed","down") 
                    m "Ты уверена?"
                    call her_main("Tzzz--","angry","angry") 
                    call her_main("","","",xpos="wardrobe",trans="d3") 
        else:
            hide screen hermione_main
            with d3
            ">Гермиона злится на тебя! Она не будет это носить!"
            menu:
                ">Ты можешь дать Гриффиндору очки, чтобы улучшить ее настроение."
                "-5 очков Гриффиндору!-":
                    $ gryffindor += 5
                    $ mad = 0
                    ">Гермиона больше не злится на тебя!"
                    $ hermione_xpos = 400
                    call her_main_rndm_happy 
                "-Не беспокоиться-":
                    $ hermione_xpos = 400
                    call her_main_rndm_angry 

        $ wardrobe_active = 1
        call her_main("","","",xpos="wardrobe") 
        call screen wardrobe
        

    if mad >= 6 and mad <=10:
        if wardrobe_chitchat_active:
            $ wardrobe_active = 0
            hide screen hermione_main
            with d3
            m "[hermione_name]..."
            m "Я хочу, чтобы ты надела--"
            call her_main("Нет, [genie_name]...","open","closed",xpos="base") #525=default Hermione xpos
            call her_main("Я все еще злюсь на вас за то, что вы сделали!","open","worriedL") 
            m "Ты наденешь его, если я дам Гриффиндору несколько очков?"
            call her_main("...","annoyed","suspicious") 
            call her_main("Пятнадцать очков!","open","base") 
            call her_main("И, возможно, я буду носить его. Но только возможно!","open","baseL") 

            $ menu_x = 0.2 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
            menu:
                "-Дать ей очки-":
                    m "Хорошо, [hermione_name],... вот твои очки..."
                    m "Пятнадцать очков..."
                    g4 "Гриффиндору!"
                    m "Этого достаточно для тебя?"
                    call her_main("(Из него настолько легко набить очков факультету!)","soft","baseL") 
                    call her_main("Спасибо, [genie_name].","open","closed") 
                    m "Без проблем! Теперь надень... {w=0.9} то, что я просил."
                    $ gryffindor += 15
                    $ mad = 0
                    call her_main("","","",xpos="wardrobe",trans="d3") 
                "-Не давать ей очков.-":
                    m "Я даю тебе новую одежду! Разве этого недостаточно?"
                    call her_main("Нет, этого недостаточно, [genie_name]!","open","closed") 
                    call her_main("Я хочу получить очки!","angry","angry") 
                    call her_main("(Можете засунуть эту одежду себе в зад...)","annoyed","angryL") 
                    m "Я не дам тебе очков, [hermione_name]."
                    call her_main("Tzzz--","angry","angry") 
                    call her_main("Ну тогда надень эти... {w=0.5}-вещи на себя!","scream","angryCl") 
                    m "Они будут хорошо смотреться на тебе..."
                    call her_main("Мне все равно.","annoyed","annoyed") 
                    call her_main("","","",xpos="wardrobe",trans="d3") 
        else:
            hide screen hermione_main
            with d3
            ">Гермиона действительно злится на тебя! Она не будет носить это!"
            menu:
                ">Ты можешь дать Гриффиндору очки, чтобы улучшить ее настроение."
                "-15 очков Гриффиндору!-":
                    $ gryffindor += 15
                    $ mad = 0
                    ">Гермиона больше не злится на тебя!"
                    $ hermione_xpos = 400
                    call her_main_rndm_happy 
                "-Не беспокоиться-":
                    $ hermione_xpos = 400
                    call her_main_rndm_angry 

        $ wardrobe_active = 1
        call her_main("","","",xpos="wardrobe") 
        call screen wardrobe


    if mad >= 11:
        if wardrobe_chitchat_active:
            $ wardrobe_active = 0 #activates dissolve in her_main
            hide screen hermione_main
            with d3
            m "[hermione_name]..."
            m "Пожалуйста--"
            call her_main("Нет--","open","closed",xpos="base") #525=default Hermione xpos
            call her_main("...","annoyed","annoyed") 
            m "Я просто хочу, чтобы ты надела--"
            call her_main("Я СКАЗАЛА НЕТ, [genie_name]!","scream","angryCl") 
            call her_main("tzzzz...","annoyed","angryL") 
            g4 "Отлично! {w=0.9}Забудь это."
            call her_main("","","",xpos="wardrobe",trans="d3") 
        else:
            hide screen hermione_main
            with d3
            ">Гермиона действительно злится на тебя! Нет смысла пытаться заставить ее это носить!"
            call her_main_rndm_angry 


        $ wardrobe_active = 1
        call her_main("","","",xpos="wardrobe") 
        call screen wardrobe









