import numpy as np
import pandas as pd
from utils import *


categorical = ['Product_Info_1','Product_Info_2','Product_Info_3','Product_Info_5','Product_Info_6','Product_Info_7','Employment_Info_2','Employment_Info_3','Employment_Info_5','InsuredInfo_1','InsuredInfo_2','InsuredInfo_3','InsuredInfo_4','InsuredInfo_5','InsuredInfo_6','InsuredInfo_7','Insurance_History_1','Insurance_History_2','Insurance_History_3','Insurance_History_4','Insurance_History_7','Insurance_History_8','Insurance_History_9', 'Family_Hist_1','Medical_History_2','Medical_History_3','Medical_History_4','Medical_History_5','Medical_History_6','Medical_History_7','Medical_History_8','Medical_History_9','Medical_History_11','Medical_History_12','Medical_History_13','Medical_History_14','Medical_History_16','Medical_History_17','Medical_History_18','Medical_History_19','Medical_History_20','Medical_History_21','Medical_History_22','Medical_History_23','Medical_History_25','Medical_History_26','Medical_History_27','Medical_History_28','Medical_History_29','Medical_History_30','Medical_History_31','Medical_History_33','Medical_History_34','Medical_History_35','Medical_History_36','Medical_History_37','Medical_History_38','Medical_History_39','Medical_History_40','Medical_History_41']

continuous = ['Product_Info_4', 'Ins_Age', 'Ht', 'Wt', 'BMI', 'Employment_Info_1', 'Employment_Info_4', 'Employment_Info_6', 'Insurance_History_5', 'Family_Hist_2', 'Family_Hist_3', 'Family_Hist_4', 'Family_Hist_5']

discrete = ['Medical_History_1', 'Medical_History_10', 'Medical_History_15', 'Medical_History_24', 'Medical_History_32']




raw_data = pd.read_csv('training.csv')

# This step is necessary as it converts string categorical value to numeric categorical value
mapping = sorted([entry for entry in raw_data['Product_Info_2'].tolist() if str(entry) != 'nan'])

dic = {}
reverse_dic = {}
n = 0
for item in mapping:
    if item not in dic:
        dic[item] = n
        n += 1
for key, value in dic.items():
    reverse_dic[value] = key

raw_data['Product_Info_2'] = raw_data['Product_Info_2'].map(dic)
impute = DataImputation(raw_data.drop(columns=['Id']), categorical=categorical, continuous=continuous, discrete=discrete)
impute.central_tendency()
impute.retrieve_imputed_dataframe().to_csv('training_result.csv')



raw_data = pd.read_csv('testing.csv')

raw_data['Product_Info_2'] = raw_data['Product_Info_2'].map(dic)
impute = DataImputation(raw_data.drop(columns=['Id']), categorical=categorical, continuous=continuous, discrete=discrete)
impute.central_tendency()
impute.retrieve_imputed_dataframe().to_csv('testing_result.csv')
