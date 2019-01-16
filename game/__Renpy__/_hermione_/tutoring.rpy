label l_tutoring_check:
    if v_tutoring == 0:
        jump l_tutoring
    elif v_tutoring == 1 and whoring >= 1:
        jump l_tutoring
    elif v_tutoring == 2 and whoring >= 2:
        jump l_tutoring
    elif v_tutoring == 3 and whoring >= 3:
        jump l_tutoring
    elif v_tutoring == 4 and whoring >= 5:
        jump l_tutoring
    elif v_tutoring == 5 and whoring >= 8:
        jump l_tutoring
    elif v_tutoring == 6 and whoring >= 11:
        jump l_tutoring
    elif v_tutoring == 7 and whoring >= 14:
        if gift_item_inv[6] >= 1:# Adult magazines
            jump l_tutoring
        else:
            m "Мне нужно купить взрослые журналы для этого урока."
    elif v_tutoring == 8 and whoring >= 17:
        if gift_item_inv[7] >= 1:# Porn magazines
            jump l_tutoring
        else:
            m "Мне нужно купить порно журналы для этого урока."
    elif v_tutoring == 9 and whoring >= 20:
        if gift_item_inv[11] >= 1:# Vibrator
            jump l_tutoring
        else:
            m "Мне нужно купить вибратор для этого урока."
    elif v_tutoring == 10 and whoring >= 23:
        if gift_item_inv[14] >= 1:# Anal plugs
            jump l_tutoring
        else:
            m "Мне нужно купить анальную пробку для этого урока."
    elif v_tutoring == 11 and whoring >= 23:
        jump l_tutoring
    elif v_tutoring == 12 and whoring >= 23:
        jump l_tutoring
    elif v_tutoring == 13 and whoring >= 23:
        jump l_tutoring
    else:
        m "Сейчас не самое подходящее время. Позже..."

    jump day_time_requests

