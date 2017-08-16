import random
import time

def quest():
    print ('(King Charles)welcome to your quest')
    print ('(King Charles)you must save the dragonstone from the monsters!')
    print ('(King Charles)first what is your name?')
    name =raw_input('ENTER NAME:   ')
    print('(King Charles)now what is your class?')
    classe=raw_input('knight, mage, or thief:   ' )
    print('(King Charles)ok '+  classe +' '+ name  + ', you will need a weapon')
    print('and a mount')
    if classe== 'knight':
        print ('(King Charles)choose your weapon. ')
        weapon = raw_input('Sword, battle axe, mace:   ')
    if classe== 'mage':
        print ('(King Charles)choose your weapon. ')
        weapon = raw_input( 'staff of fire, staff of ice, staff of lightning:   ')
    if classe== 'thief':
        print ('(King Charles)choose your weapon. ')
        weapon = raw_input( 'dagger, distract spell, crossbow:   ')
    print('(King Charles)now what mount do you want?')
    mount= raw_input('Horse, Tiger, dog(companion):   ')
    print ('one ' + mount + ' and ' + weapon +' coming up')
    print (' ')
    print ('(King Charles)You and your ' + mount + ' should head east along the main')
    print('road to the cave of solitude where we believe the stone is located.
    print('Im giving you 100 gold.')
    gold = 100
    hpotion= 0
    mapps= False
    start= raw_input('Head east?(yes)   ')
    raw_input == 'yes'
    print ('you head east...  ')
    print ('.')
    time.sleep(.400)
    print ('.')
    time.sleep(.400)
    print('.')
    time.sleep(2)
    print('You arrive at a bridge crossing the river of coal. A group of')
    print('bandits block the bridge. ')
    bridge= raw_input('They do not see you yet, (a)Sneak around, (b)attack with')
    print('your '+weapon +' and '+mount +', or (c)try to talk it through with them:   ')
    while bridge== ('a'):
        if classe == 'thief':
            print ('(a) sneak under the bridge or (b) wade through the river')
            sneak1 = raw_input()
            if sneak1 == 'a':
                print('You distract the guards and climb under the bridge to the other ')
                ('side, your ' +mount +' follows you.')
                break
            if sneak1 == 'b':
                print ('you wade acrosss the river with out them knowing.')
                break

        if classe == 'knight' or 'mage':
            print ('You attempt to wade through the river, but one of the bandits')
            print('spots you and fires a volly of arrows')
            print ('(a)speed up or (b)dive and swim downstream')
            sneak2= raw_input()
            if sneak2=='a':
                print ('you are impailed by and arrow and bleed out. ')
                print ('you died')
                time.sleep(20)
                exit()
            if sneak2=='b':
                print('you swimm with the current away from the bridge. By')
                print('guiding yourself to shore you arive on the other side, off')
                print('course however. You have lost your ' +mount+'.')
                break

    while bridge == 'b':
        if classe == 'knight':
            print('you approch the party with your ' + weapon +'drawn and attack')
            ('the party, catching them off guard.')
            print('your '+weapon+' anialites the first unsuspecting victim and')
            ('the rest flee.')
            break
        if classe == 'mage':
            print('you cast a spell at the party, they are blown into the river')
            print('and washed away.' )
            break
        if classe == 'thief':
            print('you take down the first guard imediatly but are soon after')
            ('impailed by a sword. ')
            print ('you died')
            time.sleep(20)
            exit()

    while bridge == 'c':
        print('you approch the bandits and are struck down immediatly.')
        print ('you died')
        time.sleep(20)
        exit()

    print ('you continue your journy...')
    print ('.')
    time.sleep(.400)
    print ('.')
    time.sleep(.400)
    print ('.')
    time.sleep(2)
    print ('you come across your first villige, Pickett. You will have to stay the night.')
    pickett= raw_input('(a)trade (b)purchase a room at the inn:   ')
    #trade option broken
    while pickett == ('a'):
        print ('you go to the general store and look at the stock')
        raw_input('would you like to (1)trade, (2)leave')
        if raw_input ==('2'):

            print('Here is the stock:  ')
            raw_input('1)health potion(60g), (2)map(100g)')
            if raw_input==('1'):
                hpotion=+ 1
                print ('you now have'+ hpotion +'(s)')
                raw_input ('buy another?')
                if raw_input== 'yes' or 'y':
                    hpotion=+ 1
                    print ('you now have'+ hpotion +'(s)')
                    break
                elif raw_input== 'no' or 'n':
                    print ('you leave the store.')

            if raw_input==('2'):
                print ('you have a map now, it will provide direction on your journy. ')
                mapps= True
                break
    while pickett== ('b'):
        print ('you purchase a room at the local in and stay the night. ')











quest()
