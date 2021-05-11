import requests
import urllib
import json
import os,sys



def get_company_currency(apikey=None):
    ''' Get the Company Default Currency from Hubspot '''
    parameter_dict = {'hapikey': apikey, 'includeAssociations': 'true'}
    headers = {}
    company_url = "https://api.hubapi.com//integrations/v1/me?"
    parameters = urllib.parse.urlencode(parameter_dict)
    hs_url = company_url + parameters
    r = requests.get(url = hs_url, headers = headers)
    response_dict = json.loads(r.text)
    return(response_dict['currency'])

def get_exchange_rate(apikey=None, base_currency='EUR'):
    ''' Use the company default currency and get the conversion rate '''
    url = "https://v6.exchangerate-api.com/v6/{apikey}/latest/{base_currency}".format(**locals())
    exchange_rate = requests.get(url)
    print(json.loads(exchange_rate.text))

def main():
    ''' Pull out all API keys from os environment '''
    try:
        hs_apikey = os.environ['HS_APIKEY']
        ex_apikey = os.environ['EX_APIKEY']
    except:
        print('You are missing to export the OS variable HS_APIKEY or/and EX_APIKEY')
        print("")
        print("OS error: ", sys.exc_info()[0])
        raise

    ''' Execute the magic '''
    get_exchange_rate(apikey=ex_apikey, base_currency=get_company_currency(apikey=hs_apikey))

if __name__ == "__main__":
    main()
