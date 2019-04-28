import json,urllib.request
from datetime import *

#def make_catalog(users_early_days_first_harvest, users_late_days_first_harvest,expected_planting_date):
def make_catalog(users_early_days_first_harvest, users_late_days_first_harvest):


    cat_dicts=[]
    output=True
    page_number=1
    crop_number=1
    while output:
        data = urllib.request.urlopen("https://www.growstuff.org/crops.json/?page=" + str(page_number)).read()
        output = json.loads(data)
        if not output:
            break
        for one_crop in output:
            tempdict = {}
            if not one_crop:
                break
            #print("Local crop number:  " + str(crop_number))
            #print("Crop ID of source API: " + str(one_crop['id']))
            if one_crop['median_days_to_first_harvest']:
                first_harvest=one_crop['median_days_to_first_harvest']
                if ((first_harvest>=users_early_days_first_harvest) and (first_harvest<=users_late_days_first_harvest)):
                    #print("inside 1st harvest window")
                    #tempdict['utf16name']= str(one_crop['name'].encode("utf-16"))
                    tempdict['utf8name']= str(one_crop['name'].encode("utf-8").decode("utf-8")).title()
                    tempdict['cropname']= str(one_crop['name'])
                    if one_crop['perennial']:
                        tempdict['isPerennial']="Yes"
                    else:
                        tempdict['isPerennial']="No"
                    #print(tempdict)
                    # date_from_now =             (datetime.now() + timedelta(days=22)).strftime('%m-%d-%Y')  #strftime('%Y-%m-%d')
                    # result_first_harvest_early= (datetime.now() + timedelta(days=22)).strftime('%m-%d-%Y')
                    # result_first_harvest_late=   (datetime.now() + timedelta(days=33)).strftime('%m-%d-%Y')
                    if (one_crop['median_days_to_last_harvest']):
                        median_days_to_last_harvest=one_crop['median_days_to_last_harvest']
                        if median_days_to_last_harvest<first_harvest:
                            result_date_last_harvest=(datetime.now() + timedelta(days=median_days_to_last_harvest)).strftime('%m-%d-%Y') +"**"
                        else:
                            result_date_last_harvest=(datetime.now() + timedelta(days=median_days_to_last_harvest)).strftime('%m-%d-%Y')
                    else:
                        result_date_last_harvest="NA"
                    result_date_first_harvest= (datetime.now() + timedelta(days=first_harvest)).strftime('%m-%d-%Y')
                    tempdict['first_harvest_date_start']= result_date_first_harvest
                    tempdict['first_harvest_date_end']= result_date_last_harvest
                    #tempdict['wiki_url']=(one_crop['en_wikipedia_url'].encode("utf-8"))
                    tempdict['wiki_url']=(one_crop['en_wikipedia_url'])
                    tempdict['crop_list_num']=len(cat_dicts)+1
                    #print(len(cat_dicts))

            # print("first harvest days:  " + str(one_crop['median_days_to_first_harvest']))
            # print("slug name:  "  + one_crop['slug'])
            # print("is perennial?  " + str(one_crop['perennial']))
            #print(str(one_crop['name'])) # bad char in name crashing Python        
            #print(one_crop['name'].encode("utf-8")) # bad char in name crashing Python
            # print(one_crop['name'][:1]+"--first char") # bad char in name crashing Python, so for now am just looking at the first character\
            #print(one_crop['en_wikipedia_url'].encode("utf-16")) # bad char in wiki URL crashing Python    
            # print(one_crop['en_wikipedia_url'][:11]) # bad char in wiki URL crashing Python, so just first few char for now
            # print("median days to last harvest: " + str(one_crop['median_days_to_last_harvest']))
            if tempdict:    
                cat_dicts.append(tempdict)
            #print("---end this crop---")
            crop_number += 1
        #print(page_number)
        #print("*"*80)
        #print(output[list_index]['name'])
        page_number += 1
    print(page_number)
    return cat_dicts

first_days=95
last_days=100

make_catalog(first_days,last_days)
