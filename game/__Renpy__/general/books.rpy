label __init_variables:
    if not hasattr(renpy.store,'Copper_Book_OBJ'): #important!
        $ Copper_Book_OBJ = educational_book()
    $ Copper_Book_OBJ.id = "Copper_Book"
    $ Copper_Book_OBJ.name = "\"Медная книга духа\""
    $ Copper_Book_OBJ.effect = ">Новый навык разблокирован: шанс 1 из 3, возможность завершения дополнительной главы при чтении."
    $ Copper_Book_OBJ.chapters = 2
    $ Copper_Book_OBJ.book_description = "\nЭта книга содержит различные советы по скорочтению. " + str(Copper_Book_OBJ.chapters) + " главы."
    $ Copper_Book_OBJ.cost = 40
    $ Copper_Book_OBJ.picture = "images/store/books/1-8.png"
    
    if not hasattr(renpy.store,'Bronze_Book_OBJ'): #important!
        $ Bronze_Book_OBJ = educational_book()
    $ Bronze_Book_OBJ.id = "Bronze_Book"
    $ Bronze_Book_OBJ.name = "\"Бронзовая книга духа\""
    $ Bronze_Book_OBJ.effect = ">Новый навык разблокирован: шанс 2 из 3, возможность завершения дополнительной главы при чтении." 
    $ Bronze_Book_OBJ.chapters = 4
    $ Bronze_Book_OBJ.book_description = "\nЭта книга содержит различные советы по скорочтению. "  + str(Bronze_Book_OBJ.chapters) + " главы."
    $ Bronze_Book_OBJ.cost = 60
    $ Bronze_Book_OBJ.picture = "images/store/books/1-8.png"
    
    if not hasattr(renpy.store,'Silver_Book_OBJ'): #important!
        $ Silver_Book_OBJ = educational_book()
    $ Silver_Book_OBJ.id = "Silver_Book"
    $ Silver_Book_OBJ.name = "\"Серебряная книга духа\""
    $ Silver_Book_OBJ.chapters = 6
    $ Silver_Book_OBJ.book_description = "\nЭта книга содержит различные советы по скорочтению. " + str(Silver_Book_OBJ.chapters) + " глав."
    $ Silver_Book_OBJ.effect = ">Новый навык разблокирован: всегда завершаешь дополнительную главу при чтении."
    $ Silver_Book_OBJ.cost = 80
    $ Silver_Book_OBJ.picture = "images/store/books/1-8.png"
    
    if not hasattr(renpy.store,'Golden_Book_OBJ'): #important!
        $ Golden_Book_OBJ = educational_book()
    $ Golden_Book_OBJ.id = "Golden_Book"
    $ Golden_Book_OBJ.name = "\"Золотая книга духа\""
    $ Golden_Book_OBJ.chapters = 8
    $ Golden_Book_OBJ.book_description = "\nЭта книга содержит различные советы по скорочтению. " + str(Golden_Book_OBJ.chapters) + " глав."
    $ Golden_Book_OBJ.effect = ">Ты овладел своим духом, и с этого момента ты всегда можешь завершить две дополнительные главы при чтении."
    $ Golden_Book_OBJ.cost = 160
    $ Golden_Book_OBJ.picture = "images/store/books/1-8.png"
        
    
    if not hasattr(renpy.store,'Speedwriting_Beginners_OBJ'): #important!
        $ Speedwriting_Beginners_OBJ = educational_book()
    $ Speedwriting_Beginners_OBJ.id = "Speedwriting_Beginners"
    $ Speedwriting_Beginners_OBJ.name = "\"Скорописание для чайников\""
    $ Speedwriting_Beginners_OBJ.chapters = 2
    $ Speedwriting_Beginners_OBJ.book_description = "\nЭта книга содержит массу основных методов, используемых для улучшения способности быстро писать. " + str(Speedwriting_Beginners_OBJ.chapters) + " главы."
    $ Speedwriting_Beginners_OBJ.effect = ">Новый навык разблокирован: шанс 1 к 3, возможность заполнения дополнительной главы при оформлении документов."
    $ Speedwriting_Beginners_OBJ.cost = 90
    $ Speedwriting_Beginners_OBJ.picture = "images/store/books/1-8.png"
    
    if not hasattr(renpy.store,'Speedwriting_Amateurs_OBJ'): #important!
        $ Speedwriting_Amateurs_OBJ = educational_book()
    $ Speedwriting_Amateurs_OBJ.id = "Speedwriting_Amateurs"
    $ Speedwriting_Amateurs_OBJ.name = "\"Скорописание для начинающих\""
    $ Speedwriting_Amateurs_OBJ.chapters = 4
    $ Speedwriting_Amateurs_OBJ.book_description = "\nЭта книга содержит промежуточные методы, используемые для улучшения способности быстро писать. " + str(Speedwriting_Amateurs_OBJ.chapters) + " главы."
    $ Speedwriting_Amateurs_OBJ.effect = ">Новый навык разблокирован: шанс 2 к 3, возможность заполнения дополнительной главы при оформлении документов."
    $ Speedwriting_Amateurs_OBJ.cost = 110
    $ Speedwriting_Amateurs_OBJ.picture = "images/store/books/1-8.png"
    
    if not hasattr(renpy.store,'Speedwriting_Advanced_OBJ'): #important!
        $ Speedwriting_Advanced_OBJ = educational_book()
    $ Speedwriting_Advanced_OBJ.id = "Speedwriting_Advanced"
    $ Speedwriting_Advanced_OBJ.name = "\"Скорописание для любителей\""
    $ Speedwriting_Advanced_OBJ.chapters = 6
    $ Speedwriting_Advanced_OBJ.book_description = "\nЭта книга содержит передовые методы, используемые для улучшения способности быстро писать. " + str(Speedwriting_Advanced_OBJ.chapters) + " глав."
    $ Speedwriting_Advanced_OBJ.effect = ">Новый навык разблокирован: всегда заполняешь дополнительную главу при оформлении документов."
    $ Speedwriting_Advanced_OBJ.cost = 130
    $ Speedwriting_Advanced_OBJ.picture = "images/store/books/1-8.png"
    
    if not hasattr(renpy.store,'Speedwriting_Experts_OBJ'): #important!
        $ Speedwriting_Experts_OBJ = educational_book()
    $ Speedwriting_Experts_OBJ.id = "Speedwriting_Experts"
    $ Speedwriting_Experts_OBJ.name = "\"Скорописание для продвинутых\""
    $ Speedwriting_Experts_OBJ.chapters = 8
    $ Speedwriting_Experts_OBJ.book_description = "\nЭта книга содержит экспертные методы, используемые для улучшения способности быстро писать. " + str(Speedwriting_Experts_OBJ.chapters) + " глав."
    $ Speedwriting_Experts_OBJ.effect = ">Ты стал настоящим мастером скорописания и отныне всегда заполняешь две дополнительные главы, при заполнении документов."
    $ Speedwriting_Experts_OBJ.cost = 150
    $ Speedwriting_Experts_OBJ.picture = "images/store/books/1-8.png"
        
    
    if not hasattr(renpy.store,'Galadriel_I_OBJ'): #important!
        $ Galadriel_I_OBJ = fiction_book()
    $ Galadriel_I_OBJ.id = "Galadriel_I"
    $ Galadriel_I_OBJ.name = "\"Сказка о Галадриэль. Том I.\""
    $ Galadriel_I_OBJ.book_description = "Эта книга рассказывает историю эльфийской принцессы, которая бросает вызов традициям своего народа и решает создать свою собственную судьбу. Или это не так? " + str(Galadriel_I_OBJ.chapters / 2) + " глав."
    $ Galadriel_I_OBJ.effect = ">Твое воображение улучшилось."
    $ Galadriel_I_OBJ.chapters = 20
    $ Galadriel_I_OBJ.cost = 100
    $ Galadriel_I_OBJ.picture = "images/store/books/9.png"
    
    if not hasattr(renpy.store,'Galadriel_II_OBJ'): #important!
        $ Galadriel_II_OBJ = fiction_book()
    $ Galadriel_II_OBJ.id = "Galadriel_II"
    $ Galadriel_II_OBJ.name = "\"Сказка о Галадриэль. Том II.\""
    $ Galadriel_II_OBJ.book_description = "Эта книга рассказывает историю эльфийской принцессы, которая бросает вызов традициям своего народа и решает создать свою собственную судьбу. Или это не так? "  + str(Galadriel_II_OBJ.chapters / 2) + " глав."
    $ Galadriel_II_OBJ.effect = ">Твое воображение улучшилось."
    $ Galadriel_II_OBJ.chapters = 20
    $ Galadriel_II_OBJ.cost = 200
    $ Galadriel_II_OBJ.picture = "images/store/books/10.png"
    
    if not hasattr(renpy.store,'Armchairs_OBJ'): #important!
        $ Armchairs_OBJ = fiction_book()
    $ Armchairs_OBJ.id = "Armchairs"
    $ Armchairs_OBJ.name = "\"Игра, вокруг Кресла\""
    $ Armchairs_OBJ.book_description = "Эпическая история о предательстве, убийстве и изнасиловании. Затем еще об одном убийстве, еще одном предательстве и еще о нескольких изнасилованиях. " + str(Armchairs_OBJ.chapters / 2) + " глав."
    $ Armchairs_OBJ.effect = ">Твое воображение улучшилось."
    $ Armchairs_OBJ.chapters = 20
    $ Armchairs_OBJ.cost = 250
    $ Armchairs_OBJ.picture = "images/store/books/11.png"
    
    if not hasattr(renpy.store,'Dear_Wifu_OBJ'): #important!
        $ Dear_Wifu_OBJ = fiction_book()
    $ Dear_Wifu_OBJ.id = "Dear_Wifu"
    $ Dear_Wifu_OBJ.name = "\"Моя дорогая Waifu\""
    $ Dear_Wifu_OBJ.book_description = "{size=-4}BY AKABUR{/size}\n" "Вновь переживите славу своих дней средней школы. Ваша сводная сестра Ши, учитель г-жа Стивенс или таинственная девочка из библиотеки? Кто станет вашей \"waifu\"? " + str(Dear_Wifu_OBJ.chapters) + " глав."
    $ Dear_Wifu_OBJ.effect = ">Твое воображение улучшилось."
    $ Dear_Wifu_OBJ.chapters = 20
    $ Dear_Wifu_OBJ.cost = 300
    $ Dear_Wifu_OBJ.picture = "images/store/books/12.png"
    
    
    $ Galadriel_I_OBJ.chapter_description = [
         "Повествуется о Галадриэли - нежной и доброй эльфийской принцессе.",
         "Повествуется об отце Галадриэли - Короле Метисе и его друге детства - Мофоселисе.",
         "Король Метис объявляет о помолвке своей дочери, принцессы Галадриэль с канцлером Мофоселисом.",
         "Галадриэль отказывается выйти замуж за человека, который в три раза старше ее и которого, до этой поры, она считала своим дядей.",
         "Король Метис не слушает \"глупые\" жалобы дочери. Галадриэль решает бежать.",
         "Галадриэль удается покинуть королевские покои ночью ...",
         "Король Метис в ярости из-за побега дочери. Он решает лично возглавить поиски.",
         "Галадриэль едет на своей кобыле \"Белая голубка\" через лес. Принцесса наслаждается свободой... Вскоре она встречает всадника - весьма приятного человеческого дворянина...",
         "Галадриэль едет вместе с дворянином. Они обмениваются шутками, и он очень забавляет ее. Вдруг дворянин нападает на принцессу и сильным ударом лишает сознания!...",
         "Галадриэль приходит в себя. Она с ужасом чувствует, что дворянин входит в нее. Галадриэль зовет на помощь, но красавчик крепко держит ее и жестоко насилует.",
         "Галадриэль безуспешно пытается вырваться. И тут она замечает, что ее окружает полдюжины мужчин, которые злобно ухмыляются.",
         "После того, как дворянин заканчивает с Галадриэль, его люди пускают эльфийскую принцессу по кругу. Галадриэль плачет и умоляет их прекратить.",
         "Галадриэль приходит в себя в клетке на каком-то рынке. Ее руки связаны, ее благородные одежды разорваны в клочья, а волосы полны веток и сухой спермы.",
         "Жирный, богатый мужчина покупает Галадриэль и приводит ее в свой дом. Принцесса больше не плачет. Она счастлива выбраться из клетки.",
         "Галадриэль позволили принять ванну, после чего прислуга приносит ей чистую одежду и еду.",
         "Галадриэль начинает надеяться, что ее беды позади, но это не так. Вскоре она понимает, что это место - бордель.",
         "Эльфийская принцесса вынуждена работать шлюхой. Она ненавидит свою новую жизнь, но у нее не остается выбора.",
         "Галадриэль быстро набирает популярность. Люди, Темные Эльфы и даже карлики, она раздвигает ноги для всех.",
         "Слава о молодой и красивой эльфийской шлюхе распространяется по окрестностям. Галадриэль принимает свою новую жизнь в борделе.",
         "Но внезапно все резко меняется. Галадриэль узнает, что она беременна. - Конец первой книги -"
    ]

    $ Galadriel_II_OBJ.chapter_description = [
         "Галадриэль беременна уже несколько месяцев. К удивлению принцессы, ее популярность растет, как будто в прямой зависимости от размера ее живота.",
         "Хотя Галадриэль и ведет себя, как послушная шлюха, на самом деле, она продумывает побег из борделя.",
         "Эльфийская принцесса - шлюха ничего не знает о жизни за стенами борделя. Но это не влияет на ее решимость спастись.",
         "Планирование побега из борделя занимает много времени, но в конце-концов Галадриэль удается бежать.",
         "Галадриэль теряется в огромном городе и вынуждена провести ночь на улице.",
         "На улицах трудно найти еду. Галадриэль борется со стаей бродячих собак, и одна из них кусает Галадриэль за руку.",
         "Беременная Галадриэль предлагает составить компанию паре грязных бездомных мужчин в обмен на еду. С ними она проводит ночи.",
         "Галадриэль понимает, что ее жизнь в борделе была раем по сравнению с тем, что она имеет теперь. Она решает вернуться обратно.",
         "Владелец Галадриэль - жирный, богатый человек не наказывает Галадриэль за побег. Наоборот, он счастлив, что одна из его самых популярных девушек вернулась.",
         "Галадриэль снова в тепле и чистоте, ее хорошо кормят. Она рада, что вернулась и популярна, как никогда.",
         "Галадриэль обслуживает клиентов на протяжении всей беременности. Ребенок вот-вот родится...",
         "Богатый человек в маске заказывает Галадриэль на весь день. Лениво ублажая клиента, Галадриэль гадает кто бы это мог быть.",
         "Таинственный человек целый день развлекается с Галадриэль. Из наполненных грудей принцессы капает молоко, в то время, как человек трахает ее.",
         "Человек в маске кончает на лицо Галадриэль во второй раз за сегодня. Затем он решает снять маску и показать лицо.",
         "Галадриэль обнаруживает, что этот человек - ее отец, король Метис. Только тут и он понимает, что беременная шлюха, которую он трахал несколько часов - его дочь.",
        # Only now he realizes that the pregnant whore he fucked for hours is his daughter.
         "Он обнимает свое потерявшее дар речи дитя. Глаза Галадриэль пусты. Сперма отца капает с ее лица...",
         "Галадриэль в ужасе кричит. К ее удивлению, она обнаруживает себя в королевских покоях, в своей постели.",
         "Проходит несколько минут, пока она понимает, что она никогда не была беременна. Все приключения - это лишь сон.",
         "Галадриэль бросается к отцу и обнимает его. Девушка пережила слишком многое в \"прошлой жизни\". Она счастлива и соглашается выйти замуж за канцлера Мофоселиса.",
         "{size=-1}Галадриэль стоит у алтаря. Она довольна и счастлива. Вдруг она замечает нечто, что наполняет ее сердце ужасом. На ее руке - шрам. Место укуса собаки. - Конец -{/size}"
    ]
    
    $ Armchairs_OBJ.chapter_description = [
        "Семейство благородных северян.",
        "Королевская семья и король.",
        "Другое семейство.",
        "Инцест между братом и его сестрой - королевой.",
        "Покушение на ребенка. Он чудом выживает, но находится в коме.",
        "Другие персонажи.",
        "Одни персонажи строят козни против других.",
        "Короля отравили и он умирает. Еще несколько инцестов между братом и сестрой.",
        "Казнили некоторых персонажей, за которых вы болели.", 
        "Появилось несколько новых персонажей.",
        "Некоторые женщины были изнасилованы и жестоко убиты.",
        "Еще несколько членов дворянской семьи северян безвременно почили.",
        "Еще больше женщин изнасилованы. Некоторым из них удается выжить. (Разумеется, чтобы их изнасиловали чуть позже).",
        "Персонажи, которых вы ненавидите сталкиваются в эпической битве против персонажей, за которых вы болеете.",
        "Большинство персонажей, которых вы ненавидите пережили сражение. Все, за кого вы болели, мертвы.",
        "Еще несколько изнасилований и убийств... (Вас это уже не трогает...)",
        "Новые персонажи появляются в истории. Вы, вроде, начинаете болеть за одного из них.",
        "Персонаж, за которого вы болеете, влюбляется в милую девушку.",
        "Персонаж, за которого вы болели, зверски убит. Его девушку насилуют и тоже убивают.",
        "Новая раса наполовину замороженной нежити включается в историю. Продолжение следует..."
    ]
    
    
    $ Books_OBJ = silver_book_lib()
    $ Books_OBJ.read_books.extend([
        Copper_Book_OBJ,
        Bronze_Book_OBJ,
        Silver_Book_OBJ,
        Golden_Book_OBJ
    ])
    $ Books_OBJ.write_books.extend([
        Speedwriting_Beginners_OBJ,
        Speedwriting_Amateurs_OBJ,
        Speedwriting_Advanced_OBJ,
        Speedwriting_Experts_OBJ
    ])
    $ Books_OBJ.fiction_books.extend([
        Galadriel_I_OBJ,
        Galadriel_II_OBJ,
        Armchairs_OBJ,
        Dear_Wifu_OBJ
    ])
    
    if not hasattr(renpy.store,'cheat_reading'): #important!
        $ cheat_reading = False
    if not hasattr(renpy.store,'books'): #important!
        $ books = []
    
    ### GENIE STATS ###============================
    if not hasattr(renpy.store,'imagination'): #important!
        $ imagination = 1 #+1 for every completed book. Unlocks new sexual favors to buy. 1 point of imagination = 1 level of whoring.
    if not hasattr(renpy.store,'concentration'): #important!
        $ concentration = 0 #+1 for every completed book on concentration. Pops up during paperwork.
    if not hasattr(renpy.store,'speedwriting'): #important!
        $ speedwriting = 0 #+1 for every completed book on speedwriting. Pops up during paperwork.
    if not hasattr(renpy.store,'s_reading_lvl'): #important!
        $ s_reading_lvl = 0
    
    return


