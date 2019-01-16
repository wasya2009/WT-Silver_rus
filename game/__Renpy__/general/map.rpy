

### Map Screen ###

screen map_screen:
    zorder hermione_main_zorder-1
    
    imagemap:
        ground "interface/map/map_ground.png"
        idle "interface/map/map_idle.png"
        hover "interface/map/map_hover.png"
        # (X upper-left corner, Y upper-left corner, width, height).
        hotspot (192+140, 229, 38, 20) clicked Jump("map_attic") #attic
        hotspot (272+140, 373, 63, 41) clicked Jump("clothes_store") #clothes
        hotspot (25+140, 374, 102, 66) clicked Jump("map_forest") #forest
        hotspot (302+140, 523, 112, 49) clicked Jump("map_lake") #lake
        hotspot (273+140, 459, 75, 8) clicked Jump("map_dorms") #dorms
        #hotspot (656+140, 232, 106, 33) clicked Jump("inn_menu") #inn
        #hotspot (376+140, 84, 111, 57) clicked Jump("map_pitch") #pitch
        hotspot (307+140, 240, 59, 37) clicked Jump("shop_intro") #shop
        hotspot (33+140, 535, 39, 39) clicked Jump("day_main_menu") #return
        

###MAP LOCATIONS AND RESPONSES
# TODO: change how "random" chance works for getting items from locations or immplement a 
# limit to searching an area b/c currenly if day_random is above a vlaue the player can get
# as many items as they want
label map_attic: #Label controlling what happens when you access the attic
    if not attic_open:
        ">Ты поднимаешься на чердак, но обнаруживаешь, что дверь заперта."
        m "Черт, она заперта."
        m "Полагаю, мне нужно спросить Снейпа о ключе."
        jump return_office
    if attic_open and tentacle_owned:
        ">Вы отправляетесь на чердак и находите злое растение с щупальцами."
        m "Лучше убраться отсюда, пока растение не вспомнило, что я тот, кто его разрезал."
        ">Ты быстро возвращаешься в свою башню."
        jump return_office
    else: #Scene where genie has to take a sample of the devil's snare plant
        ">Вы пробираетесь через извилистые лестницы к чердачной двери."
        m "Хммм, кажется, она открыта."
        ">Вы проходите сквозь пыльную комнату, слегка освещенную через окна."
        m "Ну где же это волшебное растение?"
        ">Виден тонкий кусочек виноградной лозы, огибающий помещение, как бы избегая света."
        m "Это должно быть оно."
        ">Ты режешь кусочек и уходишь."
        ">Когда ты закрываешь дверь, слышишь, как в комнате что-то громко грохочет."
        $ tentacle_owned = True
        jump return_office


label map_forest: #Label controlling what happens when you go to the forest
    if daytime:
        m "Я действительно не должен покидать башню в течение дня. Это слишком рискованно..."
        jump day_main_menu
    else:
        pass
        
    call outskirts_of_hogwarts 
    
    m "Посмотрим, что я смогу найти здесь..."
        
    menu:
        "-Обыскать местность-":
            if day_random >= 7:
                ">Ты ищешь вокруг леса и тебе удается найти странно выглядящие травы."
                m "Это должно быть Wormwood."
                menu: 
                    "-Взять Wormwood-":
                        ">Ты получаешь Wormwood 1шт."
                        $ potion_inv.add("ing_wormwood")
                    "-Выбросить-":
                        pass
                ">Не найдя ничего интересного, ты возвращаешься в свою башню."
                jump return_office
            elif day_random > 5:
                ">Ты ищешь вокруг леса и тебе удается найти странно выглядящие травы."
                m "Это должно быть Трава-Мурава."
                menu: 
                    "-Взять Knotgrass-":
                        ">Ты получаешь Knotgrass 1шт."
                        $ potion_inv.add("ing_knotgrass")
                    "-ВЫбросить-":
                        pass
                ">Не найдя более ничего интересного, ты возвращаешься в свою башню."
                jump return_office
            else:
                ">Ты обыскиваешь лес, но не смог найти ничего интересного."
                jump return_office
   
label map_lake: #Label controlling what happens when you go to the lake
    if daytime:
        m "Я действительно не должен покидать замок в течение дня. Это слишком рискованно..."
        jump day_main_menu
    else:
        pass
    call outskirts_of_hogwarts 
    
    m "Посмотрим, что я смогу здесь найти..." 
    
    menu:
        "-Обыскать местность-":
            if day_random >= 7:
                ">Ты ищешь вокруг озера и сумел найти тонкую, зеленую виноградную лозу."
                m "Это должно быть Niffler's Fancy.."
                menu: 
                    "-Взять Niffler's Fancy-":
                        ">Ты получаешь Niffler's Fancy 1шт."
                        $ potion_inv.add("ing_niffler_fancy")
                    "-Выбросить-":
                        pass
                ">Не найдя более ничего интересного, ты возвращаешься в свою башню."
                jump return_office
            elif day_random > 5:
                ">Ты ищешь вокруг озера и удается найти торчащий корень, похожий на имбирь."
                m "Это должно быть корень Волчей отравы."
                menu: 
                    "-Взять Root of Aconite-":
                        ">Ты получаешь Root of Aconite 1шт."
                        $ potion_inv.add("ing_aconite_root")
                    "-Выбросить-":
                        pass
                ">Не найдя более ничего интересного, ты возвращаешься в свою башню."
                jump return_office
            else:
                ">Ты обыскиваешь озеро, но не смог найти ничего интересного."
                jump return_office  

