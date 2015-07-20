'''
Insult a user.
'''

import random
from inc import *

modFunc.addCommand('insult', 'insult', 'insult')

# TODO: extend.
nouns = [
    'fucker',
    'ass',
    'motherfucker',
    'asshole',
    'idiot',
    'skid',
    'lardass',
    'piece of shit',
    'dumb fuck',
    'retard',
    'skid',
    'fgt',
    'fgrt',
    'hipster',
    'self fornicator',
    'skidiot',
]

# TODO: extend.
adjectives = [
    'lazy',
    'dumb',
    'skiddish',
    'proprietary',
    'Windows using',
    'truffle butter loving',
    'dirty sanchez receiving',
    'brainless',
]

# TODO: extend.
phrases = [
    'Shut up, {NICK}, you {adj} {noun}!',
    'Eat shit, {NICK}!',
    'Why are you so {adj}, {NICK}, maybe you\'re just a {noun}?',
    'You are such a little {noun} {NICK}.',
    'Why be a {adj} {noun}, {NICK}?',
    '{NICK}, you {adj} {noun}.',
    "{NICK}, you're worse than a Windows user running Safari at starbucks. You {adj} {noun}!",
    "{NICK}, you're the type of user that leaves his laptop on the carpet overnight. {adj} {noun}...",
    "Even HF wouldn't accept you {NICK}!",
    "{NICK}, why do you eat so much cock fgrt?",
    "{NICK}, do the world a favor and go to nullbyte...",
    "{NICK}, dufuq faggot!",
    "{NICK}, eat a dick and puke acid.",
    "{NICK}, go eat a bloody tampon, {noun}.",
    "{NICK}, you should have been aborted.",
    "{NICK}, you're so ugly, the doctor slapped your mom for bringing you into this world.",
    "{NICK}, you suck as much cawk as TheConsultant. {noun}....",
    "{NICK}, you're a noob and Xires hasn't been fed...",
    "{NICK}, you're worse than Justin Bieber!",
    "{NICK}, ha {noun}, I fucked your mom last night, then she paid me",
    "Go fuck yourself {NICK}",
    "{NICK}, go suck chris1's tities, you {noun}!",
    "{NICK}, go get another anal creampie from your brother {adj} {noun}!",
    "Why are you still breathing {NICK}?",
    "{NICK}, do the world a favor and jump off a cliff...",
    "{NICK}, go back to the 90s...{noun}!",
    "{NICK}, hey slut, want more anal cleansing?",
    "{NICK}, your face looks like Lindsey Lohan's beat up vagina!",
    "{NICK}, my brother saw you at the gay bar last night. He said you were giving $5 blowjobs in the bathroom.... They sucked....",
    "I KNEW IT WAS YOU {NICKUPPER}. Fucking caught this {noun} eating horseshit at the farm.",
    "Go take a shower, you fucking stink {NICK}.",
    "{NICK} GTFO and go back to HF.",
    "{NICK} GTFO and go back to nullbyte.",
    "{NICK} I heard HF has super FUD cryptors. You just have to suck shwack13's dick first.. Should not be a problem for you.. I also heard you are good at that sort of thing.",
    "{NICK} you can't even program HTML bruh",
    "{NICK}, do you even code bro?",
    "{NICK}, y u mad {noun}?",
    "This insult is not for the intended user.... Just wanted to say that TheConsultant is a {adj} {noun}....",
    "Xires is love. Xires is life.",
    "chris1 for GMOD! Also, unrelated but {NICK} is a {adj} {noun}.",
    "{NICK}  <- this nigga, I caught him getting sucked off by shwack13... AGAIN",
    "{NICK}, lolfgrt",
    "{NICK} is lord of the fags and will suck dicks for shells.",
    "{NICK}, you suck as much dick as Shwack13.",
    "{NICK}, I can't believe it, you actually have an uglier mug than TheConsultant...",   
    "{NICK}, at least you have a LITTLE BIT more brains than shwack13.",
    "{NICK} <-- great... Shwack13 2.0",
    "{NICK} <-- just another {noun} as {adj} as Consultant.",
    "{NICK}, why does your ass look like shwack13's face? Thats just not normal...",
    "{NICK}, Opens cmd, tells everyone he is a hacker",
    "{NICK}, at least you give better head than Consultant.",
    "{NICK}, why do you continue to talk? You need to realise (along with theconsultant) sometimes you just have to shut the fuck up!",
    "{NICK}, your asshole is looser than TheConsultant's.",
    "{NICK}, you're almost as much of a skid as Rytiou.",
    "{NICK}, damn you're stupider than shwack13... Worst part is stupider ain't even a word...",
    "{NICK}, I want to punch you in the face, just like I do with TheConsultant every time he opens his mouth.",
    "Damn {NICK}, your breath smells like you jammed 10 cocks in TheConsultant's ass, then ate them.",
    "{NICK}, blah blah blah. You just want to eat Chris MacFarlane's asshole in a dimly lit alley.",
    "{NICK}, you remind me of Chris MacFarlane, ugly, dumb, and determined to not see it.",
    "'Hey, where's the code? I can't find it? Can anyone help me???' - Every new user",
    "My name is Chris MacFarlane (TheConsultant, schwack13) I live in Kelowna bc Canada, and I like penis as much as {NICK} does....",
    "{NICK}, It looks like you eat just as much cawk as Chris MacFarlane, {adj} {noun}.",
    "{NICK}, you enjoy crossing swords with Chris MacFarlane, don't you. DON'T YOU FAGGOT.",
    "{NICK}, you look like someone who would be friends with TheConsultant.... You can find Chris MacFarlane at 174.4.162.239.",
    "{NICK}, don't beg, you're worse than Rytiou requesting VIP.",
    "{NICK}, you are even worse than Rytiou, and we know it's a damn hard thing to be.",
    "Damn {NICK}, you're crying harder than Rytiou at a One Direction concert.",
    "{NICK}, you are a noob but you'll never be as noobish as Rytiou. He's of a different breed.",
    "{NICK}, your mom was on my dick like white on rice, on a paper plate, in a snow storm.",
    "{NICK}, you remind me of Rytiou, funny, but only halfway retarded.",
    "Damn {NICK} you look like you are starting to grow some facial hair... Can't say the same for poor Rytiou.",
    "{NICK}, you whine as much as chris1 coding EZBot.",
    "{NICK}, you'll never compare to DeepCopy, he sucked dick for bitcoins.",
    "{NICK}, you should join Puddi's new hacking team called 'Dick Squad' since you like talking about cocks so much.",
    "{NICK}, you're so lame we decided to change your nick to Rytiou's bitch.",
    "DeepCopy, the guy who can't keep from chaning his name every 5 seconds.",
    "Rytiou joins #dicksuckers,0 to meet other fgrts like yourself, {NICK}.",
    "The only cock {NICK} has is on chris1's profile picture.",
    "Just blame {NICK}. He's everybody's scapegoat.",
    "{NICK}, your dick is just as 'big' as Rytiou's brain",
    "{NICK}, you're such a little bitch, I like bushido more than you.",
    "{NICK}, did you code that on a potato?",
    "{NICK}, why do you smell like pee? Reminds me of the time i gave Rytiou a golden shower... He kept drinking it.",
    "{NICK}, you remind me of xor, smart, but has a small dick.",
    "{NICK}'s passwords are about as strong as 'Hacking Team'. Suprised he isn't pwned yet",
    "{NICK}, why are you crying like a little bitch? Bushido has more balls than you.",
    "{NICK}, your face makes me want to kill myself.",
    "{NICK}, great another shitty person to insult.",
    "{NICK}, oh look a {noun}.",
    "{NICK}, you remind me of a cheap hooker.",
    "{NICK}, is your face supposed to look like that?",
    "{NICK}, awe, did your ego get bruised?",
    "{NICK}, you have a face not even a mother could love... Just like Chris MacFarlane.",
    "{NICK}, sorry to have to be the bearer of bad news, but you're more retarded than TheConsultant.",
    "DeepCopy's, birth certificate is an apology from the condom factory."
    "{NICK}, you're lazier than chris1 adding insults to the database.",
    "{NICK}, shut up, you'll never be the man your mother is.",
    "{NICK}, wow you can google... Maybe you can teach Rytiou something.",
    "{NICK}, {noun}, you're so ugly Hello Kitty said goodbye to you.",
    "{NICK}, you belong on HF, you can meet up with Rytiou and suck each other's dicks.",
    "{NICK}'s family tree is a cactus because everybody on it is a prick.",
    "{NICK}, if you were twice as smart as DeepCopy, you'd still be stupid.",
    "{NICK}, I guess you may have a little bit of brains... Too bad it never quite worked out that way for Rytiou...",
    "{NICK}, if you were twice as smart as Deepcopy, maybe you'd have one complete neurone.",
    "{NICK}, you're just as retarded as Synfer... Well maybe not as retarded but almost.",
    "{NICK}, you remind me of Synfer a {adj} fucking {noun} that can't distinguish the difference between pee and poop."
    "{NICK}, you're as stupid as techb creating a new alias then telling everyone its him.",
    "You can report for cyber bullying whenever you see {NICK}'s face.",
    "{NICK}, you cry every night like Rytiou, don't you?",
    "{NICK}, you're such a liar, you're just like Synfer.",
    "{NICK}, you eat so much dick we should change your nick to Synfer.",
    "<insult here>",
    "{NICK}, your face is covered in donkey semen... Reminds me of the time i went to the farm with techb.",
    "You should have been the stain on the couch {NICK}.",
    "{NICK}, your father regrets not dumping you in the toilet like all of your possible siblings.",
    "{NICK}, you should crawl in a hole and eat dog shit, you can join Rytiou, he's already there.",
    "{NICK}, why don't you grow up a little bit... I don't like fighting midgits.",
    "{NICK}, are you supposed to be that ugly?",
    "{NICK}, {noun} of the year!",
    "{NICK}, we couldn't even store you with the radioactive garbage.",
    "{NICK}, you're as stupid as Rytiou, not understanding how to insult someone else at the same time as the intended target.",
    "{NICK}, you're as cheap as the hooker I paid to spit in your mouth last night.",
    "{NICK}, you're worse than dotzilla's mIRC post.",
    "{NICK}, you're so retarded you give a bad name to {noun}s everywhere.",
    "{NICK}, you're so stupid, you think downs in a fabric softener.",
    "{NICK}, you're worse than Chris MacFarlane...",
    "{NICK}, you're so fat, when you sit around the house, you sit AROUND THE HOUSE.",
    "{NICK}, you're an attention seeking whore like TheConsultant.",
    "{NICK}, you smell like shit... Take a bath or something.",
    "{NICK}, do you even lift bro?",
    "{NICK}, close your legs, smells like a fucking fish market.",
    "{NICK}, fuck off and eat another bloody tampon.",
    "{NICK}, you eat so much cock i should just call you phil.",
    "{NICK}, you remind me of phil, full of shit.",
    "{NICK}, fuck dude you're slower than phil coding a website for a friend.",
    "Damn {NICK}, you're just like phil, so full of shit your eyes are brown.",
    "{NICK}, you get fucked so hard by your gay lover i should just call you HTH.",
    "{NICK}, you're so damn stupid, you tried trading bitcoins for dogecoins.",
    "{NICK}, you're as stupid as dotzilla trying to highlight a disconnected user.",
    "{NICK}, you should get some sleep instead of fucking HTH in the ass all night.",
    "{NICK}, you're slower than phil is when he wakes up in the morning.",
]


def build_phrase(nick):
    p = random.choice(phrases)
    while '{' in p:
        rep = p[p.index('{'):p.index('}')+1]
        if rep == '{NICK}':
            p = p.replace(rep, nick)
        elif rep == '{NICKUPPER}':
			p = p.replace(rep, nick.upper())
        elif rep == '{adj}':
            p = p.replace(rep, random.choice(adjectives))
        elif rep == '{noun}':
            p = p.replace(rep, random.choice(nouns))
    return p


def insult(line, irc):
    message, username, msgto = ircFunc.ircMessage(line)
    if message[1]:
        nick = message[1].strip()  # not sure about that, document your API!
        ircFunc.ircSay(msgto, build_phrase(nick), irc)