label l_tutoring:
    $ d_flag_01 = False

    if v_tutoring == 0:   # Whoring lvl 0

        call her_main("Конечно, сэр.","open","base")
        her "Тогда я пойду за своими книгами."

        hide screen hermione_main
        play sound sd_door
        call blkfade

        play sound sd_door
        pause.3

        call h_action("hold_book")
        call her_main("","base","base",xpos="mid",ypos="base")

        call hide_blkfade

        call ctc

        call her_main("Еще раз спасибо, что делаете это для меня, сэр...","open","base",xpos="base",ypos="base")
        m "..........."
        call her_main("Сэр?","soft","baseL")
        m "Пора поговорить о твоем будущем, дитя."
        stop music fadeout 1.0
        call her_main("Я больше не ребенок, профессор!","normal","frown")
        m "В каком-то смысле ты права, но..."
        her "..........."
        m "Я могу научить тебя, но ты должна понимать некоторые вещи о магии."
        m "При правильном обучении, ты сможешь научиться увеличивать свои магические способности."
        play music ms_manatees fadein 1 fadeout 1
        call her_main("Да?","soft","baseL")
        m "Некоторые эмоции, такие как любовь и ненависть, удовольствие и боль..."
        g9 "{size=-2}(Если она на это купится, то я настоящий гений!){/size}"
        call her_main("Я изучала магию много лет и никогда не слышала о подобном.","normal","base")
        g4 "{size=-2}(Черт.){/size}"
        m "И именно поэтому ты все еще ребенок. Тебе еще многое предстоит узнать о магии."
        call her_main("Пожалуйста профессор, прекратите, называть меня ребенком. Никто не считает меня ребенком.","open","base")
        m "Да, технически..."
        call her_main("Технически?!","open","base")
        g4 "Ладно, хватит об этом. Ты пришла ко мне, чтобы попросить о помощи, и если она начинается вот так..."
        call her_main("Да, я полагаю, что вы правы...","angry","angry")
        call her_main("Хорошо, я готова усердно с вам заниматься!","base","base")
        g9 "{size=-2}(ДА!){/size}"
        call her_main("Что это было?","open","annoyed",cheeks="blush")
        m "Да, я рад, что ты начинаешь понимать, дитя."
        her "..........."
        m "Хорошо, я хочу, чтобы ты подумала о том, что я сказал. В следующий раз мы начнем наши занятия."
        call her_main("А мы можем начать прямо сейчас?","open","base")
        m "Мисс Грейнджер, ты не единственная студентка, о которой я должен заботиться."
        call her_main("Вы обучаете кого-то еще?","open","base")
        m "{size=-2}(Хотя...){/size}"
        m "Я должен заботиться обо всех студентах этой школы."
        m "Но да, есть и другая девочка, которая нуждается..."
        call her_main("Девушка из Слизерина?!","scream","wide")
        g9 "Это не твое дело, мисс Грейнджер."
        call her_main("Да, профессор. Простите, но из-за последних событий я немного на взводе.","angry","angry")
        m "Извинения приняты, а теперь спокойной ночи!"
        call her_main("Спокойной ночи, профессор, и еще раз спасибо, что уделили мне свое драгоценное время.","base","base")
        hide screen hermione_main

        call nar("Ты прогоняешь Гермиону.")

        call her_walk("mid","door",3)

        call her_head("{size=-4}(Я рада, что профессор согласился обучать меня!){/size}","base","worriedCl",cheeks="blush",xpos="base",ypos="base")
        call her_head("{size=-4}(Но удовольствие и боль? Я не понимаю, к чему он клонит...){/size}","annoyed","baseL")
        call her_chibi("leave")

        $ v_tutoring = 1
        $ aftercum = False
        jump day_start

    if v_tutoring == 1:   # Whoring lvl 1

        hide screen hermione_main
        call h_action("hold_book")

        call her_main("","base","base",trans="fade")
        m "Мисс Грейнджер, время для твоего первого урока."
        call her_main("Да, профессор.","soft","baseL")
        m "Ты снова принесла свои книги, не думаю, что они нам понадобятся."
        call her_main("Очень жаль, я люблю книги.","normal","base")
        hide screen hermione_main
        with d3

        call h_action("none")

        g9 "{size=-2}(А скоро ты будешь любить член!){/size}"
        $ renpy.play('sounds/punch01.mp3') #Hermione lays books onto the floor.

        call her_main("А?","soft","baseL")
        m "Ничего, я просто думал о нашем следующем уроке."
        call her_main("{size=-2}(Маразматик...){/size}","angry","angry")
        m "............."
        m "В любом случае, ты подумала о том, что мы обсуждали?"
        call her_main("Не совсем, я не совсем понимаю, что вы имеете в виду говоря о \"эмоциях\".","normal","base")
        g9 "{size=-2}(Ты скоро узнаешь, девочка.){/size}"
        m "Например, каковы были твои эмоции, когда ты услышала слухи о девочках из Слизерина?"
        call her_main("Пожалуйста, не надо, сэр! Это действительно заставляет меня сходить с ума!","scream","wide")
        m "И что это за чувство?"
        call her_main("...{w=0.5}сильные эмоции, я полагаю...","normal","base")
        m "Да, и разве у тебя нет эмоций, которые ты предпочитаешь другим?"
        call her_main("Когда у меня самая лучшая оценка на тесте.","smile","happyCl")
        m "{size=-2}(Эта девочка - ботаноманьяк...){/size}"
        m "Разве у тебя нет других увлечений, вещей, которые ты любишь делать?"
        call her_main("Да! Изучение и чтение книг.","smile","happyCl")
        g4 "{size=-2}(Клянусь всеми древними богами...){/size}"
        m "Все идет в неправильном направлении..."
        call her_main("А в каком направлении, сэр?","normal","base")
        g9 "{size=-2}(Тебе надо оказаться на моем члене!){/size}"
        m "Взросление, мисс Грейнджер, зрелость..."
        call her_main("Я, безусловно, самая зрелая из моих сверстников, профессор. Что еще вы спросите?","open","closed")
        m "......{w=0.5}Мисс Грейнджер, разве мы это еще не обсуждали? Тебе нужно принять, что тебе еще многому нужно научиться."
        m "Я устал от всего этого, и мне нужно работать. Спокойной ночи, дитя."
        call her_main("Может быть, репетировать с одной из этих грязных девочек из Слизерина?","open","annoyed",cheeks="blush")
        m "Может быть, это правильное направление, подумай о том, что все эти девушки делают с профессорами."
        call her_main("Но...{w=0.5} Это так неправильно...{w=0.8} Я не знаю, хочу ли я об этом думать.","open","base")
        m "Если ты хочешь развиваться и восстановить гордость Гриффиндора, ты должна!"
        call her_main("Да, вы правы! Это моя миссия! Я сделаю все возможное, профессор.","grin","angry",cheeks="blush")
        g9 "{size=-2}(Она такая наивная, это очаровательно.){/size}"
        m "Хорошо, пора ложиться спать, дитя."
        call her_main("{size=-2}(Вот еще... Как будто я ложусь спать в это время, мне нужно больше заниматься.){/size}","normal","frown")
        hide screen hermione_main
        call nar("Ты прогоняешь Гермиону.")

        call her_walk("mid","door",2)

        call her_head("{size=-4}(Грязные шлюхи...){/size}","angry","angryCl",cheeks="blush")
        call her_head("{size=-4}(О, я не должна так говорить...{w=0.5} но от этого так хорошо!){/size}","base","worriedCl",cheeks="blush")
        call her_chibi("leave")

        $ v_tutoring = 2
        $ aftercum = False
        jump day_start

    elif v_tutoring == 2:   # Whoring lvl 2
        m "Хорошо, на этот раз ты не принесла свои книги."
        call her_main("Не то чтобы я с этим согласна. Все знания, которые мне нужны - в этих книгах.","annoyed","angryL")
        m "Книги не могут научить тебя всему, некоторые знания приходят только с практикой и опытом!"
        call her_main("Возможно... Я имею в виду, вы не случайно выбраны главой Хогвартса.","annoyed","suspicious")
        m "Иногда ты, кажется, забываешь об этом, мисс Грейнджер."
        call her_main("Это прозвучало так, будто это только что сказал профессор Снейп...","open","suspicious")
        call her_main(".........","annoyed","suspicious")
        call her_main("Извините, он думает, что всегда прав, и это меня раздражает.","smile","happyCl")
        m "В отличие от тебя, мисс Грейнджер..."
        call her_main("Полагаю, в этом может быть смысл...","annoyed","angryL",cheeks="blush")
        m "С этого момента, я надеюсь, все ясно."
        call her_main("Да, профессор Дамблдор.","disgust","down_raised",cheeks="blush")
        m "Итак, задумывалась ли ты об эмоциях и их полезности в практике магии?"
        call her_main("Да, сначала я пыталась наложить заклятие, думая о поведении тех девушек из Слизерина.","open","closed")
        call her_main("Это меня так разозлило и смутило, что я потеряла концентрацию внимания и с треском провалилась.","annoyed","base")
        call her_main("Я не думаю, что это поможет.","annoyed","suspicious")
        m "Это твоя проблема, мисс Грейнджер, ты думаешь, что уже знаешь ответ и не следуешь моим инструкциям."
        m "Вот мне к примеру плевать на поведение этих девушек."
        call her_main("Что? Профессор! Вас это не волнует?!","scream","wide_stare")
        g9 "{size=-2}(Мне не все равно, просто не так, как ты думаешь.){/size}"
        m "Для этого упражнения, мисс Грейнджер. Не будь как обычно - мисс всезнайкой."
        call her_main(".........","annoyed","ahegao")
        call her_main("Сожалею об этом, {w=0.5}снова.","open","suspicious")
        m "Мне нужно, чтобы ты сосредоточилась на том, что эти девушки делают с профессорами, а не на их поведении в целом."
        call her_main("Но...","open","base",cheeks="blush")
        m "В прошлый раз ты говорила о своем священном долге и на первом же препятствии колеблешься."
        call her_main("{size=-2}(\"Священный\"? Не преувеличивайте, старец){/size}","annoyed","down")
        call her_main("{size=-2}(А может нет! Возможно, позже меня запомнят как спасителя Гриффиндорского факультета!){/size}","open","worriedCl",cheeks="blush")
        call her_main("Да, вы совершенно правы! {b}Это{/b} мой священный долг!","smile","baseL")
        g9 "{size=-2}(Это срабатывает каждый раз, это слишком легко... Она выглядит настолько горделивой.){/size}"
        call her_main("Я сделаю все, что в моих силах, профессор!","open","base",cheeks="blush")
        g9 "Я тоже в предвкушении... я уверен, что ты это сделаешь."
        call her_main("Я рада, что вы так доверяете мне.","grin","worriedCl")
        m "И я рад, что ты начинаешь в это верить. Я думаю, у тебя есть потенциал освоить эту ветку магии."
        call her_main("Вы выглядите уставшим, профессор.","open","suspicious")
        g11 "{size=-2}(Устал ждать, чтобы перепахать твою попку.){/size}"
        call her_main("Да, профессор?","annoyed","base")
        g9 "Да, можем!"
        m "В смысле, я уверен, что скоро утомлю тебя своими разговорами, мисс Грейнджер. Как насчет поспать?"
        call her_main("Спать? Сначала я должна заняться учебой.","open","closed")
        m "Я не думал об этом, но ты права, пора ложиться спать!"
        m "Просто не забудь подумать о том, что ты узнала сегодня."
        hide screen hermione_main
        call nar("Ты прогоняешь Гермиону.")

        call her_walk("mid","door",2)

        call her_head("{size=-4}(Хм, интересно, о {b}чем{/b} надо мне подумать.){/size}","base","down_raised",cheeks="blush")
        call her_head("{size=-4}(Наверное, все проблемы, вызванны этими шлюхами.){/size}","base","glance",cheeks="blush")
        call her_head("{size=-4}(Ну, я никогда не буду такой, как они, так что мне не нужно об этом беспокоиться.){/size}","silly","glance",cheeks="blush")
        call her_chibi("leave")

        $ v_tutoring = 3
        $ aftercum = False
        jump day_start

    elif v_tutoring == 3:   # Whoring lvl 3
        call her_main("Сэр, я хочу извиниться за то, что сомневалась в вас.","open","base")
        m "Да?"
        call her_main("Ваш \"нетипичный\" метод работает!","angry","worriedCl",emote="05")
        m "{size=-2}(Невозможно!){/size}"
        m "Он работает? Я имею в виду, да, естественно, он работает!"
        m "Я рад, что тебе удалось. Теперь расскажи мне больше."
        call her_main("Мне удалось снять тяжелый груз, думая о поведении двух девушек, которых я видела ранее в библиотеке.","open","closed")
        call her_main("Обычно мне удается снимать только небольшой стресс. Я не знаю, я чувствовала тепло внутри, думая об этом.","mad","angry",cheeks="blush")
        her "Это было странно, но..... {w=0.5}хорошо в то же время."
        m "{size=-2}(Она так неосведомлена о жизни! Невероятно.){/size}"
        m "Ты никогда раньше не испытывала таких ощущений?"
        call her_main("Обычно я злюсь и спешу прекратить такое поведение.","clench","worried",cheeks="blush",tears="soft")
        call her_main("Но вчера, я не знаю, я просто смотрела, не прерываясь на них.","open","worriedCl",cheeks="blush")
        call her_main("И когда я представила, как они могут ублажать профессоров, как вы мне сказали, это сработало.","open","base",cheeks="blush")
        call her_main("Я чувствую себя подобно этим шлюхам, мне так стыдно.","angry","angry",cheeks="blush")
        m "Но тебе это удалось."
        g9 "{size=-2}(К моему удивлению...){/size}"
        call her_main("Да! С помощью этого метода я буду иметь лучшие оценки в своих тестах и выиграю Кубок факультетов для Гриффиндора!","angry","worriedCl",cheeks="blush",emote="05")
        g9 "{size=-2}(В своих грезах.){/size}"
        m "Хорошо, хорошо. Теперь я хочу узнать больше об этих двух девочках."
        call her_main("Это не очень важно, профессор. И я не уверена, что это уместно.","annoyed","angryL",cheeks="blush")
        m "Как ты улучшишь себя, если я не могу тебя направлять?"
        m "И для этого я должен знать больше."
        call her_main("Хорошо, но мне неловко из-за этого.","annoyed","angryL",cheeks="blush")
        g9 "{size=-2}(О, надеюсь, они были голыми!){/size}"
        call her_main("Я пошла в библиотеку, чтобы изучить взаимодействия между растениями...","open","closed")
        g11 "{size=-2}(Да, да, продолжай...){/size}"
        call her_main("... и услышала приглушенные звуки.","base","baseL",cheeks="blush")
        call her_main("Я надеялась поймать учителя, делающего непристойные вещи с одной из этих Слизеринских шлюх.","annoyed","angryL",cheeks="blush")
        call her_main("Я медленно направилась на звуки и обнаружила двух девушек в нише.","open","base",cheeks="blush")
        call her_main("Я оставалась незаметной, чтобы наблюдать за ними.","grin","wink",cheeks="blush")
        g11 "{size=-2}(Ну же!){/size}"
        call her_main("Да, профессор?","base","ahegao_raised",cheeks="blush")
        m "Да не, пожалуйста, продолжай."
        call her_main("Они страстно целовались.","open","worriedCl",cheeks="blush")
        g9 "И? И?"
        call her_main("И через мгновение они начали...","open","closed")
        call her_main("Они начали...","open","worriedCl",cheeks="blush")
        call her_main("Они начали трогать свои груди!","scream","wide",cheeks="blush")
        m "Надеюсь, они были голыми?"
        call her_main("Что?","open","squint",cheeks="blush")
        her "Нет, к счастью, они были одеты."
        call her_main("Как такое, может происходить в нашей любимой школе!","angry","angry",cheeks="blush")
        m "Но ты продолжила наблюдать, не так ли?"
        call her_main("Только исключительно в образовательных целях.","annoyed","angryL",cheeks="blush")
        g9 "{size=-2}(\"Образовательных целях\"... Ха-ха, я никогда не слышал худшего оправдания!){/size}"
        m "И все это время ты не почувствовала определенного желания?"
        call her_main("К моему великому стыду, конечно почувствовала. Как я уже говорила, я чувствовала тепло внутри.","annoyed","angryL",cheeks="blush")
        call her_main("Примерно, такое, когда мне нужно пописать... но несколько другое. Лучше.","disgust","down_raised",cheeks="blush")
        m "Это хорошее ощущение... в следующий раз, когда ты испытаешь его, пройди путь до конца."
        call her_main("Но...","open","base",cheeks="blush")
        m "Это единственный способ стать лучше, мисс Грейнджер."
        m "Если ты подавишь его, оно не станет работать."
        call her_main("Хорошо...{w=0.3} Я постараюсь изо всех сил.","annoyed","angryL",cheeks="blush")
        her "Но, честно говоря, сэр, я думала, что вы накажите этих двух шлюх."
        m "Можешь ли ты представить доказательства их преступления? Нет?"
        m "Даже я не могу наказывать студентов без доказательства каких-либо проступков."
        g11 "{size=-2}(За исключением тебя!){/size}"
        m "В любом случае, ты молодец. Думаю, будет достаточно для этого урока."
        m "Помни, что я тебе сказал, и спокойной ночи!"
        call her_main("Спокойной ночи, профессор.","base","base")
        hide screen hermione_main
        call nar("Ты прогоняешь Гермиону.")

        call her_walk("mid","door",2)

        call her_head("{size=-4}(Что ж, я попытаюсь проследить снова за этими двумя девушками.){/size}","disgust","down_raised",cheeks="blush")
        call her_head("{size=-4}(Как настоящий сыщик!){/size}","base","glance",cheeks="blush")
        call her_head("{size=-4}(Да, верно. Гермиона - сыщик!){/size}","base","worriedCl",cheeks="blush")
        call her_chibi("leave")

        $ v_tutoring = 4
        $ aftercum = False
        jump day_start

    elif v_tutoring == 4:   # Whoring lvl 5
        m "Так, какие успехи с твоим \"исследованием\"?"
        call her_main("Да! Когда вы услышите результаты моей охоты, вы будете гордиться мной!","base","happyCl")
        m "{size=-2}(\"Охоты\"?){/size}"
        m "Твоей \"охоты\", мисс Грейнджер?"
        call her_main("Да, профессор!","smile","happyCl")
        call her_main("Как охотник в диких джунглях, я отследила этих двух грязных животных.","base","concerned",cheeks="blush",tears="soft")
        call her_main("С успехом, сэр!","smile","happyCl",cheeks="blush",emote="06")
        call her_main("В Хогвартсе так много темных и незаметных углов...","annoyed","base")
        call her_main("Поверьте, это было нелегко, профессор.","base","concerned",cheeks="blush",tears="soft")
        m "Я уверен, что ты старалась изо всех сил."
        m "Но сейчас я жду твоего отчета."
        call her_main("Да, но перед этим хочу уточнить, что мой доклад носит чисто научный характер.","base","ahegao_raised",cheeks="blush")
        m "{size=-2}(Конечно...){/size}"
        call her_main("Так, я отследила этих двух шлюшек до чердака.","open","closed")
        call her_main("Который, кстати кажется является, местом встречи для подобных девушек...","annoyed","suspicious")
        m "И каково твое мнение о них?"
        call her_main("По крайней мере, они не спят с профессорами в обмен на очки факультету.","open","suspicious")
        call her_main("","annoyed","suspicious")
        m "И это все? Нет и \"такое поведение должно быть строго наказано\"?"
        m "Тебя привлекают такие девушки, мисс Грейнджер?"
        call her_main("Что? Лесбиянки? Я не... и... нет, конечно...","open","base",cheeks="blush")
        m "Хорошо, Хорошо, вернемся к твоему отчету, продолжай."
        call her_main("{size=-2}(Я вовсе не лесбиянка...{w=0.3} Я так думаю...){/size}","disgust","down_raised",cheeks="blush")
        call her_main("{size=-2}(Гермиона, девочка, возьми себя в руки! Ты же не шлюха!){/size}","mad","wide",cheeks="blush")
        call her_main("Нет, это не так!","annoyed","closed",cheeks="blush")
        m "Прошу прощения?"
        call her_main("Э... Да, мой отчет. Мой {b}научный{/b} доклад.","open","base",cheeks="blush")
        m "{size=-2}(Да, я услышу его...){/size}"
        call her_main("Так вот, как и раньше, они начали страстно целоваться.","open","worriedCl",cheeks="blush")
        call her_main("С языком и все такое!","open","baseL",cheeks="blush")
        menu:
            "-Начать дрочить, пока она говорит-":
                $ d_flag_01 = True
                hide screen hermione_main
                hide screen blktone
                call nar(">Ты залезаешь под стол и хватаешь свой член...")
                hide screen genie
                show screen genie_jerking_off
                with d3
                call ctc
            "Ничего не делать.":
                pass
        call her_main("","open","base",cheeks="blush")
        g9 "И? И?"
        call her_main("Они задрали блузки и стали ласкать друг другу груди.","open","worriedCl",cheeks="blush")
        call her_main("{size=-2}(У них красивые и соблазнительные груди...){/size}","open","ahegao_raised",cheeks="blush")
        call her_main("Позже эти противные девушки подняли юбки и начали трогать друг друга \"там\", во время поцелуя.","silly","ahegao_raised",cheeks="blush")
        $ b_her_tears = True
        call her_main("{size=-2}(Не могу поверить, что я это сказала!){/size}","base","ahegao_raised",cheeks="blush",tears="sweat")
        call her_main("Они были очень возбуждены, и я видела, как их трусики намокают.","open","ahegao_raised",cheeks="blush")
        call her_main("Отвратительно.","annoyed","ahegao_raised",cheeks="blush")
        if d_flag_01:
            g9 "{size=-2}(Да... да...){/size}"
        $ b_her_tears = False
        call her_main("Одна из девушек сошла с ума и вставила пальцы другой \"туда\" и двигала ими неистово.","silly","worried",cheeks="blush",tears="soft")
        call her_main("Вскоре и я подражала этой девушке.","silly","ahegao_raised",cheeks="blush")
        call her_main("Эти шлюхи кричали так сильно, что я уверена, их крики слышали на другой стороне замка!","open_wide_tongue","ahegao_mad",cheeks="blush")
        if d_flag_01:
            her "{size=-2}(И мне пришлось прикусить губу, иначе они бы и меня услышали...){/size}"
            hide screen hermione_main
            with d3

            call cum_block

            g11 "Да! Вот это вещь!"
            hide screen bld1
            with d1
            show screen genie_jerking_sperm
            call cum_block
            call ctc

            call gen_chibi("cum_on_desk")
            with d3

            call her_main("Профессор!","angry","angry",cheeks="blush")

            m "Тебе тоже это понравилось, так что не притворяйся невинной."

            $ mad = +7
            $ d_flag_01 = False
        else:
            m "Тебе это тоже понравилось."
        call her_main("Возможно...","annoyed","angryL",cheeks="blush")
        m "Во всяком случае, я надеюсь, что это было поучительно."
        call her_main("\"Поучительно\"? Я не совсем понимаю, что вы имеете в виду.","open","suspicious")
        call her_main("Вы же директор, действуйте как таковой!","open","base")
        call her_main("Сделайте все возможное, чтобы остановить эти акты разврата!")
        call her_main("","annoyed","angryL")
        m "Да, конечно."
        m "{size=-2}(Лицемерка...){/size}"
        her "{size=-2}(Старый извращенец...){/size}"
        m "Ты сказала, что те девушки промокли."
        g9 "Разве ты тоже не намокла?"
        call her_main("Когда я ложилась спать, да, я заметила это.","disgust","down_raised",cheeks="blush")
        call her_main("Видимо, плохие жидкости выходят из моего тела, от столкновения с такими актами.","mad","wide",cheeks="blush")
        m "Нет, они совсем не плохие. Это происходит, когда ты взволнована."
        $ b_her_tears = True
        call her_main("Нет! Я могу себя контролировать!","scream","worriedCl",cheeks="blush",tears="soft_blink")
        $ b_her_tears = False
        call her_main("","angry","angry",cheeks="blush")
        m "Никто не может контролировать свои желания."
        m "Подумай об этом хорошенько и наслаждайся вечером, мисс Грейнджер."
        call her_main("Спокойной ночи, профессор.","annoyed","worriedL")
        hide screen hermione_main
        call nar("Ты прогоняешь Гермиону.")

        call her_walk("mid","door",2)

        call her_head("{size=-4}(Мне очень понравилось. Может быть, я тоже становлюсь извращенкой){/size}","base","ahegao_raised",cheeks="blush")
        call her_head("{size=-4}(Я потеряла контроль, это больше не повторится!){/size}","shock","down_raised",cheeks="blush")
        call her_head("{size=-4}(Хорошо, что я не дегенератка, как эти грязные девочки!){/size}","base","glance",cheeks="blush")
        call her_chibi("leave")

        $ v_tutoring = 5
        $ aftercum = False
        jump day_start

    elif v_tutoring == 5:   # Whoring lvl 8
        m "Браво, в прошлый раз ты испытала свою первую \"эмоцию\"."
        call her_main("Да, я помню, но я до сих пор не вижу связи с магией.","open","suspicious")
        m "{size=-2}(Я тоже...){/size}"
        m "Если ты хочешь прогресса, ты должна пойти немного дальше, чем простое наблюдение."
        m "Тебе нужно будет принять участие."
        call her_main("Что? Ни за что не буду участвовать в таком разврате!","scream","closed",cheeks="blush")
        call her_main("Как вы можете такое предлагать!","angry","angry")
        m "О, ты не должна идти так далеко за раз."
        call her_main("Я не уверена, что вообще хочу туда заходить.","open","closed")
        m "Сколько раз я должен напомнить тебе, почему ты делаешь это?"
        call her_main("Да, но...","open","base")
        m "Но что?"
        call her_main("Такая девушка как я не должна опускаться до подобных методов.","annoyed","suspicious")
        m "Такая девушка, как ты, должна использовать все имеющиеся в ее распоряжении средства, чтобы преуспеть."
        her "..........."
        call her_main("Хорошо, но это должно остаться между нами.","annoyed","angryL",cheeks="blush")
        call her_main("Только не рассказывайте это другим профессорам, особенно профессору Снейпу!","annoyed","down")
        m "Оу, у меня нет намерений расска... говоря о тебе и профессоре Снейпе."
        g9 "{size=-2}(Ты моя.){/size}"
        call her_main("Хорошо, что мне теперь делать?","open","closed")
        m "Иди сюда."
        hide screen hermione_main
        hide screen bld1
        with d3

        call her_walk_desk_blkfade

        hide screen genie
        show screen no_groping_01
        call hide_blkfade
        call ctc

        call bld
        m "Ты когда-нибудь трогала себя?"
        call her_main("Профессор!","base","concerned",cheeks="blush",tears="soft",xpos="mid",ypos="base")
        show screen groping_01
        with d7
        call nar(">Ты трогаешь рукой ее ногу.")
        m "Пожалуйста, ответь на вопрос, мисс Грейнджер. Ты когда-нибудь трогала себя?"
        call her_main("Нет, это так... это неправильно!","annoyed","angryL",cheeks="blush")
        m "Но когда ты смотрела на этих девочек, ты чувствовала определенные эмоции."
        call her_main("Да и что?","grin","wink",cheeks="blush")
        m "Ты не чувствовала необходимости потрогать себя?"
        call her_main("Да, но я сопротивлялась.","base","ahegao_raised",cheeks="blush")
        call nar(">Ты начинаешь ласкать ее бедра.")
        call her_main("Профессор...","open","worriedCl",cheeks="blush")
        m "И ты почувствовала эти эмоции, даже не прикоснувшись к себе."
        call her_main("Да...","open","base",cheeks="blush")
        g9 "{size=-2}(Какая шлюха!){/size}"
        if whoring <= 12 or custom_bra >0:
            call nar(">Ты продвигаешься к ее трусикам.")
        else:
            call nar(">Ты продигаешься к ее киске.")
        call her_main("","open","worriedCl",cheeks="blush")
        m "Хорошо."
        hide screen groping_01
        show screen no_groping_01
        with d3
        call nar(">Ты перестаешь ласкать ее.")
        call her_main("Почему..., почему вы остановились?","mad","wide",cheeks="blush")
        m "Потому что мне нужно, чтобы ты все обдумала, прежде чем мы снова встретимся."
        call her_main("Но...","mad","wide",cheeks="blush")
        m "Спокойной ночи, моя дорогая."
        call her_main("Спокойной ночи, профессор.","annoyed","worriedL")

        hide screen hermione_main
        call blkfade

        hide screen no_groping_01
        "Ты прогоняешь Гермиону."
        call her_chibi("stand","desk","base")
        show screen genie
        hide screen bld1
        call hide_blkfade

        call her_walk("desk","door",3)

        call her_head("{size=-4}(Это неправильно...){/size}","disgust","down_raised",cheeks="blush")
        call her_head("{size=-4}(Я не должна его слушать.){/size}","angry","worriedCl",cheeks="blush")
        call her_head("{size=-4}(И все же...){/size}","base","down_raised",cheeks="blush")
        call her_chibi("leave")

        $ v_tutoring = 6
        $ aftercum = False
        jump day_start

    elif v_tutoring == 6:   # Whoring lvl 11
        m "Итак, ты начала практиковать мои учения?"
        call her_main("Я даже не знаю с чего начать.","open","suspicious")
        m "Видишь ли, секрет в том, чтобы стимулировать соответствующие области."
        m "Области, которые являются более чувствительными, чем другие."
        call her_main("Вы имеете в виду мои интимные зоны, сэр?!","annoyed","angryL",cheeks="blush")
        m "Ну, они называются интимными по какой-то причине."
        m "Ты сказала, что никогда не трогал себя, потому что это было неправильно."
        m "Но никогда не будет ошибкой тренировать свое тело, чтобы достичь нового уровня сознания."
        g4 "{size=-2}(Что я должна делать...){/size}"
        m "Ты можешь начать со своей груди, например."
        m "Но ты должна не только ласкать свои соски, но и хватать свои сиськи и сжимать их."
        m "А тем временем, ты можешь думать об этих двух девочках."
        g9 "Или что ты хочешь делать с этими девочками."
        call her_main("Что заставляет вас думать... Нет, я не хочу...","angry","worriedCl",cheeks="blush",emote="05")
        call her_main("Я определенно не хочу {b}ничего{/b} делать с этими проститутками!","scream","worriedCl",cheeks="blush")
        m "Не лги себе. Очевидно, что ты чувствуешь некую форму притяжения к этим двум девочкам."
        call her_main("Я...{w=0.3} Я честно не знаю, что думать.","mad","angry",cheeks="blush")
        her "На данный момент мои чувства настолько запутанны..."
        g9 "{size=-2}(Именно то, на что я надеялся!){/size}"
        call her_main("Я счастлива зарабатывать очки для своего факультета и в то же время, мне так стыдно.","angry","suspicious",cheeks="blush",tears="messy")
        her "И то же самое касается ваших уроков."
        m "Тем не менее, ты не можешь отрицать свой прогресс в практике магии."
        call her_main("...{w=0.2} Да...{w=0.2} возможно, вы правы.","base","concerned",cheeks="blush",tears="soft",tears="sweat")
        m "Ты должна отпустить это, мисс Грейнджер, следуй своим инстинктам!"
        g9 "{size=-2}(Хватай мой член и дрочи его жестко!){/size}"
        $ b_her_tears = False
        call her_main("Я не уверена, что...","open","concerned",cheeks="blush",tears="mascara")
        m "Хватит медлить, время для практики!"
        m "Иди сюда."
        hide screen hermione_main
        hide screen bld1
        with d3

        call her_walk_desk_blkfade

        ">Гермиона идет к твоему столу."
        ">Ты хватаешь ее за сиськи и нежно массируешь."
        pause.5

        hide screen genie
        show screen groping_03
        with d1
        hide screen blkfade
        call her_main("","open","worriedCl",cheeks="blush",xpos="mid",ypos="base")
        call ctc

        call bld
        m "Как я уже сказал, важно научиться правильно стимулировать \"эмоциональные\" зоны тела."
        m "Недостаточно того, что я это делаю тебе, тебе нужно практиковаться, и когда ты одна."
        call her_main("","upset","worriedCl",cheeks="blush")
        m "Например, в своей кровати или в душе."
        call nar(">Ты продолжаешь массировать ее сиськи...")
        call her_main("","open","worriedCl",cheeks="blush")
        call nar(">Ты чувствуешь, как ее соски становятся твердыми.")
        call her_main("Да, но.....{w=0.3} Профессор, это неуместно для девушки с хорошим воспитанием!","open","base",cheeks="blush")
        m "Не позволяй старым предрассудкам тяготить тебя. Ты девушка с большим потенциалом."
        call nar(">Ты нежно тискаешь ее соски через ткань рубашки.")
        call her_main("Ах, спасибо, профессор.","open","ahegao_raised",cheeks="blush")
        m "Девочка с блестящим умом."
        call nar(">Ты увеличиваешь хватку ее за соски.")
        m "Девочка, которая станет женщиной-исключением."
        call her_main("Ахх, да... Я и так исключительная женщина, дурак.","grin","angry",cheeks="blush")
        m "Дурак?"
        call nar(">Ты твердо зажимаешь ее соски.")
        call her_main("Аххх, дааа, не так жестко, дааа...","silly","worried",cheeks="blush",tears="soft")
        call nar(">Ты резко останавливаешься.")

        call blkfade
        pause.5

        call her_head("Не останавливайтесь, идиот!","scream","angry",cheeks="blush",emote="01")

        hide screen hermione_main
        hide screen groping_03
        show screen genie_and_hermione
        hide screen genie_and_hermione
        show screen genie
        show screen hermione_blink
        call hide_blkfade

        call her_head("...........","mad","wide",cheeks="blush")

        call her_chibi("stand","desk","base")
        show screen genie
        hide screen bld1
        call hide_blkfade

        show screen bld1
        call her_head("Простите, профессор.","angry","angry",cheeks="blush")
        m "Урок окончен. Время попрактиковаться самостоятельно."
        m "Спокойной ночи, моя маленькая ведьма."
        call her_main("Спокойной ночи, профессор, и спасибо за этот урок.","base","happyCl")
        call her_main("{size=-2}(Мне очень жаль, что это не продлилось дольше...){/size}","annoyed","suspicious")
        hide screen bld1
        hide screen hermione_main
        with d3

        call her_walk("desk","door",3)

        show screen hermione_stand_f
        call her_head("{size=-4}(\"Моя маленькая ведьма?\"){/size}","annoyed","angryL",cheeks="blush")
        call her_head("{size=-4}(Почему бы и нет, в конце концов...){/size}","base","ahegao_raised",cheeks="blush")
        call her_chibi("leave")

        $ v_tutoring = 7
        $ aftercum = False
        jump day_start

    elif v_tutoring == 7:   # Whoring lvl 14
        m "Итак, мисс Грейнджер, ты практиковала мои учения?"
        call her_main("Да...{w=0.2} немного","annoyed","angryL",cheeks="blush")
        m "И?"
        call her_main("Мне даже удобнее, когда я голая.","smile","happyCl",cheeks="blush",emote="06")
        call her_main("{size=-2}(Нет, мне не следовало этого говорить...){/size}","mad","wide",cheeks="blush")
        m "Иди сюда и раздевайся, мы будем тренироваться."
        call her_main("Полностью?!","mad","angry",cheeks="blush")
        m "Нет, только верха будет достаточно."
        g9 "{size=-2}(На данный момент...){/size}"
        call her_main("Я покажу вам свою грудь, даже не заработав ни одного очка?","open","suspicious")
        m "Ты не можешь иметь и очки, и обучение."
        call her_main("Ладно...","angry","worriedCl",cheeks="blush",emote="05")

        hide screen hermione_main
        call her_chibi("lift_top")

        call h_action("lift_top")

        call her_main("Вот так?","annoyed","angryL",cheeks="blush")

        if custom_bra >=1 and badges and custom_outfit_old <= 0:
            m "Без лифчика, мисс Грейнджер... и иди сюда."
        else:
            m "Да и сейчас подойди сюда."

        call her_main("........","annoyed","closed",cheeks="blush")
        call her_main("","base","closed")
        m "Ну же."

        call her_walk_desk_blkfade

        ">Гермиона медленно подходит к твоему столу."
        ">Она пытается сдержать свои сиськи, чтобы не прыгали..."
        call her_chibi("hide")
        hide screen genie
        show screen genie_and_tits_01
        with d1

        hide screen blkfade
        call her_main("","base","closed",xpos="mid",ypos="base")
        call ctc

        call bld
        m "Теперь давай серьезно, если хочешь."
        g9 "{size=-2}(Даже если ты не хочешь...){/size}"

        hide screen hermione_main
        call blkfade

        ">Ты хватаешь ее сиськи и мягко сжимаешь их."

        show screen chair_left
        hide screen genie_and_tits_01
        show screen groping_naked_tits
        call hide_blkfade
        call ctc

        call her_main("Профессор, что вы делаете?","disgust","down_raised",cheeks="blush")
        g9 "Обучаю тебя, дорогая, обучаю."
        m "Разве ты не чувствуешь себя хорошо?"
        call her_main("Немного...","base","closed")
        m "Твои твердые соски говорят обратное."
        m "Я могу остановиться, если ты хочешь."
        call her_main("Нет!","grin","angry",cheeks="blush")
        call her_main("Пососите их, профессор.","silly","ahegao_raised",cheeks="blush")
        g9 "Как пожелаешь, принцесса."
        call her_main("","silly","ahegao_raised",cheeks="blush")
        call nar(">Ты начинаешь жадно сосать ее соски.")
        $ b_her_tears = True
        call her_main("Да {image=textheart} вот так.","silly","ahegao_raised",cheeks="blush",tears="sweat")
        call nar(">Ты начинаешь покусывать ее соски.")
        call her_main("Ах, неее, нет...","open_tongue","ahegao_raised",cheeks="blush")
        call nar(">Ты кусаешь их еще сильнее.")
        call her_main("Не так сильно, я...","open_wide_tongue","ahegao_mad",cheeks="blush")
        g9 "{size=-2}(Время для грандиозного финала!){/size}"

        if hermione_wear_panties:
            ">Ты быстро просовываешь руку в трусики и начинаешь яростно тереть ее киску."
        else:
            ">Ты быстро ложишь руку к ее киске и начинаешь яростно тереть ее."

        $ b_her_tears = False
        call her_main("Да! {image=textheart}","angry","dead",cheeks="blush",tears="crying")
        her "Я... Я..."
        g9 "Кончила, моя дорогая."

        hide screen hermione_main
        call blkfade
        call ctc

        call h_action("none")

        hide screen chair_left
        hide screen groping_naked_tits
        hide screen genie
        show screen genie_and_hermione
        call hide_blkfade

        call her_main("Урок окончен, профессор?","grin","glance",cheeks="blush",tears="mascara")
        m "Нет, если ты этого не хочешь."
        her "Может, хватит на сегодня."
        call her_main("Ведь у вас много работы.","grin","concerned",cheeks="blush",tears="mascara")
        m "Конечно."
        m "Но перед этим у меня для тебя небольшой подарок."

        call give_reward(">Ты даешь журналы для взрослых Гермионе.","images/store/gifts/7.png")

        m "Надеюсь, это поможет тебе в учебе."
        call her_main("Да, конечно.","grin","closed",cheeks="blush",tears="mascara")
        her "Спасибо и спокойной ночи, профессор."
        m "Спокойной ночи, дорогое дитя."

        hide screen hermione_main
        call blkfade

        hide screen genie_and_hermione
        "Ты прогоняешь Гермиону."
        call her_chibi("stand","desk","base")
        show screen genie
        call hide_blkfade

        call her_walk("desk","door",2.5)

        call her_head("{size=-4}(Я такая шлюшка...){/size}","base","ahegao_raised",cheeks="blush")
        call her_head("{size=-4}(Кончаю на глазах у профессора...){/size}","base","down_raised",cheeks="blush")
        call her_head("{size=-4}(Мне определенно нужно сделать это снова!){/size}","base","glance",cheeks="blush")
        call her_chibi("leave")

        $ v_tutoring = 8
        $ aftercum = False
        jump day_start

    elif v_tutoring == 8:   # Whoring lvl 17
        m "Так, скажи, были ли твои чтения поучительными?"
        call her_main("Я не уверена, что \"чтения\" это правильный термин, Но да. Очень \"стимулирующие\", слишком.","angry","worriedCl",cheeks="blush")
        m "Может быть, пришло время открыть для себя новые области для стимулирования."
        call her_main("Вы имеете в виду мою киску, да?","open","suspicious")
        call her_main("Я не идиотка, профессор.","annoyed","angryL")
        m "Если тебе это не подходит, мы можем остановиться на этом."
        call her_main("А если я попрошу остановиться?","annoyed","suspicious")
        g4 ".........."
        call her_main("Хаха, вы должны были видеть свое лицо!","smile","angry",cheeks="blush")
        call her_main("Со всеми вашими недавними уроками как можно предполагать, что эта область больше не *no man's land* зона.","smile","baseL")
        g4 "Ты с кем то переспала?"
        call her_main("Нет я не это имела ввиду! Я не проститутка, которая предлагает свою киску каждому мальчику в округе.","scream","closed",cheeks="blush")
        m "{size=-2}(Хорошо, твоя киска только моя!){/size}"
        call her_main("","annoyed","ahegao")
        g9 "{size=-2}(Хотя я могу согласиться поделиться ей с другими девочками...){/size}"
        m "Мисс Грейнджер, я рад, что ты ведешь себя достойно."
        call her_main("Ха, кто бы мог подумать!","annoyed","angryL",cheeks="blush")
        m "Да, я рад, что моя любимая студентка не тратит свое драгоценное время на мальчиков."
        her "Конечно...{w=0.3} {size=-4}старый лицемер{/size}."
        m "Хватит об этом! А теперь снимай рубашку и иди сюда."
        call her_main("У нас будет следующий \"урок\"?","open","suspicious")

        call her_walk_desk_blkfade

        $ hermione_wear_top = False
        call h_update_body

        if hermione_wear_bra:
            call her_head("...",xpos="base",ypos="high")
            m "И твой лифчик..."

            $ hermione_wear_bra = False
            call h_update_body

        call her_head("........","annoyed","closed",cheeks="blush",xpos="base",ypos="high")

        call her_chibi("hide")
        hide screen genie
        show screen no_groping_06
        call hide_blkfade
        call ctc

        call bld
        call her_main("И снова вы посмотрите бесплатно на мои сиськи, наслаждайтесь!","grin","angry",cheeks="blush",xpos="mid",ypos="base")
        m "Определенно намереваюсь."
        g9 "Теперь снимай свою юбку."
        pause.8

        call set_hermione_action("lift_skirt")
        pause.5

        $ hermione_wear_bottom = False
        call set_hermione_action("none","skip_update")
        pause.5

        call her_main("","base","baseL",cheeks="blush")
        call ctc

        if hermione_wear_panties:
            call her_main("Вы любите мою киску, не так ли?","base","ahegao_raised",cheeks="blush")
            g9 "О да, мне нравится твой запах, особенно когда ты мокрая."
            call her_main("Профессор...","angry","worriedCl",cheeks="blush",emote="05")
            hide screen no_groping_01
            show screen groping_06
            with d3
            call nar(">Ты ласкаешь ее клитор.")
            call her_main("Профессор!","mad","wide",cheeks="blush")
        else:
            call her_main("Вы любите мои трусики, не так ли?","base","ahegao_raised",cheeks="blush")
            g9 "О да, мне нравится их запах, особенно когда ты мокрая."
            call her_main("Профессор...","angry","worriedCl",cheeks="blush",emote="05")
            hide screen no_groping_01
            show screen groping_06
            with d3
            call nar(">Ты ласкаешь ее клитор через ткань.")
            call her_main("Профессор!","mad","wide",cheeks="blush")
            m "А теперь снимай их."

            $ hermione_wear_panties = False
            call set_hermione_action("pinch")

            call nar(">Она медленно спускает трусики.")

            call set_hermione_action("none","skip_update")

            hide screen groping_06
            show screen no_groping_06
            $ b_her_panties_off = True
            call her_main("","base","closed")
            call ctc

        m "Что, здорово? Видишь ли, у меня всего две руки."
        m "Одна может ласкать твой клитор, а другая играть с твоей киской."
        call nar(">Ты переходишь от слов к делу и с легкостью проникаешь в ее и без того мокрую киску.")

        hide screen no_groping_06
        show screen groping_06
        with d3

        call her_main("Да, вы, наверное, правы.","grin","angry",cheeks="blush")
        m "Наверное?!"
        call nar(">В то время как ты двигаешь пальцем в ее киске, ты начинаешь массировать ее клитор большим пальцем.")
        call her_main("Хаа {image=textheart}, я всего лишь ваша скромная ученица, я бы не узнала таких неприличных вещей.","silly","ahegao_raised",cheeks="blush")
        m "Одного пальца редко бывает достаточно даже с такой тугой киской, как у тебя."
        call nar(">Ты вставляешь второй палец в ее тугую и теплую киску...")
        call her_main("Дааа {image=textheart}, я постараюсь запомнить ваши тренировки.","silly","ahegao_raised",cheeks="blush")
        call nar(">Ты увеличиваешь темп и чувствуешь, как ее киска растягивается пальцами.")
        m "Может быть, третий палец?"
        $ b_her_tears = True
        call her_main("Не будьте таким быстрым.","grin","angry",cheeks="blush",tears="soft")
        call nar(">Все ее тело начинает дрожать, когда ты увеличиваешь скорость.")

        hide screen groping_06
        show screen groping_06b
        with d3

        call her_main("Неее {image=textheart}{w=0.2} не так быстро я скоро...","open_tongue","ahegao_raised",cheeks="blush")
        call nar(">Ты увеличиваешь свой темп еще быстрее.")
        call her_main("Я сделаю это...","open_wide_tongue","ahegao_mad",cheeks="blush")
        g9 "Время для серьезных решений."
        call nar(">Ты с силой вонзаешь свой влажный палец в ее дырку.")
        $ b_her_tears = False
        call her_main("Хаааа {image=textheart} даааа {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush")
        g9 "Счастливая девочка."

        call blkfade

        hide screen hermione_main
        hide screen groping_06b
        hide screen genie
        show screen no_groping_01
        call hide_blkfade

        call her_main("Я уверена, что этот урок будет очень полезным сегодня.","grin","glance",cheeks="blush",tears="mascara")
        call her_main("И другие ночи {image=textheart}.","silly","worried",cheeks="blush",tears="soft")
        m "Всегда рад помочь моей маленькой ведьмочке в учебе."
        call her_main("\"Учебе\", да, это верно.","grin","glance",cheeks="blush",tears="mascara")
        m "И чтобы помочь твоей учебе, у меня есть еще больше научных материалов."

        call give_reward(">Ты отдаешь порно журнал Гермионе.","images/store/gifts/8.png")

        call her_main("Я обещаю изучать их каждую ночь, пока не запомню эти уроки!","grin","closed",cheeks="blush",tears="mascara")
        call her_main("Спасибо и спокойной ночи, профессор.","grin","glance",cheeks="blush",tears="mascara")
        m "Спокойной ночи, моя любимая маленькая ведьма."

        hide screen hermione_main
        call blkfade

        hide screen no_groping_01
        "Ты прогоняешь Гермиону."

        call h_action("none") #Resets clothes.

        call her_chibi("stand","desk","base")
        show screen genie
        call hide_blkfade

        call her_walk("desk","door",2.5)

        call her_head("{size=-4}(Любимая...){/size}","base","ahegao_raised",cheeks="blush")
        call her_head("{size=-4}(Есть еще и другие?){/size}","mad","wide",cheeks="blush")
        call her_head("{size=-4}(Я сделаю все возможное, чтобы остаться его фавориткой!){/size}","base","worriedCl",cheeks="blush")
        call her_chibi("leave")

        $ v_tutoring = 9
        $ aftercum = False
        jump day_start

    elif v_tutoring == 9:   # Whoring lvl 20
        m "Итак, мисс Грейнджер, ты хорошо провела вечер?"
        call her_main("Вы не должны спрашивать такие вещи, профессор.","open","closed")
        m "Я должен обеспечить своим студентам приятный ночной отдых."
        call her_main("С вашими занятиями и вашей действительно \"научной\" литературой.","base","concerned",cheeks="blush",tears="soft")
        call her_main("Я стану специалистом по анатомии человека со всей этой документацией.","angry","worriedCl",cheeks="blush")
        m "Тебе нужны некоторые научные инструменты для твоего исследования?"
        call her_main("Они могут пригодиться.","grin","wink",cheeks="blush")
        call her_main("Если только это не ваш член.","annoyed","angryL",cheeks="blush")
        call her_main("{size=-2}(Не то чтобы я не ценю это, но нет очков, нет члена!){/size}","smile","angry",cheeks="blush")
        m "Мисс Грейнджер! Это серьезный вопрос!"
        call her_main("Конечно...","annoyed","suspicious")
        m ".........."
        call her_main("Так, что мне за подарок, на этот раз?","open","suspicious")

        call give_reward(">Ты даешь Гермионе вибратор.","images/store/gifts/12.png")

        call her_main("И я полагаю, вы хотите, чтобы я проверила его перед вами?","open","closed")
        g9 "Конечно."
        call her_main("А где образовательная цель во всем этом?","annoyed","suspicious")
        m "Хороший вопрос. Улучшение навыков?"
        call her_main("В чем? Волшебство?","mad","angry",cheeks="blush")
        m "Конечно."
        her "........."
        call her_main("У меня есть одна просьба.","open","baseL",cheeks="blush")
        call her_main("Если я собираюсь мастурбировать, я не хочу быть единственной. Так что наслаждайтесь бесплатным шоу.","open","worriedCl",cheeks="blush")
        g9 "С удовольствием!"
        call nar(">Ты залезаешь под стол и хватаешь свой член.")

        hide screen hermione_main
        call blkfade

        hide screen genie
        show screen genie_jerking_off
        with d3

        call hide_blkfade

        call her_main("{size=-2}(Думая о директоре мастурбирую, я уже такая мокрая {image=textheart}){/size}",xpos="mid",ypos="base")
        call her_main("{size=-2}(Я стала такой шлюхой. Не то, чтобы мне это не нравилось...){/size}","smile","angry",cheeks="blush")
        call her_main("Так... с чего мы можем начать?","open","squint",cheeks="blush")

        if hermione_wear_bra:
            m "Сними рубашку и лифчик, я хочу увидеть твои сиськи."
            pause.5

            call set_hermione_action("lift_top")
            pause.5

            $ hermione_wear_top = False
            $ hermione_wear_bra = False
            call set_hermione_action("none","skip_update")
            pause.5

        else:
            m "Сними рубашку, я хочу увидеть твои сиськи."
            pause.5

            call set_hermione_action("lift_top")
            pause.5

            $ hermione_wear_top = False
            call set_hermione_action("none","skip_update")
            pause.5

        her "Вам это нравится, не так ли?"
        g9 "О, да..."
        her "Наблюдая за другими девушками, я теперь знаю почему."
        her "Эти груди такие соблазнительные."
        call her_main("Большие или маленькие, я хочу подержать их в руках и сосать соски.","open_tongue","ahegao_raised",cheeks="blush")
        g9 "И я тоже!"
        m "А теперь снимай юбку!"
        pause.5

        call set_hermione_action("lift_skirt")
        pause.5

        $ hermione_wear_bottom = False
        call set_hermione_action("none","skip_update")
        pause.5

        $ b_her_tears = True

        call ctc

        her "Хорошая идея."
        call her_main("Иногда, я хотела бы сделать это с другими девушками.","open","squint",cheeks="blush")
        call her_main("Мастурбировать голой друг перед другом.","open","ahegao_raised",cheeks="blush")
        if hermione_wear_panties:
            g9 "Давай, снимай свои трусики!"
            her "Ваше желание для меня закон."
            pause.5

            call set_hermione_action("pinch")
            pause.5

            $ hermione_wear_panties = False
            call set_hermione_action("none","skip_update")
            pause.5

            $ u_tears_pic = "characters/hermione/face/e_her_tears_02b.png"
            call ctc

            call her_main("И я хочу потрогать киску другой девочки.","silly","ahegao_raised",cheeks="blush")
        else:
            call her_main("Потрогать ее киску, как я трогаю свою сейчас.","silly","ahegao_raised",cheeks="blush")

        call set_hermione_action("pinch")
        pause.5

        call her_main("Ласкать ее.","open_tongue","ahegao_raised",cheeks="blush")

        call set_hermione_action("fingering")
        pause.2

        call her_main("Вставить пальцы в ее мокрую киску.","open_tongue","ahegao_raised",cheeks="blush")
        g11 "Да, да! Теперь вибратор!"

        hide screen hermione_main
        call blkfade

        ##call her_pose("vibrator")
        $ vibrator = True
        show screen hermione_main

        call hide_blkfade
        call ctc

        her "О, я уже об этом забыла."
        call her_main("Я хочу слышать ее стоны, когда буду работать пальцами.","open_wide_tongue","ahegao_mad",cheeks="blush")
        her "Услышать ее оргазм!"
        call her_main("Любите меня! Аааах дааа! {image=textheart} {image=textheart}","open_wide_tongue","ahegao_mad",cheeks="blush")
        #$ b_her_squirt = True # the squirting needs some work. Graphically, I mean.
        call ctc
        g11 "ААА! Ты маленькая шлюха!!!"
        show screen genie_jerking_sperm
        her "Вибратор... ааа я все еще кончаю!!"
        show screen genie_jerking_sperm_02
        g11 "Возьми все!"

        hide screen hermione_main
        call blkfade

        ">Гермиона отдышалась и снова надела одежду."

        call h_action("none") #Resets clothes.

        hide screen her_naked
        call her_chibi("stand","desk","base")
        call gen_chibi("cum_on_desk")
        call hide_blkfade

        $ b_her_tears = False
        #$ aftercum = True   # the aftercum skirt is a bit overkill IMO. Maybe reduce the height of the stains and add some dripping down the legs.

        call her_main("Надеюсь, вам понравилось так же, как и мне.","open","concerned",cheeks="blush",tears="mascara",xpos="right",ypos="base")
        m "О, черт возьми, да, ты отлично справляешься, моя маленькая ведьма!"
        g9 "Очень хорошо!"
        call her_main("Благодарю вас, профессор.","grin","concerned",cheeks="blush",tears="mascara")
        m "После всего этого нужно отдохнуть."
        call her_main("О, да. Спокойной ночи, профессор.","grin","closed",cheeks="blush",tears="mascara")
        m "Спокойной ночи, моя грязная шлюшка."
        call nar("Ты прогоняешь Гермиону.")

        call her_walk("desk","door",2.5)

        call her_head("{size=-4}(Отдыхать...){/size}","base","down_raised",cheeks="blush")
        call her_head("{size=-4}(Не раньше, чем я снова поиграю с этой чудесной игрушкой...){/size}","base","glance",cheeks="blush")
        call her_head("{size=-4}(А потом еще разок...){/size}","silly","glance",cheeks="blush")
        call her_chibi("leave")

        $ v_tutoring = 10
        $ aftercum = False
        jump day_start

    elif v_tutoring == 10:   # Whoring lvl 23
        m "Так... Надеюсь, мои тренировки окупаются."
        call her_main("Вы имеете в виду, делая меня более \"открытой\" к чудесам взрослой жизни?","open","suspicious")
        m "Среди прочего..."
        call her_main("Так я и думала.","annoyed","suspicious")
        call her_main("Но, честно говоря, я с нетерпением жду этого урока.","open","closed")
        call her_main("{size=-2}(Может, мне не стоило этого говорить.){/size}","angry","wide")
        her "{size=-2}(Это сведет его с ума и он будет насиловать меня на столе){/size}"
        call her_main("{size=-2}(Но, я не против...){/size}","angry","worriedCl",cheeks="blush")
        call her_main("{size=-2}(А потом я могу попросить у него очки.){/size}","smile","baseL")
        m "Мисс Грейнджер? Ты в порядке?"
        call her_main("Да, профессор! Извините, я думала о моем следующем экзамене.","grin","wink",cheeks="blush")
        m "О, я уверен, что это очень важное дело. Может, на следующем уроке я смогу тебе помочь."
        call her_main("Думаю, мне бы это очень понравилось!","open","worriedCl",cheeks="blush")
        m "Итак, анальная стимуляция..."
        call her_main("Ах! Я знала, что вы так скажете.","smile","angry",cheeks="blush")
        her "{size=-2}(Еще раз, не то, чтобы я возражала...){/size}"
        call her_main("{size=-2}(Я такая шлюха, что даже Слизеринцы не могут со мной конкурировать...){/size}","base","ahegao_raised",cheeks="blush")
        m "Повтори это еще раз, мисс Грейнджер?"
        call her_main("В этой школе никто не может конкурировать со мной, верно, профессор?","smile","happyCl",cheeks="blush",emote="06")
        call her_main("В любой области!","smile","angry",cheeks="blush")
        m "В какой области? Я не уверен."
        m "Тебе еще есть чему поучиться..."
        call her_main("Что?! Чего же мы тогда ждем?","scream","closed",cheeks="blush")

        call set_hermione_action("lift_top")
        pause.2

        $ hermione_wear_top = False
        $ hermione_wear_bra = False
        call set_hermione_action("none","skip_update")

        ">Она срывает с себя рубашку и бросается к вашему столу."

        call her_walk_desk_blkfade

        hide screen genie
        show screen groping_05
        call hide_blkfade
        call ctc

        call bld
        m "Мы еще даже не начали, а ты уже мокрая, моя прелестная шлюшка."

        show screen blktone
        call her_main("Это все вы, со своими грязными разговорами!","annoyed","angryL",cheeks="blush",xpos="mid",ypos="base")
        her "Про анальную пробку, вылизывание ануса и... и..."
        call her_main("Фистинг!","open","ahegao_raised",cheeks="blush")
        m "Я никогда не упоминал об этом."
        call her_main("Оу. Вы не говорили этого?","annoyed","ahegao_raised",cheeks="blush")
        call her_main("Ну, может быть, вы не говорили, но вы {b}думали {/b} об этом!","base","ahegao_raised",cheeks="blush")
        g9 "Возможно."
        g9 "Твоя задница такая сочная, что я хочу ее съесть."
        call her_main("Вот именно!","angry","worriedCl",cheeks="blush")
        call her_main("Хватит болтать, старик. Приступайте к работе!","base","concerned",cheeks="blush",tears="soft")
        m "Я еще даже не вручил тебе твой подарок!"
        m "Я просто положу его туда, где ты обязательно найдешь."
        m "Итак, мы можем начать урок?"
        call her_main("Да, Мерлинова борода!","open","base",cheeks="blush")
        m "Но перед этим..."
        call her_main("Если скажете еще хоть слово, клянусь, я сейчас же вернусь в общежитие!","scream","angry",cheeks="blush",emote="01")
        call nar(">Ты вдруг вставляешь в нее анальную пробку.")
        call her_main("Дааа {image=textheart} вот так!","silly","ahegao_raised",cheeks="blush")
        call nar(">Ты вынимаешь его так же быстро, смачно шлепая ее по заднице.")

        play sound sd_boing1
        with flashbulb
        play sound sd_slap
        with hpunch

        call her_main("Дааа, больше {image=textheart}.","open_tongue","ahegao_raised",cheeks="blush")
        g9 "Как пожелаешь, принцесса."
        call nar(">Ты быстро вставляешь и вытаскиваешь ее.")

        play sound sd_boing1
        pause.1
        play sound sd_slap
        with hpunch

        $ u_tears_pic = "characters/hermione/face/e_her_tears_03d.png"
        $ b_her_tears = True
        call her_main("Еще!!","open_tongue","ahegao_raised",cheeks="blush")

        play sound sd_boing1
        pause.1
        play sound sd_slap
        with hpunch

        $ u_tears_pic = "characters/hermione/face/e_her_tears_03b.png"
        call her_main("Аааах {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush")

        play sound sd_boing1
        pause.1
        play sound sd_slap
        with hpunch

        m "Знаешь, ты тоже можешь себя трогать."
        $ u_tears_pic = "characters/hermione/face/e_her_tears_03d.png"
        call her_main("Я не могу.","open_wide_tongue","ahegao_mad",cheeks="blush")
        her "{size=-2}(Если я это сделаю, я потеряю то немногое достоинство, что у меня осталось){/size}"
        call her_main("{size=-2}(Но сегодня...){/size}","open_wide_tongue","ahegao_mad",cheeks="blush")
        m "Тогда я с этим разберусь."
        call nar(">Ты засунул пальчики в обе ее дырочки: киску и в анал.")
        call her_main("Нет, это слишком. {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush")
        g9 "Быстрее? Нет проблем!"
        hide screen groping_05
        show screen groping_05b
        $ b_her_tears = False
        call her_main("Ааах, вы убиваеете меня {image=textheart}.","angry","dead",cheeks="blush",tears="crying")
        call her_main("{size=-2}(И мне это нравится){/size}","silly","worried",cheeks="blush",tears="soft")
        m "Еще пальчиков?"
        call her_main("Не надо больше пожалуйссста.","open","concerned",cheeks="blush",tears="mascara")
        m "Вообще-то, это был не вопрос."
        call her_main("Если вы будете держать этот темп, я...","angry","dead",cheeks="blush",tears="crying")
        call nar(">Ты чувствуешь пальцами, как ее мышцы сжимаются.")
        call her_main("Скоро!!","open_wide_tongue","ahegao_mad",cheeks="blush")
        g9 "Хорошая девочка."
        her "Продолжай в том же духе..."
        call her_main("Даааа {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush")
        m "Я могу продолжать до тех пор, пока тебе будет угодно."
        $ u_tears_pic = "characters/hermione/face/e_her_tears_04.png"
        $ b_her_tears = True
        call her_main("Дааа {image=textheart}, нееет я умру!","open_wide_tongue","ahegao_mad",cheeks="blush")
        g9 "В экстазе."
        call her_main("Аааа, нееет, снова {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush")
        hide screen groping_05b
        show screen no_groping_05
        m "Думаю, с тебя хватит на этот вечер."
        call her_main("Да я... Я лучше пойду.","open_tongue","ahegao_raised",cheeks="blush")
        m "Ты забыла свой подарок."
        call nar(">Ты быстро вставляешь в нее анальную пробку.")
        with hpunch
        call her_main("Aaaaaaaх.","open_wide_tongue","ahegao_mad",cheeks="blush")

        hide screen hermione_main
        call blkfade

        hide screen no_groping_05
        show screen no_groping_05_desk

        ">Она падает задыхаясь на столе."
        g9 "Это самый лучший вид, в мире."

        ">Через некоторое время, она одевает рубашку."

        call h_action("none") #Resets clothes.

        hide screen no_groping_05_desk
        show screen genie
        call her_chibi("stand","desk","base")
        call hide_blkfade
        pause.5

        call her_main("Спасибо вам за все, профессор.",tears="mascara",xpos="right",ypos="base")
        call her_main("Это было очень...{w=0.5} поучительно.","grin","concerned",cheeks="blush",tears="mascara")
        call her_main("Но, пожалуйста, постарайтесь быть со мной помягче в следующий раз.","grin","closed",cheeks="blush",tears="mascara")
        g9 "У меня нет абсолютно никакой идеи, что ты подразумеваешь под этим."
        call her_main("Спокойной ночи, профессор.","grin","glance",cheeks="blush",tears="mascara")
        m "Спокойной ночи, моя дорогая анальная шлюха."
        call her_main("Профессор...","open","concerned",cheeks="blush",tears="mascara")

        call nar("Ты прогоняешь Гермиону.")

        call her_walk("desk","door",2.5)

        call her_head("{size=-4}(Наконец-то сегодня я пойду спать.){/size}","base","worriedCl",cheeks="blush")
        call her_head("{size=-4}(Это было слишком напряженно.){/size}","angry","worriedCl",cheeks="blush")
        call her_head("{size=-4}(Не то, чтобы я жаловалась...){/size}","silly","glance",cheeks="blush")
        call her_chibi("leave")

        $ v_tutoring = 11
        $ aftercum = False
        jump day_start

    elif v_tutoring == 11:
        m "[hermione_name], У меня есть кое-что для тебя."
        call her_main("Еще один подарок для меня?","base","ahegao_raised",cheeks="blush")
        call her_main("Пожалуйста, пожалуйста.","open","worriedCl",cheeks="blush")
        m "Ты не была так взволнована в прошлый раз, когда я сделал тебе подарок..."
        call her_main("Не волнуйтесь, это был просто момент слабости.","smile","angry",cheeks="blush")
        her "Я уже готова!"
        call her_main("{size=-2}(Но мое тело, вероятно, нет...){/size}","annoyed","down")
        m "Тебе понравилось с анальной пробкой?"
        call her_main("Д-да... Я ношу ее иногда...","base","ahegao_raised",cheeks="blush")
        call her_main("Но я отрезала хвостик!","annoyed","angryL",cheeks="blush")
        her "{size=-2}(Я никак не могла с ним разгуливать...){/size}"
        m "И тебе это нравится?"
        call her_main("Это очень...{w=0.5} стимулирует. Это помогает мне, когда я накладываю заклинание.","base","concerned",cheeks="blush",tears="soft")
        m "Скажи мне правду, мисс Грейнджер, ты носишь его все время, не так ли?"
        call her_main("Нееет ...","annoyed","angryL",cheeks="blush")
        call her_main("Возможно...","open_tongue","ahegao_raised",cheeks="blush")
        her "........"
        m "Не стыдись, все в порядке, моя маленькая шлюха."
        call her_main("Я ношу его все время...{w=0.3} и мне нравится!","smile","happyCl",cheeks="blush",emote="06")
        g9 "{size=-2}(Чудесно){/size}"
        m "Я хорошо тренировал тебя."
        call her_main("Чтобы быть шлюхой? Да, это так...","open","closed")
        call her_main("И теперь я хочу больше, где мой подарок?!","annoyed","suspicious")
        m "Там, там."

        call give_reward(">Ты даешь анальные шарики Гермионе","images/store/gift_anal_beads.png")

        call her_main("О! Это даже лучше, чем анальная пробка.","shock","wide",cheeks="blush")
        g9 "И они могут быть полезны и для твоей киски."
        call her_main("Так много возможностей...","smile","angry",cheeks="blush")
        her "...так мало времени."
        call her_main("Полагаю, вы хотите, чтобы я их попробовала?","smile","happyCl")
        her "Или вы предпочитаете испытать на мне их сами?"
        g9 "О, да."
        call her_main("Я даже не знаю, почему я спрашиваю...","annoyed","ahegao")
        her "{size=-2}(Старый извращенец...){/size}"
        call her_main("{size=-2}({b}Мой{/b} старый извращенец){/size}","open","worriedCl",cheeks="blush")

        call set_hermione_action("lift_top")
        pause.5

        $ hermione_wear_top = False
        $ hermione_wear_bra = False
        call set_hermione_action("none","skip_update")
        pause.5

        call her_main("Мои сиськи лучшие во всем Хогвартсе!","silly","ahegao_raised",cheeks="blush")
        m "Ты была со многими девочками, чтобы заявлять это?"
        call her_main("Я думаю...","grin","ahegao_mad",cheeks="blush")
        g9 "Я могу обучить тебя и этому."
        call her_main("Может нам сначала закончить этот урок.","base","ahegao_raised",cheeks="blush")
        m "У нас есть свободное время."
        call her_main("Кстати об этом...","base","concerned",cheeks="blush",tears="soft")

        call her_walk_desk_blkfade

        hide screen genie
        show screen no_groping_05
        with d1
        call hide_blkfade
        call ctc

        call bld
        g9 "Как всегда, это восхитительный вид."
        call blktone
        call her_main("Я рада, что вам понравилось.","angry","worriedCl",cheeks="blush",xpos="mid",ypos="base")

        call set_hermione_action("lift_skirt")
        pause.5

        $ hermione_wear_bottom = False
        $ hermione_wear_panties = False
        call set_hermione_action("none","skip_update")
        pause.5

        call her_main("Мы можем начать прямо сейчас?","grin","angry",cheeks="blush")
        g9 "Полагаю, ты хочешь, чтобы они были у тебя в заднице?"
        call her_main("Естественно.","base","ahegao_raised",cheeks="blush")
        call her_main("{size=-2}(Я попробую их в моей киске сегодня вечером){/size}","base","closed")
        hide screen no_groping_05
        show screen groping_05
        call nar(">Ты вводишь в нее первый шарик, он легко проходит.")
        her "Хммм {image=textheart}"
        m "Сколько, по-твоему, ты сможешь вместить, дорогая?"
        call her_main("А сколько их там всего?","base","ahegao_raised",cheeks="blush")
        g9 "Вот это настрой!"
        call nar(">Ты толкаешь следующий внутрь с небольшим сопротивлением.")
        call her_main("Даа {image=textheart}, еще один, пожалуйста.","open","ahegao_raised",cheeks="blush")
        call nar(">Ты чувствуешь, что бусинки проходят глубже, когда ты проталкиваешь третий шарик внутрь.")
        $ u_tears_pic = "characters/hermione/face/e_her_tears_01.png"
        $ b_her_tears = True
        call her_main("Оххх, они... они движутся {image=textheart}.","grin","ahegao_mad",cheeks="blush")
        call nar(">Для четвертого нужно немного времени, прежде чем он исчезнет.")
        $ b_her_tears = False
        call her_main("Ах {image=textheart} ах {image=textheart}.","silly","ahegao_raised",cheeks="blush")
        call nar(">Ты с усилием заталкиваешь последний.")
        call her_main("Аххх {image=textheart}, восхитительно.","open_tongue","ahegao_raised",cheeks="blush")
        her "Они так глубоко в моей заднице... почти как ваш член."
        g9 "Я могу..."
        call her_main("Нет, вы не можете! Моя задница слишком тугая для двоих.","annoyed","closed",cheeks="blush")
        call her_main("{size=-2}(Но это такая хорошая идея){/size}","grin","ahegao_mad",cheeks="blush")
        m "Я уверен, что еще есть место хотя бы для одного пальца."
        call nar(">Ты осторожно прикосаешься к ее анусу.")
        call her_main("Ахх... {image=textheart}{w=0.5} аах...{image=textheart}","silly","ahegao_raised",cheeks="blush")
        call her_main("Зачем я говорю...","grin","ahegao_mad",cheeks="blush")
        call nar(">Ты шевелишь пальцем внутри.")
        $ u_tears_pic = "characters/hermione/face/e_her_tears_03b.png"
        $ b_her_tears = True
        call her_main("Вы никогда меня не слушаете, старый извращенец.","grin","ahegao_mad",cheeks="blush")
        m "Что я могу сказать, я просто знаю, что лучше для тебя, моя маленькая ведьма."
        call nar(">Ты набираешь ритм.")
        $ u_tears_pic = "characters/hermione/face/e_her_tears_03d.png"
        $ b_her_tears = True
        call her_main("Дааа {image=textheart}.","grin","ahegao_mad",cheeks="blush")
        m "Я думал, тебе не нужен палец?"
        g9 "Может в таком случае, еще один."
        call nar(">Она дрожит, когда ты вставляешь второй палец.")
        call her_main("Аааа нееет... пожалуйста, не надо.","grin","angry",cheeks="blush")
        call her_main("Моя дырка растягивается!","open","ahegao_raised",cheeks="blush")
        g9 "У тебя отличная дырка."
        call nar(">Ты пальцем яростно теребишь ее анальные дырочки.")
        hide screen groping_05
        show screen groping_05b
        $ b_her_tears = False
        call her_main("Нет... аахх {image=textheart}.","open","concerned",cheeks="blush",tears="mascara")
        m "Твоя киска чувствует себя одинокой. Мы должны это исправить!"
        call nar(">Ты начинаешь теребить ее киску другой рукой. Она тяжело дышит.")
        call her_main("Ах... ах... вот так дааа {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush")
        call nar(">Ты вдруг резко махом вытаскиваешь все шарики.")
        call her_main("Аххххх!!","grin","dead",cheeks="blush",tears="messy")
        call nar(">И вставляешь четыре пальца в ее задницу.")
        $ u_tears_pic = "characters/hermione/face/e_her_tears_04.png"
        $ b_her_tears = True
        call her_main("Я кончаю старый ублюдок, я кончаю!","silly","ahegao_raised",cheeks="blush")
        m "Если ты хочешь..."
        call nar(">Ты продолжаешь работать с ее анусом в то время как пальчиком теребишь ее киску.")
        her "Нет, я..."
        call her_main("Кончааааю {image=textheart}{image=textheart}.","silly","worried",cheeks="blush",tears="soft")
        call her_main("Снооова ааах {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush")
        g11 "Жаль моя маленькая анальная шлюха, но я начинаю уставать."
        $ b_her_tears = False
        call her_main("Не смейте останавливаться сейчас!","scream","angry",cheeks="blush",tears="messy")
        call her_main("Просто еще немного, умоляяяю {image=textheart}.","grin","dead",cheeks="blush",tears="messy")
        call her_main("Потому что я...","grin","dead",cheeks="blush",tears="messy")
        $ u_tears_pic = "characters/hermione/face/e_her_tears_04.png"
        $ b_her_tears = True
        call her_main("Кончу снова!!","open_wide_tongue","ahegao_mad",cheeks="blush")
        hide screen hermione_main
        call blkfade

        ">Небольшая лужица образовалась на твоем столе из ее соков. Ты медленно убираешь из нее пальцы."

        hide screen groping_05b
        show screen no_groping_05_desk
        call hide_blkfade
        pause.5

        $ b_her_tears = False
        call her_main("*Пых* *пых*","open","concerned",cheeks="blush",tears="mascara")
        call her_main("Я чувствую себя полностью опустошенной, но счастливой.","grin","glance",cheeks="blush",tears="mascara")
        call her_main("Спасибо, профессор, что позволили мне, открыть для себя такие великие ощущения.","grin","glance",cheeks="blush",tears="mascara")
        call her_main("Но я устала, так что, спокойной ночи.","grin","closed",cheeks="blush",tears="mascara")
        hide screen hermione_main
        call blkfade

        ">Она надевает рубашку и мчится к двери."

        call h_action("none") #Resets clothes.

        hide screen no_groping_05_desk
        call her_chibi("stand","door","base",flip=True)
        show screen genie
        call hide_blkfade

        m "Вернись сюда, девочка."
        g11 "Мне нужен твой рот, я больше не могу сдерживатся."
        $ u_tears_pic = "characters/hermione/face/e_her_tears_03.png"
        $ b_her_tears = True
        pause.5

        call her_chibi("stand","door","base")
        pause.5

        call her_main("Профессор!","open","squint",cheeks="blush")
        call her_main(".........","base","ahegao_raised",cheeks="blush")
        call her_main("Могу ли я получить баллы за это?","mad","wide",cheeks="blush")
        g11 "Живо!"
        hide screen hermione_main
        call blkfade

        ">Она возвращается и не выглядит особенно расстроенной."

        call her_chibi("hide")
        hide screen genie
        $ genie_chibi_xpos = -10
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "blowjob_ani"
        show screen chair_left
        show screen g_c_u
        call hide_blkfade
        call ctc

        call her_head("*Slurp!* *Slurp!* *Gulp!*",xpos="base",ypos="base")
        g9 "Да, вот так..."
        call nar(">Гермиона жадно сосет твой член.")
        m "Кажется, ты торопишься. Это потому что ты не получаешь за это очки?"
        m "Считай это оплатой за твои частные уроки."
        her "Мммх..."
        m "В следующий раз приди в халате и только в халате на голое тело."
        call nar(">Она кратко кивает.")
        her "*Slurp!* *Gulp!* *Slurp!*"
        g9 "Ты отлично справляешься моя маленькая шлюха, я..."
        g11 "Да!"

        call cum_block
        $ g_c_u_pic = "cum_in_mouth_ani"
        show screen g_c_u
        hide screen bld1
        with d3

        her "*Gobble!* *Gobble!* *Gobble!*"
        call ctc

        g9 "Хорошая девочка, все проглотила!"
        call blkfade

        ">Она вытирает свой рот."
        hide screen g_c_u
        hide screen chair_left
        show screen genie
        call her_chibi("stand","desk","base")
        call hide_blkfade
        call ctc

        call her_main("Сэр, я все еще думаю, что заслуживаю немного...","annoyed","angryL",cheeks="blush")
        m "Спокойной ночи, дитя мое."
        call her_main(".........","annoyed","ahegao_raised",cheeks="blush")
        call her_main("Спокойной ночи, профессор.","annoyed","closed",cheeks="blush")
        call nar("Ты прогоняешь Гермиону.")

        $ b_her_tears = False

        call her_walk("desk","door",2.5)

        call her_head("{size=-4}(Сосать его член, не получая никаких очков!){/size}","annoyed","angryL",cheeks="blush")
        call her_head("{size=-4}(Если бы он не заставил меня так сильно кончить...){/size}","base","ahegao_raised",cheeks="blush")
        call her_head("{size=-4}(*вздох* Хотя, думаю, это не такая уж и большая цена...){/size}","base","down_raised",cheeks="blush")
        call her_chibi("leave")

        $ v_tutoring = 12
        $ aftercum = False
        jump day_start

    elif v_tutoring == 12:
        call her_main("Ой! Не могу поверить, что я забыла! Оставайтесь на месте, я скоро вернусь!","mad","wide",cheeks="blush")
        hide screen hermione_main
        play sound sd_door
        call blkfade

        play sound sd_door
        pause.3

        ###MAKE HER WEAR JUST A ROBE
        $ h_robe = "gryff_robe_gap"
        $ hermione_robe = "characters/hermione/clothes/robe/base/"+str(h_robe)+".png"
        call h_action("naked") #Removes all clothes.
        $ hermione_wear_robe = True
        call update_chibi_uniform

        call her_chibi("stand","door","base")
        call hide_blkfade

        call her_walk("door","mid",3)

        call her_main("{size=-4}*panting*{/size} О, хорошо, что вы все еще здесь.","open","base",cheeks="blush",xpos="right",ypos="base")
        m "Можно ли с уверенностью предположить, что на этот раз ты выполнила мою просьбу?"
        call her_main("Я думала, что это очевидно.","open","squint",cheeks="blush")
        call her_main("Мне даже пришлось спрятаться в нише, чтобы меня не заметили по дороге сюда!","open","base",cheeks="blush")
        call her_main("Это было так неловко!","open","worriedCl",cheeks="blush")
        call her_main("{size=-2}(И захватывающе!){/size}","open","worriedCl",cheeks="blush")
        m "Ты уверена, что под ним ничего нет?"
        call nar(">Гермиона немного раскрывает халат.")
        pause.2

        hide screen hermione_main
        $ h_robe = "gryff_robe_gap_wide"
        $ hermione_robe = "characters/hermione/clothes/robe/base/"+str(h_robe)+".png"
        call her_main("","open","squint",cheeks="blush")
        call ctc

        call her_main("Это ответ на ваш вопрос?","open","squint",cheeks="blush")
        m "Едва ли. Трудно сказать с такого расстояния. Я имею в виду, здесь так темно..."
        call her_main("...","annoyed","ahegao_raised")
        pause.2

        hide screen hermione_main
        $ h_robe = "gryff_robe_off"
        $ hermione_robe = "characters/hermione/clothes/robe/base/"+str(h_robe)+".png"
        call her_main("","base","closed",cheeks="blush",trans="d5")
        call ctc

        call her_main("Так лучше?","base","glance",cheeks="blush")
        g9 "Ах, да, наверняка. Молодец, моя девочка."

        hide screen hermione_main
        $ h_robe = "gryff_robe_gap_wide"
        $ hermione_robe = "characters/hermione/clothes/robe/base/"+str(h_robe)+".png"

        call her_main("Хорошо, мы можем сейчас начинать урок?","smile","angry",cheeks="blush")
        m "Может быть, я не знаю... тебе нравится сливочное пиво?"
        call her_main("Вы же знаете. Какое это имеет отношение?..","soft","baseL",cheeks="blush")
        g9 "......."
        call her_main("Вы имеете в виду...{w=0.3} нет, профессор!","scream","wide",cheeks="blush")
        m "О, будь уверена, мы не начнем с толстой части."
        call her_main("Тем не менее, профессор, это так грязно...","silly","ahegao_raised",cheeks="blush")
        call her_main("{size=-2}(И захватывающе){/size}","silly","ahegao_raised",cheeks="blush")
        call her_main("Кроме того, моя задница недостаточно растянута.","annoyed","closed",cheeks="blush")
        g4 "Ты шутишь, со всем тренировками?!"
        call her_main("А что за тренировки!","annoyed","ahegao_raised",cheeks="blush")
        call her_main("{size=-2}(Хорошо, что я тренировалась сама, иначе...){/size}","angry","worriedCl",cheeks="blush")
        g4 "Перестань придумывать оправдания!"
        m "Я вижу, как ты от возбуждения потираешь бедра!"
        call her_main("Я думала, здесь так темно...","open","squint",cheeks="blush")
        call her_main("Хм, хорошо, но вам лучше начать с чего-то нежного.","annoyed","suspicious")
        g9 "Я всегда нежен с тобой, дитя мое."
        call her_main("Да, конечно...","annoyed","ahegao")
        m "{size=-2}(Или может ей нравится грубо){/size}"
        m "Хорошо, на мой стол, и ты, голая, мигом!"

        call her_walk_desk_blkfade

        $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking.
        pause.5

        ">Гермиона медленно скидывает вниз халат и поднимается по твоему столу."

        $ hermione_wear_robe = False

        call her_chibi("dance","on_desk","on_desk")

        call hide_blkfade
        pause 1

        call blktone
        call her_main("Вы без ума от моего тела, не так ли?",xpos="mid",ypos="base")
        m "Почему ты спрашиваешь?.."
        call her_main("Потому что девушкам нравятся комплименты, профессор!","annoyed","suspicious")
        call her_main("Особенно, когда она собирается делать такие вещи!","annoyed","ahegao")
        m "Конечно, у тебя потрясающее тело! Это не подлежит сомнению."
        call her_main("Лучшее в школе?","base","ahegao_raised",cheeks="blush")
        m "......{w=0.3} Да, да, лучшее в школе."
        call her_main("Я могу сказать, что вы лжете!","mad","angry",cheeks="blush")
        m "Мисс Грейнджер, я жил в течение очень долгого времени и поверь мне, я видел всего несколько женщин с телом, как у тебя."
        m "И определенно ни одной в этой школе."
        m "{size=-2}(Когда же Северус отправит ко мне своих шлюх из Слизерина){/size}"
        m "{size=-2}(Интересно, могу ли я уволить его за это...){/size}"
        call her_main("Благодарю вас, профессор.","open","worriedCl",cheeks="blush")
        call her_main("Не стесняйтесь использовать мое тело как вам угодно.","angry","worriedCl",cheeks="blush")
        m "{size=-2}(*Вздох* женщины...){/size}"
        m "Наклонись над столом, моя дорогая ведьма."
        call her_main("{size=-2}(Он начинает с моей дорогой маленькой ведьмы и заканчивает моей дорогой анальной шлюхой...){/size}","annoyed","ahegao_raised",cheeks="blush")
        call her_main("{size=-2}(*Вздох* Мужики...){/size}","annoyed","ahegao_raised",cheeks="blush")
        call her_main("Как пожелаете, дорогой {b}престарелый{/b} директор.","open","squint",cheeks="blush")
        m "{size=-2}(Если бы ты знала, сколько мне на самом деле лет...){/size}"
        hide screen hermione_main
        call blkfade

        ">Гермиона вяло взбирается по твоему столу и наклоняется."

        call her_chibi("hide")
        hide screen genie

        show screen no_groping_laying_02

        call her_head("Я готов, [genie_name].",xpos="base",ypos="base")
        ">Ты берешь пустую бутылку из под сливочного пива, плюешь на ее горлышко и толкаешь его в анус девочке."

        hide screen no_groping_laying_02
        show screen scr_her_fingering_naked("slow")
        hide screen bld1
        hide screen blktone
        call hide_blkfade
        call ctc

        call her_main("Ммм, да вот так.","base","ahegao_raised",cheeks="blush")
        call her_main("Моя киска чувствует себя одинокой без вашей помощи.","grin","wink",cheeks="blush")
        call nar(">Ты начинаете пальцем тереть и ее киску.")
        m "Бедняжка."
        call her_main("Что может быть лучше, чем это, профессор?","open","ahegao_raised",cheeks="blush")
        m "Ой, я не знаю."
        call her_main("Спасибо, что позволили мне открыть для себя такие удовольствия.","open","worriedCl",cheeks="blush")
        g9 "{b}Мое{/b} удовольствие."
        call her_main("Это даже лучше, когда это взаимно, не так ли?","open","squint",cheeks="blush")
        m "Хм, да, ты совершенно права. Я рад, что ты так думаешь."
        call her_main("Теперь немного глубже, пожалуйста.","soft","baseL",cheeks="blush")
        call nar(">Ты засовываешь всю бутылку ей в задницу.")
        call her_main("Ооо, даааа! {image=textheart}","open","ahegao_raised",cheeks="blush")
        call her_main("Больше, быстрее!","open","ahegao_raised",cheeks="blush")
        show screen scr_her_fingering_naked()
        call nar(">Ты двигаешь бутылку, взад и вперед все глубже и глубже.")
        call her_main("Даааа, не забудьте про мою киску {image=textheart}.","grin","ahegao_mad",cheeks="blush")
        g9 "Ох, твоей киске лучше быть готовой к тому, что будет!"
        call nar(">Ты вставляешь все четыре пальца в ее мокрую киску.")
        call her_main("Ооо Калех, ааа, ааа, это слишком много! {image=textheart}(прим.Калех /'В оригинале Цирцея - из Одиссеи/' Калех - В мифологии островных кельтов - божественная колдунья, божество-творец и богиня погоды, а также прародительница других богов. )","open","concerned",cheeks="blush",tears="mascara")
        m "Ничто не сможет быть слишком, для моей маленькой шлюхи."
        call nar(">Ты увеличиваешь темп обеих рук.")
        call her_main("Нет, нет, да, даааа! {image=textheart}","grin","dead",cheeks="blush",tears="messy")
        call nar(">Большая часть бутылки находится внутри нее, что тебе уже за нее не ухватиться.")
        m "Выталкивай бутылку, Толкай!"
        call nar(">Всякий раз, когда она выталкивает ее, ты делаешь то же самое в другом направлении.")
        $ u_tears_pic = "characters/hermione/face/e_her_tears_04.png"
        $ b_her_tears = True
        call her_main("Это, это, аааах!!! {image=textheart}{image=textheart}","open_wide_tongue","ahegao_mad",cheeks="blush")
        call nar(">Все ее тело содрогается, когда к ней приходит оргазм.")
        hide screen hermione_main
        call blkfade

        $ b_her_tears = False
        hide screen scr_her_fingering_naked
        show screen no_groping_laying_02
        pause.3
        call hide_blkfade
        call ctc

        call her_main("*Panting* *panting*","grin","dead",cheeks="blush",tears="messy")
        call her_main("П-профессор...{w=0.3} Я так счастлива.","base","concerned",cheeks="blush",tears="soft")
        g9 "Приятно это слышать."
        hide screen hermione_main
        call blkfade

        ">Через некоторое время, она оделась."

        $ hermione_wear_robe = True

        hide screen no_groping_laying_02
        show screen genie
        call her_chibi("stand","desk","base")
        call hide_blkfade

        call bld
        m "Сладких снов моя маленькая принцесса."
        call her_main("И вам тоже, профессор.","open","base",cheeks="blush",xpos="right",ypos="base")
        g9 "Они всегда сладкие после тебя."
        call her_main("Спасибо.","base","ahegao_raised",cheeks="blush")
        m "И в следующий раз принеси свои книги, я помогу тебе с учебой."
        call nar("Ты прогоняешь Гермиону.")

        $ b_her_tears = False

        call her_walk("desk","door",2.5)

        call her_head("{size=-4}(Да, сладких снов...){/size}","base","worriedCl",cheeks="blush")
        call her_head("{size=-4}(Сладких и мокрых!){/size}","silly","glance",cheeks="blush")
        call her_chibi("leave")

        $ v_tutoring = 13

        call h_action("none") #Resets clothes.

        $ aftercum = False
        jump day_start

    elif v_tutoring == 13:
        call her_main("Я сейчас же принесу свои книги, сэр!","soft","baseL")
        hide screen hermione_main
        play sound sd_door
        call blkfade
        pause 1

        call h_action("hold_book")

        play sound sd_door
        pause.3

        call hide_blkfade
        call ctc

        call her_main("Проверка-это серьезный вопрос, [genie_name]!","open","worried")
        m "{size=-2}(Мой член в твоей заднице-серьезное дело...){/size}"
        m "В связи с этим, я вроде как солгал, это скорее пробный экзамен, чем проверка."
        call her_main("Какой сюрприз!","annoyed","ahegao_raised",cheeks="blush")
        m "Мне нужно убедиться, что ты работаешь над своей задницей."
        call her_main("........","annoyed","ahegao_raised",cheeks="blush")
        g9 "Своим членом."
        call her_main("Я вижу...","annoyed","baseL")
        call her_main("Я не против, но могу поспорить, что не получу за это очков?","annoyed","angryL",cheeks="blush")
        m "Я помогаю тебе с твоей проверкой, почему ты должна зарабатывать очки за это?"
        call her_main("И что за проверка...","annoyed","closed",cheeks="blush")
        call her_main("Ладно, раз уж вы мне очень помогаете, я согласна.","base","baseL",cheeks="blush")
        call her_main("{size=-2}(Я сейчас отдаю себя бесплатно, какая я плохая шлюха){/size}","base","concerned",cheeks="blush",tears="soft")
        m "Иди сюда и раздевайся."

        call her_walk_desk_blkfade

        hide screen hermione_main
        with d3

        call h_action("naked")
        call h_action("hold_book")

        call blktone
        hide screen blkfade
        call her_main(xpos="mid",ypos="base")
        call ctc

        m "Ладно, положи свои книги и наклонись над столом, моя маленькая шлюха."
        pause.5

        call set_hermione_action("none","skip_update")
        pause.5

        hide screen hermione_main
        call blkfade

        call her_chibi("hide")
        hide screen genie
        show screen no_groping_laying_02
        hide screen bld1
        hide screen blktone
        call hide_blkfade
        call ctc

        call bld
        g9 "Можешь открыть книгу, если хочешь."

        call her_main("Я читала про это заклинание, оно называется \"Хлопок\"!","annoyed","closed",cheeks="blush")

        hide screen hermione_main
        call nar(">Ты воспользовался моментом ее отвлечения, чтобы вставить свой член в ее анус.")

        hide screen no_groping_laying_02
        show screen chair_left
        show screen scr_her_sex("slow")
        hide screen bld1
        with d1
        with hpunch
        pause.8

        call her_main("Ах, вы, скотина {image=textheart}.","grin","ahegao_mad",cheeks="blush")
        m "Твоя задница идеально подходит, не слишком туго и не слишком растянуто!"
        call her_main("Вы хорошо тренировали меня...","silly","ahegao_raised",cheeks="blush")
        call nar(">Ты ласкаешь ее клитор, трахая ее.")
        call her_main("Мммх, да {image=textheart}.","open","ahegao_raised",cheeks="blush")
        g9 "Ты любишь это, не так ли?"
        call her_main("Ваш член в моей заднице, о да.","base","ahegao_raised",cheeks="blush")
        m "Даже без очков?"
        call her_main("Не заставляйте меня жалеть, что согласилась на это.","upset","worriedCl",cheeks="blush")
        m "Скажите, что ты любишь это, даже без очков."
        show screen scr_her_sex()
        call nar(">Ты увеличиваешь темп.")
        call her_main("Ахх даааа {image=textheart}.","open_tongue","ahegao_raised",cheeks="blush")
        call her_main("Я такая шлюха, я люблю секс даже бесплатно.","mad","wide",cheeks="blush")
        g9 "Теперь мы это знаем!"
        call her_main("Не вводите это в привычку.","open","squint",cheeks="blush")
        m "......"
        call nar(">Ты вытаскиваешь свой член и грубо засовываешь его обратно внутрь.")
        $ u_tears_pic = "characters/hermione/face/e_her_tears_01.png"
        $ b_her_tears = True
        with hpunch
        call her_main("Ааааах {image=textheart}.","open","ahegao",cheeks="blush")
        call her_main("Мне нравится, когда мой директор жестко издевается надо мной.","silly","ahegao_raised",cheeks="blush")
        call nar(">И еще раз.")
        with hpunch
        her "Даааа {image=textheart}."
        call her_main("Я люблю его большой член в моей заднице.","silly","worried",cheeks="blush",tears="soft")
        call nar(">Ты шлепнул ее по ягодице.")
        play sound sd_slap
        with hpunch
        $ b_her_tears = False
        call her_main("И быть наказанной за свою распутность.","open","concerned",cheeks="blush",tears="mascara")
        play sound sd_slap
        with hpunch
        call her_main("Ааа, вот так накажите меня еще, хозяин {image=textheart}.","silly","worried",cheeks="blush",tears="soft")
        play sound sd_slap
        with hpunch
        call her_main("Даа!","open_wide_tongue","ahegao_mad",cheeks="blush")
        play sound sd_slap
        with hpunch
        call her_main("Бооольше!","open_wide_tongue","ahegao_mad",cheeks="blush")
        play sound sd_slap
        with hpunch
        call her_main("Я собираюсь...","angry","dead",cheeks="blush",tears="crying")
        play sound sd_slap
        with hpunch
        pause.1
        play sound sd_slap
        with hpunch
        pause.1
        call her_main("Кооончить {image=textheart}{image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush")
        show screen scr_her_sex("fast")
        call nar(">Ты отчаянно трахаешь ее в попу.")
        call her_main("Да, да, еще, ааах {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush")
        g11 "Да, моя маленькая шлюха, да!"
        hide screen scr_her_sex
        show screen scr_her_sex_cum_outside()
        call her_main("*Запыхаясь* *запыхаясь*","open","concerned",cheeks="blush",tears="mascara")
        show screen scr_her_sex_cum_outside(1)
        g11 "*Запыхаясь* *запыхаясь*"

        hide screen hermione_main
        call blkfade

        hide screen chair_left
        hide screen hermione_main
        hide screen scr_her_sex_cum_outside
        pause 1
        show screen no_groping_laying_02
        hide screen bld1
        hide screen blktone
        call hide_blkfade
        pause.8

        call bld
        m "*вздох* это было... это было..."
        $ u_tears_pic = "characters/hermione/face/e_her_tears_03.png"
        $ b_her_tears = True
        call her_main("Изумительно {image=textheart}.","smile","baseL")
        call her_main("Я так рада, что вы согласились обучать меня, профессор...","silly","ahegao_raised",cheeks="blush")
        call her_main("Ваши уроки так изменили мою жизнь!","smile","angry",cheeks="blush")
        g9 "{size=-2}(Победа!){/size}"
        call her_main("Но если вы думаете, что можете трахать меня все время, не давая мне очков...","annoyed","angryL",cheeks="blush")
        call her_main("И не мечтайте!","annoyed","ahegao_raised",cheeks="blush")
        m "{size=-2}(Оооо...){/size}"
        m "Даже иногда?"
        her "......."
        call her_main("Только если вы будете хорошо себя вести...","soft","baseL",cheeks="blush")
        g9 "Я самый воспитанный профессор во всей школе!"
        call her_main("Конечно.","annoyed","angryL",cheeks="blush")
        call her_main("{size=-2}(По крайней мере, вы не самый худший...){/size}","annoyed","ahegao_raised",cheeks="blush")
        m "Спокойной ночи моя, [hermione_name]."
        call her_main("Спокойной ночи мой, [genie_name].","base","baseL",cheeks="blush")

        hide screen hermione_main
        call blkfade

        ">Ты прогоняешь Гермиону."
        ">Она без спешки снова одевается."

        call h_action("none") #Resets clothes.

        hide screen no_groping_laying_02
        pause 1

        $ b_her_tears = False

        show screen genie
        call her_chibi("stand","desk","base")
        call hide_blkfade

        call her_walk("desk","door",2.5)

        call her_head("{size=-4}(\"Мой любимый принц\"...){/size}","base","down_raised",cheeks="blush")
        call her_head("{size=-4}(Вряд ли он прекрасный принц, но.....){/size}","base","glance",cheeks="blush")
        call her_head("{size=-4}(Я сомневаюсь, что прекрасный принц мог трахнуть меня наполовину так же хорошо, как он может!){/size}","grin","ahegao_raised",cheeks="blush")
        call her_chibi("leave")

        $ v_tutoring = 14
        $ aftercum = False
        jump day_start




