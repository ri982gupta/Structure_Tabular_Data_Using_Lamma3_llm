# import fitz  # PyMuPDF
# import pdfplumber
# import pandas as pd
# import json

# def extract_text_from_first_page(pdf_path):
#     with pdfplumber.open(pdf_path) as pdf:
#         first_page = pdf.pages[0]
#         return first_page.extract_text()

# def extract_table_from_pdf(pdf_path):
#     with pdfplumber.open(pdf_path) as pdf:
#         first_page = pdf.pages[0]
#         table = first_page.extract_table()
#     return table

# def convert_table_to_json(table):
#     headers = table[0]  # Extract headers from the first row
#     data = table[1:]    # Extract the data
#     df = pd.DataFrame(data, columns=headers)
#     return df.to_json(orient='records')

# def main(pdf_path):
#     table = extract_table_from_pdf(pdf_path)
#     json_data = convert_table_to_json(table)
#     return json_data

# pdf_path = 'Dummy Bank Statement.pdf'
# json_output = main(pdf_path)
# print(json_output)


# [{"Date":"07\/01\/2023","Description":"Opening Balance","Withdrawals":"-","Deposits":"-","Balance":"$5,000.00"},{"Date":"07\/02\/2023","Description":"Electric Bill Payment","Withdrawals":"$250.00","Deposits":"-","Balance":"$4,750.00"},{"Date":"07\/05\/2023","Description":"Grocery Store","Withdrawals":"$150.00","Deposits":"-","Balance":"$4,600.00"},{"Date":"07\/08\/2023","Description":"Salary Deposit","Withdrawals":"-","Deposits":"$1,000.00","Balance":"$5,600.00"},{"Date":"07\/12\/2023","Description":"Online Shopping - Z-Mart","Withdrawals":"$100.00","Deposits":"-","Balance":"$5,500.00"},{"Date":"07\/15\/2023","Description":"Cash Withdrawal - ATM","Withdrawals":"$200.00","Deposits":"-","Balance":"$5,300.00"}]


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# import pdfplumber
# import pandas as pd
# import json

# def extract_table_from_pdf(pdf_path):
#     with pdfplumber.open(pdf_path) as pdf:
#         tables = []
#         for page in pdf.pages:
#             table = page.extract_table()
#             if table:
#                 tables.append(table)
#     return tables

# def clean_table_data(tables):
#     cleaned_data = []
#     for table in tables:
#         headers = table[0]
#         data = table[1:]
#         df = pd.DataFrame(data, columns=headers)
        
#         # Clean the data
#         df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        
#         # Convert to numeric where appropriate
#         df['Withdrawals'] = pd.to_numeric(df['Withdrawals'], errors='coerce')
#         df['Deposits'] = pd.to_numeric(df['Deposits'], errors='coerce')
#         df['Balance'] = pd.to_numeric(df['Balance'], errors='coerce')
        
#         cleaned_data.append(df)
    
#     # Combine all dataframes
#     combined_df = pd.concat(cleaned_data, ignore_index=True)
#     return combined_df

# def convert_table_to_json(df):
#     return df.to_json(orient='records', date_format='iso')

# def main(pdf_path):
#     tables = extract_table_from_pdf(pdf_path)
#     cleaned_data = clean_table_data(tables)
#     json_data = convert_table_to_json(cleaned_data)
#     return json_data

# pdf_path = 'Dummy Bank Statement.pdf'
# json_output = main(pdf_path)
# print(json_output)

# # Optionally, save the JSON to a file
# with open('output.json', 'w') as f:
#     f.write(json_output)


# C:\Users\RiGupta\Desktop\BANK_STMT\bnk1.py:60: FutureWarning: DataFrame.applymap has been deprecated. Use DataFrame.map instead.
#   df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
# Traceback (most recent call last):
#   File "C:\Users\RiGupta\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\indexes\base.py", line 3791, in get_loc
#     return self._engine.get_loc(casted_key)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "index.pyx", line 152, in pandas._libs.index.IndexEngine.get_loc      
#   File "index.pyx", line 181, in pandas._libs.index.IndexEngine.get_loc
#   File "pandas\_libs\hashtable_class_helper.pxi", line 7080, in pandas._libs.hashtable.PyObjectHashTable.get_item
#   File "pandas\_libs\hashtable_class_helper.pxi", line 7088, in pandas._libs.hashtable.PyObjectHashTable.get_item
# KeyError: 'Withdrawals'

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "C:\Users\RiGupta\Desktop\BANK_STMT\bnk1.py", line 83, in <module>    
#     json_output = main(pdf_path)
#                   ^^^^^^^^^^^^^^
#   File "C:\Users\RiGupta\Desktop\BANK_STMT\bnk1.py", line 78, in main        
#     cleaned_data = clean_table_data(tables)
#                    ^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\RiGupta\Desktop\BANK_STMT\bnk1.py", line 63, in clean_table_data
#     df['Withdrawals'] = pd.to_numeric(df['Withdrawals'], errors='coerce')
#                                       ~~^^^^^^^^^^^^^^^
#   File "C:\Users\RiGupta\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\frame.py", line 3893, in __getitem__
#     indexer = self.columns.get_loc(key)
#               ^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\RiGupta\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\indexes\base.py", line 3798, in get_loc
#     raise KeyError(key) from err
# KeyError: 'Withdrawals'


