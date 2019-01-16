

### Snape Chitchat ###

label snape_chitchat:
 
#    $ one_of_ten = renpy.random.randint(1, 10) #Generating one number out of three for various porpoises.

    ### WHORING LEVEL 01 ###
    if whoring >= 0 and whoring <= 2:
        if one_of_ten == 1:
            call sna_main("Ты правда думаешь, что сможешь это сделать?","snape_24") 
            call sna_main("Как думаешь, сможешь сломать эту девушку?","snape_25") 
        
        elif one_of_ten == 2:
            call sna_main("Разве ты не ненавидишь эту жалкую солнечную погоду?","snape_01") 
            call sna_main("Хотелось бы, чтобы дождь шел каждый день.","snape_06") 
            
        elif one_of_ten == 3:
            call sna_main("Я снова чувствую сомнение в отношении всего нашего плана ...","snape_06") 
            
        elif one_of_ten == 4:
            call sna_main("Вы уверены, что Вы не Альбус Дамблдор?","snape_05") 
            sna "Иногда мне все еще трудно поверить во все это..."
  
        elif one_of_ten == 5:
            call sna_main("Однажды я убил ученика.","snape_01") 
            call sna_main("Да... Я задушил паразита голыми руками.","snape_02") 
            call sna_main("........*рык*.","snape_03") 
            call sna_main("Это звучит правдоподобно?","snape_05") 
            call sna_main("Как только эти \"Табаки\" перестанут бояться меня,- мне конец.","snape_06") 
            call sna_main("Культивирование страха в сердцах своих учеников является самой важной задачей для каждого преподавателя.","snape_26") 

        elif one_of_ten == 6:
            call sna_main("Эти паразиты Уизли...","snape_04") 
            call sna_main("В один прекрасный день я просто сорвусь, клянусь.","snape_07") 

        elif one_of_ten == 7:
            call sna_main("Тебе не кажется, что почтовая сова немного смешна?","snape_05") 
            sna "Я бы предпочел использовать воронов."
            
        elif one_of_ten == 8:
            call sna_main("У меня был самый худший день в жизни...","snape_06") 
            sna "Так что я действительно не в настроении для болтовни..."
            
        elif one_of_ten == 9:
            call sna_main("Быть волшебником 24 часа в сутки...","snape_04") 
            call sna_main("7 дней в неделю...","snape_03") 
            call sna_main("365 дней в году, работа.","snape_04") 
            sna "Без выходных..."
            
        elif one_of_ten == 10:
            call sna_main("Квиддич...","snape_04") 
            call sna_main("Какая пустая трата времени и сил!","snape_10") 
            call sna_main("","snape_04") 
        
    
    ### WHORING LEVEL 02 ###
    if whoring >= 3 and whoring <= 5:
        if one_of_ten == 1:
            call sna_main("Я еще не заметил никаких изменений в поведении мисс Грейнджер...","snape_24") 
            call sna_main("Уверен, что знаешь, что делаешь?","snape_05") 
            call sna_main("","snape_09") 
        
        elif one_of_ten == 2:
            call sna_main("Уверен, это хорошо иметь возможность предоставлять очки факультету или забирать их. Мне это нравится.","snape_24") 
            sna "Мой авторитет среди студентов растет с каждым днем..."
            call sna_main("И когда я говорю \"авторитет\" Я имею в виду \"страх\".","snape_02") 

        elif one_of_ten == 3:
            call sna_main("Знаешь, что полнолуние, повышает мужскую потенцию?","snape_24") 
            sna "Это также облегчает фокусирование на задаче, что делает тебя более продуктивным."
            call sna_main("Но кого это вообще волнует, правильно я говорю?","snape_28") 
            call sna_main("","snape_29") 

        elif one_of_ten == 4:
            call sna_main("Мои прелестные Слизеринки, все это стоит этих мучений...","snape_06") 
            call sna_main("Их юбки становятся короче, каждую неделю, клянусь.","snape_19") 
  
        elif one_of_ten == 5:
            call sna_main("Было время, когда я был молод и полон надежд...","snape_06") 
            call sna_main("Ха-ха... Я шучу, приятель.","snape_28") 
            call sna_main("Я никогда не был полон надежд...","snape_29") 

        elif one_of_ten == 6:
            call sna_main("Кто-то вломился в мое личное хранилище...","snape_16") 
            call sna_main("Только взял немного gillyweed(жабросли)... повезло, что они не взяли ни одного из моих amorentia(приворотных зелий).","snape_29") 
            call sna_main("Не то, чтобы мне нужно использовать такие вещи.","snape_09") 

        elif one_of_ten == 7:
            call sna_main("A \"Движение за права мужчин\"...?","snape_05") 
            call sna_main("Что дальше? Движение за права домашних эльфов? (П.У.К.Н.И.-прим. переводчика)","snape_04") 
            call sna_main("Как может лучший студент быть таким тупым?","snape_06") 
            
        elif one_of_ten == 8:
            call sna_main("Я не завожу любимчиков, среди своих учеников.","snape_05") 
            call sna_main("Я просто терплю некоторых из них и ненавижу остальных.","snape_04") 
  
        elif one_of_ten == 9:
            call sna_main("В Хогвартсе есть четыре факультета...","snape_24") 
            sna "Слизерин, Когтевран, Гриффиндор и..."
            call sna_main("...и Пуфф, что-то...","snape_05") 
            call sna_main("Никого это не волнует.","snape_29") 
            call sna_main("","snape_09") 
 
        elif one_of_ten == 10:
            call sna_main("Метлы предназначены для детей и ведьм.","snape_24") 
            call sna_main("Вы никогда не увидите уважающего себя волшебника, летающего на метле.","snape_05") 
            call sna_main("","snape_09") 
        

    ### WHORING LEVEL 03 ###
    if whoring >= 6 and whoring <= 8:
        if one_of_ten == 1:
            call sna_main("Есть прогресс с нашей маленькой, мисс Всезнайкой?","snape_24") 
            call sna_main("","snape_09") 
        
        elif one_of_ten == 2:
            call sna_main("На днях эта девушка продала мне свои трусики за пять очков факультету.","snape_24") 
            call sna_main("И мужик, она была в восторге от этого...","snape_14") 
            call sna_main("Я думаю, она бы отдала их бесплатно, просто чтобы угодить мне.","snape_19") 
            call sna_main("","snape_09") 

        elif one_of_ten == 3:
            call sna_main("Пока день обещает быть приятным...","snape_23") 
            call sna_main("Спорим, ты не ожидал услышать, что я это скажу?","snape_02") 

        elif one_of_ten == 4:
            call sna_main("Квиддич, кажется, каждый год неуклонно набирает все большую популярность...","snape_24") 
            call sna_main("Какое разочарование...","snape_04") 

        elif one_of_ten == 5:
            call sna_main("Моя жизнь была невероятно скучной до твоего появления...","snape_24") 
            call sna_main("В настоящее время она...","snape_05") 
            call sna_main("...не такая скучная.","snape_02") 

        elif one_of_ten == 6:
            call sna_main("Сожаление? Я не знаю значения этого слова!","snape_05") 
            call sna_main("Я живу очень полноценной жизнью.","snape_06") 
            call sna_main("Ха-ха-ха! Прости, я просто не могу говорить такую чушь с серьезным лицом.","snape_28") 
            call sna_main("","snape_26") 

        elif one_of_ten == 7:
            call sna_main("Нет места ошибкам во время занятий.","snape_24") 
            call sna_main("Одна ошибка и эти чертовы ублюдки разорвут тебя на куски.","snape_04") 

        elif one_of_ten == 8:
            call sna_main("Ты единственный, перед кем я должен отчитываться...","snape_04") 
            call sna_main("Так, что я могу буквально делать все, что захочу...","snape_05") 
            call sna_main("...............","snape_09") 
            call sna_main("Так вот что такое свобода, хм?","snape_06") 

        elif one_of_ten == 9:
            call sna_main("Осень... самое депрессивное время года...","snape_06") 
            call sna_main("Я люблю ее!","snape_02") 
            call sna_main("","snape_23") 

        elif one_of_ten == 10:
            call sna_main("У меня в комнате висит волшебный портрет стриптизерши.","snape_24") 
            call sna_main("Одно из моих самых ценных вещей.","snape_22") 
            call sna_main("","snape_09") 
        

    ### WHORING LEVEL 04 ###
    if whoring >= 9 and whoring <= 11:
        if one_of_ten == 1:
            call sna_main("В последнее время мисс Грейнджер стала агрессивной, почти до открытой враждебности...","snape_24") 
            call sna_main("Надеюсь, ты знаешь, что делаешь...","snape_05") 
            call sna_main("","snape_09") 

        elif one_of_ten == 2:
            call sna_main("Я не должен чувствовать себя плохо из-за секса со своими студентами, верно?","snape_26") 
            call sna_main("Я имею в виду, ты должен видеть, как некоторые из этих девушек носят свою форму...","snape_05") 
            call sna_main("Они практически просят об этом.","snape_13") 
            call sna_main("","snape_12") 

        elif one_of_ten == 3:
            call sna_main("В последнее время часто идет дождь...","snape_23") 
            call sna_main("Интересно, нравится ли мне дождливая погода, просто потому, что она делает большинство людей несчастными...","snape_02") 
            call sna_main("","snape_23") 

        elif one_of_ten == 4:
            call sna_main("Согласно недавнему исследованию, 9 из 10 девочек тайно фантазируют о том, как их оскорбляет учитель.","snape_24") 
            call sna_main("Бьюсь об заклад, что 10-я девушка была Гермионой Грейнджер.","snape_03") 
            call sna_main("","snape_01") 

        elif one_of_ten == 5:
            call sna_main("Сейчас я должен прилагать усилия, чтобы сохранить видимость своего плохого настроения.","snape_24") 
            call sna_main("","snape_23") 

        elif one_of_ten == 6:
            call sna_main("У тебя есть лишние презервативы?","snape_24") 
            call sna_main("У меня есть целая пачка, но...","snape_25") 
            call sna_main("...их срок истек несколько лет назад...","snape_06") 
            call sna_main("Ты так изменил мою жизнь, приятель.","snape_02") 
            call sna_main("","snape_23") 

        elif one_of_ten == 7:
            call sna_main("Ты думаешь, мы могли бы превратить Хогвартс в школу \"только для девочек\"?","snape_24") 
            call sna_main("Академия Девочек Хогвартса!","snape_23") 
            call sna_main("Это было бы чертовски здорово... кроме, может быть Златопуста.","snape_13") 

        elif one_of_ten == 8:
            call sna_main("Почему учитель перешел дорогу?","snape_24") 
            call sna_main("Чтобы убежать от своих учеников!","snape_25") 
            call sna_main("Ха-ха-ха! Каждый раз!","snape_28") 
            call sna_main("","snape_25") 

        elif one_of_ten == 9:
            call sna_main("Хочешь услышать забавную историю?","snape_24") 
            call sna_main("Ну, я не знаю...","snape_06") 

        elif one_of_ten == 10:
            call sna_main("Знаешь ли, что \"Королевский Кубок\" есть?","snape_05") 
            call sna_main("Ты понимаешь, не так ли?","snape_13") 
            call sna_main("","snape_23") 

        
    ### WHORING LEVEL 05 ###
    if whoring >= 12 and whoring <= 14:
        if one_of_ten == 1:
            call sna_main("15 очков за минет - справедливая цена, не так ли?","snape_24") 
            call sna_main("","snape_23") 

        elif one_of_ten == 2:
            call sna_main("Ты когда-нибудь был влюблен, приятель?","snape_24") 
            call sna_main("А был влюблен в школьницу?","snape_02") 
            call sna_main("А как насчет полдюжины школьниц сразу?","snape_22") 
            call sna_main("","snape_20") 

        elif one_of_ten == 3:
            call sna_main("Что-то довольно невероятное произошло прошлой ночью между мной и одной Слизеринской шлюхой.","snape_20") 
            call sna_main("Короче говоря, все мои мышцы болят и я все еще чувствую себя опустошенным...","snape_22") 
            call sna_main("","snape_13") 

        elif one_of_ten == 4:
            call sna_main("В последнее время становится все прохладнее...","snape_24") 
            call sna_main("Зима близко...","snape_23") 
         
        elif one_of_ten == 5:
            call sna_main("Ты когда-нибудь видел маглов, одетых как ведьмы?","snape_24") 
            call sna_main("Так мило.","snape_19") 

        elif one_of_ten == 6:
            call sna_main("Знаешь, что такое \"Интернет\" ?","snape_24") 
            call sna_main("По-видимому, он позволяет выходить \"в сеть\" и увидеть волшебные фотографии обнаженных магловушек.","snape_02") # SNAPE SAYS "ON THE LINE" ON PURPOSE. I KNOW THAT WAS REALLY OBVIOUS MAESTRO
            call sna_main("Как бы мне хотелось, иметь такую вещь здесь, в Хогвартсе.","snape_26") 
            call sna_main("","snape_09") 

        elif one_of_ten == 7:
            call sna_main("У меня две главные страсти в жизни...","snape_24") 
            sna "Темные искусства..."
            call sna_main("......","snape_12") 
            call sna_main("...и шлюхи.","snape_13") 

        elif one_of_ten == 8:
            call sna_main("Ты думаешь, мне стоит отказаться от выпивки?","snape_24") 
            call sna_main("Но моя жизнь такая напряженная...","snape_06") 
            call sna_main("Хм...","snape_09") 
            call sna_main("Я попробую сократить употребление спиртного...","snape_06") 
            call sna_main("В пользу животного секса с одной моей ученицей!","snape_21") 
            call sna_main("","snape_19") 

        elif one_of_ten == 9:
            call sna_main("Мисс Грейнджер подозрительно молчит в последнее время...","snape_24") 
            call sna_main("Бьюсь об заклад, она что-то замышляет...","snape_03") 
            call sna_main("","snape_01") 

        elif one_of_ten == 10:
            call sna_main("Это довольно легко, написать книгу и убить половину главных героев ради драматического эффекта...","snape_24") 
            sna "Поставить своих персонажей против непобедимых противников и пусть они выживают правдоподобным образом..."
            call sna_main("Теперь {size=+7}это{/size} называется умением.","snape_02") 
            call sna_main("","snape_23") 
        
        
    ### WHORING LEVEL 06 ###
    if whoring >= 15 and whoring <= 17:
        if one_of_ten == 1:
            call sna_main("Что если эта девушка Грейнджер, не наша игрушка, а мы ее?","snape_11") 
            call sna_main("","snape_26") 

        elif one_of_ten == 2:
            call sna_main("Ты слышал о \"Клубе слизней\"?","snape_24") 
            sna "Что если я создам свой собственный клуб?"
            call sna_main("Я бы назвал его \"Клуб Снейпа\"!(прим. Slug Club, Snape Club-игра слов.)","snape_23") 
            sna "Я бы пригласил девушек, предложил им чай и кексы ..."
            call sna_main("Потискать немного их грудь...","snape_13") 
            call sna_main("Чертовски здорово!","snape_22") 
            call sna_main("","snape_02") 

        elif one_of_ten == 3:
            call sna_main("Скажи мне, Джинн... Тебе когда-нибудь вылизывала очко до чиста, молоденькая ведьмочка?","snape_02") 
            call sna_main("Жизненный опыт, ни больше, ни меньше...","snape_21") 
            call sna_main("","snape_02") 

        elif one_of_ten == 4:
            call sna_main("Итак, как проходит обучение?","snape_24") 
            sna "Надеюсь, все идет по плану?"
            call sna_main("","snape_05") 

        elif one_of_ten == 5:
            call sna_main("Знаешь, я вижу, Фестралов......","snape_06") 
            call sna_main("","snape_09") 

        elif one_of_ten == 6:
            call sna_main("Знаешь, что мне нравится в Квиддиче?","snape_24") 
            call sna_main("Ничего! Ни одной чертовой вещи!","snape_15") 
            call sna_main("","snape_16") 

        elif one_of_ten == 7:
            call sna_main("Хогвартс получил большую пользу от твоего прибытия.","snape_24") 
            call sna_main("Я сказал \"Хогвартс\"?. Я имею в виду \"себя\".","snape_02") 
            call sna_main("","snape_23") 

        elif one_of_ten == 8:
            call sna_main("Настоящие волшебники носят черное.","snape_24") 
            call sna_main("Я прав?","snape_02") 
            call sna_main("","snape_23") 

        elif one_of_ten == 9:
            call sna_main("Некоторые Слизеринские девченки, сейчас меня просто обожают...","snape_24") 
            call sna_main("Но я бы предпочел, лучше чтобы меня боялись...","snape_05") 
            call sna_main("Но я готов довольствоваться бессмысленным обожанием...","snape_23") 

        elif one_of_ten == 10:
            call sna_main("Ты слишком щедр с очками Гриффиндору, приятель.","snape_24") 
            call sna_main("В последнее время я едва успеваю за тобой, притормози приятель...","snape_25") 
            call sna_main("","snape_29") 
        
   
    ### WHORING LEVEL 07 ###
    if whoring >= 18 and whoring <= 20:
        if one_of_ten == 1:
            call sna_main("Мисс Грейнджер действительно меняется. Теперь я вижу это ясно...","snape_24") 
            sna "Ее оценки упали, и даже ее посещаемость сейчас далека от совершенства..."
            call sna_main("Но несмотря на это, она продолжает доставлять мне неприятности!","snape_10") 
            call sna_main("","snape_01") 

        elif one_of_ten == 2:
            call sna_main("Мой наименее любимый цвет?","snape_05") 
            call sna_main("Я назову два: красный и золотой.","snape_07") 
            call sna_main("","snape_04") 

        elif one_of_ten == 3:
            call sna_main("Я слышал, вампирская тема довольно популярна среди девушек в последнее время.","snape_24") 
            call sna_main("Из меня бы вышел отличный вампир, ты так не думаешь?","snape_05") 
            sna "Может, мне стоит прикупить пару бутафорских клыков..."
            call sna_main("Просто чтобы свести озабоченных шлюшек с ума.","snape_21") 
            call sna_main("","snape_02") 

        elif one_of_ten == 4:
            call sna_main("Я...ненавижу свою жизнь.","snape_24") 
            call sna_main("Нет, подожди, я скажу это еще раз...","snape_16") 
            call sna_main("Я...ненавижу свою жизнь.","snape_17") 
            call sna_main("Черт возьми! Я пытаюсь сказать \"люблю\", но это просто не выходит...","snape_25") 
            call sna_main("Я не припоминаю, чтобы я, когда-либо раньше использовал слова \"любовь\" и \"жизнь\" в одном предложении.","snape_29") 
            call sna_main("Позволь мне попробовать еще раз...","snape_06") 
            call sna_main("Я нен...{w} люб...{w} люблю свою жизнь!","snape_10") 
            call sna_main("Вот так, я люблю свою жизнь...","snape_23") 

        elif one_of_ten == 5:
            call sna_main("Солнечный свет, шоколад, Квиддич, кошки и апельсиновый сок...","snape_01") 
            sna "Это список вещей, которые мне не нравятся..."
            call sna_main("А вот краткий список вещей, который мне интересен...","snape_02") 
            call sna_main("Темные искусства, вино и писечки.","snape_23") 

        elif one_of_ten == 6:
            call sna_main("Ты когда-нибудь видел двух волшебников в кулачном бою?","snape_02") 
            call sna_main("Чертовски весело!","snape_28") 
            call sna_main("","snape_23") 

        elif one_of_ten == 7:
            call sna_main("Знаешь это чувство, когда только, что кончил в рот девушки, и она все это проглатывает и говорит: \"Благодарю вас, профессор\"?","snape_14") 
            call sna_main("Разве это не самое лучшее?","snape_13") 
            call sna_main("","snape_23") 

        elif one_of_ten == 8:
            call sna_main("Как думаешь, призраки Хогвартса иногда шпионят за девушками, когда они принимают душ и тому подобное?","snape_24") 
            call sna_main("Если бы я был призраком, я бы так и делал.","snape_13") 
            call sna_main("","snape_23") 

        elif one_of_ten == 9:
            call sna_main("Одна девушка призналась мне, что она часто фантазирует о том, что над ней доминирует мистер Филч.","snape_19") 
            call sna_main("Думаю, я смогу это устроить. Нужно ли это мне?!","snape_14") 
            call sna_main("","snape_02") 

        elif one_of_ten == 10:
            call sna_main("Раньше я так ненавидел свою работу...","snape_24") 
            call sna_main("Ненависть чистая, простая и бесспорная...","snape_06") 
            call sna_main("Нынче, не поймите меня превратно - я все еще ненавижу ее.","snape_09") 
            call sna_main("Но в то же время, мне она сейчас и нравится...","snape_05") 
            sna "Как я мог, не? Что происходит в последнее время?"
            call sna_main("И лелеять и ненавидеть что-то к равной степени...","snape_06") 
            call sna_main("Это как снова влюбиться...","snape_19") 
            call sna_main("","snape_06") 
        
        
    ### WHORING LEVEL 08+ ###
    if whoring >= 21:
        if one_of_ten == 1:
            call sna_main("Знаешь, что такое \"bukkake\"?","snape_24") 
            sna "Как насчет \"deepthroating\"?"
            sna "А потом появилась \"hate-sex\"."
            call sna_main("Современные дети, приятель...","snape_05") 
            sna "У них есть специальное название для всего."
            call sna_main("Хотя \"hate-sex\" всегда был...","snape_06") 
            call sna_main("В мои дни мы это просто называли \"sex\".","snape_02") 

        elif one_of_ten == 2:
            call sna_main("Сегодня я услышал таинственный тикающий шум...","snape_04") 
            call sna_main("Это было довольно запоминающимся...","snape_28") 

        elif one_of_ten == 3:
            call sna_main("На днях я организовал небольшую вечеринку...","snape_24") 
            sna "Одна девочка и три мальчика..."
            call sna_main("Они трахали ее, и я смотрел...","snape_13") 
            call sna_main(".........................","snape_29") 
            call sna_main("Думаешь, в последнее время я слишком часто практикую темную сторону?","snape_05") 
            call sna_main("","snape_06") 

        elif one_of_ten == 4:
            call sna_main("У меня кончились презервативы, приятель.","snape_24") 
            call sna_main("Думаешь, я могу подцепить болезнь?","snape_02") 
            call sna_main("","snape_01") 

        elif one_of_ten == 5:
            call sna_main("Я готовлю тайное зелье на травах, которое заставит ее соски выделять молоко...","snape_24") 
            call sna_main("Гениально, да?","snape_13") 
            call sna_main("","snape_23") 

        elif one_of_ten == 6:
            call sna_main("Значит, у этой ведьмы во рту мой член, верно?","snape_24") 
            call sna_main("Ее горяченькая подружка вылизывает мой анус своим язычком...","snape_02") 
            sna "Между тем, третья девушка стоит на коленях с открытым ртом, ожидая, когда я плюну в него..."
            sna "И каждый раз, когда я плюю, она говорит: \"Спасибо, профессор Снейп\"."
            call sna_main("Это был чертовски сюрреалистичный вечер...","snape_22") 
            call sna_main("","snape_02") 

        elif one_of_ten == 7:
            call sna_main("Эта девушка уже несколько дней умоляла меня, пописать ей в рот...","snape_06") 
            sna "Настойчивая маленькая шалунья..."
            call sna_main("Должен ли я сделать это?","snape_05") 
            call sna_main("","snape_23") 

        elif one_of_ten == 8:
            call sna_main("Я беспощадно доминирую и над студентами и над студентками...","snape_04") 
            call sna_main("Но совершенно по-разному.","snape_22") 
            call sna_main("","snape_23") 

        elif one_of_ten == 9:
            call sna_main("Я люблю свою жизнь!","snape_23") 
            call sna_main("Все еще ненавижу свою работу...","snape_16") 
            call sna_main("Я бы хотел пропускать занятия по обучению студенток, но не когда я их трахаю.","snape_14") 
            call sna_main("","snape_23") 

        elif one_of_ten == 10:
            call sna_main("Мне почти стыдно, за то, что мне весело.","snape_24") 
            call sna_main("Хочешь, я пришлю тебе какую-нибудь молодую шлюшку?","snape_14") 
            call sna_main("","snape_23") 
    

    return
    
