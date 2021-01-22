import streamlit as st

with st.beta_form('Validate'):
    checkbox = st.checkbox(label='Select to indicate validation and hit Validate')

st.markdown('---')

if checkbox:
    st.header('This is valid scale')
    st.slider(label='Enter the valid value', min_value=0, max_value=100)
else:
    st.header('This is invalid scale')
    st.slider(label='Enter the invalid value', min_value=200, max_value=300)