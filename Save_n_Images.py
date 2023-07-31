import openai
import requests

# Read the API key from the file
with open('C:/Users/AZEEM/Desktop/API.txt') as file:
    api_key = file.read().strip()

openai.api_key = api_key

response = openai.Image.create(
    prompt="a dog smoking a cigar in a poker room.",
    # n is the number of images to be generated
    n=3,
    size="256x256"
)

# Function to save an image to a file
def save_image(url, filename):
    with open(filename, 'wb') as f:
        f.write(requests.get(url).content)

# Save each image using a for loop
for i, image_data in enumerate(response['data']):
    image_url = image_data['url']
    image_filename = f'image_{i+1}.png'
    save_image(image_url, image_filename)
