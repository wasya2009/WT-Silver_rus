

label date_with_snape_01:
    call bld 
    m "Хорошо. Научи меня магии на основе волшебной палочки."
    call sna_head("Конечно, я мог бы это сделать...","snape_23",xpos="base",ypos="base") 
    call sna_head("Или я могу рассказать больше о тех молоденьких \"Слизеринских\" шлюхах...","snape_02") 
    g9 "Последнее, пожалуйста."
    call sna_head("Прекрасно... Зацени тогда...","snape_13") 
    pause.1
    call blktone 

    ">Вы провели вечер, обсуждая всякие неуместные вещи с профессором Снейпом."
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">Вы чувствуете слабую связь между вами..."
    call sly_plus 
    call hide_blktone 

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    
    return
    
    
label date_with_snape_02:
    call bld 
    m "Чтобы наше маленькое предприятие преуспело..."
    m "Тебе нужно быть более щедрым с этими очками..."
    call sna_head("Да, конечно....","snape_09",xpos="base",ypos="base") 
    sna "Мисс Грейнджер потребуется сильный стимул..."
    sna "Поэтому важно, чтобы мой факультет лидировал..."
    call sna_head("Может потребоваться время, хотя...","snape_06") 
    m "Займет время?"
    m "Почему бы просто не присудить пару сотен очков \"Слизерину\" и покончить с этим?"
    call sna_head("Нет, мы должны быть осторожны с этим...","snape_24") 
    call sna_head("Присуждение целой кучи очков моему факультету без веской причины может привлечь ненужное внимание...","snape_05") 
    m "Хм... Я понимаю, к чему ты клонишь..."
    call blktone 

    ">Вы проводите вечер обсуждая заговор против Гермионы, с профессором Снейпом..."
    ">Слабая связь между вами укрепляется."

    call sly_plus 
    call hide_blktone 
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    
    return
    

label date_with_snape_03:
    call bld 
    call sna_head("Ты слышал об этом? \"движении за права мужчин\"? Бред какой то.","snape_01",xpos="base",ypos="base") 
    sna "Она умна, популярна и обладает железной волей..."
    $ s_sprite = "characters/snape/main/snape_06.png"
    call sna_head("В последнее время я начинаю сомневаться в нашем плане...","snape_06") 
    m "Но тебе не стоит этого делать..."
    call sna_head("Разве...","snape_26") 
    m "Это может занять некоторое время, но я {size=+5}точно{/size} сломаю ее."
    m "Просто поверь мне."
    sna "Хорошо..."
    call sna_head("Какой у меня есть выбор, кроме как надеяться на лучшее...?","snape_06") 
    call blktone 

    ">Вы проводите вечер, опасаясь неопределенного будущего с профессором Снейпом."
    ">Между вами формируется слабая связь доверия."

    call sly_plus 
    call hide_blktone 

    $ snapes_support += 1 #Controls how many points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
  
    return
    

label date_with_snape_04:
    call bld 
    call sna_head("Скажи мне, Джинн...","snape_24",xpos="base",ypos="base") 
    m "Да?"        
    call sna_head("Ты веришь в теорию параллельных миров?","snape_25") 
    m "Ну, в это трудно не верить, учитывая все обстоятельства."
    call sna_head("Истинно...","snape_23") 
    call sna_head("Думаешь, где-то есть другая версия меня?","snape_05") 
    m "Вероятно..."
    call sna_head("Хм...","snape_23") 
    sna "Северус Снейп - всегда веселый белый маг..."
    m "Несомненно, почему нет?"
    call sna_head("Какие тревожные образы ты помещаешь в мой разум...","snape_03") 
    m "Как насчет другой альтернативной версии этой Грейнджер?"
    call sna_head("Да! Гермиона Грейнджер - отвратительная шлюха без достоинства! Да, мне это нравится!","snape_02") 
    m "А что, если в том другом мире веселый Северус объединится с какой-нибудь странной версией меня?"
    m "А может они вместе обучат шлюху Гермиону быть прилежной девочкой и хорошей студенткой?"
    call sna_head("Ха-ха-ха! Это уморительно!","snape_28") 
    pause.1
    call blktone 

    ">Вы проводите вечер, обсуждая науку, метафизику, философию и шлюх."
    ">Связь дружбы между тобой и профессором Снейпом укрепляется."

    call sly_plus 
    call hide_blktone 
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    
    return

    
    
