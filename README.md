# ChartMogul MRR Churn Rates Ranking
## Overview
This script pulls the MRR Churn rates for a given time period and returns the 3 highest MRR Churn rates by default.

##### Steps for Use:
  1. Add ChartMogul API keys

  You can find your ChartMogul API Token and Secret Key at https://app.chartmogul.com/#admin/api (admin permissions required). For more information check the **Authentication** section on the [ChartMogul Metrics API page] (https://github.com/chartmogul/metrics-api/blob/master/API-Documentation/api.md)

  a) Open the cm_mrr.py file in the mrr-churn folder with a text editor (e.g. TextEdit, Sublime Text 2, Atom).

  b) Add your ChartMogul API Token and Secret Key to lines 11 & 12 of cm.py.

  2. \*\*Optional\*\* Change Function Parameters
  
  a) Open the cm_mrr.py file in the mrr-churn folder with a text editor (e.g. TextEdit, Sublime Text 2, Atom).

  b) Edit any parameters in the `get_highest_values` function on line XX, see section below for details
  
  3. Run the script!

##### Configurations
On line XX, the function `get_highes_values` takes in a start date and an end date which is the time interval for which the rates will be requested. Finally, you can choose how many values to show using the `no_of_values` field. Note these values are returned from **highest to lowest**.
- `start`(Date) - The start date of the required period of data. An ISO-8601 formatted date, e.g. "2015-05-12"
- `end` (Date) - The end date of the required period of data. An ISO-8601 formatted date, e.g. "2015-05-12"
- `no_of_values` (int) - The number of rates to be returned in descending order

