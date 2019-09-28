import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random

vk_session = vk_api.VkApi(token='8a3e3ab4307b96432cbdaa367f952faf3a277c0745acd334767bfb5e4b5f153cd4a27715c6f71a9366835')
URL = "http://demo14.alpha.vkhackathon.com:8000/"
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
defmessage = "Здравствуте! Политехнический музей - большой.... Не хотели бы стать волонтером?"


class User:
    def __init__(self, json):

        self.ID = json['id'] 
        self.IS_REGISTERED = checkRegistered(self.ID)
        self.KARMA = json['karma']
        self.EVENTS_REGISTERED = json['events_registered']
        self.NAME = json['vorname']
        self.SECOND_NAME = json['nachname']

    def showIvents(self):
        url = URL + "/api/v1/post/detail/"
        eventsID = str(self.EVENTS_REGISTERED.split(", "))
        events = []
        for i in eventsID:
            json = getEventByID(int(i))
            events.append(json['title'])
        if not events:
            return "Вы не зарегестрированы ни на одно мероприятие. Хотите стать волонтером?"
        return "Вы зарегестрированы на " + ','.join(events)

    def getNextIvent(self):
        url = URL + "/api/v1/post/detail/"
        data = requests.get(url)
    
        
def getAllEvents():
    url = URL + "api/v1/post/getlist"
    data = requests.get(url).json()
    result = []
    for i in data:
        result.append(i['title'])
    return "В настоящий момент планируются " + str(len(result)) + " ивента(ов): \n" + "\n".join(result)

def getEventInfo(name):
    url = URL + "api/v1/post/getlist"
    data = requests.get(url).json()
    for i in data:
        if i['title'].lower() == name:
            return i['content']

def getUserById(Id):
    url = URL + "api/v1/acc/detail/" + str(Id)
    data = requests.get(url)
    return data.json()

def getEventByID(Id):
    url = URL + "api/v1/post/detail/" + str(Id)
    data = requests.get(url)
    return data.json()
 
def checkRegistered(id):
    url = URL + "api/v1/acc/getlist/"
    data = requests.get(url).json()
    for i in data:
        if (i['urlVK'] == id):
            return True
        return False

def sendMessage(message, id):
    vk.messages.send( #Отправляем сообщение
                    user_id = id,
                    random_id = random.randint(100,1000000),
                    message = message, 
		        )   


def messagesHendler():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            if checkRegistered(event.user_id):
                user = User(getUserById(event.user_id))
                if event.text.lower() == "помоги" or event.text.lower() == "help" or event.text.lower() == "помощь":
                    sendMessage("Вы можете использовать команды :\n Покажи мои мероприятия, Покажи карму, Расскажи о 'Название мероприятия' мероприятии \n" +
                                "Напомни мне о моём следующем мероприятии, Зарегистрируй меня на 'Название мероприятия' ",  user.ID)
                if "расскажи о" in event.text.lower():
                    strlen = len("расскажи о")
                    sendMessage(getEventInfo(event.text.lower()[strlen:]), user.ID)
                if "покажи карму" in event.text.lower():
                    sendMessage(user.KARMA, user.ID)
                
                    

            else:
                if event.text.lower() == "помоги" or event.text.lower() == "help" or event.text.lower() == "помощь":
                    sendMessage("Для полноценного использования бота необходимо зарегестрироваться в сервисе http://demo14.alpha.vkhackathon.com:8000/accounts/register/  ", event.user_id)
                if event.text.lower() == "привет" or event.text.lower() == "здравствуй":
                    sendMessage(defmessage, event.user_id)
                if event.text.lower() == "xочу стать волонтером" or event.text.lower() == "xочу стать волонтёром":
                    sendMessage("Зарегистрируйтесь http://demo14.alpha.vkhackathon.com:8000/accounts/register/ ", event.user_id)
                if "расскажи о" in event.text.lower():
                    strlen = len("расскажи о")
                    sendMessage(getEventInfo(event.text.lower()[strlen:].strip()), event.user_id) 
                if "покажи мероприятия" in event.text.lower():
                    sendMessage(getAllEvents(), event.user_id)


        

messagesHendler()




#    #Слушаем longpoll, если пришло сообщение то:			
#         if event.text == 'Привет' or event.text == 'привет': #Если написали заданную фразу
#             if event.from_user: #Если написали в ЛС
#                 if checkRegistered(event.user_id):
#                     mes = "UR registered"
#                 else:
#                     mes = "UR not registered" + str(event.user_id)
                
            
#         if event.text == "Покажи мои ивенты":
#             if event.from_user:
#                 user = User(getUserById(event.user_id))
#                 vk.messages.send( #Отправляем сообщение
#                     user_id=event.user_id,
#                     random_id = random.randint(100,1000000),
#                     message = user.showIvents, 
#                 )