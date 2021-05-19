import random as rand , os
dice_number = rand.randint(1,6)

def roll_dicev():
    os.system("cls")
    if dice_number == 1:
                    print('''    
                                                _________
                                               |         |
                                               |         |
                                               |    o    |
                                               |         |
                                               |_________| 
                      ''')
                    
    elif dice_number == 2:
        print('''
                                                _________
                                               |         |
                                               |         |
                                               |   o o   |
                                               |         |
                                               |_________| 
                 
          ''')
        
    elif dice_number == 3:
     print('''
                                                _________
                                               |         |
                                               |         |
                                               | o  o  o |
                                               |         |
                                               |_________| 
                
        ''')
     
    elif dice_number == 4:
        print('''
                                                _________
                                               |         |
                                               |  o   o  |
                                               |         |
                                               |  o   o  |
                                               |_________| 
                                                            
          ''')
        
    elif dice_number == 5:
     print('''
                                                _________
                                               |         |
                                               |  o   o  |
                                               |    o    |
                                               |  o   o  |
                                               |_________| 
                           
        ''')
     
    elif dice_number ==6:
         print ('''
                                                _________
                                               |         |
                                               |  o o o  |
                                               |         |
                                               |  o o o  |
                                               |_________| 
                 
          ''')
def roll_dice_MaxMin(minimum_number,maximum_number):
    dice_number = rand.randint(minimum_number,maximum_number)
    return dice_number

def roll_dice():
    dice_number = rand.randint(1,6)
    return dice_number


