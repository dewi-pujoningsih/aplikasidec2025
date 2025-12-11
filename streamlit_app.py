import streamlit as st

st.title("Projek LPK Kelas Nanoteknologi Pangan 2025")
st.title("===Penentuan bilangan ganjil atau genap===")
number = int(st.number_input("Masukkan sembarang angka:"))
if number%2==1:
 st.write("Angka",number,"tergolong angka ganjil")
else:
 st.write("Angka",number,"tergolong angka genap")
