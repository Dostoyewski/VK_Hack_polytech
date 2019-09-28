import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import datetime 
import urllib.request


vk_session = vk_api.VkApi(token='8a3e3ab4307b96432cbdaa367f952faf3a277c0745acd334767bfb5e4b5f153cd4a27715c6f71a9366835')
URL = "http://demo14.alpha.vkhackathon.com:8000/"
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
defmessage = "Здравствуте! Политехнический музей - большой.... Не хотели бы стать волонтером?"


def generateBarcode(code):
    url = "https://barcode.tec-it.com/barcode.ashx?data=" + code + "&code=Code128&dpi=96&dataseparator="
    img = urllib.request.urlopen(url).read()
    out = open(code + ".jpg", "wb")
    out.write(img)
    out.close


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

    return 'Мероприятие не найдено('

def getUserById(id):
    url = URL + "api/v1/acc/getlist"
    data = requests.get(url).json()
    for i in data:
        if str(id) in i['urlVK']:
            return i

def getEventByID(Id):
    url = URL + "api/v1/post/detail/" + str(Id)
    data = requests.get(url)
    return data.json()
 
def getKarmaByID(id):
    data = getUserById(id)
    return data['karma']

def getMyEvents(id):
    data = getUserById(id)['events_registered']
    data = data.split(',')
    data.pop()
    now = datetime.date.today()

    def unpack(s:str):
        s = s.split('-')
        s = map(int, s)
        t = datetime.date(*s)
        delta = t - now
        return delta.days


    events = []
    for i in data:
        events.append((getEventByID(int(i))['title'], getEventByID(int(i))['beginning_at'][:10]))
    
    e = []
    for i in events:
        if unpack(i[1]) >= 0:
            e.append(i[0])
            

    if e == []:
        return 'Ничего'


    e = '\n '.join(e)
    return e

def getNextEvent(id):
    data = getUserById(id)['events_registered']
    data = data.split(',')
    data.pop()

    now = datetime.date.today()

    c = []
    for i in data:
        c.append((getEventByID(i)['title'], getEventByID(i)['beginning_at'][:10]))

    c1 = c[:]

    def unpack(s:str):
        s = s.split('-')
        s = map(int, s)
        t = datetime.date(*s)
        delta = t - now
        return delta.days

    def min_pos(c):
        if c == []:
            return 'Пусто'
        min = 100000000
        j = 0
        for i in range(len(c)):
            if c[i][1] >= 0 and c[i][1] < min:
                min = c[i][1]
                j = i
        return c[j][0] + ' ' + str(c1[j][1])

    a = []

    for i in c:
        a.append((i[0], unpack(i[1])))

    return min_pos(a)


def checkRegistered(id):
    url = URL + "api/v1/acc/getlist/"
    data = requests.get(url).json()
    for i in data:
        if str(id) in i['urlVK']:
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
                user = event.user_id

                if event.text.lower() == "помоги" or event.text.lower() == "help" or event.text.lower() == "помощь":
                    sendMessage("Вы можете использовать команды :\n Покажи мои мероприятия\n Покажи карму\n Расскажи о 'Название мероприятия'\n Покажи все мероприятия\n Покажи следующее мероприятие",  user)
                
                elif "привет" in event.text.lower():
                    sendMessage('Привет!', user)
                    sendMessage("Вы можете использовать команды :\n Покажи мои мероприятия\n Покажи карму\n Расскажи о 'Название мероприятия'\n Покажи все мероприятия\n Покажи следующее мероприятие",  user)

                elif "расскажи о" in event.text.lower():
                    strlen = len("расскажи о ")
                    sendMessage(getEventInfo(event.text.lower()[strlen:]), user)

                elif "покажи карму" in event.text.lower():
                    sendMessage(getKarmaByID(user), user)
                
                elif "покажи мои мероприятия" in event.text.lower():
                    sendMessage(getMyEvents(user), user)
                
                elif "покажи все мероприятия" in event.text.lower():
                    sendMessage(getAllEvents(), user)

                elif "покажи следующее мероприятие" in event.text.lower():
                    sendMessage(getNextEvent(user), user)

                else:
                    sendMessage('Я тебя не понял', user)
                    sendMessage("Вы можете использовать команды :\n Покажи мои мероприятия\n Покажи карму\n Расскажи о 'Название мероприятия'\n Покажи все мероприятия\n Покажи следующее мероприятие",  user)
                    

            else:

                if event.text.lower() == "помоги" or event.text.lower() == "help" or event.text.lower() == "помощь":
                    sendMessage("Для полноценного использования бота необходимо зарегестрироваться в сервисе http://demo14.alpha.vkhackathon.com:8000/accounts/register/  ", event.user_id)

                elif event.text.lower() == "привет" or event.text.lower() == "здравствуй":
                    sendMessage(defmessage, event.user_id)
                    sendMessage("Зарегистрируйтесь http://demo14.alpha.vkhackathon.com:8000/accounts/register/ ", event.user_id)

                elif event.text.lower() == "xочу стать волонтером" or event.text.lower() == "xочу стать волонтёром":
                    sendMessage("Зарегистрируйтесь http://demo14.alpha.vkhackathon.com:8000/accounts/register/ ", event.user_id)

                else:
                    sendMessage('Я тебя не понял', event.user_id)
                    sendMessage("Вы можете использовать команды :\n Помощь ",  event.user_id)

        

messagesHendler()
