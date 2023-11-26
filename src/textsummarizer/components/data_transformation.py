import os
import urllib.request as request
import zipfile
from textsummarizer.logging import logger
from src.textsummarizer.utils.common import get_size
from pathlib import Path
from src.textsummarizer.constants import *
from src.textsummarizer.utils.common import read_yaml,create_directories
from src.textsummarizer.entity import (DataTransformationConfig)
from transformers import AutoTokenizer
from textsummarizer.logging import logger
from datasets import load_dataset,load_from_disk

class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config
        self.tokeniser = AutoTokenizer.from_pretrained(self.config.tokeniser_name)

    def convert_examples_to_features(self,example_batch):
        input_encodings = self.tokeniser(example_batch['dialogue'] , max_length = 1024, truncation = True )
        
        with self.tokeniser.as_target_tokenizer():
            target_encodings = self.tokeniser(example_batch['summary'], max_length = 128, truncation = True )
            
        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    

    def convert(self):
        dataset_samsum = load_from_disk(self.config.data_path)
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched = True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset"))    


