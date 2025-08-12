# Blog Generator Using OpenAI

# Importing OpenAI
import openai

# Importing ENV file for hiding the OpenAI API key used for connecting to OpenAI
from dotenv import dotenv_values
config = dotenv_values(".env")

# Connecting API key to OpenAI for authorisation
openai.api_key = config['API_KEY']

# Defining a blog generator function with paragraph topic as the parameter. Completions.create helps to generate response from AI. Model specifies the open AI model. Prompt provides the promt. Max Tokens provides the number of words that needs to be generated and temperature is the randomness of response given for 2 prompts.
def generate_blog(paragraph_topic):
  response = openai.completions.create(
    model = 'gpt-3.5-turbo-instruct',
    prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
    max_tokens = 400,
    temperature = 0.3
  )
  
#   Storing theresponse text from AI in a variable called retrieve_blog and returning it at the end of the function.
  retrieve_blog = response.choices[0].text
  return retrieve_blog

# For writing multiple paragraphs, using the while loop by creating a variable which is kept true first and taking input from User whether or not to continue and if yes, then what should be the topic on which paragraph needs to be generated
keep_writing = True

while keep_writing:
  answer = input('Write a paragraph? Y for yes, anything else for no. ')
  if (answer == 'Y'):
    paragraph_topic = input('What should this paragraph talk about? ')
    print(generate_blog(paragraph_topic))
  else:
    keep_writing = False