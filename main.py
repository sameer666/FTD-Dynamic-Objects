from GetToken import token
import requests
import json
import sys
import urllib3

urllib3.disable_warnings()

def mappings_edit(api_path, uuid, maps,headers):
    dm = {
            "mappings": [],
            "type": "DynamicObjectMappings",
            "id": uuid
        }
    for m in maps:
        dm["mappings"].append(m)

    try:
        r = requests.put(api_path, data=json.dumps(dm), headers=headers, verify=False)
        status_code = r.status_code
        resp = r.text
        print("Status code is: "+str(status_code))
        if status_code == 201 or status_code == 202:
            print ("Mapping operation complete")
        else :
            r.raise_for_status()
            print ("Error occurred in POST --> "+resp)
    except requests.exceptions.HTTPError as err:
        print ("Error in connection --> "+str(err))

def get_list(api_path,headers):
    objs = {}
    try:
        r = requests.get(api_path, headers=headers, verify=False)
        status_code = r.status_code
        resp = r.text
        print("Status code is: "+str(status_code))
        if status_code == 200:
            json_resp = json.loads(resp)
            for i in json_resp['items']:
                objs.update({i['name']: i['id']})
        else :
            r.raise_for_status()
            print ("Error occurred in POST --> "+resp)
    except requests.exceptions.HTTPError as err:
        print ("Error in connection --> "+str(err))
    return objs


