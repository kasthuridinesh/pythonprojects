##################################################################################################################
# ****************************Importing all modules **********************                                       #
##################################################################################################################
import json
import pytest
import requests

'''
API - Put method :The HTTP PUT request method is used to create a new resource or
 overwrite a representation of the target resource.
'''


########################################################################################################################
#         ****************   Start of the program **************                                                       #
########################################################################################################################

#  performing the put function to overwrite or update data in the API
# Using the marker function to execute a particular test function

@pytest.mark.put
@pytest.mark.httpmethods
def test_put(put_exec):
    data = put_exec
    api_put = data['put']['endpoint']
    print(api_put)

    update_json = open("put.json", "r")
    request_json = json.loads(update_json.read())
    print("*********************Put****************")

    put_response = requests.put(api_put, request_json)
    print(put_response.json())

    # Expected result =  {'userId': 1, 'title': 'Wash car', 'completed': True, 'id': 10}
    print(put_response.status_code)
    assert put_response.status_code == 200

########################################################################################################################
#        &&&&&&&&&&&&&&&&&&&& End of the program &&&&&&&&&&&&&&&&&&&&&&&&&&                                            #
########################################################################################################################
