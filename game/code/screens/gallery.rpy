## Gallery #####################################################################
##
## A basic setup for a gallery screen, using Ren'Py's built-in Gallery
## system. More information here:
## https://www.renpy.org/doc/html/rooms.html#image-gallery
##

init python:

    ## The size of gallery buttons/thumbnails
    gallery_thumb_size = (447, 259)


    ## Set up the gallery
    g = Gallery()
    g.locked_button = "gui/gallery/thumbnail_bg.png"
    g.idle_border = "gui/gallery/border.png"
    g.hover_border = "gui/gallery/border.png"

    

    ###Gallery buttons
    g.button("cg_1")
    g.unlock_image("cg_1")

    g.button("cg_2")
    g.unlock_image("cg_2")

    g.button("cg_3")
    g.unlock_image("cg_3")

## Declarations for the images used in the gallery. May or may not
## be needed if you're using Ren'Py's automatic image names.
image cg_1 = "gallery_test.png"
image cg_2 = "gallery_test.png"
image cg_3 = "gallery_test.png"

## This is just the button name + _thumb
image cg_1_thumb = AlphaMask(Transform("cg_1", xysize=gallery_thumb_size), "gui/gallery/mask.png")
image cg_2_thumb = AlphaMask(Transform("cg_2", xysize=gallery_thumb_size), "gui/gallery/mask.png")
image cg_3_thumb = AlphaMask(Transform("cg_3", xysize=gallery_thumb_size), "gui/gallery/mask.png")


default max_pages = 2 ###how many pages does a category have?
default gal_category = "background" ###which category is shown?
default current_page = 1 ##which page is currenty viewed?

screen gallery():

    tag menu


    use game_menu(_("Gallery"))



    ###for testing
    ##text "[gal_category] + [current_page] + [max_pages]"


    ####If you want to categorize CGs into different tabs (Bakcgrounds, CGs, individual characters etc.)
    ####Here you can set it up
    ####You may delete either this section or the individual page buttons section if you don't want to categorize.
    viewport:
        align (1.0, 0.5) xysize(400, 445) xoffset 15 scrollbars "vertical" mousewheel True draggable True
        style_prefix "names"
        vbox:
            
            textbutton "Backgrounds" action [SetVariable("max_pages", 2), SetVariable("current_page", 1), SetVariable("gal_category", "background"), SelectedIf(gal_category == "background")]  
            ##Set the category to a string (can be whatever, just make it unique) and the max page variable to the maximum amount of screens that'll be included under that category
            textbutton "Some name" action [SetVariable("max_pages", 3), SetVariable("current_page", 1), SetVariable("gal_category", "name"), SelectedIf(gal_category == "name")] ###We set the current page to 1 too
            textbutton "Category 3" action NullAction()
            textbutton "Category 4" action NullAction()
            textbutton "Category 5" action NullAction()
            textbutton "Category 6" action NullAction()
            textbutton "Category 7" action NullAction()



    ##individual page buttons
    hbox:
        style_prefix "page"
        align(0.5, 1.0) offset(0, -85) spacing 15


        ###page arrow
        button:
            xysize(34,31) xalign 0.5
            add "gui/button/page_btn.png":
                fit "contain"
                xysize(34,31)
                rotate -90

            if current_page != 1:
                action SetVariable("current_page", current_page-1)
            else:
                action SetVariable("current_page", max_pages)
            at button_fade
            focus_mask None



       
        ## range(1, 10) gives the numbers from 1 to 9.
        for page in range(1, max_pages+1):
            textbutton "[page]" action SetVariable("current_page", page), SelectedIf(current_page == page) at page_wiggle_heavy


        ###page arrow
        button:
            xysize(34,31) xalign 0.5 
            add "gui/button/page_btn.png":
                fit "contain"
                xysize(34,31)
                rotate 90
            if current_page != max_pages:
                action [SetVariable("current_page", current_page+1)]
            else:
                action [SetVariable("current_page", 1)]
            at button_fade
            focus_mask None


    
    



    
    ## Organize the gallery images into a grid

    fixed:
        style_prefix 'gal'
        grid 2 2:

            use expression ("gal_" + str(gal_category) + "_" + str(current_page))



    ###heart decoration on top
    add "gui/gallery/dec.png"







####Test Gallery pages

##for naming use the name of the category (background in this case) and the page number
screen gal_background_1:

    ###make only 4 buttons
    add g.make_button('cg_1','cg_1_thumb')
    add g.make_button('cg_2','cg_2_thumb')
    add g.make_button('cg_3','cg_3_thumb')
    add g.make_button('cg_3','cg_3_thumb')


screen gal_background_2:

    ###you can make less than 4 buttons, just not more
    add g.make_button('cg_1','cg_1_thumb')



screen gal_name_1:

    
    add g.make_button('cg_1','cg_1_thumb')
    add g.make_button('cg_2','cg_2_thumb')


screen gal_name_2:

    add g.make_button('cg_1','cg_1_thumb')
    add g.make_button('cg_2','cg_2_thumb')
    add g.make_button('cg_3','cg_3_thumb')


screen gal_name_3:

    add g.make_button('cg_1','cg_1_thumb')
    add g.make_button('cg_2','cg_2_thumb')
    add g.make_button('cg_3','cg_3_thumb')
    add g.make_button('cg_3','cg_3_thumb')







######Styles

style names_button_text:
    idle_color u"#fcd3e1" hover_color u"#ffffff"
    selected_idle_color u"#ffffff"
    align(0.5, 0.5) #xoffset -30
    #font "gui/font/MotleyForcesRegular.ttf" 
    size 40
style names_button:
    background Frame("gui/game_menu/ret_btn.png",left=30, top=40, right=30, bottom=40, tile=False) xysize(300,85)

style names_vbox:
    spacing 5
style names_vscrollbar:
    xoffset -50
style gal_fixed:
    yfill True
    xsize config.screen_width-420
    align (0.5, 0.5)
    yoffset 100

style gal_grid:
    align (0.5, 0.5)
    xsize config.screen_width-420
    ysize config.screen_height-200
    spacing 50