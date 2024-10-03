from models.item_groups import ItemGroups


itemgrouplist = [{
        "id": 1,
        "name": "Furniture",
        "description": "",
        "created_at": "2019-09-22 15:51:07",
        "updated_at": "2022-05-18 13:49:28"
    },
    {
        "id": 2,
        "name": "Stationery",
        "description": "",
        "created_at": "1999-08-14 13:39:27",
        "updated_at": "2011-06-16 05:00:47"
    }]

itemgrouptoupdate =    {
        "id": 3,
        "name": "Clothing",
        "description": "",
        "created_at": "1975-12-14 06:58:09",
        "updated_at": "2011-12-04 21:16:55"
    }


emptyitemgroup = {}

obj = ItemGroups("./CargoHub/data/testdb/test_")

def additemgroups():
    obj.data = []
    for x in itemgrouplist:
        obj.add_item_group(x)

def test_addvaliditemgroups():
    additemgroups()
    assert len(obj.data) == len(itemgrouplist)

def test_getitemgroups():
    additemgroups()
    assert len(obj.get_item_groups()) == len(itemgrouplist)

def test_getitemgroup():
    additemgroups()
    data = obj.get_item_group(2)
    assert data == itemgrouplist[1]

def test_getinvaliditemgroups():
    additemgroups()
    data = obj.get_item_group((len(itemgrouplist) + 1))
    assert data == None


def test_addemptyitemgroups():
    additemgroups()
    obj.add_item_group(emptyitemgroup)
    assert len(obj.data) == len(itemgrouplist) # geen check voor lege dict

def test_updateitemgroup():
    additemgroups()
    obj.update_item_group(2, itemgrouptoupdate)
    assert obj.get_item_group(2)["id"] == 2 # update id niet automatisch

def test_updateinvalid():
    additemgroups()
    obj.update_item_group((len(itemgrouplist) + 1), itemgrouptoupdate)
    assert len(obj.data) == len(itemgrouplist)
    assert obj.get_item_group((len(itemgrouplist) + 1)) == None

def test_removeitemgroup():
    additemgroups()
    obj.remove_item_group(2)
    assert len(obj.data) == len(itemgrouplist) - 1

def test_removeinvaliditemgroup():
    additemgroups()
    obj.remove_item_group(len(itemgrouplist) + 1)
    assert len(obj.data) == len(itemgrouplist)

def test_dbload():
    additemgroups()
    obj.load(False)
    assert len(obj.data) == len(itemgrouplist)

def test_dbsave():
    additemgroups()
    obj.save()
    obj.data = []
    obj.load(False)

    assert len(obj.data) == len(itemgrouplist)



    