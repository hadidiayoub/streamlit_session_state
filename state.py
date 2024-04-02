import streamlit as st

st.title('Counter Example')
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Increment')
if increment:
    #ktwli khdam bli howa lvariable blast st.session_state.count
    st.session_state.count += 1


st.write('Count = ', st.session_state.count)


_="""st.title('Counter Example')
count = 0

increment = st.button('Increment')
if increment:
    count += 1

st.write('Count = ', count)"""



# CRUD in session state
###### Create
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

###### Reads
st.write(st.session_state.key)

###### Update
st.session_state.key = 'value2' #or st.session_state['key'] = 'value2'

###### Delete