label books_list:
    menu:
        "-Образовательные книги-":
            label books_on_improvement:
            $ books_menu_list = Books_OBJ.get_edu()
        "-Художественная литература-":
            label fiction_books_menu:
            $ books_menu_list = Books_OBJ.get_fic()
        "-Назад-":
            jump desk
    python:
        books_menu = []
        for book in books_menu_list:
            if book.purchased:
                if book.done:
                    books_menu.append((book.getMenuTextDone(),book))
                else:
                    books_menu.append((book.getMenuText(),book))
        books_menu.append(("-Назад-", "nvm"))
        BookOBJ = renpy.display_menu(books_menu)
    if BookOBJ == "nvm":
        jump books_list
    else:
        jump handle_book_selection
    
    
label handle_book_selection:
    $ the_gift = BookOBJ.picture
    show screen gift
    with d3
    "[BookOBJ.book_description]"
    if BookOBJ.done:
        if BookOBJ.id == "Armchairs":
            m "Почему Я хочу сделать это с собой снова?"
        else:
            ">Ты уже закончил это дело."
        hide screen gift
    else:
        menu:
            "-Прочитать книгу-":
                hide screen gift
                jump check_book_order
            "-Неважно-":
                hide screen gift
    if BookOBJ in Books_OBJ.get_edu():
        jump books_on_improvement
    if BookOBJ in Books_OBJ.get_fic():
        jump fiction_books_menu
    else:
        jump books_list
    

