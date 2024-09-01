import winsound
import os
import sys
import time
import threading


print("Welcome to The Stanley Parable Python Version. ")
user_choice_cutscene = input("Show cutscene? Please enter 'y' for Yes or 'n' for No: ").lower()
if user_choice_cutscene == 'c':
    print("CREDITS:\nCreator of the Stanley Parable: Galactic Cafe Software\nTranslated into Python by Ethan Keenan, 2024\nText provided by the Stanley Parable Fandom\nTested by:\nGabe Mollenhauer\nRobbie Ashcroft\nAndrew and Libby Keenan\nLuke Fisher\nSteven Hussey, \nHannah Reibelt, \nAmelia Welch, and\nAllison Baldwin")

            
      

if user_choice_cutscene == 'y':
    #Show the cutscene
    print("SHOW: CUTSCENE:")
    print("This is the story of a man named Stanley.")
    time.sleep(2.5)
    print("Stanley worked for a company in a big building, where he was Employee No. 427.")
    time.sleep(2.5)
    print("Emloyee No. 427's job was simple, he sat at his desk in Room 427, and he pushed buttons on a keyboard.")
    time.sleep(2.5)
    print("Orders came to him throught a monitor on the desk, telling him what buttons to push, how long to push them, and in what order.")
    time.sleep(2.5)
    print("This is what Employee No. 427 did every day, of every month, of every year. And although others might have considered it soul-rending, \nStanley relished every moment that the orders came in, as though he had been made exactly for the job.")
    time.sleep(2.5)
    print("Stanley was happy.")
    time.sleep(5)
    print("And then one day, something very peculiar happened. Something that would forever change Stanley. Something he would never quite forget.")
    time.sleep(3)
    print("He had been at his desk for nearly an hour, when he realised that not one single order had arrived on the monitor for him to follow.")
    time.sleep(3)
    print("No-one had shown up to give him instructions, call a meeting, or even say hi.")
    time.sleep(3)
    print("Never in all his years at the company had this happened, this complete isolation.")
    time.sleep(2.5)
    print("Something was very clearly wrong.")
    time.sleep(2.5)
    print("Shocked, frozen solid, Stanley found himself unable to move for the longest time.")
    time.sleep(2.5)
    print("But as he came to his wits and regained his senses, he got up from his desk, and stepped out of his office.")
    time.sleep(5)
    print("All of his co-workers were gone. What could it mean?")
    time.sleep(2.5)
    print("Stanley decided to go to the meeting room; perhaps he had simply missed a memo.")
    time.sleep(2.5)
    print("When Stanley came to a set of two open doors, he entered the door on his left.")
    time.sleep(2.5)
elif user_choice_cutscene == 'n':
    
    print("All of his co-workers were gone. What could it mean?")
    time.sleep(2.5)
    print("Stanley decided to go to the meeting room; perhaps he had simply missed a memo.")
    time.sleep(2.5)
    print("When Stanley came to a set of two open doors, he entered the door on his left.")
    time.sleep(2.5)

user_choice_doors = input("Please enter 'L' for Left or 'R' for Right: ").lower()

