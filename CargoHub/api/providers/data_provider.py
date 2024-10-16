from Services.Service_warehouses import ServiceWarehouses
from Services.Service_locations import ServiceLocations
from Services.Service_transfers import ServiceTransfers
from Services.Service_items import ServiceItems
from Services.Service_item_lines import ServiceItemLines
from Services.Service_item_groups import ServiceItemGroups
from Services.Service_item_types import ServiceItemTypes
from Services.Service_Inventories import ServiceInventories
from Services.Service_suppliers import ServiceSuppliers
from Services.Service_Orders import ServiceOrders
from Services.Service_Clients import ServiceClients
from Services.Service_shipments import ServiceShipments

DEBUG = False

ROOT_PATH = "./CargoHub/data/"

_warehouses = None
_locations = None
_transfers = None
_items = None
_item_lines = None
_item_groups = None
_item_types = None
_inventories = None
_suppliers = None
_orders = None
_shipments = None
_clients = None


def init():
    global _warehouses
    _warehouses = ServiceWarehouses(ROOT_PATH, DEBUG)
    global _locations
    _locations = ServiceLocations(ROOT_PATH, DEBUG)
    global _transfers
    _transfers = ServiceTransfers(ROOT_PATH, DEBUG)
    global _items
    _items = ServiceItems(ROOT_PATH, DEBUG)
    global _item_lines
    _item_lines = ServiceItemLines(ROOT_PATH, DEBUG)
    global _item_groups
    _item_groups = ServiceItemGroups(ROOT_PATH, DEBUG)
    global _item_types
    _item_types = ServiceItemTypes(ROOT_PATH, DEBUG)
    global _inventories
    _inventories = ServiceInventories(ROOT_PATH, DEBUG)
    global _suppliers
    _suppliers = ServiceSuppliers(ROOT_PATH, DEBUG)
    global _orders
    _orders = ServiceOrders(ROOT_PATH, DEBUG)
    global _clients
    _clients = ServiceClients(ROOT_PATH, DEBUG)
    global _shipments
    _shipments = ServiceShipments(ROOT_PATH, DEBUG)


def fetch_warehouse_pool():
    return _warehouses


def fetch_location_pool():
    return _locations


def fetch_transfer_pool():
    return _transfers


def fetch_item_pool():
    return _items


def fetch_item_line_pool():
    return _item_lines


def fetch_item_group_pool():
    return _item_groups


def fetch_item_type_pool():
    return _item_types


def fetch_inventory_pool():
    return _inventories


def fetch_supplier_pool():
    return _suppliers


def fetch_order_pool():
    return _orders


def fetch_client_pool():
    return _clients


def fetch_shipment_pool():
    return _shipments
