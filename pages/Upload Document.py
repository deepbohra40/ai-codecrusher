import os
import time

import streamlit as st
from azure.storage.blob import BlobServiceClient

import azurecognitive_search_AzureOpenAI_Test

st.set_page_config(page_title="ESG Survey Automation", page_icon=":robot:")

st.header("AI-CodeCrusher$ : ESG Survey Automation")



if 'clicked' not in st.session_state:
    st.session_state.clicked = False

if "file_uploader_key" not in st.session_state:
    st.session_state["file_uploader_key"] = 0

if "uploaded_files" not in st.session_state:
    st.session_state["uploaded_files"] = []

def click_button():
    st.session_state.clicked = True

def clear_button():
    st.session_state["file_uploader_key"] += 1
    #st.rerun()


if st.session_state.clicked:
    with st.spinner(text="Embedding in progress..."):
        azurecognitive_search_AzureOpenAI_Test.vector_stores()
    st.success("Completed!")
    st.session_state.clicked = False


st.subheader("Upload Documents:")
if not st.session_state.clicked:
    #upload_files=st.file_uploader("Choose a file", accept_multiple_files=True)
    upload_files = st.file_uploader(
        "",
        accept_multiple_files=True,
        key=st.session_state["file_uploader_key"],
    )
    blob_service_client = BlobServiceClient.from_connection_string(os.environ.get("AZURE_CONN_STRING"))
    for uploaded_file in upload_files:
        bytes_data= uploaded_file.read()
        blob_client = blob_service_client.get_blob_client(
            container=os.environ.get("CONTAINER_NAME"), blob=uploaded_file.name
        )
        try:
            response = blob_client.upload_blob(bytes_data)
            st.info(f"Data uploaded Successfully - Filename {uploaded_file.name}")
        except Exception as err:
            if str(err).find("BlobAlreadyExists") != -1:
                errorText = "Error - Uploaded file name '" + uploaded_file.name + "' already exists - "
                st.error(errorText)

if upload_files:
    st.session_state["uploaded_files"] = upload_files


st.button('Clear Uploads', on_click=clear_button)

st.subheader("Embed Document:")

st.markdown("_(Please click 'Clear Uploads' before running Embedding)_")


st.button('Run Embedding', on_click=click_button)



