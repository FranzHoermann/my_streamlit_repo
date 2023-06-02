import datetime
import streamlit as st

d = st.date_input(
    "When\'s your birthday",
    datetime.date(2019, 7, 6),min_value = datetime.date(1960,1,1))
st.write('Your birthday is:', d)

