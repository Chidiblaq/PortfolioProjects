#!/usr/bin/env python
# coding: utf-8

# step 1 -- Imports

# In[1]:


import requests
import pandas as pd
import sqlalchemy
from time import sleep


# step 2

# In[2]:


headers = {
    'authority': 'api2.realtor.ca',
    'sec-ch-ua': '^\\^Google',
    'accept': '*/*',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
    'origin': 'https://www.realtor.ca',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.realtor.ca/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'visid_incap_2269415=56oEKAXmT1e8LgWFhTODX39HT2EAAAAAQUIPAAAAAAA6XQQJauxAZNKYdTMi51ef; nlbi_2269415=QaoGOd78EWeyusHAkG5lugAAAAAihIiZUQqjacyaIhgm93n/; _fbp=fb.1.1632585611808.1195553212; gig_bootstrap_3_mrQiIl6ov44s2X3j6NGWVZ9SDDtplqV7WgdcyEpGYnYxl7ygDWPQHqQqtpSiUfko=gigya-pr_ver4; ASP.NET_SessionId=ls0ga3brpkfa0gwbb4t5iwjb; visid_incap_2271082=Bc3F/XJ7TXy966CgTpn81s9HT2EAAAAAQUIPAAAAAAAN6ueej0G2bHS8YfvoFfRL; nlbi_2271082=Y41sWIuXbWoSw4ZNcbDG1QAAAAAnuH/JvEJyvwbXFE/zX4aq; incap_ses_1184_2269415=MAMGBVlRRBprgaaLPGpuEGWAUGEAAAAAUMf2tKoUjjdygWbVgIw0EQ==; incap_ses_458_2269415=563WS3ux8DkbKMuoCSVbBuPyUWEAAAAAovhxVyjZzO9XyNCp20L7Ow==; incap_ses_458_2271082=BMetKrhiDTE7LcuoCSVbBujyUWEAAAAAgNH9YrvVt5nqijVx0EZ3Mw==; incap_ses_1104_2271082=j6+DUoVfyHLtmbXFmDJSD9P1UWEAAAAAqfG5AXvjjFQISsLO4gwV4w==; incap_ses_1104_2269415=yBPiJnyRn1owr8DFmDJSDwL9UWEAAAAApUlEomlbyOylhaCs3U3kEg==; incap_ses_459_2269415=JJiaRC5kCQTnO5eakbJeBvE9UmEAAAAAt+uTDRhKdXyPtNXmOQL7Fg==; incap_ses_452_2269415=2TbtdM7jlydht9bGEdRFBo/NUmEAAAAA3S/ehFvuui8jIjqRZO5wDg==; incap_ses_374_2269415=YP9/KO5RfGPDRyHzb7cwBbjSUmEAAAAAM8TVj8Yj5IMkP/X1yR58bQ==; incap_ses_1098_2269415=SqcoX+WOskd+XK+QpeE8D+DXUmEAAAAAwSHqqUztYsYNA4CjAehGBQ==; incap_ses_868_2269415=0oYkQdLIZSW6tK5B28ELDIAoU2EAAAAAhLkoQrFwL/pKfYWQJijdmA==; incap_ses_1105_2269415=+ufkHAEF7S8kNVUYtMZVD2lPU2EAAAAAN+IrEp7zORC2fHIpbel5Cw==; incap_ses_1372_2269415=nsKNYGt5Gl+3rCyoKFMKEzCHU2EAAAAAFWMoocoVKfbpcXWhbw/09A==; incap_ses_457_2269415=WZZ7FBhWAxRpMQEEkpdXBjCLU2EAAAAAtsb/LakuHY44P/fQDh5Fdw==; incap_ses_9125_2269415=7k/OTxGY9mEmwzP7cYOifpSOU2EAAAAAIDzUgxoLc8wUKblKQF7DFw==; incap_ses_1371_2269415=0rLzGXYGVSFi7pRugsUGE2RVVGEAAAAA9oRCalWypy9jXuqksc+vCw==; incap_ses_1100_2269415=fSU2ItKCF1EhXRLfm/xDD3CjVGEAAAAA5sqkvxIb3mMZ3PB/NF90+g==; incap_ses_1099_2269415=l614GKsZgTeQDAiMJm9AD5ioVGEAAAAAGO5EQljCtOZQ2pNiC/7w9g==; incap_ses_1319_2269415=xNvABJz+oxFlooyjzQdOEm3mVGEAAAAAxiQf/7+Dg+CZPa9S3pSOkw==; incap_ses_8218_2269415=+y2aFYvCpXqsN2E7uTMMcnjNVWEAAAAAfHPk/xbBsMXgbuLbpMPNTg==; incap_ses_197_2271082=3X/wR9xLtUNxBvKYAOO7AiUpVmEAAAAAnO0hNZiy8G3Uj8+vTlCNtg==; incap_ses_197_2269415=l+ICQuRgMU2MMfiYAOO7AgkxVmEAAAAASRrEoGwj4tp1MRR8VKhjLA==; incap_ses_1183_2269415=OhEqR+IVNDAvLF4EqdxqEPyYV2EAAAAAj75sX5j7/ivaxxNTG2895A==; nlbi_2269415_2147483646=wrGTc9ggtGxbM37akG5lugAAAAA0nsxxFO1DAuYLqRO0Jgti; reese84=3:FoqroZXTX0um54SOwIWKjA==:YO/yl3InHTMII3M6BnzM4zkbG1owlrcizV7RqLEDrQfMgcGBcqC2k5r0yaS6XeNvcypeVlgUTbf+7ezOc2RpTLkTTl3xbtJ09wg8bs3ieMnYIR56Z7FuPN8LXSQcruXu1yE4hZFM0YiGNprDnV2Kibf+/t1PgSvcC9KI9Ct+JtAe/ZEu4CJu4pEUl+o3gikzaiqi8MsW97bSQcyTFsSiIbk2qd/bJ08X63cvhSi8WTHUJqYt+bMKe1Xyk9HwwKZoKOCUFXiS3ii4vN0v/FHLk8Jy7o9LQB/Z1xzOVtjoA7NNmcXNiRPOABG+6cAtm088xS5DOzomuJGllFBgAyF54Vwc2Aus1UVxbTEJSDxXQeXAUALPutaa7yRdJLeeBO48oePz7joPHjKNOjDviGenYnq9PPyelddtxVbUPeQSyRCj5/33eJnYA4B1IqyXZbGe:npm/6v3pppT1/jtFb9eSCDl4lxXy40xw2WOBV1LuS9M=; _gid=GA1.2.1060470715.1633131322; _ga=GA1.1.47856707.1632585606; incap_ses_1183_2271082=FXDrZneGFnV0218EqdxqEDubV2EAAAAAURvnkWlw2CeqpDLIEHCilA==; _4c_=XZNtb5swEMe^%^2FSsXUvCrENg^%^2BGSHnRJVIVqa2qtdteRo59AasEI2NCsyrffWeWJl0Bibv^%^2F^%^2FXw2x917MFTQBDOaxTHFm2Vo3ASvcOiC2XtgtfKvfTALUirVlqQi5EqKMCkyGQpJKboFiA0TW0IguAnefK6ExBnNSEHi^%^2BHgTqOYjh4Kt6Gv3GYtzQnBfxPQHJb7EWUYTjNvhBJwDeZqQ^%^2F1GvICrbE^%^2Foe9LbGlJVzbTebTodhiCyI2hkbSTHdifbbvXDa9QoexNs8KaKYclZM7k1TntWQsjgiLCZ8coZ142Fa5DT^%^2FBKM6wowlPJnsNQzzWndu8mysm2fhcvJ0B2alunkZk7VkG9YMcTVB7VHsYP5LNNL0e7DXbHHNyPfF5MmaFqw7vBxauLOmb1fLOT2rzyCsrHxspVB^%^2BsaLphHTaNCeNTRa9tdDIw3xxu8SqSqMAq0GLqIgI^%^2Bu4Pepm3oPGVb61C^%^2B^%^2B52^%^2FXO1RDfheZpxwiPsDpaiTTIMt9aoXrq1w00QGmBz1alXDCjYawnrQStX^%^2BV1YTi5qBbqsHMqcjWprPRKlaA^%^2B6UWb4uu6kntelKUP1XjRlL8rxK7xryhLU1Qo7LNiKuvMdiOXZ60Z6BL2F6RtnD^%^2Bg86hKs9s31AzqtoHFa1MYuzG6HuhS^%^2BT^%^2BwlgtzGmqEDf9BFZc0OrooYVYOTEfweT9eha2ELWGT7pctKY8oaIml2U4Q67WBM^%^2F9F6Jw3n7CKHo9yOw4ZGbfBMfhXOJ9Iw^%^2FtkLjdqL1fj59gFcZXBO0RdKe2o8vR^%^2B7TxOnfBFlLbpOSwXdqzNtcDxNTxwzyjk2LaXYFA4rkeNE^%^2BQuJ^%^2FXkwaZEwTgkPJbA8TBTjYcGLTSi3yUakfJsqsQnOKSk^%^2BLMlSfkpJ838Zj8e^%^2F; _ga_Y07J3B53QP=GS1.1.1633131320.7.1.1633131388.60',
}

