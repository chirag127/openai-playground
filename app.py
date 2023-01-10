import random
import streamlit as st

# Make a streamlet app.Which is an alternative to the.Open AI playground.With all the options like opening I playground.
st.title("Open AI Playground")
# make a dropdown menu for the company, companies are all, openai , cohere and etc
company = st.selectbox(
    "Select a company",
    [
        "All",
        "OpenAI",
        "Cohere",
        "Hugging Face",
        "Google",
        "Facebook",
        "Microsoft",
        "IBM",
        "Salesforce",
        "Amazon",
        "Apple",
        "Baidu",
        "Bloomberg",
        "DeepMind",
        "Databricks",
        "D-Wave",
        "Intel",
        "Nvidia",
        "Qualcomm",
        "SAP",
        "SAS",
        "Seldon",
        "Tencent",
        "Uber",
        "Yandex",
        "Yelp",
        "Zillow",
        "Zymergen",
    ],
)
# make a input box taking keys
openai_keys = st.text_input("enter your key")
keys = openai_keys.split(",")
keys = [key.strip() for key in keys]
prompt = st.text_input("enter your prompt")
model = st.selectbox(
    "Select a model",
    [
        "text-davinci-003",
        "text-curie-001",
        "text-babbage-001",
        "text-ada-001",
        "code-davinci-002",

    ],
)
temperature = st.slider("temperature", 0.0, 1.0, 0.7)

max_length = st.slider("max_length", 0, 8000, 256)


stop_sequence = st.text_input("stop_sequence")

top_p = st.slider("top_p", 0.0, 1.0, 1.0)

frequency_penalty = st.slider("frequency_penalty", 0.0, 1.0, 0.0)

presence_penalty = st.slider("presence_penalty", 0.0, 1.0, 0.0)
best_of = st.slider("best_of", 0, 1, 1)
inject_start_text = st.text_input("inject_start_text")


import openai


# make a button
if st.button("Generate"):

    openai.api_key = random.choice(keys)
    response = openai.Completion.create(
        prompt=prompt, model=model, temperature=temperature, max_length=max_length, stop=stop_sequence, top_p=top_p, frequency_penalty=frequency_penalty, presence_penalty=presence_penalty, best_of=best_of, inject=inject_start_text
    )

    st.write(response)
