
import logging

from src.clean_data import clean_data
from src.validate import validate_data
from src.load import load_data

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def run_pipeline():
    logger.info("Pipeline started")

    try:
        clean_df, rejected_df = clean_data()

        validate_data(clean_df)
        load_data()

        logger.info(
            "Pipeline completed: %s clean, %s rejected",
            len(clean_df),
            len(rejected_df),
        )

        print("Pipeline completed successfully.")

    except Exception:
        logger.exception("Pipeline failed")
        raise


if __name__ == "__main__":
    run_pipeline()
