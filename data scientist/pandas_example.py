import pandas as pd
import os
import warnings
warnings.filterwarnings("ignore")
class pandas_example():
    #File name
    FILE_NAME = 'car-sales.csv'
    #Data raw
    cars =[]
    #Full file path
    FILE_PATH =""

    FILE_PATH = os.path.join(os.path.dirname(__file__),'data',FILE_NAME)    
    cars = pd.read_csv(FILE_PATH)

    #Get dataframe select columns
    df = cars[['Doors','Price']]
    #View dataframe with overview
    #df.info()
    #standardized price column 
    df.Price = df.Price.replace('[\$\,\.]','',regex = True).astype(int)
    

    print(df)    

def main():
    pandas = pandas_example()    

if __name__ =="__main__":
    main()