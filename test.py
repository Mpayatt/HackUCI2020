import paralleldots
Name = 'Gokul'

api_key = '' #DO NOT PUBLISH KEY!

paralleldots.set_api_key(api_key)

File_Name = 'test.py'
File_object = open(File_Name, "a")
read_Object = File_object.read


def sentimentVal(receivedMessage):
    results = paralleldots.sentiment(read_Object, "en")
    output = 0
    for sense, num in results['sentiment'].items():
        if num > output:
            output = num
            emotion = sense
    return emotion

def messageSent(receivedMessage, emotion, Name):
    if emotion == 'positive' or emotion == 'neutral':
        message = Name + " is safe. They said: " + message + ". - Mr.Gency Bot"
    else:
        message = Name + " may be in trouble. They said: " + message + ". If \
                they are in trouble, please contact them or someone who may \
                be able to help. - Mr.Gency Bot"
    return message
    



    
    
print(messageSent(sentimentVal(read_Object), Name))