data = {
  'LatitudeMax': '49.31729',
  'LongitudeMax': '-123.02307',
  'LatitudeMin': '49.19818',
  'LongitudeMin': '-123.22474',
  'Sort': '6-D',
  'PropertyTypeGroupID': '1',
  'PropertySearchTypeId': '1',
  'TransactionTypeId': '2',
  'Currency': 'CAD',
  'RecordsPerPage': '12',
  'ApplicationId': '1',
  'CultureId': '1',
  'Version': '7.0',
  'CurrentPage': '1'
}

response = requests.post('https://api2.realtor.ca/Listing.svc/PropertySearch_Post', headers=headers, data=data)


# Step 3 -- Check the status code

# In[3]:


response


# Step 4 -- Create Json Object

# In[4]:


result_json = response.json()


# Step 5 -- Output Keys

# In[5]:


result_json.keys()


# Step 6 -- Find the data
# 
# a. Address
# 
# b. Bedrooms
# 
# c. Bathrooms
# 
# d. Agent Name
# 
# e. Area Code
# 
# f. Phone Number
# 
# g. Agent Organization
# 
# h. Property Type
# 
# i. Parking
# 
# j. Amenities Near by
# 
# k. Ownership Type
# 
# l. Land Size
# 
# m. Price

# In[6]:


