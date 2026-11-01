"""
Welcome to Zombie Apocaclips -- A text-based Python story game!
   A game by @Synrimon (github & hackclub)
YOU are a promosing photographer caught up in mankind's greatest
biological blunder: Zombies. Traverse a decaying world full of
stories.


GUIDE:
------- Set Up -------
How can you play this? Here's how!
Should also work on mobile, it's just going to be really squished.
Some places might not support the color coding & cleared screen,
but this shouldn't detract from the main game.


   * Code HS:
       1. Go to https://codehs.com/sandbox/maroonarmadillo5402/zombie-apocaclips
       2. Hit the green "Run" button
  
   * Online Python Interpreter:
       BEWARE -- > ANSI Escape stuff might not work. (colored txt, cleared screen, etc.)
       1. Copy ALL of this code
       2. Search "Online Python Interpreter"
       3. Choose one of the first two (not sponsored) links
       4. Click the left side and paste the code
       5. Press the "run" (or play) button
      
   * VS Code:
       1. Copy ALL of this code
       2. Go to https://vscode.dev/ (VS Code website)
       3. Create a file in .py
       4. Select Python as the language
       5. paste code in
           install the Python API in extensions if needed
------- Play -------
* Scrolling:
   Depending on where you're running this, you might have to
   constantly scroll down to view all the dialogue!


* Inputs:
   Answers you can type are encapsulated in parenthesis
   ex: Waffles or pancakes ( waffles/pancakes )
   Type exactly what u see bc it's case sensitive


* Saving:
   Currently, NOT a feature yet, but I'm planning on making it


   How it WOULD work v
   1. Type save in any input box
   2. String is produced with your progress and choices
   3. Copy, save it somewhere like a google doc or note
   4. Come back, enter load into the first input
   5. Paste string in


* Dev Mischief:
   I may or may not have put small tidbits that are hidden:
   they're not hinted at in the game; they're in the code
   I usually make them for me bc :3 silly
   Feel free to find them if u wanna


------- Have fun -------
"""
# ------ Imports -------
import random
   # Usage:
           # from 1 to 10 -- > (1, 10)
           # use random.randint(num,num) function
import time
   # Usage:
           # defaults to seconds.
           # use time.sleep(seconds) function
import re
   # Usage:
       # Meta Charas
           # [] character set (ex: [a-c])
           # * zero+ occurances
           # + one+ occurances
       # findall() ex: ("word", text)
import sys
   # Usage:
       # sys.stdout.flush()
       # sys.stdout.write()
# ------ Imports -------
# ------ Add-ons ------
   # --- ANSI Colors+ ---
red     = "\033[31m"
green   = "\033[32m"
yellow  = "\033[33m"
blue    = "\033[34m"
purple  = "\033[35m"
cyan    = "\033[36m"
grey    = "\033[90m"
b_red    = "\033[91m"
b_white  = "\033[97m"
b_cyan   = "\033[96m"
b_green  = "\033[92m"
b_yellow = "\033[93m"
b_blue   = "\033[94m"
b_purple = "\033[95m"
colors = [red, green, yellow, blue, purple, cyan, grey, b_red, b_white, b_cyan, b_green, b_yellow, b_blue, b_purple]


italic = "\033[3m"
bold = "\033[1m"
underline = "\x1b[4m"
markups = [italic, bold,]


normal = "\033[0m" # < -- color + bold
alt_normal = "\x1b[0m" # < -- italic + underline


resets = [normal, alt_normal]
# b infront of a color means bright/ neon
   # --- ANSI Colors+ ---
def clear():
   time.sleep(3)
   print("\033[H\033[2J")
   return "cleared"


def ep_titling(title):
   print(f"-------{title}-------")
   time.sleep(2)


def dialogue_spacing(dialogue_here):
   # takes a list/tuple
   i = 0
   for i in range(len(dialogue_here)):
       print(dialogue_here[i])
       time.sleep(4)
       i += 1
# ------ Add-ons ------
# ------ Save -------
def save_game(episode, completion):
   global player_inv
   item = list(player_inv.values())
   save_code = f"""{episode}:{completion}|{item}"""
   return save_code
