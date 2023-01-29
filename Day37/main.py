import requests as req, os
from dotenv import load_dotenv
from datetime import datetime as dt
load_dotenv()

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
PIXELA_API_KEY = os.getenv('DAY37_PIXELA_API_KEY')
USERNAME = 'johnsuico'

# Ex 37-1 Create a new account
user_params = {
    'token': PIXELA_API_KEY,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = req.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)


# Ex 37-2 Create a new graph
GRAPH_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'

graph_config = {
    'id': 'graph1',
    'name': 'Code Graph',
    'unit': 'Commit',
    'type': 'int',
    'color': 'sora'
}

headers = {
    'X-USER-TOKEN': PIXELA_API_KEY
}

# res = req.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(res.text)

# Ex 37-3 Post a pixel
PIXEL_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1'

today_date = dt.now()

pixel_config = {
    'date': today_date.strftime('%Y%m%d'),
    'quantity': '3'
}

# res = req.post(url=PIXEL_ENDPOINT, json=pixel_config, headers=headers)
# print(res.text)

# Ex 37-4 PUT and DELETE requests
PUT_PIXEL_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/20230129'

put_config = {
    'quantity': '10'
}

# res = req.put(url=PUT_PIXEL_ENDPOINT, json=put_config, headers=headers)
# print(res.text)

DELETE_PIXEL_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/20230129'

res = req.delete(url=DELETE_PIXEL_ENDPOINT, headers=headers)
print(res.text)