label check_book_order:
    if BookOBJ in Books_OBJ.read_books:
        if (BookOBJ.id == "Copper_Book") or (BookOBJ.id == "Bronze_Book" and Books_OBJ.isDone("Copper_Book")) or (BookOBJ.id == "Silver_Book" and Books_OBJ.isDone("Bronze_Book")) or (BookOBJ.id == "Golden_Book" and Books_OBJ.isDone("Silver_Book")):
            jump reading_book
    
    if BookOBJ in Books_OBJ.write_books:
       if (BookOBJ.id == "Speedwriting_Beginners") or (BookOBJ.id == "Speedwriting_Amateurs" and Books_OBJ.isDone("Speedwriting_Beginners")) or (BookOBJ.id == "Speedwriting_Advanced" and Books_OBJ.isDone("Speedwriting_Amateurs")) or (BookOBJ.id == "Speedwriting_Experts" and Books_OBJ.isDone("Speedwriting_Advanced")):
            jump reading_book
    
    if BookOBJ in Books_OBJ.fiction_books:
        if (BookOBJ.id == "Galadriel_II" and Books_OBJ.isDone("Galadriel_I")):
            jump reading_book
        elif BookOBJ.id != "Galadriel_II":
            jump reading_book
    
    m "Чтение книг не по порядку не принесет мне никакой пользы."

    jump books_list
    
    
