from browser import ajax, document
import json

URL = '/v1/ajax/concatenate/names'


def on_complete(req):

    if req.status == 200 or req.status == 0:
        data = req.json
        document['result'].html = 'Bem vindo <b>' + \
            data['first_name'] + '</b><b> ' + data['last_name'] + '</b>'
    else:
        print(req.text)


def sendDataByGet(event):
    data = {
        'first_name': document['firstName'].value,
        'last_name': document['lastName'].value,
    }
    ajax.get(
        url=URL,
        mode='text',
        encoding='utf-8',
        timeout=10,
        data=data,
        oncomplete=on_complete
    )


def sendDataByPost(event):
    data = {
        'first_name': document['firstName'].value,
        'last_name': document['lastName'].value,
    }
    ajax.post(
        URL,
        headers={"Content-Type": "application/json; charset=utf-8"},
        data=json.dumps(data),
        oncomplete=on_complete
    )


button_get = document['buttonGet']
button_get.bind('click', sendDataByGet)
button_post = document['buttonPost']
button_post.bind('click', sendDataByPost)
