init python:
    class hermione_job(object):
        inProgress = False
        responses = ""

        def checkProgress(self):
            if self.inProgress:
                renpy.jump(self.responses)



label maid_responses:
    $ payment = renpy.random.randint(10, 25)

    call play_sound("door") #Sound of a door opening.
    call her_walk("door","mid",2)
    pause.2

    call h_outfit_OBJ(hg_maid_OBJ)

    show screen bld1
    call her_main("","base","base",xpos="right",ypos="base")
    pause.5

    menu:
        "-Спросить, как прошел ее день-":
            if day_random <= 2:
                m "Как прошел твой день?"
                her "Он был как обычно, дневная уборка номера."
                her "Хотя учитывая, что я должна быть в классе в течении всего дня, я думаю, что это не нормально."
                m "Не волнуйся [hermione_name], ты получишь свои очки."
                m "Только подумай, как будут счастливы твои друзья, когда они выиграют Кубок в этом году."
                her "Наверное..."
                m "10 очков Гриффиндору"
                her "Спасибо [genie_name]"
                $ gryffindor+= 10
                $ gold += payment
            elif day_random >= 3 and day_random <= 5:
                her "Я действительно должна делать это?"
                m "Что ты имеешь в виду [hermione_name]?"
                her "Это так унизительно. Я должна убирать комнаты других студентов!"
                m "Ты можешь остановиться в любое время."
                her "Могу?"
                m "Конечно, я просто возьму одну из потаскушек Слизерина, которых ты обогнала."
                m "Я уверен, что они исполнят все прихоти за шанс заработать очки для своего факультета."
                m "Думаю они, могут и за бесценок, если не бесплатно."
                her "Хорошо, я поняла вас. Это просто... конечно, есть и другие способы заработать деньги [genie_name]?"
                her "Я имею в виду, что вы же директор школы, вы можете просто подать несколько отчетов и получить зарплату из Министерства?"
                m "Я могу, просто это не так приятно."
                her "Хммм. Могу я хотя бы сейчас получить свои очки?"
                m "Конечно, 10 очков Гриффиндору."
                her "Спасибо [genie_name]."
                $ gryffindor+= 10
                $ gold += payment
            elif day_random >= 6 and day_random <= 8:
                if whoring >= 15:
                    her " "
                else:
                    "bla bla bla"
            elif day_random >=9:
                if whoring >= 15:
                    "bla bla bla"
                else:
                    her "Я думаю, вам нужно начать применять более суровое наказание за сексуальные домогательства."
                    her "Хммм. Могу я хотя бы сейчас получить свои очки?"
                    m "Конечно, 10 очков Гриффиндору."
                    her "Спасибо [genie_name]."
                    $ gryffindor+= 10
                    $ gold += payment
        "-Отпустить ее-":
            her "Вот вся оплата."
            ">Ты получаешь [payment] галлеонов."
            m "Молодец [hermione_name], 20 очков Гриффиндору."
            her "Спасибо [genie_name]."
            $ gryffindor+= 20
            $ gold += payment

    call her_walk("mid","leave",2)

    $ hermione_sleeping = True
    $ current_job = 0
    jump night_main_menu

label barmaid_responses:
    $ payment = renpy.random.randint(20, 50)

    call play_sound("door") #Sound of a door opening.
    call her_walk("door","mid",2)
    pause.2

    call h_outfit_OBJ(hg_maid_OBJ)

    show screen bld1
    call her_main("","base","base",xpos="right",ypos="base")
    pause.5

    menu:
        "-Спросить, как прошел ее день-":
            if day_random <= 2:
                her "Хорошо."
                m "Ничего необычного не происходило?"
                her "Едва ли, я просто подаю людям напитки."
                m "Ну в таком случае 10 очков Гриффиндору."
                her "Спасибо [genie_name], вот вся оплата."
                ">Ты получил [payment] галлеонов."
                her "Доброй ночи [genie_name]."
                $ gryffindor+= 10
                $ gold += payment
            elif day_random >= 3 and day_random <= 5:
                "bla bla bla"
                jump day_time_requests
            elif day_random >= 6 and day_random <= 8:
                "bla bla bla"
                jump day_time_requests
            elif day_random >=9:
                "bla bla bla"
                jump day_time_requests
        "-Отпустить ее-":
            her "Вот вся оплата."
            ">Ты получаешь [payment] галлеонов"
            m "Молодец [hermione_name], 20 очков Гриффиндору."
            her "Спасибо [genie_name]."
            $ gryffindor+= 20
            $ gold += payment

    call her_walk("mid","leave",2)

    $ hermione_sleeping = True
    $ current_job = 0
    jump night_main_menu

