import streamlit as st
from transformers import pipeline, set_seed

generator = pipeline('text-generation', model='gpt2')

def remove_punctuation(test_str):
  result = ''.join(filter(lambda x: x.isalpha() or x.isdigit() or x.isspace(), test_str))
  return result

def select_templates():
    return "Once upon a time, in <location> <loc_desc>, there lived a <char_prop> <char_job> named <char_name>."

def generate_location():
    generated_text = generator("A location called", max_length=7, num_return_sequences=1)
    return remove_punctuation(generated_text[0]['generated_text'].split("A location called ")[1])

def generate_loc_desc():
    generated_text = generator("One word to describe a location is", max_length=11, num_return_sequences=1)
    return remove_punctuation(generated_text[0]['generated_text'].split("One word to describe a location is ")[1])

def generate_character_properties():
    generated_text = generator("One word to describe a person is", max_length=11, num_return_sequences=1)
    return remove_punctuation(generated_text[0]['generated_text'].split("One word to describe a person is ")[1])

def generate_character_job():
    generated_text = generator("A job called", max_length=7, num_return_sequences=1)
    return remove_punctuation(generated_text[0]['generated_text'].split("A job called ")[1])

def generate_story(story_promt):
    generated_text = generator(story_promt, max_length=150, num_return_sequences=1)
    return generated_text[0]['generated_text'].rsplit('.', 1)[0]

def generate_end():
    generated_text = generator("At the end of story, ", max_length=30, num_return_sequences=1)
    return generated_text[0]['generated_text'].rsplit('.', 1)[0]



char_name = st.text_input('Character Name', 'Cinderella')

generate = st.button('Generate')

story_text = 'Once upon a time ......'
if generate:
    story_prompt = select_templates()
    story_prompt = story_prompt.replace("<location>",generate_location())
    story_prompt = story_prompt.replace("<loc_desc>",generate_loc_desc())
    story_prompt = story_prompt.replace("<char_prop>",generate_character_properties())
    story_prompt = story_prompt.replace("<char_job>",generate_character_job())
    story_prompt = story_prompt.replace("<char_name>",char_name)
    story_text = generate_story(story_prompt)+". "+generate_end()



story = st.text_area('Your Story', story_text)