###UE CUSTOM THINGS
# Music
define ms_arabian_nights = "music/Arabian_Nights.mp3"
define ms_bushwick = "music/Bushwick_Tarantella_Loop.mp3"
define ms_croft_manor = "music/Croft_Manor.mp3"
define ms_dice_game = "music/Dice_Game.mp3"
define ms_gtkm = "music/Going_to_Kill_Me.mp3"
define ms_gorilla = "music/Gorilla_Theme.mp3"
define ms_india = "music/India's_Different.mp3"
define ms_jafar = "music/Jafar's_Hour.mp3"
define ms_kabul = "music/Kabul_Flight_Jumpstart.mp3"
define ms_manatees = "music/Music for Manatees.mp3"
define ms_marketplace = "music/Marketplace.mp3"
define ms_outlaw_star = "music/Outlaw_Star_Freedom.mp3"
define ms_ozone = "music/Ozone.ogg"
define ms_sleep_walking = "music/Sleep_Walking.mp3"
define ms_tension = "music/Tension.mp3"
define ms_the_calm_before = "music/The_Calm_Before.mp3"
define ms_the_eastern_wind = "music/The_Eastern_Wind.mp3"
define ms_the_kiss = "music/The_Kiss.mp3"
define ms_the_xfiles = "music/The_X-Files.mp3"
define ms_vision = "music/Vision.mp3"
# Sounds
define sd_boing1 = "sounds/boing.mp3"
define sd_boing2 = "sounds/boing02.mp3"
define sd_boing3 = "sounds/boing03.mp3"
define sd_burp = "sounds/burp.mp3"
define sd_door = "sounds/door.mp3"
define sd_door2 = "sounds/door2.mp3"
define sd_door3 = "sounds/door3.mp3"
define sd_fall = "sounds/fall.wav"
define sd_glitch = "sounds/gltch.mp3"
define sd_iris_run = "sounds/iris_run.mp3"
define sd_kungfupunch = "sounds/kung-fu-punch.mp3"
define sd_magic4 = "sounds/magic4.ogg"
define sd_monster = "sounds/mon.wav"
define sd_monster_dead = "sounds/mondead.wav"
define sd_pistol2 = "sounds/pistol2.mp3"
define sd_pop1 = "sounds/pop01.mp3"
define sd_pop2 = "sounds/pop02.mp3"
define sd_pop3 = "sounds/pop03.mp3"
define sd_punch1 = "sounds/punch01.mp3"
define sd_punch2 = "sounds/punch02.mp3"
define sd_rustling = "sounds/rustling.mp3"
define sd_scratch = "sounds/scratch.wav"
define sd_slap = "sounds/slap.mp3"
define sd_spit = "sounds/spit.mp3"
define sd_win2 = "sounds/win2.mp3"
# Screens
screen genie_and_hermione: #Genie sitting, Hermione stands right in front of him (behind the desk even).
    tag favor
    add "images/main_room/genie_and_hermione_01.png" at Position(xpos = table_position_x -84, ypos = 10)

