from models.locations import Locations

locations = [{
        "id": 1,
        "warehouse_id": 1,
        "code": "C.9.2",
        "name": "Row: C, Rack: 9, Shelf: 1"
        }, 
        {
        "id": 2,
        "warehouse_id": 1,
        "code": "C.9.2",
        "name": "Row: C, Rack: 9, Shelf: 2"
}]

locationtoupdate = {
        "id": 3,
        "warehouse_id": 1,
        "code": "C.9.2",
        "name": "Row: C, Rack: 9, Shelf: 3"
}


emptylocation = {}

obj = Locations("./CargoHub/data/test_")

def addlocations():
    obj.data = []
    for x in locations:
        obj.add_location(x)

def test_addvalidlocations():
    addlocations()
    assert len(obj.data) == 2

def test_getlocation():
    addlocations()
    data = obj.get_location(2)
    assert data["id"] == 2

def test_getinvalidlocation():
    addlocations()
    data = obj.get_location(3)
    assert data == None

def test_addemptylocations():
    addlocations()
    obj.add_location(emptylocation)
    assert len(obj.data) == 2 # geen check voor lege dict

def test_updatelocation():
    addlocations()
    obj.update_location(2, locationtoupdate)
    assert obj.get_location(2)["id"] == 2 # update id niet automatisch

def test_invalidupdateinvalid():
    addlocations()
    obj.update_location(3, locationtoupdate)
    assert len(obj.data) == 2
    assert obj.get_location(3) == None

def test_removelocation():
    addlocations()
    obj.remove_location(2)
    assert len(obj.data) == 1

def test_removeinvalidlocation():
    addlocations()
    obj.remove_location(3)
    assert len(obj.data) == 2

def test_getlocationswarehouse():
    addlocations()
    data = obj.get_locations_in_warehouse(1)
    assert len(data) == 2

def test_getinvalidlocationwarehouse():
    addlocations()
    data = obj.get_locations_in_warehouse(2)
    assert len(data) == 0

def test_dbload():
    addlocations()
    obj.load(False)
    assert len(obj.data) == 2

def test_dbsave():
    addlocations()
    obj.save()
    obj.data = []
    obj.load(False)

    assert len(obj.data) == 2



    