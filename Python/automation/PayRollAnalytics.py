from PayRollUtilities.DataGenerator import DataGenerator
from PayRollUtilities.DataLoader import DataLoader

def generate_csvs():
    # Generate All
    data_generator = DataGenerator()
    data_generator.generate_all()

def load_tables():
    #Load tables and Data Quality Metrics
    DataLoading=DataLoader()
    summary_df=DataLoading.data_loading()
    return summary_df

def dqm_loading():
    summary_df=load_tables()
    DataLoading=DataLoader()
    DataLoading.data_quality_metrics_loading(summary_df)
    print("Loaded Data Quality Metrics")

if __name__ == "__main__":
    generate_csvs()
    dqm_loading()
