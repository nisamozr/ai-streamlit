import streamlit as st
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

st.set_page_config(
    page_title="Research API",
    page_icon="📰",
)

st.title("Research API")

st.markdown("### Auth")
st.markdown(
    """
    Currently, we have google OAuth setup on our frontend.\n
    However, some of these APIs are created to require only user_id as query parameter or in request body. This is to ease testing and integration.\n
    Once these APIs are finalized, we can decide on how to proceed with authentication and begin implementing it.
    """
)
st.info("💡 These are some user ids for testing: ")
st.code(
    """
    442da8cd-7ac5-44ef-8aed-6ed7f31d99b3
    """
)
st.code(
    """
    b2b0bb76-8617-48b3-9229-0064818a3a46
    """
)


# pg = st.navigation(
#     {
#         "Conversations": [
#             st.Page("conversations.py"),
#         ],
#         "Chat completions": [
#             st.Page("document.py"),
#             st.Page("report.py"),
#             st.Page("research.py"),
#         ],
#     }
# )

# pg.run()
