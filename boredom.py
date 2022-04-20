import requests


def get_request(input):
    input = {'value': input}
    "Call a random activity for 'anything' input"
    if input['value'] == 'anything':
        request_value = "https://www.boredapi.com/api/activity"
    else:
        request_value = "https://www.boredapi.com/api/activity?type={}".format(input['value'])
    "Get web response to query"
    response = requests.get(request_value)
    "Store the web response in dict format"
    answer = response.json()
    more_participants = 'You can do this with somebody.'
    possible_cost = 'This activity might imply costs.'
    activity = answer['activity']
    if answer['participants'] == 1:
        activity = activity + '. '
    else:
        activity = activity + '. ' + more_participants
    if answer['price'] == 0:
        activity = activity
    else:
        activity = activity + ' ' + possible_cost
    return activity