label date_with_snape_05:
    call bld 
    call sna_head("Так... Как продвигается наш маленький план?","snape_05",xpos="base",ypos="base") 
    sna "Эта несчастная девушка доставляет тебе неприятности?"

    menu:
        "\"Да. Она упрямая.\"":
            call sna_head("Ничего удивительного...","snape_06") 
        "\"Нет, не совсем так...\"":
            call sna_head("Серьезно?","snape_05") 
            sna "Интересно..."
    call sna_head("Но ты уверен, что сможешь ее сломать?","snape_01") 
    m "О, конечно."
    m "Это может занять некоторое время..."
    call sna_head("Что ж, у нас есть время...","snape_06") 
    call sna_head("Ты все еще бессилен, верно?","snape_05") 
    m "Да, в значительной степени..."
    call sna_head("Великолепно!","snape_02") 
    m "......................."
    call sna_head("Я имею в виду, это плохо для {size=+5}тебя{/size}, но хорошо для {size=+5}нас{/size}, верно?","snape_29") 
    m "Верно..."
    call blktone 

    ">Профессор Снейп, кажется, чувствует себя неловко, извлекая выгоду из твоего положения..."
    ">Связь дружбы между вами слегка укрепляется..."

    call sly_plus 
    call hide_blktone 
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return
    

label date_with_snape_06:
    call bld 
    m "Итак, расскажи мне об этих \"Слизеринских\" шлюхах побольше!"
    call sna_head("Что я могу сказать? В последнее время моя жизнь заметно улучшилась, мой друг.","snape_23",xpos="base",ypos="base") 
    call sna_head("Сейчас у меня есть целый гарем скупых студенток на выбор.","snape_22") 
    g9 "Здорово!"
    call sna_head("Да. Благодаря тебе, я могу делать все, что захочу!","snape_02") 
    sna "И что более важно..."
    call sna_head("Кого бы я ни захотел!","snape_13") 
    m "Серьезно?"
    call sna_head("Ну, вроде того...","snape_09") 
    sna "Очевидно, я вообще \"делаю все, что захочу\"..."
    call sna_head("Но не поверишь, что некоторые из девушек готовы сделать в обмен на баллы факультету!","snape_13") 
    call sna_head("Или даже всего лишь хорошие оценки...","snape_22") 
    pause.1
    call blktone 

    ">Обычная холодная внешность профессора Снейпа распадается на глазах..."
    ">Узы вашей дружбы снова укрепляются..."

    call sly_plus 
    call hide_blktone 
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return
    
    
label date_with_snape_07:
    call bld 
    call sna_head("Значит, в твоем мире ты какое-то всемогущее существо?","snape_05",xpos="base",ypos="base") 
    m "Да, в некотором роде..."
    call sna_head("Тогда почему ты подчиняешься этой женщине Жасмин?","snape_05") 
    m "О... Ну..."
    m "...она принцесса."
    call sna_head("И?","snape_05") 
    sna "Она твоя принцесса? Ты даже не человек."
    sna "Ты поклялся ей в верности?"
    hide screen s_head2  
    m "Едва ли..."
    call sna_head("Почему ты тогда беспокоишься?","snape_06") 
    call sna_head("Как я вижу, ты всемогущее существо, а она просто магл...","snape_09") 
    m "Она кто?"
    call sna_head("Человек... Она просто человек....","snape_25") 
    call sna_head("Так зачем пытаться угодить ей?","snape_05") 
    m "Ну это сложно..."
    call sna_head("..............","snape_05") 
    m ".................."
    call sna_head("Она горячая штучка, не правда ли?","snape_02") 
    m "Чушь..."
    call sna_head("Попался.","snape_23") 
    pause.1
    call blktone 

    ">Вы и профессор Снейп разделяете сладко-горький момент полный мужской солидарности."
    ">Узы вашей дружбы крепнут."

    call sly_plus 
    call hide_blktone 

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return
    
    
label date_with_snape_08:
    call bld 
    call sna_head("Как думаешь, если мы захотим...","snape_05",xpos="base",ypos="base") 
    sna "Мы можем вернуть публичную порку?"
    m "Что ты имеешь в виду?"
    call sna_head("Ну, много лет назад порка была вполне приемлемой мерой наказания для студентов.","snape_06") 
    sna "*Вздох* Давненько..."
    call sna_head("Нынешним студентам просто совершенно не хватает дисциплины...","snape_16") 
    sna "Я не хочу ничего, кроме как публично выпороть каждого из них..."
    call sna_head("Особенно девочек...","snape_22") 
    m "Хм... Меня устраивает..."
    m "Но разве подобная реформа не привлечет к нам ненужного внимания?"
    call sna_head("Да. Ты, конечно, прав.","snape_29") 
    sna "Я становлюсь алчным..."
    call sna_head("Я просто упиваюсь властью, мой друг!","snape_28") 
    sna "И это изысканное вино ничуть не улучшает мое суждение!"
    pause.1
    call blktone 

    ">Профессор Снейп ведет себя полностью непринужденно в твоей компании."
    ">Связь мужской дружбы между вами еще больше укрепляется.\n>Количество начисляемых очков \"Слизерину\" значительно увеличилось..."

    call sly_plus 
    call hide_blktone 

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return


