from Text_Summarizer.config.configurations import ConfigurationManager
from Text_Summarizer.components.data_validation import DataValidation
from Text_Summarizer.logging import logger

class DataValidationPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.check_validation_status()
