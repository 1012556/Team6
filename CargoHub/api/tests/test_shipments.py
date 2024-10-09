from models.shipments import Shipments
from providers import data_provider
import json

shipment_correct_1 = {
  "id": 1,
  "order_id": 1,
  "source_id": 33,
  "order_date": "2000-03-09",
  "request_date": "2000-03-11",
  "shipment_date": "2000-03-13",
  "shipment_type": "I",
  "shipment_status": "Pending",
  "notes": "Zee vertrouwen klas rots heet lachen oneven begrijpen.",
  "carrier_code": "DPD",
  "carrier_description": "Dynamic Parcel Distribution",
  "service_code": "Fastest",
  "payment_type": "Manual",
  "transfer_mode": "Ground",
  "total_package_count": 31,
  "total_package_weight": 594.42,
  "created_at": "2000-03-10T11:11:14Z",
  "updated_at": "2000-03-11T13:11:14Z",
  "items": [
    {
      "item_id": "P007435",
      "amount": 23
    },
    {
      "item_id": "P009557",
      "amount": 1
    },
    {
      "item_id": "P009553",
      "amount": 50
    },
    {
      "item_id": "P010015",
      "amount": 16
    },
    {
      "item_id": "P002084",
      "amount": 33
    },
    {
      "item_id": "P009663",
      "amount": 18
    },
    {
      "item_id": "P010125",
      "amount": 18
    },
    {
      "item_id": "P005768",
      "amount": 26
    },
    {
      "item_id": "P004051",
      "amount": 1
    },
    {
      "item_id": "P005026",
      "amount": 29
    },
    {
      "item_id": "P000726",
      "amount": 22
    },
    {
      "item_id": "P008107",
      "amount": 47
    },
    {
      "item_id": "P001598",
      "amount": 32
    },
    {
      "item_id": "P002855",
      "amount": 20
    },
    {
      "item_id": "P010404",
      "amount": 30
    },
    {
      "item_id": "P010446",
      "amount": 6
    },
    {
      "item_id": "P001517",
      "amount": 9
    },
    {
      "item_id": "P009265",
      "amount": 2
    },
    {
      "item_id": "P001108",
      "amount": 20
    },
    {
      "item_id": "P009110",
      "amount": 18
    },
    {
      "item_id": "P009686",
      "amount": 13
    }
  ]
}

shipment_correct_2 = {
  "id": 2,
  "order_id": 2,
  "source_id": 9,
  "order_date": "1983-11-28",
  "request_date": "1983-11-30",
  "shipment_date": "1983-12-02",
  "shipment_type": "I",
  "shipment_status": "Transit",
  "notes": "Wit duur fijn vlieg.",
  "carrier_code": "PostNL",
  "carrier_description": "Royal Dutch Post and Parcel Service",
  "service_code": "TwoDay",
  "payment_type": "Automatic",
  "transfer_mode": "Ground",
  "total_package_count": 56,
  "total_package_weight": 42.25,
  "created_at": "1983-11-29T11:12:17Z",
  "updated_at": "1983-11-30T13:12:17Z",
  "items": [
    {
      "item_id": "P003790",
      "amount": 10
    },
    {
      "item_id": "P007369",
      "amount": 15
    },
    {
      "item_id": "P007311",
      "amount": 21
    },
    {
      "item_id": "P004140",
      "amount": 8
    },
    {
      "item_id": "P004413",
      "amount": 46
    },
    {
      "item_id": "P004717",
      "amount": 38
    },
    {
      "item_id": "P001919",
      "amount": 13
    },
    {
      "item_id": "P010075",
      "amount": 5
    },
    {
      "item_id": "P006603",
      "amount": 48
    },
    {
      "item_id": "P004504",
      "amount": 30
    },
    {
      "item_id": "P009594",
      "amount": 35
    },
    {
      "item_id": "P008851",
      "amount": 25
    },
    {
      "item_id": "P002129",
      "amount": 46
    },
    {
      "item_id": "P002320",
      "amount": 4
    },
    {
      "item_id": "P008341",
      "amount": 23
    }
  ]
}

