import query
import pandas as pd 
import numpy as np
import sql_db
import operator
from sklearn.preprocessing import OneHotEncoder

social = pd.read_sql_query(query.query, sql_db.conn)

print("dimensions", social.shape)

print("column names", social.columns)

#check for NA
print("total na", social.isnull().values.sum())

#remove NA
social = social.dropna()

#make sure no more NAs
print("total na after", social.isnull().values.sum())


def get_value_counts(df):
	for (colname, colval) in df.iteritems():
		if colname != "patientunitstayid":
			print(df[colname].value_counts())


#get_value_counts(social)
#separate minorities with caucasian

caucasian = social[social["ethnicity"] == "Caucasian"]


minorities = social[social["ethnicity"] != "Caucasian"]

print("################################")
print("CAUCASIANS")
print("################################")

#get_value_counts(caucasian)
print("################################")
print("MINORITIES")
print("################################")

#get_value_counts(minorities)




#one hot encoding of categorical variables
enc = OneHotEncoder







