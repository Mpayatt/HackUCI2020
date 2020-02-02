# HackUCI2020: Mr.Gency the Emergency Bot

<p align="center">
  <img width="460" height="460" src="https://github.com/Mpayatt/HackUCI2020/blob/master/images/LogoSmall.png">
</p>
  

  
**Abstract**

  Disasters can be stressful not only to the victims, but also their loved ones who can be left worrying out of the loop. With the unexpecting occurrences of natural disasters causing displacement and disruptions in communications around the world, those effected often need ways to quickly inform many people as soon as possible. The recent fires and floods that occurred in Australia are an example of disasters that may develop this fear and worry in the hearts of loved ones, fear that could be alleived by a quick text message. 
  
  Our project introduces the SMS bot Mr. Gency (pronounced M-ur-gency ), a bot powered by Twilio to help families stay notified of their loved one's well-being during a disaster. This is a system that allows users to sign up and input their name and emergency contact information into a system via SMS messages. In the event of an emergency, as soon as they are safe, the user can send a quick message to our bot describing their status. The bot will then quickly send short messages to everyone on their contacts to let them know their status.  
  
<p align="center">
  <img width="460" height="230" src="https://github.com/Mpayatt/HackUCI2020/blob/master/images/Mr.%20Gency.png?raw=true">
</p>
  
**Business Model**
  
  As this is an system designed for emergencies, we looked at implimenting it for the most benefit for the people. One way we considered it was through implementing Mr. Gency at the local govornment and county level. Were a Disaster management department were to subscribe, this service would be made available to everyone in the county, which would be validated by area code.
  We also looked at disaster-prone areas to implement this model so that we are able to study its effectiveness and improve upon it. Areas include places in Tornado Valley, New Orleans, and Los Angeles. In more rural areas, like Iberia parish in Louisiana, they have to deal with antiquated communications equiptment in some of the most hurricane and flood-prone environments. Services that could be baught cheaply would enable the people to do some of the communication themselves. If further developed, it could also help identify people that are safe to help the county direct releif and rescue efforts.

<p align="center">
  <img width="508" height="300" src="https://github.com/Mpayatt/HackUCI2020/blob/master/images/hazards.png">
</p>
  
**Future Plans**

  We worked on several features that might not make the cut for the hackathon due to time constraints. we used and API called ParallelDots that allows for us to examine their status from a message. From the analysis of the text, we could change the outgoing message to reflect if they are safe, still in danger etc. This would be useful because in the event of an emergency, the user might not be in a good state of mind to give a consise message themselves. We managed to get this feature working in isolation, but might not get it fully implemented in time.
  We also intended to implement input validation and greater interactivity, but seeing as this is a very rough proof of concept, these were cut for time. If we switched to Node.js, we could have created a chatbot with a greater degree of interactivity, but all of us had Python experience, so we went with that instead for the time being.
  Based on our progress, we came up with ideas that could be implemented in future models that could potentially improve communication and effectiveness. If subscribed to by a county for disaster releif, it could track who is reported in as safe, and this could help direct rescue efforts. 
  

  
**Our Hack Experience**

  Overall, our team had a fantastic experience at HackUCI 2020. We had fun teaming up and working together on a problem that seemed pertinent to society today. There were hurdles in trying to develop our program, trying to stay awake and active, and people scraping authorization codes for Twilio from our GitHub accounts. Nevertheless, this was an amazing experience for our team!
  
 

**Note**
if the Authorization code is missing in the final build, it is because we had an issue where our codes were sraped from out github repository and used to purchase 30$ worth of phone numbers. If you want to make make this work, you'll need 
your own keys.
