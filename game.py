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

def day_titling(title):
    print(f"-------{title}-------")

def dialogue_spacing(dialogue_here):
    # takes a list/tuple
    i = 0
    for i in range(len(dialogue_here)):
        print(dialogue_here[i])
        time.sleep(4)
        i += 1

# ------ Add-ons ------

# ----- Inventory -----

player_inv = {
    "Item Slot 1" : "Empty",
    "Item Slot 2" : "Empty",
    "Item Slot 3" : "Empty",
    "Item Slot 4" : "Empty",
    "Item Slot 5" : "Empty",
    "Item Slot 6" : "Empty",
    "Item Slot 7" : "Empty"}

# ----- Inventory -----

# ----- Save -----
def saving_system(raw_save):
    saved = list(raw_save)
    #global (any & all inputs)
    #save_code = f"words:words, words:words"
    #save guide:
        # : < -- episode separator
        # , < -- item separators
        # | < -- event / action seperators
    
    def extraction(save_code):
        # Episode Extraction:
        current_episode = list(save_code.split(":"))

        extraction1 = current_episode.copy()

        current_episode = current_episode[0]
        
        # Event Extraction:
        event_code = extraction1.copy()
        event_code.pop(0) # < -- episode x included
        event_code = event_code.split("|")

        extraction2 = event_code.copy()

        event_code.pop(1) # < -- actions x included

        # Action Extraction:
        action_code = extraction2.copy()
        action_code.pop(0) # < -- events x included

        extraction3 = action_code.copy()

        action_code.pop(1) # < -- items x included

        # Item Extraction
        item_code = extraction3.copy()
        item_code.pop(0) # < -- actions x included
        
        item_code = item_code.split(",")
        action_code = action_code.split(",")
        last_episode = raw_episode[0]
        event_code = event_code.split(",")

        saved_data = [last_episode, event_code, action_code, item_code]
        return saved_data

        """save_code_text = "episode_0: event, event, item | talk1, talk 2, item"
        save_episode = list(save_code_text.split(":"))
        episode = save_episode[0]
        print(episode)"""
    extraction(raw_save)

    current_episode = saved_data[0]
    current_event = saved_data[1]
    current_action = saved_data[2]
    current_inventory = saved_data[3]
    match current_episode:
        case 1:
            #call episode function
            #episode_1(current_event, current_action)
            #for i in range(saved_data)

            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
# ----- Save -----

# ----- Endings -----
    # --- Death ---
pool_noodle = "placeholder"
ripped_sweater = "placeholder"

    # --- Death ---

# ----- Endings -----

# ----- Start -----
try:
    print(f"""
    Welcome to Zombie Apocaclips -- A text-based Python story game!
        A game by @Synrimon (github & hackclub)
    YOU are a promosing photographer caught up in mankind's greatest
    biological blunder: Zombies. Traverse a decaying world full of
    stories. 

    More parts of this game will be added on later C:

    {blue}If you have a save code please interrupt this message.{normal}
    """)

    time.sleep(5)
except KeyboardInterrupt:
    save_code = input("What's your save code? ( copy and paste here )")
    saving_system(save_code)
# ----- Start -----

# ----- Story Parts -----
    # --- The Day Everything went Wrong ---