if user_choice_doors == 'l':
    print("Stanley walked down the hallway to the meeting room, yet there was not a single person here either.")
    print("Feeling a wave of disbelief, Stanley decided to go up to his boss's office, hoping he might find an answer there.")
    time.sleep(1.5)
    print("")
    print("Hi! There's a broom closet just ahead in the corridor, you can jump in and have a poke around to satisfy some sort of idea you might have.")
    print("")
    user_choice_broom_closet = input("Have a look in the broom closet? (y/n)").lower()
    if user_choice_broom_closet == 'y':
        print("Stanley stepped into the broom closet, but there was nothing here.")
        print("So he turned around and got back on track.")
    elif user_choice_broom_closet == 'n':
        print("Stanley continued along the hallway.")
        print("Coming to a staircase, Stanley walked upstairs to his boss's office")
    user_choice_staircase = input("Go up or down? (u/d)").lower()
    if user_choice_staircase == 'u':
        print("Stanley walked up the staircase.")
        time.sleep(3)
    elif user_choice_staircase == 'd':
        print("But Stanley just couldn't do it. He considered the possibility of facing his boss\nadmitting he had left his post during work hours.")
        time.sleep(2)
        print("He might be fired for that. And in such a competitive economy, why had he taken that risk")
        time.sleep(2)
        print("All because he believed everyone had vanished?")
        time.sleep(2)
        print("His boss would think he was crazy.")
        time.sleep(3)
        print("And then something occurred to Stanley.")
        time.sleep(2)
        print("'Maybe... ' he thought to himself.")
        time.sleep(2)
        print("Maybe I am crazy... All of my coworkers blinking mysteriously out of existence in a single moment for no reason at all")
        time.sleep(2)
        print("None of it made any logical sense.")
        time.sleep(2)
        print("And as Stanley pondered this, he began to make other strange observations")
        time.sleep(2)
        print("for example, why was this commandline talking to him?")
        time.sleep(2)
        print("and why was he folling the instructions of a person he wasn't even sure existed?")
        time.sleep(2)
        print("'No,' Stanley said to himself. 'this is all too strange, this can't be real.'")
        time.sleep(2)
        print("And at last, he came to the conclusion that had been on the tip of his tongue.")
        time.sleep(2)
        print("He just hadn’t found the words for it.")
        time.sleep(2)
        print("“I’m dreaming!” he yelled. “This is all a dream!”")
        time.sleep(2)
        print("What a relief Stanley felt to have finally found an answer, an explanation.")
        time.sleep(2)
        print("His coworkers weren’t actually gone, he wasn’t going to lose his job, he wasn’t crazy after all!")
        time.sleep(2)
        print("And he thought to himself: “I suppose I’ll wake up soon")
        time.sleep(2)
        print("“I'll have to go back to my boring real life job pushing buttons, I may as well enjoy this while I’m still lucid.”")
        time.sleep(2)
        print("So he imagined himself flying, and began to gently float above the ground.")
        time.sleep(2)
        print("Then he imagined himself soaring through space on a magical star field, and it too appeared!")
        time.sleep(2)
        print("It was so much fun, and Stanley marveled that he had still not woken up. How was he remaining so lucid?")
        time.sleep(2)
        print("And then perhaps the strangest question of them all entered Stanley’s head")
        time.sleep(2)
        print("One he was amazed he hadn’t asked himself sooner")
        time.sleep(2)
        print("“Why is there text on my screen dictating everything that I’m doing and thinking?”")
        time.sleep(2)
        print("Now the voice was describing itself being considered by Stanley, who found it particularly strange.")
        time.sleep(2)
        print("“I’m dreaming about a voice describing me thinking about how it’s describing my thoughts,“ he thought!")
        time.sleep(2)
        print("And while he thought it all very odd, and wondered if this voice spoke to all people in their dreams")
        time.sleep(2)
        print("the truth was that of course this was not a dream. How could it be?")
        time.sleep(2)
        print("Was Stanley simply deceiving himself? Believing that if he's asleep he doesn't have to take responsibility for himself?")
        time.sleep(2)
        print("Stanley is as awake right now as he's ever been in his life.")
        time.sleep(2)
        print("Now hearing the voice speak these words was quite a shock to Stanley. After all, he knew for certain, beyond a doubt, that this was in fact a dream!")
        time.sleep(2)
        print("Did the voice not see him float and make the magical stars just a moment ago?")
        time.sleep(2)
        print("How else would the voice explain all that?")
        time.sleep(2)
        print("This voice was a part of himself too, surely, surely, if he could just...")
        time.sleep(2)
        print("He would prove it. He would prove that he was in control, that this was a dream")
        time.sleep(2)
        print("So he closed his eyes gently, and he invited himself to wake upHe felt the cool weight of the blanket on his skin, the press of the mattress on his back.")
        time.sleep(2)
        print("the fresh air of a world outside this one. “Let me wake up,” he thought to himself.")
        time.sleep(2)
        print("“I'm through with this dream, I wish it to be over. “Let me go back to my job, let me continue pushing the buttons, please, it's all I want.")
        time.sleep(2)
        print("“I want my apartment, and my wife, and my job. “All I want is my life exactly the way it's always been.")
        time.sleep(2)
        print("“My life is normal, I am normal. Everything will be fine.")
        time.sleep(3)
        print("“I am okay.”")
        time.sleep(2)
        print("Stanley opened his eyes and found the same room.")
        time.sleep(2)
        print("Stanley began screaming. “Please someone wake me up! My name is Stanley! I have a boss! I have an office! I am real!")
        time.sleep(2)
        print("“Please just someone tell me I'm real! I must be real! I must be! “Can anyone hear my voice? Who am I? Who am I?!”")
        time.sleep(1)
        print("And everything went black.")
        time.sleep(2)
        os.system('cls')
        time.sleep(2)
        print("This is the story of a woman named Mariella. Mariella woke up on a day like any other. She arose, got dressed, gathered her belongings, and walked to her place of work.")
        time.sleep(3)
        print("But on this particular day, her walk was interrupted by the body of a man who had stumbled through town talking and screaming to himself and then collapsed dead on the sidewalk.")
        time.sleep(2)
        print("And although she would soon turn to go call for an ambulance, for just a few, brief moments, she considered the strange man.")
        time.sleep(2)
        print("He was obviously crazy; this much she knew. Everyone knows what crazy people look like.")
        time.sleep(2)
        print("And in that moment, she thought to herself how lucky she was to be normal.")
        time.sleep(2)
        print("I am sane. I am in control of my mind. I know what is real, and what isn't.")
        time.sleep(2)
        print("It was comfornting to think this, and in a certain way, seeing this man made her feel better. But then she remembered the meeting she had scheduled for that day")
        time.sleep(2)
        print("the very important people whose impressions of her would affect her career, and, by extension, the rest of her life.")
        time.sleep(2)
        print("She had no time for this, so it was only a moment that she stood there, staring down at the body.")
        time.sleep(2)
        print("And then she turned and ran.")
        time.sleep(5)
        sys.exit()
            
            
