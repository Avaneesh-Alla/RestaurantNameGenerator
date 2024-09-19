import streamlit as st
import langchainhelper as LCH
st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("American", "Indian", "Mexican", "Arabic", "Italian"))

if cuisine:
    response = LCH.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip(""))
    menu_items = response['menu_items'].strip("").split(" ,")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)g