screen groping_05:
    tag favor
    add "groping_05" at Position(xpos = table_position_x -84, ypos = 10)
    add "groping_05_blinking" at Position(xpos = table_position_x -84, ypos = 10)

screen groping_05b:
    tag favor
    add "groping_05b" at Position(xpos = table_position_x -84, ypos = 10)
    add "groping_05_blinking" at Position(xpos = table_position_x -84, ypos = 10)

screen no_groping_05:
    tag favor
    add "images/animation/grope_d_05.png" at Position(xpos = table_position_x -84, ypos = 10)
    add "groping_05_blinking" at Position(xpos = table_position_x -84, ypos = 10)

screen no_groping_05_desk:
    tag favor
    add "images/animation/grope_d_06.png" at Position(xpos = table_position_x -84, ypos = 10)

screen no_groping_06: #Facing Genie.
    tag favor
    add "images/animation/grope_e_05.png" at Position(xpos = table_position_x -84, ypos = 10)
    add "groping_06_blinking" at Position(xpos = table_position_x -84, ypos = 10)

screen groping_06:
    tag favor
    add "groping_06" at Position(xpos = table_position_x -84, ypos = 10)
    add "groping_06_blinking" at Position(xpos = table_position_x -84, ypos = 10)

screen groping_06b:
    tag favor
    add "groping_06b" at Position(xpos = table_position_x -84, ypos = 10)
    add "groping_06_blinking" at Position(xpos = table_position_x -84, ypos = 10)

