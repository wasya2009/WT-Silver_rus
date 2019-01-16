

### Hermione Chitchats ###

label chit_chat:
    #$ one_of_ten = renpy.random.randint(1, 10) #Generating one number out of three for various porpoises.


    ### WHORING LEVEL 01 ###
    if whoring >= 0 and whoring <= 2:
        if one_of_ten == 1:
            call her_main("Может быть, если бы я работала усерднее, я смогла бы втиснуть еще несколько занятий в свое расписание...","open","angryCl")
            call her_main("","normal","base")

        elif one_of_ten == 2:
            call her_main("Фактически, я не против того, чтобы называться \"мисс-всезнайка\".","open","angryCl")
            her "Я думаю, это довольно лестно..."
            call her_main("","normal","base")

        elif one_of_ten == 3:
            call her_main("Василиск, также известный как царь змей.","open","angryCl")
            her "Херпо Фол первым вывел василиска."
            her "Он добился этог--"
            call her_main("Простите, профессор, завтра у нас еще один тест...","open","worriedL")
            her "Я просто хочу убедиться, что я готова..."
            call her_main("","base","base")

        elif one_of_ten == 4:
            call her_main("Если бы мое тело не требовало сна...","open","worriedL")
            call her_main("Я бы смогла уделять учебе в два раза больше времени?!","angry","wide")
            call her_main("Интересно, есть ли заклинание для этого...","open","base")
            call her_main("","normal","base")

        elif one_of_ten == 5:
            call her_main("До сих пор профессор Трелони не научила меня ни одному фундаментальному знанию, сэр.","open","angryCl")
            call her_main("","normal","base")

        elif one_of_ten == 6:
            call her_main("Хотелось бы, чтобы больше студентов были честными, ответственными и старательными, как я.","open","angryCl")
            call her_main("","normal","base")

        elif one_of_ten == 7:
            call her_main("Как могут некоторые люди быть настолько невежественны к проблемам мира?","open","angryCl")
            her "Лично я считаю, что каждый из нас должен приложить больше усилий, чтобы сделать наш мир лучше."
            call her_main("","normal","base")

        elif one_of_ten == 8:
            call her_main("В последнее время шел сильный дождь...","open","worriedL")
            call her_main("","base","base")

        elif one_of_ten == 9:
            call her_main("Мало кто знает об этом...","open","worriedL")
            call her_main("...но я очень люблю шоколад.","base","base")
            call her_main("","base","base")

        elif one_of_ten == 10:
            call her_main("Извините, сэр, но у меня нет времени на пустые разговоры...","base","base")
            call her_main("","normal","base")


    ### WHORING LEVEL 02 ###
    if whoring >= 3 and whoring <= 5:
        if one_of_ten == 1:
            call her_main("Я где-то читала, что полнолуние часто облегчает концентрацию на задаче...","open","angryCl")
            call her_main("","normal","base")

        elif one_of_ten == 2:
            call her_main("Я люблю свернуться калачиком у камина во время ливня с хорошей книгой...","base","base")
            call her_main("","base","base")

        elif one_of_ten == 3:
            call her_main("В последнее время в школе ходит своеобразный слух о профессоре Снейпе...","open","worriedL")
            call her_main("Нет, наверное, не стоит...","soft","base")
            call her_main("","normal","base")

        elif one_of_ten == 4:
            call her_main("Несмотря на сомнительный характер услуг, которые вы покупаете у меня в последнее время, сэр...","open","angryCl")
            her "Я благодарна вам за помощь..."
            call her_main("Гриффиндор нуждается в этих очках сейчас больше, чем когда-либо...","annoyed","frown")
            call her_main("","normal","base")

        elif one_of_ten == 5:
            call her_main("Почему Квиддич так популярен среди девушек - это просто за пределами моего понимания...","open","angryCl")
            call her_main("","normal","base")

        elif one_of_ten == 6:
            call her_main("Наше \"Движение за Права Мужчин\" неуклонно набирает популярность.","open","angryCl")
            her "Очень приятно знать, что вы помогаете улучшать наше общество."
            call her_main("","normal","base")

        elif one_of_ten == 7:
            call her_main("Школьная библиотека Хогвартса считается довольно обширной...","open","angryCl")
            call her_main("Однако, я хочу, чтобы она стала еще больше...","open","suspicious")
            call her_main("","normal","base")

        elif one_of_ten == 8:
            call her_main("Как один из лучших учеников в этой школе, я должна поддерживать репутацию...","open","worriedL")
            her "Люди смотрят на меня..."
            call her_main("...так что, ваше благоразумие очень ценится, сэр.","open","base")
            call her_main("","annoyed","worriedL")

        elif one_of_ten == 9:
            call her_main("Эта услуга, которую я вам продала, сэр...","open","worried")
            call her_main(".......","normal","worriedCl")
            call her_main("Я согласилась только потому, что нужды моего факультета всегда на первом месте.","open","down")
            call her_main("Я просто хотела, чтобы вы это знали, сэр...","upset","closed")

        elif one_of_ten == 10:
            call her_main("До \"Осеннего Балла\" еще несколько месяцев...","open","angryCl")
            call her_main("Но некоторые девушки уже обсуждают, какое платье они собираются надеть...","open","worried")
            call her_main("","annoyed","annoyed")


    ### WHORING LEVEL 03 ###
    if whoring >= 6 and whoring <= 8:
        if one_of_ten == 1:
            call her_main("Помните, когда вы впервые попросили меня показать вам мои трусики, сэр?","open","angryCl")
            her "Тогда, я была так зла, на вас..."
            call her_main("Теперь я вижу, что я просто был эгоисткой...","annoyed","frown")
            her "В конце концов, на кону честь моего факультета..."
            call her_main("И это будет моей единственной заботой!","normal","frown")

        elif one_of_ten == 2:
            call her_main("Скорость, с которой факультет Слизерина набирает очки в последнее время, просто неимоверна.","open","angryCl")
            call her_main("Думаю, за этим стоит профессор Снейп.","angry","angry")
            call her_main("Вы должны разобраться с этим, сэр.","open","angryCl")
            call her_main("","normal","base")

        elif one_of_ten == 3:
            call her_main("Яйца Ashwinder'а(огневицы), шипы розы, Лунный камень...","open","worriedL")
            call her_main("А? Я снова думаю вслух?","open","worried")
            call her_main("Прошу прощения...","grin","worriedCl",emote="05")
            call her_main("Просто у нас скоро будет еще один тест...","soft","baseL")

        elif one_of_ten == 4:
            call her_main("Сэр, я всем сердцем ненавижу весь факультет Слизерина.","angry","angry")

        elif one_of_ten == 5:
            call her_main("Хогвартс стал для меня вторым домом в последнее время...","open","closed")
            call her_main("Я даже больше не скучаю по родителям...","annoyed","down")
            call her_main("Если подумать, я совсем по ним не скучаю...","angry","wide")
            call her_main("Я отвратительная дочь...","angry","down_raised")

        elif one_of_ten == 6:
            call her_main("*Зевок!* Я читала об одной технике, которая якобы позволяет сократить время сна на половину...","annoyed","ahegao")
            call her_main("Не думаю, что она и правда работает.... *Зевок!*","annoyed","down")

        elif one_of_ten == 7:
            call her_main("Даже после окончания Хогвартса я планирую продолжать усердно работать.","open","angryCl")
            call her_main("Если я отдам все, что смогу, я сделаю этот мир лучше, я знаю это!","open","base")
            call her_main("","normal","base")

        elif one_of_ten == 8:
            call her_main("Мне почему-то кажется, что этот год станет поворотным в моей жизни...","open","worried")
            call her_main("","soft","baseL")

        elif one_of_ten == 9:
            call her_main("Некоторые редко посещаемые школьные коридоры не очень хорошо освещены и довольно пыльные...","open","angryCl")
            her "Пожалуйста, позаботьтесь об этом, сэр..."
            call her_main("","normal","base")

        elif one_of_ten == 10:
            call her_main("Я читала об этой штуке под названием \"Маховик Времени\".","open","base")
            her "Он позволяет перемещаться во времени..."
            call her_main("Наличие такого устройства сделало бы чудеса в моем расписании...","open","closed")
            call her_main("","annoyed","suspicious")


    ### WHORING LEVEL 04 ###
    if whoring >= 9 and whoring <= 11:
        if one_of_ten == 1:
            call her_main("Мое \"Движение за Права Мужчин\" в последнее время теряет популярность...","open","worried")
            call her_main("Как будто людям на это наплевать!","annoyed","angryL")

        elif one_of_ten == 2:
            call her_main("Спасибо, что купили все эти услуги у меня, сэр.","open","angryCl")
            call her_main("Конечно, некоторые из них были на грани неуместного...","normal","frown")
            call her_main("Но я не возражаю жертвовать своей честью, если это позволит Гриффиндору конкурировать со Слизерином на равных условиях.","open","angryCl")
            call her_main("","normal","base")

        elif one_of_ten == 3:
            call her_main("Квиддич глупый!","angry","angry")
            call her_main("Есть. Я сказала это.","annoyed","suspicious")

        elif one_of_ten == 4:
            call her_main("Сэр, есть кое-что о профессоре Снейпе, что вы должны знать...","open","base")
            call her_main(".................","open","worriedL")
            call her_main(".........................","annoyed","frown")
            call her_main("Хм... Неважно...","open","angryCl")
            call her_main("","normal","base")

        elif one_of_ten == 5:
            call her_main("Некоторые из девушек Слизерина продают сексуальные услуги почти в открытую...","open","angryCl")
            call her_main("Вы должны положить конец такой практике, сэр.","open","base")
            call her_main("(Я едва справляюсь...)","annoyed","angryL")

        elif one_of_ten == 6:
            call her_main("Жизнь работает таинственным образом...","open","worriedL")
            call her_main("Вы не согласны, сэр?","open","suspicious")
            call her_main("","soft","baseL")

        elif one_of_ten == 7:
            call her_main("Слизеринцы...","angry","angry",emote="01")
            call her_main("","angry","angry")

        elif one_of_ten == 8:
            call her_main("В последнее время, я так много времени провожу в вашем кабинете, сэр...","open","worriedL")
            call her_main("Если я не буду осторожна, некоторые люди могут подумать, что я стала вашим питомцем...","open","worried")
            call her_main("Я хотела сказать, домашнее животное учителя...","angry","worriedCl",emote="05")
            call her_main("","normal","worriedCl")

        elif one_of_ten == 9:
            call her_main("Мои любимые цвета?","open","base")
            call her_main("Алый и золотой, конечно!","open","base")
            call her_main("","normal","base")

        elif one_of_ten == 10:
            call her_main("Странно, что мои лучшие друзья мальчики?","open","worriedL")
            call her_main("","base","base")


    ### WHORING LEVEL 05 ###
    if whoring >= 12 and whoring <= 14:
        if one_of_ten == 1:
            call her_main("Сэр, при всем уважении...","normal","frown")
            her "Разврат профессора Снейпа выходит из-под контроля!"
            call her_main("Вы должны что-то сделать, сэр.","open","worried")
            call her_main("","normal","base")

        elif one_of_ten == 2:
            call her_main("Я готова пойти на многое, чтобы обеспечить лидерство моего факультета...","open","angryCl")
            her "Но это не значит, что я получаю удовольствие, продавая вам себя за очки факультету, сэр."
            call her_main("{size=-4}(Как какая-то ведьма-проститутка...){/size}","angry","down_raised")

        elif one_of_ten == 3:
            call her_main("Что это будет сегодня, сэр?","annoyed","annoyed")

        elif one_of_ten == 4:
            call her_main("В последнее время я учусь не так много, как раньше...","open","worried")
            call her_main("Я теряю свою мотивацию?","open","worriedL")
            call her_main("","soft","baseL")

        elif one_of_ten == 5:
            call her_main("Мой наименее любимый предмет?","open","suspicious")
            call her_main("Гадание.","annoyed","frown")

        elif one_of_ten == 6:
            call her_main("Мой отец говорил: \"Магия-это просто наука, которую мы еще не понимаем\".","open","base")
            call her_main("Конечно, он не мог ошибаться...","open","worriedL")
            call her_main("","soft","baseL")

        elif one_of_ten == 7:
            call her_main("Несмотря на все...","open","angryCl")
            call her_main("Я благодарна, за то, что вы продолжаете покупать у меня услуги, сэр...","open","worriedL")
            call her_main("","soft","baseL")

        elif one_of_ten == 8:
            call her_main("Сегодня довольно холодно, не так ли?","open","base")
            call her_main("","soft","base")

        elif one_of_ten == 9:
            call her_main("Скоро будет \"Осенний бал\"...","open","base")
            call her_main("","soft","base")

        elif one_of_ten == 10:
            call her_main("Люди чаще пропускают мои собрания в клубе \"Движение за Права Мужчин\"...","open","worriedL")
            call her_main("","soft","baseL")


    ### WHORING LEVEL 06 ###
    if whoring >= 15 and whoring <= 17:
        if one_of_ten == 1:
            call her_main("Хотите, я покажу вам свою грудь сегодня, сэр?","open","down")
            call her_main("Да... Я бы охотно открылась вам, профессор...","base","ahegao_raised")
            call her_main("Вот какая я бескорыстная!","annoyed","annoyed")

        elif one_of_ten == 2:
            call her_main("Я никак не могу помочь, но мне жаль домашних эльфов, которые стирают мое белье...","open","base")
            call her_main("В смысле, все эти ужасные пятна спермы...","open","down")
            call her_main("","angry","down_raised")

        elif one_of_ten == 3:
            call her_main("Не имеет значения, сколько раз вы спрашиваете меня об этом, сэр...","open","base")
            her "Ответ останется прежним..."
            call her_main("У меня нет ничего, кроме обиды на \"Слизеринцев\"!","angry","angry")
            call her_main("","annoyed","angryL")

        elif one_of_ten == 4:
            call her_main("Когда я думаю обо всех услугах, которые я вам продала за последние месяцы...","open","base")
            call her_main("Хотя я чувствую себя при этом немного неловко...","open","down")
            call her_main("Я также очень горжусь собой.","upset","closed")

        elif one_of_ten == 5:
            call her_main("Я до сих пор посвящаю много времени учебе...","open","base")
            her "Но не настолько, как раньше..."
            call her_main("Почему-то мне больше не нравится учиться...","open","worried")
            call her_main("","soft","baseL")

        elif one_of_ten == 6:
            call her_main("Гриффиндор получит Кубок в этом году!","open","angryCl")
            call her_main("{size=-4}(Даже если это будет стоить мне моего достоинства...){/size}","angry","down_raised")
            call her_main("","upset","closed")

        elif one_of_ten == 7:
            call her_main("Я не против осенней погоды...","open","base")
            call her_main("Но мое любимое время года-зима.","open","closed")
            call her_main("","soft","base")

        elif one_of_ten == 8:
            call her_main("Я раньше смотрела свысока на девочек, которые проводят слишком много времени, беспокоясь о том, как они выглядят...","open","base")
            her "Но я была не права..."
            her "Я начинаю понимать, как важно, чтобы девушка выглядела красиво."
            call her_main("...............","annoyed","worriedL")
            call her_main("В последнее время я на диете...","angry","wink")
            call her_main("","angry","worriedCl",emote="05")
            call her_main("","normal","worriedCl")

        elif one_of_ten == 9:
            call her_main("В последнее время я чувствую себя довольно уверенно рядом с мальчиками...","open","base")
            call her_main("Я думаю, я должна поблагодарить вас за это, сэр.","base","base")

        elif one_of_ten == 10:
            call her_main("Мой любимый предмет?","open","base")
            call her_main("Хм...","soft","baseL")
            call her_main("Я полагаю, что это \"очарования\"...","open","base")
            call her_main("","soft","base")


    ### WHORING LEVEL 07 ###
    if whoring >= 18 and whoring <= 20:
        if one_of_ten == 1:
            call her_main("Просто дайте мне знать, что потребуется от меня сегодня, сэр.","open","angryCl")
            call her_main("","normal","base")

        elif one_of_ten == 2:
            call her_main("Я почти не училась...","open","worried")
            her "Несмотря на это, моя популярность среди других студентов, кажется, растет..."
            call her_main("Хм...","soft","baseL")

        elif one_of_ten == 3:
            call her_main("Я бы прямо сейчас \"не отказалась\" от бутылочки сливочного пива...","smile","glance")
            call her_main("","grin","baseL")

        elif one_of_ten == 4:
            call her_main("Что случилось, сэр? У вас есть другой подарок для меня?","base","base")
            call her_main("О... Я вижу...","annoyed","angryL")

        elif one_of_ten == 5:
            call her_main("У меня все хорошо, спасибо, что спросили.","base","base")

        elif one_of_ten == 6:
            call her_main("Я потолстела, сэр?","open","worried")
            call her_main("Интересно, работает ли диета...","annoyed","worriedL")

        elif one_of_ten == 7:
            call her_main("Помню, я говорила, что книги-это мои друзья...","open","closed")
            call her_main("Теперь это звучит так глупо.","grin","worriedCl",emote="05")
            call her_main("","soft","base")

        elif one_of_ten == 8:
            call her_main("Добавить яйцо ashwinder(огневицы) в котел...","open","angryCl")
            her "Затем добавить красную подкову и нагреть..."
            her "Затем сок луковицы..."
            call her_main("Или сначала была капля тимьяна?","open","worriedL")
            call her_main("..............","soft","baseL")
            call her_main("Ох, какая разница?","grin","worriedCl",emote="05")
            call her_main("","base","base")

        elif one_of_ten == 9:
            call her_main("Как вы думаете, я достаточно накрасилась, сэр?","open","base")
            her "Если нанести слишком много, будет выглядеть - вульгарно..."
            call her_main("Но нанести слишком мало будет выглядеть - серо...","soft","baseL")
            call her_main("Я не хочу выглядеть серо!","annoyed","angryL")

        elif one_of_ten == 10:
            call her_main("Хотите увидеть мои сиськи сегодня, сэр?","smile","glance")
            call her_main("25 очков, пожалуйста.","smile","angry")
            call her_main("","upset","closed")


    ### WHORING LEVEL 08+ ###
    if whoring >= 21:
        if one_of_ten == 1:
            call her_main("У вас есть журналы для взрослых, которые вам не нужны, сэр?","open","baseL",cheeks="blush")
            call her_main("","base","baseL",cheeks="blush")

        elif one_of_ten == 2:
            call her_main("Простите, что беспокою вас этим, сэр...","open","base")
            her "Но у вас есть презервативы?"
            call her_main("Это конечно не для меня... Я спрашиваю для своей подруги...","angry","worriedCl",emote="05")

        elif one_of_ten == 3:
            call her_main("В последнее время становится холодно...","open","base")
            call her_main("Надеюсь, скоро пойдет снег...","base","base")

        elif one_of_ten == 4:
            call her_main("Прыгать и кричать для команды Гриффиндора!","open","closed")
            call her_main("Такие отважные и смелые, спортивные, красные и золотые!","smile","happyCl",emote="06")
            call her_main("","base","base")

        elif one_of_ten == 5:
            call her_main("Надеюсь, все пройдет гладко...","open","worriedL")
            call her_main("","soft","baseL")

        elif one_of_ten == 6:
            call her_main("Интересно, что Джинни Уизли оденет на бал...","base","base")

        elif one_of_ten == 7:
            call her_main("Учитывая характер услуг, которые вы у меня покупаете, сэр...","open","closed")
            call her_main("Я редко утруждаю себя, надевать нижнее белье...","open","worried")

        elif one_of_ten == 8:
            call her_main("Сэр, не могли бы вы засунуть свой пенис мне в рот?","angry","base")
            call her_main("Сэр, я прошу вас об этом...","open_wide_tongue","ahegao")
            call her_main("Пятьдесят пять очков, пожалуйста!","smile","angry")
            call her_main("","angry","wink")

        elif one_of_ten == 9:
            call her_main("Читала статью о положительном влиянии спермы на кожу женщины...","open","closed")
            call her_main("Интересно, откуда у них такая информация...","base","glance")
            call her_main("Журнал проводил какие-то исследования?","angry","wink")
            call her_main("","base","glance")

        elif one_of_ten == 10:
            call her_main("Все происходит примерно так...","open","closed")
            her "Первый Гриффиндор, затем Когтевран, далее Пуффендуй..."
            call her_main("А Слизерина даже нет в списке!","open","annoyed",cheeks="blush")
            call her_main("","upset","closed")


    return


