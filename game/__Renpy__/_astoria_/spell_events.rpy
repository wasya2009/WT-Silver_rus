





label susan_imperio:
    call ast_main("Хорошо, [ast_genie_name].","smile","base","base","mid",xpos="base",ypos="base",trans="fade")
    call ast_main("Я приведу [ast_susan_name]!","grin","angry","angry","mid")
    call blkfade

    call nar(">Астория ушла, что бы позвать Сьюзан.")
    pause.5
    call play_sound("door")
    hide screen blkfade
    call sus_main("Здравствуйте, Профессор.","open","base","worried","mid",xpos="mid",ypos="base",trans="fade")
    call sus_main("Вы хотели меня видеть?","upset","base","worried","down")

    m "Да, Мисс Боунс, ты не могла бы пока просто постоять там пока--"
    call ast_main("Подождите секунду, [ast_genie_name],...","scream","closed","base","mid",xpos="close",ypos="base",trans="hpunch")
    call ast_main("50 очков, помните!","grin","angry","angry","mid")
    m "..."
    m "Правее..."
    m "Хорошо... 50 очков для \"Слизерина\"!"
    $ slytherin +=50
    call ast_main("Благодарю вас!","grin","happyCl","base","mid")
    hide screen astoria_main
    with d3
    call ast_main("","grin","angry","angry","L",xpos="base",ypos="base")
    call blkfade

    hide screen blkfade
    call sus_main("Что вы делаете--","open","wide","worried","R",xpos="mid",ypos="base",trans="fade")

    call cast_spell("imperio")
    call ast_main("{size=+10}{b}IMPERIO{/b}{/size}","scream","angry","angry","angry")

    show screen blktone
    call ast_main("[ast_susan_name], Я приказываю тебе делать все, что скажет старик!")
    call sus_main("Хорошо, я сделаю все, что скажет старик--","open","base","base","up")

    hide screen blktone
    call ast_main("Готово, [ast_genie_name]! Вероятно, это продлится пару дней...","smile","base","base","R")
    call ast_main("Вы можете идти, [ast_susan_name]!","grin","happyCl","base","mid")
    call sus_main("Ладно","base","base","base","up")
    hide screen susan_main
    with d3

    $ susan_imperio_counter += 20 #Lasts 20 days.
    $ susan_imperio_influence = True
    $ spells_locked = True

    call nar(">Сьюзан сейчас под влиянием Imperio.\n>Эффект будет длиться 20 дней.")
    jump astoria_requests




