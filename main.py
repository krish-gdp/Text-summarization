from textsummarizer.logging import logger

from src.textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textsummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>stage{STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>stage {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)
    raise(e)
