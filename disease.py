import query
import pandas as pd 
import sql_db
import operator

social = pd.read_sql_query(query.query, sql_db.conn)

print("dimensions", social.shape)

print("column names", social.columns)

#check for NA
print(social.isnull().values.any())

print(social.describe())

'''
#print(df.shape)
dxcodes = diagnosis['icd9code']

	

def get_icd_codes(dxcode):
	icd9 = []
	icd10 = []
	for i in range(len(dxcode)):
		#icd9, icd10 = dxcode[i].split(",")
		code = dxcode[i].split(",")
		if len(code) == 2:
			icd10.append(code[1])
			if len(code[0].split(".")) == 1:
				icd9.append(code[0])
			else:
				tmp_icd9 = code[0].split(".")[0] + code[0].split(".")[1]
				icd9.append(tmp_icd9)
			
		if code[0] == '':
			pass
		else:
			if len(code[0].split(".")) == 1:
				icd9.append(code[0])
			else:
				tmp_icd9 = code[0].split(".")[0] + code[0].split(".")[1]
				icd9.append(tmp_icd9)
	return icd9, icd10

icd9, icd10 = get_icd_codes(dxcodes)


def unique(list1): 
    unique_list = [] 
    for x in list1: 
        if x not in unique_list: 
            unique_list.append(x) 
    return unique_list
   

def highest_count(codes):
	code_counts = dict()
	for i in unique(codes):
		#print("element", i,"count", icd9.count(i))
		code_counts[i] = codes.count(i)
	highest_icd9 = dict(sorted(code_counts.items(), key=operator.itemgetter(1), reverse = True))
	return code_counts, highest_icd9


print(len(icd9))

print(highest_count(icd9))

'''






