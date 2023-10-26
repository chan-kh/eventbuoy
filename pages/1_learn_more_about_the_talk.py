import streamlit as st
from conversation_utils import *
from style_utils import *
show_style()

if "messages" not in st.session_state:
    st.session_state.messages = []


#Change HERE for title
# st.subheader("A Copilot for CBT Therapy💕😣👼")


st.markdown('[Build your own AI Bot](https://shorturl.at/qBUX6)')


st.caption("Disclaimer: This is an AI system. Responses may take up to 20 seconds. Please be patient. ")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])





if 'webbot_id' not in st.session_state:
    st.session_state['webbot_id'] = 272

# if 'active_conversation_id' not in st.session_state:
#     response = create_conversation(webbot_id=st.session_state['webbot_id'], name="random")

#     if response is not None:
#         st.session_state['active_conversation_id'] = response.get('id')

response = create_conversation(webbot_id=st.session_state['webbot_id'], name="random")


if response is not None:
    st.session_state['active_conversation_id'] = response.get('id')

conversation = get_conversation(conversation_id=st.session_state['active_conversation_id'])
conversation_list = [conversation]

#change HERE for the chat box
if prompt := st.chat_input("Learn more about the talk"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    

    conversation_id = st.session_state['active_conversation_id']
    with st.spinner("Please wait..."):
        #Change here for the instruction id
        response = create_question_answer(webbot_id=st.session_state['webbot_id'], conversation_id=conversation_id, question=prompt, model_name="gpt-3.5-turbo", instruction_id = 17144)
    conversation_id = st.session_state['active_conversation_id']
    conversation = get_conversation(conversation_id=conversation_id)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        question_answer = conversation['questionanswers'][0]
        full_response = question_answer.get("answer")
        full_response = full_response.replace("Assistant: ", "", 1)
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

#change HERE for sidebar

# st.sidebar.subheader("A Copilot for CBT Therapy💕😣👼")

# st.sidebar.divider()
# st.sidebar.markdown('[Build your own AI Bot](https://shorturl.at/qBUX6)')

# st.sidebar.divider()
# st.sidebar.write("Disclaimer:")
# st.sidebar.write("This is an AI system.")
# st.sidebar.write("Responses may take up to 20 seconds. Please be patient.")
