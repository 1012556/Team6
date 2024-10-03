from models.suppliers import Suppliers


supplierlist = [
    {
        "id": 1,
        "code": "SUP0001",
        "name": "Lee, Parks and Johnson",
        "address": "5989 Sullivan Drives",
        "address_extra": "Apt. 996",
        "city": "Port Anitaburgh",
        "zip_code": "91688",
        "province": "Illinois",
        "country": "Czech Republic",
        "contact_name": "Toni Barnett",
        "phonenumber": "363.541.7282x36825",
        "reference": "LPaJ-SUP0001",
        "created_at": "1971-10-20 18:06:17",
        "updated_at": "1985-06-08 00:13:46"
    },
    {
        "id": 2,
        "code": "SUP0002",
        "name": "Holden-Quinn",
        "address": "576 Christopher Roads",
        "address_extra": "Suite 072",
        "city": "Amberbury",
        "zip_code": "16105",
        "province": "Illinois",
        "country": "Saint Martin",
        "contact_name": "Kathleen Vincent",
        "phonenumber": "001-733-291-8848x3542",
        "reference": "H-SUP0002",
        "created_at": "1995-12-18 03:05:46",
        "updated_at": "2019-11-10 22:11:12"
    }
   ]

suppliertoupdate =   {
        "id": 3,
        "code": "SUP0003",
        "name": "White and Sons",
        "address": "1761 Shepard Valley",
        "address_extra": "Suite 853",
        "city": "Aguilarton",
        "zip_code": "63918",
        "province": "Wyoming",
        "country": "Ghana",
        "contact_name": "Jason Hudson",
        "phonenumber": "001-910-585-6962x8307",
        "reference": "WaS-SUP0003",
        "created_at": "2010-06-14 02:32:58",
        "updated_at": "2019-06-16 19:29:49"
    }


emptysupplier = {}

obj = Suppliers("./CargoHub/data/testdb/test_")

def addsuppliers():
    obj.data = []
    for x in supplierlist:
        obj.add_supplier(x)

def test_addvalidsuppliers():
    addsuppliers()
    assert len(obj.data) == len(supplierlist)

def test_getsuppliers():
    addsuppliers()
    assert len(obj.get_suppliers()) == len(supplierlist)

def test_getsupplier():
    addsuppliers()
    data = obj.get_supplier(2)
    assert data == supplierlist[1]

def test_getinvalidsupplier():
    addsuppliers()
    data = obj.get_supplier((len(supplierlist) + 1))
    assert data == None


def test_addemptysuppliers():
    addsuppliers()
    obj.add_supplier(emptysupplier)
    assert len(obj.data) == len(supplierlist) # geen check voor lege dict

def test_updatesupplier():
    addsuppliers()
    obj.update_supplier(2, suppliertoupdate)
    assert obj.get_supplier(2)["id"] == 2 # update id niet automatisch

def test_invalidupdatesupplier():
    addsuppliers()
    obj.update_supplier((3), suppliertoupdate)
    assert len(obj.data) == len(supplierlist) # update timestamp pas doen als de supplier is gevonden

def test_removesupplier():
    addsuppliers()
    obj.remove_supplier(2)
    assert len(obj.data) == len(supplierlist) - 1

def test_removeinvalidsupplier():
    addsuppliers()
    obj.remove_supplier(len(supplierlist) + 1)
    assert len(obj.data) == len(supplierlist)

def test_dbload():
    addsuppliers()
    obj.load(False)
    assert len(obj.data) == len(supplierlist)

def test_dbsave():
    addsuppliers()
    obj.save()
    obj.data = []
    obj.load(False)

    assert len(obj.data) == len(supplierlist)