label map_dorms: #Label controlling what happens when you go to the dorms
    menu:
        "-Обыскать местность-":#Luna's Hair
            if day_random >= 7:
                ">Ты обыскиваешь общежития и сумел найти комок ярко-оранжевого меха."
                m "Он должен принадлежать какому-то животному."
                menu: 
                    "-Взять мех-":
                        ">Ты получаешь Клок Шерсти 1шт."
                        $ potion_inv.add("ing_cat_hair")
                    "-Выбросить-":
                        pass
                ">Не найдя более ничего интересного, ты возвращаешься в свою башню."
                jump return_office
            elif day_random > 5:
                ">Ты обыскиваешь общежития и удается найти расческу с волосами в ней."
                m "Это вероятно чьи-то волосы."
                menu: 
                    "-Взять волосы-":
                        ">Ты получаешь Волос Полумны - 1шт."
                        $ potion_inv.add("ing_luna_hair")
                    "-Выбросить-":
                        pass
                ">Не найдя более ничего интересного, ты возвращаешься в свою башню."
                jump return_office
            else:
                ">Ты обыскиваешь общежития, но не смог найти ничего интересного."
                jump return_office         
            
label map_pitch: #Label controlling what happens when you go to the quidditch pitch
    if pitch_open:
        hoo "Здравствуйте, профессор Дамблдор, рада вас видеть сегодня вне кабинета."
        hoo "Что привело вас сегодня на поле для Квиддича?"
        m "Квиддич, что это за имя такое?" #put in low talking tone
        hoo "Вы о чем?"
        m "Ничего, просто комментирую погоду." #Maybe change this
        hoo "Хорошо я рада, что Вы здесь. Я хотела поговорить с вами о насущной проблеме, которая тревожит меня в данный момент."
        m "Что случилось?"
        hoo "Посещаемость матчей по квиддичу медленно снижается в течении последних нескольких месяцев."
        hoo "Кажется, студенты просто не хотят появляться, чтобы смотреть, как играют их команды. Это влияет на их боевой дух."
        m "И как бы вы хотели это исправить?"
        hoo "Возможно, мы могли бы сделать участие в матче обязательным."
        m "Не думаю, что это сработает. Если бы я это сделал, вы бы просто получили много недовольных студентов, освистывающих свою собственную команду."
        m "Если уже плохая посещаемость уменьшает моральный дух, представляю, что будет в этом случае."
        hoo "Тогда что вы предлагаете?"
        m "Вам нужен способ привлечь толпу. Чтобы привести сюда студентов и заставить их аплодировать."
        m "Вам нужна команда поддержки."
        hoo "Что?"
        m "Команда девушек, танцующих и подбадривающих свою команду. Чтобы их сокурсники были полны энтузиазма."
        hoo "Я не уверена, сэр, Хогвартс всегда был традиционной школой."
        hoo "Но нужно, что-то делать со сложившейся ситуацией."
        m "Хорошо, если вы так чувствуете, я думаю, вам просто нужно согласиться с тем, что число студентов, наблюдающих за игрой, уменьшается."
        hoo "Отлично, но мне не нравится команда из этих \"Болельщиц\". В лучшем случае мне было бы комфортно с одной танцующей девушкой." #Maybe adjust this so that there is a team
        m "Думаю, у меня есть идеальный кандидат. Я отправлю ее на следующую тренировку, чтобы попробовать."
        hoo "Хорошо, просто убедитесь, что она одета подобающе."
        $ pitch_first = False
        jump return_office
    else:
        ">Вы осматриваете поле, но не видите ни студентов, ни учителей"
        m "Не должно быть практики."
        jump return_office
            
label outskirts_of_hogwarts:
    call blkfade 
    hide screen genie
    show screen chair_left
    show screen desk
    call gen_chibi("stand","desk","base") 
    call hide_blkfade 
        
    call gen_walk("desk","leave",3) 
    call blkfade 
        
    stop music fadeout 1.0
    
    centered "{size=+7}{color=#cbcbcb}Окрестности Хогвартса{/color}{/size}"

    play music "sounds/night.mp3" fadein 1 fadeout 1 #NIGHT SOUNDS.
    
    show screen blkback # Hide room

    $ end_u_1_pic =  "images/yule_ball/171.png"
    show screen end_u_1
    pause.3
    call hide_blkfade 
    pause.8
    $ renpy.play('sounds/steps_grass.mp3') # SOUNDS OF STEPS IN THE GRASS.
    $ end_u_3_pic =  "images/yule_ball/172.png"
    show screen end_u_3
    with d7 
    
    return
    
label return_office:
    call blkfade 
    #">You return to your office."
    
    hide screen end_u_1
    hide screen end_u_3
    hide screen chair_left
    hide screen desk
    call gen_chibi("hide") 
    show screen genie
    hide screen blkback
    pause.5
    call hide_blkfade 
    
    if daytime:
        jump day_main_menu
    else:
        jump night_main_menu
