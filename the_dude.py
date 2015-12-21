"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function
import random

THE_DUDE_PHRASES = [
    "God damn you Walter! You fuckin' ass hole! Everything's a fuckin' travesty with you man! And what was all that shit about Vietnam? What the FUCK has anything got to do with Vietnam? What the fuck are you talking about?",
    "Walter, he peed on my rug!",
    "Walter, the chinaman who peed on my rug, I can't go give him a bill, so what the fuck are you talking about?",
    "We're going to cut your dick off, Larry.",
    "Mind if I do a J?",
    "Hey, nice marmot!",
    "And then the music business, briefly. Roadie for Metallica. Speed of Sound Tour. Bunch of ass holes.",
    "Thank you Donny.",
    "So if you could just write me my check for ten percent of a half a million... five grand... I'll go out and mingle.",
    "Beaver? Uhhhh, you mean vagina...? I mean, you know the guy?",
    "He thinks the carpet pissers did this?",
    "I was one of the original authors of the Port Huron Statement. Not the compromised second draft...",
    "Oh boy. How ya gonna keep 'em down on the farm once they've seen Karl Hungus?",
    "Fuckin' A, man. I got a rash, man.",
    "Does the Pope shit in the woods?",
    "That was the chief of police of Malibu. A real reactionary.",
    "I could be just sitting at home with pee stains on my rug.",
    "Did you ever hear of The Seattle Seven? That was me... and six other guys.", 
    "My only hope is that the big Lebowski kills me before the Germans can cut my dick off.",
    "Me and the driver. I'm not handling the money driving the car and talking on the phone all at the same time.",
    "I hate the fuckin' Eagles man.",
    "Where's the fucking money Lebowski?",
    "The Dude abides.",
    "Do you see a wedding ring on my finger? Does this place look like I'm fucking married? The toilet seat's up, man!",
    "Fortunately, I'm adhering to a pretty strict drug regimen to keep my mind, you know, limber.",
    "Obviously you're not a golfer.",
    "He fixes the cable?",
    "I'm just gonna go find a cash machine.",
    "Employed? Is this a... what day is this?",
    "You're not wrong Walter. You're just an ass hole.",
    "Mr. Treehorn treats objects like women, man.",
    "Well, they finally did it. They killed my fucking car.",
    "Let me explain something to you. I am not Mr. Lebowski. You're Mr. Lebowski. I'm the Dude. So that's what you call me. You know, that, or His Dudeness, or Duder, or El Duderino, if you're not into the whole brevity thing.",
    "Yeah, well, you know, that's just, like, your opinion, man.",
    "That rug really tied the room together.",
    "Walter, ya know, it's Smokey, so his toe slipped over the line a little, big deal. It's just a game, man.",
    "It's like what Lenin said... you look for the person who will benefit... and... uh... You know what I'm trying to say...",
    "You're not wrong Walter. You're just an ass hole.",
    "Mr. Treehorn treats objects like women, man.",
    "Walter, I love you, but sooner or later, you're going to have to face the fact you're a god damn moron.",
    "The usual. I bowl. Drive around. The occasional acid flashback.",
    "Hey, careful, man, there's a beverage here!",
    "What are you, a fucking park ranger now?",
    "Look, nothing is fucked, here, man.",    
    "You mean coitus?",
    "Yes, Walter, you're right. There is an unspoken message here. It's FUCK YOU, LEAVE ME THE FUCK ALONE! <break time='1s'/> Yeah, I'll be at practice.",
    "Nobody calls me Lebowski. You got the wrong guy. I'm the Dude, man.",
    "Fuck sympathy! I don't need your fuckin' sympathy, man, I need my fucking johnson!",
    "Walter, what is the point? Look, we all know who is at fault here, what the fuck are you talking about?",
    "Walter, this isn't a guy who built the railroads here.",
    "I'll tell you what I'm blathering about... I've got information man! New shit has come to light! And shit... man, she kidnapped herself.",
    "She's not my special lady, she's my fucking lady friend. I'm just helping her conceive, man!",
    "Man, if my fuckin' ex-wife asked me to take care of her fuckin' dog while she and her boyfriend went to Honolulu I'd tell her to go fuck herself.",
    "This is a very complicated case, Maude. You know, a lotta ins, a lotta outs, a lotta what-have-yous. And, uh, a lotta strands to keep in my head, man. Lotta strands in old Duder's head.",
    "Racially he's pretty cool?",
    "Listen, Maude, I'm sorry if your stepmother is a nympho, but I don't see what it has to do with. do you have any Kahlua?",
    "Brother Seamus? Like an Irish monk?",
    "Who gives a shit about the fucking marmot!",
    "Well, I still jerk off manually.",
    "Well, they finally did it. They killed my fucking car."
]


def lambda_handler(event, context):
    if (event['session']['application']['applicationId'] !=
            "amzn1.echo-sdk-ams.app.24f14c2d-5b34-4253-9c62-fa019a4efc7b"):
        raise ValueError("Invalid Application ID")
    
    #if event['session']['new']:
    #    on_session_started({'requestId': event['request']['requestId']},
    #                       event['session'])
    
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def on_session_started(session_started_request, session):
    pass


def on_launch(launch_request, session):
    return get_welcome_response()


