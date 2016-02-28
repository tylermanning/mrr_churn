#!/usr/bin/python

import requests
from pprint import pprint
from operator import itemgetter


# Edit lines 11 & 12
# Find your ChartMogul API Token and Secret key at https://app.chartmogul.com/#admin/api
#################################
token = 'CHARTMOGUL_API_TOKEN'
secret = 'CHARTMOGUL_SECRET_KEY'
#################################

# Takes in an MRR Churn Metric string and the number of 
# values to be returned in a list in descending order
def get_highest_values(start, end, no_of_values):
	payload = (('start-date', start), ('end-date', end))
	endpoint = 'https://api.chartmogul.com/v1/metrics/mrr-churn-rate'

	# Make a GET request & decode the JSON response
	response = requests.get(endpoint, params=payload, auth=(token,secret))
	mrr_churn = response.json()

	#Sort the churn rates and return the requested values
	l = sorted(mrr_churn['entries'], key=itemgetter('mrr-churn-rate'), reverse=True)
	return pprint(l[:no_of_values]) 

# Change start/end dates or number of values to return
# Dates must be 'YYYY-MM-DD' format
get_highest_values('2014-08-01', '2015-07-31', 3)