label imperio_spell_1:
    call play_music("hermione_theme")
    call blkfade

    call nar(">Ты вызвал Сьюзан в свой кабинет.")
    pause.5
    call play_sound("door")
    hide screen blkfade
    call sus_main("Здравствуйте, [sus_genie_name]. Вы хотели меня видеть?.","open","base","worried","mid",xpos="mid",ypos="base",trans="fade")
    call ast_main("Эй, [ast_susan_name]!","grin","narrow","narrow","L",xpos="base",ypos="base")
    call sus_main("Астория? Что ты здесь делаешь?","open","base","worried","R")

    call ast_main("О, не обращай на меня внимания...","pout","base","base","R")
    call ast_main("Я здесь всего лишь для того, чтобы наложить на тебя проклятие.","grin","angry","angry","mid")
    call sus_main("П-проклятие на меня?!!","open","wide","worried","wide")
    call sus_main("Нет! Профессор, кто-ниб--","scream","wide","worried","mid")

    call cast_spell("imperio")
    call ast_main("{size=+10}{b}Imperio Core Meum!{/b}{/size}","scream","angry","angry","angry")

    call sus_main("Ч-что ты--","open","wide","worried","wide")
    call nar("Струйка оранжевого дыма срывается с конца палочки Астории и ударяет в нос Сьюзан.")
    call sus_main("--делаешь...","upset","base","base","up")
    call sus_main("...","upset","narrow","base","up")
    hide screen astoria_main
    with d3
    call ast_main("Итак, что мы делаем теперь?","grin","angry","angry","mid",xpos="close",ypos="base")
    m "Ты же тоже читала книгу, не так ли?"
    call ast_main("Там было только о том, как его создавать, [ast_genie_name]!","open","base","base","R")
    call ast_main("Что же мы должны заставить ее захотеть?","grin","angry","angry","L")
    m "Хммм?"
    m "Как на счет, заставить ее раздеться?"
    call ast_main("[ast_genie_name]!","disgust","closed","worried","mid")
    m "Что? Разве ты не делала этого?"
    call ast_main("Я заставляла ее только снять верх.","open","base","base","mid")
    m "Угу, хорошо... давай сделаем это снова..."
    call ast_main("Ладно...","smile","base","base","L")
    call ast_main("Сьюзи, ты меня слышишь?","open","closed","base","mid")
    call sus_main("Да...","upset","narrow","worried","up")
    call ast_main("Хорошо, я хочу, что бы ты обратила внимание.","open","base","base","L")
    call sus_main("...","base","narrow","base","up")
    call ast_main("Отныне, у тебя есть неконтролируемое желание продемонстрировать мне и Дамби свои груди!","open","closed","base","mid")
    call sus_main("Мои груди? Ладно...","upset","narrow","worried","down")
    call ast_main("Хорошо, теперь проснись!","smile","base","base","L")
    call sus_main("Я про..--...","open","narrow","base","down")

    call nar(">Тело Сьюзан слегка двигается, пока в ее глаза возвращается жизнь.")
    call sus_main("Ч-ч-что случилось?","scream","wide","worried","wide",trans="hpunch")

    call sus_main("И почему я...","open","base","base","down")
    call sus_main("О нет...","upset","narrow","worried","down")
    call ast_main("Что-то не так, Сьюзи?","grin","narrow","narrow","L")
    call sus_main("*gulp*","upset","closed","worried","down")
    call sus_main("сэр, не возражаете, если я покажу вам свою... г-грудь?","open","closed","worried","mid")
    m "Вашу {b}грудь{/b}, Мисс Боунс?"
    call ast_main("(Хихихихи--)","grin","angry","angry","L")
    call sus_main("Мне ужасно жаль, сэр!","open","closed","base","mid")
    call sus_main("Пожалуйста, не смотрите!!!","upset","closed","worried","mid")

    hide screen susan_main
    $ susan_wear_top = False
    call update_sus_uniform
    call sus_main("","upset","closed","worried","mid")
    pause.5

    m "О нет, Мисс Боунс!"
    m "Что вы делаете?!"
    hide screen bld1
    with d3
    pause.8

    call gen_chibi("jerking_off_behind_desk")
    pause.5

    call ast_main("(...)","pout","narrow","narrow","mid")
    call sus_main("М-м-мне жаль, профессор Дамблдор, я не знаю, что на меня нашло...","open","narrow","worried","down")
    call sus_main("М-м-мне жаль, что вам приходится это видеть...","upset","closed","base","mid")
    call ast_main("Видеть что, Сюзи?","grin","angry","angry","mid")
    call sus_main("Мои большие сиськи...","open","closed","worried","mid")
    call ast_main("(Я знала, что они мерзкие!)","grin","angry","angry","L")
    call sus_main("Пожалуйста, Сэр--","open","narrow","worried","mid")
    call sus_main("Не думайте обо мне плохо...","upset","closed","worried","mid")

    hide screen susan_main
    $ susan_wear_bra = False
    call update_sus_uniform
    call sus_main("","upset","closed","worried","mid")
    call ctc

    g4 "{size=+10}Хорошо!{/size}"
    call ast_main("Дамби!","scream","wide","wide","mid")
    m "Что? Ты не можешь меня винить за это!"
    call ast_main("Не это! Ты не должен считать, будто они хороши!","clench","angry","angry","mid")
    call ast_main("(И прекрати трогать себя... Гадость...)","pout","angry","angry","R",cheeks="blush")
    m "Разве нет?"
    call ast_main("{b}Нет!{/b} они огромные и мягкие, и мягкие и... и... и... и... и мерзкие!","scream","closed","angry","mid")
    g9 "Ты права на счет того, что они огромные и мягкие..."
    call ast_main("Дамби!","clench","angry","angry","mid")
    call sus_main("Как вы двое можете быть такими злыми!","upset","narrow","worried","R")
    call ast_main("Успокойся, [ast_susan_name]!","scream","angry","angry","L")
    call sus_main("[ast_susan_name]?! Что это значит?","open","wide","worried","wide")
    call ast_main("Пфффф... ты знаешь...","pout","angry","angry","R")
    call sus_main("Как ты смеешь!","scream","closed","angry","mid")
    call sus_main("И вы позволите ей так разговаривать, сэр?","scream","base","angry","mid")
    g4 "Что... что? Я немного.... ох... отвлекся..."

    call nar(">Ты продолжаешь гладить свой твердый, как камень, член, в то время, как грудь Сьюзан изумительно вздымается.")
    g4 "(Такие большие...)"
    call sus_main("...","upset","base","worried","down")
    call ast_main("Хорошо, мне кажется, вам это очень нравится, профессор Дамблдор!","disgust","angry","angry","mid")
    m "Еще немного дольше..."

    call cast_spell("imperio")
    call ast_main("{size=+10}{b} IMPERIO!{/b}{/size}","scream","angry","angry","angry")

    call sus_main("Ч-ч-что...","open","base","base","up")
    call nar(">Мягкая струйка желтого дыма струится из палочки Астории прямо в нос Сьюзан.")

    call gen_chibi("hide")
    show screen genie
    with d3
    pause.1
    m "(Черт возьми! Только не снова...)"

    call sus_main("...","upset","base","worried","down")
    call ast_main("Оденься, Сюзи.","smile","base","base","mid")
    call sus_main("Хорошо...","upset","narrow","worried","mid")

    hide screen susan_main
    $ susan_wear_bra = True
    call update_sus_uniform
    call sus_main("","upset","narrow","worried","mid")
    pause.5
    call nar("Сьюзан машинально одевается...")

    hide screen susan_main
    $ susan_wear_top = True
    call update_sus_uniform
    call sus_main("","upset","narrow","base","mid")
    pause.5
    call nar("Ее глаза все время тупо смотрят вперед.")

    m "Охх... Зачем ты это сделала?"
    call ast_main("Ты был слишком взволнован, старик.","clench","angry","angry","mid")
    m "Ну и что?"
    call ast_main("Тебе не стоит слишком много веселиться, иначе ты никогда не захочешь практиковать новые заклинания!","pout","angry","angry","R")
    m "Ты, хотя бы, могла заставить ее танцевать, или типа того..."
    call ast_main("Мы могли бы так сделать...","pout","base","base","L")
    m "Тогда, почему нет?"
    call ast_main("Потому, что это скучно!","disgust","ahegao","ahegao","ahegao")
    call ast_main("Я хочу узнать больше заклинаний!","open","closed","base","mid")
    m "Эх... хорошо..."
    call ast_main("Отлично. Я уже прочла название следующего!","grin","angry","angry","mid")
    m "Серьезно? И что это?"
    call ast_main("Imperio Tempus...","open","closed","base","mid")
    call ast_main("Я не видела, что оно может сделать.. Хотя...","upset","base","base","down")
    m "Хочешь начать читать сейчас?"
    call ast_main("Уже немного поздно, сэр.","worried","base","base","mid")
    call ast_main("Кроме того, я лучше верну Бесси обратно в ее сарай, пока люди не заметили.","grin","angry","angry","L")
    call sus_main("(Бесси...?)","upset","wide","worried","wide")
    m "Хорошо..."
    call ast_main("Просто дай мне знать, когда будешь готов прочитать следующую главу, Дамби!","smile","narrow","narrow","mid")
    m "Хорошо, я скажу тебе."
    call ast_main("Спокушки, Дамби!","grin","closed","base","mid")
    m "Доброй ночи..."
    call ast_main("Давай, Сюзи, возвращайся в свою комнату и ложись спать.","open","base","base","L")
    call sus_main("Да...","upset","narrow","worried","down")
    hide screen susan_main
    with d3
    pause.5

    call ast_main("(Это так весело!)","grin","closed","base","mid")
    hide screen astoria_main
    hide screen bld1
    with d3


    $ astoria_busy = True
    $ susan_busy = True
    $ spells_locked = True #Locks spells until you send Astoria to Tonks.

    if astoria_affection < 1:
        $ astoria_affection = 1
        $ astoria_spell_progress = 0

    jump day_main_menu