label date_with_snape_09:
    call bld 
    call sna_head("...итак, после я вернусь обратно в Россию, не так ли?","snape_24",xpos="base",ypos="base") 
    g4 "Обратно в Россию?"
    call sna_head("Но подожди, все становится хуже.","snape_01") 
    call sna_head("Видимо, теперь я свободно говорю по-русски.","snape_05") 
    g4 "Подожди, что?"
    call sna_head("А я несчастный магл, живущий в дыре города, полном обветшалых зданий.","snape_06") 
    sna "Я пытаюсь зарабатывать на жизнь, рисуя комиксы и создавая игры на \"Ren'Py\"..."
    call sna_head("И это так странно, потому что я даже не знаю, что за \"Ren'Py\"!","snape_24") 
    m "Хм... Тогда что случилось?"
    call sna_head("Немного... В основном занимался сидячей работой в течение нескольких месяцев...","snape_05") 
    sna "Тогда как-то удалось создать относительно успешную игру..."
    call sna_head("В конце концов начал зарабатывать приличные деньги своими рисунками...","snape_24") 
    call sna_head("А потом, когда я увидел надежду на будущее...","snape_06") 
    call sna_head("Я проснулся...","snape_04") 
    call sna_head("....................","snape_09") 
    m "......................"
    call sna_head("Как ты думаешь, что все это значит?","snape_05") 
    m "Звучит как еще один игровыкидыш от Akabur'а."
    call sna_head("Что?","snape_05") 
    m "Просто не обращай внимания."
    m "Глупый сон, ничего больше."
    call sna_head("Больше похоже на какой-то кошмар...","snape_29") 
    pause.1
    call blktone 

    ">Профессор Снейп доверяет тебе больше, чем раньше..."
    ">(До такой степени, что он не думает дважды о том, чтобы поделиться с тобой своими странными грезами)."

    call sly_plus 
    call hide_blktone 
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return
    
    
label date_with_snape_10:
    call bld 
    call sna_head("В чем смысл жизни, Джинн?","snape_29",xpos="base",ypos="base") 
    g4 "Что?"
    call sna_head("Так как ты всемогущее существо, ты должен знать такие вещи, верно?","snape_05") 
    m "Возможно..."
    call sna_head("Отлично. Скажи мне тогда.","snape_06") 
    m "Хм... Ты уверен, что готов к этому?"
    call sna_head("Да. Положись на меня, друг.","snape_05") 
    m "Ладно..."
    call sna_head("................!","snape_01") 
    m "Это пластмасса..."
    call sna_head("Прошу прощения?","snape_05") 
    m "Это пластмасса..."
    call sna_head("Не понял...","snape_25") 
    m "Эта планета планирует превратиться во что-то другое через миллион лет или около того..."
    m "Для этого ей нужна особый вид материала, который она не может производить самостоятельно."
    m "Так рождается новая форма жизни-люди."
    call sna_head("..............","snape_11") 
    m "Ты хотел узнать цель вашего существования?"
    m "Это для производства пластмасс. Все просто."
    call sna_head("Ты издеваешься?!","snape_30") 
    call sna_head("Нет, нет... Этого не может быть...","snape_26") 
    g9 "Хи-хи..."
    call sna_head("Ты что, издеваешься надо мной?","snape_25") 
    g9 "Ты бы видел свое лицо."
    call sna_head("Ты действительно заставил меня волноваться, ты чертов нечеловеческий ублюдок!","snape_15") 
    g9 "Я знаю! Было трудно сопротивляться..."
    call blktone 

    ">Вы проводите вечер, умело избегая целого ряда подобных тем."
    ">Несмотря на твой отказ сотрудничать, узы дружбы между вами снова укрепляются."

    call sly_plus 
    call hide_blktone 

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return