screen no_groping_laying_01:
    tag favor
    add "images/animation/grope_laying_01.png" at Position(xpos = table_position_x -84, ypos = 10)

screen no_groping_laying_02:
    tag favor
    add "images/animation/grope_laying_b_01.png" at Position(xpos = table_position_x -84, ypos = 10)

screen scr_her_fingering_naked(speed="normal"):
    tag favor
    if speed == "slow":
        add "ani_her_fingering_slow_naked" at Position(xpos = table_position_x -84, ypos = 10)
    else:
        add "ani_her_fingering_naked" at Position(xpos = table_position_x -84, ypos = 10)
    add "ani_her_fingering_blinking" at Position(xpos = table_position_x -84, ypos = 10)

screen scr_her_sex(speed="normal"):
    tag favor
    if speed == "slow":
        add "ani_her_sex_slow_naked" at Position(xpos = table_position_x -84, ypos = 10)
    elif speed == "normal":
        add "ani_her_sex_naked" at Position(xpos = table_position_x -84, ypos = 10)
    elif speed == "fast":
        add "ani_her_sex_fast_naked" at Position(xpos = table_position_x -84, ypos = 10)

screen scr_her_sex_cum_outside(blink=0):
    tag favor
    add "ani_her_sex_cum_outside_naked" at Position(xpos = table_position_x -84, ypos = 10)