def on_intent(intent_request, session):
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    if intent_name == "TheDudePhrasesIntent":
        return the_dude_random_phrases(intent, session)
    elif intent_name == "TheDudeAmIWrongIntent":
        return am_i_wrong(intent, session)
    elif intent_name == "TheDudeFixesTheCableIntent":
        response={
            'title':"He fixes the cable?",
            'output':"He fixes the cable?",
            'reprompt':"Listen, Maude, I'm sorry if your stepmother is a nympho, but I don't see what it has to do with. do you have any Kahlua?"
        }
    elif intent_name == "TheDudeGotTheMoneyIntent":
        response={
            'title':"A complicated case.",
            'output':"This is a very complicated case, Maude. You know, a lotta ins, a lotta outs, a lotta what have yous. A lotta strands to keep in my head, man. Lotta strands in old Duder's head.",
            'reprompt':"Delayed after-effects?"
        }
    elif intent_name == "TheDudeWhoIsThisIntent":
        response={
            'title':"Dude, the Bagman.",
            'output':"Dude. The bag man, man. Where do you want us to go?",
            'reprompt':"Yeah. Me and, the driver. I'm not handling the money, driving the car and talking on the phone all at the same time."
        }
    elif intent_name == "TheDudeUsIntent":
        response={
            'title':"Dude, the Bagman.",
            'output':"Yeah. Me and, the driver. I'm not handling the money, driving the car and talking on the phone all at the same time.",
            'reprompt':"Shit! Walter, you fuck... you fucked it up! You fucked it up! Her life was in our hands, man!"
        }
    elif intent_name == "TheDudeWalterVietnamIntent":
        response={
            'title':"What the fuck has anything got to do with Vietnam?",
            'output':"God damn you Walter! You fuckin' ass hole! Everything's a fuckin' travesty with you man! And what was all that shit about Vietnam? What the FUCK has anything got to do with Vietnam? What the fuck are you talking about?",
            'reprompt':"You're a fuck Walter!"
        }
    elif intent_name == "TheDudePhonesRingingIntent":
        response={
            'title':"Thank you, Donny.",
            'output':"Thank you Donny.",
            'reprompt':"That rug really tied the room together."
        }
    elif intent_name == "TheDudeHateTheEaglesIntent":
        response={
            'title':"I hate the fuckin' Eagles, man!",
            'output':"Come on, man. I had a rough night and I hate the fuckin' Eagles, man!",
            'reprompt':"I was one of the original authors of the Port Huron Statement. Not the compromised second draft..."
        }
    elif intent_name == "TheDudeEmployedIntent":
        response={
            'title':"Employed?",
            'output':"Employed?",
            'reprompt':"Is this a... what day is this?"
        }
    elif intent_name == "TheDudeDressedLikeThatIntent":
        response={
            'title':"What day is this?",
            'output':"Is this a... what day is this?",
            'reprompt':"I do mind, the Dude minds. This will not stand, ya know, this aggression will not stand, man."
        }
    elif intent_name == "TheDudeIfYouDontMindIntent":
        response={
            'title':"This aggression will not stand, man.",
            'output':"I do mind, the Dude minds. This will not stand, ya know, this aggression will not stand, man.",
            'reprompt':"The old man told me to take any rug in the house."
        }
    elif intent_name == "TheDudeRecreationIntent":
        response={
            'title':"The occasional acid flashback.",
            'output':"The usual. I bowl. Drive around. The occasional acid flashback.",
            'reprompt':"You mean coitus?"
        }
    else:
        raise ValueError("Invalid intent")
        
    return standard_dude_response(intent, session, response)


def on_session_ended(session_ended_request, session):
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    card_title = "The Dude"
    session_attributes = {}
    
    speech_output = "Dude here. You can ask me for a quote by saying something like, give me a quote. Or you can engage me in conversation by saying something like, phone's ringing dude. To which I would reply, thank you donny."
    reprompt_text = "Come on man, I don't have all day. How about you ask me for a quote?"
    
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def the_dude_random_phrases(intent, session):
    card_title = "The Dude Phrases"
    session_attributes = {}
    
    speech_output = THE_DUDE_PHRASES.pop(random.randint(0,len(THE_DUDE_PHRASES)-1))
    reprompt_text = THE_DUDE_PHRASES.pop(random.randint(0,len(THE_DUDE_PHRASES)-1))
    
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def standard_dude_response(intent, session, response):
    card_title = response['title']
    session_attributes = {}
    
    speech_output = response['output']
    reprompt_text = response['reprompt']
    
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def am_i_wrong(intent, session):
    card_title = "You're not wrong, you're just an asshole."
    session_attributes = {}
    
    speech_output = "No you're not wrong."
    reprompt_text = "You're not wrong Walter. You're just an ass hole."
    should_end_session = False
    session_attributes['amiwrong']=1
    
    if 'attributes'in session.keys():
        if session['attributes'] != None:
            if 'amiwrong' in session['attributes'].keys():
                if session['attributes']['amiwrong']==1:
                    speech_output = "You're not wrong Walter. You're just an ass hole."
                    reprompt_text = "Walter, I love you, but sooner or later, you're going to have to face the fact you're a goddamn moron."
                    should_end_session = False
                    session_attributes['amiwrong']=0
        
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }