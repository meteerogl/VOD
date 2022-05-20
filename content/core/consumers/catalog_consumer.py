import requests
import json
# We can use RabbitMQ for consume catalog data

# get catalog_name_by_id
def get_catalog_name_list():
    try:
        request = requests.get('http://docker.for.mac.localhost:8001/catalog/list')
        return request.json()['data']
    except Exception as e:
        return None
'''
 2.Method
 When catalog name or smt chance in Catalog service.
 We can create update_catalog_list endpoint and 
 it triggers update_catalog_list endpoint and write on redis in this service. - (category_list)
'''
