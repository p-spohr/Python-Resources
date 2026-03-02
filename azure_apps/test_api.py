import requests
import pandas as pd
import pathlib
import json

data_dir = pathlib.Path(__file__).absolute().parent

loan_df = pd.read_table(data_dir / 'api_loan_approval_test.csv', header= 0, delimiter= ',', index_col= False)

# print(loan_df.head())

features_df = loan_df[['Married','Education','Self_Employed','ApplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History']]

# print(features_df.head())
# print(features_df.isna().value_counts())
# print(features_df.dropna(axis= 0).isna().value_counts())

features_df.dropna(axis= 0, inplace= True)

# print(features_df.iloc[0].to_dict())

send_data = features_df.iloc[0].to_dict()
print(send_data)
api_uri = 'https://dp-100-exam-oxcnx.germanywestcentral.inference.ml.azure.com/score'

headers =    {'bearer': ''}

request = requests.post(api_uri, data= send_data)
# request = requests.get(api_uri, params= send_data)

print(request.text)