######################################################################################################################
#            **************  Importing modules    ***************                                                    #
######################################################################################################################
import json
import jsonpath
import pytest
import requests

'''
API - post method :POST requests are used to send data to the API server and create or update a resource.
Since POST requests modify data, it's important to have API tests for all of your POST methods.
 
'''


#######################################################################################################################
#     ******************* Starting of the  program **********************                                                    #
######################################################################################################################
# posting data from config file to Api
# using marker to execute particular test function

@pytest.mark.post
@pytest.mark.httpmethods
def test_post(post_exec):
    data = post_exec
    api_post = data['post']['endpoint']
    print(api_post)

    f = open("post.json", "r")

    request_json = json.loads(f.read())
    post_response = requests.post(api_post, request_json)
    id = jsonpath.jsonpath(post_response.json(), "id")
    # printing zero index value
    print(id[0])
    print(post_response)
    # printing datas which are posted in the api
    print(post_response.json())
    return post_response.json()
    assert post_response.json ==201

########################################################################################################################
#           ************  End of the program **************************                                                #
########################################################################################################################