def dyna():

    print('############### FMC Dynamic Objects Operations ###############')
    print('')
    print('1. Create a new Dynamic Object')
    print('2. Update an existing Dynamic Object')
    print('3. Delete a Dynamic Object')
    print('4. Get current mappings for Dynamic Object')
    c1 = input('Enter the option: ')
    
    auth_token = token(username, password, server)
    headers = {
        'Content-Type': 'application/json',
        'X-auth-access-token': auth_token
    }

    get_api_path = 'https://' + server + '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/dynamicobjects?expanded=true'
    
    if c1 == '1':
        print('')
        name = input('Enter a name for Dynamic Object: ')
        print('Select a method to add mappings to the object')
        print('----------------------------------------------------------')
        print('1. Comma seperated values of mappings to be added')
        print('2. File path containing the values of mappings to be added')
        print('3. If no mappings to be added')
        print('----------------------------------------------------------')
        c4 = input('Enter option: ')
        if c4 == '3':
            mappings = ''
        elif c4 == '1':
            mappings = input('Enter comma seperated values of mappings to be added (e.g. 1.1.1.1,2.2.2.2): ')
            mappings = mappings.strip()
            print('mappings:  ' + mappings)
            maps = mappings.split(',')
        elif c4 == '2':
            filename = input("Enter path of the input file: ")
            inputFile = open(filename, "r")
            mappings = []
            for i in inputFile:
                mappings = i
            maps = mappings.split(',')
            for m in range(0,len(maps)):
                maps[m] = maps[m].strip()
        
        body = {
                "name": name,
                "type": "DynamicObject",
                "objectType": "IP"
                }

        api_path = 'https://' + server + '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/dynamicobjects'

        try:
            r = requests.post(api_path, data=json.dumps(body), headers=headers, verify=False)
            status_code = r.status_code
            resp = r.text
            #print("Status code is: "+str(status_code))
            if status_code == 201 or status_code == 202:
                print ("Object Created")
                json_resp = json.loads(resp)
                uuid = json_resp['id']
                #print(uuid) 
            else :
                r.raise_for_status()
                print ("Error occurred in POST --> "+resp)
        except requests.exceptions.HTTPError as err:
            print ("Error in connection --> "+str(err))

        if mappings != '':
            
            api_path = 'https://' + server + '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/dynamicobjects/' + uuid + '/mappings?action=add'
            mappings_edit(api_path,uuid,maps,headers) 

        print('Task Complete')
        print('--------------------------')
        print('1. Back to Dynamic Objects')
        print('2. Exit')
        print('--------------------------')
        c5 = input('Enter Option: ')
        if  c5 == '1':
            dyna()
        elif c5 == '2':
            sys.exit()         

    if c1 == '2':
        objs = get_list(get_api_path, headers)
        ob = list(objs.keys())
        cnt = 1
        print('')
        for o in objs:
            print(str(cnt) + '. ' + o)
            cnt += 1
        
        c2 = input('Select the dynamic object: ')
        oid = objs[ob[int(c2)-1]]
        print('------------------------')
        print('1. Add mappings')
        print('2. Remove mappings')
        print('------------------------')
        c3 = input('Enter the action: ')

        if c3 == '1':
            print('')
            mappings = input('Enter comma seperated values of mappings to be added: ')
            mappings = mappings.strip()
            api_path = 'https://' + server + '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/dynamicobjects/' + oid + '/mappings?action=add'
            maps = mappings.split(',')
            mappings_edit(api_path,oid,maps,headers)

        elif c3 == '2':
            mappings = input('Enter comma seperated values of mappings to be removed: ')
            mappings = mappings.strip()
            print('mappings:  ' + mappings) 
            api_path = 'https://' + server + '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/dynamicobjects/' + oid + '/mappings?action=remove'
            maps = mappings.split(',')
            mappings_edit(api_path,oid,maps,headers)
        
        print('Task Complete')
        print('--------------------------')
        print('1. Back to Dynamic Objects')
        print('2. Exit')
        print('--------------------------')
        c5 = input('Enter Option: ')
        if  c5 == '1':
            dyna()
        elif c5 == '2':
            sys.exit()

    if c1 == '3':
        objs = get_list(get_api_path, headers)
        ob = list(objs.keys())
        cnt = 1
        print('')
        for o in objs:
            print(str(cnt) + '. ' + o)
            cnt += 1
        print('')
        c2 = input('Select the dynamic object to be deleted: ')
        oid = objs[ob[int(c2)-1]]
        api_path = 'https://' + server + '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/dynamicobjects/' + oid
        try:
            r = requests.delete(api_path, headers=headers, verify=False)
            status_code = r.status_code
            resp = r.text
            #print("Status code is: "+str(status_code))
            if status_code == 200:
                print ("Object Deleted")
            else :
                r.raise_for_status()
                print ("Error occurred in POST --> "+resp)
        except requests.exceptions.HTTPError as err:
            print ("Error in connection --> "+str(err))
        print('Task Complete')
        print('--------------------------')
        print('1. Back to Dynamic Objects')
        print('2. Exit')
        print('--------------------------')
        c5 = input('Enter Option: ')
        if  c5 == '1':
            dyna()
        elif c5 == '2':
            sys.exit()

    if c1 == '4':
        objs = get_list(get_api_path, headers)
        ob = list(objs.keys())
        cnt = 1
        print('')
        for o in objs:
            print(str(cnt) + '. ' + o)
            cnt += 1
        print('')
        c2 = input('Select the dynamic object: ')
        oid = objs[ob[int(c2)-1]]
        api_path = 'https://' + server + '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/dynamicobjects/' + oid + '/mappings'
        try:
            r = requests.get(api_path, headers=headers, verify=False)
            status_code = r.status_code
            resp = r.text
            print("Status code is: "+str(status_code))
            if status_code == 200:
                print('')
                json_resp = json.loads(resp)
                for i in json_resp['items']:
                    print(i['mapping'])
            else :
                r.raise_for_status()
                print ("Error occurred in POST --> "+resp)
        except requests.exceptions.HTTPError as err:
            print ("Error in connection --> "+str(err))
        print('Task Complete')
        print('--------------------------')
        print('1. Back to Dynamic Objects')
        print('2. Exit')
        print('--------------------------')
        c5 = input('Enter Option: ')
        if  c5 == '1':
            dyna()
        elif c5 == '2':
            sys.exit()


if __name__ == "__main__":
    print('This aplication allows users to perform a set of operations on Firepower Dynamic objects')
    print('------------------')
    print('Connect to the FMC')
    print('')
    server = input('Enter the FMC IP or Hostname: ')
    username = input('Enter the Username: ')
    password = input('Enter the Password: ')
    #server = 'fmc7.cisco.com'
    #username = 'sameer'
    #password = 'Sameer3#Azure'
    dyna()


