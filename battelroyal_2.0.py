import random
import time


ar = ['Kilo 141', 'M4A1', 'M13', 'Grau', 'AS Val']

våpen = random.choice(ar)

smg = ['MP5', 'Uzi', 'PP19 BIZON', 'MP7', 'P90', 'Fennec', 'AUG']

våpen2 = random.choice(smg)

nummere = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

numer1 = random.choice(nummere)
numer2 = random.choice(nummere)
numer3 = random.choice(nummere)
numer4 = random.choice(nummere)

a = input('										Wellcome To The 'r'''
 ▄█     █▄     ▄████████    ▄████████  ▄███████▄   ▄██████▄  ███▄▄▄▄      ▄████████ 
███     ███   ███    ███   ███    ███ ██▀     ▄██ ███    ███ ███▀▀▀██▄   ███    ███ 
███     ███   ███    ███   ███    ███       ▄███▀ ███    ███ ███   ███   ███    █▀  
███     ███   ███    ███  ▄███▄▄▄▄██▀  ▀█▀▄███▀▄▄ ███    ███ ███   ███  ▄███▄▄▄     
███     ███ ▀███████████ ▀▀███▀▀▀▀▀     ▄███▀   ▀ ███    ███ ███   ███ ▀▀███▀▀▀     
███     ███   ███    ███ ▀███████████ ▄███▀       ███    ███ ███   ███   ███    █▄  
███ ▄█▄ ███   ███    ███   ███    ███ ███▄     ▄█ ███    ███ ███   ███   ███    ███ 
 ▀███▀███▀    ███    █▀    ███    ███  ▀████████▀  ▀██████▀   ▀█   █▀    ██████████ 
                           ███    ███                                                ''''!Are You Ready To Fight? [yes] [no]')

while a not in ['yes', 'no']:
	a = input('write yes or no')


if a == 'yes':
	b = input('Good, you ar now entering the warzone. Where do you want to drop? [Superstore] [Downtown] ')
	b = b.lower()
	
	while b not in ['superstore', 'downtown']:
	  b = input('Try again')

	print()	
			
else:
	b = 'ø'
	print('Ok, Bye. ')
	
if b == 'superstore':
	c = input('You are in the air and there is comming two other teams towards you. do tou want to drop with them and fight? [yes] [no] ')
	print()
	
	if c == 'yes':
		d = input('They opens a chest and gets a shotgun. Do you still [rush] or [bail]? ')
		print()	
		
		if d == 'rush':
			print('Dumb idea you get one shot in the face and die.')
		else:
			print('They get a AR and hunts you down. ')
	else:
		s = input('That was close, but you are now over at Boneyard, you open a chest and find a bunker card, and the code is {} {} {} {}. Shal you [go] or [leave] '.format(numer1, numer2, numer3, numer4))
		print(r'''  
	                              ______________________________________
                               |                                      |
                    _.---------|.--.                                  |
                 .-'  `       .'/  ``                                 |
              .-'           .' |    /|                                |
           .-'         |   /   `.__//			            		{}{}	{}	{}	          |
        .-'           _.--/        /                                  |
       |        _  .-'   /        /                                   |
       |     ._  \      /     `  /                                    |
       |        ` .    /     `  /                                     |
       |         \ \ '/        /                                      |
       |        - \  /        /|                                      |
       |        '  .'        / |                                      |
       |          '         |.'|                                      |
       |                    |  |                                      |
       |                    |  |______________________________________|
       |                    |.'
       |                    /
       |                   /
       |                  /
       )                 /|
    .A/`-.              / |
   AMMMA. `-._         / /
  AMMMMMMMMA. `-.     / /
 AMMMMMMMMMMMMA. `.    /
AMMMMMMMMMMMMMMMMA.`. /
MMMMMMMMMMMMMMMMMMMA.`.
MMMMMMMMMMMMMMMMMMMMMA.`.
MMMMMMMMMMMMMMMMMMMMMMMA.
MMMMMMMMMMMMMMMMMMMMMMMMMA.
MMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMV'
''')
		if s == 'go':
			t = input('Well you are now at the bunker, time to enter the code.')
			kode = str(numer1)+str(numer2)+str(numer3)+str(numer4)
	
			if t == kode:
				print('Acsepted. Someone comes up behinde you and shots you with a RPG. GG')
	
			else:
				print('WRONG CODE. Someone is rushing you, and they have a RPG. GG')
	
		else:
			print('Ok, bye. A player has left the game.')
	
	
