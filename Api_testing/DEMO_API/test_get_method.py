#######################################################################################################################
#                           Importing library                                                                         #
######################################################################################################################

import pytest
import requests

'''
Api- http-get method : The GET method is used to retrieve data from a server at the specified resource.
 For example, say you have an API with a /users endpoint.
  Making a GET request to that endpoint should return a list of all available users.
'''


######################################################################################################################
#                           Starting  of the program                                                                #
######################################################################################################################

# Getting data from api
# Using marker function to execute particular tests function
@pytest.mark.get
@pytest.mark.httpmethods
def test_get(get_exec):
    api_get = 'https://jsonplaceholder.typicode.com/todos/1'
    # data = get_exec
    # api_get = data['get']['endpoint']
    # # logging.info(api_get)

    get_response = requests.get(api_get)
    print("Checking the response")
    print(get_response)
    # <Response [200]
    # logging.info(get_response.status_code)
    print(get_response.status_code)
    # logging.info(get_response.text)
    print(get_response.text)
    # logging.info(get_response.url)
    print(get_response.url)
    # logging.info(get_response.headers['Content-Type'])
    print((get_response.headers['Content-Type']))
    # logging.info(get_response.content)
    print(get_response.content)
    # logging.info(get_response.json())
    print(get_response.json())
    # logging.info(type(get_response.json()))
    print(get_response.json())
    assert get_response.status_code == 200

########################################################################################################################
#       ******************** End of the program ****************************                                           #
########################################################################################################################
