import streamlit as st
import requests


st.set_page_config(page_title="Conversations API", page_icon="󰭻")

st.title("Conversations API")
st.info("💡 If you do not have a user_id, you may use this for testing:")
st.code("b2b0bb76-8617-48b3-9229-0064818a3a46")
# st.markdown("""
#             """)

# """
# GET ALL CONVOS
# """
st.markdown("## Get All Conversations")
user_id = ""
st.markdown("`GET /api/v2/conversations/{user_id}`")


def update_request_param_user_id(new_val):
    request_param_user_id = new_val


user_id = st.text_input(label="Enter User ID*", value=user_id, key="user_id_1")

if st.button("GET All Conversations", key="all_convos"):
    res = requests.get(f"{st.secrets['base_url']}/api/v2/conversations/{user_id}")

    st.subheader("Response from API:")
    st.json(res.text)


# """
# GET CONVO DETAILS
# """
st.markdown("## Get Conversation Details")
st.markdown("`GET /api/v2/conversations/c/{conversation_id}`")
convo_id = st.text_input(label="Enter Conversation ID*")
# st.text("Making get request to")
# st.code(f"/api/v2/conversations/{user_id}")
if st.button("GET Conversations details", key="convo_details"):
    res = requests.get(f"{st.secrets['base_url']}/api/v2/conversations/c/{convo_id}")

    st.subheader("Response from API:")
    st.json(res.text)


# """
# GET ALL CONVOS (COOKIE AUTH)
# """
st.markdown("## Get All Conversations (cookie based authentication)")
if st.button("GET My Conversations", key="all_convos_auth"):
    st.toast("Auth not implemented on streamlit")
    # res = requests.get(f"{st.secrets['base_url']}/api/v2/conversations/{user_id}")
    #
    # st.subheader("Response from API:")
    # st.json(res.text)

# """
# GET CONVO DETAILS (COOKIE AUTH)
# """
st.markdown("## Get Conversation Details (cookie based authentication)")
if st.button("GET Conversations details", key="convo_details_auth"):
    st.toast("Auth not implemented on streamlit")
    # res = requests.get(f"{st.secrets['base_url']}/api/v2/conversations/c/{convo_id}")
    #
    # st.subheader("Response from API:")
    # st.json(res.text)
