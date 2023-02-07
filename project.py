# Importing libraries
import numpy as np
import sqlite3
import pandas as pd
from bokeh.plotting import figure, output_file, show
import sqlalchemy as db

# Loading data
train = pd.read_csv(r"C:\Users\jvrdolja\Desktop\Written_project\train.csv")
ideal = pd.read_csv(r"C:\Users\jvrdolja\Desktop\Written_project\ideal.csv")
test = pd.read_csv(r"C:\Users\jvrdolja\Desktop\Written_project\test.csv")

con = sqlite3.connect("project.db")
curs = con.cursor()
engine = db.create_engine("sqlite:///project.db")

print(train)