label reading_book:
    stop music fadeout 2.0
    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    if fire_in_fireplace:
        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    if daytime and not raining and not fire_in_fireplace:
        play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    if not daytime and not raining and not fire_in_fireplace:
        play bg_sounds "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        
    if fire_in_fireplace:   #Shows Genie reading a book near the fireplace.
        hide screen chair_right
        hide screen genie
        show screen reading_near_fire
        with Dissolve(0.3)
    else:                   #Shows Genie reading a book near the window.
        hide screen chair_right
        hide screen genie
        show screen reading
        with Dissolve(0.3)
    
    if raining:
        ">Ты читаешь книгу под названием [BookOBJ.name], под шум дождя, барабанящего по крыше башни."
    else:
        ">Ты читаешь книгу [BookOBJ.name]..."

    if cheat_reading:
        if BookOBJ in Books_OBJ.get_edu():
            $ BookOBJ.progress = BookOBJ.chapters
        elif BookOBJ in Books_OBJ.get_fic():
            label cheat_reading_loop:
                call read_chapter 
                if BookOBJ.progress < BookOBJ.chapters:
                    jump cheat_reading_loop
        jump book_complete
    else:
        call read_book 

        if _return == "DONE":
            jump book_complete

        call book_speed_check 
        $ speed_check = _return
        if speed_check >= 1:
            if s_reading_lvl == 1:
                ">Реализуя некоторые трюки, которые ты подчерпнул из \"Скорочтения для чайников\", тебе позволяют сэкономить время и продолжить чтение."
            if s_reading_lvl == 2:
                ">Внедрение техники скорочтения позволяет сэкономить время и продолжить чтение."
            if s_reading_lvl == 3:
                ">Внедрение техники скорочтения позволяет еще больше сэкономить время и дальше продолжить чтение."
            if s_reading_lvl > 3:
                ">Внедрение передовых методов быстрого чтения, позволяет тебе буквально пролистывать книгу и улавливать смысл на лету."
            call read_book 

        if _return == "DONE":
            jump book_complete
        
        if speed_check == 2:
            call read_book 

        if _return == "DONE":
            jump book_complete

        if raining:
            if not fire_in_fireplace:
                ">Барабанящий дождь за окном успокаивает тебя, ты отлично себя чувствуешь, продолжая читать книгу..."
                ">Ты пытаешься продолжить читать, но вскоре понимаешь, что воздух в комнате становится невыносимо слишком влажный."
            else:
                ">Барабанящий дождь за окном успокаивает тебя, и ты отлично себя чувствуешь, продолжая читать книгу..."
                call read_book 

        if _return == "DONE":
            jump book_complete

        ">Осталось еще несколько глав."
    
    if fire_in_fireplace:
        show screen done_reading_near_fire
        hide screen reading_near_fire
    else:
        show screen done_reading  
        hide screen reading
    
    if daytime:
        jump night_start
    else: 
        jump day_start
    
    
