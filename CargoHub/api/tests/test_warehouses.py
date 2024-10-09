from models.warehouses import Warehouses

warehouse1 = {
    "id": 1,
    "code": "YQZZNL56",
    "name": "Heemskerk cargo hub",
    "address": "Karlijndreef 281",
    "zip": "4002 AS",
    "city": "Heemskerk",
    "province": "Friesland",
    "country": "NL",
    "contact": {
        "name": "Fem Keijzer",
        "phone": "(078) 0013363",
        "email": "blamore@example.net"
    },
    "created_at": "1983-04-13 04:59:55",
    "updated_at": "2007-02-08 20:11:00"
}

warehouse2 = {
    "id": 2,
    "code": "ABC",
    "name": "ABC",
    "address": "ABC",
    "zip": "ABC",
    "city": "ABC",
    "province": "ABC",
    "country": "ABC",
    "contact": {
        "name": "Fem Keijze",
        "phone": "(078) 001336",
        "email": "blamore@example.ne"
    },
    "created_at": "1983-04-13 04:59:56",
    "updated_at": "2007-02-08 20:11:01"
}

warehouse3 = {
    "id": 3,
    "code": "DWADNL5192",
    "name": "HalloMensen cargo hub",
    "address": "Wijnhaven 107",
    "zip": "4002 AS",
    "city": "Heemskerk",
    "province": "Friesland",
    "country": "NL",
    "contact": {
        "name": "Fem Keijzer",
        "phone": "(078) 0013363",
        "email": "blamore@example.net"
    },
    "created_at": "1983-04-13 04:59:55",
    "updated_at": "2007-02-08 20:11:00"
}

warehouseEmpty = {
    "id": None,
    "code": "",
    "name": "",
    "address": "",
    "zip": "",
    "city": "",
    "province": "",
    "country": "",
    "contact": {
        "name": "",
        "phone": "",
        "email": ""
    },
    "created_at": "",
    "updated_at": ""
}

warehouseCompletelyEmpty = {
}

obj = Warehouses("./CargoHub/data/testdb/test_")

def test_AddWarehouses():
    obj.data = []
    obj.add_warehouse(warehouse1)
    assert len(obj.data) == 1, "Er is geen warehouse toegevoegd / Er is meer dan 1 warehouse in de json. Het aantal warehouses moet 1 zijn, maar is {}".format(len(obj.data))

def test_AddEmptyWarehouse():
    obj.data = []
    obj.add_warehouse(warehouseCompletelyEmpty)
    assert len(obj.data) == 0, "Een warehouse kan niet toegevoegd worden zonder een complete body. Het aantal warehouses moet 0 zijn, maar is {}".format(len(obj.data))

def test_AddIncompleteWarehouse():
    obj.data = []
    obj.add_warehouse(warehouseEmpty)
    assert len(obj.data) == 0, "Een warehouse kan niet toegevoegd worden met body waarbij fields incompleet zijn. Het aantal warehouses moet 0 zijn, maar is {}".format(len(obj.data))

def test_DuplicateWarehouse():
    obj.data = []
    obj.add_warehouse(warehouse1)
    obj.add_warehouse(warehouse1)  # should not add, because it used the same id, code, name and adress
    assert len(obj.data) == 1, "Er mag geen duplicate warehouses zijn. Het aantal warehouses moet 1 zijn, maar is {}".format(len(obj.data))

def test_PartiallyDuplicateWarehouse():
    obj.data = []
    obj.add_warehouse(warehouse1)
    obj.add_warehouse(warehouse3)  # should not add, its already in there
    assert len(obj.data) == 2, "De warehouses mag toegevoegd worden, alleen de id, code, naam en adress zijn anders. Het aantal warehouses moet 2 zijn, maar is {}".format(len(obj.data))


def test_RemoveWarehouses():
    obj.data = []
    obj.add_warehouse(warehouse1)
    length_warehouse_before = len(obj.data)  # should be 1
    obj.remove_warehouse(1)  # uses id 1 for warehouse 1
    assert len(obj.data) == length_warehouse_before - 1, "Er is geen warehouse verwijderd. Het aantal warehouses moet 0 zijn, is {}".format(len(obj.data))