image groping_06: #Genie groping Hermione under her skirt. Hermione is facing Genie.
    "images/animation/grope_e_01.png"
    pause.2
    "images/animation/grope_e_02.png"
    pause.2
    "images/animation/grope_e_03.png"
    pause.5
    "images/animation/grope_e_02.png"
    pause.2
    "images/animation/grope_e_01.png"
    pause.2
    repeat

image groping_06b: #Genie groping Hermione under her skirt. Hermione is facing Genie.
    "images/animation/grope_e_01.png"
    pause.1
    "images/animation/grope_e_02.png"
    pause.1
    "images/animation/grope_e_03.png"
    pause.2
    "images/animation/grope_e_02.png"
    pause.1
    "images/animation/grope_e_01.png"
    pause.1
    repeat

image groping_06_blinking: #Animation of Hermione blinking her eyes.
    "images/animation/00.png"
    pause.1
    "images/animation/grope_e_04.png"
    pause.1
    "images/animation/00.png"
    pause 3
    "images/animation/grope_e_04.png"
    pause.1
    "images/animation/00.png"
    pause.1
    "images/animation/grope_e_04.png"
    pause.1
    "images/animation/00.png"
    pause 3
    repeat

image groping_05: #Genie groping Hermione under her skirt. Hermione is facing Genie.
    "images/animation/grope_d_01.png"
    pause.2
    "images/animation/grope_d_02.png"
    pause.2
    "images/animation/grope_d_03.png"
    pause.5
    "images/animation/grope_d_02.png"
    pause.2
    "images/animation/grope_d_01.png"
    pause.2
    repeat

