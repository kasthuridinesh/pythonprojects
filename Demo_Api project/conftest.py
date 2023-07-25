##################################################################################################################
# **************************** Importing all modules **********************                                       #
##################################################################################################################
import pytest
import yaml


########################################################################################################################
#         ****************   Start of the program **************                                                       #
########################################################################################################################
# ******** Fixture for post execution ********  #
@pytest.fixture(scope='session')
def post_exec():
    with open("API_endpoint.yaml", "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    yield data
    print("quit")


#  ************ Fixture for get execution ************** #
@pytest.fixture(scope='session')
def get_exec():
    with open("API_endpoint.yaml", "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    yield data
    print("quit")


#    ********** Fixture for put Execution *********** #
@pytest.fixture(scope='session')
def put_exec():
    with open("API_endpoint.yaml", "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    yield data
    print("quit")


#  ******** Fixture for delete execution ********** #
@pytest.fixture(scope='session')
def delete_exec():
    with open("API_endpoint.yaml", "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    yield data
    print("quit")

########################################################################################################################
#           ****************** End of the program **************************                                           #
########################################################################################################################
