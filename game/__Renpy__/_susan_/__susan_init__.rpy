

label susan_init:

    if not hasattr(renpy.store,'susan_base') or reset_persistants or reset_susans_wardrobe:

        #Body
        $ susan_base                = "characters/susan/body/base/base_01.png" 
        $ susan_boobs               = "characters/susan/body/base/boobs_0.png" 
        $ susan_l_arm               = "characters/susan/body/arms/l_arm_back.png" 
        $ susan_r_arm               = "characters/susan/body/arms/r_arm_thigh.png" 
        $ susan_xpos                = 300
        $ susan_ypos                = 0
        $ susan_zorder              = 5
        $ susan_flip                = 1

        #Face
        $ susan_mouth               = "characters/susan/face/mouth/base.png" 
        $ sus_mouth                 = "base"
        $ sus_lipstick              = "nude" 
        
        $ susan_eye                 = "characters/susan/face/eyes/eye_base.png" 
        $ susan_eye_bg              = "characters/susan/face/eyes/eye_base_bg.png" 
        $ susan_pupil               = "characters/susan/face/eyes/pupil_mid.png" 
        $ sus_eye_color             = "green"
        
        $ susan_eyebrow             = "characters/susan/face/brow/base.png" 
        
        $ susan_cheeks              = "characters/susan/face/extras/blank.png" 
        $ susan_tears               = "characters/susan/face/extras/blank.png" 
        $ susan_extra               = "characters/susan/face/extras/blank.png"

        #Hair
        $ susan_hair                = "characters/susan/body/hair/hair_A_1_base.png"
        $ susan_hair_shadow         = "characters/susan/body/hair/hair_A_1_top.png" 
        $ sus_hair_style            = "A"
        $ sus_hair_color            = 1
        
        #Clothes
        
        #Save State
        $ sus_request_wear_top              = True
        $ sus_request_wear_bra              = True
        $ sus_request_wear_bottom           = True
        $ sus_request_wear_panties          = True

        $ sus_request_wear_onepiece         = False
        $ sus_request_wear_garterbelt       = False

        $ sus_request_wear_neckwear         = False
        $ sus_request_wear_gloves           = False
        $ sus_request_wear_stockings        = False
        $ sus_request_wear_robe             = False

        $ sus_request_wear_hat              = False
        $ sus_request_wear_glasses          = False
        $ sus_request_wear_ears             = False
        $ sus_request_wear_makeup           = False
        $ sus_request_wear_accs             = False
    
        $ sus_request_wear_buttplug         = False
        $ sus_request_wear_piercings        = False
        $ sus_request_wear_tattoos          = False
        
        #Toggle
        $ susan_wear_top               = True
        $ susan_wear_bra               = True
        $ susan_wear_bottom            = True
        $ susan_wear_panties           = True

        $ susan_wear_onepiece          = False
        $ susan_wear_garterbelt        = False

        $ susan_wear_neckwear          = False
        $ susan_wear_gloves            = False
        $ susan_wear_stockings         = False
        $ susan_wear_robe              = False

        $ susan_wear_hat               = False
        $ susan_wear_glasses           = False
        $ susan_wear_ears              = False
        $ susan_wear_makeup            = False
        $ susan_wear_accs              = False
        $ susan_badges                 = False
        $ susan_wear_piercings         = False
        $ susan_wear_tattoos           = False

        
        #Top
        $ susan_top                 = "characters/susan/clothes/tops/base/shirt_1.png" 
        $ sus_top                     = "shirt_1"
        $ sus_top_color               = "base" 
        
        #Bottom
        $ susan_skirt               = "characters/susan/clothes/bottoms/base/skirt_1.png" 
        $ sus_skirt                   = "skirt_1"
        $ sus_skirt_color             = "base" 
        
        #Underwear
        $ susan_bra                 = "characters/susan/clothes/underwear/base/lace_bra.png" 
        $ sus_bra                     = "lace_bra"
        $ sus_bra_color               = "base"  
        
        $ susan_panties             = "characters/susan/clothes/underwear/base/lace_panties.png"
        $ sus_panties                 = "lace_panties"
        $ sus_panties_color           = "base" 
        
        $ susan_onepiece            = "characters/susan/clothes/onepieces/base/blank.png"
        $ sus_onepiece                = "blank"
        $ sus_onepiece_color          = "base"

        $ susan_garterbelt          = "characters/susan/clothes/underwear/base/blank.png"
        $ sus_garterbelt              = "blank"
        $ sus_garterbelt_color        = "base" 
        
        
        #Other Clothing
        $ susan_neckwear            = "characters/susan/clothes/neckwear/base/blank.png"
        $ sus_neckwear                = "blank"
        $ sus_neckwear_color          = "base"

        $ susan_accs_list           = [] 
        $ susan_accs                = "characters/susan/accessories/blank.png"
        
        $ susan_gloves              = "characters/susan/clothes/gloves/base/blank.png"
        $ sus_gloves                  = "blank"
        $ sus_gloves_color            = "base"
        
        $ susan_stockings           = "characters/susan/clothes/stockings/base/blank.png" 
        $ sus_stockings               = "blank" 
        $ sus_stockings_color         = "base" 
         
        $ susan_robe                = "characters/susan/clothes/robe/blank.png"
        $ sus_robe                    = "blank"
        $ sus_robe_color              = "base"

        
        #Accessories
        $ susan_makeup_list         = []

        $ susan_hat                 = "characters/susan/accessories/hats/blank.png"
        $ sus_hat                     = "blank"
        $ sus_hat_color               = "base"

        $ susan_glasses             = "characters/susan/accessories/glasses/blank.png"
        $ sus_glasses                 = "blank"
        $ sus_glasses_color           = "base"

        $ susan_ears                = "characters/susan/accessories/ears/blank.png"
        $ sus_ears                    = "blank" 

        
        #Cum layers
        $ susan_face_covered        = False
        $ susan_face_cum            = "characters/susan/face/cum/cum_0.png"
        
        $ susan_body_covered        = False
        $ susan_body_cum            = "characters/susan/face/cum/cum_3.png"
        
        $ susan_aftersperm          = False
        $ susan_clothes_cum         = "characters/susan/face/cum/aftersperm.png"
        
    #if not hasattr(renpy.store,'ADD') or reset_persistants:

    return


label susan_progress_init:

    if not hasattr(renpy.store,'susan_busy') or reset_persistants:
    
        ##Favour stuff
        $ susan_level = 0
        
        $ susan_imperio_influence = False
        $ susan_imperio_counter = 0 #Maybe the higher Astoria's spell level gets, the longer this lasts?
        $ reset_susans_wardrobe = False
        
        ##Flags
        $ susan_busy = False
        $ susan_unlocked = False
        $ susan_wardrobe_unlocked = False
        $ chitchated_with_susan = False
        
        ##Names
        $ susan_name = "Мисс Боунс"
        $ sus_genie_name = "Сэр"
        
    

    return