# ----- Inventory -----
player_inv = {
   "Item Slot 1" : "Empty",
   "Item Slot 2" : "Empty",
   "Item Slot 3" : "Empty",
   "Item Slot 4" : "Empty",
   "Item Slot 5" : "Empty",
   "Item Slot 6" : "Empty",
   "Item Slot 7" : "Empty"}
def inv_full():
   global player_inv
   y = 0
   for x in player_inv.values():
       if value != empty:
           y += 1
   if y == len(player_inv.values()):
       return "full"
   else:
       return "not full"
# ----- Zombie Fight -----
def fight_zombies(zoms):
   global player_inv
   player_health = 10
   zombies_health = zoms * 3
   damage_base = [ ]
   if zoms == 1:
       x = "is"
       y = f"{red}zombie{normal}"
   else:
       x = "are"
       y = f"{red}zombies{normal}"
   for i in player_inv.values():
       if i == "baseball bat":
           damage_base.append((i, 2, "swing"))
       if i == "99+ reinforced stick":
           damage_base.append((i, 99, "swing"))
   while zombies_health > 0:
       zombies_left = zombies_health / 3
       action = int(input(f"""
   There {x} {red}{zombies_left}{normal} {y} left!
  


   Camera Guy (you)                                    Zombie(s)
   HP: {player_health}                                       {zombies_health}/{zoms * 3}




         {bold}Attack{normal}
   1) {damage_base[0][3]}
       """))
   random_bonus = random.randint(0,10)
   if random_bonus == 7 or 10:
       random_bonus = 3
   elif random_bonus == 2 or 3:
       random_bonus = 2
   elif random_bonus == 0:
       random_bonus = -1
   else:
       random_bonus = 0
   print(f"""
   {blue}(You can't save during a fight.){normal}
   """)
   time.sleep(3)
   match action:
       case 1:
           print(f"    {damage} damage dealth")
  
  
# ----- Endings -----
   # --- Death ---
pool_noodle = f"""
   The {red}zombie{normal} rushes you before you even get to use
   the pool noodle and... do {italic}what?{alt_normal}


   The last thing you hear is your camera clicking. Must've fallen
   out of your pocket when you got tackled.


   The last photo of you, a photo of your ridiculous attempt to fight
   a {red}zombie{normal} with a pool noodle.
"""
ripped_sweater = f"""
   Regardless of your efforts to be sneaky, the {red}zombie{normal} spots you
   and tackles you. Your ripped sweated didn't stand a chance.


   The last thing you hear is your camera clicking. Must've fallen
   out of your pocket when you got tackled.


   The last photo of you, a photo of you failing to sneak past a {red}zombie{normal}
   with two sweaters on saves to your camera roll.
   """
ding_dong_ditch = f"""
   Behind you gathers a crowd of {red}zombies{normal}, enclosing you in to your fate.


   The last thing you hear is your camera clicking when a zombie stepped on it,
   taking the last picture of you, a photo of you freezing up admist a crowd of {red}undead{normal}
"""
   # --- Death ---
# ----- Endings -----
# ----- Start -----
try:
   clear()
   print(f"""
   Welcome to {red}{bold}Zombie Apocaclips{normal} -- A text-based Python story game!
       A game by {yellow}@Synrimon{normal} (github & hackclub)
   YOU are a promosing photographer caught up in mankind's greatest
   biological blunder: Zombies. Traverse a decaying world full of
   stories and capture it all on camera.


   More parts of this game will be added on later C:


   {blue}If you have a save code please interrupt this message.{normal}
   """)
   time.sleep(5)
except KeyboardInterrupt:
   save_code = input("What's your save code? ( copy and paste here )")
   load_save(save_code)