label gryffindor_cheer_responses:
    $ payment = renpy.random.randint(40, 80)

    call play_sound("door") #Sound of a door opening.
    call her_walk("door","mid",2)
    pause.2

    call h_outfit_OBJ(hg_gryffCheer_OBJ)

    show screen bld1
    call her_main("","base","base",xpos="right",ypos="base")
    pause.5

    menu:
        "-Спросить, как прошел ее день.-":
            if day_random <= 2:
                m "Привет, [hermione_name], как прошел твой день?"
                call her_main("Было хорошо [genie_name], я думаю, что команда действительно начинает оживляться.","base","base")
                m "Как так?"
                call her_main("С момента когда я начинала, похоже они, улучшили свою игру.","open","base")
                call her_main("Они также кажутся намного счастливее. Гарри всегда смотрит на меня с улыбкой на лице.","base","base")
                m "И он часто на тебя смотрит?"
                call her_main("Конечно, мы же хорошие друзья.","open","base")
                m "Я уверен, что причина в этом."
                call her_main("Ну, вот деньги, [genie_name].","base","base")
                ">Ты получаешь [payment] галлеонов."
                m "Молодец, [hermione_name], 20 очков Гриффиндору."
                call her_main("Спасибо [genie_name].","base","happyCl")
                $ gryffindor+= 20
                $ gold += payment
            elif day_random >= 3 and day_random <= 5:
                m "Привет, [hermione_name], как прошел твой день?"
                call her_main("Утомительно. Это приветствие действительно довольно утомительное.","open","worried")
                m "Произошло что-нибудь интересное?"
                call her_main("Если не считать, что я почти потеряла пом-пом.","normal","base")
                m "Они хорошо заплатили тебе?"
                call her_main("Конечно, вот, пожалуйста [genie_name]","open","base")
                ">Ты получаешь [payment] галлеонов."
                m "Молодец [hermione_name], 20 очков для Гриффиндору."
                call her_main("Спасибо [genie_name].","base","happyCl")
                $ gryffindor+= 20
                $ gold += payment
            elif day_random >= 6 and day_random <= 8:
                m "С возвращением [hermione_name]."
                call her_main("Здравствуйте [genie_name].","open","base")
                m "Как ты сегодня?"
                call her_main("Очень хорошо, все мальчики сказали, что я помогаю поддерживать их дух.","open","base")
                m "{size=-5}Я уверен, что это не единственное, что ты поддерживала...{/size}"
                call her_main("В каком смысле [genie_name]?","open","suspicious")
                m "Я говорю, что уверен, что ты хорошо их развлекала."
                call her_main("Я думаю, да.","open","worriedL")
                m "Они хорошо тебе заплатили за повышение их \"духа\"?"
                call her_main("Конечно.","open","closed")
                ">Ты получаешь [payment] галлеонов."
                m "Хорошая работа [hermione_name], 20 очков для Гриффиндору."
                call her_main("Спасибо [genie_name].","base","happyCl")
                $ gryffindor+= 20
                $ gold += payment
            elif day_random >=9 and lock_public_favors == True or whoring <= 15:
                m "Ты выглядишь очень бодрой сегодня."
                call her_main("Конечно, мы же победили!","base","base")
                m "Победили?"
                call her_main("Мы выиграли! Мы обыгрываем Слизерин на тренировочном матче.","smile","happyCl")
                m "Ты выглядишь немного взволнованной перед тренировочным матчем."
                call her_main("Ну это была такая игра. Не говоря уже о том, что мы начали уверенно обыгрывать Слизерин.","smile","baseL")
                m "Ну я рад, что ты наслаждаешься своей работой."
                call her_main("[genie_name]. Учитывая, что большая часть \"работы\", которую я делаю, чтобы помочь факультету приватна, хорошо делать иногда и что-то публичное для него.","open","base")
                m "Не говоря уже о том, что тебе еще платят за это..."
                call her_main("А, точно. Вот, пожалуйста.","soft","baseL")
                ">Ты получаешь [payment] галлеонов."
                m "Молодец [hermione_name], 20 очков Гриффиндору."
                call her_main("Спасибо [genie_name].","base","happyCl")
            else:
                m "С возвращением [hermione_name], как прошел твой день?"
                call her_main("Мы победили! Нам удалось победить Слизерина.","base","base")
                m "Должно быть, это было очень волнующе. Я уверен, что твое приветствие дало мотивацию к победе."
                call her_main("Я думаю, что это так [genie_name]. Все они были очень рады получить свои награды за победу в игре.","base","happyCl")
                menu:
                    "-Награду?-":
                        m "Какую награду ты им пообещала?"
                        call her_main("Ну, я была так увлечена волей к победе над Слизерином, что, возможно, пообещала им, что я сделаю всей команде минеты, если они выиграют.","grin","baseL")
                        m "Ты отсосала каждому члену команды после игры?"
                        call her_main("И мальчику с водой...","smile","glance")
                        m "И как ты это делала? Ты ползала по комнате на коленях?"
                        call her_main("Конечно, нет, они все выстроились и ждали своей очереди.","scream","angryCl")
                        m "Они выстроились? И что потом?"
                        call her_main("Я сосала их члены, пока они не начали кончать, а затем я стала все проглатывать. Наверняка вы и так знаете, как делают минет.","annoyed","worriedL")
                        m "Это не совсем то, что я имел в виду."
                        call her_main("Ну, я рада, что сделала это. Не могу дождаться завтра, чтобы втереть этой Астории в лицо.","smile","baseL")
                        m "Я рад, что ты думаешь, что это того стоило. Они тебе заплатили?"

                        her "Конечно [genie_name], вот, пожалуйста."
                    "-Ладно-":
                        m "Я уверен, что все именно так и было. Они тебе заплатили?"
                        her "Конечно [genie_name], вот, пожалуйста."
                ">Ты получаешь [payment] галлеонов."
                m "Молодец [hermione_name], 20 очков Гриффиндору."
                her "Спасибо [genie_name]."
        "-Отпустить ее-":
            call her_main("Вот ваши деньги [genie_name].","soft","baseL")
            ">Ты получаешь [payment] галлеонов."
            m "Молодец [hermione_name], 20 очков Гриффиндору."
            call her_main("Спасибо [genie_name].","base","happyCl")
            $ gryffindor+= 20
            $ gold += payment

    call her_walk("mid","leave",2)

    $ hermione_sleeping = True
    $ current_job = 0
    jump night_main_menu

