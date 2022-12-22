import requests
from settings import base_url, name, pet_id, headers, image, files


"""Add a new pet"""

body = {'name': name, 'pet_id': pet_id, 'status':'available'}

res_post_new_pet = requests.post(f'{base_url}/pet', data=body, headers={'accept': 'application/json'})
print('POST /pet   Add a new pet')
print('  Статус запроса:', res_post_new_pet.status_code)
print('  Ответ сервера body:', res_post_new_pet.json(), '\n')


"""Find pet by ID"""

res_find_id = requests.get(f'{base_url}/pet/{pet_id}', headers=headers)

print('GET /pet/{pet_id}   Add a new pet')
print('  Статус запроса:', res_find_id.status_code)
print('  Ответ сервера body:', res_find_id.json(), '\n')

"""Finds pets by status"""

status='available'

res_status = requests.get(f'{base_url}/pet/findByStatus?status={status}', headers=headers)

print('GET /pet/findByStatus?status={status}  Finds pets by status')
print('  Статус запроса:',res_status.status_code)
print('  Ответ сервера body:', res_status.json(), '\n')


"""Updates a pet in the store with form data"""

body2 = {'name': 'Richi', 'pet_id': pet_id, 'status':'available'}

res_post_form_data = requests.post(f'{base_url}/pet', data=body2, headers=headers)

print('post /pet   Updates a pet in the store with form data')
print('  Статус запроса:', res_post_form_data.status_code)
print('  Ответ сервера body:', res_post_form_data.json(), '\n')



"""Uploads an image"""

res_image = requests.post(f'{base_url}/pet/{pet_id}/uploadImage', headers=headers, files=files)
print('POST /pet/{petId}/uploadImage  Uploads an image')
print('  Статус запроса:', res_image.status_code)
print('  Ответ сервера body:', res_image.json(), '\n')


"""Update an existing pet"""

body3= {'name': 'Hermann fon Bismark', 'pet_id': pet_id, 'status':'available'}
res_update = requests.put(f'{base_url}/pet', data=body3, headers=headers)

print('PUT /pet  Update an existing pet')
print('  Статус запроса:', res_update.status_code)
print('  Ответ сервера body:', res_update.json(), '\n')

"""Deletes a pet"""


res_delete = requests.delete(f'{base_url}/pet/{pet_id}')

print('DELETE /pet/{pet_id}  Deletes a pet')
print(f'Удалили питомца под номером - {pet_id}')
print('  Статус запроса:', res_delete.status_code)