#starting point

result_items = result_json['Results']


# In[7]:


len(result_items)


# In[8]:


#address of the first

result_items[0]['Property']['Address']['AddressText']


# In[9]:


#bedrooms
result_items[0]['Building']['Bedrooms']


# In[10]:


#bathrooms
result_items[0]['Building']['BathroomTotal']


# In[11]:


#Agent name
result_items[0]['Individual'][0]['Name']


# In[12]:


#Area Code
result_items[0]['Individual'][0]['Phones'][0]['AreaCode']


# In[13]:


#Phone number
result_items[0]['Individual'][0]['Phones'][0]['PhoneNumber']


# In[14]:


#Agent organization
result_items[0]['Individual'][0]['Organization']['Name']


# In[15]:


#Property type
result_items[0]['Property']['Type']


# In[16]:


#Parking
result_items[0]['Property']['Parking'][0]['Name']


# In[17]:


#Amenities nearby
result_items[0]['Property']['AmmenitiesNearBy']


# In[18]:


#Ownership type
result_items[0]['Property']['OwnershipType']


# In[19]:


#Land size
result_items[0]['Land']['SizeTotal']


# In[20]:


#Price
result_items[0]['Property']['Price']


# Step 7 -- Put everything together -- Loop through and append data inside a list

# In[21]:


