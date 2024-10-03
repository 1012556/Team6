from models.item_types import ItemTypes


itemtypelist = [{
        "id": 1,
        "name": "Desktop",
        "description": "",
        "created_at": "1993-07-28 13:43:32",
        "updated_at": "2022-05-12 08:54:35"
    },
    {
        "id": 2,
        "name": "Tablet",
        "description": "",
        "created_at": "1977-05-01 00:05:04",
        "updated_at": "2001-04-14 02:41:59"
    }
   ]

itemtypetoupdate =         {
        "id": 3,
        "name": "Smartphone",
        "description": "",
        "created_at": "2014-08-23 03:26:57",
        "updated_at": "2017-09-20 11:51:15"
    }


emptyitemtype = {}

obj = ItemTypes("./CargoHub/data/testdb/test_")

def additemtypes():
    obj.data = []
    for x in itemtypelist:
        obj.add_item_type(x)

def test_addvaliditemtypes():
    additemtypes()
    assert len(obj.data) == len(itemtypelist)

def test_getitemtypes():
    additemtypes()
    assert len(obj.get_item_types()) == len(itemtypelist)

def test_getitemtype():
    additemtypes()
    data = obj.get_item_type(2)
    assert data == itemtypelist[1]

def test_getinvaliditemtype():
    additemtypes()
    data = obj.get_item_type((len(itemtypelist) + 1))
    assert data == None


def test_addemptyitemtypes():
    additemtypes()
    obj.add_item_type(emptyitemtype)
    assert len(obj.data) == len(itemtypelist) # geen check voor lege dict

def test_updateitemtype():
    additemtypes()
    obj.update_item_type(2, itemtypetoupdate)
    assert obj.get_item_type(2)["id"] == 2 # update id niet automatisch

def test_invalidupdateinvalid():
    additemtypes()
    obj.update_item_type((len(itemtypelist) + 1), itemtypetoupdate)
    assert len(obj.data) == len(itemtypelist)
    assert obj.get_item_type((len(itemtypelist) + 1)) == None

def test_removeitemtype():
    additemtypes()
    obj.remove_item_type(2)
    assert len(obj.data) == len(itemtypelist) - 1

def test_removeinvaliditemtype():
    additemtypes()
    obj.remove_item_type(len(itemtypelist) + 1)
    assert len(obj.data) == len(itemtypelist)

def test_dbload():
    additemtypes()
    obj.load(False)
    assert len(obj.data) == len(itemtypelist)

def test_dbsave():
    additemtypes()
    obj.save()
    obj.data = []
    obj.load(False)

    assert len(obj.data) == len(itemtypelist)



    