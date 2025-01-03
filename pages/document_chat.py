import json
import requests
import streamlit as st


if "is_file_uploaded" not in st.session_state:
    st.session_state["is_file_uploaded"] = False

st.title("Document Querying")
st.info("💡 If you do not have a user_id, you may use this for testing:")
st.code("b2b0bb76-8617-48b3-9229-0064818a3a46")

# """
# UPLOAD PDF
# """
st.markdown("## Upload PDF")
st.markdown("`POST /api/v1/files/upload`")
pdf_file = st.file_uploader("Choose PDF file", type="pdf")
user_id = st.text_input(
    label="Enter User ID*", key="user_id_1", help="REQUIRED to associate file with user"
)
conversation_id = st.text_input(
    label="Enter Conversation ID (OPTIONAL)",
    key="convo_id",
    help="Enter a new UUID4 to create a new conversation with the id",
)
if st.button("Upload Your File", disabled=(not pdf_file)):
    file = pdf_file

    res = requests.post(
        f"{st.secrets['base_url']}/api/v1/files/upload",
        files={"file": file},
        data={"user": user_id},
    )

    st.subheader("Response from API:")
    st.json(res.text)
    print(res.status_code, res.json())
    if res.status_code == 200:
        st.session_state.is_file_uploaded = True
        conversation_id = res.json()["conversation_id"]


# """
# Query Document
# """
st.markdown("## Query Document")
st.markdown("`POST /api/v1/chat/completions`")

user_id = st.text_input(
    label="Enter User ID*",
    value=user_id,
    key="user_id_2",
    help="REQUIRED to locate associated pdf file",
)
conversation_id = st.text_input(
    label="Enter Conversation ID*",
    value=conversation_id,
    key="convo_id2",
    help="REQUIRED to locate associated pdf file",
)
user_query = st.text_area(label="Query the document")
is_stream = st.checkbox(label="Stream output")

request_body = {
    "type": "document",
    "messages": [{"role": "user", "content": user_query}],
    "stream": is_stream,
    "user": user_id,
    "conversation_id": conversation_id,
}


st.subheader("Request Body: ")
st.json(request_body)

st.divider()
if st.button("Chat", icon="🤖"):
    res = requests.post(
        f"{st.secrets['base_url']}/api/v1/chat/completions/",
        data=json.dumps(request_body),
    )

    if not is_stream:
        st.subheader("Response from API: ")
        st.json(res.text)
    else:
        st.subheader("Streamed response from API: ")
        st.markdown(res.text)