address = []
bedrooms = []
bathrooms = []
agent_name = []
area_code = []
phone_number = []
agent_organization = []
property_type = []
parking = []
amenities_nearby = []
ownership_type = []
land_size = []
price = []

for result in result_items:
    
    #address
    try:
        address.append(result['Property']['Address']['AddressText'])
    except:
        address.append('')
    
    #bedrooms
    try:
        bedrooms.append(result['Building']['Bedrooms'])
    except:
        bedrooms.append('')
    
    #bathrooms
    try:
        bathrooms.append(result['Building']['BathroomTotal'])
    except:
        bathrooms.append('')
    
    #agent name
    try:
        agent_name.append(result['Individual'][0]['Name'])
    except:
        agent_name.append('')
        
    #area code
    try:
        area_code.append(result['Individual'][0]['Phones'][0]['AreaCode'])
    except:
        area_code.append('')
    
    #phone number
    try:
        phone_number.append(result['Individual'][0]['Phones'][0]['PhoneNumber'])
    except:
        phone_number.append('')
    
    #agent_organization
    try:
        agent_organization.append(result['Individual'][0]['Organization']['Name'])
    except:
        agent_organization.append('')
    
    #property_type
    try:
        property_type.append(result['Property']['Type'])
    except:
        property_type.append('')
    
    #parking
    try:
        parking.append(result['Property']['Parking'][0]['Name'])
    except:
        parking.append('')
    
    #amenities_nearby
    try:
        amenities_nearby.append(result['Property']['AmmenitiesNearBy'])
    except:
        amenities_nearby.append('')
    
    #ownership_type
    try:
        ownership_type.append(result['Property']['OwnershipType'])
    except:
        ownership_type.append('')
    
    #land_size
    try:
        land_size.append(result['Land']['SizeTotal'])
    except:
        land_size.append('')
    
    #price
    try:
        price.append(result['Property']['Price'])
    except:
        price.append('')


# Step 8 -- Pandas Dataframe

# In[22]:


df_realtor4 = pd.DataFrame({'address': address, 'bedrooms': bedrooms, 'bathrooms': bathrooms,
                           'agent_name': agent_name, 'area_code': area_code, 'phone_number': phone_number,
                           'agent_organization': agent_organization, 'property_type': property_type,
                           'parking': parking, 'amenities_nearby': amenities_nearby, 'ownership_type': ownership_type,
                           'land_size': land_size, 'price': price})


# In[23]:


df_realtor4


# Step 9 -- Multiple Pages

# In[24]:


address = []
bedrooms = []
bathrooms = []
agent_name = []
area_code = []
phone_number = []
agent_organization = []
property_type = []
parking = []
amenities_nearby = []
ownership_type = []
land_size = []
price = []

