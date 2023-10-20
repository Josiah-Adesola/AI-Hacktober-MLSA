import streamlit as st

jamb_score = st.number_input('What was your Jamb score')
# st.write('Your jamb score was ', jamb_score)

maths = st.selectbox(
    'What was your WAEC grade in Maths?',
    ('A', 'B', 'C', 'D', 'E', 'F'))

english = st.selectbox(
    'What was your WAEC grade in English?',
    ('A', 'B', 'C', 'D', 'E', 'F'))

st.write('Your jamb score was ', jamb_score)
st.write('Your Maths WAEC grade was ', maths)
st.write('Your English WAEC grade was ', english)