image groping_05b: #Genie groping Hermione under her skirt. Hermione is facing Genie.
    "images/animation/grope_d_01.png"
    pause.1
    "images/animation/grope_d_02.png"
    pause.1
    "images/animation/grope_d_03.png"
    pause.2
    "images/animation/grope_d_02.png"
    pause.1
    "images/animation/grope_d_01.png"
    pause.1
    repeat

image groping_05_blinking: #Animation of Hermione blinking her eyes.
    "images/animation/00.png"
    pause.1
    "images/animation/grope_d_04.png"
    pause.1
    "images/animation/00.png"
    pause 3
    "images/animation/grope_d_04.png"
    pause.1
    "images/animation/00.png"
    pause.1
    "images/animation/grope_d_04.png"
    pause.1
    "images/animation/00.png"
    pause 3
    repeat

image ani_her_fingering_blinking: #Animation of Hermione blinking her eyes.
    "images/animation/00.png"
    pause.1
    "images/animation/grope_fingering_blink.png"
    pause.1
    "images/animation/00.png"
    pause 3
    "images/animation/grope_fingering_blink.png"
    pause.1
    "images/animation/00.png"
    pause.1
    "images/animation/grope_fingering_blink.png"
    pause.1
    "images/animation/00.png"
    pause 3
    repeat

