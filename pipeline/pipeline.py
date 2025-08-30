from src.vector_store import VectorStore
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self, persist_directory: str="./chroma_db"):
        try:
            logger.info("Initializing AnimeRecommendationPipeline...")
            vector_builder = VectorStore(processed_csv="", persist_directory=persist_directory)
            retriever = vector_builder.load_vector_store().as_retriever()
            self.recommender = AnimeRecommender(retriever=retriever, api_key=GROQ_API_KEY, model_name=MODEL_NAME)
            logger.info("AnimeRecommendationPipeline initialized successfully.")
        except Exception as e:
            logger.error(f"Error initializing AnimeRecommendationPipeline: {e}")
            raise CustomException("Error during pipeline initialization", e)
    
    def recommend(self, query: str):
        try:
            logger.info(f"Generating recommendations for query: {query}")
            recommendations = self.recommender.get_recommendations(query)
            logger.info("Recommendations generated successfully.")
            return recommendations
        except Exception as e:
            logger.error(f"Error generating recommendations: {e}")
            raise CustomException("Error during recommendation generation", e)