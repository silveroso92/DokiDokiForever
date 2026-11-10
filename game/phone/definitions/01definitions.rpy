# /!\ default
# pc as in phone character :monikk:
default pc_sayori  = phone.character.Character("Sayori", phone.asset("sayori_icon.png"), "s", 21, "#22Abf8")
default pc_mc      = phone.character.Character("MC", phone.asset("mc_icon.png"), "mc", 35, "#484848")
default pc_yuri    = phone.character.Character("Yuri", phone.asset("yuri_icon.png"), "y", 20, "#a327d6")
default pc_monika  = phone.character.Character("Monika", phone.asset("monika_icon.png"), "m", 40, "#0a0")
default pc_natsuki= phone.character.Character("Natsuki", phone.asset("natsuki_icon.png"), "n", 45, "#fbb")
default pc_elsea =  phone.character.Character("Elsea", phone.asset("natsuki_icon.png"), "e", 50, "#b60505")
default pc_mom =  phone.character.Character("Mom", phone.asset("natsuki_icon.png"), "mom", 50, "#b60505")
default pc_dad =  phone.character.Character("Dad", phone.asset("natsuki_icon.png"), "dad", 50, "#b60505")

default pov_key = "[player]"

define phone_s  = Character("Sayori", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_mom  = Character("Mom", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_m  = Character("Monika", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_d  = Character("Dad", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")


init 100 python in phone.application:
    add_app_to_all_characters(message_app)
    add_app_to_all_characters(call_history_app)
    add_app_to_all_characters(calendar_app)

init 100 python in phone.calendar:
    add_calendar_to_all_characters(2023, 6, MONDAY)

init phone register:
    define "Welcome":
        add "s" add "mc" add "y" add "m" add "n" add "e"
        icon phone.asset("default_icon.png")
        as thanks_for_using_my_framework key "ddu"


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
    phone_mc "What is it?"
    phone_mom "What do you think you are doing??"
    "My heart drops"
    phone_mc "...w..what?"
    "I look at the caller ID."
    "Crap"
    phone_mom "You heard what I said. Why are you not in school? We just got a call that you never showed up for your homeroom! And what's this about falling asleep in class?"
    phone_mc "...."
    phone_mom "Well? Are you gonna say something or just sit there being silent?"
    "All the frustration begins to well up and I start choking on my words."
    phone_mc "..I, I just can't...keep..."
    phone_mom "You are too old to be trying to pull this crap. Do you really think you and Elsea will have any sort of future if you keep acting like this? Get to school! NOW!"
    phone_mc "You...don't know-"
    phone_mom "Know what?"
    phone_mc "...of course you don't. That would require you to be here."
    phone_mom "...WHAT?? WHO DO YOU THINK YOU-{nw=2}
    phone end call

    return

label_phone_dad_day03_1:
    phone call "dad"
    phone_mc "I'm here! I'm here!"
    phone_dad "So you haven't gone deaf. Good to know."
    phone_mc "What's up?"
    phone_dad "Just making sure that 'what' is you. We don't want to hear about any truancy today so I figured I'd give you a wake up call."
    "And what if I would have just turned my phone off?"
    phone_dad "In case you were thinking about turning your phone off, we would have called your neighbor again to give you a bit of motivation."
    phone_add "And I personally would give her that bounty. Dead or alive."
    "*gulp*"
    phone_mc "... I wasn't going to skip today, okay? I'm fully aware of the stakes."
    phone_dad "You better be. You need to start watching out for yourself. While we may be your safety net now, we're not gonna just hold you. We'll fling you back into it."
    phone_dad "Remember, we're not gonna be here forever. That goes for everyone. So you need to prepare to hold your own weight."
    phone_mc "Yeah. I know..."
    phone_d "Okay. You should have time to make yourself some breakfast, so do that and don't skip it. Based on your behavior yesterday I take it you didn't eat much, did you?"
    phone_mc "Wait. How did you-{nw=2}
    phone_dad "Call it 22 years experience."
    phone_mc "But I'm 18..."
    phone_dad "And the second one I have to live with who gets like that."
    phone_mom "What was that?"
    phone_dad "I said you order breakfast yet?"
    phone_mom "*grumble*"
    "I chuckle for the first time in days"
    phone_dad "I gotta go. Get some food and go to school."
    phone_mc "Yeah. Will do."
    phone end call

    return