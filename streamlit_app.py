import streamlit as st

st.title("H1 Test App")
st.write("This is a test app for authorized security research.")

if "my_secret" in st.secrets:
    st.write(f"Secret loaded: {len(st.secrets['my_secret'])} chars")
else:
    st.write("No secrets configured.")
