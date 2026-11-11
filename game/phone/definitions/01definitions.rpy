# /!\ default
# pc as in phone character :monikk:
default pc_sayori  = phone.character.Character("Sayori", phone.asset("sayori_icon.png"), "s", 21, "#22Abf8")
default pc_mc      = phone.character.Character(" ", phone.asset("mc_icon.png"), "mc", 35, "#484848")
default pc_yuri    = phone.character.Character("Yuri", phone.asset("yuri_icon.png"), "y", 20, "#a327d6")
default pc_monika  = phone.character.Character("Monika", phone.asset("monika_icon.png"), "m", 40, "#0a0")
default pc_natsuki  = phone.character.Character("Natsuki", phone.asset("natsuki_icon.png"), "n", 45, "#fbb")
default pc_elsea  =  phone.character.Character("Elsea", phone.asset("mc_icon.png"), "e", 50, "#b60505")
default pc_mom  =  phone.character.Character("Mom", phone.asset("mc_icon.png"), "mom", 50, "#b60505")
default pc_dad  =  phone.character.Character("Dad", phone.asset("mc_icon.png"), "dad", 50, "#b60505")

default pov_key = "mc"

define phone_s  = Character("Sayori", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_mom  = Character("Mom", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_m  = Character("Monika", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_d  = Character("Dad", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_mc_sayer  = Character(" ", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define call_mc = Character("[player]", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")

init 100 python in phone.application:
    add_app_to_all_characters(message_app)
    add_app_to_all_characters(call_history_app)
    add_app_to_all_characters(calendar_app)

init 100 python in phone.calendar:
    add_calendar_to_all_characters(2023, 6, MONDAY)

init phone register:
    define "Welcome":
        add "s" add "mc" add "y" add "m" add "n" add "e" add "d" add "mom"
        icon phone.asset("default_icon.png")
        as thanks_for_using_my_framework key "ddu"

label break_up_text:
    phone discussion "ddu":
        "mc" "what do you mean?"
        "e" "Its just been too much. i cant keep doing this with you. I need a break"
        "mc" "What did I do wrong. tell me. we can work this out"
        "e" "We cant. im sorry we couldnt make this work"

    phone end discussion

    return

label phone_discussion_test:
    phone discussion "ddu":
        time year 2027 month 6 day 5 hour 16 minute 30 delay -1 # exact date and time at which i wrote this. yes i am feeling quite silly and goofy
        label "'Sayori' has been added to the group" delay -1
        label "'MC' has been added to the group" delay -1
        label "'Yuri' has been added to the group" delay -1
        label "'Monika' has been added to the group" delay -1
        label "'Natsuki' has been added to the group" delay 0.2
        "m" "Hey there!"
        "n" "Thank you for using my framework."
        "n" "I mean {i}of course{/i} you're using {b}this{/b} framework."
        "n" "...not like there are any better ones out there~"
        "s" "natsuki!!!!! {emoji=EllenScream}"
        "s" "no being a meanie!!!!!!!{emoji=EllenScream}{emoji=EllenScream}{emoji=EllenScream}"
        "y" "If you are interested in DDLC mods, be sure to check out our mod {a=https://undercurrentsmod.weebly.com}Doki Doki Undercurrents{/a}! {emoji=Melody}"
        "mc" "In case you encounter an issue (or wanna make a suggestion),"
        "mc" "you can:"
        "mc" "DM me at {i}elckarow{/i} on Discord,"
        "mc" "open an issue on {a=https://github.com/Elckarow/Better-EMR-Phone}GitHub{/a},"
        "mc" "make a post on the phone's {a=https://elckarow.itch.io/better-emr-phone}Itch page{/a}."
        "s" "Happy coding!" 
    phone end discussion

    return

label phone_call_test:
    phone call "s"
    phone_s "Ohayouuu!!!!!!!!!!!!!!!!"
    phone_s "Hey!"
    "Why is she always this energetic?"
    phone end call
    "..."

    return

label phone_mom_day02_1:
    phone call "mom"
    call_mc "What is it?"
    phone_mom "What do you think you are doing??"
    phone_mc_sayer "My heart drops"
    call_mc "...w..what?"
    phone_mc_sayer "I look at the caller ID."
    phone_mc_sayer "Crap"
    phone_mom "You heard what I said. Why are you not in school? We just got a call that you never showed up for your homeroom! And what's this about falling asleep in class?"
    call_mc "...."
    phone_mom "Well? Are you gonna say something or just sit there being silent?"
    phone_mc_sayer "All the frustration begins to well up and I start choking on my words."
    call_mc "..I, I just can't...keep..."
    phone_mom "You are too old to be trying to pull this crap. Do you really think you and Elsea will have any sort of future if you keep acting like this? Get to school! NOW!"
    call_mc "You...don't know-"
    phone_mom "Know what?"
    call_mc "...of course you don't. That would require you to be here."
    phone_mom "...WHAT?? WHO DO YOU THINK YOU-{nw=0.5}"
    phone end call
    
    return

label phone_dad_day03_1:
    phone call "dad"
    call_mc "I'm here! I'm here!"
    phone_dad "So you haven't gone deaf. Good to know."
    call_mc "What's up?"
    phone_dad "Just making sure that 'what' is you. We don't want to hear about any truancy today so I figured I'd give you a wake up call."
    phone_mc_sayer "And what if I would have just turned my phone off?"
    phone_dad "In case you were thinking about turning your phone off, we would have called your neighbor again to give you a bit of motivation."
    phone_add "And I personally would give her that bounty. Dead or alive."
    phone_mc_sayer "*gulp*"
    call_mc "... I wasn't going to skip today, okay? I'm fully aware of the stakes."
    phone_dad "You better be. You need to start watching out for yourself. While we may be your safety net now, we're not gonna just hold you. We'll fling you back into it."
    phone_dad "Remember, we're not gonna be here forever. That goes for everyone. So you need to prepare to hold your own weight."
    call_mc "Yeah. I know..."
    phone_d "Okay. You should have time to make yourself some breakfast, so do that and don't skip it. Based on your behavior yesterday I take it you didn't eat much, did you?"
    call_mc "Wait. How did you-{nw=0.7}"
    phone_dad "Call it 22 years experience."
    call_mc "But I'm 18..."
    phone_dad "And the second one I have to live with who gets like that."
    phone_mom "What was that?"
    phone_dad "I said you order breakfast yet?"
    phone_mom "*grumble*"
    phone_mc_sayer "I chuckle for the first time in days"
    phone_dad "I gotta go. Get some food and go to school."
    call_mc "Yeah. Will do."
    phone end call

    return

    
#    d "Sayori's mom told us about Elsea. Sorry to hear about that kiddo."
#    d "I understand your wounds are still fresh and this is a big change, so I was able to talk to your mother to give a bit of leniency from what happened this morning, but that doesn't excuse you from responsibilities."
#    d "You're almost an adult. You won't be able to run away from your problems. Focus on your school right now so you don't ruin your future. "
#    d "We're here if you need to talk. "
#    d "Love you." 