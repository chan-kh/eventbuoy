import json 
import requests
from datetime import datetime
import streamlit as st
from config import *

def post(api_url, data):
    response = requests.post(api_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    status_code = response.status_code
    if str(status_code).startswith('2'):
        print("Data sent successfully to the API! %s ", api_url)
        # print("Response: %s ", response.content)
        try:
            return json.loads(response.content)
        except:
            return response.content

    else:
        print('Error sending data to the API \n %s : \n %s ', api_url,response.content)
        return None

def get(api_url):
    response = requests.get(api_url)
    response_content = response.content
    status_code = response.status_code
    if str(status_code).startswith('2'):
        # print('Received data:', response_content)
        try:
            return json.loads(response_content)
        except:
            return response_content
    else:
        print('Error receiving data from the API:', response.status_code)
        return None
    

def get_suggested_questions(webbot_id,conversation_id):
    api_url = "{0}/questionanswer?webbot_id={1}&conversation_id={2}&active=false".format(base_url, webbot_id, conversation_id)
    response = get(api_url)
    questions = []
    if response:
        if isinstance(response, list) and len(response) > 0:
            for item in response:
                questions.append(item['question'])
    return questions




def list_conversations(webbot_id):
    """ Returns all of the Conversations """
    api_url = "{0}/conversation?webbot_id={1}".format(base_url, webbot_id)
    response = get(api_url)
    return response


def create_conversation(webbot_id, name="default", x_fields=None):
    """ Creates a Conversation """
    api_url = "{0}/conversation".format(base_url)
    data = {"webbot_id": webbot_id, "name": name}
    response = post(api_url, data)
    return response


def get_conversation(conversation_id, x_fields=None):
    """ Returns a Conversation """
    api_url = "{0}/conversation/{1}".format(base_url, conversation_id)
    response = get(api_url)
    return response

def create_question_answer(webbot_id, conversation_id, question, model_name, instruction_id, x_fields=None):
    """ Creates a QuestionAnswer """
    print("conversation_id: %s" % conversation_id)
    print("webbot_id: %s" % webbot_id)
    print("Creating a QuestionAnswer for question %s" % question)
    api_url = "{0}/questionanswer".format(base_url)
    data = {"webbot_id" : webbot_id, "conversation_id": conversation_id, "question": question, "model_name": model_name, "instruction_id": instruction_id}
    response = post(api_url, data)
    print("Asnwer: %s" % response.get('answer'))
    return response


def update_rating_api(webbot_id, question_answer_id, rating, x_fields=None):
    """ Updates a QuestionAnswer's rating """
    api_url = "{0}/questionanswer/{1}".format(base_url, question_answer_id)
    data = {"rating": int(rating), "webbot_id": int(webbot_id)}
    response = requests.put(api_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    if response.status_code == 200:
        print("Rating updated successfully!")
    else:
        print('Error updating rating:', response.status_code)
    return response.content


def generate_questions(webbot_id,context_id):
    """ Generates questions for a file """
    api_url = "{0}/questions/generate".format(base_url)
    data = {"webbot_id": webbot_id, "context_id": context_id}
    response = post(api_url, data)
    return None

def get_question_answer_conversation():
    """ Get a QuestionAnswer Ratings for Insights """
    api_url = "{0}/questionanswer?webbot_id={1}".format(base_url, st.session_state['webbot_id'])
    response = get(api_url)
    return response

def get_backup_suggestions():
    response = get_question_answer_conversation()
    response = response[0]
    suggested_questions = response.get('suggested_questions', [])
    # st.write(suggested_questions)
    return suggested_questions

def get_backup_more_suggestions():
    response = get_question_answer_conversation()
    if len(response) > 0:
        response = response[0]
        more_questions = response.get('more_questions', [])
        # st.write(more_questions)
        return more_questions
    else: 
        return []

def post(api_url, data):
    response = requests.post(api_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    status_code = response.status_code
    if str(status_code).startswith('2'):
        print("Data sent successfully to the API! %s ", api_url)
        # print("Response: %s ", response.content)
        try:
            return json.loads(response.content)
        except:
            return response.content

    else:
        print('Error sending data to the API \n %s : \n %s ', api_url,response.content)
        return None

def get(api_url):
    response = requests.get(api_url)
    response_content = response.content
    status_code = response.status_code
    if str(status_code).startswith('2'):
        # print('Received data:', response_content)
        try:
            return json.loads(response_content)
        except:
            return response_content
    else:
        print('Error receiving data from the API:', response.status_code)
        return None
    
def update_text_prompts():
    st.session_state['completion1']= {"assistant_message" : "Please generate an Instruction above"}
    st.session_state['completion2']= {"assistant_message" : "Please generate an Instruction above"}
    st.session_state['retrieval'] = "Please generate an Instruction above"
    st.session_state['groundTruth'] = "Please generate an Instruction above"
    return True

def update_state_template_submission():
    print("Show up in the func")
    st.session_state['template_submitted'] = True
    return st.session_state['template_submitted']

def get_file_meta(file_id):
    api_url = base_url + "files/" + str(file_id)
    response = get(api_url)
    return response
