import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import psycopg2
import getpass
import pdvega
import config

import os 

conn = psycopg2.connect(dbname=config.dbname, user=config.user, host=config.host, port=config.port,password=config.password)
cur=conn.cursor()

query_schema = 'SET search_path to ' + "eicu_crd" + ';'

