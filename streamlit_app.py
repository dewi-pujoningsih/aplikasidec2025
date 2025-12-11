import streamlit as st
st.title(":blue[Projek LPK 2025]")
st.header(":orange[Penentuan bilangan ganjil atau genap]")
number = st.number_input("Insert a number",min_value=0, max_value=10000)
if number%2==1:
  st.write("Bilangan", number,"termasuk bilangan ganjil")
else:
  st.write("Bilangan", number,"termasuk bilangan genap")
