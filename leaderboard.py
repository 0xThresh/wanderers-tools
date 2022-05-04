import requests
from bs4 import BeautifulSoup
import pandas as pd

'''
Fun features to consider adding:
- Wanderer with most losses
- Wanderers with highest win percentages 
'''

# variables
wanderers_url = 'https://battles.wanderers.ai/highscore.php'

# initiate session handler
session = requests.Session()

# get the high score page
response = session.get(wanderers_url)

# load the page into BS and convert it into a string
formsoup = BeautifulSoup(response.text, features='lxml')
formsoup = str(formsoup)

# ingest the page into a pandas table, which pulls the data we care about
table = pd.read_html(formsoup)

# grab the dataframe object from table
table = table[0]

# sort by most Won, then by W/L %
leaders = table.nlargest(20, ['Won:', 'Win/Loss %:'])

# remove "View" column, which doesn't contain the opensea link anymore
leaders = leaders.iloc[: , :-1]

leaders = leaders.to_string(index=False)

# output needs to be updated to whatever discord bot needs
print(leaders)
