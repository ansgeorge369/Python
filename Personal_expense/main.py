import pandas as pd  #for csv file which acts as database
import csv
from datetime import datetime

class CSV:
    CSV_FILE = "Finance_Data.csv"     #class variable
    COLUMNS = ["date", "amount", "category", "description"]
    
    #initialize csv. create one csv if not created if created initialize
    
    @classmethod  #decorator so that initialize_csv has access to class but not to instance
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)     #try to read if csv file if present
        except FileNotFoundError: 
            df = pd.DataFrame(columns=cls.COLUMNS)   #pandas data frame format of csv
            df.to_csv(cls.CSV_FILE, index=False)       #convert to csv
            
    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date" : date,
            "amount" : amount,
            "category" : category,
            "description" : description             #store in a python dictonary
        }
        
        with open(cls.CSV_FILE, "a", newline="") as csvfile:      #open a new csv file
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            
            
CSV.initialize_csv()