#-----------------------------------------------------------------------------------------------------------------------------


# import pdfplumber
# import pandas as pd
# import json

# def extract_table_from_pdf(pdf_path):
#     with pdfplumber.open(pdf_path) as pdf:
#         tables = []
#         for page in pdf.pages:
#             table = page.extract_table()
#             if table:
#                 tables.append(table)
#     return tables

# def clean_table_data(tables):
#     cleaned_data = []
#     for table in tables:
#         headers = table[0]
#         data = table[1:]
#         df = pd.DataFrame(data, columns=headers)
        
#         # Clean the data
#         df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        
#         # Check for the existence of each column before converting to numeric
#         if 'Withdrawals' in df.columns:
#             df['Withdrawals'] = pd.to_numeric(df['Withdrawals'], errors='coerce')
#         if 'Deposits' in df.columns:
#             df['Deposits'] = pd.to_numeric(df['Deposits'], errors='coerce')
#         if 'Balance' in df.columns:
#             df['Balance'] = pd.to_numeric(df['Balance'], errors='coerce')
        
#         cleaned_data.append(df)
    
#     # Combine all dataframes
#     combined_df = pd.concat(cleaned_data, ignore_index=True)
#     return combined_df

# def convert_table_to_json(df):
#     return df.to_json(orient='records', date_format='iso')

# def main(pdf_path):
#     tables = extract_table_from_pdf(pdf_path)
#     cleaned_data = clean_table_data(tables)
#     json_data = convert_table_to_json(cleaned_data)
#     return json_data

# pdf_path = 'Dummy Bank Statement.pdf'
# json_output = main(pdf_path)
# print(json_output)

# # Optionally, save the JSON to a file
# with open('output.json', 'w') as f:
#     f.write(json_output)



# [{"Date":"07\/01\/2023","Description":"Opening Balance","Withdrawals":null,"Deposits":null,"Balance":null,"07\/18\/2023":null,"Car Insurance Premium":null,"$350.00":null,"-":null,"$4,950.00":null},{"Date":"07\/02\/2023","Description":"Electric Bill Payment","Withdrawals":null,"Deposits":null,"Balance":null,"07\/18\/2023":null,"Car Insurance Premium":null,"$350.00":null,"-":null,"$4,950.00":null},{"Date":"07\/05\/2023","Description":"Grocery Store","Withdrawals":null,"Deposits":null,"Balance":null,"07\/18\/2023":null,"Car Insurance Premium":null,"$350.00":null,"-":null,"$4,950.00":null},{"Date":"07\/08\/2023","Description":"Salary Deposit","Withdrawals":null,"Deposits":null,"Balance":null,"07\/18\/2023":null,"Car Insurance Premium":null,"$350.00":null,"-":null,"$4,950.00":null},{"Date":"07\/12\/2023","Description":"Online Shopping - Z-Mart","Withdrawals":null,"Deposits":null,"Balance":null,"07\/18\/2023":null,"Car Insurance Premium":null,"$350.00":null,"-":null,"$4,950.00":null},{"Date":"07\/15\/2023","Description":"Cash Withdrawal - ATM","Withdrawals":null,"Deposits":null,"Balance":null,"07\/18\/2023":null,"Car Insurance Premium":null,"$350.00":null,"-":null,"$4,950.00":null},{"Date":null,"Description":null,"Withdrawals":null,"Deposits":null,"Balance":null,"07\/18\/2023":"07\/22\/2023","Car Insurance Premium":"Coffee Shop","$350.00":"$20.00","-":"-","$4,950.00":"$4,930.00"},{"Date":null,"Description":null,"Withdrawals":null,"Deposits":null,"Balance":null,"07\/18\/2023":"07\/25\/2023","Car Insurance Premium":"Gas Station","$350.00":"$50.00","-":"-","$4,950.00":"$4,880.00"},{"Date":null,"Description":null,"Withdrawals":null,"Deposits":null,"Balance":null,"07\/18\/2023":"07\/28\/2023","Car Insurance Premium":"Water Bill Payment","$350.00":"$300.00","-":"-","$4,950.00":"$4,580.00"},{"Date":null,"Description":null,"Withdrawals":null,"Deposits":null,"Balance":null,"07\/18\/2023":"07\/30\/2023","Car Insurance Premium":"Gym Membership Fee","$350.00":"$80.00","-":"-","$4,950.00":"$4,500.00"},{"Date":null,"Description":null,"Withdrawals":null,"Deposits":null,"Balance":null,"07\/18\/2023":"07\/31\/2023","Car Insurance Premium":"Movie Streaming Service\nSubscription","$350.00":"$50.00","-":"-","$4,950.00":"$4,450.00"},{"Date":null,"Description":null,"Withdrawals":null,"Deposits":null,"Balance":null,"07\/18\/2023":"07\/31\/2023","Car Insurance Premium":"Monthly Maintenance Fee","$350.00":"$200.00","-":"-","$4,950.00":"$4,250.00"}]   


