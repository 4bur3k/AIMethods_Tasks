from json import load
from mimetypes import init
import numpy as np
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

np.random.seed(42)
torch.manual_seed(42)


def load_tokenizer_and_model(model_name_or_path):
  return GPT2Tokenizer.from_pretrained(model_name_or_path), GPT2LMHeadModel.from_pretrained(model_name_or_path).cuda()


def generate(
    model, tok, text,
    do_sample=True, max_length=120, repetition_penalty=5.0,
    top_k=5, top_p=0.95, temperature=1,
    num_beams=None,
    no_repeat_ngram_size=3
    ):
  input_ids = tok.encode(text, return_tensors="pt").cuda()
  out = model.generate(
      input_ids.cuda(),
      max_length=max_length,
      repetition_penalty=repetition_penalty,
      do_sample=do_sample,
      top_k=top_k, top_p=top_p, temperature=temperature,
      num_beams=num_beams, no_repeat_ngram_size=no_repeat_ngram_size
      )
  return list(map(tok.decode, out))


tok, model = load_tokenizer_and_model("sberbank-ai/rugpt3small_based_on_gpt2")


def init_model(model_name):
  if model_name == 'Small':
    tok, model = load_tokenizer_and_model("sberbank-ai/rugpt3small_based_on_gpt2")
  else :
    tok, model = load_tokenizer_and_model("sberbank-ai/rugpt3medium_based_on_gpt2")
  
  return [tok, model]


def generate_button_cklick():
    print('Genrating... ', model_name, max_words)
    generated = generate(model, tok, text, max_length=max_words)
    return generated[0]
    



import streamlit as st

output_string = ''

st.title('ruGPT-3 generator')

col1, col2 = st.columns([2, 3])

with col1:
    st.subheader('Params')
    text = st.text_input('Print any phrase')
    model_name = st.radio('Choose the model', ('Small', 'Medium'))

    tok, model = init_model(model_name)

    max_words  = st.slider('Max words number', min_value= 10, max_value= 120, value=40)
    if st.button('Generate'):
      output_string = generate_button_cklick()

    
 
with col2:
    st.subheader('Resoult')
    st.text_area(label='Generated text', value=output_string, height=300)
