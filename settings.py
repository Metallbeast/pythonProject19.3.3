base_url = 'https://petstore.swagger.io/v2/pet'
name = 'Richard'
pet_id = '12345'
headers = {'accept': 'application/json'}
image = 'Cat.jpg'
files = {'file': (image, open(image, 'rb'), 'image/jpeg')}