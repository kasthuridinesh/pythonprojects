#######################################################################################################################
#    ********************* Importing modules ***************************                                              #
#######################################################################################################################

import pytest
import requests

'''
API - Delete method: HTTP DELETE request is used to delete an existing record in the data source in the REST ful 
architecture.
 '''


########################################################################################################################
#       ***************** Start of the program ****************************                                            #
########################################################################################################################
# deleting tasks from the API
# Using the marker function to execute a particular test function
@pytest.mark.delete
@pytest.mark.httpmethods
def test_delete(delete_exec):
    data = delete_exec
    api_delete = data['delete']['endpoint']
    print(api_delete)
    delete_response = requests.delete(api_delete)
    print(delete_response.json())
    print(delete_response.status_code)
    assert delete_response.status_code == 200
########################################################################################################################
#                   ************* End of the program **********************                                            #
########################################################################################################################
