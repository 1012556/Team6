from models.items import Items


itemlist = [
    {
        "uid": "P000001",
        "code": "sjQ23408K",
        "description": "Face-to-face clear-thinking complexity",
        "short_description": "must",
        "upc_code": "6523540947122",
        "model_number": "63-OFFTq0T",
        "commodity_code": "oTo304",
        "item_line": 11,
        "item_group": 73,
        "item_type": 14,
        "unit_purchase_quantity": 47,
        "unit_order_quantity": 13,
        "pack_order_quantity": 11,
        "supplier_id": 34,
        "supplier_code": "SUP423",
        "supplier_part_number": "E-86805-uTM",
        "created_at": "2015-02-19 16:08:24",
        "updated_at": "2015-09-26 06:37:56"
    },
    {
        "uid": "P000002",
        "code": "nyg48736S",
        "description": "Focused transitional alliance",
        "short_description": "may",
        "upc_code": "9733132830047",
        "model_number": "ck-109684-VFb",
        "commodity_code": "y-20588-owy",
        "item_line": 69,
        "item_group": 85,
        "item_type": 39,
        "unit_purchase_quantity": 10,
        "unit_order_quantity": 15,
        "pack_order_quantity": 23,
        "supplier_id": 57,
        "supplier_code": "SUP312",
        "supplier_part_number": "j-10730-ESk",
        "created_at": "2020-05-31 16:00:08",
        "updated_at": "2020-11-08 12:49:21"
    }
   ]

itemtoupdate =  { 
        
        "uid": "P000003",
        "code": "QVm03739H",
        "description": "Cloned actuating artificial intelligence",
        "short_description": "we",
        "upc_code": "3722576017240",
        "model_number": "aHx-68Q4",
        "commodity_code": "t-541-F0g",
        "item_line": 54,
        "item_group": 88,
        "item_type": 42,
        "unit_purchase_quantity": 30,
        "unit_order_quantity": 17,
        "pack_order_quantity": 11,
        "supplier_id": 2,
        "supplier_code": "SUP237",
        "supplier_part_number": "r-920-z2C",
        "created_at": "1994-06-02 06:38:40",
        "updated_at": "1999-10-13 01:10:32"
    }


emptyitem = {}

obj = Items("./CargoHub/data/testdb/test_")

def additems():
    obj.data = []
    for x in itemlist:
        obj.add_item(x)

def test_addvaliditems():
    additems()
    assert len(obj.data) == len(itemlist)

def test_getitems():
    additems()
    assert len(obj.get_items()) == len(itemlist)

def test_getitem():
    additems()
    data = obj.get_item("P000002")
    assert data == itemlist[1]

def test_getinvaliditem():
    additems()
    data = obj.get_item((len(itemlist) + 1))
    assert data == None


def test_addemptyitems():
    additems()
    obj.add_item(emptyitem)
    assert len(obj.data) == len(itemlist) # geen check voor lege dict

def test_updateitem():
    additems()
    obj.update_item("P000002", itemtoupdate)
    assert obj.get_item("P000002")["uid"] == "P000002" # update id niet automatisch

def test_invalidupdateinvalid():
    additems()
    obj.update_item((len(itemlist) + 1), itemtoupdate)
    assert len(obj.data) == len(itemlist)
    assert obj.get_item((len(itemlist) + 1)) == None

def test_removeitem():
    additems()
    obj.remove_item("P000002")
    assert len(obj.data) == len(itemlist) - 1

def test_removeinvaliditem():
    additems()
    obj.remove_item(len(itemlist) + 1)
    assert len(obj.data) == len(itemlist)

def test_dbload():
    additems()
    obj.load(False)
    assert len(obj.data) == len(itemlist)

def test_dbsave():
    additems()
    obj.save()
    obj.data = []
    obj.load(False)

    assert len(obj.data) == len(itemlist)

def test_getitems_foritemline():
    additems()
    data = obj.get_items_for_item_line(11)
    assert data[0] == itemlist[0]

def test_invalid_getitems_foritemline():
    additems()
    data = obj.get_items_for_item_line(1)
    assert data == [] # error toevoegen?

def test_getitems_foritemgroup():
    additems()
    data = obj.get_items_for_item_group(73)
    assert data[0] == itemlist[0]

def test_invalid_getitems_foritemgroup():
    additems()
    data = obj.get_items_for_item_group(1)
    assert data == [] # error toevoegen?

def test_getitems_foritemtype():
    additems()
    data = obj.get_items_for_item_type(14)
    assert data[0] == itemlist[0]

def test_invalid_getitems_foritemtype():
    additems()
    data = obj.get_items_for_item_type(1)
    assert data == [] # error toevoegen?

def test_getitems_forsupplier():
    additems()
    data = obj.get_items_for_supplier(34)
    assert data[0] == itemlist[0]

def test_invalid_getitems_forsupplier():
    additems()
    data = obj.get_items_for_supplier(1)
    assert data == [] # error toevoegen?



    