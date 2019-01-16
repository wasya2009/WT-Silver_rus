﻿

screen wardrobe():
    
    tag wardrobe_menu
    zorder hermione_main_zorder-1

    if active_girl == "hermione":
        $ icon_ypos_offset = 0
    if active_girl == "astoria": #She's too small! >.<
        $ icon_ypos_offset = -20
        $ wardrobe_toggle_page = 4 #Force disables toggle pages.
    if active_girl == "susan":
        $ icon_ypos_offset = 0
        $ wardrobe_toggle_page = 4 #Force disables toggle pages.
        
    imagemap:
        cache False
        

        ## Ground & Hovers-utf ##
        if wardrobe_page == 0: #default
            add "interface/wardrobe/"+str(interface_color)+"/icons_"+str(active_girl)+".png" zoom 0.5
            ground "interface/wardrobe/"+str(interface_color)+"/ground_right_"+str(wardrobe_color)+".png"
            hover "interface/wardrobe/"+str(interface_color)+"/hover_right_"+str(wardrobe_color)+".png"
        elif wardrobe_page == 1: #hair
            add "interface/wardrobe/"+str(interface_color)+"/icons_"+str(active_girl)+"_hair.png" zoom 0.5
            ground "interface/wardrobe/"+str(interface_color)+"/ground_full_"+str(wardrobe_color)+".png"
            hover "interface/wardrobe/"+str(interface_color)+"/hover_full_"+str(wardrobe_color)+".png"
        elif wardrobe_page == 2: #tops
            add "interface/wardrobe/"+str(interface_color)+"/icons_"+str(active_girl)+"_tops.png" zoom 0.5
            ground "interface/wardrobe/"+str(interface_color)+"/ground_full_"+str(wardrobe_color)+".png"
            hover "interface/wardrobe/"+str(interface_color)+"/hover_full_"+str(wardrobe_color)+".png"
        elif wardrobe_page == 3: #bottoms
            add "interface/wardrobe/"+str(interface_color)+"/icons_"+str(active_girl)+"_bottoms.png" zoom 0.5
            ground "interface/wardrobe/"+str(interface_color)+"/ground_full_"+str(wardrobe_color)+".png"
            hover "interface/wardrobe/"+str(interface_color)+"/hover_full_"+str(wardrobe_color)+".png"
        elif wardrobe_page == 4: #other clothings
            add "interface/wardrobe/"+str(interface_color)+"/icons_"+str(active_girl)+"_stockings.png" zoom 0.5
            ground "interface/wardrobe/"+str(interface_color)+"/ground_full_"+str(wardrobe_color)+".png"
            hover "interface/wardrobe/"+str(interface_color)+"/hover_full_"+str(wardrobe_color)+".png"
        elif wardrobe_page == 5: #accessories
            add "interface/wardrobe/"+str(interface_color)+"/icons_"+str(active_girl)+"_accessories.png" zoom 0.5
            ground "interface/wardrobe/"+str(interface_color)+"/ground_full_"+str(wardrobe_color)+".png"
            hover "interface/wardrobe/"+str(interface_color)+"/hover_full_"+str(wardrobe_color)+".png"
        elif wardrobe_page == 6: #underwear
            add "interface/wardrobe/"+str(interface_color)+"/icons_"+str(active_girl)+"_underwear.png" zoom 0.5
            ground "interface/wardrobe/"+str(interface_color)+"/ground_full_"+str(wardrobe_color)+".png"
            hover "interface/wardrobe/"+str(interface_color)+"/hover_full_"+str(wardrobe_color)+".png"
        elif wardrobe_page == 7: #outfits
            add "interface/wardrobe/"+str(interface_color)+"/icons_"+str(active_girl)+"_outfits.png" zoom 0.5
            ground "interface/wardrobe/"+str(interface_color)+"/ground_full_"+str(wardrobe_color)+".png"
            hover "interface/wardrobe/"+str(interface_color)+"/hover_full_"+str(wardrobe_color)+".png"
        elif wardrobe_page == 8: #gifts
            add "interface/wardrobe/"+str(interface_color)+"/icons_"+str(active_girl)+"_gifts.png" zoom 0.5
            ground "interface/wardrobe/"+str(interface_color)+"/ground_full_"+str(wardrobe_color)+".png"
            hover "interface/wardrobe/"+str(interface_color)+"/hover_full_"+str(wardrobe_color)+".png"
            


        ## Always Active ##
        hotspot (745+280,10,45,45) clicked [SetVariable("wardrobe_page",0),Jump("close_wardrobe")]    #Close Wardrobe and set to default.
        if active_girl == "hermione":
            text ""+hermione_name xalign 0.5 xpos 820 ypos 57 size 20
        if active_girl == "astoria":
            text ""+astoria_name xalign 0.5 xpos 820 ypos 57 size 20
        if active_girl == "susan":
            text ""+susan_name xalign 0.5 xpos 820 ypos 57 size 20
        text "Гардероб" xpos 668 ypos 154+360 size 12

        hotspot (993,10,32,23) clicked Jump("hide_wardrobe")

        #Wardrobe background color
        for i in range(0,len(wr_background_color)):
            $ col = i % 5

            hotspot (667+(20*col), 559, 20, 20) clicked [SetVariable("wardrobe_color",wr_background_color[i]), Jump("update_wardrobe_color")]
            add "interface/wardrobe/icons/colors/"+wr_background_color[i]+".png" xpos 668+(20*col) ypos 560

        
        ## Page Specific Hotspots ##
        if wardrobe_page == 0: #default #Not used yet.
            pass
        else:
            pass

        #Hair
        if wardrobe_page == 1:
            hotspot (561, 122, 86, 93) clicked [SetVariable("wardrobe_page_choice",0),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #return to default
            text "Прическа & Акс." xalign 0.5 xpos 208 ypos 96 size 18
        else:
            hotspot (609, 122, 38, 93) clicked [SetVariable("wardrobe_page_choice",1),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #default

        #Tops
        if wardrobe_page == 2:
            hotspot (561, 232, 86, 93) clicked [SetVariable("wardrobe_page_choice",0),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #return to default
            text "Одежда-Выше Пояса" xalign 0.5 xpos 208 ypos 96 size 18
        else:
            hotspot (609, 232, 38, 93) clicked [SetVariable("wardrobe_page_choice",2),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #default

        #Bottoms
        if wardrobe_page == 3:
            hotspot (561, 342, 86, 93) clicked [SetVariable("wardrobe_page_choice",0),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")]
            text "Одежда-Ниже Пояса" xalign 0.5 xpos 208 ypos 96 size 18
        else:
            hotspot (609, 342, 38, 93) clicked [SetVariable("wardrobe_page_choice",3),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")]

        #Other Clothings
        if wardrobe_page == 4:
            hotspot (561, 452, 86, 93) clicked [SetVariable("wardrobe_page_choice",0),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #return to default
            text "Акссесуары и др." xalign 0.5 xpos 208 ypos 96 size 18
        else:
            hotspot (609, 452, 38, 93) clicked [SetVariable("wardrobe_page_choice",4),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #default

        #Miscellaneous Accessories
        if wardrobe_page == 5:
            hotspot (987, 122, 84, 93) clicked [SetVariable("wardrobe_page_choice",0),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #return to default
            text "Разное" xalign 0.5 xpos 208 ypos 96 size 18
        else:
            hotspot (987, 122, 40, 93) clicked [SetVariable("wardrobe_page_choice",5),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #default

        #Underwear
        if wardrobe_page == 6:
            hotspot (987, 232, 84, 93) clicked [SetVariable("wardrobe_page_choice",0),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #return to default
            text "Нижнее Белье" xalign 0.5 xpos 208 ypos 96 size 18
        else:
            hotspot (987, 232, 40, 93) clicked [SetVariable("wardrobe_page_choice",6),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")]

        #Outfits
        if wardrobe_page == 7:
            hotspot (987, 342, 84, 93) clicked [SetVariable("wardrobe_page_choice",0),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #return to default
            text "Костюмы & Наряды" xalign 0.5 xpos 208 ypos 96 size 18
        else:
            hotspot (987, 342, 40, 93) clicked [SetVariable("wardrobe_page_choice",7),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #default

        #Gifts
        if wardrobe_page == 8:
            hotspot (987, 452, 84, 93) clicked [SetVariable("wardrobe_page_choice",0),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #return to default
            text "Подарки & Квест Предм." xalign 0.5 xpos 208 ypos 96 size 18
        else:
            hotspot (987, 452, 40, 93) clicked [SetVariable("wardrobe_page_choice",8),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #default


### ON/OFF Toggles ###

        if wardrobe_toggle_page == 0: #Default Page
            hotspot (658,89,76,13) clicked [SetVariable("wardrobe_toggle_page",1),Show("wardrobe")]
            hotspot (734,89,76,13) clicked [SetVariable("wardrobe_toggle_page",2),Show("wardrobe")]
            hotspot (810,89,76,13) clicked [SetVariable("wardrobe_toggle_page",3),Show("wardrobe")]
            text "Одежда" xalign 0.5 xpos 658+38 ypos 90 size 12 
            text "Акс." xalign 0.5 xpos 734+38 ypos 90 size 12
            text "Поза" xalign 0.5 xpos 810+38 ypos 90 size 12
        if wardrobe_toggle_page == 1: #Clothing
            hotspot (658,89,74,13) clicked [SetVariable("wardrobe_toggle_page",0),Show("wardrobe")]
            hotspot (734,89,74,13) clicked [SetVariable("wardrobe_toggle_page",2),Show("wardrobe")]
            hotspot (810,89,76,13) clicked [SetVariable("wardrobe_toggle_page",3),Show("wardrobe")]
            text "Одежда" xalign 0.5 xpos 658+38 ypos 89 size 14
            text "Акс." xalign 0.5 xpos 734+38 ypos 90 size 12
            text "Поза" xalign 0.5 xpos 810+38 ypos 90 size 12
        if wardrobe_toggle_page == 2: #Accessories
            hotspot (658,89,74,13) clicked [SetVariable("wardrobe_toggle_page",1),Show("wardrobe")]
            hotspot (734,89,74,13) clicked [SetVariable("wardrobe_toggle_page",0),Show("wardrobe")]
            hotspot (810,89,76,13) clicked [SetVariable("wardrobe_toggle_page",3),Show("wardrobe")]
            text "Одежда" xalign 0.5 xpos 658+38 ypos 90 size 12 
            text "Акс." xalign 0.5 xpos 734+38 ypos 89 size 14
            text "Поза" xalign 0.5 xpos 810+38 ypos 90 size 12
        if wardrobe_toggle_page == 3: #Pose
            hotspot (658,89,74,13) clicked [SetVariable("wardrobe_toggle_page",1),Show("wardrobe")]
            hotspot (734,89,74,13) clicked [SetVariable("wardrobe_toggle_page",2),Show("wardrobe")]
            hotspot (810,89,76,13) clicked [SetVariable("wardrobe_toggle_page",0),Show("wardrobe")]
            text "Одежда" xalign 0.5 xpos 658+38 ypos 90 size 12
            text "Акс." xalign 0.5 xpos 734+38 ypos 90 size 12
            text "Поза" xalign 0.5 xpos 810+38 ypos 89 size 14

        #Toggle Clothing
        if wardrobe_toggle_page == 1 or (wardrobe_toggle_page == 0 and wardrobe_page == 2 
                                      or wardrobe_toggle_page == 0 and wardrobe_page == 3 
                                      or wardrobe_toggle_page == 0 and wardrobe_page == 4  
                                      or wardrobe_toggle_page == 0 and wardrobe_page == 6  
                                      or wardrobe_toggle_page == 0 and wardrobe_page == 7):

            ## Top Toggle ##
            if whoring >= 12 and wardrobe_page != 6:
                hotspot (667,120,18,18) clicked Jump("her_top_toggle")
                if h_request_wear_top:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115 #ypos-5 of hotspot ypos #2nd row Ypos+25
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115
                text "Верх" xpos 688 ypos 124 size 10
            else:
                if h_request_wear_top:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true_hidden.png" xpos 667 ypos 115 #grayed out
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false_hidden.png" xpos 667 ypos 115 #grayed out
                text "{color=#858585}Верх{/color}" xpos 688 ypos 124 size 10            #grayed out

            ## One-Pieces ##
            if whoring >= 12:
                hotspot (667,120+25,18,18) clicked Jump("her_onepiece_toggle")
                if hermione_wear_onepiece:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+25 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+25
                text "Комбинация" xpos 688 ypos 124+25 size 10
            else:
                if hermione_wear_onepiece:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true_hidden.png" xpos 667 ypos 115+25 #grayed out
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false_hidden.png" xpos 667 ypos 115+25 #grayed out
                text "{color=#858585}Комбинация{/color}" xpos 688 ypos 124+25 size 10          #grayed out

            ## Bra Toggle ##
            if whoring >= 12:
                hotspot (667+5,120+50,18,18) clicked Jump("her_bra_toggle")
                if hermione_wear_bra:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667+5 ypos 115+50 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667+5 ypos 115+50
                text "Бюстгальтер" xpos 688+5 ypos 124+50 size 10
            else:
                if hermione_wear_bra:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true_hidden.png" xpos 667+5 ypos 115+50 #grayed out
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false_hidden.png" xpos 667+5 ypos 115+50 #grayed out
                text "{color=#858585}Бюстгальтер{/color}" xpos 688+5 ypos 124+50 size 10          #grayed out

            ## Bottom Toggle ##
            if whoring >= 12 and wardrobe_page != 6:
                hotspot (667,120+75,18,18) clicked Jump("her_bottom_toggle")
                if h_request_wear_bottom:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+75 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+75
                text "Попа" xpos 688 ypos 124+75 size 10
            else:
                if h_request_wear_bottom:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true_hidden.png" xpos 667 ypos 115+75 #grayed out
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false_hidden.png" xpos 667 ypos 115+75 #grayed out
                text "{color=#858585}Попа{/color}" xpos 688 ypos 124+75 size 10          #grayed out

            ## Panties Toggle ##
            if whoring >= 12:
                hotspot (667+5,120+100,18,18) clicked Jump("her_panties_toggle")
                if hermione_wear_panties:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667+5 ypos 115+100 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667+5 ypos 115+100
                text "Трусики" xpos 688+5 ypos 124+100 size 10
            else:
                if hermione_wear_panties:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true_hidden.png" xpos 667+5 ypos 115+100 #grayed out
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false_hidden.png" xpos 667+5 ypos 115+100 #grayed out
                text "{color=#858585}Трусики{/color}" xpos 688+5 ypos 124+100 size 10          #grayed out

            ## Garterbelt Toggle ##
            if whoring >= 12:
                hotspot (667+5,120+125,18,18) clicked Jump("her_garterbelt_toggle")
                if hermione_wear_garterbelt:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667+5 ypos 115+125 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667+5 ypos 115+125
                text "Подвязки" xpos 688+5 ypos 124+125 size 10
            else:
                if hermione_wear_garterbelt:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true_hidden.png" xpos 667+5 ypos 115+125 #grayed out
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false_hidden.png" xpos 667+5 ypos 115+125 #grayed out
                text "{color=#858585}Подвязки{/color}" xpos 688+5 ypos 124+125 size 10          #grayed out

            ## Neckwear ##
            if whoring >= 0: #
                hotspot (667,120+150,18,18) clicked Jump("her_neckwear_toggle")
                if hermione_wear_neckwear:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+150 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+150
                text "Шея" xpos 688 ypos 124+150 size 10
            else:
                pass

            ## Body Accessories Toggle ##
            if whoring >= 0:
                hotspot (667,120+175,18,18) clicked [SetVariable("toggle_obj","body_accs"), Jump("her_body_accs_toggle")]
                if hermione_wear_body_accs:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+175 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+175
                text "Акс. Тела" xpos 688 ypos 124+175 size 10
            else:
                if hermione_wear_body_accs:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true_hidden.png" xpos 667 ypos 115+175 #grayed out
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false_hidden.png" xpos 667 ypos 115+175 #grayed out
                text "{color=#858585}Акс. Тела{/color}" xpos 688 ypos 124+175 size 10          #grayed out

            ## Gloves ##
            if whoring >= 0:
                hotspot (667,120+200,18,18) clicked Jump("her_gloves_toggle")
                if hermione_wear_gloves:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+200 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+200
                text "Перчатки" xpos 688 ypos 124+200 size 10
            else:
                pass

            ## Stockings Toggle ##
            if whoring >= 0:
                hotspot (667,120+225,18,18) clicked Jump("her_stockings_toggle")
                if hermione_wear_stockings:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+225 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+225
                text "Чулки" xpos 688 ypos 124+225 size 10
            else:
                pass

            ## Robe Toggle ##
            if whoring >= 0:
                hotspot (667,120+250,18,18) clicked Jump("her_robe_toggle")
                if hermione_wear_robe:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+250 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+250
                text "Мантия" xpos 688 ypos 124+250 size 10
            else:
                pass

            ## Outfit Toggle ##
            if whoring >= 0:
                hotspot (667,120+285,18,18) clicked [SetVariable("wardrobe_costume_selection",None),Jump("wardrobe_wear_costume")] #"wardrobe_costume_selection",None #wardrobe_wear_costume
                if not wardrobe_costume_selection:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+285 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+285
                text "Наряд" xpos 688 ypos 124+285 size 10
            else:
                pass

        #Toggle Accessories
        if wardrobe_toggle_page == 2 or (wardrobe_toggle_page == 0 and wardrobe_page == 1 
                                     or wardrobe_toggle_page == 0 and wardrobe_page == 5 
                                         ):

            ## Head Accessory Toggle ##
            if whoring >= 0:
                hotspot (667,120,18,18) clicked [SetVariable("toggle_obj","hat"), Jump("her_hat_toggle")]
                if hermione_wear_hat:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115 #ypos-5 of hotspot ypos #2nd row Ypos+25
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115
                text "Убор" xpos 688 ypos 124 size 10
            else:
                pass

            ## Glasses Toggle ##
            if whoring >= 0:
                hotspot (667,120+25,18,18) clicked [SetVariable("toggle_obj","glasses"), Jump("her_glasses_toggle")]
                if hermione_wear_glasses:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+25 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+25
                text "Очки" xpos 688 ypos 124+25 size 10
            else:
                pass

            ## Ears Toggle ##
            if whoring >= 0:
                hotspot (667,120+50,18,18) clicked [SetVariable("toggle_obj","ears"), Jump("her_ears_toggle")]
                if hermione_wear_ears:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+50 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+50
                text "Ушки" xpos 688 ypos 124+50 size 10
            else:
                pass

            ## Face (Makeup) Toggle ##
            if whoring >= 0:
                hotspot (667,120+75,18,18) clicked [SetVariable("toggle_obj","makeup"), Jump("her_makeup_toggle")]
                if hermione_wear_makeup:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+75 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+75
                text "Макияж" xpos 688 ypos 124+75 size 10
            else:
                pass

            ## Piercings Toggle ##
            if whoring >= 12:
                hotspot (667,120+100,18,18) clicked [SetVariable("toggle_obj","piercings"), Jump("her_piercings_toggle")]
                if hermione_wear_piercings:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+100 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+100
                text "Пирсинг" xpos 688 ypos 124+100 size 10
            else:
                if hermione_wear_piercings:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true_hidden.png" xpos 667 ypos 115+100 #grayed out
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false_hidden.png" xpos 667 ypos 115+100 #grayed out
                text "{color=#858585}Пирсинг{/color}" xpos 688 ypos 124+100 size 10          #grayed out

            ## Tattoos Toggle ##
            if whoring >= 6:
                hotspot (667,120+125,18,18) clicked [SetVariable("toggle_obj","tattoos"), Jump("her_tattoos_toggle")]
                if hermione_wear_tattoos:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+125 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+125
                text "Татуировки" xpos 688 ypos 124+125 size 10
            else:
                if hermione_wear_tattoos:
                    add "interface/wardrobe/"+str(interface_color)+"/check_true_hidden.png" xpos 667 ypos 115+125#grayed out
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false_hidden.png" xpos 667 ypos 115+125 #grayed out
                text "{color=#858585}Татуировки{/color}" xpos 688 ypos 124+125 size 10          #grayed out

        #Change Pose/Action
        if wardrobe_toggle_page == 3:

            ## No Pose ##
            hotspot (667,120,18,18) clicked [SetVariable("wr_her_action","none"), Jump("wardrobe_change_her_action")]
            if hermione_action == "none":
                add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115 #ypos-5 of hotspot ypos #2nd row Ypos+25
            else:
                add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115
            text "Нет позы" xpos 688 ypos 124 size 10

            ## Hold Book ##
            if v_tutoring >= 1:
                hotspot (667,120+25,18,18) clicked [SetVariable("wr_her_action","hold_book"), Jump("wardrobe_change_her_action")]
                if hermione_action == "hold_book":
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+25 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+25
                text "Держать Книгу" xpos 688 ypos 124+25 size 10
            else:
                if hermione_action == "hold_book":
                    add "interface/wardrobe/"+str(interface_color)+"/check_true_hidden.png" xpos 667 ypos 115+25 #grayed out
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false_hidden.png" xpos 667 ypos 115+25 #grayed out
                text "{color=#858585}Держать Книгу{/color}" xpos 688 ypos 124+25 size 10          #grayed out

            ## Lift Top ##
            if whoring >= 9:
                hotspot (667,120+50,18,18) clicked [SetVariable("wr_her_action","lift_top"), Jump("wardrobe_change_her_action")]
                if hermione_action == "lift_top":
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+50 #ypos-5 of hotspot ypos #2nd row Ypos+25
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+50
                text "Поднять Верх" xpos 688 ypos 124+50 size 10
            else:
                if hermione_action == "lift_top":
                    add "interface/wardrobe/"+str(interface_color)+"/check_true_hidden.png" xpos 667 ypos 115+50 #grayed out
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false_hidden.png" xpos 667 ypos 115+50 #grayed out
                text "{color=#858585}Поднять Верх{/color}" xpos 688 ypos 124+50 size 10            #grayed out

            ## Lift Bottom ##
            if whoring >= 6:
                hotspot (667,120+75,18,18) clicked [SetVariable("wr_her_action","lift_skirt"), Jump("wardrobe_change_her_action")]
                if hermione_action == "lift_skirt":
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+75 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+75
                text "Поднять Низ" xpos 688 ypos 124+75 size 10
            else:
                if hermione_action == "lift_skirt":
                    add "interface/wardrobe/"+str(interface_color)+"/check_true_hidden.png" xpos 667 ypos 115+75 #grayed out
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false_hidden.png" xpos 667 ypos 115+75 #grayed out
                text "{color=#858585}Поднять Низ{/color}" xpos 688 ypos 124+75 size 10          #grayed out

            ### FREE SPACE ###
            #if whoring >= 20:
            #    hotspot (667,120+100,18,18) clicked [SetVariable("wr_her_action","milk_breasts"), Jump("wardrobe_change_her_action")]
            #    if hermione_action == "milk_breasts":
            #        add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+100 #ypos-5 of hotspot ypos
            #    else:
            #        add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+100
            #    text "Milk Breasts" xpos 688 ypos 124+100 size 10
            #else:
            #    if hermione_action == "milk_breasts":
            #        add "interface/wardrobe/"+str(interface_color)+"/check_true_hidden.png" xpos 667 ypos 115+100 #grayed out
            #    else:
            #        add "interface/wardrobe/"+str(interface_color)+"/check_false_hidden.png" xpos 667 ypos 115+100 #grayed out
            #    text "{color=#858585}Milk Breasts{/color}" xpos 688 ypos 124+100 size 10          #grayed out

            ## Lift Breasts ##
            if whoring >= 14:
                hotspot (667,120+125,18,18) clicked [SetVariable("wr_her_action","lift_breasts"), Jump("wardrobe_change_her_action")]
                if hermione_action == "lift_breasts":
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+125 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+125
                text "Поднять Грудь" xpos 688 ypos 124+125 size 10
            else:
                if hermione_action == "lift_breasts":
                    add "interface/wardrobe/"+str(interface_color)+"/check_true_hidden.png" xpos 667 ypos 115+125 #grayed out
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false_hidden.png" xpos 667 ypos 115+125 #grayed out
                text "{color=#858585}Поднять Грудь{/color}" xpos 688 ypos 124+125 size 10          #grayed out

            ## Hands Behind ##
            if whoring >= 14:
                hotspot (667,120+150,18,18) clicked [SetVariable("wr_her_action","hands_behind"), Jump("wardrobe_change_her_action")]
                if hermione_action == "hands_behind":
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+150 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+150
                text "За спину" xpos 688 ypos 124+150 size 10
            else:
                if hermione_action == "hands_behind":
                    add "interface/wardrobe/"+str(interface_color)+"/check_true_hidden.png" xpos 667 ypos 115+150 #grayed out
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false_hidden.png" xpos 667 ypos 115+150 #grayed out
                text "{color=#858585}За спину{/color}" xpos 688 ypos 124+150 size 10          #grayed out

            ## Covering ##
            if whoring >= 11:
                hotspot (667,120+175,18,18) clicked [SetVariable("wr_her_action","covering"), Jump("wardrobe_change_her_action")]
                if hermione_action == "covering":
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+175 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+175
                text "Прикрыть" xpos 688 ypos 124+175 size 10
            else:
                if hermione_action == "covering":
                    add "interface/wardrobe/"+str(interface_color)+"/check_true_hidden.png" xpos 667 ypos 115+175 #grayed out
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false_hidden.png" xpos 667 ypos 115+175 #grayed out
                text "{color=#858585}Прикрыть{/color}" xpos 688 ypos 124+175 size 10          #grayed out

            ## Fingering ##
            if whoring >= 17:
                hotspot (667,120+200,18,18) clicked [SetVariable("wr_her_action","fingering"), Jump("wardrobe_change_her_action")]
                if hermione_action == "fingering":
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+200 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+200
                text "Щекотать" xpos 688 ypos 124+200 size 10
            else:
                if hermione_action == "fingering":
                    add "interface/wardrobe/"+str(interface_color)+"/check_true_hidden.png" xpos 667 ypos 115+200 #grayed out
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false_hidden.png" xpos 667 ypos 115+200 #grayed out
                text "{color=#858585}Щекотать{/color}" xpos 688 ypos 124+200 size 10          #grayed out

            ## Pinch ##
            if whoring >= 17:
                hotspot (667,120+225,18,18) clicked [SetVariable("wr_her_action","pinch"), Jump("wardrobe_change_her_action")]
                if hermione_action == "pinch":
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+225 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+225
                text "Ущипнуть" xpos 688 ypos 124+225 size 10
            else:
                if hermione_action == "pinch":
                    add "interface/wardrobe/"+str(interface_color)+"/check_true_hidden.png" xpos 667 ypos 115+225 #grayed out
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false_hidden.png" xpos 667 ypos 115+225 #grayed out
                text "{color=#858585}Ущипнуть{/color}" xpos 688 ypos 124+225 size 10          #grayed out

            ## Hands Cuffed ##
            if whoring >= 20:
                hotspot (667,120+250,18,18) clicked [SetVariable("wr_her_action","hands_cuffed"), Jump("wardrobe_change_her_action")]
                if hermione_action == "hands_cuffed":
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 115+250 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 115+250
                text "Наручники" xpos 688 ypos 124+250 size 10
            else:
                if hermione_action == "hands_cuffed":
                    add "interface/wardrobe/"+str(interface_color)+"/check_true_hidden.png" xpos 667 ypos 115+250 #grayed out
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false_hidden.png" xpos 667 ypos 115+250 #grayed out
                text "{color=#858585}Наручники{/color}" xpos 688 ypos 124+250 size 10          #grayed out

            ## Strip Naked ##
            if whoring >= 11:
                hotspot (667+5,120+275,18,18) clicked [SetVariable("wr_her_action","naked"), Jump("wardrobe_change_her_action")]
                if wr_her_action == "naked":
                    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667+5 ypos 115+275 #ypos-5 of hotspot ypos
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667+5 ypos 115+275
                text "Раздеть" xpos 688+5 ypos 124+275 size 10
            else:
                if wr_her_action == "naked":
                    add "interface/wardrobe/"+str(interface_color)+"/check_true_hidden.png" xpos 667+5 ypos 115+275 #grayed out
                else:
                    add "interface/wardrobe/"+str(interface_color)+"/check_false_hidden.png" xpos 667+5 ypos 115+275 #grayed out
                text "{color=#858585}Раздеть{/color}" xpos 688+5 ypos 124+275 size 10          #grayed out

        #Temporarily disables toggles for Susan/Astoria.
        if wardrobe_toggle_page == 4:
            pass

        ## Wardrobe ChitChat Toggle
        hotspot (667,150+385,18,18) clicked Jump("wardrobe_chitchat_toggle")
        if wardrobe_chitchat_active:
            add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 667 ypos 145+385 #ypos-5 of hotspot ypos
        else:
            add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 667 ypos 145+385
        text "Болтовня" xpos 688 ypos 154+385 size 10


### Wardrobe Hair & Head Accessories ###  

        if wardrobe_page == 1:

            #Hair-Style and Hair-Color
            hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_head_category",0),Show("wardrobe")]
            add "characters/"+str(active_girl)+"/body/head/A_1.png" xpos 10 ypos 102+icon_ypos_offset zoom 0.35/scaleratio
            text "Прически" xpos 76 ypos 140+75 size 10
            #Makeup
            if active_girl in ["hermione"]:
                hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_head_category",1),Show("wardrobe")]
                add "interface/wardrobe/icons/items/lipstick.png" xpos 0+90 ypos 90 zoom 0.3
                text "Макияж" xpos 76+90 ypos 140+75 size 10
            #Glasses
            if active_girl in ["hermione"]:
                hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_head_category",2),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/accessories/vintage_glasses.png" xpos -130+180 ypos -120
                text "Очки" xpos 76+180 ypos 140+75 size 10
            #Ears
            if active_girl in ["hermione"]:
                hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_head_category",3),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/accessories/cat_ears.png" xpos -10+270 ypos 40 zoom 0.5
                text "Ушки" xpos 76+270 ypos 140+75 size 10
            #Hats
            if active_girl in ["hermione"]:
                hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_head_category",4),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/accessories/tiara.png" xpos -130+360 ypos -120
                text "Убор" xpos 76+360 ypos 140+75 size 10

            #Hair Color Palette
            if wardrobe_head_category == 0 and active_girl in ["hermione"]: #Hair Color
                hotspot (347, 95, 20, 20) clicked [SetVariable("wardrobe_hair_color","1"), Jump("wardrobe_update")]
                add "interface/wardrobe/icons/colors/base.png" xpos 348 ypos 96

                for i in range(0,len(wr_haircolor)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((370+(20*col)), (84+(20*row)), 20, 20) clicked [SetVariable("wardrobe_hair_color",wr_haircolor[i]), Jump("wardrobe_update")]
                    add "interface/wardrobe/icons/colors/haircolor/"+wr_haircolor[i]+".png" xpos 371+(20*col) ypos (85+(20*row))

            #Color Palette
            if wardrobe_head_category == 2 and active_girl in ["hermione"]: #Glasses
                hotspot (347, 95, 20, 20) clicked [SetVariable("wardrobe_head_color","base"), Jump("wardrobe_update")]
                add "interface/wardrobe/icons/colors/base.png" xpos 348 ypos 96

                for i in range(0,len(wr_clothcolor)):
                    $ row = i // 7
                    $ col = i % 7

                    hotspot ((370+(20*col)), (84+(20*row)), 20, 20) clicked [SetVariable("wardrobe_head_color",wr_clothcolor[i]), Jump("wardrobe_update")]
                    add "interface/wardrobe/icons/colors/"+wr_clothcolor[i]+".png" xpos 371+(20*col) ypos (85+(20*row))


            #Hair-Style and Hair-Color
            if wardrobe_head_category == 0:
                hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_head_category",0),Show("wardrobe")]
                add "characters/"+str(active_girl)+"/body/head/A_1.png" xpos 10 ypos 102+icon_ypos_offset zoom 0.35/scaleratio
                text "Прически" xpos 76 ypos 140+75 size 10
                for i in range(0,len(wr_hair)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("hair_style_choice",(wr_hair[i])),SetVariable("hair_color_choice",wardrobe_hair_color), Jump("change_hair")]
                    add "characters/"+str(active_girl)+"/body/head/"+wr_hair[i]+"_"+str(wardrobe_hair_color)+".png" xpos 10+(90*col) ypos (102+icon_ypos_offset+92+(92*row)) zoom 0.35/scaleratio

            #Makeup
            if wardrobe_head_category == 1:
                hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_head_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/items/lipstick.png" xpos 0+90 ypos 90 zoom 0.3
                text "Макияж" xpos 76+90 ypos 140+75 size 10
                for i in range(0,len(wr_makeup)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("makeup_choice",(wr_makeup[i])), Jump("equip_makeup")]
                    add "interface/wardrobe/icons/items/"+wr_makeup[i]+".png" xpos 0+(90*col) ypos (90+92+(92*row)) zoom 0.3

            #Glasses
            if wardrobe_head_category == 2:
                hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_head_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/accessories/vintage_glasses.png" xpos -130+180 ypos -120
                text "Очки" xpos 76+180 ypos 140+75 size 10
                for i in range(0,len(wr_glasses)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("glasses_color_choice",wardrobe_head_color),SetVariable("head_accessory_choice",wr_glasses[i]), Jump("equip_head_accessory")]
                    add "characters/"+str(active_girl)+"/accessories/glasses/"+str(wardrobe_head_color)+"/"+wr_glasses[i]+".png" xpos -165+(90*col) ypos (-10+92+(92*row)) zoom 1.0/scaleratio

            #Ears
            if wardrobe_head_category == 3:
                hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_head_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/accessories/cat_ears.png" xpos -10+270 ypos 40 zoom 0.5
                text "Ушки" xpos 76+270 ypos 140+75 size 10
                for i in range(0,len(wr_ears)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("head_accessory_choice",(wr_ears[i])), Jump("equip_head_accessory")]
                    add "characters/"+str(active_girl)+"/accessories/ears/"+wr_ears[i]+".png" xpos -30+(90*col) ypos (100+92+(92*row)) zoom 0.5/scaleratio

            #Hats
            if wardrobe_head_category == 4:
                hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_head_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/accessories/tiara.png" xpos -130+360 ypos -120
                text "Убор" xpos 76+360 ypos 140+75 size 10
                for i in range(0,len(wr_hats)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("head_accessory_choice",(wr_hats[i])), Jump("equip_head_accessory")]
                    add "characters/"+str(active_girl)+"/accessories/hats/"+wr_hats[i]+".png" xpos -180+(90*col) ypos (60+92+(92*row)) zoom 0.5


### Wardrope Tops ###

        if wardrobe_page == 2:

            #Uniform
            hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_tops_category",0),Show("wardrobe")]
            add "interface/wardrobe/icons/"+str(active_girl)+"/tops/tops_uniform.png" xpos 15 ypos 60+icon_ypos_offset zoom 0.35
            text "Форма" xpos 76 ypos 140+75 size 10
            #Muggle
            if active_girl in ["hermione"]:
                hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_tops_category",1),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/tops/tops_muggle.png" xpos 15+90 ypos 60 zoom 0.35
                text "Магловское" xpos 76+90 ypos 140+75 size 10
            #Wicked
            if active_girl in ["hermione"]:
                hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_tops_category",2),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/tops/tops_wicked.png" xpos 15+180 ypos 60 zoom 0.35
                text "Рок-н-ролл" xpos 76+180 ypos 140+75 size 10
            #
            #hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_tops_category",3),Show("wardrobe")]
            #add "interface/wardrobe/icons/"+str(active_girl)+"/tops/tops_onepiece.png" xpos 15+270 ypos 60 zoom 0.35
            #text "" xpos 76+270 ypos 140+75 size 10
            #Misc
            #hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_tops_category",4),Show("wardrobe")]
            #add "interface/wardrobe/icons/"+str(active_girl)+"/tops/tops_misc.png" xpos 15+360 ypos 60 zoom 0.35
            #text "Misc." xpos 76+360 ypos 140+75 size 10

            #Color Palette
            if  wardrobe_tops_category == 0 and active_girl in ["hermione"]: #Uniform, house colors only!
                hotspot (347, 95, 20, 20) clicked [SetVariable("wardrobe_uniform_color","base"), Jump("wardrobe_update")]
                add "interface/wardrobe/icons/colors/base.png" xpos 348 ypos 96

                for i in range(0,len(wr_housecolor)):
                    $ row = i // 7
                    $ col = i % 7

                    hotspot ((370+(20*col)), (84+(20*row)), 20, 20) clicked [SetVariable("wardrobe_uniform_color",wr_housecolor[i]), Jump("wardrobe_update")]
                    add "interface/wardrobe/icons/colors/"+wr_housecolor[i]+".png" xpos 371+(20*col) ypos (85+(20*row))

            if  wardrobe_tops_category == 1 and active_girl in ["hermione"]: #Muggle clothing, all colors
                hotspot (347, 95, 20, 20) clicked [SetVariable("wardrobe_tops_color","base"), Jump("wardrobe_update")]
                add "interface/wardrobe/icons/colors/base.png" xpos 348 ypos 96

                for i in range(0,len(wr_clothcolor)):
                    $ row = i // 7
                    $ col = i % 7

                    hotspot ((370+(20*col)), (84+(20*row)), 20, 20) clicked [SetVariable("wardrobe_tops_color",wr_clothcolor[i]), Jump("wardrobe_update")]
                    add "interface/wardrobe/icons/colors/"+wr_clothcolor[i]+".png" xpos 371+(20*col) ypos (85+(20*row))


            #Uniforms
            if wardrobe_tops_category == 0:
                hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_tops_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/tops/tops_uniform.png" xpos 15 ypos 60+icon_ypos_offset zoom 0.35
                text "Форма" xpos 76 ypos 140+75 size 10
                for i in range(0,len(wr_tops_uniform)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("top_color_choice",wardrobe_uniform_color),SetVariable("top_choice",wr_tops_uniform[i]), Jump("equip_top")]
                    add "characters/"+str(active_girl)+"/clothes/tops/"+str(wardrobe_uniform_color)+"/"+wr_tops_uniform[i]+".png" xpos 15+(90*col) ypos (60+icon_ypos_offset+92+(92*row)) zoom 0.35/scaleratio

            #Muggle
            if wardrobe_tops_category == 1:
                hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_tops_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/tops/tops_muggle.png" xpos 15+90 ypos 60 zoom 0.35
                text "Магловское" xpos 76+90 ypos 140+75 size 10
                for i in range(0,len(wr_tops_normal)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("top_color_choice",wardrobe_tops_color),SetVariable("top_choice",wr_tops_normal[i]), Jump("equip_top")]
                    add "characters/"+str(active_girl)+"/clothes/tops/"+str(wardrobe_tops_color)+"/"+wr_tops_normal[i]+".png" xpos 15+(90*col) ypos (60+92+(92*row)) zoom 0.35/scaleratio

            #Wicked
            if wardrobe_tops_category == 2:
                hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_tops_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/tops/tops_wicked.png" xpos 15+180 ypos 60 zoom 0.35
                text "Рок-н-Ролл" xpos 76+180 ypos 140+75 size 10
                for i in range(0,len(wr_tops_wicked)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("top_color_choice","base"),SetVariable("top_choice",wr_tops_wicked[i]), Jump("equip_top")] #Wicked tops have NO recolor!
                    add "characters/"+str(active_girl)+"/clothes/tops/base/"+wr_tops_wicked[i]+".png" xpos 15+(90*col) ypos (60+92+(92*row)) zoom 0.35/scaleratio

            #NOT IN USE 
            #if wardrobe_tops_category == 3:
            #    hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_tops_category",0),Show("wardrobe")]
            #    add "interface/wardrobe/icons/"+str(active_girl)+"/tops/tops_onepiece.png" xpos 15+270 ypos 60 zoom 0.35
            #    text "" xpos 76+270 ypos 140+75 size 10
            #    for i in range(0,len(wr_tops_onepieces)):
            #        $ row = i // 5
            #        $ col = i % 5

            #        hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("top_color_choice",wardrobe_tops_color),SetVariable("top_choice",wr_tops_onepieces[i]), Jump("equip_top")]
            #        add "characters/"+str(active_girl)+"/clothes/tops/"+str(wardrobe_tops_color)+"/"+wr_tops_onepieces[i]+".png" xpos 15+(90*col) ypos (60+92+(92*row)) zoom 0.35

            #Misc
            #if wardrobe_tops_category == 4:
            #    hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_tops_category",0),Show("wardrobe")]
            #    add "interface/wardrobe/icons/"+str(active_girl)+"/tops/tops_misc.png" xpos 15+360 ypos 60 zoom 0.35
            #    text "Misc." xpos 76+360 ypos 140+75 size 10
            #    for i in range(0,len(wr_tops_misc)):
            #        $ row = i // 5
            #        $ col = i % 5

            #        hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("top_color_choice",wardrobe_tops_color),SetVariable("top_choice",wr_tops_misc[i]), Jump("equip_top")]
            #        add "characters/"+str(active_girl)+"/clothes/tops/"+str(wardrobe_tops_color)+"/"+wr_tops_misc[i]+".png" xpos 15+(90*col) ypos (60+92+(92*row)) zoom 0.35


### Wardrobe Bottoms ###

        if wardrobe_page == 3:

            #Uniform
            hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",0),Show("wardrobe")]
            add "interface/wardrobe/icons/"+str(active_girl)+"/bottoms/bottoms_uniform.png" xpos 15 ypos 17 zoom 0.35
            text "Форма" xpos 76 ypos 140+75 size 10
            #Uniform Low
            if active_girl in ["hermione"]:
                hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",1),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/bottoms/bottoms_uniform_low.png" xpos 15+90 ypos 17 zoom 0.35
                text "Форма мини" xpos 76+90 ypos 140+75 size 10
            #Skirts
            if active_girl in ["hermione"]:
                hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",2),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/bottoms/bottoms_skirts.png" xpos 15+180 ypos 17 zoom 0.35
                text "Юбки" xpos 76+180 ypos 140+75 size 10
            #Pants
            if active_girl in ["hermione"]:
                hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",3),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/bottoms/bottoms_pants.png" xpos 15+270 ypos 17 zoom 0.35
                text "Шорты-Брюки" xpos 76+270 ypos 140+75 size 10
            #Misc
            #hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",4),Show("wardrobe")]
            #add "interface/wardrobe/icons/"+str(active_girl)+"/bottoms/bottoms_misc.png" xpos 15+360 ypos 17 zoom 0.35
            #text "Misc." xpos 76+360 ypos 140+75 size 10

            #Color Palette
            if active_girl in ["hermione"]:
                hotspot (347, 95, 20, 20) clicked [SetVariable("wardrobe_bottoms_color","base"), SetVariable("update_wr_colors",True), Jump("wardrobe_update")]
                add "interface/wardrobe/icons/colors/base.png" xpos 348 ypos 96

                for i in range(0,len(wr_clothcolor)):
                    $ row = i // 7
                    $ col = i % 7

                    hotspot ((370+(20*col)), (84+(20*row)), 20, 20) clicked [SetVariable("wardrobe_bottoms_color",wr_clothcolor[i]), Jump("wardrobe_update")]
                    add "interface/wardrobe/icons/colors/"+wr_clothcolor[i]+".png" xpos 371+(20*col) ypos (85+(20*row))


            #Uniforms
            if wardrobe_bottoms_category == 0:
                hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/bottoms/bottoms_uniform.png" xpos 15 ypos 17 zoom 0.35
                text "Форма" xpos 76 ypos 140+75 size 10
                for i in range(0,len(wr_bottoms_uniform)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("bottom_color_choice",wardrobe_bottoms_color),SetVariable("skirt_choice",wr_bottoms_uniform[i]), Jump("equip_bottom")]
                    add "characters/"+str(active_girl)+"/clothes/bottoms/"+str(wardrobe_bottoms_color)+"/"+wr_bottoms_uniform[i]+".png" xpos 15+(90*col) ypos (17+icon_ypos_offset+92+(92*row)) zoom 0.35/scaleratio

            #Uniform Low
            if wardrobe_bottoms_category == 1:
                hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/bottoms/bottoms_uniform_low.png" xpos 15+90 ypos 17 zoom 0.35
                text "Форма мини" xpos 76+90 ypos 140+75 size 10
                for i in range(0,len(wr_bottoms_uniform_low)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("bottom_color_choice",wardrobe_bottoms_color),SetVariable("skirt_choice",wr_bottoms_uniform_low[i]), Jump("equip_bottom")]
                    add "characters/"+str(active_girl)+"/clothes/bottoms/"+str(wardrobe_bottoms_color)+"/"+wr_bottoms_uniform_low[i]+".png" xpos 15+(90*col) ypos (17+92+(92*row)) zoom 0.35/scaleratio

            #Skirts
            if wardrobe_bottoms_category == 2:
                hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/bottoms/bottoms_skirts.png" xpos 15+180 ypos 17 zoom 0.35
                text "Юбки" xpos 76+180 ypos 140+75 size 10
                for i in range(0,len(wr_bottoms_skirts)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("bottom_color_choice",wardrobe_bottoms_color),SetVariable("skirt_choice",wr_bottoms_skirts[i]), Jump("equip_bottom")]
                    add "characters/"+str(active_girl)+"/clothes/bottoms/"+str(wardrobe_bottoms_color)+"/"+wr_bottoms_skirts[i]+".png" xpos 15+(90*col) ypos (17+92+(92*row)) zoom 0.35/scaleratio

            #Pants
            if wardrobe_bottoms_category == 3:
                hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/bottoms/bottoms_pants.png" xpos 15+270 ypos 17 zoom 0.35
                text "Шорты-Брюки" xpos 76+270 ypos 140+75 size 10
                for i in range(0,len(wr_bottoms_pants)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("bottom_color_choice",wardrobe_bottoms_color),SetVariable("skirt_choice",wr_bottoms_pants[i]), Jump("equip_bottom")]
                    add "characters/"+str(active_girl)+"/clothes/bottoms/"+str(wardrobe_bottoms_color)+"/"+wr_bottoms_pants[i]+".png" xpos 15+(90*col) ypos (17+92+(92*row)) zoom 0.35/scaleratio

            #Misc
            #if wardrobe_bottoms_category == 4:
            #    hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",0),Show("wardrobe")]
            #    add "interface/wardrobe/icons/"+str(active_girl)+"/bottoms/bottoms_misc.png" xpos 15+360 ypos 17 zoom 0.35/scaleratio
            #    text "Misc." xpos 76+360 ypos 140+75 size 10
            #    for i in range(0,len(wr_bottoms_misc)):
            #        $ row = i // 5
            #        $ col = i % 5

            #        hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("bottom_color_choice",wardrobe_bottoms_color),SetVariable("skirt_choice",wr_bottoms_misc[i]), Jump("equip_bottom")]
            #        add "characters/"+str(active_girl)+"/clothes/bottoms/"+str(wardrobe_bottoms_color)+"/"+wr_bottoms_misc[i]+".png" xpos 15+(90*col) ypos (17+92+(92*row)) zoom 0.35/scaleratio


## Wardrobe Other Clothings ##

        if wardrobe_page == 4:

            #Neckwear
            if active_girl in ["hermione","astoria","susan"]:
                hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_stockings_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/other_clothings/neckwear.png" xpos 15 ypos 60 zoom 0.35
                text "Галстук" xpos 76 ypos 140+75 size 10
            #Body Accessories
            if active_girl in ["hermione"]:
                hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_stockings_category",1),Show("wardrobe")]
                add "images/store/29.png" xpos 0+90 ypos 90 zoom 0.3
                text "Акс. Тела" xpos 76+90 ypos 140+75 size 10
            #Gloves
            if active_girl in ["hermione"]:
                hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_stockings_category",2),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/other_clothings/gloves.png" xpos 15+180 ypos 30 zoom 0.35
                text "Перчатки" xpos 76+180 ypos 140+75 size 10
            #Stockings
            if active_girl in ["hermione","astoria","susan"]:
                hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_stockings_category",3),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/other_clothings/stockings.png" xpos -85+270 ypos -195 zoom 0.7
                text "Чулки" xpos 76+270 ypos 140+75 size 10
            #Robes
            if active_girl in ["hermione","astoria"]:
                hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_stockings_category",4),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/other_clothings/robes.png" xpos 45+360 ypos 75 zoom 0.25
                text "Мантия" xpos 76+360 ypos 140+75 size 10

            #Color Palette
            if active_girl in ["hermione"]:
                hotspot (347, 95, 20, 20) clicked [SetVariable("wardrobe_other_clothings_color","base"), Jump("wardrobe_update")]
                add "interface/wardrobe/icons/colors/base.png" xpos 348 ypos 96

                for i in range(0,len(wr_clothcolor)):
                    $ row = i // 7
                    $ col = i % 7

                    hotspot ((370+(20*col)), (84+(20*row)), 20, 20) clicked [SetVariable("wardrobe_other_clothings_color",wr_clothcolor[i]), Jump("wardrobe_update")]
                    add "interface/wardrobe/icons/colors/"+wr_clothcolor[i]+".png" xpos 371+(20*col) ypos (85+(20*row))


            #Neckwear
            if wardrobe_stockings_category == 0:
                hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_stockings_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/other_clothings/neckwear.png" xpos 15 ypos 60 zoom 0.35
                text "Галстук" xpos 76 ypos 140+75 size 10
                for i in range(0,len(wr_neckwears)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("neckwear_color_choice",wardrobe_other_clothings_color),SetVariable("neckwear_choice",wr_neckwears[i]), Jump("equip_neckwear")]
                    add "characters/"+str(active_girl)+"/clothes/neckwear/"+str(wardrobe_other_clothings_color)+"/"+str(wr_neckwears[i])+".png" xpos 15+(90*col) ypos 60+icon_ypos_offset+92+(92*row) zoom 0.35/scaleratio

            #Body Accessories
            if wardrobe_stockings_category == 1:
                hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_stockings_category",0),Show("wardrobe")]
                add "images/store/29.png" xpos 0+90 ypos 90 zoom 0.3
                text "Акс. Тела" xpos 76+90 ypos 140+75 size 10
                for i in range(0,len(wr_body_accs)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("body_accessory_choice",(wr_body_accs[i])), Jump("equip_body_accessory")]
                    add "characters/"+str(active_girl)+"/accessories/body_accs/"+wr_body_accs[i]+".png" xpos 15+(90*col) ypos (60+icon_ypos_offset+92+(92*row)) zoom 0.35/scaleratio

            #Gloves
            if wardrobe_stockings_category == 2:
                hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_stockings_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/other_clothings/gloves.png" xpos 15+180 ypos 30 zoom 0.35
                text "Перчатки" xpos 76+180 ypos 140+75 size 10
                for i in range(0,len(wr_gloves)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("gloves_color_choice",wardrobe_other_clothings_color),SetVariable("gloves_choice",wr_gloves[i]), Jump("equip_gloves")]
                    add "characters/"+str(active_girl)+"/clothes/gloves/"+str(wardrobe_other_clothings_color)+"/"+str(wr_gloves[i])+".png" xpos 15+(90*col) ypos 30+icon_ypos_offset+92+(92*row) zoom 0.35/scaleratio

            #Stockings
            if wardrobe_stockings_category == 3:
                hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_stockings_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/other_clothings/stockings.png" xpos -85+270 ypos -195 zoom 0.7
                text "Чулки" xpos 76+270 ypos 140+75 size 10
                for i in range(0,len(wr_stockings)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("stockings_color_choice",wardrobe_other_clothings_color),SetVariable("stockings_choice",wr_stockings[i]), Jump("equip_stockings")]
                    add "characters/"+str(active_girl)+"/clothes/stockings/"+str(wardrobe_other_clothings_color)+"/"+str(wr_stockings[i])+".png" xpos -25+(90*col) ypos -75+92+(92*row) zoom 0.5/scaleratio

            #Robes
            if wardrobe_stockings_category == 4:
                hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_stockings_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/other_clothings/robes.png" xpos 45+360 ypos 75 zoom 0.25
                text "Мантия" xpos 76+360 ypos 140+75 size 10
                for i in range(0,len(wr_robes)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("robe_choice",wr_robes[i]),Jump("equip_robe")]
                    add "characters/"+str(active_girl)+"/clothes/robe/base/"+str(wr_robes[i])+".png" xpos 45+(90*col) ypos 77+92+(92*row) zoom 0.25/scaleratio


## Wardrobe Miscellaneous Accessories ##

        if wardrobe_page == 5:

            #Potions
            hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe")]
            add "images/store/32.png" xpos 0 ypos 90 zoom 0.3
            text "Зелья" xpos 76 ypos 140+75 size 10
            #Items and Toys
            if active_girl in ["hermione"]:
                hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",1),Show("wardrobe")]
                add "images/store/gifts/15.png" xpos 0+90 ypos 90 zoom 0.3
                text "Игрушки" xpos 76+90 ypos 140+75 size 10
            #
            #hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",2),Show("wardrobe")]
            #add "" xpos 0+180 ypos 90 zoom 0.3/scaleratio
            #text "" xpos 76+180 ypos 140+75 size 10
            #Piercings
            if active_girl in ["hermione"]:
                hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",3),Show("wardrobe")]
                add "interface/wardrobe/icons/items/piercingB.png" xpos 0+270 ypos 90 zoom 0.3
                text "Пирсинг" xpos 76+270 ypos 140+75 size 10
            #Tattoos
            if active_girl in ["hermione"]:
                hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",4),Show("wardrobe")]
                add "interface/wardrobe/icons/items/tattoo.png" xpos 0+360 ypos 90 zoom 0.3
                text "Татуировки" xpos 76+360 ypos 140+75 size 10

            #Color Palette
            if wardrobe_accessories_category == 3 and active_girl in []: #Piercings Color. Not added yet.
                hotspot (347, 95, 20, 20) clicked [SetVariable("wardrobe_accessories_color","base"), Jump("wardrobe_update")]
                add "interface/wardrobe/icons/colors/base.png" xpos 348 ypos 96

                for i in range(0,len(wr_clothcolor)):
                    $ row = i // 7
                    $ col = i % 7

                    hotspot ((370+(20*col)), (84+(20*row)), 20, 20) clicked [SetVariable("wardrobe_accessories_color",wr_clothcolor[i]), Jump("wardrobe_update")]
                    add "interface/wardrobe/icons/colors/"+wr_clothcolor[i]+".png" xpos 371+(20*col) ypos (85+(20*row))


            ## Potions Category ##
            if wardrobe_accessories_category == 0:
                hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe")]
                add "images/store/32.png" xpos 0 ypos 90 zoom 0.3
                text "Зелья" xpos 76 ypos 140+75 size 10
                for i in range(0,len(wr_potions_list)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("potion_choice",(wr_potions_list[i])), Jump("use_potion")]
                    add "interface/wardrobe/icons/potions/"+wr_potions_list[i]+".png" xpos 65+(90*col) ypos (138+92+(92*row)) zoom 0.8

            ## Items and Toys Category ##
            if wardrobe_accessories_category == 1:
                hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe")]
                add "images/store/gifts/15.png" xpos 0+90 ypos 90 zoom 0.3
                text "Игрушки" xpos 76+90 ypos 140+75 size 10
                for i in range(0,len(wr_items_list)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("item_choice",(wr_items_list[i])), Jump("use_item")]
                    add "interface/wardrobe/icons/items/"+wr_items_list[i]+".png" xpos 0+(90*col) ypos (90+92+(92*row)) zoom 0.3

            ## 
            #if wardrobe_accessories_category == 2:
            #    hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe")]

            ##  Piercings ##
            if wardrobe_accessories_category == 3:
                hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/items/piercingB.png" xpos 0+270 ypos 90 zoom 0.3
                text "Пирсинг" xpos 76+270 ypos 140+75 size 10
                for i in range(0,len(wr_piercings_list)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("piercing_color_choice","base"),SetVariable("piercing_choice",(wr_piercings_list[i])), Jump("equip_piercing")] #ADD Piercing Color (replase "base")
                    add "characters/"+str(active_girl)+"/accessories/piercings/base/"+wr_piercings_list[i]+".png" xpos 15+(90*col) ypos (70+92+(92*row)) zoom 0.35/scaleratio                                      #ADD Piercing Color (replase /base/)/scaleratio

            ##  Tattoos ##
            if wardrobe_accessories_category == 4:
                hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/items/tattoo.png" xpos 0+360 ypos 90 zoom 0.3
                text "Татуировки" xpos 76+360 ypos 140+75 size 10
                for i in range(0,len(wr_tattoos_list)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("tattoo_choice",(wr_tattoos_list[i])), Jump("equip_tattoo")]
                    add "characters/"+str(active_girl)+"/body/tattoos/"+wr_tattoos_list[i]+".png" xpos 15+(90*col) ypos (60+92+(92*row)) zoom 0.35/scaleratio



## Wardrobe Underwear ##
 
        if wardrobe_page == 6:

            #Bras
            hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_underwear_category",0),Show("wardrobe")]
            add "interface/wardrobe/icons/"+str(active_girl)+"/underwear/underwear_bra.png" xpos 15 ypos 55+icon_ypos_offset zoom 0.35
            text "Бюстгальтеры" xpos 76 ypos 140+75 size 10
            #Panties
            hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_underwear_category",1),Show("wardrobe")]
            add "interface/wardrobe/icons/"+str(active_girl)+"/underwear/underwear_panties.png" xpos 15+90 ypos 17 zoom 0.35
            text "Трусики" xpos 76+90 ypos 140+75 size 10
            #One-Pieces
            if active_girl in ["astoria","susan"]:
                hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_underwear_category",2),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/tops/tops_onepiece.png" xpos 15+180 ypos 47+icon_ypos_offset zoom 0.35
                text "Комбинация" xpos 76+180 ypos 140+75 size 10
            #Garterbelts
            if active_girl in ["hermione","susan"]:
                hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_underwear_category",3),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/underwear/underwear_garterbelt.png" xpos 15+270 ypos 17 zoom 0.35
                text "Подвязки" xpos 76+270 ypos 140+75 size 10
            #Stockings
            if active_girl in ["hermione","astoria","susan"]:
                hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_underwear_category",4),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/other_clothings/stockings.png" xpos -85+360 ypos -195 zoom 0.7
                text "Чулки" xpos 76+360 ypos 140+75 size 10

            #Color Palette
            if active_girl in ["hermione"]:
                hotspot (347, 95, 20, 20) clicked [SetVariable("wardrobe_underwear_color","base"), Jump("wardrobe_update")]
                add "interface/wardrobe/icons/colors/base.png" xpos 348 ypos 96

                for i in range(0,len(wr_clothcolor)):
                    $ row = i // 7
                    $ col = i % 7

                    hotspot ((370+(20*col)), (84+(20*row)), 20, 20) clicked [SetVariable("wardrobe_underwear_color",wr_clothcolor[i]), Jump("wardrobe_update")]
                    add "interface/wardrobe/icons/colors/"+wr_clothcolor[i]+".png" xpos 371+(20*col) ypos (85+(20*row))


            #Bras
            if wardrobe_underwear_category == 0:
                hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_underwear_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/underwear/underwear_bra.png" xpos 15 ypos 55+icon_ypos_offset zoom 0.35
                text "Бюстгальтеры" xpos 76 ypos 140+75 size 10
                for i in range(0,len(wr_bras)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("underwear_color_choice",wardrobe_underwear_color),SetVariable("underwear_choice",wr_bras[i]), Jump("equip_bra")]
                    add "characters/"+str(active_girl)+"/clothes/underwear/"+str(wardrobe_underwear_color)+"/"+wr_bras[i]+".png" xpos 15+(90*col) ypos (55+icon_ypos_offset+92+(92*row)) zoom 0.35/scaleratio

            #Panties
            if wardrobe_underwear_category == 1:
                hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_underwear_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/underwear/underwear_panties.png" xpos 15+90 ypos 17 zoom 0.35
                text "Трусики" xpos 76+90 ypos 140+75 size 10
                for i in range(0,len(wr_panties)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("underwear_color_choice",wardrobe_underwear_color),SetVariable("underwear_choice",wr_panties[i]), Jump("equip_panties")]
                    add "characters/"+str(active_girl)+"/clothes/underwear/"+str(wardrobe_underwear_color)+"/"+wr_panties[i]+".png" xpos 15+(90*col) ypos (17+icon_ypos_offset+92+(92*row)) zoom 0.35/scaleratio

            #Nighties & Onepieces #Needs art edits for large breasts, poses,...
            if wardrobe_underwear_category == 2 and (active_girl == "astoria" or active_girl == "susan"):
                hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_underwear_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/tops/tops_onepiece.png" xpos 15+180 ypos 47+icon_ypos_offset zoom 0.35
                text "Комбинация" xpos 76+180 ypos 140+75 size 10
                for i in range(0,len(wr_onepieces)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("underwear_color_choice",wardrobe_underwear_color),SetVariable("underwear_choice",(wr_onepieces[i])), Jump("equip_onepiece")]
                    add "characters/"+str(active_girl)+"/clothes/onepieces/"+str(wardrobe_underwear_color)+"/"+wr_onepieces[i]+".png" xpos 15+(90*col) ypos (47+icon_ypos_offset+92+(92*row)) zoom 0.35/scaleratio

            #Garterbelts
            if wardrobe_underwear_category == 3:
                hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_underwear_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/underwear/underwear_garterbelt.png" xpos 15+270 ypos 17 zoom 0.35
                text "Подвязки" xpos 76+270 ypos 140+75 size 10
                for i in range(0,len(wr_garterbelts)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("underwear_color_choice",wardrobe_underwear_color),SetVariable("underwear_choice",(wr_garterbelts[i])), Jump("equip_garterbelt")]
                    add "characters/"+str(active_girl)+"/clothes/underwear/"+str(wardrobe_underwear_color)+"/"+wr_garterbelts[i]+".png" xpos 15+(90*col) ypos (17+icon_ypos_offset+92+(92*row)) zoom 0.35/scaleratio

            #Stockings
            if wardrobe_underwear_category == 4:
                hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_underwear_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/other_clothings/stockings.png" xpos -85+360 ypos -195 zoom 0.7
                text "Чулки" xpos 76+360 ypos 140+75 size 10
                for i in range(0,len(wr_stockings)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("stockings_color_choice",wardrobe_underwear_color),SetVariable("stockings_choice",wr_stockings[i]), Jump("equip_stockings")]
                    add "characters/"+str(active_girl)+"/clothes/stockings/"+str(wardrobe_underwear_color)+"/"+str(wr_stockings[i])+".png" xpos -25+(90*col) ypos -75+92+(92*row) zoom 0.5/scaleratio


## Wardrobe Outfits ## 

        if wardrobe_page == 7:

            #Outfits
            if active_girl in ["hermione","astoria","susan"]:
                hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_outfits_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/outfits/outfits.png" xpos 75 ypos 116 zoom 0.18
                text "Наряды" xpos 76 ypos 140+75 size 10
            #Costumes
            if active_girl in ["hermione"]:
                hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_outfits_category",1),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/outfits/costumes.png" xpos 75+90 ypos 116 zoom 0.18
                text "Костюмы" xpos 76+90 ypos 140+75 size 10
            #One-Pieces
            if active_girl in ["hermione"]:
                hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_outfits_category",2),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/outfits/onepieces.png" xpos 75+180 ypos 116 zoom 0.18
                text "Комбинация" xpos 76+180 ypos 140+75 size 10
            #
            #if active_girl in []:
                #hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_outfits_category",3),Show("wardrobe")]
                #add "interface/wardrobe/icons/"+str(active_girl)+"/outfits/mannequin.png" xpos 75+270 ypos 116 zoom 0.18
                #text "" xpos 76+270 ypos 140+75 size 10
            #Dresses
            if active_girl in ["hermione"]:
                hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_outfits_category",4),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/outfits/dresses.png" xpos 75+360 ypos 116 zoom 0.18
                text "Платья" xpos 76+360 ypos 140+75 size 10


            #Outfits
            if wardrobe_outfits_category == 0:
                hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_outfits_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/outfits/outfits.png" xpos 75 ypos 116 zoom 0.18
                text "Наряды" xpos 76 ypos 140+75 size 10
                $ index = 0
                for i in range(0,len(wr_outfits)):
                    $ row = i // 5
                    $ col = i % 5

                    if index < len(hg_purchased_outfits):

                        hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("wardrobe_costume_selection",hg_purchased_outfits[index]), Jump("wardrobe_wear_costume")]
                        add "images/store/cs_gui/"+wr_outfits[i]+".png" xpos 75+(90*col) ypos 116+92+(92*row) zoom 0.18
                        $ index = index+1

            #Costumes
            if wardrobe_outfits_category == 1:
                hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_outfits_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/outfits/costumes.png" xpos 75+90 ypos 116 zoom 0.18
                text "Костюмы" xpos 76+90 ypos 140+75 size 10
                $ index = 0
                for i in range(0,len(wr_costumes)):
                    $ row = i // 5
                    $ col = i % 5

                    if index < len(hg_purchased_costumes):

                        hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("wardrobe_costume_selection",hg_purchased_costumes[index]), Jump("wardrobe_wear_costume")]
                        add "images/store/cs_gui/"+wr_costumes[i]+".png" xpos 75+(90*col) ypos 116+92+(92*row) zoom 0.18
                        $ index = index+1

            #One-Pieces
            if wardrobe_outfits_category == 2:
                hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_outfits_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/outfits/onepieces.png" xpos 75+180 ypos 116 zoom 0.18
                text "Комбинация" xpos 76+180 ypos 140+75 size 10
                $ index = 0
                for i in range(0,len(wr_outfits_onepieces)):
                    $ row = i // 5
                    $ col = i % 5

                    if index < len(hg_purchased_onepieces):

                        hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("wardrobe_costume_selection",hg_purchased_onepieces[index]), Jump("wardrobe_wear_costume")]
                        add "images/store/cs_gui/"+wr_outfits_onepieces[i]+".png" xpos 75+(90*col) ypos 116+92+(92*row) zoom 0.18
                        $ index = index+1

            #
            #if wardrobe_outfits_category == 3:
            #    hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_outfits_category",0),Show("wardrobe")]
            #    add "interface/wardrobe/icons/"+str(active_girl)+"/outfits/mannequin.png" xpos 75+270 ypos 116 zoom 0.18
            #    text "" xpos 76+270 ypos 140+75 size 10
            #    $ index = 0
            #    for i in range(0,len(wr_swimsuits)):
            #        $ row = i // 5
            #        $ col = i % 5

            #        if index < len(hg_purchased_swimsuits):

            #            hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("wardrobe_costume_selection",hg_purchased_swimsuits[index]), Jump("wardrobe_wear_costume")]
            #            add "images/store/cs_gui/"+wr_swimsuits[i]+".png" xpos 75+(90*col) ypos 116+92+(92*row) zoom 0.18
            #            $ index = index+1

            #Dresses
            if wardrobe_outfits_category == 4:
                hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_outfits_category",0),Show("wardrobe")]
                add "interface/wardrobe/icons/"+str(active_girl)+"/outfits/dresses.png" xpos 75+360 ypos 116 zoom 0.18
                text "Платья" xpos 76+360 ypos 140+75 size 10
                $ index = 0
                for i in range(0,len(wr_dresses)):
                    $ row = i // 5
                    $ col = i % 5

                    if index < len(hg_purchased_dresses):

                        hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("wardrobe_costume_selection",hg_purchased_dresses[index]), Jump("wardrobe_wear_costume")]
                        add "images/store/cs_gui/"+wr_dresses[i]+".png" xpos 75+(90*col) ypos 116+92+(92*row) zoom 0.18
                        $ index = index+1


## Wardrobe Gifts ##

        if wardrobe_page == 8:
            # note that gift_items are indices (starting with 0) but the
            # image files are starting with/off by 1.

            hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_gifts_category",0),Show("wardrobe")]
            add "images/store/gifts/2.png" xpos 0 ypos 90 zoom 0.3      #Gifts
            text "Подарки" xpos 76 ypos 140+75 size 10

            #hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_gifts_category",1),Show("wardrobe")]
            #add "images/store/gifts/7.png" xpos 0+90 ypos 90 zoom 0.3  #Magazines
            #text "Magazines" xpos 76+90 ypos 140+75 size 10

            #hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_gifts_category",2),Show("wardrobe")]
            #add "images/store/gifts/4.png" xpos 0+180 ypos 90 zoom 0.3  #Beverage
            #text "Beverages" xpos 76+180 ypos 140+75 size 10

            #hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_gifts_category",3),Show("wardrobe")]
            #add "images/store/gifts/3.png" xpos 0+270 ypos 90 zoom 0.3 #Sex Toys
            #text "Toys" xpos 76+270 ypos 140+75 size 10

            hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_gifts_category",4),Show("wardrobe")]
            add "images/store/01.png" xpos 0+360 ypos 90 zoom 0.3
            text "Квест Предм." xpos 76+360 ypos 140+75 size 10

            #Sweets
            if wardrobe_gifts_category == 0:
                hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_gifts_category",0),Show("wardrobe")]
                add "images/store/gifts/2.png" xpos 0 ypos 90 zoom 0.3      #Gifts
                text "Подарки" xpos 76 ypos 140+75 size 10

                if active_girl == "hermione":
                    for i in range(0,18): #0,18
                        $ row = i // 5    #6
                        $ col = i % 5     #6
                        if gift_item_inv[i] > 0:
                            hotspot ((75+(90*col)), (140+92+(92*row)), 83, 85) clicked [SetVariable("wardrobe_gift_item",i),Jump("wardrobe_give_gift")]
                        add "images/store/gifts/"+str(i+1)+".png" xpos 0+(90*col) ypos (90+92+(92*row)) zoom 0.30
                        text str(gift_item_inv[i]) xpos 75+(90*col) ypos (210+92+(92*row))
                else: #ADD for Astoria
                    pass

            #Magazines
            #if wardrobe_gifts_category == 1: 
            #    hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_gifts_category",0),Show("wardrobe")]   
            #    add "images/store/gifts/7.png" xpos 0+90 ypos 90 zoom 0.3  #Magazines
            #    text "Magazines" xpos 76+90 ypos 140+75 size 10

            #Beverages
            #if wardrobe_gifts_category == 2:
            #    hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_gifts_category",0),Show("wardrobe")]
            #    add "images/store/gifts/4.png" xpos 0+180 ypos 90 zoom 0.3  #Beverage
            #    text "Beverages" xpos 76+180 ypos 140+75 size 10

            #Toys
            #if wardrobe_gifts_category == 3:
            #    hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_gifts_category",0),Show("wardrobe")]
            #    add "images/store/gifts/3.png" xpos 0+270 ypos 90 zoom 0.3 #Sex Toys
            #    text "Toys" xpos 76+270 ypos 140+75 size 10

            #Quest Items
            if wardrobe_gifts_category == 4:
                hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_gifts_category",0),Show("wardrobe")]
                add "images/store/01.png" xpos 0+360 ypos 90 zoom 0.3
                text "Квест Предм." xpos 76+360 ypos 140+75 size 10


                if active_girl == "hermione":

                    #Collar Event
                    if collar == 0 and whoring >= 24:
                        hotspot (75+270, 140+92, 83, 85) clicked [Jump("start_collar_event")]
                        add "characters/hermione/accessories/collars/collar_0.png" xpos -40+270 ypos 55+92 zoom 0.5/scaleratio
                        text "Событие, ошейник" xpos 76+270 ypos 140+75+92 size 10
                    else:
                        add "characters/hermione/accessories/collars/collar_5.png" xpos -40+270 ypos 55+92 zoom 0.5/scaleratio

                    #Dress/Start End Event
                    if whoring >= 24 and have_no_dress_hap and not gave_the_dress:
                        hotspot (75+360, 140+92, 83, 85) clicked [Jump("giving_the_dress")]
                        add "images/store/cs_gui/ball_dress.png" xpos 70+370 ypos 116+92 zoom 0.18
                        text "Конец" xpos 76+360 ypos 140+65+92 size 10
                        text "Событие" xpos 76+360 ypos 140+75+92 size 10
                    else:
                        add "images/store/cs_gui/ball_dress_b.png" xpos 70+370 ypos 116+92 zoom 0.18

# ADD wardrobe page for stats here!










