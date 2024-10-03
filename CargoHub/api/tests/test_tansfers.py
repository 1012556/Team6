from models.transfers import Transfers


transferlist = [
    {
        "id": 1,
        "reference": "TR00001",
        "transfer_from": None,
        "transfer_to": 9229,
        "transfer_status": "Completed",
        "created_at": "2000-03-11T13:11:14Z",
        "updated_at": "2000-03-12T16:11:14Z",
        "items": [
            {
                "item_id": "P007435",
                "amount": 23
            }
        ]
    },
    {
        "id": 2,
        "reference": "TR00002",
        "transfer_from": 9229,
        "transfer_to": 9284,
        "transfer_status": "Completed",
        "created_at": "2017-09-19T00:33:14Z",
        "updated_at": "2017-09-20T01:33:14Z",
        "items": [
            {
                "item_id": "P007435",
                "amount": 23
            }
        ]
    }
   ]

transfertoupdate =  {
        "id": 3,
        "reference": "TR00003",
        "transfer_from": None,
        "transfer_to": 9199,
        "transfer_status": "Completed",
        "created_at": "2000-03-11T13:11:14Z",
        "updated_at": "2000-03-12T14:11:14Z",
        "items": [
            {
                "item_id": "P009557",
                "amount": 1
            }
        ]
    }


emptytransfer = {}

obj = Transfers("./CargoHub/data/testdb/test_")

def addtransfers():
    obj.data = []
    for x in transferlist:
        obj.add_transfer(x)

def test_addvalidtransfers():
    addtransfers()
    assert len(obj.data) == len(transferlist)
    assert obj.data[0]["transfer_status"] == "Scheduled"
    assert obj.data[1]["transfer_status"] == "Scheduled"

def test_gettransfers():
    addtransfers()
    assert len(obj.get_transfers()) == len(transferlist)

def test_gettransfer():
    addtransfers()
    data = obj.get_transfer(1)
    assert data == transferlist[0]

def test_getinvalidtransfer():
    addtransfers()
    data = obj.get_transfer((len(transferlist) + 1))
    assert data == None


def test_addemptytransfers():
    addtransfers()
    obj.add_transfer(emptytransfer)
    assert len(obj.data) == len(transferlist) # geen check voor lege dict

def test_updatetransfer():
    addtransfers()
    obj.update_transfer(2, transfertoupdate)
    assert obj.get_transfer(2)["id"] == 2 # update id niet automatisch

def test_invalidupdateinvalid():
    addtransfers()
    obj.update_transfer((len(transferlist) + 1), transfertoupdate)
    assert len(obj.data) == len(transferlist)
    assert obj.get_transfer((len(transferlist) + 1)) == None

def test_removetransfer():
    addtransfers()
    obj.remove_transfer(2)
    assert len(obj.data) == len(transferlist) - 1

def test_removeinvalidtransfer():
    addtransfers()
    obj.remove_transfer(len(transferlist) + 1)
    assert len(obj.data) == len(transferlist)

def test_dbload():
    addtransfers()
    obj.load(False)
    assert len(obj.data) == len(transferlist)

def test_dbsave():
    addtransfers()
    obj.save()
    obj.data = []
    obj.load(False)

    assert len(obj.data) == len(transferlist)

def test_items_transfer():
    addtransfers()
    data = obj.get_items_in_transfer(1)
    assert data == transferlist[0]["items"]

def test_items_invalidtransfer():
    addtransfers()
    data = obj.get_items_in_transfer(4)
    assert data == None





    