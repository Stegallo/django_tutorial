import requests
import json
from datetime import datetime, timedelta
import time
my_domain = $my_domain
username = $username
token = $token

def main():
    """
        main body
    """

    url = 'https://www.pythonanywhere.com/api/v0/user/{username}/schedule/'.format(
        username=username
    )

    response = requests.get(
        url,
        headers={'Authorization': 'Token {token}'.format(token=token)}
    )

    try:
        id = json.loads(response.text)[0]['id']

        url = 'https://www.pythonanywhere.com/api/v0/user/{username}/schedule/{id}/'.format(
            username=username,
            id=id
        )

        response = requests.delete(
            url,
            headers={'Authorization': 'Token {token}'.format(token=token)}
        )
    except Exception as ex:
        print(ex)

    schedule_time = datetime.now() + timedelta(minutes=2)

    url = 'https://www.pythonanywhere.com/api/v0/user/{username}/schedule/'.format(
        username=username
    )
    params = {
        'command': 'sh /home/DjangoTutorialStegallo/deploy.sh',
        'enabled': True,
        'interval': 'daily',
        'hour': schedule_time.hour,
        'minute': schedule_time.minute
    }

    response = requests.post(
        url,
        params,
        headers={'Authorization': 'Token {token}'.format(token=token)}
    )

if __name__ == '__main__':
    main()
