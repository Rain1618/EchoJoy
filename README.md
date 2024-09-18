# EchoJoy

Built for **HackMIT 2024** 💻\
View our submission [here](https://ballot.hackmit.org/project/qyydc-fruuw-uvpbi-suxhg)\
Check out the other components of our project [here](https://github.com/janez45/HackMIT-2024)

VR-powered AI therapist that offers personalized emotional support by remembering past conversations and bringing up cherished memories and photos to uplift users 😄

## Inspiration

## What it does
EchoJoy is a VR-powered AI therapist designed to provide personalized emotional support. It remembers your past conversations and life moments, and when you're feeling low, it brings up nostalgic photos and happy memories to lift your spirits. With the ability to adjust environments and moods, EchoJoy creates a comforting, immersive experience that helps users reconnect with their happiest moments, offering both companionship and therapeutic relief when needed. Powered by Suno, it is also able to generate the right song for the right mood to help you feel your best! 🎵

## How we built it
The main VR app was built with Unity and C#, as well as many API calls to OpenAI, Whisper, and ElevenLabs. Vapi was also used to create the AI call that allowed for emotion detecting and uploading information such as your resume so the A.I understands you better. We also incorporated the Suno API and Convex when adding music and testing backends.

## Challenges we ran into

Unexpectedly, the "hardware" component was very difficult to integrate. To give you an understanding of what happened, here is a list of very unfortunate events: usb-c cord not powerful enough (the official cord is $80...), hard to integrate any external API with Unity, the literal GPU of our computer is incompatible with the headset, WiFi connection 😢, no bones to animate the mouth of our virtual companion, OS bigotry and anti-Mac discrimination 💢... Additionally, many of us were new to Unity, which we found rather challenging despite wanting to try something new. We are very grateful for the help of the greatest mentor ever, Gurjot, and fellow hackers in figuring these issues out.

## What's next 
If we had more time, we definitely want to fully integrate the parts into one full app with music, AI voice, and changing scenery based on what the user says. A big challenge was also animating Uncle Iroh's mouth to match when the AI responds, but it is something we definitely want to achieve to enhance the immersive experience. Other enhancements would also be interacting with the environment, such as being able to pick up and "drink" the tea, therapy dogs running/lying around, or even having multiple players interact with each other like customers at Iroh's tea shop.

## VR headset setup
We used the Meta Quest 2 headset for this project. \
Start by checking if your device is compatible:  https://www.meta.com/help/quest/articles/headsets-and-accessories/oculus-link/requirements-quest-link/ \
Set up developer mode: https://developers.meta.com/horizon/documentation/native/android/mobile-device-setup/ \
\
How to export builds: In Unity, go to File -> Build settings -> click on Build. Upload the .apk file to Google Drive or smth. Then in the VR headset, download the .apk file
Follow these instructions after: https://youtu.be/tau63RyAIoc