label date_with_snape_11:
    call bld 
    call sna_head("Итак... В вашем мире есть страна под названием Англия?","snape_05",xpos="base",ypos="base") 
    m "Мы использовали для..."
    call sna_head("Что случилось?","snape_26") 
    m "\"Великой катастрофы\"..."
    m "Она сожгла большую часть населения мира за считанные часы..."
    call sna_head("................","snape_26") 
    m "Превращение около восьмидесяти процентов поверхности планеты в палящую пустыню..."
    m "А остальные двадцать процентов превратились в ледяную пустошь..."
    m "............."
    call sna_head("Это...","snape_26") 
    call sna_head("Ужасно...","snape_06") 
    call sna_head("Ты уверен, что хочешь вернуться в то место?","snape_25") 
    m "Конечно."
    m "Это может быть немного дико, но эй... это дом."
    call blktone 

    ">Профессор Снейп находит новый уровень уважения к тебе..."
    ">Узы дружбы между вами двумя крепнут."

    call sly_plus 
    call hide_blktone 
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return

    
label date_with_snape_12:
    call bld 
    call sna_head("Я думал о том, что ты сказал на днях...","snape_09",xpos="base",ypos="base") 
    sna "О том, что твой родной мир всего лишь выжженная пустыня и все такое..."
    m "Да?"
    call sna_head("Как думаешь, Альбус будет там в порядке?","snape_06") 
    m "О, абсолютно!"
    m "Так как я вполне буквально заменил его на этом стуле..."
    m "Вероятно, он заменил меня в том же самом месте в Аграбе.(в лавке)"
    call sna_head("Аграбе?","snape_05") 
    m "Да... Очень большой город."
    m "Один из немногих, кто поднялся после Великой катастрофы."
    m "Вероятно, самый большой из них..."
    m "сердце человеческой цивилизации, если хочешь."
    call sna_head("Я рад это слышать...","snape_23") 
    m "Конечно..."
    m "Хотя, если твой друг Альбус действительно материализовался в том же месте, что и я, до того, как наложил заклинание..."
    m "Полагаю, принцесса может его обезглавить..."
    call sna_head("ЧТО?!","snape_01") 
    m "Но вероятность этого очень мала..."
    m "Около пяти процентов... Может десять... Двадцать процентов максимум."
    call sna_head(".......................................................","snape_03") 
    pause.1
    call blktone 

    ">Профессор Снейп, кажется, (вроде) благодарен тебе, что его опасения по поводу Альбуса Дамблдора благополучно развеялись..."
    ">Узы вашей дружбы снова укрепляются..."

    call sly_plus 
    call hide_blktone 

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return

    
label date_with_snape_13:
    call bld 
    call sna_head("Знаешь что?","snape_01",xpos="base",ypos="base") 
    m "Что?"
    call sna_head("Впервые за очень долгое время...","snape_01") 
    call sna_head("Я думаю...","snape_03") 
    call sna_head("Я действительно доволен тем, как моя жизнь идет.","snape_25") # 0_0
    call sna_head("Какое тревожное чувство...","snape_26") 
    m "Ты уверен, что это не эйфория, вызванная сексом, который у тебя был совсем недавно?"
    call sna_head("Может быть.","snape_22") 
    call sna_head("Тем не менее, ты можешь тренировать только одну девушку...","snape_09") 
    call sna_head("Но она имеет большое влияние на мою жизнь...","snape_24") 
    sna "И даже сама школа..."
    m "Другими словами, ты становишься менее задумчивым и винишь в этом меня."
    call sna_head("Что-то вроде этого...","snape_23") 
    call sna_head("Я теряю свою мрачность, мужик.","snape_28") # :)
    pause.1
    call blktone 

    ">Профессор Снейп действительно стал немного веселее в последнее время..."
    ">Он даже выглядит моложе, чем раньше, когда ты впервые его встретил..."
    ">Чувство благодарности профессора Снейпа укрепляет узы вашей дружбы."

    call sly_plus 
    call hide_blktone 

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return

    
label date_with_snape_14:
    call bld 
    call sna_head("...итак она говорит : \"Сэр, пожалуйста, не могли бы вы меня немного подушить,!\".","snape_02",xpos="base",ypos="base") 
    call sna_head("И я счастлив, выполнить ее просьбу!","snape_13") 
    call sna_head("Значит, я душу эту маленькую сучку, когда трахаю ее, так?","snape_19") 
    sna "И она закатывает глаза до такой степени, что я больше не могу видеть ее зрачки!"
    sna "Ее лицо приобретает слегка фиолетовый оттенок, и она едва дышит."
    call sna_head("И тогда я думаю, что, стоит немного ослабить хватку...","snape_14") 
    call sna_head("И в тот момент эта сучка начинает кончать!","snape_21") 
    m "Чудно! А потом ты проснулся?"
    call sna_head("Что? Нет, это действительно происходило.","snape_05") 
    call sna_head("Я наконец-то засадил той белокурой ведьмочке из \"Слизерина\".","snape_13") 
    g9 "Здорово!"
    call sna_head("Я знаю.","snape_13") 
    call sna_head("Хотя она довольно странная...","snape_25") 
    call sna_head("И я имею в виду я реально облажался.","snape_26") 
    g9 "Наш тип девушки!"
    call sna_head("В точку!","snape_22") 
    pause.1
    call blktone 

    ">Ты и профессор Снейп скреплены сходством вашего вкуса к женщинам."
    ">Узы вашей дружбы никогда не были сильнее."

    call sly_plus 
    call hide_blktone 

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return

    
label date_with_snape_15:
    call sna_head("Прошло уже много времени...","snape_05",xpos="base",ypos="base") 
    m "Что ты имеешь в виду?"
    call sna_head("Заклинание, которое привело в наш мир...","snape_24") 
    sna "Ты сказал, что со временем это пройдет..."
    call sna_head("Ты чувствуешь какие-то изменения?","snape_05") 
    m "Нет... никаких..."
    m "Может нужно больше времени?"
    call sna_head("Возможно...","snape_01") 
    sna "А может быть, что-то еще..."
    m "Например?"
    call sna_head("Понятия не имею...","snape_09") 
    sna "Но об этом я еще немного подумаю..."
    call sna_head("О, и еще одна вещь...","snape_24") 
    m "Хм...?"
    call sna_head("В это время года обычно я очень занят...","snape_24") 
    sna "Тем более сейчас, когда мне нужно постоянно покрывать отсутствие Альбуса."
    hide screen s_head2
    m "..................."
    call sna_head("Я не уверен, смогу ли я еще так проводить вечера, неторопливо наслаждаясь вином...","snape_06") 
    m "Правда?"
    call sna_head("Да...","snape_06") 
    sna "Я все еще буду иногда заходить, чтобы поболтать время от времени, но это все."
    hide screen s_head2
    m "Понятно..."
    m "С этого момента мне придется искать другой способ проводить вечера..."
    call sna_head("Уверен, мисс Грейнджер будет рада помочь.","snape_02") 
    m "Да, до тех пор, пока \"Слизерин\" лидерует."
    call sna_head("Серьезно? Она все еще беспокоится об этом?","snape_05") 
    m "Еще как."
    call sna_head("Ну, в таком случае я лично гарантирую, что \"Слизерин\" будет получать как можно больше очков дома, на сколько это возможно.","snape_23") 
    pause.1
    call blktone 

    ">Ваш уровень дружбы с профессором Снейпом достиг максимального значения."
    ">Поздравляю. Если бы это было \"dating-sim\" ты получил концовку с Северусом Снейпом."
    ">Факультету \"Слизерин\" присуждается значительное количество очков и получает ежедневное максимальное начисление."

    call sly_plus 
    call hide_blktone 

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    
    $ sfmax = True # Turns TRUE when friendship with Snape been maxed out.

    return

    
label sly_plus:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">Факультету \"Слизерин\" начисление очков увеличилось..."
    return



