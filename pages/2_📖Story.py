import streamlit as st
from transformers import pipeline, set_seed
import json
import random
import logging

st.set_page_config(page_title="Story", page_icon="open_book")

generator = pipeline('text-generation', model='gpt2')

with open('prompt.json') as json_file:
    promt_data = json.load(json_file)

def get_promt(key):
    logging.info('get promt for %s',key)
    if key == 'locations':
        return random.choice(promt_data[key])["name"]
    else:
        return random.choice(promt_data[key])["description"]



def select_templates():
    logging.info('get promt template')
    return "Once upon a time, in <location>, there lived a <char_prop> <char_job> named <char_name>."

def generate_story(story_promt):
    try:
        logging.info('generate story with prompt')
        generated_text = generator(story_promt, max_length=50, num_return_sequences=1)
        return generated_text[0]['generated_text'].rsplit('.', 1)[0]
    except:
        logging.error('fail generate story with prompt')
        return story_promt


char_name = st.text_input('Character Name', 'Cinderella')

generate = st.button('Generate')

story_text = 'Once upon a time ......'
if generate:
    story_prompt = select_templates()
    story_prompt = story_prompt.replace("<location>",get_promt("locations"))
    story_prompt = story_prompt.replace("<char_prop>",get_promt("properties"))
    story_prompt = story_prompt.replace("<char_job>",get_promt("jobs"))
    story_prompt = story_prompt.replace("<char_name>",char_name)
    logging.info('Done getting prompt %s',story_prompt)
    story_text = generate_story(story_prompt)+"."


story = st.text_area('Your Story', story_text)