label slytherin_cheer_responses:
    $ payment = renpy.random.randint(50, 100)

    call play_sound("door") #Sound of a door opening.
    call her_walk("door","mid",2)
    pause.2

    call h_outfit_OBJ(hg_slythCheer_OBJ)

    show screen bld1
    if day_random >=9 and lock_public_favors == False:
        $ uni_sperm = True
        call her_main("","base","ahegao_raised",xpos="right",ypos="base")
    else:
        call her_main("","base","base",xpos="right",ypos="base")
    pause.5

    menu:
        "-Спросить, как прошел ее день.-":
            if day_random <= 2:
                m "Как прошел твой день [hermione_name]?"
                call her_main("Изнурительно. Эти свиньи из Слизерина настаивали, чтобы я их подбадривала всю их тренировку.","open","angryCl")
                her "Они едва ли играли в игру к концу тренировки. Они просто стояли и смотрели на меня."
                m "Ну и каков был твой распорядок дня?"
                call her_main("В основном, звезды прыгают, когда я приветствую \"Вперед Слизерин!\".","annoyed","frown")
                m "Так ты просто прыгала туда-сюда? Это не кажется очень сложным приветствием."
                call her_main("Это не так, но это то, на чем они настаивали.","annoyed","angryL")
                m "Ну, это определенно звучит так, как будто ты заработала свои очки."
                m "30 очков Гриффиндору."
                call her_main("Спасибо [genie_name], вот ваши деньги.","open","closed")
                ">Ты получаешь [payment] галлеонов."
                $ gold += payment
                $ gryffindor+= 30
            elif day_random >= 3 and day_random <= 5:
                m "Как прошел твой день [hermione_name]?"
                call her_main("Без происшествий. Я закончила всю свою рутину, а затем вернулась в свою комнату.","open","suspicious")
                m "Ты ни с кем не разговаривала?"
                call her_main("Я стараюсь избегать Слизеринцев как можно лучше.","annoyed","angryL")
                m "Неужели они так невыносимы."
                call her_main("Да.","open","angryCl")
                m "Ну, ты заработала свои очки."
                m "30 очков Гриффиндору."
                call her_main("Спасибо [genie_name], вот ваши деньги.","open","closed")
                ">Ты получаешь [payment] галлеонов."
                $ gold += payment
                $ gryffindor+= 30
            elif day_random >= 6 and day_random <= 8:
                m "Привет [hermione_name]."
                call her_main("Привет [genie_name].","normal","base")
                m "Как ты сегодня?"
                call her_main("Очень хорошо. На самом деле, я думаю, что у меня все слишком хорошо.","annoyed","worriedL")
                m "Как так?"
                call her_main("Я думаю, что мои аплодисменты оказывают слишком позитивный эффект.","open","worried")
                call her_main("Я не уверена, что хочу, чтобы команда Слизерина выбилась в лидеры, тем более при моем участии.","open","worriedL")
                m "Просто думай об этом, как помощь своему факультету, другим способом."
                call her_main("Я полагаю, вы правы [genie_name].","open","base")
                m "Конечно, они заплатили тебе?"
                call her_main("Да [genie_name].","base","base")
                ">Ты получаешь [payment] галлеонов."
                m "Молодец [hermione_name], 20 очков Гриффиндору."
                call her_main("Спасибо [genie_name].","base","happyCl")
                $ gryffindor+= 20
                $ gold += payment
            elif day_random >=9 and lock_public_favors == True:
                call her_main("[genie_name], что-то нужно сделать с этими мальчиками из Слизерина.","open","angryCl")
                call her_main("Это плохо, что я должна подбадривать их, но они начинают слегка щупать меня.","annoyed","angryL")
                m "Щупать?"
                call her_main("Да, они щупают меня. Это очень неуместно, и это прерывает мой процесс.","scream","angryCl")
                m "Ты продолжаешь танцевать, пока они щупают тебя?"
                call her_main("Конечно, я всегда заканчиваю любое взятое дело. Я не потерплю неудачу из-за нескольких мальчишек.","open","angryCl")
                m "И что ты хочешь, чтобы я сделал?"
                call her_main("Поговорите с профессором Снейпом, скажите ему наказать их. Они будут прислушиваться к нему.","angry","angry")
                m "Очень хорошо, я поговорю с ним. Я не уверен, что это даст эффект."
                call her_main("Это лучше, иначе я не буду вкладывать все свои усилия в процесс.","normal","frown")
                m "{size=-5}Я уверен, что он покажет им.{/size}"
                call her_main("Вы о чем [genie_name]?","open","suspicious")
                m "Ни о чем [hermione_name], я сказал, что поговорю с профессором Снейпом сегодня вечером."
                call her_main("Спасибо [genie_name], вот ваши деньги.","annoyed","angryL")
                ">Ты получаешь [payment] галлеонов."
                $ gold += payment
                m "Молодец [hermione_name], 30 очков Гриффиндору."
                call her_main("Спасибо [genie_name].","open","closed")
                $ gryffindor+= 30
            else:#Comes back with cum on her
                m "Что, черт возьми, с тобой случилось?"
                call her_main("Я сделала свою работу [genie_name].","angry","down_raised")
                m "О чем ты вообще говоришь? Ты должна была быть чирлидершей."
                call her_main("Я... [genie_name]. Сегодня я просто выступала с другим видом приветствия.","soft","ahegao")
                m "И это приветствие включало дрочку всей команды Слизерина?"
                call her_main("Ну, все началось не так. Сначала я просто танцевала с ними в раздевалке.","angry","down_raised")
                her "И одно привело к другому..."
                m "Хорошо, я не хочу этого слышать. Сколько тебе заплатили за эти \"аплодисменты\"?"
                call her_main("Заплатили мне?","silly","dead")
                m "Тебе должны хорошо заплатить за это [hermione_name]."
                call her_main("О... Должно быть я, забыла. Мне жаль, [genie_name]","base","baseL",cheeks="blush")
                m "Ладно, но ты не получишь никаких очков."
                call her_main("Понятно, [genie_name]. Это все?","base","base")
                m "Да, теперь ты можешь идти."
                call her_main("Спасибо [genie_name].","base","glance")
        "-Отпустить ее-":
            call her_main("Вот ваши деньги.","open","base")
            ">Ты получаешь [payment] галлеонов."
            m "Молодец [hermione_name], 30 очков Гриффиндору."
            call her_main("Спасибо [genie_name].","base","glance")
            $ gryffindor+= 30
            $ gold += payment

    call her_walk("mid","leave",2)

    $ hermione_sleeping = True
    $ current_job = 0
    $ uni_sperm = False
    jump night_main_menu