def test_UpdateWarehouses():  # check if each part of the warehouse has updated.
    obj.data = []
    obj.add_warehouse(warehouse1)
    obj.update_warehouse(1, warehouse2)

    updated_warehouse = obj.get_warehouse(2)

    assert updated_warehouse["id"] == 2, "De id zou van 1 naar 2 moeten zijn bijgewerkt, maar het is {}".format(updated_warehouse["id"])
    assert updated_warehouse["code"] == warehouse2["code"], "De code zou moeten zijn bijgewerkt naar '{}', maar het is '{}'".format(warehouse2["code"], updated_warehouse["code"])
    assert updated_warehouse["name"] == warehouse2["name"], "De naam zou moeten zijn bijgewerkt naar '{}', maar het is '{}'".format(warehouse2["name"], updated_warehouse["name"])
    assert updated_warehouse["address"] == warehouse2["address"], "Het adres zou moeten zijn bijgewerkt naar '{}', maar het is '{}'".format(warehouse2["address"], updated_warehouse["address"])
    assert updated_warehouse["zip"] == warehouse2["zip"], "De postcode zou moeten zijn bijgewerkt naar '{}', maar het is '{}'".format(warehouse2["zip"], updated_warehouse["zip"])
    assert updated_warehouse["city"] == warehouse2["city"], "De stad zou moeten zijn bijgewerkt naar '{}', maar het is '{}'".format(warehouse2["city"], updated_warehouse["city"])
    assert updated_warehouse["province"] == warehouse2["province"], "De provincie zou moeten zijn bijgewerkt naar '{}', maar het is '{}'".format(warehouse2["province"], updated_warehouse["province"])
    assert updated_warehouse["country"] == warehouse2["country"], "Het land zou moeten zijn bijgewerkt naar '{}', maar het is '{}'".format(warehouse2["country"], updated_warehouse["country"])
    assert updated_warehouse["contact"] == warehouse2["contact"], "De contactinformatie zou moeten zijn bijgewerkt naar '{}', maar het is '{}'".format(warehouse2["contact"], updated_warehouse["contact"])
    assert updated_warehouse["updated_at"] == warehouse2["updated_at"], "De updated_at timestamp zou moeten zijn veranderd naar '{}', maar het is '{}'".format(warehouse2["updated_at"], updated_warehouse["updated_at"])

def test_GetWarehouse():
    obj.data = []
    obj.add_warehouse(warehouse1)
    result = obj.get_warehouse(1)
    assert result is not None, "Een bestaande warehouse zou je moeten kunnen getten, maar het resultaat is {}".format(result)

def test_GetNonExistentWarehouse():
    obj.data = []
    result = obj.get_warehouse(999)  # Id bestaat niet
    assert result is None, "Een niet-bestaande warehouse zou je niet moeten kunnen getten, maar het resultaat is {}".format(result)

def test_UpdateNonExistentWarehouse():
    obj.data = []
    initial_length = len(obj.data)
    obj.update_warehouse(999, warehouse2)  # Non-existent ID
    assert len(obj.data) == initial_length, "Het aantal warehouses zou gelijk moeten blijven na het bijwerken van een niet-bestaande warehouse. Het aantal warehouses is {}".format(len(obj.data))

def test_RemoveNonExistentWarehouse():
    obj.data = []
    obj.remove_warehouse(1)  # Non-existent ID
    assert len(obj.data) == 0, "Het aantal warehouses zou gelijk moeten blijven na het verwijderen van een niet-bestaande warehouse. Het aantal warehouses moet 0 zijn, maar het is {}".format(len(obj.data))

def test_UpdateWarehouseWithIncompleteWarehouse():
    obj.data = []
    obj.add_warehouse(warehouse1)
    original_warehouse = obj.get_warehouse(1)
    obj.update_warehouse(1, warehouseEmpty)
    assert original_warehouse == obj.get_warehouse(1), "De warehouse zou niet veranderd moeten zijn, maar toch zijn er onderdelen geupdate."

# test of elk onderdeel van de warehouse valid is, zoals een telefoon nummer is ook echt een telefoonnummer etc