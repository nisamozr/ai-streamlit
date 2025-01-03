import json

import requests
import streamlit as st

st.title("Report Generation API")
st.info("💡 If you do not have a user_id, you may use this for testing:")
st.code("b2b0bb76-8617-48b3-9229-0064818a3a46")
# """
# Generate Report
# """
st.markdown("## Generate Report")
st.markdown("`POST /api/v1/chat/completions`")

st.markdown(
    """
        This endpoint generates a concise report based on the user query. 

        To get an in-depth response to the user query, use our research endpoint which generates a comprehensive answer.
        """
)

user_id = st.text_input(
    label="Enter User ID*",
    help="To save conversation in db and associate with user",
    key="user_id_2",
)
conversation_id = st.text_input(
    label="Enter Conversation ID [Optional]",
    help="Use this to query existing report",
    key="convo_id2",
)
user_query = st.text_area(label="Suitable topic for generating report")
is_stream = st.checkbox(label="Stream output")

request_body = {
    "type": "report",
    "messages": [{"role": "user", "content": user_query}],
    "stream": is_stream,
    "user": user_id,
}

if conversation_id:
    request_body["conversation_id"] = conversation_id


st.subheader("Request Body: ")
st.json(request_body)

st.divider()
if st.button("Chat", icon="🤖", disabled=(not user_query)):
    res = requests.post(
        f"{st.secrets['base_url']}/api/v1/chat/completions/",
        data=json.dumps(request_body),
        timeout=10 * 60,  # 10 mins
        verify=False,
    )

    if not is_stream:
        st.subheader("Response from API: ")
        st.json(res.text)
    else:
        st.subheader("Streamed response from API: ")
        st.markdown(res.text)