image ani_her_fingering_slow_naked:
    "images/animation/grope_fingering_n_01.png"
    pause.3
    "images/animation/grope_fingering_n_02.png"
    pause.3
    "images/animation/grope_fingering_n_03.png"
    pause.3
    "images/animation/grope_fingering_n_04.png"
    pause.3
    repeat

image ani_her_fingering_naked:
    "images/animation/grope_fingering_n_01.png"
    pause.2
    "images/animation/grope_fingering_n_02.png"
    pause.2
    "images/animation/grope_fingering_n_03.png"
    pause.2
    "images/animation/grope_fingering_n_04.png"
    pause.2
    repeat

image ani_her_sex_slow_naked:
    "images/animation/21_sex_n_01.png"
    pause.15
    "images/animation/21_sex_n_02.png"
    pause.15
    "images/animation/21_sex_n_03.png"
    pause.15
    "images/animation/21_sex_n_04.png"
    pause.15
    "images/animation/21_sex_n_05.png"
    pause.15
    "images/animation/21_sex_n_06.png"
    pause.15
    "images/animation/21_sex_n_07.png"
    pause.15
    repeat

image ani_her_sex_naked:
    "images/animation/21_sex_n_01.png"
    pause.1
    "images/animation/21_sex_n_02.png"
    pause.1
    "images/animation/21_sex_n_03.png"
    pause.1
    "images/animation/21_sex_n_04.png"
    pause.1
    "images/animation/21_sex_n_05.png"
    pause.1
    "images/animation/21_sex_n_06.png"
    pause.1
    "images/animation/21_sex_n_07.png"
    pause.1
    repeat

image ani_her_sex_fast_naked:
    "images/animation/21_sex_n_01.png"
    pause.05
    "images/animation/21_sex_n_02.png"
    pause.05
    "images/animation/21_sex_n_03.png"
    pause.05
    "images/animation/21_sex_n_04.png"
    pause.05
    "images/animation/21_sex_n_05.png"
    pause.05
    "images/animation/21_sex_n_06.png"
    pause.05
    "images/animation/21_sex_n_07.png"
    pause.05
    repeat

image ani_her_sex_cum_outside_naked:
    "images/animation/22_cum_n_01.png"
    pause.1
    "images/animation/22_cum_n_02.png"
    pause.1
    "images/animation/22_cum_n_03.png"
    pause.1
    "images/animation/22_cum_n_04.png"
    pause.1
    "images/animation/22_cum_n_05.png"
    pause.1
    "images/animation/22_cum_n_06.png"
    pause.1
    "images/animation/22_cum_n_07.png"
    pause.1
    "images/animation/22_cum_n_08.png"
    pause.1
    "images/animation/22_cum_n_09.png"
    pause.1
    "images/animation/22_cum_n_10.png"
    pause.1
    "images/animation/22_cum_n_11.png"
    pause.1
    "images/animation/22_cum_n_12.png"
    pause.1
    "images/animation/22_cum_n_13.png"
    pause.1
    "images/animation/22_cum_n_14.png"
    pause.1
    "images/animation/22_cum_n_15.png"
    pause.1
    "images/animation/22_cum_n_16.png"
    pause.1
    "images/animation/22_cum_n_17.png"
    pause.1
    "images/animation/22_cum_n_18.png"
    pause.1
    "images/animation/22_cum_n_19.png"
    pause 2
    "images/animation/22_cum_n_20.png"
    pause.1
    "images/animation/22_cum_n_21.png"
    pause.1
    "images/animation/22_cum_n_22.png"
    pause.1
    "images/animation/22_cum_n_23.png"
    pause.1
    repeat