#-----------------------------------------------------------------------------------------------------------------------------


# import pdfplumber
# import pandas as pd
# import json

# def extract_table_from_pdf(pdf_path):
#     with pdfplumber.open(pdf_path) as pdf:
#         tables = []
#         for page in pdf.pages:
#             table = page.extract_table()
#             if table:
#                 tables.append(table)
#     return tables

# def clean_table_data(tables):
#     cleaned_data = []
#     for table in tables:
#         headers = table[0]
#         data = table[1:]
        
#         # Ensure the headers match the expected structure
#         expected_headers = ["Date", "Description", "Withdrawals", "Deposits", "Balance"]
#         if len(headers) > len(expected_headers):
#             headers = headers[:len(expected_headers)]
        
#         df = pd.DataFrame(data, columns=headers)
        
#         # Clean the data
#         df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        
#         # Only keep the expected columns
#         df = df[expected_headers]
        
#         # Convert to numeric where appropriate
#         df['Withdrawals'] = pd.to_numeric(df['Withdrawals'], errors='coerce')
#         df['Deposits'] = pd.to_numeric(df['Deposits'], errors='coerce')
#         df['Balance'] = pd.to_numeric(df['Balance'], errors='coerce')
        
#         cleaned_data.append(df)
    
#     # Combine all dataframes
#     combined_df = pd.concat(cleaned_data, ignore_index=True)
#     return combined_df

# def convert_table_to_json(df):
#     return df.to_json(orient='records', date_format='iso')

# def main(pdf_path):
#     tables = extract_table_from_pdf(pdf_path)
#     cleaned_data = clean_table_data(tables)
#     json_data = convert_table_to_json(cleaned_data)
#     return json_data

# pdf_path = 'Dummy Bank Statement.pdf'
# json_output = main(pdf_path)
# print(json_output)

# # Optionally, save the JSON to a file
# with open('output.json', 'w') as f:
#     f.write(json_output)


# File "C:\Users\RiGupta\Desktop\BANK_STMT\bnk1.py", line 241, in <module>
#     json_output = main(pdf_path)
#                   ^^^^^^^^^^^^^^
#   File "C:\Users\RiGupta\Desktop\BANK_STMT\bnk1.py", line 236, in main       
#     cleaned_data = clean_table_data(tables)
#                    ^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\RiGupta\Desktop\BANK_STMT\bnk1.py", line 218, in clean_table_data
#     df = df[expected_headers]
#          ~~^^^^^^^^^^^^^^^^^^
#   File "C:\Users\RiGupta\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\frame.py", line 3899, in __getitem__
#     indexer = self.columns._get_indexer_strict(key, "columns")[1]
#               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\RiGupta\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\indexes\base.py", line 6115, in _get_indexer_strict        
#     self._raise_if_missing(keyarr, indexer, axis_name)
#   File "C:\Users\RiGupta\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\indexes\base.py", line 6176, in _raise_if_missing
#     raise KeyError(f"None of [{key}] are in the [{axis_name}]")
# KeyError: "None of [Index(['Date', 'Description', 'Withdrawals', 'Deposits', 
# 'Balance'], dtype='object')] are in the [columns]"

#-------------------------------------------------------------------------------------------------------------------------------------------------------------


# import pdfplumber
# import pandas as pd
# import json

# def extract_table_from_pdf(pdf_path):
#     with pdfplumber.open(pdf_path) as pdf:
#         tables = []
#         for page in pdf.pages:
#             table = page.extract_table()
#             if table:
#                 tables.append(table)
#     return tables

# def clean_table_data(tables):
#     cleaned_data = []
#     expected_headers = ["Date", "Description", "Withdrawals", "Deposits", "Balance"]
    
#     for table in tables:
#         headers = table[0]
#         data = table[1:]
        
#         # Align headers if necessary
#         if len(headers) > len(expected_headers):
#             headers = headers[:len(expected_headers)]
#         elif len(headers) < len(expected_headers):
#             headers += [None] * (len(expected_headers) - len(headers))
        