shipment_correct_3 = {
  "id": 3,
  "order_id": 3,
  "source_id": 52,
  "order_date": "1973-01-28",
  "request_date": "1973-01-30",
  "shipment_date": "1973-02-01",
  "shipment_type": "I",
  "shipment_status": "Pending",
  "notes": "Hoog genot springen afspraak mond bus.",
  "carrier_code": "DHL",
  "carrier_description": "DHL Express",
  "service_code": "NextDay",
  "payment_type": "Automatic",
  "transfer_mode": "Ground",
  "total_package_count": 29,
  "total_package_weight": 463.0,
  "created_at": "1973-01-28T20:09:11Z",
  "updated_at": "1973-01-29T22:09:11Z",
  "items": [
    {
      "item_id": "P010669",
      "amount": 16
    }
  ]
}

shipment_wrong_id_1 = {
  "id": 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
  "order_id": 2,
  "source_id": 9,
  "order_date": "1983-11-28",
  "request_date": "1983-11-30",
  "shipment_date": "1983-12-02",
  "shipment_type": "I",
  "shipment_status": "Transit",
  "notes": "Wit duur fijn vlieg.",
  "carrier_code": "PostNL",
  "carrier_description": "Royal Dutch Post and Parcel Service",
  "service_code": "TwoDay",
  "payment_type": "Automatic",
  "transfer_mode": "Ground",
  "total_package_count": 56,
  "total_package_weight": 42.25,
  "created_at": "1983-11-29T11:12:17Z",
  "updated_at": "1983-11-30T13:12:17Z",
  "items": [
    {
      "item_id": "P003790",
      "amount": 10
    },
    {
      "item_id": "P007369",
      "amount": 15
    },
    {
      "item_id": "P007311",
      "amount": 21
    },
    {
      "item_id": "P004140",
      "amount": 8
    },
    {
      "item_id": "P004413",
      "amount": 46
    },
    {
      "item_id": "P004717",
      "amount": 38
    },
    {
      "item_id": "P001919",
      "amount": 13
    },
    {
      "item_id": "P010075",
      "amount": 5
    },
    {
      "item_id": "P006603",
      "amount": 48
    },
    {
      "item_id": "P004504",
      "amount": 30
    },
    {
      "item_id": "P009594",
      "amount": 35
    },
    {
      "item_id": "P008851",
      "amount": 25
    },
    {
      "item_id": "P002129",
      "amount": 46
    },
    {
      "item_id": "P002320",
      "amount": 4
    },
    {
      "item_id": "P008341",
      "amount": 23
    }
  ]
}

shipment_wrong_id_2 = {
  "id": -1,
  "order_id": 2,
  "source_id": 9,
  "order_date": "1983-11-28",
  "request_date": "1983-11-30",
  "shipment_date": "1983-12-02",
  "shipment_type": "I",
  "shipment_status": "Transit",
  "notes": "Wit duur fijn vlieg.",
  "carrier_code": "PostNL",
  "carrier_description": "Royal Dutch Post and Parcel Service",
  "service_code": "TwoDay",
  "payment_type": "Automatic",
  "transfer_mode": "Ground",
  "total_package_count": 56,
  "total_package_weight": 42.25,
  "created_at": "1983-11-29T11:12:17Z",
  "updated_at": "1983-11-30T13:12:17Z",
  "items": [
    {
      "item_id": "P003790",
      "amount": 10
    },
    {
      "item_id": "P007369",
      "amount": 15
    },
    {
      "item_id": "P007311",
      "amount": 21
    },
    {
      "item_id": "P004140",
      "amount": 8
    },
    {
      "item_id": "P004413",
      "amount": 46
    },
    {
      "item_id": "P004717",
      "amount": 38
    },
    {
      "item_id": "P001919",
      "amount": 13
    },
    {
      "item_id": "P010075",
      "amount": 5
    },
    {
      "item_id": "P006603",
      "amount": 48
    },
    {
      "item_id": "P004504",
      "amount": 30
    },
    {
      "item_id": "P009594",
      "amount": 35
    },
    {
      "item_id": "P008851",
      "amount": 25
    },
    {
      "item_id": "P002129",
      "amount": 46
    },
    {
      "item_id": "P002320",
      "amount": 4
    },
    {
      "item_id": "P008341",
      "amount": 23
    }
  ]
}

