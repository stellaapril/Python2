import json

data = {"fiscal_year": [], "start_date": [""], "area": [""], "asset_type": [""], "planning_status": [""]}

with open('jsonfile.json','w')as f:
  json.dump(data,f)
