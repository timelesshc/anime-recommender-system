from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStore
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()
logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting the build pipeline...")

        # Load and process data
        data_loader = AnimeDataLoader(
            original_csv="data/anime_with_sypnopsis.csv",
            processed_csv="data/processed_anime.csv"
        )
        processed_csv = data_loader.load_and_process()
        logger.info(f"Data loaded and processed. Processed file: {processed_csv}")

        # Create vector store
        vector_store = VectorStore(processed_csv=processed_csv)
        vector_store.create_vector_store()
        logger.info("Vector store created successfully.")

        logger.info("Build pipeline completed successfully.")
    except Exception as e:
        logger.error(f"Error in build pipeline: {e}")
        raise CustomException("Error during build pipeline execution", e)
    
if __name__ == "__main__":
    main()