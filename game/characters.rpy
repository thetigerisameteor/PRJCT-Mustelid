default Bry = Character("Bryer", image='bry',
callback=name_callback, cb_name= 'Bry',
namebox_background=Frame("gui/nameboxBryer.png", 0, 0))

#image bry sad = At("Bryer/BrySad.png", sprite_highlight('Bry'))
image bry sad = At("Bryer/BryerFrustratedHoldingBackTears.png", sprite_highlight('Bry'))
image bry serious = At("Bryer/BrySerious.png", sprite_highlight('Bry'))
image bry awkward = At("Bryer/BryerAwkward.png", sprite_highlight('Bry'))
image bry happy = At("Bryer/BryerHappy.png", sprite_highlight('Bry'))


define Mal = Character("Malcolm", image='mal', callback=name_callback, cb_name= 'Mal',
namebox_background=Frame("gui/nameboxMalcolm.png", 0, 0))

image mal neutral = At("Malcolm/MalNeutralGrumpy.png", sprite_highlight('Mal'))
image mal angry = At("Malcolm/MalAngrySnarl.png", sprite_highlight('Mal'))