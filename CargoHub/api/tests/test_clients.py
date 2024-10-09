
from models.clients import Clients
import json


client_correct1 = {
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

client_correct2 = {
        "id": 2,
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

client_correct3 = {
        "id": 3,
        "name": "Mehmet",
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

client_wrong1 = {
        "id": 10000000000000000000000000000000000000000000000000000000000000000000000000000,
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

client_wrong2 = {
        "id": -1,
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

client_wrong3 = {
        "id": "1",
        "name": 1,
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

client_wrong4 = {
        "id": "",
        "name": "",
        "address": "",
        "city": "",
        "zip_code": "",
        "province": "",
        "country": "",
        "contact_name": "",
        "contact_phone": "",
        "contact_email": "",
        "created_at": "",
        "updated_at": ""
    }


emptyclient = { }

obj = Clients("./CargoHub/data/testdb/test_")

def test_AddClients_normaal():
    obj.data = []
    obj.add_client(client_correct1) 
    assert len(obj.data) == 1, "Client1 is niet correct toegevoegd, verwachtte 1 client maar kreeg {}".format(len(obj.data))

def test_AddClients_empty():
    obj.data = []
    obj.add_client(emptyclient)
    assert len(obj.data) == 0, "empyt client is toegevoegd, verwachtte 0 client maar kreeg {}".format(len(obj.data)) # voegt lege client toe terwijl dit niet moet

def test_AddClients_double():  
    obj.data = []
    obj.add_client(client_correct1) 
    obj.add_client(client_correct1)
    assert len(obj.data) == 1, "2 dezelfde clients zijn toegevoegd, verwachtte 1 client maar kreeg {}".format(len(obj.data)) # voegt dezelfde clients toe

def test_AddClients_wrong_info_max_value():
    obj.data = []
    obj.add_client(client_wrong1)
    assert len(obj.data) == 0, "client met verkeerd id wordt toegevoegd (max value), verwachtte 0 clients maar kreeg {}".format(len(obj.data)) # voegt client toe met verkeerde info
    
def test_AddClients_wrong_info_min_value():
    obj.data = []    
    obj.add_client(client_wrong2)
    assert len(obj.data) == 0, "client met verkeerd id wordt toegevoegd (min value), verwachtte 0 clients maar kreeg {}".format(len(obj.data))
    
def test_AddClients_wrong_info_id_string():
    obj.data = []    
    obj.add_client(client_wrong3)
    assert len(obj.data) == 0, "client met verkeerd id wordt toegevoegd (string), verwachtte 0 clients maar kreeg {}".format(len(obj.data))
    
def test_AddClients_wrong_info_empty_string():
    obj.data = []    
    obj.add_client(client_wrong4)
    assert len(obj.data) == 0, "client met lege strings wordt toegevoegd, verwachtte 0 clients maar kreeg {}".format(len(obj.data))

def test_RemoveClients():
    obj.data = []
    obj.add_client(client_correct1)
    len_cient_list_before = len(obj.data)
    obj.remove_client(1)
    assert len(obj.data) < len_cient_list_before, "client wordt verwijderd, verwachtte 0 clients maar kreeg {}".format(len(obj.data))

def test_RemoveClients_empty():
    obj.data = []
    obj.remove_client(1)
    assert len(obj.data) == 0, "client wordt verwijderd van lege lijst, verwachtte 0 clients maar kreeg {}".format(len(obj.data))

def AddClients(): #, "{}".format(len(obj.data))
    obj.data = []
    obj.add_client(client_correct1)
    obj.add_client(client_correct2)

def test_get_clients():
    AddClients()
    list_to_compare = []
    list_to_compare.append(client_correct1)
    list_to_compare.append(client_correct2)
    assert len(obj.data) == len(list_to_compare), "lijst met clients wordt uit db gehaald, verwachtte 2 maar kreeg {}".format(len(obj.data))

def test_get_client_correct_id():
    AddClients()
    client = obj.get_client(2)
    assert client["id"] == 2, "client wordt uit de database gehaald, verwachtte 2 maar kreeg {}".format(client["id"])

def test_get_client_wrong_id_not_in_db():
    AddClients()
    client = obj.get_client(4)
    assert client is None, "client wordt gezocht met onbestaand id, verwachtte None maar kreeg {}".format(client)

def test_get_client_wrong_id_min_value():
    AddClients()
    client = obj.get_client(-1)
    assert client is None, "client wordt gezocht met onbestaand id, verwachtte None maar kreeg {}".format(client)

def test_update_client_correct():
    AddClients()
    obj.update_client(2, client_correct3)
    assert client_correct3 in obj.data, "update client met correcte info, verwachtte nieuwe client in bd maar kreeg {}".format(len(obj.data))
    assert client_correct3["id"] == 2, "update client met correcte info, verwachtte id 2 maar kreeg {}".format(client_correct3["id"])

def test_update_client_wrong_info_id_max():
    AddClients()
    obj.update_client(2, client_wrong1)
    assert client_wrong1 not in obj.data, "update client met verkeerd id(max), verwachtte true maar kreeg {}".format(client_wrong1 not in obj.data)

def test_update_client_wrong_info_id_min():
    AddClients()
    obj.update_client(2, client_wrong2)
    assert client_wrong2 not in obj.data, "update client met verkeerd id(min), verwachtte true maar kreeg {}".format(client_wrong2 not in obj.data)

def test_update_client_wrong_info_id_string():
    AddClients()
    obj.update_client(2, client_wrong3)
    assert client_wrong3 not in obj.data, "update client met verkeerd id(string), verwachtte true maar kreeg {}".format(client_wrong3 not in obj.data)

def test_update_client_wrong_info_empty_string():
    AddClients()
    obj.update_client(2, client_wrong4)
    assert client_wrong4 not in obj.data, "update client met lege strings, verwachtte true maar kreeg {}".format(client_wrong4 not in obj.data)

def test_update_client_wrong_info_empty():
    AddClients()
    obj.update_client(2, emptyclient)
    assert emptyclient not in obj.data, "update client met lege strings, verwachtte true maar kreeg {}".format(emptyclient not in obj.data)

def test_remove_client():
    AddClients()
    obj.remove_client(2)
    assert len(obj.data) == 1, "haalt client weg uit db, verwachtte 1 maar kreeg {}".format(len(obj.data))

def test_remove_client_wrong_id():
    AddClients()
    obj.remove_client(10)
    assert len(obj.data) == 2, "probeert niet bestaande client weg te halen uit db, verwachtte 2 maar kreeg {}".format(len(obj.data))

def test_client_db_load_empty():
    obj.data = []
    obj.load(False)
    assert len(obj.data) == 0, "lengte van de db bij leeg en false, verwachtte 0 maar kreeg {}".format(len(obj.data))

def test_client_db_load_full():
    obj.data.append(client_correct1)
    obj.data.append(client_correct2)
    f = open(obj.data_path, "w")
    json.dump(obj.data, f)
    f.close()
    obj.data = []
    obj.load(False)
    assert len(obj.data) == 2, "lengte van db bij 1 client en false, verwachtte 1 maar kreeg {}".format(len(obj.data))

def test_clien_db_load_true():
    obj.load(True)
    assert len(obj.data) == 0, "lege lijst als er geen json is, verwachtte 0 maar kreeg {}".format(len(obj.data))

def test_client_db_save():
    AddClients()
    obj.save()
    obj.load(False)
    assert len(obj.data) == 2, "haalt lijst uit json, verwachtte 2 maar kreeg {}".fromat(len(obj.data))