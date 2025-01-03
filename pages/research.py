import json

import requests
import streamlit as st

st.title("Research Generation API")
st.info("💡 If you do not have a user_id, you may use this for testing:")
st.code("b2b0bb76-8617-48b3-9229-0064818a3a46")
# """
# Generate Research
# """
st.markdown("## Generate Research")
st.markdown("`POST /api/v1/chat/completions`")

# Info
st.markdown(
    """
        This endpoint generates a comprehensive research based on the user query. 
        Our agent searches through multiple research papers and articles to provide in-depth information.

        Due to its comprehensive nature, the process is very time intensive. Thus, it is not feasible to provide the research as a response to this endpoint. 
        We provide a conversation id, which can be used later view the research generated. 
        Endpoint can be used to chat with the agent normally once research is generated.

        To get an instant response on the user query, use our report endpoint which generates a succint, but equally informative answer.
        """
)


user_id = st.text_input(
    label="Enter User ID*",
    help="To save conversation in db and associate with user",
    key="user_id_2",
)
conversation_id = st.text_input(
    label="Enter Conversation ID [Optional]",
    help="Use this to query existing research",
    key="convo_id2",
)
user_query = st.text_area(label="Suitable topic for generating research")
is_stream = st.checkbox(label="Stream output")

request_body = {
    "type": "research",
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
    try:
        res = requests.post(
            f"{st.secrets['base_url']}/api/v1/chat/completions/",
            data=json.dumps(request_body),
            timeout=12 * 60,  # 10 mins
            verify=False,
        )
        st.subheader("Response from API: ")
        st.json(res.text)

    except Exception as e:
        print("Something went wrong", e)
        st.markdown("Oops, something went wrong")
        raise
    except:
        st.markdown("Oops, something went wrong")
        raise
