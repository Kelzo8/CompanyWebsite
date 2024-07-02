import streamlit as st
import pandas

st.set_page_config()

st.title('Company Website')
st.write("""gsjkadsaghkfskjdfgsdhksdfhdsaghafjadfjlas
gbsajkdbas.bsbdfjk.sbcfgasdjkadsbjk""")

st.subheader("Our Team")

col1, empty, col2, empty2, col3 = st.columns([1.4, 0.5, 1.5, 0.5, 1.5])

df = pandas.read_csv("data (1).csv")
with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images (1)/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images (1)/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images (1)/" + row["image"])