else:
	if b == 'downtown':
		e = input('You just landed on the roof, you got a sniper. Do you want to trie to shot someone? [yes] [no] ')
		print()
	
	
		if e == 'yes':
			f = input('BANG, nice shot, you kiled someone. Do you want to continue looting? [yes] [no] ')
			print()
			
			if f == 'yes':
				g = input('You run down the stairs and loot the rest of the building. when you are done you got an {} and your trusty sniper. What do you do now? [loot] [find a place to hide]? '.format(våpen))
				print()
			
				if g == 'loot':
						h = input('You see that the cirkel is closing in and you start to walk towards the Stadium. You loot a couple buildings on your way. You now have a lot of cash and by your self a gassmask so you dont die in the storm. When you are over at the Stadium you could either go on the roof or just enter. What do you do? [roof] [just enter] ')
						print()
				
						if h == 'just enter':
							i = input('Wach out someone is on the roof! Fast [shot] ')
							print()
						
							if i == 'shot':
								j = input('You just quik scoped him! Good job, but you havent won yet. What to do now? [loot dead person] ')
								print()
								
								if j == 'loot dead person':
								  k = input('There is allready a guy up there with a shotgun. [kill the shotgun man] [dont]')
								  print()
								  
								  if k == 'kill the shotgun man':
  									l = input('Thanks, those guys dont deserve to play. What to do now? [finish looting] [camp the loot] ')
  									print()
  									
  									if l == 'finish looting':
  										m = input('There are now only 10 players left, and the zone is closing in. Are you going to [wait] or [go now]? ')
  										print()
  										
  										if m == 'wait':
  											n = input('Do you hear that? Someone is comming up the zipline. Do you [bail] or [wait and fight] ')
  											print()
  											
  											if n == 'wait and fight':
  												o = input('Wow, you are realy playing this the hard way. Wel you did the right thing. You pull out the ar and spray the kid as he comes up. Now you have a choise play [agressiv] or [defence] ')
  												print()
  												
  												if o == 'agressiv':
  													p = input('Ok then, you se a guy at TVStation and try to snipe him. Headshot, nice what now? [camp zone] [hunt more] ')
  													print()
  													
  													if p == 'camp zone':
  														q = input('There is only tree pepole left, they must hav had a masive fight. Do you get [higground] or [hide] ')
  														print()
  														
  														if q == 'higground':
  															r = input('Wait! They are figthing, maby you coud snpie one of the when they are done? [snipe] [wait] ')
  															print()
  														
  															if r == 'snipe':
  																print(r''' 
  																
   ▄█     █▄     ▄████████    ▄████████  ▄███████▄   ▄██████▄  ███▄▄▄▄      ▄████████ 
  ███     ███   ███    ███   ███    ███ ██▀     ▄██ ███    ███ ███▀▀▀██▄   ███    ███ 
  ███     ███   ███    ███   ███    ███       ▄███▀ ███    ███ ███   ███   ███    █▀  
  ███     ███   ███    ███  ▄███▄▄▄▄██▀  ▀█▀▄███▀▄▄ ███    ███ ███   ███  ▄███▄▄▄     
  ███     ███ ▀███████████ ▀▀███▀▀▀▀▀     ▄███▀   ▀ ███    ███ ███   ███ ▀▀███▀▀▀     
  ███     ███   ███    ███ ▀███████████ ▄███▀       ███    ███ ███   ███   ███    █▄  
  ███ ▄█▄ ███   ███    ███   ███    ███ ███▄     ▄█ ███    ███ ███   ███   ███    ███ 
   ▀███▀███▀    ███    █▀    ███    ███  ▀████████▀  ▀██████▀   ▀█   █▀    ██████████ 
                             ███    ███                                               
   ▄█    █▄   ▄█   ▄████████     ███      ▄██████▄     ▄████████ ▄██   ▄              
  ███    ███ ███  ███    ███ ▀█████████▄ ███    ███   ███    ███ ███   ██▄            
  ███    ███ ███▌ ███    █▀     ▀███▀▀██ ███    ███   ███    ███ ███▄▄▄███            
  ███    ███ ███▌ ███            ███   ▀ ███    ███  ▄███▄▄▄▄██▀ ▀▀▀▀▀▀███            
  ███    ███ ███▌ ███            ███     ███    ███ ▀▀███▀▀▀▀▀   ▄██   ███            
  ███    ███ ███  ███    █▄      ███     ███    ███ ▀███████████ ███   ███            
  ███    ███ ███  ███    ███     ███     ███    ███   ███    ███ ███   ███            
   ▀██████▀  █▀   ████████▀     ▄████▀    ▀██████▀    ███    ███  ▀█████▀             
                                                      ███    ███                      ''')
  								
  							
  									
  								
  									
  					
  								
  									
  															else:
  																print('wach out..... he sniped you inn the head. GG')
  															
  														else:
  															print('The zone is closing in and you panic. One of the enemy sees you and GG. ')
  															
  									else:
  									  print('You stick by the loot for a while, but the all out of a suden you get sprayed down by a {}. GG'.format(våpen2))
                        
							else:
								print('He sees you and throws a granade perfect. BANG! GG')
								
						
						else:
							print('On your way up there is a enemy and he snpies you. GG')
								
			
				
				else:
					print('You are now over at Hospital, and your on the top camping and trying to snipe sombody. Then all out of a suden somebody assasinates you. GG')
						
			
			
			else:
				print('Someone if flying towards you, you take a step back. But ther is no ground there. you fall down 12 storries and GG.')
		
		else:
			print('Well, what now. No, dont, get away from the edge. You jumped. GG')		
					
											
				
		
print()
		
time.sleep(2)
print(r'''Takk til alle som har hjulpet meg med programmet og gitt meg ideer. Dere har hjulpet meg med med å greie dette. Jeg hadde aldri greid å lage dette uten ideer og trubleshoting fra dere.''')
time.sleep(6)
print(r'''•Marthe''')
time.sleep(1.5)
print(r'''•Torjus''')
time.sleep(1.5)
print(r'''•Stian''')
time.sleep(1.5)
print(r'''•Emil''')
time.sleep(1.5)
print(r'''•Eirik''')
time.sleep(1.5)
print(r'''•Nikolai''')
time.sleep(1.5)
print(r'''•Marius''')
time.sleep(1.5)
print(r'''•Benjamin''')