shipment_wrong_id_3 = {
  "id": "",
  "order_id": 2,
  "source_id": 9,
  "order_date": "1983-11-28",
  "request_date": "1983-11-30",
  "shipment_date": "1983-12-02",
  "shipment_type": "I",
  "shipment_status": "Transit",
  "notes": "Wit duur fijn vlieg.",
  "carrier_code": "PostNL",
  "carrier_description": "Royal Dutch Post and Parcel Service",
  "service_code": "TwoDay",
  "payment_type": "Automatic",
  "transfer_mode": "Ground",
  "total_package_count": 56,
  "total_package_weight": 42.25,
  "created_at": "1983-11-29T11:12:17Z",
  "updated_at": "1983-11-30T13:12:17Z",
  "items": [
    {
      "item_id": "P003790",
      "amount": 10
    },
    {
      "item_id": "P007369",
      "amount": 15
    },
    {
      "item_id": "P007311",
      "amount": 21
    },
    {
      "item_id": "P004140",
      "amount": 8
    },
    {
      "item_id": "P004413",
      "amount": 46
    },
    {
      "item_id": "P004717",
      "amount": 38
    },
    {
      "item_id": "P001919",
      "amount": 13
    },
    {
      "item_id": "P010075",
      "amount": 5
    },
    {
      "item_id": "P006603",
      "amount": 48
    },
    {
      "item_id": "P004504",
      "amount": 30
    },
    {
      "item_id": "P009594",
      "amount": 35
    },
    {
      "item_id": "P008851",
      "amount": 25
    },
    {
      "item_id": "P002129",
      "amount": 46
    },
    {
      "item_id": "P002320",
      "amount": 4
    },
    {
      "item_id": "P008341",
      "amount": 23
    }
  ]
}

shipment_wrong_string = {
  "id": "",
  "order_id": "",
  "source_id": "",
  "order_date": "",
  "request_date": "",
  "shipment_date": "",
  "shipment_type": "",
  "shipment_status": "",
  "notes": "",
  "carrier_code": "",
  "carrier_description": "",
  "service_code": "",
  "payment_type": "",
  "transfer_mode": "",
  "total_package_count": "",
  "total_package_weight": "",
  "created_at": "",
  "updated_at": "",
  "items": ""
}

shipment_wrong_empty = {}

obj = Shipments("./CargoHub/data/testdb/test_")

def test_AddShipments_normaal():
    obj.data = []
    obj.add_shipment(shipment_correct_1) 
    assert len(obj.data) == 1, "Shipment is niet correct toegevoegd, verwachtte 1 shipment maar kreeg {}".format(len(obj.data))

def test_AddShipments_empty():
    obj.data = []
    obj.add_shipment(shipment_wrong_empty)
    assert len(obj.data) == 0, "empty shipment is toegevoegd, verwachtte 0 shipments maar kreeg {}".format(len(obj.data)) # voegt lege shipment toe terwijl dit niet moet

def test_Addshipments_double():  
    obj.data = []
    obj.add_shipment(shipment_correct_1) 
    obj.add_shipment(shipment_correct_1)
    assert len(obj.data) == 1, "2 dezelfde shipments zijn toegevoegd, verwachtte 1 shipment maar kreeg {}".format(len(obj.data)) # voegt dezelfde shipments toe

