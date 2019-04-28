

import json,urllib.request
page_number=1
list_index=0
data = urllib.request.urlopen("https://www.growstuff.org/crops.json/?page=" + str(page_number)).read()
output = json.loads(data)
print("d"*80)
#print(data)
print("oAll")
#print(output)
if not output:
    print("page is empty")
else:
    print("o2"*80)
    output_fields ="name of crop # "+ str(list_index+1)  +"  is :  " + output[0]['name'] 
    output_fields = output_fields+ "\nwiki of crop# "+ str(list_index+1)  +"  is :  " + output[0]['en_wikipedia_url']
    output_fields = output_fields+ "\ndays 1st harvest is " + str(output[0]['median_days_to_first_harvest'])
    output_fields = output_fields+ "\ndays last harvest is " + str(output[0]['median_days_to_last_harvest'])

    print(output_fields)

    