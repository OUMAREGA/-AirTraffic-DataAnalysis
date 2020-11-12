from util.tables import TABLES
import pandas as pd
import numpy as np
from os.path import dirname

racine = dirname(dirname(__file__))

not_null = lambda df,index: df[index].notnull()

type_rules = {
    "YEAR": lambda df,index: df[index].astype(str).str.match("^[0-9]{4}$"),
    "TIME": lambda df,index: df[index].astype(str).str.match("^(-)?[0-9]{3,4}$")
}

NUMERIC_TYPES = [ "TINYINT", "TINYINT UNSIGNED", "SMALLINT", "SMALLINT UNSIGNED", "FLOAT", "FLOAT UNSIGNED", "INT", "INT UNSIGNED", "YEAR", "TIME" ]


def parse_csv(dbConnection ,table_name: str,csv_path: str):
    df = pd.read_csv(csv_path)
    table_sql_schema = TABLES[table_name]["columns"]
    uniqueIndexes = []
    for column in table_sql_schema:
        column_name = column["name"]
        structure = column["structure"]
        column_type = structure["type"]

        if column_type in NUMERIC_TYPES:
                #pass
                if "UNSIGNED" in column_type:
                    df[column_name] = df[column_name].astype(str).str.extract("(\d+(\.\d+)?)",expand=True)
                else:
                    df[column_name] = df[column_name].astype(str).str.extract("(\d+(\-\.\d+)?)",expand=True)

        if "options" in structure:

            if "NOT NULL" in structure["options"]: 
                mask = not_null(df,column_name)
                df = df[mask]
                
            if "PRIMARY KEY" in structure["options"]:
                mask = not_null(df,column_name)
                df = df[mask]

        if column_type in type_rules:
            mask = type_rules[column_type](df,column_name)
            df = df[mask]

        if "special_rule" in structure:
            mask = df[column_name].str.contains(structure["special_rule"])
            df = df[mask]
    
        if "concat" in column:
            df[column_name] = df[column_name].astype(str) + column["concat"]
    
        if column_type == "DATETIME":
            df[column_name] = pd.to_datetime(df[column_name],errors="coerce")
        if "references" in structure:
            primary_key = structure["references"]["index"]
            primary_table = structure["references"]["table"]
            primary_df = pd.read_sql(f"SELECT {primary_key} FROM {primary_table}",dbConnection)
            #print(f"SELECT {primary_key} FROM {primary_table}")
            #print("table primaire",primary_df)
            df = df[df[column_name].astype(str).isin(primary_df[primary_key].astype(str))]
                
        if "unique" in structure:
            uniqueIndexes.append(column_name)
        #print(column_name,structure)
            
    if len(uniqueIndexes) > 0:
        df = df.drop_duplicates(subset=uniqueIndexes,keep="first")
    #print(TABLES[table_name])
    if "foreign_composite" in TABLES[table_name]:
        #print("FOREIGN COMPOSITE KEYS DETECTED !")
        keys = ",".join(TABLES[table_name]["foreign_composite"]["keys"])
        primary_table = TABLES[table_name]["foreign_composite"]["table"]
        #print(f"SELECT {keys} FROM {primary_table}")
        primary_df = pd.read_sql(f"SELECT {keys} FROM {primary_table}",dbConnection)
        df = pd.merge(primary_df.astype(str), df, how='inner')
        
    return df
    