label book_speed_check:
    if s_reading_lvl == 1: #33% chance
        if renpy.random.randint(1, 3) == 1: #Success.
            return 1
    if s_reading_lvl == 2: #66% chance
        if renpy.random.randint(1, 3) > 1: #Success.
            return 1
    if s_reading_lvl == 3: #100% chance
        return 1
    if s_reading_lvl > 3: #Double 100% chance
        return 2
    return 0
    


label read_book:
    if BookOBJ.progress >= BookOBJ.chapters:
        return "DONE" #prevents cases where book is done but read_book was called
    call read_chapter 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    if BookOBJ in Books_OBJ.get_edu():
        $ renpy.say(None,">Ты закончил \"главу [BookOBJ.progress]\" этой книги.")
    if BookOBJ in Books_OBJ.get_fic():
        $ renpy.say(None,">Ты закончил \"главу "+str(BookOBJ.progress/2)+"\" этой книги.")
    if BookOBJ.progress >= BookOBJ.chapters:
        return "DONE" #this is here to indicate completeing a book without escapeing the call otherwise renpy would treat a jump or call as a recursive action
    return
    
    
label read_chapter:
    $ BookOBJ.progress += 1 
    if BookOBJ in Books_OBJ.get_fic():
        if BookOBJ.id == "Dear_Wifu":
            call waifu 
        else:
            $tmp_desc = BookOBJ.getChapterDesc()
            "[tmp_desc]"
            if BookOBJ.progress < BookOBJ.chapters:
                $ BookOBJ.progress += 1
                $tmp_desc = BookOBJ.getChapterDesc()
                "[tmp_desc]"
    return


