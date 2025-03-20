import streamlit as st
from Bundesliga.bundesliga import bundesliga
from EPL.epl import epl
from LaLiga.laliga import laliga
from SerieA.seriea import seriea
from home import home_page

def main():
    st.set_page_config(
        page_title='Прогноз исходов футбольных матчей', 
        page_icon='⚽', 
        layout='centered', 
        initial_sidebar_state='auto'
    )
    
    # Скрываем меню и кнопку Deploy и добавляем стили
    custom_styles = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
            /* Настройка темы через CSS */
            .stApp {
                background-color: #333333;
                color: #FFFFFF;
            }
            .css-1d391kg, .css-12oz5g7 {
                background-color: #252525;
            }
            
            /* Дополнительные стили для кастомизации интерфейса */
            .stButton>button {
                background-color: #FF5733;
                color: white;
                border-radius: 5px;
                padding: 0.5rem 1rem;
                font-weight: bold;
            }
            .stButton>button:hover {
                background-color: #0d47a1;
            }
            .stTextInput>div>div>input {
                border-color: #FF5733;
            }
            </style>
            """
    st.markdown(custom_styles, unsafe_allow_html=True)

    st.sidebar.header("Выберите лигу")
    selected_page = st.sidebar.radio("Выбрать", ["Главная", "Bundesliga","EPL","La Liga", "Serie A"])

    if selected_page == "Главная":
        home_page()
    elif selected_page == "Bundesliga":
        bundesliga()
    elif selected_page=="EPL":
        epl()
    elif selected_page=="La Liga":
        laliga()
    elif selected_page=="Serie A":
        seriea()

        
if __name__ == "__main__":
    main()


