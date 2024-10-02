from models.inventories import Inventories


Inventorylist = [{
        "id": 1,
        "item_id": "P000001",
        "description": "Face-to-face clear-thinking complexity",
        "item_reference": "sjQ23408K",
        "locations": [
            3211,
            24700,
            14123,
            19538,
            31071,
            24701,
            11606,
            11817
        ],
        "total_on_hand": 262,
        "total_expected": 0,
        "total_ordered": 80,
        "total_allocated": 41,
        "total_available": 141,
        "created_at": "2015-02-19 16:08:24",
        "updated_at": "2015-09-26 06:37:56"
    },
    {
        "id": 2,
        "item_id": "P000002",
        "description": "Focused transitional alliance",
        "item_reference": "nyg48736S",
        "locations": [
            19800,
            23653,
            3068,
            3334,
            20477,
            20524,
            17579,
            2271,
            2293,
            22717
        ],
        "total_on_hand": 194,
        "total_expected": 0,
        "total_ordered": 139,
        "total_allocated": 0,
        "total_available": 55,
        "created_at": "2020-05-31 16:00:08",
        "updated_at": "2020-11-08 12:49:21"
    }, 
    {
        "id": 3,
        "item_id": "P000002",
        "description": "Focused transitional alliance",
        "item_reference": "nyg48736S",
        "locations": [
            19800,
            23653,
            3068,
            3334,
            20477,
            20524,
            17579,
            2271,
            2293,
            22717
        ],
        "total_on_hand": 194,
        "total_expected": 0,
        "total_ordered": 139,
        "total_allocated": 0,
        "total_available": 55,
        "created_at": "2020-05-31 16:00:08",
        "updated_at": "2020-11-08 12:49:21"
    }]

inventorytoupdate = {
        "id": 3,
        "item_id": "P000003",
        "description": "Cloned actuating artificial intelligence",
        "item_reference": "QVm03739H",
        "locations": [
            5321,
            21960
        ],
        "total_on_hand": 24,
        "total_expected": 0,
        "total_ordered": 90,
        "total_allocated": 68,
        "total_available": -134,
        "created_at": "1994-06-02 06:38:40",
        "updated_at": "1999-10-13 01:10:32"
    }


emptyinventory = {}

obj = Inventories("./CargoHub/data/test_")

def addinventories():
    obj.data = []
    for x in Inventorylist:
        obj.add_inventory(x)

def test_addvalidinventories():
    addinventories()
    assert len(obj.data) == len(Inventorylist)

def test_getinventories():
    addinventories()
    assert len(obj.get_inventories()) == len(Inventorylist)

def test_getinventoriesitem():
    addinventories()
    assert len(obj.get_inventories_for_item("P000001")) == 1

def test_getmultipleinventoriesitem():
    addinventories()
    assert len(obj.get_inventories_for_item("P000002")) == 2

def test_getinvalidinventoriesitem():
    addinventories()
    assert len(obj.get_inventories_for_item("P000003")) == 0

def test_totalsitems():
    addinventories()
    data = obj.get_inventory_totals_for_item("P000001")
    assert data["total_expected"] == 0
    assert data["total_ordered"] == 80
    assert data["total_allocated"] == 41
    assert data["total_available"] == 141

def test_totalmultipleitems():
    addinventories()
    data = obj.get_inventory_totals_for_item("P000002")
    assert data["total_expected"] == 0
    assert data["total_ordered"] == 139 *2
    assert data["total_allocated"] == 0 * 2
    assert data["total_available"] == 55 * 2

def test_totalsinvaliditems():
    addinventories()
    data = obj.get_inventory_totals_for_item("P000003")
    assert data["total_expected"] == 0
    assert data["total_ordered"] == 0
    assert data["total_allocated"] == 0
    assert data["total_available"] == 0

def test_getiventory():
    addinventories()
    data = obj.get_inventory(2)
    assert data == Inventorylist[1]

def test_getinvalidinventories():
    addinventories()
    data = obj.get_inventory((len(Inventorylist) + 1))
    assert data == None


def test_addemptyinventories():
    addinventories()
    obj.add_inventory(emptyinventory)
    assert len(obj.data) == len(Inventorylist) # geen check voor lege dict

def test_updateinventory():
    addinventories()
    obj.update_inventory(2, inventorytoupdate)
    assert obj.get_inventory(2) == inventorytoupdate # update id niet automatisch

def test_invalidupdateinvalid():
    addinventories()
    obj.update_inventory((len(Inventorylist) + 1), inventorytoupdate)
    assert len(obj.data) == len(Inventorylist)
    assert obj.get_inventory((len(Inventorylist) + 1)) == None

def test_removeinventory():
    addinventories()
    obj.remove_inventory(2)
    assert len(obj.data) == len(Inventorylist) - 1

def test_removeinvalidinventory():
    addinventories()
    obj.remove_inventory(len(Inventorylist) + 1)
    assert len(obj.data) == len(Inventorylist)

def test_dbload():
    addinventories()
    obj.load(False)
    assert len(obj.data) == len(Inventorylist)

def test_dbsave():
    addinventories()
    obj.save()
    obj.data = []
    obj.load(False)

    assert len(obj.data) == len(Inventorylist)



    