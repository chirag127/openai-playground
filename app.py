import streamlit as st
import openai
import cohere


st.title("Text Generation")
# Create a sidebar
st.sidebar.title("Options")

# Company dropdown menu
companies = ["OpenAI","Cohere"]
company = st.sidebar.selectbox("Select the company", companies)

# API key input
api_key = st.sidebar.text_input("Enter the API key")
openai.api_key = api_key

# Prompt input
prompt = st.text_area("Enter the prompt", height=200)

if company == "Cohere":
    models = ["xlarge"]
elif company == "OpenAI":
    models = ["code-davinci-002", "code-cushman-001","text-davinci-003", "text-curie-001", "text-babbage-001", "text-ada-001"]

model = st.sidebar.selectbox("Select the model", models)

# Temperature slider
temperature = st.sidebar.slider("Temperature", min_value=0.00, max_value=1.00, step=0.01, value=0.00)

# Max length slider
max_length = st.sidebar.slider("Max Length", min_value=1, max_value=8000, step=50, value=250)

# Stop sequence input
stop_sequence = st.sidebar.text_input("Enter the stop sequence", value="")

if stop_sequence == "":
    stop_sequence = None


# Top P slider
top_p = st.sidebar.slider("Top P", min_value=0.00, max_value=1.00, step=0.01, value=0.00)

# Frequency penalty slider
frequency_penalty = st.sidebar.slider("Frequency Penalty", min_value=0.00, max_value=1.00, step=0.01, value=0.00)

# Presence penalty slider
presence_penalty = st.sidebar.slider("Presence Penalty", min_value=0.00, max_value=1.00, step=0.01, value=0.00)


# Generate button
button = st.button("Generate")
#         import cohere
# co = cohere.Client('{apiKey}')
# response = co.generate(
#   model='',
#   prompt='{prompt}',
#   max_tokens=50,
#   temperature=0.9,
#   k=0,
#   p=0.75,
#   frequency_penalty=0,
#   presence_penalty=0,
#   stop_sequences=[],
#   return_likelihoods='NONE')
# print('Prediction: {}'.format(response.generations[0].text))
if button:

    if company == "Cohere":
        client = cohere.Client(api_key)
        response = client.generate(
            model=model,
            prompt=prompt,
            max_tokens=max_length,
            temperature=temperature,
            k=0,
            p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop_sequences=stop_sequence,
        )
        result = response.generations[0].text



    elif company == "OpenAI":

        completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_length,
        stop=stop_sequence,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
    )
        result = completions.choices[0].text

    st.code(result)
