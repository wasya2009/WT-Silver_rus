

### POLYJUICE POTION ###

#Cat ears.

label potion_scene_1_1_1: #catears (keep in mind Genie is trying to transform her into another girl)
    m "[hermione_name]?"
    call her_main("Да, [genie_name]?","base","base") 
    m "Сегодня у меня есть новое задание для тебя."
    call her_main("Что значит новое? Что мне нужно сделать?","normal","frown") 
    m "Это довольно просто, сегодня ты будешь пить зелье."
    call her_main("Сколько я получу за это?","open","suspicious") 
    m "20 очков."
    call her_main("Хм... А что это за зелье?","annoyed","suspicious") 
    call her_main("Polyjuice? Amortentia? Babbling Beverage? Felix Felicis?","grin","worriedCl",emote="05") 
    m "Это секрет, [hermione_name]."
    call her_main("...","annoyed","down") 
    m "Ладно, [hermione_name], что скажешь? Ты будешь пить это маленькое безобидное зелье?"
    m "За Гриффиндор?"
    call her_main("Ладно...","open","closed") 
    call nar(">Гермиона пробует густое зелье.") 
    call her_main("Это пахнет отвратительно. Как грязь и мокрый мех собаки. disgust","narrow") 
    call her_main("Я точно должна пить это?","open","worried") 
    m "Ты должна. Я предлагаю зажать пальцами нос, если оно так дурно пахнет."
    call her_main("За Гриффиндор.","mad","worriedCl",tears="soft_blink") 
    
    call her_chibi("drink_potion","mid","base") 
    
    call nar(">Гермиона зажимает нос и быстро опустошает колбу.") 
    call her_main("","full","ahegao_intense") 
    pause
    call her_main("","angry","base",tears="soft") 
    
    call her_chibi("stand","mid","base") 
    
    her "Уххх. Это ужасно."
    m "Очень хорошо."
    call her_main("Теперь-то вы можете сказать, что делает это зелье?","angry","base",tears="soft") 
    m "Мы можем узнать это в любой момент..."
    call her_main("Что ж? Вы думаете, что моя грудь станет больше? Я не чувствую, что она увеличивается.","annoyed","down") 
    m "Нет. Хмммм, это, вероятно, не сработало."
    call her_main("Что оно должно было сделать?","annoyed","ahegao") 
    m "Нечего не расскажу, это должен был быть сюрприз."
    m "Черт!"
    call her_main("Это все, [genie_name]?","soft","base") 
    m "Да, [hermione_name], 20 очков Гриффиндору."
    call her_main("Спасибо [genie_name].","base","base") 
    call nar(">Гермиона возвращается в класс.") 
    $ gryffindor += 20

    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    call her_walk("mid","leave",2) 
    
    $ cat_ears_potion_return = True #Triggers Hermione return

    #Equip Cat-Ears
    $ h_ears = "cat_ears"
    $ h_request_wear_ears = True
    $ hermione_wear_ears = True
    call update_her_uniform 

    $ hermione_takes_classes = True
    jump day_main_menu