#         df = pd.DataFrame(data, columns=headers)
        
#         # Rename columns to match expected headers
#         df.columns = expected_headers
        
#         # Clean the data
#         df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        
#         # Convert to numeric where appropriate
#         df['Withdrawals'] = pd.to_numeric(df['Withdrawals'], errors='coerce')
#         df['Deposits'] = pd.to_numeric(df['Deposits'], errors='coerce')
#         df['Balance'] = pd.to_numeric(df['Balance'], errors='coerce')
        
#         cleaned_data.append(df)
    
#     # Combine all dataframes
#     combined_df = pd.concat(cleaned_data, ignore_index=True)
#     return combined_df

# def convert_table_to_json(df):
#     return df.to_json(orient='records', date_format='iso')

# def main(pdf_path):
#     tables = extract_table_from_pdf(pdf_path)
#     cleaned_data = clean_table_data(tables)
#     json_data = convert_table_to_json(cleaned_data)
#     return json_data

# pdf_path = 'Dummy Bank Statement.pdf'
# json_output = main(pdf_path)
# print(json_output)

# # Optionally, save the JSON to a file
# with open('output.json', 'w') as f:
#     f.write(json_output)


# [{"Date":"07\/01\/2023","Description":"Opening Balance","Withdrawals":null,"Deposits":null,"Balance":null},{"Date":"07\/02\/2023","Description":"Electric 
# Bill Payment","Withdrawals":null,"Deposits":null,"Balance":null},{"Date":"07\/05\/2023","Description":"Grocery Store","Withdrawals":null,"Deposits":null,"Balance":null},{"Date":"07\/08\/2023","Description":"Salary Deposit","Withdrawals":null,"Deposits":null,"Balance":null},{"Date":"07\/12\/2023","Description":"Online Shopping - Z-Mart","Withdrawals":null,"Deposits":null,"Balance":null},{"Date":"07\/15\/2023","Description":"Cash Withdrawal - ATM","Withdrawals":null,"Deposits":null,"Balance":null},{"Date":"07\/22\/2023","Description":"Coffee Shop","Withdrawals":null,"Deposits":null,"Balance":null},{"Date":"07\/25\/2023","Description":"Gas Station","Withdrawals":null,"Deposits":null,"Balance":null},{"Date":"07\/28\/2023","Description":"Water Bill Payment","Withdrawals":null,"Deposits":null,"Balance":null},{"Date":"07\/30\/2023","Description":"Gym Membership Fee","Withdrawals":null,"Deposits":null,"Balance":null},{"Date":"07\/31\/2023","Description":"Movie Streaming Service\nSubscription","Withdrawals":null,"Deposits":null,"Balance":null},{"Date":"07\/31\/2023","Description":"Monthly Maintenance Fee","Withdrawals":null,"Deposits":null,"Balance":null}]



#-------------------------------------------------------------------------------------------------------------------------------------------------------------



# import pdfplumber
# import pandas as pd
# import json

# def extract_table_from_pdf(pdf_path):
#     with pdfplumber.open(pdf_path) as pdf:
#         tables = []
#         for page in pdf.pages:
#             table = page.extract_table()
#             if table:
#                 tables.append(table)
#     return tables

# def clean_table_data(tables):
#     cleaned_data = []
#     expected_headers = ["Date", "Description", "Withdrawals", "Deposits", "Balance"]
    
#     for table in tables:
#         headers = table[0]
#         data = table[1:]
        
#         # Align headers if necessary
#         if len(headers) > len(expected_headers):
#             headers = headers[:len(expected_headers)]
#         elif len(headers) < len(expected_headers):
#             headers += [None] * (len(expected_headers) - len(headers))
        
#         df = pd.DataFrame(data, columns=headers)
        
#         # Rename columns to match expected headers
#         df.columns = expected_headers
        
#         # Clean the data
#         df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        
#         # Convert to numeric where appropriate
#         df['Withdrawals'] = pd.to_numeric(df['Withdrawals'], errors='coerce')
#         df['Deposits'] = pd.to_numeric(df['Deposits'], errors='coerce')
#         df['Balance'] = pd.to_numeric(df['Balance'], errors='coerce')
        
#         cleaned_data.append(df)
    
#     # Combine all dataframes
#     combined_df = pd.concat(cleaned_data, ignore_index=True)
#     return combined_df

# def convert_table_to_json(df):
#     # Convert NaN values to None for proper JSON formatting
#     df = df.where(pd.notna(df), None)
    
#     # Convert DataFrame to list of dictionaries (records)
#     records = df.to_dict(orient='records')
    
#     # Serialize to JSON with proper formatting
#     json_data = json.dumps(records, indent=4)
#     return json_data