# ----- Start -----
# ----- Story Parts -----
def episode_1(event):
   clear()
   ep_titling("The Day Everything went Wrong")
   completion = ["interact 1", "interact 2"]
   #episode_1: complete, complete, item | talk1, talk 2 - item
   global player_inv, colors, resets, markups
   closet = ["baseball bat", "pool noodle", "ripped sweater", "99+ reinforced stick"]
   dialogue1 = (f"""
   It was late, the sun was setting. You were tinkering with your camera as
   everything turned to a dark purple in your room an emergency broadcast
   drowned out all your passing thoughts. It lost you at {red}'disease'{normal}.
   Not soon after you could hear commotion down the street.""",
   f"""
   You get an unsettling chill as you approach your bedroom window, camera
   in hand. Peeking out through your closed blinds you see what everyone was
   screaming about: {red}zombies{normal}. Something you'd never believe unless you saw it
   yourself.""",
   """
   All you could think about was how crazy a photo of this would be. How you
   felt the urge to remember this day forever.
   """,
   """


   So... you took a picture
   """,
   """
      _______       _____      _____        _______        _____     ______
    /         \\    |     |    |     |     /         \\     |     |   /     /
   |    ---    \\   |     |    |_____|    |    ---    \\    |     |  /     /
   |   |   \\ ___\\  |     |     _____     |   |   \\ ___\\   |      V      /
   |   |           |     |    |     |    |   |            |            /
   |   |     ____  |     |    |     |    |   |     ____   |      ^     \\
   |    ____/   /  |     |    |     |    |    ____/   /   |     | \\     \\
   \\           /   |     |    |     |    \\           /    |     |  \\     \\
    -----------     -----     -------     -----------      -----    -------
   """,
   """
   As you slide your camera down from your face, you hear something from your front door.
   It was faint, but still audible from where you were.
   """)
   dialogue2 = (f"""
   Someone was banging on your door. But {red}who?{normal}
   So, you went to investigate.
   """, f"""
   As you approach the kitchen, groaning sounds could be heard. Before entering,
   you decide to quietly check your hallway closet for something to defend yourself
   with. If there's one of those {red}creatures{normal} are out there, it'd be
   a good idea to be prepared.
   """,
   """
   You check the closet quietly and see...
   """, f"""
   a {closet[0]}, {closet[1]}, and a {closet[2]}
   """)
  
   def dev_game1():
       event1_dialogue = (f"""
   You decide to walk out the front door, {yellow}99+ reinforced stick{yellow} in hand. A couple more
   zombies are on your path down stairs, but it doesn't matter. The second they lunge for you, you just
   swing your stick.
           """, """
   Life became so much simplier and you decided to explore the outside world with your new powers and
   take photographs like everything was normal.
           """)
       dialogue_spacing(event1_dialogue)
       search_where = int(input("""
      
           """))
   def find_the_item():
       while True:
           try:
               search_where = int(input("""
       Where do you want to search?


   1) Dining room          5) Bedroom
   2) Kitchen              6) Bedroom closet
   3) Hallway closet       7) Laundry room
   4) Bathroom             8) Balcony


           """))
           except ValueError:
               time.sleep(1)
               if search_where != "save now":
                   print("Type a number!")
           match search_where:
               case 1:
                   dialogue4 =  (f"""
   You search the dining room, checking under the table, the counters,
   the corners of the room.
                   """, f"""
   {red}To no success{normal}
                   """, """
   Guess you'll have to look elsewhere.
                   """)
                   dialogue_spacing(dialogue4)
               case 2:
                   dialogue4 = (f"""
   You search inside the kitchen. Stumbling about the mess the {red}zombie{normal}
   had left behind. There wasn't much to look through; you took most of the big
   furniture out anyways.""",f"""
   {red}Unsurprisingly, you found nothing{normal}
                   """, """
   Guess you'll have to look somehwere else.
                   """)
                   dialogue_spacing(dialogue4)
                   player_inv["Item Slot 1"] = "baseball bat"
               case 3:
                   dialogue4 = (f"""
   You look through the hallway closet once more. The pool noodle and ripped
   sweater are still there along with a few other random things crammed into this
   small space. You shoved things aside and squeeze deeper into the closet.
                   """, f"""
   {red}If the strap {italic}was{alt_normal}{red} here, you would've already have
   found it by now.{normal}
                   """, """
   You'll have to check somewhere else now.
                   """)
                   dialogue_spacing(dialogue4)
               case 4:
                   dialogue4 = (f"""
   You enter the bathroom near the hallway. It was pretty bare; nothing to sift
   through and find. You open a few cabinets and drawers and...
                   """, f"""
   {red}There was nothing there. Nothing.{normal}
                   """, """
   You're better off checking someplace else.
                   """)
                   dialogue_spacing(dialogue4)
               case 5:
                   dialogue4 = (f"""
   You enter your bedroom, the tools you were using to upgrade your hand held
   camera still cluttered your desk and miscellaneous tools crowded corners of your
   room. You sigh and decide to start underneath your bed.
                   """, """
   Later, you moved on to your shelves and piles on the floor until...
                   """, f"""
   {red}you stubbed your toe on the corner of your desk.
                   """, """
   You found nothing and, truly, you weren't gonna find anything you didn't
   interact with recently.
                   """, f"""
   Epic failure.{normal}
                   """, """
   Guess you'll have to check somewhere else.
                   """, """
   Don't stub your toe this time.
                   """)
                   dialogue_spacing(dialogue4)
               case 6:
                   dialogue4 = (f"""
   You enter your bed room closet. Grey sweaters and black pants are the only
   thing hanging in there with the occasional empty hanger. Your other clothes
   were stuffed in an old suitcase or dresser, unfolded. Regardless of how
   futile this search was, you continued.
                   """, f"""
   {red}Only to find out you should've quit while you started{normal}
                   """, """
   Guess you'll have to search elsewhere for the case.
                   """)
                   dialogue_spacing(dialogue4)
               case 7:
                   dialogue4 = [f"""
   You manuever around stacks of dirty, clean, and {italic}ehhhhhh{alt_normal} linens.
   You get to the washer and dryer and find something dangling above it.
                   """, """
   You pull on it.
                   """, """
   The baseball case and a bunch of random items that were stacked on top of it came
   flying off and onto you.
                   """, """
   After coughing all the dust out your lungs and disentangling the strap of the case
   you stand up in triumph.
                   """, """
   Of all places to leave it, this was definitely the last place you expected...
                   """, f"""
   Still, {yellow}you can now take your bat anywhere and everywhere now{normal}
                   """]
                   player_inv["Item Slot 1"] = "baseball bat"
                   dialogue_spacing(dialogue4)
                   break
               case 8:
                   dialogue4 = [f"""
   You enter your balcony. You were on the third floor, so {yellow}luckily{normal} you
   didn't have to worry about some {red}zombie{normal} wandering in through the back.
                   """, """
   You decide to look at the street and see what's going on. It hadn't been long since
   you heard the commotion earlier but it seems as it moved further down the street.
   It was odd seeing the street empty but looking so busy with random object littering
   it. It was relatively quiet and peaceful here.
                   """, """
   You thought about taking yet another picture, but you remembered you were searching
   for the batcase and got to work.
                   """, f"""
   {red}However, it wasn't there.{normal}
                   """, """
   Guess you'll have to go back inside to find it.
                   """]


                   dialogue_spacing(dialogue4)
               case "save now":
                   save_code(1, completion)
               case _:
                   print("Sorry, that's not a place you can explore.")
                   dialogue_spacing(dialogue4)
   dialogue_spacing(dialogue1)
   time.sleep(1.5)
   for i in range(4):
       print(f"{red}    Thud.{normal}")
       time.sleep(1)
   print(" ")
   if completion[0] != "done":
       dialogue_spacing(dialogue2)
       grab_item = input("    What do you grab? ( baseball bat/pool noodle/ripped sweater )")
       match grab_item:
           case "baseball bat":
               dialogue3 = (f"""
   You reach within the closet and grab the {grab_item}. It's thick and sturdy.
   With this in hand, you creep over to the edge of the hallway and peer into the kitchen.
   You see your front door wide open and a mess on your kitchen floor.
               """, """
   Looks like that old, rickety lock never stood a chance.
               """, """
   The again, what were you expecting from the apartment you could afford while finishing
   highschool?
               """, """
   Frustrations aside, you enter the kitchen, tightly gripping the baseball bat.
   Whoever was in here promptly noticed and began to dash into your direction.
               """,
               """
   you raised your bat,
               """, """
   closed your eyes,
               """,
               """
   and breathed:
               """,
               """
       ________                  _______               _____        _____
       |        \\                /       \\             |     \\      /     |
       |    |     |            /     |     \\           |      \\    /      |
       |          /           /      |      \\          |       \\  /       |  
       |         /           /               \\         |        \\/        |
       |         `.         /       ___       \\        |     \\      /     |
       |    |      \\       /      /     \\      \\       |     |\\____/|     |
       |    |       |     /      /       \\      \\      |     |      |     |
       |           /     /      /         \\      \\     |     |      |     |
       ```````````      ```````           ```````      `````        `````
               """, f"""
   You didn't stop to think about what had happened. Instead, you quickly drag the
   {red}zombie{normal} out the door, shut the door, and started to pile furniture
   infront of it.
               ""","""
   Your heart was pounding and  you collapsed after shoving another chair next to
   the pile barricading your door.
               ""","""
   There was so much to worry about, but you felt too tired to think it all through.
               """, f"""
   You take your bat and twist it around in your hands. It was much more useful in
   the {red}apocalypse{normal} than what it had been when everything was tranquill.
   Likely, you'd have to use it again so you decide to stand up and find the strap
   that allowed you to carry it with ease.
               """)
               dialogue_spacing(dialogue3)
               completion[0] = "done"
               if completion[1] != "done":
                   find_the_item()
           case "pool noodle":
               dialogue3 = (f"""
   Your reach within the closet and grab the {grab_item}. It's soft and squishy
   and you begin to doubt your choice already.
               """, f"""
   What was a POOL NOODLE going to do against a crazy {red}zombie{normal}?
               """, f"""
   You decide to stop thinking about it (because, really, {italic}were{alt_normal} you thinking?)
               """, """
   You inch over to the kitchen with uncertainty.
               """, """
   Whatever was in there noticed you and promptly dashed in your direction.
       """, f"""
   You raise your {grab_item} and...
                   """, pool_noodle)
               dialogue_spacing(dialogue3)
           case "ripped sweater":
               dialogue3 = (f"""
   Your reach within the closet and grab the {grab_item}. The fabric was flimsy and
   uncomfortable, but you put it on regardless.
               """, f"""
   You inch over to the kitchen, trying to be subtle and get by the {red}zombie{normal}.      
               """, ripped_sweater)
               dialogue_spacing(dialogue3)
           case "99+ reinforced stick":
               dialogue3 = (f"""
   Your reach within the closet and grab the {grab_item}. With this mighty stick in hand,
   you stepped out boldly into the kitchen, being noticed immediantly and
               """, """
       ________                  _______               _____        _____
       |        \\                /       \\             |     \\      /     |
       |    |     |            /     |     \\           |      \\    /      |
       |          /           /      |      \\          |       \\  /       |  
       |         /           /               \\         |        \\/        |
       |         `.         /       ___       \\        |     \\      /     |
       |    |      \\       /      /     \\      \\       |     |\\____/|     |
       |    |       |     /      /       \\      \\      |     |      |     |
       |           /     /      /         \\      \\     |     |      |     |
       ```````````      ```````           ```````      `````        `````
               """)
               dialogue_spacing(dialogue3)
               if completion[3] != "done":
                   print(f"""
   hiiiiii, you found a {yellow}dev path{normal} :3 I'm still working on it tho bc I work on other
   paths that players will discover first before these paths!


   There will be more dev paths, but, due to their nature, they might skip a couple episodes...
   I'll try to make them continuous too!
  
   (99+ reinforced stick is a reference to a webcomic called '99+ reinforced wooden stick' :P
   maybe I should include more references to random books, mangas, and animes I read and watch...
   or things in general :> )


   BTW: {red}You CAN'T {underline}SAVE{alt_normal} on a devpath and there won't be safegaurds if you
   put an answer that isn't there.{normal}
  
   I might change this {italic}wayyyyyyy{alt_normal} later on, but not rn.
   """)
               dev_game1()
           case "save now":
               save_code(1, completion)
           case _:
               print("Sorry, that's not an answer.")
                   #episode_1(skipv_alue)


