import openai
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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

# Images URLs indexes assigned to three different variables
image_url1 = response['data'][0]['url']
image_url2 = response['data'][1]['url']
image_url3 = response['data'][2]['url']

# Function to show an image in a separate window
def show_image(url):
    img = mpimg.imread(url)
    imgplot = plt.imshow(img)
    plt.show()

# Show each image in a separate window
show_image(image_url1)
show_image(image_url2)
show_image(image_url3)