label imperio_spell_2: #second level imperio spell #needs posing
    call play_music("hermione_theme")
    call ast_main("Ты, наконец-то, готов попробовать новое заклинание, Дамби?","grin","narrow","narrow","mid",xpos="close",ypos="base",trans="fade")
    m "Еще бы!"
    call ast_main("Круто, я не могу дождаться, что бы увидеть выражение тупого лица Сьюзан...","grin","closed","base","mid")
    m "Позволь, я позову ее сюда."
    call blkfade

    call nar(">Ты вызываешь Сьюзан в кабинет.")
    pause.5
    call play_sound("door")
    hide screen blkfade
    call sus_main("Вы хотели меня видеть, [sus_genie_name]?","open","base","worried","mid",xpos="mid",ypos="base",trans="fade")
    call sus_main("Астория? Почему ты снова здесь?","open","base","worried","R")
    call ast_main("Ох... Просто так...","pout","base","base","down")
    call sus_main("Что-то не так, профессор?","upset","base","worried","mid")
    m "На самом деле да..."
    call sus_main("П-правда? Это потому, что я возвращаю свои книги в библиотеку на день позже?","open","wide","base","wide")
    call sus_main("Я клянусь, это больше не повторится!","open","closed","worried","mid")
    m "Что? Нет, боюсь, есть проблемы с твоей формой..."
    call sus_main("Ох... Это из-за того, что я не ношу школьную форму?","open","base","worried","down")
    call sus_main("Я стану ее носить с этого момента, если вам так нужно!","upset","base","base","mid")
    m "На самом деле, ношение слишком большого количества одежды является проблемой."
    call sus_main("Ч-ч-ч-что???","scream","wide","base","wide")
    call sus_main("Вы же это не серьезно, сэр!","open","wide","base","mid")
    m "Да, Мисс Боунс..."
    g9 "Скрывать такую прелестную грудь под одеждой - серьезный проступок!"
    call sus_main("","open","wide","base","wide")
    call ast_main("(Пфффф, славно-грубо)","pout","angry","angry","R")
    call sus_main("Профессор Дамблдор! Как вы можете говорить что-то подобное!","scream","base","angry","mid",trans="hpunch")
    call sus_main("Я думаю, мне лучше уйти...","upset","closed","worried","mid")
    hide screen astoria_main
    with d3
    call ast_main("","grin","angry","angry","L",xpos="base",ypos="base")
    pause.5

    call cast_spell("imperio")
    call ast_main("{size=+10}{b}IMPERIO TEMPUS! {/b}{/size}","scream","angry","angry","angry")

    call nar("В мгновение, фиолетовый дым вырывается из палочки Астории и летит в Сьюзан.")
    call sus_main("Что это--","open","wide","base","wide")

    show screen blktone
    call sus_main("...","upset","narrow","base","mid")
    call ast_main("Хахахахаха","grin","happyCl","base","mid")
    call ast_main("Выражение ее лица было бесценно, когда ты сказал про грудь...","grin","base","base","L")
    m "Тебе понравилось?"
    hide screen astoria_main
    with d3
    call ast_main("Конечно! Как и все, что собьет с Бесси спесь.","smile","narrow","narrow","L",xpos="close",ypos="base")
    call ast_main("Хотя, ты сказал это прежде, чем я бросила Imperio на нее, так что нам придется использовать Obliviate, что бы сохранить это в тайне.","upset","base","worried","L")
    m "Да, конечно..."
    m "(Что, черт возьми, такое Obliviate?)" #"прим. - Забвение"
    call ast_main("Так что мы сегодня заставим ее сегодня делать, [ast_genie_name]?","smile","base","base","mid")
    m "Ну, если верить книгам, это заклинание должно позволить нам навсегда изменить в ней что-то."
    call ast_main("Хмм.....","pout","narrow","narrow","R")
    call ast_main("Я знаю!","grin","angry","angry","mid")
    call ast_main("Давай заставим ее забыть про все, что происходит в этой комнате, как только она выйдет!","open","angry","angry","L")
    call ast_main("Таким образом, мы сможем не волноваться на счет сплетен о нас.","open","angry","angry","mid")
    m "Хорошая мысль, вундеркинд."
    call ast_main("...","pout","angry","angry","mid")
    m "Но, это все, что мы собираемся изменить в ней?"
    m "Не можем ли мы сделать чего-нибудь немного... побольше?"
    call ast_main("Ты имеешь в виду, что-то вроде показать нам свои дыньки?","pout","narrow","narrow","mid")
    m "Ну, если ты настаиваешь..."
    call ast_main("Тьфу... ты такой грязный извращенец!","clench","angry","angry","mid")
    m "Мы можем сделать еще что-то, если--"
    call ast_main("Я не говорила \"нет\".","upset","closed","base","mid")
    m "Ох... А что на счет того, что бы сделать--"
    call ast_main("Я выбираю, [ast_genie_name]!","scream","closed","angry","mid")
    m "Что? Почему?"
    call ast_main("Потому, что это мое заклинание и моя палочка!","open","narrow","narrow","mid")
    call ast_main("Не говоря уже о том, что ты бы сделал что-нибудь что-то сверхъестественное и грубое...","open","narrow","narrow","R")
    m "Наверное..."
    m "Итак, каков твой план?"
    call ast_main("Просто потерпи и все сам увидишь, старик!","disgust","narrow","narrow","mid")
    call ast_main("Сюзи, послушай!","scream","closed","base","L")
    call sus_main("Да...","upset","narrow","base","up")
    call ast_main("С этого момента ты не будешь помнить ничего из того, что происходит в этом кабинете.","open","base","base","L")
    call sus_main("Хорошо...","upset","narrow","base","mid")
    m "Это все?"
    call ast_main("Тише, старик, я еще не закончила!","disgust","narrow","narrow","mid")
    call ast_main("Так же, ты будешь чувствовать неконтролируемое желание снять верх одежды каждый раз, как увидишь меня и Дамби вместе, поняла?","open","closed","base","mid")
    call sus_main("Да...","upset","base","worried","down")
    m "Отлично! Но, не начнет ли она теперь просто убегать?"
    call ast_main("Хмммм... Ты, наверное, прав...","upset","base","worried","L")
    call ast_main("И последнее, тебе нельзя покидать этот кабинет, пока я не разрешу, понятно, Сюзи?","open","narrow","narrow","L")
    call sus_main("Да, Астория...","upset","narrow","worried","mid")
    call ast_main("Потрясающе! Теперь проснись, [ast_susan_name]!","grin","angry","angry","L")
    call sus_main("...","upset","narrow","base","up")

    hide screen blktone
    call nar(">Глаза Сьюзан медленно обретают цвет...")
    call sus_main("Ох...","upset","narrow","base","up")
    call sus_main("Что случилось?","open","narrow","worried","mid")
    call ast_main("Ничего, Сюзи, Дамблдор как раз объяснял, почему твоя униформа не в порядке.","grin","base","base","mid")
    call sus_main("Моя униформа... Вы правы... слишком много одежды...","open","narrow","worried","down")
    call sus_main("Мне нужно снять верх...","open","base","worried","down")
    call ast_main("Ммммм... Правильно, Сюзи. Почему бы тебе не показать старому Дамблдору свои огромные сиськи...","grin","angry","angry","mid")
    call sus_main("Н-н-но,... он такой старый.","upset","narrow","worried","L")
    call ast_main("Это верно... Только мерзкая шлюшка показала бы свои груди такому морщинистому старику...","grin","angry","angry","L")
    m "Эй!"
    call ast_main("Тссс, Дамби,... не порть мне удовольствие!","clench","angry","angry","mid")
    m "Прекрасно..."
    call sus_main("Я-я-я.. Я не шлюха...","upset","narrow","worried","down")
    call ast_main("Ну, я уверена, что ты тогда сможешь не снимать свою кофту, [ast_susan_name].","open","closed","base","mid")
    call sus_main("И... что-то не так, сэр!","open","base","worried","mid")
    call sus_main("Я ничего не могу поделать...","upset","narrow","worried","down")
    call ast_main("","grin","angry","angry","L")
    pause.2

    hide screen susan_main
    $ susan_wear_top = False
    $ susan_wear_bra = False
    call update_sus_uniform
    call sus_main("","upset","closed","worried","mid")
    call ctc

    g4 "Отлично!"
    hide screen bld1
    with d3
    pause.1
    call gen_chibi("jerking_off_behind_desk")
    pause.8

    call ast_main("[ast_genie_name]! Ты трогаешь себя?","scream","wide","wide","mid")
    m "Угх... Я ничего не могу поделать..."
    g4 "Не каждый день бывает такой стояк..."
    call ast_main("А ну прекрати! Это мерзко!","clench","angry","angry","mid")
    m "Хоро--"
    call sus_main("Пожалуйста, сэр... это слишком!","open","closed","base","mid")
    call sus_main("Достаточно того, что я вынуждена показывать вам свою грудь...","open","closed","worried","mid")
    call ast_main("Подожди...","open","wide","wide","wide")
    call ast_main("Продолжай, Дамби!","clench","angry","angry","mid")
    m "Что?"
    call sus_main("Что?","scream","wide","base","mid")
    call ast_main("Если Бесси так ненавидит это... Тогда я это люблю!","clench","angry","angry","L")
    call ast_main("Кроме того, под столом мне ничего не видно.","open","closed","base","mid")
    call sus_main("(...)","upset","closed","worried","mid")
    m "Так что, все в порядке?"
    call ast_main("Мммм... Только не жди, что я дотронусь до него, старик!","upset","angry","angry","mid")
    call sus_main("Мне это не нравится!","open","closed","base","mid")
    call ast_main("Тебя никто не спрашивал, шлюха!","clench","angry","angry","L")
    call sus_main("Я не щлюха!","scream","closed","angry","mid")
    call ast_main("Ха! Ты стоишь здесь, позволяя старику Дамблдору пялиться на твои огромные сиськи, пока он передергвает свой морщинистый старый член!","open","closed","base","mid")
    call ast_main("Если это не шлюха, тогда я не знаю, как это назвать!","disgust","narrow","narrow","L")
    call sus_main("Я-я не знаю, зачем я делаю это...","upset","closed","worried","mid")
    call sus_main("Ты, наверное, наложила заклинание на меня!","open","closed","angry","mid")
    call ast_main("Да!","grin","angry","angry","L")
    call sus_main("Останови это!","open","base","angry","R")
    call ast_main("Нет!","open","closed","base","mid")
    call sus_main("Пожалуйста, Астория...","upset","narrow","worried","down")

    call nar(">Ты начинаешь выпадать из беседы двух девушек, концентрируясь на Сьюзен и ее вздымающемся бюсте...")
    g4 "Угу, да... вот так..."
    call ast_main("Ты сможешь уйти, когда старик Дамби закончит.","open","closed","base","mid")
    call sus_main("Что? Ты имеешь в виду, что я должна дождаться, пока он...","open","base","worried","mid")
    call sus_main("Это невероятно!","scream","base","angry","mid")
    call sus_main("Я собираюсь доложить о вас обоих в Министерство Магии!","open","closed","angry","mid")
    call sus_main("Моя тетя - Мракоборец, вы знаете!","open","base","angry","mid")
    call ast_main("Да... Я встречала твою жуткую старую тетку.","pout","narrow","narrow","R")
    call sus_main("Что? Ты прокляла и ее тоже, ты, маленькая злобная ведьма?","open","wide","base","R")
    call ast_main("Я хочу...","pout","narrow","base","R")
    call sus_main("Она распорядится запереть вас обоих в Азкабане!","open","closed","angry","mid")
    call sus_main("Ты больше никогда не увидишь меня, или кого-то еще...","scream","closed","angry","mid")
    call ast_main("Ха!","grin","angry","angry","L")
    call sus_main("И вы, Дамблдор! Надеюсь, вам нравится размахивать своим отвратительным членом, потому как это был последний раз, когда вы это делаете!","scream","narrow","angry","mid")
    g4 "Угу, да... скажи это снова..."
    call sus_main("Тьфу! Вы оба больны!","open","narrow","angry","mid")
    g4 "Мммм... продолжай трясти своими сиськами..."
    g4 "Я почти достиг... {b}ШЛЮХА!{/b}"
    call sus_main("Я не {size=+10}ШЛЮХА!{/size}","scream","closed","angry","mid",trans="vpunch")
    call nar(">Когда Сьюзан срывает голос на крик, усилия заставляют ее гигантские сиськи подняться и шлепнуться вместе.")

    g4 "{size=+10}ОНО ПРИБЛИЖАЕТСЯ!{/size}"
    hide screen bld1
    with d3
    pause.1
    call gen_chibi("cumming_behind_desk")
    call cum_block
    g4 "{size=+10}Аааааа... ДАААА!!!!{/size}"
    call ast_main("Вау... Не думала, что в тебе столько всего, Дамби...","worried","wide","wide","wide")

    hide screen susan_main
    $ susan_wear_top = True
    $ susan_wear_bra = True
    call update_sus_uniform
    call sus_main("{size=+10}Хммм! Надеюсь, вам понравятся извращенцы в Азкабане!{/size}","upset","narrow","angry","down")
    call play_sound("door")
    hide screen susan_main
    with d3
    call ast_main("","pout","narrow","narrow","R")
    call gen_chibi("cum_on_desk")
    pause.5

    call nar(">Заколдованная Сьюзан, потрясенная твоей чудовищной эякуляцией, поворачивается и выбегает из твоего кабинета, держа рубашку в руке...")
    m "Тьфу... мы должны остановить ее?"
    call ast_main("Все прекрасно [ast_genie_name], я ведь сделала так, что бы она забыла обо всем, что происходит в этом кабинете, помнишь?","open","closed","base","mid")
    m "Ох... да..."
    call ast_main("Ну.. Я позволю тебе убраться...","disgust","narrow","narrow","mid")
    m "(...)"
    call ast_main("Увидимся [ast_genie_name]! И не забывай, что у нас есть новое заклинание на пробу!","open","closed","base","mid")
    m "Разве мы не можем повторить это?"
    call ast_main("НЕТ!","clench","angry","angry","mid")
    m "Прекрасно... Увидимся позже..."
    hide screen astoria_main
    with d3
    pause.5

    call nar(">Астория покидает твой кабинет, весело подпрыгивая во время ходьбы...")


    $ astoria_busy = True
    $ susan_busy = True
    $ spells_locked = True #Locks spells until you send Astoria to Tonks.

    if astoria_affection < 2:
        $ astoria_affection = 2
        $ astoria_spell_progress = 0

    jump day_main_menu


