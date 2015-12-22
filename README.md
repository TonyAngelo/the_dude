# The Dude
An Amazon Alexa Skill for talking with The Dude

The Alexa Skill [voice interface](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/defining-the-voice-interface) consists of three parts; the intent schema, slots and sample utterances. These files don't actually get used for anything, instead there content gets put into the Interaction Model when building the skill.

The Alexa Skill interacts with the [AWS Lambda function](https://developer.amazon.com/appsandservices/solutions/alexa/alexa-skills-kit/docs/developing-an-alexa-skill-as-a-lambda-function) the_dude.py

## Modes of operation

There are currently two different ways to interact with The Dude. 

### Mode the first

One way to interact with The Dude is to ask for a quote from the movie.

Example: "Alexa, ask The Dude for a quote."

You can keep asking for more quotes once the skill is launched.

Example: "Give me another."

### Mode the second

The other way to interact with The Dude is to engage him in conversation. Currently, these are the sayings that The Dude will respond to:

- "are you employed sir"
- "you don't go out looking for a job dressed like that on a weekday"
- "well i do work sir so if you don't mind"
- "phone's ringing dude"
- "you can imagine where it goes from here"
- "am I wrong" (line gets repeated)
- "what do you do for recreation"
- "i'm sorry dude goddamn wind"
- "i'll pull over and kick your ass out"
- "so Dieter has the money"
