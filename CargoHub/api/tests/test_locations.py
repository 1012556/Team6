from CargoHub.api.Services.Service_locations import ServiceLocations

location1 = {
        "id": 1,
        "warehouse_id": 1,
        "code": "C.9.2",
        "name": "Row: C, Rack: 9, Shelf: 1"
        }

location2 = {
        "id": 2,
        "warehouse_id": 1,
        "code": "C.9.2",
        "name": "Row: C, Rack: 9, Shelf: 2"
}

locationtoupdate = {
        "id": 3,
        "warehouse_id": 1,
        "code": "C.9.2",
        "name": "Row: C, Rack: 9, Shelf: 3"
}


emptylocation = {}

obj = Locations("./CargoHub/data/test_")

def addlocations():
    obj.add_location(location1)
    obj.add_location(location2)

def test_addvalidlocations():
    obj.data = []
    addlocations()
    assert len(obj.data) == 2

def test_getlocation():
    obj.data = []
    addlocations()
    data = obj.get_location(2)
    assert data["id"] == 2

def test_addemptylocations():
    obj.data = []
    addlocations()
    obj.add_location(emptylocation)
    assert len(obj.data) == 2 # geen check voor lege dict

def test_updatelocation():
    obj.data = []
    addlocations()
    obj.update_location(2, locationtoupdate)
    assert obj.get_location(2)["id"] == 2 # update id niet automatisch

def test_removelocation():
    obj.data = []
    addlocations()
    obj.remove_location(2)
    assert len(obj.data) == 1

def test_getlocationswarehouse():
    obj.data = []
    addlocations()
    data = obj.get_locations_in_warehouse(1)
    assert len(data) == 2

def test_dbload():
    obj.data = []
    addlocations()
    obj.load(False)
    assert len(obj.data) == 2

def test_dbsave():
    obj.data = []
    addlocations()
    obj.save()
    obj.data = []
    obj.load(False)

    assert len(obj.data) == 2



    