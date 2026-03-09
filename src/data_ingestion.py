import pandas as pd
import numpy as np
from typing import Union
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataIngestion:
    """
    Data Ingestion module for loading data from various sources
    """
    
    def __init__(self, source_path: str):
        """
        Initialize the DataIngestion class
        
        Args:
            source_path (str): Path to the data source
        """
        self.source_path = source_path
        self.data = None
    
    def load_csv(self) -> pd.DataFrame:
        """Load data from CSV file"""
        try:
            self.data = pd.read_csv(self.source_path)
            logger.info(f"Data loaded successfully from {self.source_path}")
            logger.info(f"Shape: {self.data.shape}")
            return self.data
        except Exception as e:
            logger.error(f"Error loading CSV: {str(e)}")
            raise
    
    def load_json(self) -> pd.DataFrame:
        """Load data from JSON file"""
        try:
            self.data = pd.read_json(self.source_path)
            logger.info(f"Data loaded successfully from {self.source_path}")
            return self.data
        except Exception as e:
            logger.error(f"Error loading JSON: {str(e)}")
            raise
    
    def load_parquet(self) -> pd.DataFrame:
        """Load data from Parquet file"""
        try:
            self.data = pd.read_parquet(self.source_path)
            logger.info(f"Data loaded successfully from {self.source_path}")
            return self.data
        except Exception as e:
            logger.error(f"Error loading Parquet: {str(e)}")
            raise
    
    def get_data_info(self) -> dict:
        """Get information about the loaded data"""
        if self.data is None:
            logger.warning("No data loaded yet")
            return {}
        
        return {
            "shape": self.data.shape,
            "columns": self.data.columns.tolist(),
            "dtypes": self.data.dtypes.to_dict(),
            "missing_values": self.data.isnull().sum().to_dict()
        }
    
    def get_data(self) -> pd.DataFrame:
        """Return the loaded data"""
        return self.data
