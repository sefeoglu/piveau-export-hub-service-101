import requests

def get_datasets(base_url, service_name):
    """ get the list of dataset ids from piveau hub service
    Args:
        base_url (str): the base url of the piveau hub service (e.g. http://localhost:8082)
        service_name (str): the service name (e.g. datasets)
    Returns: 
        response_json (dict): the json response from the service
    """
    #send request to endpoint
    base_url = base_url + "/" + service_name
    
    response = requests.get(base_url)
    
    response_json = response.json()

    return response_json

def get_dataset(base_url, service_name, dataset_id):
    """ get the dataset from piveau hub service
    Args:
        base_url (str): the base url of the piveau hub service (e.g. http://localhost:8082)
        service_name (str): the service name (e.g. datasets)
        dataset_id (str): the id of the dataset
    Returns: 
        response_json (dict): the json response from the service
    """
    #send request to endpoint
    
    base_url = base_url + "/" + service_name + "/" + dataset_id
    response = requests.get(base_url)
    
    response_json = response.json()

    return response_json