import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Anime Recommender", page_icon=":sparkles:", initial_sidebar_state="expanded")

image_path = "https://assets-prd.ignimgs.com/2022/08/17/top25animecharacters-blogroll-1660777571580.jpg?width=1280&format=jpg&auto=webp&quality=80"
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(image_path, width=600)

# Sidebar
st.sidebar.title("About")
st.sidebar.info(
    "🔎 This app recommends anime titles based on your query.\n\n"
    "💡 Try entering an anime title like *Naruto*, or a description like *high school romance*."
)

# Main header
st.markdown(
    "<h2 style='text-align: center; color: #FF66B2;'>✨ Anime Recommender ✨</h2>",
    unsafe_allow_html=True
)
st.write("---")

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

query = st.text_input(
    "🎬 Enter an anime title or description:",
    placeholder="e.g., A story about ninjas with strong friendships..."
)
if query:
    with st.spinner("⚡ Finding the best matches..."):
        recommendations = pipeline.recommend(query)
    st.subheader("🎉 Recommended Anime:")
    st.write(recommendations)