label job_1:
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    $ hermione_takes_classes = True
    if whoring <= 6:
        her "*Хмпф!*..."
    elif whoring >=7 and whoring <= 15:
        her "Да [genie_name]..."
    else:
        her "Как пожелаете [genie_name]."

    call her_walk("mid","leave",2)

    $ current_job = 1
    jump day_main_menu

label job_2:
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    $ hermione_takes_classes = True
    if whoring <= 6:
        her "*Хмпф!*..."
    elif whoring >=7 and whoring <= 15:
        her "Да [genie_name]..."
    else:
        her "Как пожелаете [genie_name]."

    call her_walk("mid","leave",2)

    $ current_job = 2
    jump day_main_menu

label job_3:
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    $ hermione_takes_classes = True
    if whoring <= 6:
        her "*Хмпф!*..."
    elif whoring >=7 and whoring <= 15:
        her "Да [genie_name]..."
    else:
        her "Как пожелаете [genie_name]."

    call her_walk("mid","leave",2)

    $ current_job = 3
    jump day_main_menu

label job_4:
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    $ hermione_takes_classes = True
    if whoring <= 6:
        her "*Хмпф!*..."
    elif whoring >=7 and whoring <= 15:
        her "Да [genie_name]..."
    else:
        her "Как пожелаете [genie_name]."

    call her_walk("mid","leave",2)

    $ current_job = 4
    jump day_main_menu























