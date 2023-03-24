import streamlit as st
import openai



def generate_proposal(prompt: str, temperature: int = 0.5, top_p:int = 0.5, max_tokens:int = 1000) -> str:
        """
        Generates text based on the given prompt using the default OpenAI model (text-davinci-002)
        and temperature (0.5).
        
        Args:
            prompt (str): The prompt to use for generating the text.
        
        Returns:
            str: The generated text.
        """
        # Create the completion call using the OpenAI API
        completion_dict = openai.Completion.create(
            prompt=prompt,
            model="text-davinci-003",
            temperature=temperature,
            max_tokens= max_tokens,
            top_p = top_p
        )


        # Extract and return the generated text from the completion call response
        generated_text = completion_dict['choices'][0]['text'].strip()
        return generated_text


st.title('Welcome to The Upwork Proposal Generator!')


api_key = st.text_input('What is your OpenAI API key?')

openai.api_key = api_key

temperature = st.slider('Temperature:',min_value=float(0),max_value=float(1),step=0.05,value=float(1))

top_p = st.slider('Top_p:',min_value=float(0),max_value=float(1), step=0.05,value=float(0.15))


greeting = st.text_input('What is the name of the client?')

project_scope = st.text_input('What is the client looking for?')

introduction = st.text_input('Who are you and why should I trust you?')

step_by_step = st.text_input('How will you tackle this problem?')

relevant_portfolio = st.text_input('Describe your relevant portfolio for this job.')

communication = st.text_input("What is your communication plan?")

budget = st.text_input("What is you budget for this job?")

conclusion = st.text_input("Conclusion")

cta = st.selectbox('Select your CTA:',
                   ('Feel Free to send a message',
                    'Looking forward to hearing from you',
                    'Happy to answer any questions you may have',
                    'Would love to hear more about the project')
)   


user_prompt = f'''
Please create a upwork proposal for me, here's the relevant information about this project surrounded by brackets

[The name of the client is {greeting}.
He is looking for {project_scope}.
I believe I am the right person for this job because {introduction}. 
{relevant_portfolio}
I would tackle this problem by {step_by_step}
During the job, I plan on communicating with you via {communication}
My budget for this job is {budget}.
All in all, {conclusion}
{cta}]

Now that you have all of the relevant information,please craft the entire proposal for me with a empathetic, casual but formal tone:
'''

isClicked = st.button("Generate Proposal",key='generate_proposal_button',type='primary')
if isClicked:
        # Use st.spinner() to display a spinner while the email copy is being generated
        with st.spinner('Generating email copy...'):
            proposal = generate_proposal(user_prompt, temperature, top_p)
        
        # Display the generated email copy once it's ready
        st.success('Email copy generated successfully:')
        st.text_area('Proposal:', proposal, height = 200)
        isClicked = False