def episode_2(skip_value):
   clear()
   global player_inv, colors, resets, markups
   ep_titling("The Hermit Crab Finally Emegerges")
   dialogue1 = (f"""
   It's been days. After that {red}first encounter{normal} you wanted nothing to do
   with the outside world, so you shut yourself in. You heard all sorts of
   commotions outside from your balcony, from your kitchen, from your neighbors.
   """, """
   This started to feel like a bad decision...
   """, f"""
   The power flickered off a couple days before and it was {red}only a matter of time
   before it fully turned off{normal}. Not only that, a {red}strange smell{normal} started coming
   from the apartment next door. It was so bad you started to pad your walls to
   {italic}try{alt_normal} to stop it.
   """, f"""
   You thought you'd be better off inside, but being crammed in your room felt
   {red}horrible{normal}. The only thing you could really do was take pictures, sleep, eat,
   and plan for what you needed to do next or ration.
   """, """
   You were fine on food if you just kept rationing, but water.
   """, f"""
   Water was a whole other deal. You had to be extremely careful with it.
   You started filling buckets, bowls, {bold}anything{normal} with tap water.
   """, """
   You finally decide that it's time to take down the barricade.
   """)
   dialogue2 = ("""
   After removing the barricade, you stop for a to catch your breath before heading
   out. You finally made it out the house!
   """, f"""
   But what was out there was {red}disturbing{normal}.
   """, f"""
   You retreated back into your apartment, holding your nose. The {red}zombie{normal} you had
   gotten rid of was {red}gone{normal}. Worst part was that it looked like the next door neighbors had
   dragged it over into their apartment.
   """, f"""
   That definitely explained the {red}strange smell{normal}. What ever was being done with it or why
   they would ever take that was beyond you and you didn't want to think about it.
   """, """
   Keeping your nose plugged and your bat ready with one hand, you begin to go back out after closing
   your door and down the stairs.
   """, """
   A lot of doors were open or broken. Random items trashed the bottom floor of the apartment and all
   the blinds were closed. Then you heard the familiar groaning you were trying to avoid.
   """, f"""
   Instead of running back to your apartment you decide to bolt out of the complex. Which worked.
   {italic}this time.{normal}.
   """)
   move_items = random.randint(3,7)
   def remove_the_barricade(remove):
       clear()
       print("""
       Get out the house:
   push items away to get out
       """)
       for i in range(remove):
           direction = random.randint(1,2)
           item = random.randint(1,4)
           match item:
               case 1:
                   item = "chair"
               case 2:
                   item = "table"
               case 3:
                   item = "stool"
               case 4:
                   item = "rack"
           if direction == 1:
               direction = ">>>"
           else:
               direction = "<<<"
           move = input(f"""
   ( {direction} )
           """)
           if move != direction:
               i -= 1
               print(f"""
   You struggled, but couldn't move the {item}
   """)
           else:
               print(f"""   
   Moved a {item} out of the way
           """)
           clear()




   def exploration():
       where = input(f"""
           Where do you want to go?


   1) Convienence store      3) Pharmacy
   2) Empty houses           4) park


               ( 1/2/3/4 )
               """)
       match where:
           case 1:
               dialogue3 = ("""
   You decided to walk down to a nearby convienence store to see if they still had anything left.
   As you walked towards it you begin going over the chances of anything still being there and
   what you needed most. Currently, any water was useful, but more food couldn't hurt and a
   first aid hit would be good to have. All this thinking of the convienence store reminded
   you of before the apocalypse. You used to drop by just to get a hot dog or donut then dip.
               """, f"""
   You're nearly there when you spot a couple of {red}zombies{normal} bumbling about on the
   street. This was the first time you had seen so many all together at once. It kinda worried
   you. Sure, you could defeat one, but {itlaic}more?{alt_normal}. That was definitely not
   going to end well.
               """, f"""
   This time you decided to try and distract them. You pick up a decent sized rock and
   chuck it at the furthest car's window. The sound alerts the nearby {red}zombie{normal}
               """, """
   With them out of the way, you sneaked into the store.
               """, """
   There wasn't much in there. The entire place was trashed and the shelves were mostly
   emptied with rotting food on the floor, but you searched regardless. You still found
   something worth noting. You snagged some water that must've fallen out of the package
   and some crushed crackers.
               """)
               dialogue_spacing(dialogue3)
           case 2:
               dialogue3 = (f"""
   You decided to go and explore the neighborhood nearby to see if there was any empty
   houses. The further you walked, the more {red}zombies{normal} you saw. You decided to
   just try a couple random doors to see if they were open.
               """, """
   One did and you fell inside the house by accident. It was dark and you could barely make
   out a figure staggering towards you.
               """, """
   As you squint to figure out whose infront of you a soft, familiar groan comes from inside
   the same house. You freeze up in shock as the figure gets close to you.
               """, ding_dong_ditch)
               dialogue_spacing(dialogue3)
           case 3:
               dialogue3 = (f"""
   You decide to go check the pharmacy. Once you reached it your hope dwindles. There's
   crowds upon crowds of {red}zombies{normal} flooding around or in the pharmacy. This was probably
   a hot spot for people during the first few days of the apoclypse.
               """, """
   You decided if you were going to get anything from that store you had to sneak all the way around
   the building. So you did just that. You snuck to the back and saw the back door had a padlock.
               """)
               dialogue_spacing(dialogue3)
               pin_code = 2167
               padlock = int(input(f"""
               Enter pin code:
                 {bold}___{normal}
                {bold}|{normal} 0 {bold}|{normal}
                {bold}`---`{normal} 
        {bold}___{normal}      {bold}___{normal}      {bold}___{normal}
       {bold}|{normal} 1 {bold}|    |{normal} 2 {bold}|    |{normal} 3 {bold}|{normal}
       {bold}`---`    `---`    `---`
        {bold}___      ___      ___{normal}
       {bold}|{normal} 4 {bold}|    |{normal} 5 {bold}|    |{normal} 6 {bold}|{normal}
       {bold}`---`    `---`    `---`{normal}
        {bold}___      ___      ___{normal}
       {bold}|{normal} 7 {bold}|    |{normal} 8 {bold}|    |{normal} 9 {bold}|
       `---`    `---`    `---`{normal}
               """))
               if padlock == pin_code:
                   dialogue3b = (f"""
   To your surprise the lock actually opens. Guess {yellow}luck{normal} is really on your
   side.
                   """, """
   You pull the door open gently and peer inside. It was dark in the back, so you couldn't
   see much. You open the door more, to let the daylight in and see nothing nearby, so you
   let yourself in. You're still anxious though. There were so many zombies in the front;
   what were the chances no zombies were in this part of the pharmacy too?
                   """, """
   You step slowly into the back, sticking close to the right wall. You eventually reach
   the countertop and you decide to search for anything useful like baindaids, first aid
   kits, anything really. 
                   """, """
   placeholder
                   """)
           case 4:
               dialogue3 = ("""
   You decide to visit the park to get your mind off things. It wasn't too long before you
   arrived there. No one was around, and for good reason. This was the last place a kid
   should be wandering around.
               """, """
   You near a tree and started to see nuts scattered across the sidewalk...
               """, """
   They looked like walnuts, so you decided to pick every. single. one. up and stuff them
   in your case to take home with you.
               """, """
   After this little excursion, you decide to head back to your apartment, it was starting
   to get late and it definitely wasn't going to be safe staying out here anyways. Although,
   it was nice going outside.
               """, """
   As you head back to your apartment you see someone on the street. You squint and see...
               """, f"""
   {red}It was the zombie that had chased you out the apartment complex earlier.{normal} This was
   definitely the last thing you expected to see coming home. It didn't notice you now, but there
   was no way you could get to your apartment without getting it's attention. So you grabbed your
   bat out of it's case and started to slowly approach the zombie...
               """)
               fight


   dialogue_spacing(dialogue1)
   remove_the_barricade(move_items)
   dialogue_spacing(dialogue2)
  
