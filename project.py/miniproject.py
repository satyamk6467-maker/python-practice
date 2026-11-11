# rule based ai paython chatbot 
import datetime
import time 

name= input("swagat hai , enter the name ")
presenthour= datetime.datetime.now().hour

if 5<= presenthour <= 11:
    print("good morning ," ,name )
elif 11<= presenthour <=17:
    print("good afternoon ,", name )
elif 17<= presenthour <=20:
    print("good evening ,",name )
else:
    print("good night,",name )



print("nammaste! welcome to your chatbot")
print("you can ask me the basic question ")

#chart bot memory formation 
response ={
    "hello": "hii, welcome. how can i help you",
    "how are you ": "i am fine .thank you",
    "who are you ":" i am your smart AI chat bot",
    "motivate me ":"keep going .every bug you solve is the new thing you have achived",
    "happy": " great to hear that ",
    "function kya hote hai ":" we have learnt this in chapter 7"
}

# method / function to get response of chat 
def getresponsebot(userquestion):
    userquestion= userquestion.lower()
    for eachkey in response:
        if eachkey in userquestion:
            return response[eachkey]
    return " i am not able to answer . i am still learning yet"

# take user input 
while True:
    userinput= input("please ask your question:")
    reply = getresponsebot(userinput)
    print("bot response :",reply)

    if "bye" in userinput.lower():
        break

    