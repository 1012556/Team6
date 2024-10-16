from datetime import datetime
from pydantic import BaseModel

class Item_types(BaseModel):
    def __init__(self, id, name, description="", created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

class Clients(BaseModel):
    def __init__(self, id, name, address, city, zip_code, province, country, contact_name, contact_phone, contact_email, created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.province = province
        self.country = country
        self.contact_name = contact_name
        self.contact_phone = contact_phone
        self.contact_email = contact_email
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()


class Inventory(BaseModel):
    def __init__(self, id, item_id, description, item_reference, locations, total_on_hand, total_expected, total_ordered, total_allocated, total_available, created_at=None, updated_at=None):
        self.id = id
        self.item_id = item_id
        self.description = description
        self.item_reference = item_reference
        self.locations = locations
        self.total_on_hand = total_on_hand
        self.total_expected = total_expected
        self.total_ordered = total_ordered
        self.total_allocated = total_allocated
        self.total_available = total_available
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

class ItemGroup(BaseModel):
    def __init__(self, id, name, description="", created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

class ItemLine(BaseModel):
    def __init__(self, id, name, description="", created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

class Item(BaseModel):
    def __init__(self, uid, code, description, short_description, upc_code, model_number, commodity_code, item_line, item_group, item_type, unit_purchase_quantity, unit_order_quantity, pack_order_quantity, supplier_id, supplier_code, supplier_part_number, created_at=None, updated_at=None):
        self.uid = uid
        self.code = code
        self.description = description
        self.short_description = short_description
        self.upc_code = upc_code
        self.model_number = model_number
        self.commodity_code = commodity_code
        self.item_line = item_line
        self.item_group = item_group
        self.item_type = item_type
        self.unit_purchase_quantity = unit_purchase_quantity
        self.unit_order_quantity = unit_order_quantity
        self.pack_order_quantity = pack_order_quantity
        self.supplier_id = supplier_id
        self.supplier_code = supplier_code
        self.supplier_part_number = supplier_part_number
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

class Location(BaseModel):
    id: int
    warehouse_id: int
    code: str
    name: str
    created_at: str
    updated_at: str

class Order(BaseModel):
    def __init__(self, id, source_id, order_date, request_date, reference, reference_extra, order_status, notes, shipping_notes, picking_notes, warehouse_id, ship_to, bill_to, shipment_id, total_amount, total_discount, total_tax, total_surcharge, items, created_at=None, updated_at=None):
        self.id = id
        self.source_id = source_id
        self.order_date = order_date
        self.request_date = request_date
        self.reference = reference
        self.reference_extra = reference_extra
        self.order_status = order_status
        self.notes = notes
        self.shipping_notes = shipping_notes
        self.picking_notes = picking_notes
        self.warehouse_id = warehouse_id
        self.ship_to = ship_to
        self.bill_to = bill_to
        self.shipment_id = shipment_id
        self.total_amount = total_amount
        self.total_discount = total_discount
        self.total_tax = total_tax
        self.total_surcharge = total_surcharge
        self.items = items
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

class Shipment(BaseModel):
    def __init__(self, id, order_id, source_id, order_date, request_date, shipment_date, shipment_type, shipment_status, notes, carrier_code, carrier_description, service_code, payment_type, transfer_mode, total_package_count, total_package_weight, created_at=None, updated_at=None, items=None):
        self.id = id
        self.order_id = order_id
        self.source_id = source_id
        self.order_date = order_date
        self.request_date = request_date
        self.shipment_date = shipment_date
        self.shipment_type = shipment_type
        self.shipment_status = shipment_status
        self.notes = notes
        self.carrier_code = carrier_code
        self.carrier_description = carrier_description
        self.service_code = service_code
        self.payment_type = payment_type
        self.transfer_mode = transfer_mode
        self.total_package_count = total_package_count
        self.total_package_weight = total_package_weight
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        self.items = items or []

class Supplier(BaseModel):
    def __init__(self, id, code, name, address, address_extra, city, zip_code, province, country, contact_name, phonenumber, reference, created_at=None, updated_at=None):
        self.id = id
        self.code = code
        self.name = name
        self.address = address
        self.address_extra = address_extra
        self.city = city
        self.zip_code = zip_code
        self.province = province
        self.country = country
        self.contact_name = contact_name
        self.phonenumber = phonenumber
        self.reference = reference
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

class Transfer(BaseModel):
    def __init__(self, id, reference, transfer_from, transfer_to, transfer_status, created_at=None, updated_at=None, items=None):
        self.id = id
        self.reference = reference
        self.transfer_from = transfer_from
        self.transfer_to = transfer_to
        self.transfer_status = transfer_status
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        self.items = items or []

class Warehouse(BaseModel):
    name: str
    address: str
    zip: str
    city: str
    province: str
    country: str
    contact: dict
    created_at: str
    updated_at: str