# def main(pdf_path):
#     tables = extract_table_from_pdf(pdf_path)
#     cleaned_data = clean_table_data(tables)
#     json_data = convert_table_to_json(cleaned_data)
#     return json_data

# pdf_path = 'Dummy Bank Statement.pdf'
# json_output = main(pdf_path)
# print(json_output)

# # Optionally, save the JSON to a file
# with open('output.json', 'w') as f:
#     f.write(json_output)



# [
#     {
#         "Date": "07/01/2023",
#         "Description": "Opening Balance",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     },
#     {
#         "Date": "07/02/2023",
#         "Description": "Electric Bill Payment",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     },
#     {
#         "Date": "07/05/2023",
#         "Description": "Grocery Store",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     },
#     {
#         "Date": "07/08/2023",
#         "Description": "Salary Deposit",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     },
#     {
#         "Date": "07/12/2023",
#         "Description": "Online Shopping - Z-Mart",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     },
#     {
#         "Date": "07/15/2023",
#         "Description": "Cash Withdrawal - ATM",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     },
#     {
#         "Date": "07/22/2023",
#         "Description": "Coffee Shop",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     },
#     {
#         "Date": "07/25/2023",
#         "Description": "Gas Station",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     },
#     {
#         "Date": "07/28/2023",
#         "Description": "Water Bill Payment",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     },
#     {
#         "Date": "07/30/2023",
#         "Description": "Gym Membership Fee",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     },
#     {
#         "Date": "07/31/2023",
#         "Description": "Movie Streaming Service\nSubscription",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     },
#     {
#         "Date": "07/31/2023",
#         "Description": "Monthly Maintenance Fee",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     }
# ]



#-------------------------------------------------------------------------------------------------

# LAMMA3


# import json
# from lamma3.pdf import PDFDocument

# def extract_table_from_pdf(pdf_path):
#     with open(pdf_path, "rb") as f:
#         pdf_document = PDFDocument(f)
#         tables = pdf_document.extract_tables()
#     return tables

# def clean_table_data(tables):
#     cleaned_data = []
#     expected_headers = ["Date", "Description", "Withdrawals", "Deposits", "Balance"]
    
#     for table in tables:
#         headers = table[0]
#         data = table[1:]
        
#         # Align headers if necessary
#         if len(headers) > len(expected_headers):
#             headers = headers[:len(expected_headers)]
#         elif len(headers) < len(expected_headers):
#             headers += [None] * (len(expected_headers) - len(headers))
        
#         df = pd.DataFrame(data, columns=headers)
        
#         # Rename columns to match expected headers
#         df.columns = expected_headers
        
#         # Clean the data
#         df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        
#         # Convert to numeric where appropriate
#         df['Withdrawals'] = pd.to_numeric(df['Withdrawals'], errors='coerce')
#         df['Deposits'] = pd.to_numeric(df['Deposits'], errors='coerce')
#         df['Balance'] = pd.to_numeric(df['Balance'], errors='coerce')
        
#         cleaned_data.append(df)
    
#     # Combine all dataframes
#     combined_df = pd.concat(cleaned_data, ignore_index=True)
#     return combined_df

# def convert_table_to_json(df):
#     # Convert NaN values to None for proper JSON formatting
#     df = df.where(pd.notna(df), None)
    
#     # Convert DataFrame to list of dictionaries (records)
#     records = df.to_dict(orient='records')
    
#     # Serialize to JSON with proper formatting
#     json_data = json.dumps(records, indent=4)
#     return json_data

# def main(pdf_path):
#     tables = extract_table_from_pdf(pdf_path)
#     cleaned_data = clean_table_data(tables)
#     json_data = convert_table_to_json(cleaned_data)
#     return json_data

# pdf_path = 'Dummy Bank Statement.pdf'
# json_output = main(pdf_path)
# print(json_output)

# # Optionally, save the JSON to a file
# with open('output.json', 'w') as f:
#     f.write(json_output)


# C:\Users\RiGupta\Desktop\BANK_STMT>pip install lamma3
# ERROR: Could not find a version that satisfies the requirement lamma3 (from versions: none)
# ERROR: No matching distribution found for lamma3

# C:\Users\RiGupta\Desktop\BANK_STMT>
# C:\Users\RiGupta\Desktop\BANK_STMT>python bnk1.py     
# Traceback (most recent call last):
#   File "C:\Users\RiGupta\Desktop\BANK_STMT\bnk1.py", line 512, in <module>
#     from lamma3.pdf import PDFDocument
# ModuleNotFoundError: No module named 'lamma3'


#-----------------------------------------------------------------------------------------------------------------------------


# import pdfplumber
# import pandas as pd
# import json