def test_Addshipments_wrong_info_max_value():
    obj.data = []
    obj.add_shipment(shipment_wrong_id_1)
    assert len(obj.data) == 0, "shipment met verkeerd id wordt toegevoegd (max value), verwachtte 0 shipments maar kreeg {}".format(len(obj.data)) # voegt shipment toe met verkeerde info
    
def test_Addshipments_wrong_info_min_value():
    obj.data = []    
    obj.add_shipment(shipment_wrong_id_2)
    assert len(obj.data) == 0, "shipment met verkeerd id wordt toegevoegd (min value), verwachtte 0 shipments maar kreeg {}".format(len(obj.data))
    
def test_Addshipments_wrong_info_id_string():
    obj.data = []    
    obj.add_shipment(shipment_wrong_id_3)
    assert len(obj.data) == 0, "shipment met verkeerd id wordt toegevoegd (string), verwachtte 0 shipments maar kreeg {}".format(len(obj.data))
    
def test_Addshipments_wrong_info_empty_string():
    obj.data = []    
    obj.add_shipment(shipment_wrong_string)
    assert len(obj.data) == 0, "shipment met lege strings wordt toegevoegd, verwachtte 0 shipments maar kreeg {}".format(len(obj.data))

def test_Removeshipments():
    obj.data = []
    obj.add_shipment(shipment_correct_1)
    len_cient_list_before = len(obj.data)
    obj.remove_shipment(1)
    assert len(obj.data) < len_cient_list_before, "shipment wordt verwijderd, verwachtte 0 shipments maar kreeg {}".format(len(obj.data))

def test_Removeshipments_empty():
    obj.data = []
    obj.remove_shipment(1)
    assert len(obj.data) == 0, "shipment wordt verwijderd van lege lijst, verwachtte 0 shipments maar kreeg {}".format(len(obj.data))

def Addshipments(): #, "{}".format(len(obj.data))
    obj.data = []
    obj.add_shipment(shipment_correct_1)
    obj.add_shipment(shipment_correct_2)

def test_get_shipments():
    Addshipments()
    list_to_compare = []
    list_to_compare.append(shipment_correct_1)
    list_to_compare.append(shipment_correct_2)
    assert len(obj.data) == len(list_to_compare), "lijst met shipments wordt uit db gehaald, verwachtte 2 maar kreeg {}".format(len(obj.data))

def test_get_client_correct_id():
    Addshipments()
    shipment = obj.get_shipment(2)
    assert shipment["id"] == 2, "shipment wordt uit de database gehaald, verwachtte 2 maar kreeg {}".format(shipment["id"])

def test_get_client_wrong_id_not_in_db():
    Addshipments()
    shipment = obj.get_shipment(4)
    assert shipment is None, "shipment wordt gezocht met onbestaand id, verwachtte None maar kreeg {}".format(shipment)

def test_get_client_wrong_id_min_value():
    Addshipments()
    shipment = obj.get_shipment(-1)
    assert shipment is None, "shipment wordt gezocht met onbestaand id, verwachtte None maar kreeg {}".format(shipment)

def test_update_client_correct():
    Addshipments()
    obj.update_shipment(2, shipment_correct_3)
    assert shipment_correct_3 in obj.data, "update shipment met correcte info, verwachtte nieuwe shipment in bd maar kreeg {}".format(len(obj.data))
    assert shipment_correct_3["id"] == 2, "update shipment met correcte info, verwachtte id 2 maar kreeg {}".format(shipment_correct_3["id"])

def test_update_client_wrong_info_id_max():
    Addshipments()
    obj.update_shipment(2, shipment_wrong_id_1)
    assert shipment_wrong_id_1 not in obj.data, "update shipment met verkeerd id(max), verwachtte true maar kreeg {}".format(shipment_wrong_id_1 not in obj.data)

def test_update_client_wrong_info_id_min():
    Addshipments()
    obj.update_shipment(2, shipment_wrong_id_2)
    assert shipment_wrong_id_2 not in obj.data, "update shipment met verkeerd id(min), verwachtte true maar kreeg {}".format(shipment_wrong_id_2 not in obj.data)