label potion_scene_1_1_2: #Scene where Hermione comes back after classes angry and confused at being given cat ears and a tail.
    call play_sound("door") #Sound of a door opening.
    call her_chibi("stand","mid","base") 
    
    show screen bld1
    call her_main("Как вы могли так поступить со мной, [genie_name]?","angry","angry") 
    her "Пытаетесь превратить меня в кошку!!"
    call her_main("Ну же!","annoyed","worriedL") 
    m "Я не пытался превратить тебя в кошку, [hermione_name]."
    call her_main("Тогда почему у меня уши и хвост?!","scream","angryCl") 
    m "Я не знаю, вообще-то я пытался превратить тебя в другую девочку."
    call her_main("Что? Это было зельем превращения, [genie_name]?","shock","wide") 
    m "А чего такого?"
    call her_main("Нет смысла придуриваться, [genie_name].","annoyed","annoyed") 
    call her_main("По крайней мере, я знаю, что к утру эффект рассеется...","annoyed","angryL") 
    
    menu:
        "-Отпустить ее-":
            m "Доброй ночи, [hermione_name]."
            call her_main("Доброй, [genie_name].","upset","closed") 
            hide screen bld1
            hide screen hermione_main
            hide screen blktone 
            hide screen ctc
            with d3
            
            call her_walk("mid","leave",2) 
            
            $ cat_ears_potion_return = False #Triggers Hermione return
            $ h_request_wear_ears = False
            $ hermione_wear_ears = False
            call update_her_uniform 

            $ hermione_sleeping = True
            jump night_main_menu
            
        "-Заставить ее отсосать-" if whoring >= 17:
            pass
            
    m "Подожди, [hermione_name], не желаешь заработать 75 очков Гриффиндору?"
    call her_main("75 очков?! Как?","annoyed","suspicious") 
    m "За отсос."
    call her_main("Как? Я похожа на кошку! Почему вы спрашиваете меня об этом именно сейчас?","angry","wide") 
    call her_main("Вы же не какой-то извращенец, которому нравится спариваться с животными? И за жестокое обращение с животными можно сесть по статье 245 УК РФ!","angry","base")   
    m "Я просто думаю, ты сейчас выглядишь крайне уникально, чтобы этим не воспользоваться..."
    call her_main("Ладно, просто пообещайте что не будете делать ничего странного.","upset","closed") 
    m "Обещаю. Теперь встань на колени."
    call blkfade 
    pause.5
    
    ">Гермиона подходит и становится на колени возле тебя."
    m "Хорошая девочка."
    call her_main("...","open_wide_tongue","base") 
    ">Гермиона берет в ротик."                ###Have the chibi scene of her sucking
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    hide screen genie
    
    $ genie_chibi_xpos = -10 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "blowjob_ani"
    show screen chair_left
    show screen g_c_u
    
    call her_chibi("hide") 
    hide screen blkfade
    hide screen blktone
    hide screen bld1
    with fade
    call ctc 
    
    call bld 
    m "Господи, что с твоим языком?! Он как липучка."
    her "*Чавкает*"  
    $ g_c_u_pic = "hand_ani"
    with d3
    $ hermione_main_zorder = 8
    call her_main("Это из-за вашего глупого зелья, оно \nсделало мой язык более шершавым.","open_wide_tongue","angry") 
    call her_main("Вы хотите что бы я остановилась?","grin","baseL") 
    hide screen hermione_main
    m "Нет, продолжай, просто старайся языком меньше касаться моего члена."
    call her_main("Хорошо, [genie_name].","annoyed","angryL") 
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3
    
    call nar(">Гермиона снова глотает ваш член, заботясь\nо том, что бы не доставлять дискомфорта своим язычком.") #start sucking scene. might insert more sucking noises for a little while or add pauses
    m "Ты собираешься идти на свои уроки?"
    $ g_c_u_pic = "hand_ani"
    with d3
    call her_main("Конечно, [genie_name].","base","glance") 
    hide screen hermione_main  
    $ g_c_u_pic = "blowjob_ani"
    with d3
    m "Даже выглядя вот так?"                         ###start sucking
    m "Что люди могут подумать? Разве они просто не предположат, что ты оказалась под злым слизеринским заклинанием?"
    m "Или они просто подумают, что маленькая мисс Грейнджер снова попрошайничает..."
    m "Нося мало одежды и выглядя как кошка?"
    call nar(">Ты хочешь положить свои ладони ей на затылок, но уши препятствуют этому.") 
    m "Они довольно мягкие."
    call nar(">Ты начинаешь мило поглаживать ее ушки.","start") 
    call nar(">Гермиона начинает невольно мурлыкать.","end") 
    m "Святые угодники!"
    m "Ух ты, похоже на то, что весь ее рот стал вибратором."
    $ g_c_u_pic = "hand_ani"
    with d3
    call her_main("Я ничего не могу сделать, [genie_name], всякий раз, когда \nчто-нибудь касается моих ушей, я просто начинаю мурлыкать...","base","happyCl") 
    hide screen hermione_main
    m "Это потрясающе, теперь суй его обратно себе в рот."
    call her_main("Хорошо, [genie_name].","smile","happyCl",emote="06") 
    $ g_c_u_pic = "blowjob_ani"
    with d3
    hide screen hermione_main
    with d3
    m "Ты сразу кладешь руки на ее ушки и начнешь гладить их, когда она тебе сосет."### start sucking
    her "*Чавкает*"
    m "Господи, это фантастика."
    her "*Чавкает*"
    m "Готовься, девочка, великий потоп на подходе."
    her "*Чавкает*"
    call nar(">Ты хватаешь ее за уши и тянешь за голову, чувствуя, что уже на подходе.") #show genie climax scene
    g4 "{size=+10}ЕЕЕЕ!!!!!!!!!!!!!!!!!{/size}"
    her "*Чавкает*"
    call nar(">Ты кончаешь ей прямо в глотку.") #have picture 125 and 126 play each time she swallows
    call ctc 
    
    $ g_c_u_pic = "cum_in_mouth_ani"
    with d3
    call her_main("","full_cum","dead") 
    pause .1
    call her_main("*странные звуки*","cum","worriedCl") 
    call her_main("","full_cum","dead") 
    pause .1
    call her_main("*странные звуки*","cum","worriedCl") 
    call her_main("","full_cum","dead") 
    pause .1
    call her_main("*странные звуки*","cum","worriedCl") 
    call nar(">Ты вытаскиваешь свой член из ее мурлыкающего рта.") 
    call her_main("Мммм, это зелье не так плохо на \nвкус...","base","glance") 
    hide screen hermione_main
    m "Хорошо, ты честно отработала свои 75 очков."
    $ gryffindor += 75
    $ g_c_u_pic = "hand_ani"
    with d3
    call her_main("Спасибо, [genie_name]. Это все?","base","ahegao_raised") 
    hide screen hermione_main
    m "Одна последняя вещь."
    m "Кто хорошая девочка?"
    call her_main("..........","annoyed","worriedL") 
    call her_main("Мур... Я.....","smile","baseL") 

    $ hermione_main_zorder = 5
    hide screen hermione_main
    hide screen chair_left
    call her_chibi("hide") 
    call gen_chibi("hide") 
    show screen genie
    hide screen bld1
    hide screen blktone 
    with fade

    $ cat_ears_potion_return = False #Triggers Hermione return
    $ hermione_wear_ears = False
    call update_her_uniform 

    $ hermione_sleeping = True
    jump night_main_menu
    
    
