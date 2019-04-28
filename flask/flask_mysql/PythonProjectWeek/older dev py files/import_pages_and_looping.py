

import json,urllib.request
page_number=20
list_index=1
users_early_days_first_harvest=80
users_late_days_first_harvest=100
data = urllib.request.urlopen("https://www.growstuff.org/crops.json/?page=" + str(page_number)).read()
output = json.loads(data)
print("d"*80)
#print(data)
print("oAll")
# print(output)

# if not output:
#     print("page is empty")
# else:
#     print("o2"*80)
#     output_fields ="name of crop # "+ str(list_index+1)  +"  is :  " + output[0]['name'] 
#     #output_fields = output_fields+ "\nwiki of crop# "+ str(list_index+1)  +"  is :  " + str(output[0]['en_wikipedia_url'])
#     output_fields = output_fields+ "\ndays 1st harvest is " + str(output[0]['median_days_to_first_harvest'])
#     output_fields = output_fields+ "\ndays last harvest is " + str(output[0]['median_days_to_last_harvest'])

#     print(output_fields)


output=True
page_number=1
crop_number=1
while output:
    data = urllib.request.urlopen("https://www.growstuff.org/crops.json/?page=" + str(page_number)).read()
    output = json.loads(data)
    if not output:
        break
    for one_crop in output:
        if not one_crop:
            break
        print("Local crop number:  " + str(crop_number))
        print("Crop ID of source API: " + str(one_crop['id']))
        if one_crop['median_days_to_first_harvest']:
            first_harvest=one_crop['median_days_to_first_harvest']
            if ((first_harvest>=users_early_days_first_harvest) and (first_harvest<=users_late_days_first_harvest)):
                print("inside 1st harvest window")

        print("first harvest days:  " + str(one_crop['median_days_to_first_harvest']))
        print(one_crop['perennial'])
        #print(one_crop['name']) # bad char in name crashing Python
        print(one_crop['name'][:1]+"--first char") # bad char in name crashing Python, so for now am just looking at the first character\
        #print(one_crop['en_wikipedia_url'][:5]) # bad char in wiki URL crashing Python    
        print(one_crop['en_wikipedia_url'][:11]) # bad char in wiki URL crashing Python, so just first few char for now
        print("median days to last harvest" + str(one_crop['median_days_to_last_harvest']))
        print("---end this crop---")
        crop_number += 1
    print(page_number)
    print("*"*80)
    #print(output[list_index]['name'])
    page_number += 1
