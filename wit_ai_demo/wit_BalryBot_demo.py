from wit import Wit

#Util
def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val
def send(request, response):
    print(response['text'])

#detectFoodType
def detect_food_type(request):
    context = request['context']
    entities = request['entities']

    food = first_entity_value(entities, 'food')
    if food == 'pizza':
        context['foodType'] = 'junk food'
    elif food == 'sandwich':
        context['foodType'] = 'snacks'
    elif food == 'cake' or food == 'brownie':
        context['foodType'] = 'desserts'
    elif food == 'burrito' or food == 'burritos' or food == 'taco' or food == 'tacos':
        context['foodType'] = 'Mexican food'
    elif food == 'orange chicken':
        context['foodType'] = 'Chinese food'
    return context

#getLastLogin
def get_last_login(request):
    context = request['context']
    entities = request['entities']

    user = first_entity_value(entities, 'contact')
    if user:
        context['lastLogTime'] = 'about an hour ago (user: ' + user + ')'
        if context.get('missingContact') is not None:
            del context['missingContact']
    else:
        context['missingContact'] = True
        if context.get('lastLogTime') is not None:
            del context['lastLogTime']

    return context

#getForcast
def get_forecast(request):
    context = request['context']
    entities = request['entities']

    loc = first_entity_value(entities, 'location')
    if loc:
        context['forecast'] = 'sunny in ' + loc
        if context.get('missingLocation') is not None:
            del context['missingLocation']
    else:
        context['missingLocation'] = True
        if context.get('forecast') is not None:
            del context['forecast']

    return context

actions = {
    'send': send,
    'getForecast': get_forecast,
    'getLastLogin': get_last_login,
    'detectFoodType': detect_food_type,
}

client = Wit(access_token='7VTHUKNFULKFVBZ53M5DO2Z2VFGS3AYJ', actions=actions)
client.interactive()