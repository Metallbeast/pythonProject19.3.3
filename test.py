import requests
import json

def test_add_pet():
    input_pet = {
        "id":234,
        "category":{
            "id":22,
            "name":"Anabolik "
        },
        "name":"doggie",
        "photoUrls":[
            "string"
        ],
        "tags":[
            {
                "id":12,
                "name":"dog"
            }
        ],
        "status":"available"
    }

    header = {'accept':'application/json', 'Content-Type':'application/json'}

    res_post = requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)

    print(res_post.text)
    res_json = json.loads(res_post.text)
    assert input_pet == res_json

    res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')

    assert res_get.status_code == 200
    assert json.loads(res_get.text) == input_pet

def test_delete_pet():
    input_pet = {
        "id":23487,
        "category":{
            "id":22,
            "name":"Bolik "
        },
        "name":"doggie",
        "photoUrls":[
            "string"
        ],
        "tags":[
            {
                "id":12,
                "name":"dog"
            }
        ],
        "status":"available"    }

    header = {'accept':'application/json', 'Content-Type':'application/json'}
    res_delete = requests.delete(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}', header=header)
    out_del = {
        "code":200,
        "type":"unknown",
        "message":"234"
    }
    assert json.loads(res_delete.text) == out_del

    res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')

    assert res_get.status_code == 404
    assert json.loads(res_get.text) == input_pet

def test_sold_list():
    input_pet = {
        "id":23419,
        "category":{
            "id":22,
            "name":"Anabolik "
        },
        "name":"cat",
        "photoUrls":[
            "string"
        ],
        "tags":[
            {
                "id":12,
                "name":"dog"
            }
        ],
        "status":"available"
    }

    header = {'accept':'application/json', 'Content-Type':'application/json'}

    requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)
    res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/findByStatus', params={'status':'available'})

    assert res_get.status_code == 200
    assert input_pet in list(json.loads(res_get.text))
    print(list(json.loads(res_get.text)))
