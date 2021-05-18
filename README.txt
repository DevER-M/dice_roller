This randomised dice roller uses the random module (which is pre-installed)
ways to use :


import random_dice_roller as rdr 

rdr.roll_dice_visual()     # for visual dice and not in numbers 
print(rdr.roll_dice_any_number(minimum_number=1,maximum_number=100))  # for any numbers int 
print(rdr.roll_dice()) # to roll the normal dice(1 to 6) in a number format