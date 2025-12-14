screen gallery_navigation:
    vbox:
        style_prefix "gallery"
        spacing 20
        xoffset -200
        yoffset 50
        textbutton "CGs" action ShowMenu("gallery_cgs")
        textbutton "Credits" action ShowMenu("staff_credits")
        textbutton "Supporters" action ShowMenu("supporters")
        textbutton "Return":
            action Return()
            yoffset 450

style gallery_button_text:
        idle_color "#808080"
        hover_color "#F7EB6A"
        selected_color "#AA1945"
        size 33
