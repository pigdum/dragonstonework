import random
import time

def quest():
    print ('(King Charles)welcome to your quest')
    print ('(King Charles)you must save the dragonstone from the monsters!')
    print ('(King Charles)first what is your name?')
    name =raw_input('ENTER NAME:   ')
    print('(King Charles)now what is your class?')
    classe=raw_input('knight, mage, or thief:   ' )
    print('(King Charles)ok '+  classe +' '+ name  + ', you will need a weapon and a mount')
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
    print ('(King Charles)You and your ' + mount + ' should head east along the main road to the cave of solitude where we')
    print ('believe the stone is located. Im giving you 100 gold.')
    gold = 100
    start= raw_input('Head east?(yes)   ')
    raw_input == 'yes'
    print ('you head east...  ')
    print ('.')
    time.sleep(.400)
    print ('.')
    time.sleep(.400)
    print('.')
    time.sleep(2)
    print('You arrive at a bridge crossing the river of coal. A group of bandits block the bridge. ')
    bridge= raw_input('They do not see you yet, (a)Sneak around, (b)attack with your '+weapon +' and '+mount +', or (c)try to talk it through with them:   ')
    if bridge == 'a':
        if classe == 'thief':
            print ('(a) sneak under the bridge or (b) wade through the river')
            sneak1 = raw_input()
            if sneak1 == 'a':
                print('You distract the guards and climb under the bridge to the other side, your ' +mount +' follows you.')
            if sneak1 == 'b':
                print ('you wade acrosss the river with out them knowing.')

        if classe == 'knight' or 'mage':
            return ('You attempt to wade through the river, but one of the bandits spots you and fires a volly of arrows')
            print ('(a)speed up or (b)dive and swim downstream')
            sneak2= raw_input()
            if sneak2=='a':
                print ('you are impailed by and arrow and bleed out. press comand d to exit.')
                exit()
            if sneak2=='b':
                print('you swimm with the current away from the bridge. By guiding yourself to shore you arive on the other side, off course however. You have lost your ' +mount+'.')

    if bridge == 'b':
        if classe == 'knight':
            print('you approch the party with your ' + weapon +'drawn and attack the party, catching them off guard.')
            print('your '+weapon+' anialites the first unsuspecting victim and the rest flee. you now have 15 gold '
        if classe == 'mage':
            print('you cast a '+weapon(9-20)+' spell at the party, they are blown into the river and washed away.' )
        if classe == 'thief':
            print('you take down the first guard imediatly but are soon after impailed by a sword. comand d to exit')

    if bridge == 'c':
        print('you approch the bandits and are struck down immediatly. command d to exit')
        exit()

    print ('you continue your journy...')
    print ('.')
    time.sleep(.400)
    print ('.')
    time.sleep(.400)
    print ('.')
    time.sleep(2)
    print ('you come across your first villige, Pickett. You will have to stay the night.')
    print raw_input('(a)trade (b)purchase a room at the inn or (c)')






quest()