label book_complete:
    if fire_in_fireplace:
        show screen done_reading_near_fire
    else:
        show screen done_reading

    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">Это была последняя глава, ты закончил всю книгу."
    if BookOBJ.id == "Dear_Wifu":
        jump waifu_completed
    if BookOBJ.id == "Armchairs":
        g4 "Что за херня! Я ненавижу человека, который это написал!"
        m "Впрочем, все эти изнасилования натолкнули меня на пару идей..."
    
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    "[BookOBJ.effect]" # ex. ">New skill unlocked: a 1 out of 6 chance of completing an additional chapter when doing paperwork.."
        
    if BookOBJ in Books_OBJ.fiction_books:
        $ imagination += 1
    if BookOBJ in Books_OBJ.read_books:
        $ s_reading_lvl += 1
    if BookOBJ in Books_OBJ.write_books:
        $ speedwriting += 1
        $ concentration += 1
    
    $ BookOBJ.done = True

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading
    
    if daytime:
        jump night_start
    else: 
        jump day_start
    
    
init python:
    class silver_book_lib(object):
        read_books = []
        write_books = []
        fiction_books = []
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
        
        def get_all(self):
            all_books = []
            all_books.extend(self.read_books)
            all_books.extend(self.write_books)
            all_books.extend(self.fiction_books)
            return all_books
        def get_edu(self):
            edu_books = []
            edu_books.extend(self.read_books)
            edu_books.extend(self.write_books)
            return edu_books
        def get_fic(self):
            return self.fiction_books
            
        
        def purchase(self, id=""):
            for book in self.get_all():
                if book.id == id:
                    book.purchased = True
        
        def get_purchased(self):
            purchased_books = []
            for book in self.get_all():
                if book.purchased:
                    purchased_books.append(book)
            return purchased_books
        
        def isDone(self, id=""):
            for book in self.get_all():
                if book.id == id:
                    return book.done
            return None

    class silver_book(object):
        id = ""
        cost = 0
        chapters = 0
        progress = 0
        done = False
        purchased = False
        name = ""
        effect = ""
        book_description = ""
        picture = ""
        def __repr__(self):
            return self.id
        def getMenuText(self):
            return "-"+str(self.name)+"-"
        def getMenuTextDone(self):
            return "-"+str(self.name)+"-{image=check_08}"
        def getStoreMenuText(self):
            return "-"+str(self.name)+"- ("+str(self.cost)+" g.)"
        def getMenuTextPurchased(self):
            return "{color=#858585}-"+str(self.name)+"- ("+str(self.cost)+" g.){/color}"

    class educational_book(silver_book):
        pass
    
    class fiction_book(silver_book):
        chapter_description = []
        def getChapterDesc(self):
           return self.chapter_description[self.progress-1] #"Chapter "+str(self.progress)+": "+
           
           
