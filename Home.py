import streamlit as st
import os
import configparser

st.set_page_config(
    page_title="OCI FSDR Plan Steps Export/Update",
    page_icon="☁️"  # Cloud emoji to represent OCI
)

def load_oci_profiles():
    config_path = os.path.expanduser("~/.oci/config")
    if not os.path.exists(config_path):
        return []
    
    config = configparser.ConfigParser()
    config.read(config_path)
    return config.sections()

def main():
    st.title("OCI FSDR Plan Steps Export/Update")
    st.write("Welcome to the OCI FSDR Plan Steps Export/Update tool.")
    
    profiles = load_oci_profiles()
    if profiles:
        selected_profile = st.selectbox("Select OCI Authentication Profile", profiles)
        st.session_state['oci_profile'] = selected_profile
    else:
        st.error("No OCI profiles found in ~/.oci/config. Please ensure you have valid OCI configuration.")
        return

    st.write("Please use the sidebar to navigate between Export and Update functionalities.")

if __name__ == "__main__":
    main()