label imperio_spell_3:
    call play_music("hermione_theme")
    call ast_main("","smile","base","base","mid",xpos="close",ypos="base",trans="fade")
    m "Готова попробовать последнее заклинание Imperio?"
    call ast_main("Конечно, [ast_genie_name]! Я не могу дождаться, что бы увидеть глупое лицо и взгляд Сьюзи на этот раз!","grin","angry","angry","down")
    m "Я могу позвать ее сюда?"
    call ast_main("Тебе обязательно об этом спрашивать, старик?","smile","narrow","narrow","mid")
    m "Я полагаю, нет..."
    call blkfade

    call nar(">Ты вызываешь Сьюзан в свой кабинет.")
    pause.5
    call play_sound("door")
    hide screen blkfade
    call sus_main("Вы хотели меня видеть, сэр?","open","base","worried","mid",xpos="mid",ypos="base",trans="fade")
    call sus_main("Астория?...","upset","base","worried","R")
    call sus_main("Ты, кажется, здесь часто бываешь...","upset","narrow","worried","R")
    call ast_main("Я удивлена, что ты это заметила, Сюзи...","pout","base","base","R")
    call sus_main("Я не уверена, зачем меня позвали сюда...","open","base","worried","mid")

    hide screen susan_main
    $ susan_wear_top = False
    call update_sus_uniform
    call sus_main("","upset","base","worried","mid")
    pause.5

    call nar(">Пока Сьюзан говорит, ее руки, кажется, обретают собственный разум, тихо снимая с нее кофту.")
    call sus_main("Это из-за библиотечных книг, которые я вернула на день позже, сэр?","open","narrow","worried","down")
    call sus_main("Я обещаю, что это больше не повторится..","upset","closed","worried","mid")
    m "Дело не в чертовых книгах, Мисс Боунс!"
    call sus_main("Тогда в чем?","base","narrow","base","mid")

    hide screen susan_main
    $ susan_wear_bra = False
    call update_sus_uniform
    call sus_main("","base","base","base","mid")
    pause.5

    g4 "(!!!)"
    call ast_main("Может быть, это из-за того, что ты демонстрируешь свои мерзкие сиськи?","pout","base","base","R")
    call sus_main("Астория! Как ты можешь говорить подобные грубости! Я бы никогда...","open","closed","angry","mid")
    call sus_main("","upset","wide","worried","down",trans="hpunch")
    pause.8
    call nar(">Глаза Сьюзан опускаются на ее обнаженную грудь.")
    call sus_main("ЧТО??!!!","scream","wide","worried","down")
    call sus_main("Я прошу прощения, Профессор Дамблдор!","upset","closed","worried","mid")
    call sus_main("Я не знаю, что со мной!","open","closed","base","mid")
    call ast_main("Может быть, это просто потому, что ты мерзкая шлюшка!","pout","base","base","L")
    call sus_main("Я не {size=+10}шлюшка{/size}, Астория!","scream","closed","angry","mid")
    call ast_main("Пффф... Тебе, должно быть, нравится показывать сиськи директору, потому что ты такая ханжа...","pout","base","base","R")
    call sus_main("Я-- не знаю, почему это происходит...","open","wide","worried","wide")
    call sus_main("Ты, должно быть, прокляла меня!","scream","narrow","angry","R")
    call ast_main("Бинго!","grin","angry","angry","L")
    call sus_main("Профессор! Вы должны остановить ее!","scream","wide","base","mid")
    hide screen astoria_main
    with d3
    m "Угу... Я боюсь, что нет, Сьюзен..."
    call ast_main("","grin","angry","angry","L",xpos="base",ypos="base")
    call sus_main("ЧТО?!","scream","wide","base","wide")
    call sus_main("Тогда, моя тетя отправит вас в--","upset","narrow","angry","mid")

    call cast_spell("imperio")
    call ast_main("{size=+10}{b}IMPERIO MAXIMUS!{/b}{/size}","scream","angry","angry","angry")

    call nar(">Густой поток золотого дыма извергается из палочки Астории и плывет в сторону Сьюзен...")
    call sus_main("... в Азкабан...","open","narrow","base","up")

    show screen blktone
    call sus_main("...","upset","narrow","base","mid")
    hide screen astoria_main
    with d3
    call ast_main("Хорошо... Так, что мы можем заставить сделать ее в этот раз, [ast_genie_name]?","grin","base","base","mid",xpos="close",ypos="base")
    m "Хммм... Ты на самом деле собираешься позволить мне выбрать в этот раз, или просто хочешь меня по раздражать?"
    call ast_main("Эй! Я не раздражаю!","scream","closed","angry","mid",trans="hpunch")
    m "Ну, тогда ты позволишь мне выбрать?"
    call ast_main("Хорошо... Только не будь таким грубым, Дамби!","disgust","narrow","narrow","mid")
    call ast_main("Или скучным... это было бы еще хуже!","upset","narrow","narrow","mid")

    m "Хорошо.. Ну, перво-наперво..." #I'll add a menu here with more options once art assets are drawn for them

    hide screen blktone
    hide screen bld1
    with d3
    pause.1
    call gen_chibi("jerking_off_behind_desk")
    pause.8

    show screen bld1
    call nar(">Твои руки скрываются под столом, где обхватывают набухающий член.")
    g9 "Так-то лучше..."
    call ast_main("(...)","pout","angry","angry","R")
    m "Что?"
    call ast_main("Я же говорила тебе не быть занудой! Мы уже делали это в прошлый раз!","open","closed","base","mid")
    g9 "Если это слишком скучно, почему бы тебе не заставить ее отсосать у меня?"
    call ast_main("Дамби! Это слишком грубо!","disgust","narrow","narrow","mid")
    call ast_main("Я не хочу видеть твой отвратительный старый член!","clench","narrow","narrow","R")
    m "Тьфу... прекрасно... А что ты хочешь сделать?"
    call ast_main("Хорошо, так как ты спросил...","open","closed","base","mid")
    call ast_main("Сюзи, ты меня слушаешь?","open","narrow","narrow","L")

    show screen blktone
    call sus_main("Да...","upset","narrow","base","up")
    call ast_main("Я хочу, что бы ты залезла под стол Дамби.","grin","base","base","L")
    m "Я думал, ты не хочешь, что бы она отсосала мне?"
    call ast_main("Заткнись и перестань быть таким грубым, Дамби!","scream","closed","angry","mid")
    call sus_main("...","upset","narrow","base","up")
    call ast_main("Теперь иди, [ast_susan_name]!","grin","narrow","angry","mid")

    hide screen astoria_main
    hide screen susan_main
    hide screen blktone
    call blkfade

    call nar("Сьюзан медленно обходит вокруг твоего стола, прежде чем послушно заползти под него.")
    pause.5
    hide screen blkfade
    call ast_main("","smile","base","base","down",xpos="mid",ypos="base",trans="fade")
    hide screen bld1
    call ctc

    show screen blktone
    call ast_main("И тебе нельзя вылезать, пока Дамби не забрызгает тебя своей мерзкой дрянью!","open","closed","base","mid")
    sus "Да..."
    call ast_main("И ты должна любить это!","disgust","narrow","base","down")
    sus "...Любить это?"
    call ast_main("Да! Ты должна любить то, как она пахнет, как выглядит и то, насколько это мерзко!","open","closed","base","mid")
    sus "Я буду любить это..."
    call ast_main("Хорошо!","clench","angry","angry","angry")
    m "Это не слишком?"
    call ast_main("Пффф! Это сочное ожидание для тебя, Дамби!","pout","narrow","narrow","mid")
    call ast_main("Если бы это было для тебя, то она бы трогала твой противный старый морщинистый член!","pout","narrow","narrow","R")
    call ast_main("Своим ртом!","disgust","narrow","narrow","down")
    m "Полагаю, ты права..."
    call ast_main("Конечно, я права!","pout","narrow","narrow","R")
    call ast_main("Теперь вернись к поглаживанию своего мерзкого члена!","open","closed","angry","mid")
    m "Тебе не нужно повторять мне дважды!"
    call nar(">Ты возобновляешь свои усилия, воодушевляясь образом хорошенько обконченной рыжей девушки, прячущейся под столом.")
    call ast_main("И Сюзи...","open","narrow","narrow","down")
    sus "Да..."
    call ast_main("Самое время тебе проснуться...","grin","angry","angry","down")
    sus "..."

    call play_music("hermione_theme")
    hide screen blktone
    hide screen bld1
    with d3
    pause.5
    show screen bld1
    with hpunch
    sus "Ч-ч-ч-что происходит?"
    call play_sound("kick")
    with vpunch
    pause.2
    sus "Ой..."
    pause.5
    sus "Где я?"
    call ast_main("Ты не помнишь, как заползала под стол директора, умоляя его дрочить его старый мерзкий член?","open","closed","base","mid")
    with hpunch
    sus "ЧТО?"
    sus "Я никогда не просила что-то подобное!"
    call ast_main("Действительно? Потому, что это выглядит так, будто ты...","grin","base","base","R")
    sus "Я--"
    sus "Я не знаю, почему..."
    call ast_main("Если тебе там не нравится, почему бы тебе от туда, просто не выбраться?","pout","base","base","R")
    sus "Я не могу!"
    call ast_main("Правда? Почему же, Сюзи?","grin","narrow","narrow","down")
    sus "Я не знаю... Я просто не могу...!"
    call ast_main("Хммм... должно быть потому, что ты такая маленькая противная шлюшка...","open","closed","base","mid")
    with hpunch
    sus "Я не!"
    call ast_main("Ты уверена?","grin","angry","angry","down")
    sus "Д-да..."
    call ast_main("Потому, что это точно так не выглядит...","open","narrow","narrow","down")
    call ast_main("На самом деле, похоже что ты самая противная маленькая шлюха, которую когда-либо видела эта школа!","grin","closed","base","mid")
    g4 "Вот так, Астория..."
    sus "Профессор... {b}Пожалуйста...{/b}"
    call ast_main("Пожалуйста что, Сьюзан?","open","closed","base","mid")
    call ast_main("Пожалуйста, прекрати?","open","narrow","narrow","down")
    call ast_main("Или, пожалуйста, залей меня спермой?","disgust","narrow","narrow","down")
    with hpunch
    sus "АСТОРИЯ!"
    call ast_main("Ответь на вопрос, Сюзи...","open","base","base","mid")
    sus "..."
    sus "Пожалуйста, сэр..."
    sus "{size=-3}Измажьте {size=-3}меня {size=-3}в {size=-3}своей {size=-3}сперме...{/size}"
    call ast_main("Я знала это!","scream","wide","wide","wide")
    call ast_main("Ты грязная маленькая шлюшка, в конце-концов, не так ли?!","clench","angry","angry","down")
    sus "Это не так! Я не понимаю, почему я здесь!"
    call ast_main("Тогда ладно... Если ты такая хорошая девочка...","open","closed","base","mid")
    call ast_main("Почему бы тебе не рассказать мне, как тебе там внизу?","smile","narrow","narrow","down")
    sus "Здесь внизу?"
    sus "Под столом профессора Дамблдора?"
    call ast_main("Мммм... Держу пари, что там внизу мерзко...","clench","angry","angry","down")
    call ast_main("Вероятно, там пахнет мерзко из-за всего того, что он спускает под свой стол...","open","base","base","R")
    call ast_main("Не говоря уже про его вонючий старый член...","disgust","ahegao","ahegao","ahegao")
    m "Гм..."
    call ast_main("Тссс, Дамби!","pout","angry","angry","R")
    call ast_main("Так, продолжай, Сюзи.. расскажи мне, какого это...","open","closed","base","mid")

    sus "Это... это..."
    call nar(">Вы слышите, как Сьюзан делает глубокий вдох, перед тем, как заговорить.")
    sus "{size=+10}Это невероятно!{/size}"
    call ast_main("","grin","angry","angry","mid")
    sus "Это все фантастично!"
    call ast_main("","smile","base","base","mid")
    sus "Пятна спермы на задней стенке стола..."
    call ast_main("","disgust","narrow","base","mid")
    sus "Густой запах спермы в воздухе..."
    call ast_main("","disgust","narrow","narrow","R")
    sus "То, как Дамблдор гладит свой {b}член{/b}..."
    call ast_main("","clench","narrow","narrow","R")
    sus "Этот член... Это лучшая часть..."
    sus "Я просто хочу--"
    call ast_main("(Ииигх--...)","tongue_disgust","closed","narrow","R",trans="hpunch")

    sus "..."
    call nar(">Ты слышишь, как слова Сьюзан уходят в небытие, когда она делает еще один вдох...")
    sus "Я бы хотела жить здесь, внизу! Ты это хотела услышать, злая ведьма?!"
    call ast_main("Почти...","grin","narrow","narrow","down")
    call ast_main("Я хочу, что бы ты признала то, что ты шлюха...","grin","angry","angry","mid")
    call ast_main("Тогда я тебя отпущу...","open","closed","base","mid")
    sus "Правда? Это значит, что мне не придется..."
    sus "Хорошо..."
    sus "{size=-5}Я... {size=-3}шлюха...{/size}"
    call ast_main("Хммм, Я не уверена, что что-то расслышала... А ты, Дамби?","pout","base","base","R")
    m "Ах... почти..."
    call ast_main("Давай, Сюзи... еще раз...","smile","narrow","narrow","down")
    with hpunch
    sus "Я шлюха, да!"
    g4 "Ааааааа... ДАААА..."
    sus "Я противная шлюха, которая заползла под стол директора и--"

    g4 "СЕЙЧАС КОНЧУ, ШЛЮХА!"
    hide screen bld1
    call gen_chibi("cumming_behind_desk")
    call cum_block
    sus "Нет, подождите! Астория, ты же сказала, что я могу уйти--"
    call cum_block
    g4 "ААААГРХХХХ!!!"
    call nar("Отчаянные крики Сьюзен окончательно добивают тебя, кончая, твой член заливает мощной струей спермы лицо Сьюзен...")
    g4 "ВОТ ТЕБЕ ШЛЮХА!!!"
    call cum_block
    sus "..."

    call ast_main("Вот и все, [ast_genie_name]! Убедись, что ты закончил...","grin","angry","angry","mid")
    g4 "Аааагрх... не беспокойся об этом..."
    call nar(">Ты даешь своему члену сделать последние выстрелы, разбрызгивая остатки спермы по лицу Сьюзан...")

    call gen_chibi("cum_on_desk")
    pause.5
    g4 "Продолжим..."
    call ast_main("Отличная работа, [ast_genie_name]...","open","closed","base","mid")
    call ast_main("Ты можешь теперь идти, Сюзи...","smile","narrow","narrow","down")
    sus "..."
    hide screen astoria_main
    call blkfade

    call nar(">Сьюзен медленно выбирается из-под твоего стола...")

    $ susan_face_covered = True
    hide screen blkfade
    call sus_main("","upset","narrow","worried","L",xpos="mid",ypos="base",trans="fade")
    call ctc

    call ast_main("О мой бог! Он совершенно залил тебя!","scream","base","base","mid",xpos="close",ypos="base")
    call sus_main("...","upset","narrow","base","L")
    call ast_main("Я не знала, что у тебя ее так много, Дамби!","scream","wide","wide","wide")
    call ast_main("Отличная работа!","open","wide","wide","mid")
    m "Спасибо..."
    call ast_main("И Сюзи... это тебе идет.","grin","angry","angry","L")
    call sus_main("Ты закончила, Астория?","open","narrow","base","L")
    call ast_main("Да, теперь ты можешь идти, Сюзи...","smile","narrow","narrow","L")

    call nar(">Сьюзен, одеваясь, медленно вытирает сперму с лица.")

    hide screen susan_main
    $ susan_face_covered = False
    call sus_main("Надеюсь, вы двое счастливы...","upset","narrow","base","down")

    call play_sound("door")
    hide screen susan_main
    with d3
    pause.5

    call nar(">Она поворачивается и выбегает за дверь, слезы текут по ее лицу.")
    call ast_main("Ахахахахахаха, это было невероятно, Дамби!","happy","wide","wide","mid")
    call ast_main("Ты видел выражение лица этой шлюхи!","grin","ahegao","ahegao","ahegao")
    m "..."
    m "Да..."
    call ast_main("Что случилось, старик?","clench","angry","angry","mid")
    m "(Я создал монстра...)"
    m "Ничего... Это просто... тебе не кажется, что это немного слишком?"
    call ast_main("Пфффф... это именно то, что заслуживает эта шалава!","open","closed","angry","mid")
    call ast_main("Ей еще повезло, что я не заставила ее прикасаться к твоей мерзкой сосиске!","clench","angry","angry","down")
    m "..."
    call ast_main("И не говори мне, что ты добрый, старик!","pout","narrow","narrow","mid")
    m "Ну, обычно это происходит уже после того, как я--"
    call ast_main("Это не то, что я имела в виду!","clench","closed","angry","mid")
    call ast_main("Кроме того, эти заклинания, в первую очередь, были твоей идеей!","open","closed","base","mid")
    m "Я не думаю, что это--"
    call ast_main("В любом случае, уже поздно...","pout","narrow","narrow","R")
    call ast_main("Я лучше пойду в кровать.","open","closed","base","mid")
    m "Тьфу... Хмм... доброй ночи."
    call ast_main("Доброй ночи, [ast_genie_name]!","grin","happyCl","base","mid")

    call play_sound("door")
    hide screen astoria_main
    with d3
    pause.5

    call nar(">Астория выходит из твоего кабинета, напевая по дороге.")
    m "(Эта девочка еще хуже меня...)"

    $ astoria_busy = True
    $ susan_busy = True
    $ spells_locked = True #Locks spells until you send Astoria to Tonks.

    if astoria_affection < 3:
        $ astoria_affection = 3
        $ astoria_spell_progress = 0

    jump day_main_menu





#humiliate self for genie and astoria
#training labels are on the other page.

label hornify_spell_1: #first level hornify spell
    #Start grinding her hips in front of genie
label hornify_spell_2: #second level hornify spell
    #Takes her top of and starts shaking her boobs for genie
label hornify_spell_3: #third level hornify spell
    #Plays with herself in front of astoria and genie


label slutify_spell_1: #first level sluttify spell
    #Underwear becomes slutty
label slutify_spell_2: #second level sluttify spell
    #Skirt becomes short, vest only and slutty Underwear
label slutify_spell_3: #third level sluttify spell
    #Pink heart dress and no underwear


label orgasmio_spell_1: #first level orgasmio spell
    #Mild orgasm
label orgasmio_spell_2: #second level orgasmio spell
    #Intense orgasm
label orgasmio_spell_3: #third level orgasmio spell
    #Extreme orgasm, Astoria casts the spell multiple times






