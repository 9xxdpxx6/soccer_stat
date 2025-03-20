import streamlit as st
from PIL import Image


def home_page():

    st.image("logo1.png",width=150)

    st.title("Прогноз исходов футбольных матчей ⚽")

    st.write("Это веб-приложение прогнозирует исходы футбольных матчей в ведущих европейских лигах: Bundesliga, EPL, La Liga, Serie A")

    st.info("При переходе между разными лигами, пожалуйста, обновляйте сайт для лучшей производительности")

    st.write("Выберите лигу на боковой панели, чтобы начать")

    container = st.container()

    with container:
        st.write("* Bundesliga: Немецкая футбольная лига")
        st.text("")
        st.write("* EPL: Английская Премьер-лига")
        st.text("")
        st.write("* La Liga: Испанская футбольная лига")
        st.text("")
        st.write("* Serie A: Итальянская футбольная лига")
        st.text("")

    st.info("Модель обучена на 25-летней истории результатов (1999-2024). Она делает прогнозы на основе прошлых встреч команд и их текущей формы.")

    st.success(" ")

if __name__ == "__main__":
    home_page()
