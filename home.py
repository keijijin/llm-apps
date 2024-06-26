import streamlit as st
import streamlit_authenticator as stauth
import yaml

def init_auth():
    config_str = st.secrets['config']['CREDENTIALS']

    config = yaml.safe_load(config_str)

    credentials = {
        "usernames": {
            key: {
                "email": value['email'],
                "name": value['name'],
                "password": value['password']
            }
            for key, value in config['usernames'].items()
        }
    }

    authenticator = stauth.Authenticate(
        credentials,
        st.secrets["cookie"]["name"],
        st.secrets["cookie"]["key"],
        st.secrets["cookie"]["expiry_days"],
        st.secrets["preauthorized"]
    )

    return authenticator

def login_proc(authenticator: stauth.Authenticate):
    # ログイン処理
    # authenticator.login()
    fields = {
        "Form name": "ログイン",
        "Login": 'ログイン',
        "Username": "ユーザ名",
        "Password": "パスワード"
    }
    name, authentication_status, username = authenticator.login(location='main', fields=fields)

    if st.session_state["authentication_status"]:
        # authenticator.logout()
        authenticator.logout(button_name='ログアウト', location='main')
        st.write(f'Enjoy *{st.session_state["name"]}*')
        
        from apps import agent, function_calling, qa, recipe, simple_chat, sql, tagging

        app_options = ["agent", "function_calling", "qa", "recipe", "simple_chat", "sql", "tagging"]
        selected_app = st.sidebar.selectbox("Select an app", app_options)

        if selected_app == "agent":
            agent.app()
        elif selected_app == "function_calling":
            function_calling.app()
        elif selected_app == "qa":
            qa.app()
        elif selected_app == "recipe":
            recipe.app()
        elif selected_app == "simple_chat":
            simple_chat.app()
        elif selected_app == "sql":
            sql.app()
        elif selected_app == "tagging":
            tagging.app()

        # if st.sidebar.button("ログアウト"):
        #     authenticator.logout('main')
        #     st.session_state['authentication_status'] = None
        #     st.experimental_rerun()
        

    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')

if __name__ == "__main__":
    auth = init_auth()
    login_proc(auth)