def test_update_client_wrong_info_id_string():
    Addshipments()
    obj.update_shipment(2, shipment_wrong_id_3)
    assert shipment_wrong_id_3 not in obj.data, "update shipment met verkeerd id(string), verwachtte true maar kreeg {}".format(shipment_wrong_id_3 not in obj.data)

def test_update_client_wrong_info_empty_string():
    Addshipments()
    obj.update_shipment(2, shipment_wrong_string)
    assert shipment_wrong_string not in obj.data, "update shipment met lege strings, verwachtte true maar kreeg {}".format(shipment_wrong_string not in obj.data)

def test_update_client_wrong_info_empty():
    Addshipments()
    obj.update_shipment(2, shipment_wrong_empty)
    assert shipment_wrong_empty not in obj.data, "update shipment met lege strings, verwachtte true maar kreeg {}".format(shipment_wrong_empty not in obj.data)

def test_remove_client():
    Addshipments()
    obj.remove_shipment(2)
    assert len(obj.data) == 1, "haalt shipment weg uit db, verwachtte 1 maar kreeg {}".format(len(obj.data))

def test_remove_client_wrong_id():
    Addshipments()
    obj.remove_shipment(10)
    assert len(obj.data) == 2, "probeert niet bestaande shipment weg te halen uit db, verwachtte 2 maar kreeg {}".format(len(obj.data))

def test_client_db_load_empty():
    obj.data = []
    obj.load(False)
    assert len(obj.data) == 0, "lengte van de db bij leeg en false, verwachtte 0 maar kreeg {}".format(len(obj.data))

def test_client_db_load_full():
    obj.data.append(shipment_correct_1)
    obj.data.append(shipment_correct_2)
    f = open(obj.data_path, "w")
    json.dump(obj.data, f)
    f.close()
    obj.data = []
    obj.load(False)
    assert len(obj.data) == 2, "lengte van db bij 1 shipment en false, verwachtte 1 maar kreeg {}".format(len(obj.data))

def test_clien_db_load_true():
    obj.load(True)
    assert len(obj.data) == 0, "lege lijst als er geen json is, verwachtte 0 maar kreeg {}".format(len(obj.data))

def test_client_db_save():
    Addshipments()
    obj.save()
    obj.load(False)
    assert len(obj.data) == 2, "haalt lijst uit json, verwachtte 2 maar kreeg {}".format(len(obj.data))

def test_get_items_in_shipment():
    Addshipments()
    items = shipment_correct_1["items"]
    items_test = obj.get_items_in_shipment(1)
    assert items == items_test, "checkt of items in shipment gelijk is aan items in db, verwachtte true maar kreeg {}".format(items == items_test)
  
def test_update_items_in_shipment():
    Addshipments()
    items = shipment_correct_2["items"]
    obj.update_items_in_shipment(1, items)
    for item in items:
      shipment_correct_1["items"].append(item)
    assert shipment_correct_1 == obj.data[shipment_correct_1], "checkt of de shipment items correct geüpdatet worden, verwachtte true maar kreeg {}".format(shipment_correct_1 == obj.data[shipment_correct_1])

def test_update_items_in_shipment_double_items():
    Addshipments()
    items = [{
      "item_id": "P003790",
      "amount": 10
    },
    {
      "item_id": "P007369",
      "amount": 15
    },
    {
      "item_id": "P007311",
      "amount": 21
    }]
    obj.update_items_in_shipment(1, items)
    assert shipment_correct_1 == obj.data[shipment_correct_1], "check of er geen dubbele items worden toegevoegd, verwachtte true maar kreeg {}".format(shipment_correct_1 == obj.data[shipment_correct_1])

def test_update_item_in_shipment_inventory(): #moet nog geschreven worden als update item shipment af is
    Addshipments()
  	