

### Walk Of Shame ###

label hg_ps_WalkOfShame: #This will become more intense as the wear a shorter skirt and wear a sluttier shirt favours are completed

    m "[hermione_name], какие у тебя сегодня занятия?"
    call her_main("Какие? С каких это пор вы проявляете интерес к моему образованию?","normal","frown")
    m "Я твой директор, конечно я забочусь о твоем образовании."
    call her_main("Хммм...","normal","frown")
    call her_main("Ну, у меня урок зельеварения с профессором Снейпом по утрам, а затем защита от темных искусств после обеда.","normal","frown")
    m "Итак, сегодня у тебя занятия у профессора Снейпа?"
    call her_main("Да [genie_name].","normal","frown")
    m "Это хорошо. Сегодня у меня есть для тебя задание."
    call her_main("Задание?","normal","frown")
    m "Да, я бы хотел, чтобы ты посетила занятия."
    call her_main("Это все?","normal","frown")
    m "Без cвоей рубашки."
    call her_main("ЧТО?","normal","frown")
    call her_main("С какой стати мне это делать?","normal","frown")
    m "Потому что я попросил тебя."
    call her_main("...Но как насчет профессора Снейпа? А как же мои одноклассники?","normal","frown")
    m "Не беспокойся о профессоре Снейпе, я уверен, что он уже привык к твоим выходкам."
    m "А что касается твоих одноклассников, есть ли кто-то кто будет удивлен?"
    call her_main("Ну, Джинни была бы...","normal","frown")
    m "Что? В шоке, узнав, что ее подруга мега шлюха, которая демонстрирует себя кому угодно, кто добавит очков ее факультету?"
    m "Посмотри на себя [hermione_name], посмотри, во что ты одета. Я удивлюсь, если в школе найдется кто-то, кто не знает, какая ты шлюха."
    call her_main("...","normal","frown")
    ">Она сдерживает слезы, протягивая тебе свою рубашку."
    call her_main("Я полагаю, что вы правы [genie_name].","normal","frown")
    call her_main("Что ж, мне лучше пойти... Нельзя опаздывать на занятия.","normal","frown")
    ">Она неохотно покидает твой кабинет."
    $ hg_ps_WalkOfShame_OBJ.inProgress = True

label hg_ps_WalkOfShame_complete:#Returns to your office after being made walk around the school with no shirt
    return