# def extract_table_from_pdf(pdf_path):
#     with pdfplumber.open(pdf_path) as pdf:
#         tables = []
#         for page in pdf.pages:
#             table = page.extract_table()
#             if table:
#                 tables.append(table)
#     return tables

# def clean_table_data(tables):
#     cleaned_data = []
#     expected_headers = ["Date", "Description", "Withdrawals", "Deposits", "Balance"]
    
#     for table in tables:
#         headers = table[0]
#         data = table[1:]
        
#         # Align headers if necessary
#         if len(headers) > len(expected_headers):
#             headers = headers[:len(expected_headers)]
#         elif len(headers) < len(expected_headers):
#             headers += [None] * (len(expected_headers) - len(headers))
        
#         df = pd.DataFrame(data, columns=headers)
        
#         # Rename columns to match expected headers
#         df.columns = expected_headers
        
#         # Clean the data
#         df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        
#         # Convert to numeric where appropriate
#         df['Withdrawals'] = pd.to_numeric(df['Withdrawals'], errors='coerce')
#         df['Deposits'] = pd.to_numeric(df['Deposits'], errors='coerce')
#         df['Balance'] = pd.to_numeric(df['Balance'], errors='coerce')
        
#         cleaned_data.append(df)
    
#     # Combine all dataframes
#     combined_df = pd.concat(cleaned_data, ignore_index=True)
#     return combined_df

# def convert_table_to_json(df):
#     # Convert NaN values to None for proper JSON formatting
#     df = df.where(pd.notna(df), None)
    
#     # Convert DataFrame to list of dictionaries (records)
#     records = df.to_dict(orient='records')
    
#     # Serialize to JSON with proper formatting
#     json_data = json.dumps(records, indent=4)
#     return json_data

# def main(pdf_path):
#     tables = extract_table_from_pdf(pdf_path)
#     cleaned_data = clean_table_data(tables)
#     json_data = convert_table_to_json(cleaned_data)
#     return json_data

# if __name__ == "__main__":
#     pdf_path = 'Dummy Bank Statement.pdf'
#     json_output = main(pdf_path)
#     print(json_output)

#     # Optionally, save the JSON to a file
#     with open('output.json', 'w') as f:
#         f.write(json_output)


# [
#     {
#         "Date": "07/01/2023",
#         "Description": "Opening Balance",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     },
#     {
#         "Date": "07/02/2023",
#         "Description": "Electric Bill Payment",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     },
#     {
#         "Date": "07/05/2023",
#         "Description": "Grocery Store",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     },
#     {
#         "Date": "07/08/2023",
#         "Description": "Salary Deposit",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     },
#     {
#         "Date": "07/12/2023",
#         "Description": "Online Shopping - Z-Mart",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     },
#     {
#         "Date": "07/15/2023",
#         "Description": "Cash Withdrawal - ATM",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     },
#     {
#         "Date": "07/22/2023",
#         "Description": "Coffee Shop",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     },
#     {
#         "Date": "07/25/2023",
#         "Description": "Gas Station",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     },
#     {
#         "Date": "07/28/2023",
#         "Description": "Water Bill Payment",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     },
#     {
#         "Date": "07/30/2023",
#         "Description": "Gym Membership Fee",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     },
#     {
#         "Date": "07/31/2023",
#         "Description": "Movie Streaming Service\nSubscription",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     },
#     {
#         "Date": "07/31/2023",
#         "Description": "Monthly Maintenance Fee",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": NaN
#     }
# ]


#-----------------------------------------------------------------------------------------------------------------


# import pdfplumber
# import pandas as pd
# import json

# def extract_table_from_pdf(pdf_path):
#     with pdfplumber.open(pdf_path) as pdf:
#         tables = []
#         for page in pdf.pages:
#             table = page.extract_table()
#             if table:
#                 tables.append(table)
#     return tables

# def clean_table_data(tables):
#     cleaned_data = []
#     expected_headers = ["Date", "Description", "Withdrawals", "Deposits", "Balance"]
    
#     for table in tables:
#         headers = table[0]
#         data = table[1:]
        
#         # Align headers if necessary
#         if len(headers) > len(expected_headers):
#             headers = headers[:len(expected_headers)]
#         elif len(headers) < len(expected_headers):
#             headers += [None] * (len(expected_headers) - len(headers))
        
#         df = pd.DataFrame(data, columns=headers)
        
#         # Rename columns to match expected headers
#         df.columns = expected_headers
        
#         # Clean the data
#         df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        
#         # Convert to numeric where appropriate
#         df['Withdrawals'] = pd.to_numeric(df['Withdrawals'].str.replace('[\$,]', '', regex=True), errors='coerce')
#         df['Deposits'] = pd.to_numeric(df['Deposits'].str.replace('[\$,]', '', regex=True), errors='coerce')
#         df['Balance'] = pd.to_numeric(df['Balance'].str.replace('[\$,]', '', regex=True), errors='coerce')
        
