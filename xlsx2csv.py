import glob
import pandas as pd
from joblib import Parallel, delayed
files = glob.glob("*.xlsx")+glob.glob("*.xls")

def to_csv(f):

	df = pd.read_excel(f,sheet_name=None)
	for n in df:
		print (n)
		df[n].to_csv(f+n.replace(" ","_")+".csv",index=False,encoding = 'utf-8')
Parallel(n_jobs=10,verbose=10)(delayed(to_csv)(f) for f in files)
	























