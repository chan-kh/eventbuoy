import streamlit as st 


def show_style():
    st.set_page_config(
    page_title="Eventbuoy Maigrate")
    
    hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
    st.markdown(hide_menu_style, unsafe_allow_html=True)
    
    # # st.markdown(
    # f'''
    #     <style>
    #         .sidebar .sidebar-content {{
    #             width: 10px;
    #         }}
    #     </style>
    # ''',
    # unsafe_allow_html=True
    # )