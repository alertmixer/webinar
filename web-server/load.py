import requests

from requests.exceptions import HTTPError

while True:
    for url in ['http://webserver:8000/loaded_view']:
        try:
            response = requests.get(url)

            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print('HTTP error occurred:' + str(http_err))
        except Exception as err:
            print('Other error occurred:' + str(err))
        else:
            print('Success!')
