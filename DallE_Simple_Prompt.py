import openai

openai.api_key="Your API_KEY"

response = openai.Image.create(
  prompt="a dog smoking a cigar in a poker room.",
  n=1,
  size="256x256"
)

image_url = response['data'][0]['url']
print(image_url)