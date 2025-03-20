import streamlit as st
from Bundesliga.bundesliga import bundesliga
from EPL.epl import epl
from LaLiga.laliga import laliga
from SerieA.seriea import seriea
from home import home_page

def main():
    st.set_page_config(page_title='Прогноз исходов футбольных матчей', page_icon='⚽', layout='centered', initial_sidebar_state='auto')

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


