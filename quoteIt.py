import random

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

#----------#

def get_welcome_response():
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Hello! Welcome to the inspire me skill. Get ready to be inspired. Ask me an inspirational quote."
    reprompt_text = "Knock, knock... Please ask me to tell you an inspirational quote."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_end_response():
    session_attributes = {}
    card_title = "Goodbye"
    speech_output = "Thanks For using this skill. See ya."
    reprompt_text = "Thanks For using this skill. See ya."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "I hope you got inspired. You are the best! See ya!"
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def create_quote_attributes(selected_quote):
    return {"quote": selected_quote}


def get_a_quote(intent, session):
    sessionAttributes={}
    session_attributes = {}
    quotes=['Nothing is impossible, the word itself says Im possible.',
                'Ive learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel.',
                'Whether you think you can or you think you cannot, you are right',
                'Perfection is not attainable, but if we chase perfection we can catch excellence.',
                'Life is 10% what happens to me and 90% of how I react to it.',
                'If you look at what you have in life, you will always have more. If you look at what you do not have in life, you will never have enough.',
                'Remember no one can make you feel inferior without your consent.',
                'I cannot change the direction of the wind, but I can adjust my sails to always reach my destination.',
                'Believe you can and you are halfway there.',
                'To handle yourself, use your head; to handle others, use your heart.',
                'Too many of us are not living our dreams because we are living our fears.',
                'Do or do not. There is no try.',
                'Whatever the mind of man can conceive and believe, it can achieve.',
                'Twenty years from now you will be more disappointed by the things that you did not do than by the ones you did do, so throw off the bowlines, sail away from safe harbor, catch the trade winds in your sails. Explore, Dream, Discover.',
                'I have missed more than 9000 shots in my career. I have lost almost 300 games. 26 times I have been trusted to take the game winning shot and missed. I have failed over and over and over again in my life. And that is why I succeed.',
                'Strive not to be a success, but rather to be of value.',
                'I am not a product of my circumstances. I am a product of my decisions.',
                'When everything seems to be going against you, remember that the airplane takes off against the wind, not with it.',
                'The most common way people give up their power is by thinking they do not have any.',
                'The most difficult thing is the decision to act, the rest is merely tenacity.',
                'It is during our darkest moments that we must focus to see the light.',
                'Do not judge each day by the harvest you reap but by the seeds that you plant.',
                'The only way to do great work is to love what you do.',
                'Change your thoughts and you change your world.',
                'The question is not who is going to let me; it is who is going to stop me.',
                'If you hear a voice within you say you cannot paint, then by all means paint and that voice will be silenced.',
                'Build your own dreams, or someone else will hire you to build theirs.',
                'Remember that not getting what you want is sometimes a wonderful stroke of luck.',
                'You cannot use up creativity. The more you use, the more you have.',
                'I have learned over the years that when our mind is made up, this diminishes fear.',
                'I would rather die of passion than of boredom.',
                'A truly rich man is one whose children run into his arms when his hands are empty.',
                'A person who never made a mistake never tried anything new.',
                'What is money? A man is a success if he gets up in the morning and goes to bed at night and in between does what he wants to do.',
                'I have been impressed with the urgency of doing. Knowing is not enough; we must apply. Being willing is not enough; we must do.',
                'If you want to lift yourself up, lift up someone else.',
                'Limitations live only in our minds. But if we use our imaginations, our possibilities become limitless.',
                'If you are offered a seat on a rocket ship, do not ask what seat! Just get on.',
                'Certain things catch your eye, but pursue only those that capture the heart.',
                'When one door of happiness closes, another opens, but often we look so long at the closed door that we do not see the one that has been opened for us.',
                'Everything has beauty, but not everyone can see.',
                'How wonderful it is that nobody need wait a single moment before starting to improve the world.',
                'When I was 5 years old, my mother always told me that happiness was the key to life. When I went to school, they asked me what I wanted to be when I grew up. I wrote down happy. They told me I did not understand the assignment, and I told them they did not understand life.',
                'The only person you are destined to become is the person you decide to be.',
                'We cannot help everyone, but everyone can help someone.',
                'Everything you have ever wanted is on the other side of fear.',
                'We can easily forgive a child who is afraid of the dark; the real tragedy of life is when men are afraid of the light.',
                'Nothing will work unless you do.',
                'I alone cannot change the world, but I can cast a stone across the water to create many ripples.',
                'What we achieve inwardly will change outer reality.'
                ]
    index=random.randint(0,50)
    sessionAttributes = create_quote_attributes(quotes[index])
    myQuote=sessionAttributes['quote']
    speech_output = "Here is your quote: " + myQuote
    reprompt_text = "I hope you were inspired."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        "", speech_output, reprompt_text, should_end_session))


#----------#

def on_session_started(session_started_request, session):
    return get_welcome_response()

def on_launch(launch_request, session):
    return get_welcome_response()


def on_intent(intent_request, session):
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    if intent_name == "getQuoteIntent":
        return get_a_quote(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    return get_end_response()
    
#----------#

def lambda_handler(event, context):
    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