for i in range(1,51):
    
    headers = {
    'authority': 'api2.realtor.ca',
    'sec-ch-ua': '^\\^Google',
    'accept': '*/*',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
    'origin': 'https://www.realtor.ca',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.realtor.ca/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'visid_incap_2269415=56oEKAXmT1e8LgWFhTODX39HT2EAAAAAQUIPAAAAAAA6XQQJauxAZNKYdTMi51ef; nlbi_2269415=QaoGOd78EWeyusHAkG5lugAAAAAihIiZUQqjacyaIhgm93n/; _fbp=fb.1.1632585611808.1195553212; gig_bootstrap_3_mrQiIl6ov44s2X3j6NGWVZ9SDDtplqV7WgdcyEpGYnYxl7ygDWPQHqQqtpSiUfko=gigya-pr_ver4; ASP.NET_SessionId=ls0ga3brpkfa0gwbb4t5iwjb; visid_incap_2271082=Bc3F/XJ7TXy966CgTpn81s9HT2EAAAAAQUIPAAAAAAAN6ueej0G2bHS8YfvoFfRL; nlbi_2271082=Y41sWIuXbWoSw4ZNcbDG1QAAAAAnuH/JvEJyvwbXFE/zX4aq; incap_ses_1184_2269415=MAMGBVlRRBprgaaLPGpuEGWAUGEAAAAAUMf2tKoUjjdygWbVgIw0EQ==; incap_ses_458_2269415=563WS3ux8DkbKMuoCSVbBuPyUWEAAAAAovhxVyjZzO9XyNCp20L7Ow==; incap_ses_458_2271082=BMetKrhiDTE7LcuoCSVbBujyUWEAAAAAgNH9YrvVt5nqijVx0EZ3Mw==; incap_ses_1104_2271082=j6+DUoVfyHLtmbXFmDJSD9P1UWEAAAAAqfG5AXvjjFQISsLO4gwV4w==; incap_ses_1104_2269415=yBPiJnyRn1owr8DFmDJSDwL9UWEAAAAApUlEomlbyOylhaCs3U3kEg==; incap_ses_459_2269415=JJiaRC5kCQTnO5eakbJeBvE9UmEAAAAAt+uTDRhKdXyPtNXmOQL7Fg==; incap_ses_452_2269415=2TbtdM7jlydht9bGEdRFBo/NUmEAAAAA3S/ehFvuui8jIjqRZO5wDg==; incap_ses_374_2269415=YP9/KO5RfGPDRyHzb7cwBbjSUmEAAAAAM8TVj8Yj5IMkP/X1yR58bQ==; incap_ses_1098_2269415=SqcoX+WOskd+XK+QpeE8D+DXUmEAAAAAwSHqqUztYsYNA4CjAehGBQ==; incap_ses_868_2269415=0oYkQdLIZSW6tK5B28ELDIAoU2EAAAAAhLkoQrFwL/pKfYWQJijdmA==; incap_ses_1105_2269415=+ufkHAEF7S8kNVUYtMZVD2lPU2EAAAAAN+IrEp7zORC2fHIpbel5Cw==; incap_ses_1372_2269415=nsKNYGt5Gl+3rCyoKFMKEzCHU2EAAAAAFWMoocoVKfbpcXWhbw/09A==; incap_ses_457_2269415=WZZ7FBhWAxRpMQEEkpdXBjCLU2EAAAAAtsb/LakuHY44P/fQDh5Fdw==; incap_ses_9125_2269415=7k/OTxGY9mEmwzP7cYOifpSOU2EAAAAAIDzUgxoLc8wUKblKQF7DFw==; incap_ses_1371_2269415=0rLzGXYGVSFi7pRugsUGE2RVVGEAAAAA9oRCalWypy9jXuqksc+vCw==; incap_ses_1100_2269415=fSU2ItKCF1EhXRLfm/xDD3CjVGEAAAAA5sqkvxIb3mMZ3PB/NF90+g==; incap_ses_1099_2269415=l614GKsZgTeQDAiMJm9AD5ioVGEAAAAAGO5EQljCtOZQ2pNiC/7w9g==; incap_ses_1319_2269415=xNvABJz+oxFlooyjzQdOEm3mVGEAAAAAxiQf/7+Dg+CZPa9S3pSOkw==; incap_ses_8218_2269415=+y2aFYvCpXqsN2E7uTMMcnjNVWEAAAAAfHPk/xbBsMXgbuLbpMPNTg==; incap_ses_197_2271082=3X/wR9xLtUNxBvKYAOO7AiUpVmEAAAAAnO0hNZiy8G3Uj8+vTlCNtg==; incap_ses_197_2269415=l+ICQuRgMU2MMfiYAOO7AgkxVmEAAAAASRrEoGwj4tp1MRR8VKhjLA==; incap_ses_1183_2269415=OhEqR+IVNDAvLF4EqdxqEPyYV2EAAAAAj75sX5j7/ivaxxNTG2895A==; nlbi_2269415_2147483646=wrGTc9ggtGxbM37akG5lugAAAAA0nsxxFO1DAuYLqRO0Jgti; reese84=3:FoqroZXTX0um54SOwIWKjA==:YO/yl3InHTMII3M6BnzM4zkbG1owlrcizV7RqLEDrQfMgcGBcqC2k5r0yaS6XeNvcypeVlgUTbf+7ezOc2RpTLkTTl3xbtJ09wg8bs3ieMnYIR56Z7FuPN8LXSQcruXu1yE4hZFM0YiGNprDnV2Kibf+/t1PgSvcC9KI9Ct+JtAe/ZEu4CJu4pEUl+o3gikzaiqi8MsW97bSQcyTFsSiIbk2qd/bJ08X63cvhSi8WTHUJqYt+bMKe1Xyk9HwwKZoKOCUFXiS3ii4vN0v/FHLk8Jy7o9LQB/Z1xzOVtjoA7NNmcXNiRPOABG+6cAtm088xS5DOzomuJGllFBgAyF54Vwc2Aus1UVxbTEJSDxXQeXAUALPutaa7yRdJLeeBO48oePz7joPHjKNOjDviGenYnq9PPyelddtxVbUPeQSyRCj5/33eJnYA4B1IqyXZbGe:npm/6v3pppT1/jtFb9eSCDl4lxXy40xw2WOBV1LuS9M=; _gid=GA1.2.1060470715.1633131322; _ga=GA1.1.47856707.1632585606; incap_ses_1183_2271082=FXDrZneGFnV0218EqdxqEDubV2EAAAAAURvnkWlw2CeqpDLIEHCilA==; _4c_=XZNtb5swEMe^%^2FSsXUvCrENg^%^2BGSHnRJVIVqa2qtdteRo59AasEI2NCsyrffWeWJl0Bibv^%^2F^%^2FXw2x917MFTQBDOaxTHFm2Vo3ASvcOiC2XtgtfKvfTALUirVlqQi5EqKMCkyGQpJKboFiA0TW0IguAnefK6ExBnNSEHi^%^2BHgTqOYjh4Kt6Gv3GYtzQnBfxPQHJb7EWUYTjNvhBJwDeZqQ^%^2F1GvICrbE^%^2Foe9LbGlJVzbTebTodhiCyI2hkbSTHdifbbvXDa9QoexNs8KaKYclZM7k1TntWQsjgiLCZ8coZ142Fa5DT^%^2FBKM6wowlPJnsNQzzWndu8mysm2fhcvJ0B2alunkZk7VkG9YMcTVB7VHsYP5LNNL0e7DXbHHNyPfF5MmaFqw7vBxauLOmb1fLOT2rzyCsrHxspVB^%^2BsaLphHTaNCeNTRa9tdDIw3xxu8SqSqMAq0GLqIgI^%^2Bu4Pepm3oPGVb61C^%^2B^%^2B52^%^2FXO1RDfheZpxwiPsDpaiTTIMt9aoXrq1w00QGmBz1alXDCjYawnrQStX^%^2BV1YTi5qBbqsHMqcjWprPRKlaA^%^2B6UWb4uu6kntelKUP1XjRlL8rxK7xryhLU1Qo7LNiKuvMdiOXZ60Z6BL2F6RtnD^%^2Bg86hKs9s31AzqtoHFa1MYuzG6HuhS^%^2BT^%^2BwlgtzGmqEDf9BFZc0OrooYVYOTEfweT9eha2ELWGT7pctKY8oaIml2U4Q67WBM^%^2F9F6Jw3n7CKHo9yOw4ZGbfBMfhXOJ9Iw^%^2FtkLjdqL1fj59gFcZXBO0RdKe2o8vR^%^2B7TxOnfBFlLbpOSwXdqzNtcDxNTxwzyjk2LaXYFA4rkeNE^%^2BQuJ^%^2FXkwaZEwTgkPJbA8TBTjYcGLTSi3yUakfJsqsQnOKSk^%^2BLMlSfkpJ838Zj8e^%^2F; _ga_Y07J3B53QP=GS1.1.1633131320.7.1.1633131388.60',
    }

    data = {
      'LatitudeMax': '49.31729',
      'LongitudeMax': '-123.02307',
      'LatitudeMin': '49.19818',
      'LongitudeMin': '-123.22474',
      'Sort': '6-D',
      'PropertyTypeGroupID': '1',
      'PropertySearchTypeId': '1',
      'TransactionTypeId': '2',
      'Currency': 'CAD',
      'RecordsPerPage': '12',
      'ApplicationId': '1',
      'CultureId': '1',
      'Version': '7.0',
      'CurrentPage': str(i),
    }
    
    #response
    try:
        response = requests.post('https://api2.realtor.ca/Listing.svc/PropertySearch_Post', headers=headers, data=data)
    except requests.exceptions.ConnectionError:
        response.status_code = "Connection refused"
        sleep(5)

    
    #json object
    result_json = response.json()
    
    #result items
    result_items = result_json['Results']
    
    for result in result_items:

        #address
        try:
            address.append(result['Property']['Address']['AddressText'])
        except:
            address.append('')

        #bedrooms
        try:
            bedrooms.append(result['Building']['Bedrooms'])
        except:
            bedrooms.append('')

        #bathrooms
        try:
            bathrooms.append(result['Building']['BathroomTotal'])
        except:
            bathrooms.append('')

        #agent name
        try:
            agent_name.append(result['Individual'][0]['Name'])
        except:
            agent_name.append('')

        #area code
        try:
            area_code.append(result['Individual'][0]['Phones'][0]['AreaCode'])
        except:
            area_code.append('')

        #phone number
        try:
            phone_number.append(result['Individual'][0]['Phones'][0]['PhoneNumber'])
        except:
            phone_number.append('')

        #agent_organization
        try:
            agent_organization.append(result['Individual'][0]['Organization']['Name'])
        except:
            agent_organization.append('')

        #property_type
        try:
            property_type.append(result['Property']['Type'])
        except:
            property_type.append('')

        #parking
        try:
            parking.append(result['Property']['Parking'][0]['Name'])
        except:
            parking.append('')

        #amenities_nearby
        try:
            amenities_nearby.append(result['Property']['AmmenitiesNearBy'])
        except:
            amenities_nearby.append('')

        #ownership_type
        try:
            ownership_type.append(result['Property']['OwnershipType'])
        except:
            ownership_type.append('')

        #land_size
        try:
            land_size.append(result['Land']['SizeTotal'])
        except:
            land_size.append('')

        #price
        try:
            price.append(result['Property']['Price'])
        except:
            price.append('')


# In[25]:


df_realtor4 = pd.DataFrame({'address': address, 'bedrooms': bedrooms, 'bathrooms': bathrooms,
                           'agent_name': agent_name, 'area_code': area_code, 'phone_number': phone_number,
                           'agent_organization': agent_organization, 'property_type': property_type,
                           'parking': parking, 'amenities_nearby': amenities_nearby, 'ownership_type': ownership_type,
                           'land_size': land_size, 'price': price})


# In[26]:


df_realtor4


# In[27]:


df_realtor4.shape


# Step 10 -- Store results in excel

# In[28]:


df_realtor4.to_excel('realtor_data.xlsx', index=False)


# Step 11 -- Store in PostgreSQL

# In[29]:


# #create SQLalchemy engine
# engine = sqlalchemy.create_engine('postgresql://postgres:XXXXXXXXXXXXXXXXXXX')
# df_realtor4.to_sql('real_estate_data', engine)