def episode_1(skip_value):
    completion_values = ("Event", "Event", "Item") # < -- Pair with completion
    completion = ["Event 1", "Event 2", ] # < -- Use a match case to match the values. I'm TIRED of coding if-elses bro.
    #episode_#: event, event, item | talk1, talk 2, item

    #possible code:
    global colors, resets

    clear()
    # ^--- Readying

    # match value:
    # 

    # ^--- Match-case
    day_titling("The Day Everything went Wrong")
    time.sleep(2)

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
    Someone was banging on your door. But {red} who? {normal}
    So, you went to investigate. 
    """, f"""
    As you approach the kitchen, groaning sounds could be heard. Before entering,
    you decide to quietly check your hallway closet for something to defend yourself
    with. If there's one of those {red}creatures {normal} are out there, it'd be
    a good idea to be prepared.
    """,
    """
    You check the closet quietly and see...


    """, closet[0:3])
    def find_the_item():
        found = 0
        while True:
            try:
                search_where = int(input("""
        here do you want to search?

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
                event2_dialogue =  [f"""
    You search the dining room, checking under the table, the counters, 
    the corners of the room.
                """, """
    {red}To no success{normal}
                """, """
    Guess you'll have to look elsewhere.
                """]
            case 2:
                event2_dialogue = [f"""
    You search inside the kitchen. Stumbling about the mess the {red}zombie{normal}
    had left behind. There wasn't much to look through; you took most of the big
    furniture out anyways.""","""
    {red}Unsurprisingly, you found nothing{normal}
                """, """
    Guess you'll have to look somehwere else.
                """]
            case 3:
                event2_dialogue = [f"""
    You look through the hallway closet once more. The pool noodle and ripped
    sweater are still there along with a few other random things crammed into this
    small space. You shoved things aside and squeeze deeper into the closet.
                """, """
    {red}If the strap {italic}was{alt_normal}{red} here, you would've already have
    found it by now.{normal}
                """, """
    You'll have to check somewhere else now.
                """]
            case 4:
                event2_dialogue
            case 5:
                pass
            case 6:
                pass
            case 7:
                event2_dialogue = [f"""
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
                """, """
    Nevertheless, 
                """]
            case 8:
                pass
            case _:
                print("Sorry, that's not a place you can explore.")
        clear()

    # --- activities ---
    dialogue_spacing(dialogue1)
    time.sleep(1.5)
    for i in range(4):
        print(f"{red} Thud.{normal}")
        time.sleep(1)
    print(" ")
    dialogue_spacing(dialogue2)
    grab_item = input("What do you grab? ( baseball bat/pool noodle/ripped sweater )")
    match grab_item:
        case "baseball bat":
            dialogue3 = (f""" 
    Your reach within the closet and grab the {grab_item}. It's thick and sturdy.
    With this in hand, you creep over to the edge of the hallway and peer into the kitchen.
    You see your front door wide open and a mess on your kitchen floor.
            """, """
    Looks like that old, rickety lock never stood a chance. 
            """, """
    The again, what were you expecting from the apartment you could afford while finishing
    highschool?
            """, """
    Frustrations aside, you  raise your bat and step out. 
    Whoever was in here promptly noticed and began to dash into your direction.
            """,
            """
    You raised your bat
            """, """
    Closed your eyes
            """,
            """
    And breathed,
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
            """, """
    You didn't stop to think about what had happened. Instead, you quickly drag the 
    {red}zombie{normal} out the door, shut the door, and started to pile furniture 
    infront of it.
            ""","""
    Your heart was pounding and  you collapsed after shoving another chair next to
    the pile barricading your door.
            ""","""
    There was so much to worry about, but you felt too tired to think it all through.
            """, """
    You take your bat and twist it around in your hands. It was much more useful in
    the {red}apocalypse{normal} than what it had been when everything was tranquill.
    Likely, you'd have to use it again so you decide to stand up and find the strap
    that allowed you to carry it with ease.
            """)
            dialogue_spacing(dialogue3)
        case "pool noodle":
            dialogue3 = (f""" 
    Your reach within the closet and grab the {grab_item}. 
            """)
        case "ripped sweater":
            dialogue3 = (f""" 
    Your reach within the closet and grab the {grab_item}. The fabric was flimsy and
    uncomfortable, but you put it on regardless. 
            """)
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
        case _:
            print("Sorry, that's not an answer.")
            #episode_1(skipv_alue)

def episode_2(skip_value):
    pass
def episode_3(skip_value):
    pass
def episode_4(placeholder):
    pass
def episode_5(placeholder):
    pass
def episode_6(placeholder):
    pass
def episode_7(placeholder):
    pass


episode_1(0)

# ----- Gameplay Order -----
    # Episode list planner:
        # Episode 1 : Entry into the apocalypse
        # Episode 2 : Venturing out
        # Episode 3 : Exploring further
        # Episode 4 : Survivors?
        # Episode 5 : 
        # Episode 6 : 
        # Episode 7 : 

