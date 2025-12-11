import streamlit as st

st.title("Projek LPK Kelas Nanoteknologi Pangan 2025")
st.title("===Penentuan bilangan ganjil atau genap===")
number = st.number_input(
    "Masukkan angka dengan 0 desimal",
    min_value=0,
    max_value=10000,
    format="%.0f"
)


#number = int(st.number_input("Masukkan sembarang angka:"))
if number%2==1:
 st.write("Angka",number,"tergolong angka ganjil")
else:
 st.write("Angka",number,"tergolong angka genap")