#         cleaned_data.append(df)
    
#     # Combine all dataframes
#     combined_df = pd.concat(cleaned_data, ignore_index=True)
#     return combined_df

# def convert_table_to_json(df):
#     # Convert NaN values to None for proper JSON formatting
#     df = df.where(pd.notna(df), None)
    
#     # Convert DataFrame to list of dictionaries (records)
#     records = df.to_dict(orient='records')
    
#     # Serialize to JSON with proper formatting
#     json_data = json.dumps(records, indent=4)
#     return json_data

# def main(pdf_path):
#     tables = extract_table_from_pdf(pdf_path)
#     cleaned_data = clean_table_data(tables)
#     json_data = convert_table_to_json(cleaned_data)
#     return json_data

# if __name__ == "__main__":
#     pdf_path = 'Dummy Bank Statement.pdf'
#     json_output = main(pdf_path)
#     print(json_output)

#     # Optionally, save the JSON to a file
#     with open('output.json', 'w') as f:
#         f.write(json_output)


# C:\Users\RiGupta\Desktop\BANK_STMT\bnk1.py:794: SyntaxWarning: invalid escape sequence '\$'
#   df['Withdrawals'] = pd.to_numeric(df['Withdrawals'].str.replace('[\$,]', '', regex=True), errors='coerce')
# C:\Users\RiGupta\Desktop\BANK_STMT\bnk1.py:795: SyntaxWarning: invalid escape sequence '\$'
#   df['Deposits'] = pd.to_numeric(df['Deposits'].str.replace('[\$,]', '', regex=True), errors='coerce')
# C:\Users\RiGupta\Desktop\BANK_STMT\bnk1.py:796: SyntaxWarning: invalid escape sequence '\$'
#   df['Balance'] = pd.to_numeric(df['Balance'].str.replace('[\$,]', '', regex=True), errors='coerce')
# [
#     {
#         "Date": "07/01/2023",
#         "Description": "Opening Balance",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": 5000.0
#     },
#     {
#         "Date": "07/02/2023",
#         "Description": "Electric Bill Payment",
#         "Withdrawals": 250.0,
#         "Deposits": NaN,
#         "Balance": 4750.0
#     },
#     {
#         "Date": "07/05/2023",
#         "Description": "Grocery Store",
#         "Withdrawals": 150.0,
#         "Deposits": NaN,
#         "Balance": 4600.0
#     },
#     {
#         "Date": "07/08/2023",
#         "Description": "Salary Deposit",
#         "Withdrawals": NaN,
#         "Deposits": 1000.0,
#         "Balance": 5600.0
#     },
#     {
#         "Date": "07/12/2023",
#         "Description": "Online Shopping - Z-Mart",
#         "Withdrawals": 100.0,
#         "Deposits": NaN,
#         "Balance": 5500.0
#     },
#     {
#         "Date": "07/15/2023",
#         "Description": "Cash Withdrawal - ATM",
#         "Withdrawals": 200.0,
#         "Deposits": NaN,
#         "Balance": 5300.0
#     },
#     {
#         "Date": "07/22/2023",
#         "Description": "Coffee Shop",
#         "Withdrawals": 20.0,
#         "Deposits": NaN,
#         "Balance": 4930.0
#     },
#     {
#         "Date": "07/25/2023",
#         "Description": "Gas Station",
#         "Withdrawals": 50.0,
#         "Deposits": NaN,
#         "Balance": 4880.0
#     },
#     {
#         "Date": "07/28/2023",
#         "Description": "Water Bill Payment",
#         "Withdrawals": 300.0,
#         "Deposits": NaN,
#         "Balance": 4580.0
#     },
#     {
#         "Date": "07/30/2023",
#         "Description": "Gym Membership Fee",
#         "Withdrawals": 80.0,
#         "Deposits": NaN,
#         "Balance": 4500.0
#     },
#     {
#         "Date": "07/31/2023",
#         "Description": "Movie Streaming Service\nSubscription",
#         "Withdrawals": 50.0,
#         "Deposits": NaN,
#         "Balance": 4450.0
#     },
#     {
#         "Date": "07/31/2023",
#         "Description": "Monthly Maintenance Fee",
#         "Withdrawals": 200.0,
#         "Deposits": NaN,
#         "Balance": 4250.0
#     }
# ]


#-------------------------------------------------------------------------------------------------------------------------------



# import pdfplumber
# import pandas as pd
# import json

# def extract_table_from_pdf(pdf_path):
#     with pdfplumber.open(pdf_path) as pdf:
#         tables = []
#         for page in pdf.pages:
#             table = page.extract_table()
#             if table:
#                 tables.append(table)
#     return tables

