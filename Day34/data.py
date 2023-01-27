import requests as req

question_quote_req = req.get(url='https://opentdb.com/api.php?amount=10&type=boolean')
question_quote_req.raise_for_status()
question_data = question_quote_req.json()['results']