def episode_3(skip_value):
   clear()
   completion = ["story pt 1"]
   ep_title("Field Trip Day")
   dialogue1 = (f"""
   After finally exploring the area around you, you felt curious. You had only visited local
   shops and buildings up until now, but today you felt like going on a {yellow}field trip{normal}. What
   could a little bit of walking do to you anyways? It's not like you haven't dealt with a
   {red}zombie{normal} before.
   """, """
   You prepare yourself by taking the bat with you and proceeding quietly down the stairs.
   After you made it out the complex you hid behind objects to avoid zombies. Being
   outside felt nice, besides the dangers associated with it. You decided to make use of
   your trip out by entering a nearby convienence store. There wasn't much left.
  
   """)
def episode_4(skip_value):
   clear()
   completion = ["story pt 1"]
   ep_titling("Not Alone")
   dialogue1 = (f"""
   While exploring further out you can't shake the feeling someone's watching you. Almost
   as if you're {red}never alone{normal} when you make these trips. You feel so uneasey
   because of this to the point your considering not exploring far anymore. It was
   fun while it lasted, but what if it was a {red}zombie{normal} tailing you?
   """, """
   Had they gained sentience? Did they grow a brain? Either way, it felt horrible.
   """, f"""
   You continued to explore the aquarium today, probably for the last time. It was
   pretty empty, guess it was closed the day the outbreak took place. It was so cool
   though. The display lights were surprisingly still on for some of the displays, making
   the tanks even more intriguing to look at. Some of the water had evaporated and the
   tanks were in critical shape. With no one to upkeep them, they began to cloud with all
   sorts of things like algae or dust. Most of the fish had {red}died{normal}, but some lived on,
   creating new, smaller ecosystems.
   """, """
   You explore further, and further. Then you reach a staff-only area that was poorly sectioned
   off. The lights were still on
   """)
