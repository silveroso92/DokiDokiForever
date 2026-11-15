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
    phone_mom "...WHAT?? WHO DO YOU THINK YOU-{nw=0.5}"
    phone end call
    
    return

label phone_dad_day03_1:
    phone call "dad"
    phone_mc "I'm here! I'm here!"
    phone_dad "So you haven't gone deaf. Good to know."
    phone_mc "What's up?"
    phone_dad "Just making sure that 'what' is you. We don't want to hear about any truancy today so I figured I'd give you a wake up call."
    "And what if I would have just turned my phone off?"
    phone_dad "In case you were thinking about turning your phone off, we would have called your neighbor again to give you a bit of motivation."
    phone_dad "And I personally would give her that bounty. Dead or alive."
    "*gulp*"
    phone_mc "... I wasn't going to skip today, okay? I'm fully aware of the stakes."
    phone_dad "You better be. You need to start watching out for yourself. While we may be your safety net now, we're not gonna just hold you. We'll fling you back into it."
    phone_dad "Remember, we're not gonna be here forever. That goes for everyone. So you need to prepare to hold your own weight."
    phone_mc "Yeah. I know..."
    phone_dad "Okay. You should have time to make yourself some breakfast, so do that and don't skip it. Based on your behavior yesterday I take it you didn't eat much, did you?"
    phone_mc "Wait. How did you-{nw=0.7}"
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

label sayori_text_day06_1:
    phone discussion "stl":
        "s" "Hey! Get any progress yesterday?"
        mc "I remember on our walk home that I told her my plan of barreling through the rest of my homework. I figured at the time it was the easiest thing to open up to her about."
        "mc" "Yeah. I got basically all of it done. Just got my post school roadmap to do."
        "s" "Cool Beans! : )"
        "s" "So Whatcha got planned today?"
        "mc" "I gotta get groceries. Ran out of food."
        mc "As I sit there and go back to thinking of food to add, it hits me: Sayori most likely wants to hang out today. "
        mc "Sure, we spend time in the club and on walks, but we haven't really done anything outside of school together in a while."
        "mc" "Hey, would you want to head out with me to the store? We can take a few detours on the way there. I was planning on heading out soon anyway."
        "s" "Yeah! I'll be ready in a bit! You can come over whenever!!"
        "mc" "Great! See you in a few."
        "s" "See ya!! :D"
    phone end discussion
    return
 
label dad_text_day2:
    phone discussion "dd2":
        "dad" "Sayori's mom told us about Elsea. Sorry to hear about that kiddo."
        "dad" "I understand your wounds are still fresh and this is a big change, so I was able to talk to your mother to give a bit of leniency from what happened this morning, but that doesn't excuse you from responsibilities."
        "dad" "You're almost an adult. You won't be able to run away from your problems. Focus on your school right now so you don't ruin your future."
        "dad" "We're here if you need to talk."
        "dad" "Love you."
        pause
    phone end discussion
    return

label break_up_text:
    phone discussion "but":
        pause  
    phone end discussion

    return
