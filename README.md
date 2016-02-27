# ChartMogul MRR Churn Rates Ranking
## Overview
This script pulls the MRR Churn rates for a given time period and returns the 3 highest MRR Churn rates by default.

##### Steps for Use:
  1. Add ChartMogul API keys

  You can find your ChartMogul API Token and Secret Key at https://app.chartmogul.com/#admin/api (admin permissions required). For more information check the **Authentication** section on the [ChartMogul Metrics API page] (https://github.com/chartmogul/metrics-api/blob/master/API-Documentation/api.md)

  a) Open the cm_mrr.py file in the mrr-churn folder with a text editor (e.g. TextEdit, Sublime Text 2, Atom).

  b) Add your ChartMogul API Token and Secret Key to lines 11 & 12 of cm.py.

  c) \*\*Optional\*\* Edit any parameters in the `get_highest_values` function, see section below for details
  
  2. Run the script!

##### Options