def episode_5(skip_value):
   clear()
   completion = ["story pt 1"]
   ep_titling("It's 10PM do YOU know where your friend is?")
   dialogue1= ("""
   You woke up on the cold cement. It wasn't great, but it was better than nothing out here.
   You sit up, rubbing your eyes and look around for Vell. It was pretty empty thought, so
   you thought he was just out searching for materials. They might've been looking for wires
   or tools to fic the generator he found the other day with you.
   """, """
   It was nice. Not rotting inside your apartment anymore. Not constantly dreading a tomorrow.
   Not being alone anymore.
   """, """
   Vell gave you so many things to look forward to in this apocalypse.
   """)
   dialogue_spacing(dialogue1)
def episode_6(skip_value):
   clear()
   completion = ["story pt 1"]
   ep_titling("Living with the Memories")
   global player_inv, colors, resets, markups
   dialoge1 = ("""
   placeholder
   """, """
   placeholder
   """)
def episode_7(skip_value):
   clear()
   completion = ["story pt 1"]
   ep_titling("Leaving before it's too late")
   global player_inv, colors, resets, markups
  




#Episode play:


episode_1(0)
#episode_2(0)


# ----- Gameplay Order -----
   # Episode list planner:
       # Episode 1 : Entry into the apocalypse
       # Episode 2 : Venturing out
       # Episode 3 : Exploring further
       # Episode 4 : Survivors?
       # Episode 5 : Something's wrong
       # Episode 6 : Survive another day
       # Episode 7 :
# ----- Save -----
def load_save(raw_save):
   global player_inv
   def interpretting_save(save_code):
       #save_code = {episode}:{completion}|{item}
       #save guide:
       # : < -- episode separator
       #  | < -- completion separator (a list)
       split1 = list(save_code.split(":"))
       last_episode = int(split1[0])


       split2 = split1.pop[0]
       split2 = split1.split("|")
       episode_completion = split2.pop[1]
       episode_completion = list(episode_completion)
       current_inventory = split2.pop[0]
       current_inventory = list(current_inventory)
       return last_episode, episode_completion, current_inventory
   interpretting_save(save_code)
   for i in range(player_inv):
       if current_inventory[i] != "Empty":
           player_inv[i] = current_inventory[i]
   match last_episode:
       case 1:
           episode_1(current_completion)
       case 2:
           episode_2(current_completion)
       case 2:
           episode_3(current_completion)
       case 4:
           episode_4(current_completion)
       case 5:
           episode_5(current_completion)
       case 6:
           episode_6(current_completion)
       case 7:
           episode_7(current_completion)
   return "loading save..."