#Luna transformation.

label potion_scene_1_2: #Luna potion
    m "Могу я предложить тебе выпить?"
    call her_main("Вы же не собираетесь спаивать меня?","normal","base") 
    m "Ничего подобного, просто безвредное маленькое зелье."
    call nar(">Ты вручаешь ей бутылочку зелья.") 
    call her_main("Ваше очередное таинственное зелье?","open","suspicious") 
    her "Дайте угадаю, вы, конечно же, не расскажете об его эффектах и мне придется опозориться перед всем классом?"
    m "Не совсем."
    call her_main("Что-то новое.","annoyed","suspicious") 
    her "... как-то волнующе."
    her "Так что же это такое?"
    m "Это просто зелье превращения."
    call her_main("Умгх, оно такое противное.","normal","worriedCl") 
    her "... и в кого оно превратит меня?"
    m "Это, мисс Грейнджер, является секретом."
    call her_main("Как всегда.","normal","baseL",tears="soft") 
    m "Все это будет куда приятнее, если ты представишь, сколько очков за это получишь."
    m "Насколько сильно ты готова опередить по очкам Слизерин?"
    her "Вы правы, [genie_name]. Я не могу позволить Гриффиндору проиграть."
    
    call her_chibi("drink_potion","mid","base") 
    pause 2
    
    call nar(">Она опустошает бутылочку зелья.") 
    pause.5
    
    call her_chibi("stand","mid","base") 
    
    call her_main("Брррр.","disgust","narrow") 
    her "Это похоже на сопли тролля..."
    m "Пока ты пьешь это, ты зарабатываешь Гриффиндору много очков."
    her "И буду над этим работать."
    call her_main("Что теперь? Мне нужно идти в класс?","upset","wink") 
    m "Еще нет, расскажи мне что-нибудь."
    call her_main("Ну, с тех пор как я начала свои \"Внеклассные занятия\" с вами, моя посещаемость и оценки стали падать.","open","closed") 
    m "На самом деле?"

    if whoring <= 13:
        call her_main("Да! [genie_name], раньше я была лучшей в классе. Мои оценки были безупречны. ","scream","angryCl") 
        m "И как твои оценки сейчас?"
        call her_main("Я все еще на высоте, но уже не так сильно.","annoyed","angryL") 
        m "Настали времена, когда учебное превосходство не должно быть твоей главной заботой."
        call her_main("Хммм, и что \'должно\' быть моей главной заботой?","annoyed","suspicious") 
        m "В данный момент, я бы сказал, что твое лицо сейчас в приоритете."
        call her_main("Извините, такое вряд ли подходит директору.","open_tongue","glance") 
        m "Нет, я серьезно. Ты правда должна увидеть изменения на своем лице."

    else:
        call her_main("Нет. Я понимаю, что есть другие вещи, в которых я могу преуспеть.","base","base") 
        m "Такие вещи, как сосать член за очки факультета?"
        call her_main("Профессор!","scream","angryCl") 
        m "Ох, не будь такой скромной, если бы по сосанию члена был бы разряд, ты была бы Сашей Грей."
        call her_main("Благодарю вас, профессор. Знаете, есть немного времени, чтобы заработать еще несколько очков перед уроком. Если вы не против, я могу...","scream","angryCl") 
        m "Я должен знать, на чье лицо буду кончать. "
        call her_main("Что вы имеете в виду?... Мое лицо конечно... Я имею в виду...","scream","angryCl") 
        m "Может, подойдешь к зеркалу?..."
        
    "*POOF*"
    hide screen hermione_main
    hide screen hermione_blink
    $ luna_chibi("stand")
    
    $ changeLuna(1, 1, 4, 1)
    
    her "Уххх, я чувствую. что из меня сейчас что-то выйдет...Зелье работает?"
    m "Прям магия какая-то."
    call nar(">Гермиона начинает изучать себя, щупая свою одежду, она остановилась на груди.") 
    $ changeLuna(5, 1, 5, 1)
    her "Видимо, я все еще девочка. Кто-то из Когтеврана?"
    m "Ты очень наблюдательная."
    call nar(">Гермиона хватает себя за волосы.") 
    $ changeLuna(1, 7, 1, 4)
    her "Определенно блондинка, хотя она могла бы время от времени расчесывать свои волосы..."
    $ changeLuna(1, 5, 1, 1)
    call nar(">Внезапно Гермиона чувствует, что что-то застряло в неубранных волосах. При ближайшем рассмотрении - это оказывается волшебной палочкой.") 
    $ changeLuna(4, 1, 3, 1)
    her "..."
    her "Вы превратили меня в... Полумну Лавгуд?!"
    m "Ты такая проницательная, [hermione_name]."
    m "(Без понятия кто это, но она очень симпатичная)"
    $ changeLuna(4, 1, 3, 17)
    her "Почему вы хотите, чтобы я выглядела как Полумна? Она же сумасшедшая!"
    m "Я не вижу в ней ничего плохого."
    $ changeLuna(1, 1, 4, 4)
    her "У нее... есть воображаемые друзья и она верит в то, что, возможно, не существует, [genie_name]. Она безумна!"
    m "К счастью, меня не интересует ее психическое здоровье. Меня интересует ее впечатляющая и вполне реальная грудь."
    $ changeLuna(5, 1, 5, 3)
    her "Вы не заинтересованы в... женской маленькой груди..."
    m "В настоящее время она у тебя. И она выглядит не такой уж и маленькой, [hermione_name]. Мне кажется...кто-то ревнует?"
    $ changeLuna(1, 1, 3, 3)
    her "Совсем нет, я полагаю, вполне естественно, что у вас из за преклонного возраста проблемы со зрением."
    m "(Я определенно задел за живое) Как ты разговариваешь со старшими, [hermione_name]? Возможно, тебе нужна хорошая порка, чтобы напомнить о правильных манерах."
    $ changeLuna(1, 1, 4, 9)
    her "Я... прошу прощения, [genie_name]. Я не знаю, что случилось со мной."
    m "Извинения приняты. Но я уверен, что твои извинения не такие яркие, как твои сиськи."
    $ changeLuna(1, 2, 1, 4)
    her "Мне хотелось бы думать, что я больше, чем просто парочка сисек, но спасибо, [genie_name]. Это было лестно. В некотором смысле."
    m "Если ты хочешь развеять все сомнения, мы могли бы сравнить. Почему бы тебе не поднять рубашку и не показать мне, что ты... ошибаешься..."
    $ changeLuna(4, 2, 3, 4)
    her "Мне все еще не очень комфортно..."
    call nar(">Гермиона быстро снимает свой верх, добираясь до лифчика.") 
    hide screen luna
    $ luna_chibi("stand_topless")
    $ luna_wear_top = False
    $ luna_wear_bra = False
    $ changeLuna(5, 2, 5, 3)
    her "Видите. Совершенно обычная грудь."
    m "Я не совсем уверен...мягкая бледная кожа, симпатичные розовые сосочки. Я думаю, что у тебя может быть серьезная конкуренция, [hermione_name]."
    $ changeLuna(5, 1, 3, 17)
    her "Вы наверное шутите?! Они же повисают и даже не вмещаются в ладонь!"
    m "Хммм, я не уверен. Я думаю, что требуется более тщательное изучение."
    call nar(">В отчаянии Гермиона подходит и дает тебе рассмотреть свою новую грудь.") 
    m "Да, при тщательном осмотре, кажется, что я ошибся. Грудь Полумны и правда уступает твоей."
    $ changeLuna(5, 1, 3, 4)
    her "Я рада, что вы изменили свое мнение. Спасибо. Если это все, я пойду."
    m "Достаточно, [hermione_name]. 20 очков Гриффиндору."
    hide screen luna
    $ luna_chibi("stand")
    $ luna_wear_top = True
    $ luna_wear_bra = True
    $ changeLuna(3, 1, 1, 1)
    her "Ну, я лучше подойду в класс."
    m "Ты пойдешь на уроки, выглядя как другой человек?"
    $ changeLuna(1, 1, 5, 1)
    her "Это не проблема. Полумна вряд ли в своем классе, я могу просто притвориться, что я - это она. Возможно, я даже улучшу ее результаты тестов. А вы скажете учителям, что я не смогу пока посещать занятия?"
    m "Хм. Но, что, если ты столкнешься с ней в залах?"
    $ changeLuna(5, 1, 1, 4)
    her "Поверьте, [genie_name], Полумна, вероятно, подумает, что я просто в ее воображении или что-нибудь подобное."
    hide screen bld1
    hide screen blkfade
    hide screen luna
    $ menu_x = 0.5 
    $ hermione_takes_classes = True
    call play_sound("door") #Sound of a door opening.
    hide screen luna_chibi
    with d3
    jump day_main_menu

    