elif user_choice_doors == "r":
    print("This was not the way to the meeting room, and Stanley knew this perfectly well.")
    print("Perhaps he wanted to stop by the employee lounge first, just to admire it.")
    print("Stanley opened the door to the lounge")
    time.sleep(1.5)
    print("Ah, yes. Truly a room worth admiring. It really had been worth the detour after all, just to spend a few moments\nin this immaculate, beautifully constructed room.")
    time.sleep(3.5)
    print("But, eager to get back to business, Stanley took the first door on his left.")
    time.sleep(1.5)
    print("Hi! There's a broom closet just ahead in the corridor, you can jump in and have a poke around to satisfy some sort of idea you might have. Thanks!")
    user_choice_broom_closet = input("Have a look in the broom closet? (y/n)").lower()
    if user_choice_broom_closet == 'y':
        print("Stanley stepped into the broom closet, but there was nothing here.")
        print("So he turned around and got back on track.")
    elif user_choice_broom_closet == 'n':
        print("Stanley walked past the broom closet and continued on his journey.")

    user_choice_back_on_track = input("Take the door? (y/n)").lower()
    if user_choice_back_on_track == 'y':
        print("And so he detoured through the maintenance section, walked throught the opposite door, and got back on track")
        user_choice_confusion_ending_impending = input("Hi again! There's a maintenance elevator to your left. Get on? (you know the drill by now- y/n)").lower()
        if user_choice_confusion_ending_impending == 'y':
            print("But Stanley didn't wat to go back to the office.")
            time.sleep(1)
            print("He wanted to wander about and get even further off track.")
            time.sleep(1)
            print("So now, in order to get back he needed to go... um... hm... uh... from here it's... left.")
            time.sleep(2)
            print("No, no, no. Not the right. Why would I have ever said it was to the right? What was I thinking?")
            time.sleep(2)
            print("It's clearly- oh dear, would you hold on for a minute, please?")
            time.sleep(7)
            print("now, let's see. We went, um, right... left... down... left... right...")
            time.sleep(3)
            print("Ah, yep! Okay, okay, yes! I've got it now! The story is absolutely, definitely, this way.")
            time.sleep(2.5)
            print("Stanley walks out onto a- oh, damn it.")
            time.sleep(3)
            print("Hi again! Quick bit of context: Stanley has just walked out onto a catwalk, in a room filled with screens. This room\nwill definitely be seen again in the story")
            time.sleep(4)
            print("NO! No... no, no, no, no, no, no, no! This isn't right at all! You're not supposed to be here, yet! This is all a spoiler!\nQuick, Stanley, close your eyes!")
            time.sleep(3)
            print("Okay, okay, okay okay, we just... we just have to get back to, um... oh... Who am I kidding? It's all rubbish now. \nThe whole story, completely unusable.")
            time.sleep(3)
            print("How about rather than waste my time trying to salvage this nonsense, we'll just restart the game from the beginning. \nAnd this time, suppose we don't wander so far off-track, hm?")
            time.sleep(3)
            print("Okay, from the top!")
            os.system('cls')
            time.sleep(1)
            print("Welcome to The Stanley Parable Python Version. ")
            time.sleep(3)
            print("Stanley has arrived at the two doors room, but instead of two, there are now six.")
            time.sleep(2.5)
            print("When Stanley- wait... wait, what?")
            time.sleep(2.5)
            print("No, I... no, I restarted! I swear I definitely restarted the game over, completely fresh.")
            time.sleep(2.5)
            print("Everything should be...")
            time.sleep(1.5)
            print("Or did something change? Stanley, did you change anything when we were back in that room with all the monitors? Did you move the story somewhere, or...")
            time.sleep(1)
            print("Hold on... why am I asking you? I'm the one who wrote the story! It was right here just a minute ago.")
            time.sleep(1.5)
            print("I know for sure that it's here somewhere.")
            time.sleep(3)
            print("")
            print("")
            print("Okay then, it's an adventure!")
            time.sleep(1)
            print("Come Stanley, let's find the story!")
            time.sleep(3)
            print("Stanley wanders the hallways")
            time.sleep(5)
            print("Still wandering")
            time.sleep(5)
            print("Still wandering...")
            time.sleep(5)
            print("I'll say it - this is the worst adventure I've ever been on.")
            time.sleep(5)
            print("I can promise you, there definitely was a story here before. Do we just... do we need to restart the game again? Well, I find it unlikely that we'll ever progress by starting over and over again.")
            time.sleep(3)
            print("But it's got to be better than this. Okay, let's give it a shot. Why not?")
            time.sleep(3)
            os.system('cls')
            time.sleep(1)
            print("Welcome to The Stanley Parable Python Version.")
            time.sleep(2)
            print("Stanley arrived in the two doors room, but there are no doors in sight.")
            time.sleep(2)
            print("Okay, yep, it's worse. I might be remembering this wrong. It's possible the story is back where we just came from.")
            time.sleep(2)
            print("Why don't we go back the other direction and see if we missed anything?")
            time.sleep(2)
            print("Stanley wanders the hallways for a while")
            time.sleep(5)
            print("Stanley appears to find something")
            time.sleep(2)
            print("Aha! I knew we'd missed something! The story! Here it comes!")
            time.sleep(3)
            print("No, wait, nevermind, not the story! Okay, let's head back the other way and retrace our steps")
            time.sleep(2)
            print("Stanley arrives in cluttered wooden hallways")
            time.sleep(2)
            print("Now this... well, I'll be honest, I don't recognize this place at all. Is this the story?")
            time.sleep(2)
            print("I don't think so. I can't quite recall, but I believe my story took place in an office building... is that correct? Hm... do you remember, Stanley?")
            time.sleep(2)
            print("Well, do you know what, since I've completely forgotten what we were supposed to be doing, how about this...")
            time.sleep(2)
            print(" __   _____  _   _  __        _____ _   _ _ ")
            print(" \ \ / / _ \| | | | \ \      / /_ _| \ | | |")
            print("  \ V / | | | | | |  \ \ /\ / / | ||  \| | |")
            print("   | || |_| | |_| |   \ V  V /  | || |\  |_|")
            print("   |_| \___/ \___/     \_/\_/  |___|_| \_(_)")
            time.sleep(3)
            print("Congratulations!")
            time.sleep(3)
            print("I know you put in a lot of hard work, and it really paid off, so good job!")        
            time.sleep(3)
            print("Oh no. No. I don't feel right about this at all.\nWe both know you didn't put in any actual work for that win.")
            time.sleep(4)
            print("Some people win fair and square and this was not one of those situations.")
            time.sleep(3)
            print("Okay, I'm getting weirded out by this.")
            time.sleep(3)
            print("I don't care what might happen this time; I have to restart.")
            time.slee(4)
            os('cls')
            time.sleep(2)
            print("Welcome to The Stanley Parable Python Version. ")
            time.sleep(3)
            print("Alright, I've got a solution.")
            time.sleep(3)
            print("This time, to make sure we don't get lost,\nI've employed the help of The Stanley Parable Adventure Line™!")
            time.sleep(4)
            print("Just follow the Line™. How simple is that?")
            time.sleep(3)
            print("Stanley enters the Two Doors Room, not following the Line™")
            time.sleep(3)
            print("No, no, I'm done, we're leaving it up to the Line™ from now on.")
            time.sleep(3)
            print("You see? The Line™ knows where the story is, it's over in this direction!")
            time.sleep(3)
            print("Onward Stanley! To destiny!")
            
            





    #DONT get back on track- go to cargo lift