# def clean_table_data(tables):
#     cleaned_data = []
#     expected_headers = ["Date", "Description", "Withdrawals", "Deposits", "Balance"]
    
#     for table in tables:
#         headers = table[0]
#         data = table[1:]
        
#         # Align headers if necessary
#         if len(headers) > len(expected_headers):
#             headers = headers[:len(expected_headers)]
#         elif len(headers) < len(expected_headers):
#             headers += [None] * (len(expected_headers) - len(headers))
        
#         df = pd.DataFrame(data, columns=headers)
        
#         # Rename columns to match expected headers
#         df.columns = expected_headers
        
#         # Clean the data
#         df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        
#         # Convert to numeric where appropriate
#         df['Withdrawals'] = pd.to_numeric(df['Withdrawals'].str.replace(r'[\$,]', '', regex=True), errors='coerce')
#         df['Deposits'] = pd.to_numeric(df['Deposits'].str.replace(r'[\$,]', '', regex=True), errors='coerce')
#         df['Balance'] = pd.to_numeric(df['Balance'].str.replace(r'[\$,]', '', regex=True), errors='coerce')
        
#         cleaned_data.append(df)
    
#     # Combine all dataframes
#     combined_df = pd.concat(cleaned_data, ignore_index=True)
#     return combined_df

# def convert_table_to_json(df):
#     # Convert NaN values to None for proper JSON formatting
#     df = df.where(pd.notna(df), None)
    
#     # Convert DataFrame to list of dictionaries (records)
#     records = df.to_dict(orient='records')
    
#     # Serialize to JSON with proper formatting
#     json_data = json.dumps(records, indent=4)
#     return json_data

# def main(pdf_path):
#     tables = extract_table_from_pdf(pdf_path)
#     cleaned_data = clean_table_data(tables)
#     json_data = convert_table_to_json(cleaned_data)
#     return json_data

# if __name__ == "__main__":
#     pdf_path = 'Dummy Bank Statement.pdf'
#     json_output = main(pdf_path)
#     print(json_output)

#     # Optionally, save the JSON to a file
#     with open('output.json', 'w') as f:
#         f.write(json_output)


# [
#     {
#         "Date": "07/01/2023",
#         "Description": "Opening Balance",
#         "Withdrawals": NaN,
#         "Deposits": NaN,
#         "Balance": 5000.0
#     },
#     {
#         "Date": "07/02/2023",
#         "Description": "Electric Bill Payment",
#         "Withdrawals": 250.0,
#         "Deposits": NaN,
#         "Balance": 4750.0
#     },
#     {
#         "Date": "07/05/2023",
#         "Description": "Grocery Store",
#         "Withdrawals": 150.0,
#         "Deposits": NaN,
#         "Balance": 4600.0
#     },
#     {
#         "Date": "07/08/2023",
#         "Description": "Salary Deposit",
#         "Withdrawals": NaN,
#         "Deposits": 1000.0,
#         "Balance": 5600.0
#     },
#     {
#         "Date": "07/12/2023",
#         "Description": "Online Shopping - Z-Mart",
#         "Withdrawals": 100.0,
#         "Deposits": NaN,
#         "Balance": 5500.0
#     },
#     {
#         "Date": "07/15/2023",
#         "Description": "Cash Withdrawal - ATM",
#         "Withdrawals": 200.0,
#         "Deposits": NaN,
#         "Balance": 5300.0
#     },
#     {
#         "Date": "07/22/2023",
#         "Description": "Coffee Shop",
#         "Withdrawals": 20.0,
#         "Deposits": NaN,
#         "Balance": 4930.0
#     },
#     {
#         "Date": "07/25/2023",
#         "Description": "Gas Station",
#         "Withdrawals": 50.0,
#         "Deposits": NaN,
#         "Balance": 4880.0
#     },
#     {
#         "Date": "07/28/2023",
#         "Description": "Water Bill Payment",
#         "Withdrawals": 300.0,
#         "Deposits": NaN,
#         "Balance": 4580.0
#     },
#     {
#         "Date": "07/30/2023",
#         "Description": "Gym Membership Fee",
#         "Withdrawals": 80.0,
#         "Deposits": NaN,
#         "Balance": 4500.0
#     },
#     {
#         "Date": "07/31/2023",
#         "Description": "Movie Streaming Service\nSubscription",
#         "Withdrawals": 50.0,
#         "Deposits": NaN,
#         "Balance": 4450.0
#     },
#     {
#         "Date": "07/31/2023",
#         "Description": "Monthly Maintenance Fee",
#         "Withdrawals": 200.0,
#         "Deposits": NaN,
#         "Balance": 4250.0
#     }
# ]


#-----------------------------------------------------------------------------------------------------------



