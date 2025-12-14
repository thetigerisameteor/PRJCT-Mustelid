screen gallery_cgs:
    tag menu
    add "gui/bg gallery.png"

    hbox:
            xalign 0.5
            yalign 0.5
            spacing 30
            use gallery_navigation
            grid 2 2:
                add gallery.make_button(name="cg_gallery1", unlocked="cgs/small/cg1.png", locked="cgs/small/locked.png")
                add gallery.make_button(name="cg_gallery2", unlocked="cgs/small/cg2.png", locked="cgs/small/locked.png")
                add gallery.make_button(name="cg_gallery3", unlocked="cgs/small/cg3.png", locked="cgs/small/locked.png")
                spacing 15