if user_choice_back_on_track == 'n':
 print("Stanley was so bad at following directions, it's incredible he wasn't fired years ago.")
 time.sleep(3)
 print("Stanley entered the cargo shed, and stepped onto the cargo lift.")
 time.sleep(3)
 print("Look, Stanley, I think perhaps we've gotten off on the wrong foot.")
 time.sleep(3)
 print("I'm not your enemy, really, I'm not.")
 time.sleep(3)
 print("I realize that investing your trust in someone else can be difficult")
 time.sleep(3)
 print("but the fact is that the story has been about nothing but you all this time.")
 time.sleep(3)
 print("There is an option to jump onto a catwalk, or jump entirely off the lift.")
 time.sleep(3)       
 user_choice_catwalk_cargo_hall = input("Catwalk, jump off or stay on? (C/J/S)").lower()
 if user_choice_catwalk_cargo_hall == "c":
      print("Stanley jumped onto the catwalk")
      time.sleep(3)
if user_choice_catwalk_cargo_hall == "s":
    print("Stanley stayed on the cargo lift")
    time.sleep(5)
    print("There's someone you've been neglecting, Stanley. Someone you've forgotten about. Please, stop trying to make every decision by yourself.")
    time.sleep(3)
    print("Now, I'm not asking for me; I'm asking for her")
    time.sleep(3)
    print("Stanley arrived in the upper cargo room")
    time.sleep(3)
    print("This is it, Stanley, your chance to redeem yourself. To put your work aside, to let her back into your life")
    time.sleep(3)
    print("She's been waiting.")
    time.sleep(3)
    print("Stanley enters a room with a telephone on a table.")
    time.sleep(3)
    print("That's her, Stanley. You need to be the one to do this, to reach out to her. If you can truly place your faith in another, then pick up the phone.")
    time.sleep(3)
    user_choice_phone_room = input("Pick up the phone?").lower()
    if user_choice_phone_room =="y":
        time.sleep(2)
        print("Oh, Stanley, is that you? \nHold on sweetie, sorry to keep you waiting. \nI'm just pulling the bread out of the oven.")
        time.sleep(3)
        print("Alright... okay, there we go!\nAlright now!")
        time.sleep(3)
        print("Stanley enters the apartment.")
        time.sleep(3)
        print("Hahahahahaha, Got-cha! Oh, come on. Did you actually think you had a loving wife?\nWho'd want to commit their life to you? I'm trying to make a point here, Stanley,\nI'm trying to get you to see something.\nCome inside. Let me show you what's really going on here")
        time.sleep(4)
        print("Stanley tries to walk out of the apartment, but a wall rises to block his way.")
        time.sleep(4)
        print("Sorry, but you're in my story now.")
        time.sleep(3)
        os('cls')
        print("This is a very sad story about the death of a man named Stanley.\nStanley is quite a boring fellow. He has a job that demands nothing of him, and every button that he pushes is a reminder of the inconsequential nature of his existence.\nLook at him there, pushing buttons, doing exactly what he's told to do.\nNow, he's pushing a button. Now, he's eating lunch. Now, he's going home; now, he's coming back to work.\nOne might even feel sorry for him, except that he's chosen this life. But in his mind - ah, in his mind he can go on fantastic adventures.\nFrom behind his desk, Stanley dreamed of wild expeditions into the unknown, fantastic discoveries of new lands. It was wonderful. And each day that he returned to work was a reminder that none of it would ever happen to him.")
        time.sleep(5)
        print("And so he began to fantasize about his own job.\nFirst he imagined that one day, while at work, he stepped up from his desk to realize that all of his co-workers, his boss, everyone in the building, had suddenly vanished off the face of the Earth.\nThe thought excited him terribly. So, he went further.\nHe imagined that he came to two open doors, and that he could go through either.\nAt last, choice! It barely even mattered what lay behind each door - the mere thought that his decisions would mean something was almost too wonderful to behold.")
        time.sleep(5)
        print("As he wandered through this fantasy world, he began to fill it with many possible paths and destinations.\nDown one path lay an enormous round room with monitors and mind controls, and down another was a yellow line that weaved in many directions, and down another was a game with a baby.\nAnd he called it The Stanley Parable.\nIt was such a wonderful fantasy, and so in his head, he relived it again, and then again, and again, over and over, wishing beyond hope that it would never end, that he would always feel this free.\nSurely there's an answer down some new path - mustn't there be?\nPerhaps if he played just one more time.")
        time.sleep(5)
        print("But there is no answer.\nHow could there possibly be? In reality, all he's doing is pushing the same buttons he always has.\nNothing has changed. The longer he spends here the more invested he gets, the more he forgets which life is the real one.\nAnd I'm trying to tell him this: that in this world he can never be anything but an observer.\nThat as long as he remains here he's slowly killing himself. But he won't listen to me. He won't stop. Here, watch this. Stanley, the next time the screen asks you to push a button, do not do it.")
        time.sleep(3)

        key_pressed1, key_pressed2 = False, False

        def timeout():
            time.sleep(5)
            if not key_pressed1 or not key_pressed2:
                sys.exit()

        def get_key():
            global key_pressed1, key_pressed2
            input("Press E")
            key_pressed1 = True
            input("Press K")
            key_pressed2 = True
            time.sleep(10)

            key_pressed = False
            thread = threading.Thread(target=timeout)
            thread.start()
            get_key()

        
        
        
        
        
if user_choice_catwalk_cargo_hall == "j":
    print("Stanley jumped off the cargo lift")
            
        
else:
    print("Invalid input. Please enter 'L' or 'R'.")
time.sleep(1)
