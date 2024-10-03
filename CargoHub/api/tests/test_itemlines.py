from models.item_lines import ItemLines


itemlinelist = [{
        "id": 1,
        "name": "Home Appliances",
        "description": "",
        "created_at": "1979-01-16 07:07:50",
        "updated_at": "2024-01-05 23:53:25"
    },
    {
        "id": 2,
        "name": "Office Supplies",
        "description": "",
        "created_at": "2009-07-18 08:13:40",
        "updated_at": "2020-01-12 14:32:49"
    }]

itemlinetoupdate =        {
        "id": 3,
        "name": "Fashion",
        "description": "",
        "created_at": "1990-01-04 22:40:49",
        "updated_at": "2003-05-17 08:21:43"
    }


emptyitemline = {}

obj = ItemLines("./CargoHub/data/testdb/test_")

def additemlines():
    obj.data = []
    for x in itemlinelist:
        obj.add_item_line(x)

def test_addvaliditemlines():
    additemlines()
    assert len(obj.data) == len(itemlinelist)

def test_getitemlines():
    additemlines()
    assert len(obj.get_item_lines()) == len(itemlinelist)

def test_getitemline():
    additemlines()
    data = obj.get_item_line(2)
    assert data == itemlinelist[1]

def test_getinvaliditemline():
    additemlines()
    data = obj.get_item_line((len(itemlinelist) + 1))
    assert data == None


def test_addemptyitemlines():
    additemlines()
    obj.add_item_line(emptyitemline)
    assert len(obj.data) == len(itemlinelist) # geen check voor lege dict

def test_updateitemline():
    additemlines()
    obj.update_item_line(2, itemlinetoupdate)
    assert obj.get_item_line(2)["id"] == 2 # update id niet automatisch

def test_invalidupdateinvalid():
    additemlines()
    obj.update_item_line((len(itemlinelist) + 1), itemlinetoupdate)
    assert len(obj.data) == len(itemlinelist)
    assert obj.get_item_line((len(itemlinelist) + 1)) == None

def test_removeitemline():
    additemlines()
    obj.remove_item_line(2)
    assert len(obj.data) == len(itemlinelist) - 1

def test_removeinvaliditemline():
    additemlines()
    obj.remove_item_line(len(itemlinelist) + 1)
    assert len(obj.data) == len(itemlinelist)

def test_dbload():
    additemlines()
    obj.load(False)
    assert len(obj.data) == len(itemlinelist)

def test_dbsave():
    additemlines()
    obj.save()
    obj.data = []
    obj.load(False)

    assert len(obj.data) == len(itemlinelist)



    