

import json,urllib.request
data = urllib.request.urlopen("https://www.growstuff.org/crops.json/?page=1").read()
output = json.loads(data)
print("d"*80)
print(data)
print("o"*80)
print ("name of first crop is :  " + output[0]['name'] + " and days 1st harvest is " + str(output[0]['median_days_to_first_harvest']))