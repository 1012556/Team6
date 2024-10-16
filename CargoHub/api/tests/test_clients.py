
from CargoHub.api.Services.ServicesClients import Clients


client1 = {
        "id": 1,
        "name": "Damian Virgilio",
        "address": "1296 Daniel Road Apt. 349",
        "city": "Pierceview",
        "zip_code": "28301",
        "province": "Colorado",
        "country": "United States",
        "contact_name": "Bryan Clark",
        "contact_phone": "242.732.3483x2573",
        "contact_email": "robertcharles@example.net",
        "created_at": "2010-04-28 02:22:53",
        "updated_at": "2022-02-09 20:22:35"
    }

client2 = {
        "id": 2,
        "name": "Mees",
        "address": "1296 Daniel Road Apt. 349",
        "city": "Pierceview",
        "zip_code": "28301",
        "province": "Colorado",
        "country": "United States",
        "contact_name": "Bryan Clark",
        "contact_phone": "242.732.3483x2573",
        "contact_email": "robertcharles@example.net",
        "created_at": "2010-04-28 02:22:53",
        "updated_at": "2022-02-09 20:22:35"
    }

client3 = {
        "id": 3,
        "name": "Joey",
        "address": "1296 Daniel Road Apt. 349",
        "city": "Pierceview",
        "zip_code": "28301",
        "province": "Colorado",
        "country": "United States",
        "contact_name": "Bryan Clark",
        "contact_phone": "242.732.3483x2573",
        "contact_email": "robertcharles@example.net",
        "created_at": "2010-04-28 02:22:53",
        "updated_at": "2022-02-09 20:22:35"
    }

client4 = {
        "id": 4,
        "name": "Joey",
        "address": "1296 Daniel Road Apt. 349",
        "city": "Pierceview",
        "zip_code": "28301",
        "province": "Colorado",
        "country": "United States",
        "contact_name": "Bryan Clark",
        "contact_phone": "242.732.3483x2573",
        "contact_email": "robertcharles@example.net",
        "created_at": "2010-04-28 02:22:53",
        "updated_at": "2022-02-09 20:22:35"
    }
emptyclient = { }

obj = Clients("./CargoHub/data/test_")

def test_AddClients():
    obj.add_client(client1)
    assert len(obj.data) == 2
    obj.add_client(emptyclient)
    assert len(obj.data) == 2 # lege client word ook toegevoegd
    
def test_RemoveClients():
    obj.add_client(client2)
    obj.remove_client(client2["id"])
    len_cient_list_before = len(obj.data)
    assert obj.data < len(len_cient_list_before)
    
def addCients():
    obj.add_location(location1)
    obj.add_location(location2)

def test_addvalidlocations():
    obj.data = []
    assert len(obj.data) == 2
    assert len(obj.data) == 3

def test_getlocation():
    obj.data = []
    addlocations()
    data = obj.get_location(2)
    assert data["id"] == 2

def test_addemptylocations():
    obj.data = []
    obj.add_location(emptylocation)
    assert len(obj.data) == 3 # geen check voor lege dict

def test_updatelocation():
    obj.update_location(2, locationtoupdate)
    assert obj.get_location(2)["id"] == 2 # update id niet automatisch

def test_removelocation():
    obj.remove_location(3)
    assert len(obj.data) == 3

def test_getlocationswarehouse():
    data = obj.get_locations_in_warehouse(1)
    assert len(data) == 2

def test_dbload():
    obj.data = []
    obj.load(False)
    assert len(obj.data) == 1

def test_dbsave():
    obj.data = []
    addlocations()
    obj.save()
    obj.data = []
    obj.load(False)

    assert len(obj.data) == 3
    