#Lamia transformation.
    
label potion_scene_1_3: #Lamia potion
    call her_main("Это глупо.","scream","worriedCl") 
    m "У меня нет слов."
    jump day_main_menu

    
#Clone transformation.
    
label potion_scene_1_4: #Clone potion
    m "Ты когда-нибудь испытывала противоречия в том, что мы делаем здесь? [hermione_name]?"
    her "Противоречия... Я думаю,что я... А почему вы спрашиваете?"
    m "Потому что у меня есть новое зелье, которое может помочь тебе разобраться со своими внутренними конфликтами."
    her "Что? Как?"
    m "Он разбивает твой разум на две части, позволяя тебе противостоять себе и решать проблему."
    her "Разделяет мой разум?! Это звучит не очень безопасно!"
    m "Это только метафорически разлагает твой разум. Я гарантирую, что это безопасно."
    her "Хорошо, если вы делали это сами."
    m "Конечно, нет... теперь, если ты не против, выпей его, мы сможем разобраться с твоей противоречивой природой."
    her "..."
    her "Ну ладно, что ж..."
    call nar(">Гермиона пьет зелье.") 
    her "Мммммм, сладкое...."
    herA "Ухххх...какое кислое...."

    #Hermione split into two versions of herself, one slutty, one prudish
    #Slutty one wants to have sex with Genie 
    #Genie obliges
    #Slutty Hermione enjoying it immensely 
    #Genie trying to convince pruddy Hermione to join in
    #Prude Hermione wants no part in it, although she is slightly aroused
    #Slut Hermione 
    #Genie cums in Hermione
    #Slut Hermione wants to go again 
    #Slut Hermione offers to suck Genie to get him hard 
    #Genie says why don't we get prude Hermione to do it
    #Slut Hermione says that's a great idea
    #Prude Hermione refuses
    #Slut Hermione and Genie force her to her knees
    #Genie talks dirty to Prude Hermione while Slutty Hermione encourages her
    #Genie ends up covering her in cum
    #Prude Hermione partially speechless
    #Slutty Hermione wants to go again but Genie is spent
    #Hermione reforms into one person
    #Genie ridicules her, saying that even the most prudish and reseverved version of herself ended up sucking him off
    #Hermione feels both shame and pride
    #THE END

    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    call her_walk("mid","leave",2) 
    
    $ hermione_takes_classes = True
    jump day_main_menu