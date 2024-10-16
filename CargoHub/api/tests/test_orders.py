import pytest
from unittest.mock import patch
from models.orders import Orders

order1 = {
        "id": 9876,
        "source_id": 33,
        "order_date": "2019-04-03T11:33:15Z",
        "request_date": "2019-04-07T11:33:15Z",
        "reference": "ORD00001",
        "reference_extra": "Bedreven arm straffen bureau.",
        "order_status": "Delivered",
        "notes": "Voedsel vijf vork heel.",
        "shipping_notes": "Buurman betalen plaats bewolkt.",
        "picking_notes": "Ademen fijn volgorde scherp aardappel op leren.",
        "warehouse_id": 18,
        "ship_to": 1,
        "bill_to": 3,
        "shipment_id": 1,
        "total_amount": 9905.13,
        "total_discount": 150.77,
        "total_tax": 372.72,
        "total_surcharge": 77.6,
        "created_at": "2019-04-03T11:33:15Z",
        "updated_at": None,
        "items": [
            {"item_id": "P007435", "amount": 23},
            {"item_id": "P009557", "amount": 1},
            {"item_id": "P009553", "amount": 50},
            {"item_id": "P010015", "amount": 16},
            {"item_id": "P002084", "amount": 33},
            {"item_id": "P009663", "amount": 18},
            {"item_id": "P010125", "amount": 18},
            {"item_id": "P005768", "amount": 26},
            {"item_id": "P004051", "amount": 1},
            {"item_id": "P005026", "amount": 29},
            {"item_id": "P000726", "amount": 22},
            {"item_id": "P008107", "amount": 47},
            {"item_id": "P001598", "amount": 32},
            {"item_id": "P002855", "amount": 20},
            {"item_id": "P010404", "amount": 30},
            {"item_id": "P010446", "amount": 6},
            {"item_id": "P001517", "amount": 9},
            {"item_id": "P009265", "amount": 2},
            {"item_id": "P001108", "amount": 20},
            {"item_id": "P009110", "amount": 18},
            {"item_id": "P009686", "amount": 13}
        ]
        }


order2 = {
        "id": 9876,
        "source_id": 12,
        "order_date": "2019-04-03T11:33:15Z",
        "request_date": "2019-04-07T11:33:15Z",
        "reference": "ORD00001",
        "reference_extra": "Bedreven arm straffen bureau.",
        "order_status": "Delivered",
        "notes": "Voedsel vijf vork heel.",
        "shipping_notes": "Buurman betalen plaats bewolkt.",
        "picking_notes": "Ademen fijn volgorde scherp aardappel op leren.",
        "warehouse_id": 18,
        "ship_to": 1,
        "bill_to": 3,
        "shipment_id": 1,
        "total_amount": 9905.13,
        "total_discount": 150.77,
        "total_tax": 372.72,
        "total_surcharge": 77.6,
        "created_at": "2019-04-03T11:33:15Z",
        "updated_at": "2019-04-05T07:33:15Z",
        "items": [
            {"item_id": "P007435", "amount": 12},
        ]
        }


incomplete_order = {
    "id": None,
    "source_id": None,
    "order_date": None,
    "request_date": None,
    "reference": None,
    "reference_extra": None,
    "order_status": "Delivered",
    # "notes": "Voedsel vijf vork heel.",
    # "shipping_notes": "Buurman betalen plaats bewolkt.",
    "picking_notes": None,
    "warehouse_id": 18,
    "ship_to": 1,
    "bill_to": 3,
    "shipment_id": 1,
    "total_amount": 9905.13,
    "total_discount": 150.77,
    "total_tax": 372.72,
    "total_surcharge": 77.6,
    "created_at": "2019-04-03T11:33:15Z",
    "updated_at": "2019-04-05T07:33:15Z",
    "items": [
        {"item_id": "P007435", "amount": 23},
        {"item_id": "P009557", "amount": 1},
        {"item_id": "P009553", "amount": 50},
        {"item_id": "P010015", "amount": 16},
        {"item_id": "P002084", "amount": 33},
        {"item_id": "P009663", "amount": 18},
        {"item_id": "P010125", "amount": 18},
        {"item_id": "P005768", "amount": 26},
        {"item_id": "P004051", "amount": 1},
        {"item_id": "P005026", "amount": 29},
        {"item_id": "P000726", "amount": 22},
        {"item_id": "P008107", "amount": 47},
        {"item_id": "P001598", "amount": 32},
        {"item_id": "P002855", "amount": 20},
        {"item_id": "P010404", "amount": 30},
        {"item_id": "P010446", "amount": 6},
        {"item_id": "P001517", "amount": 9},
        {"item_id": "P009265", "amount": 2},
        {"item_id": "P001108", "amount": 20},
        {"item_id": "P009110", "amount": 18},
        {"item_id": "P009686", "amount": 13}
    ]
    }

items1 =    [{"item_id": "P007435", "amount": 30},
            {"item_id": "P009557", "amount": 2},]

item_nonexistent = [{"item_id": "1321323131", "amount": 23}]

empty_order = {}

obj = Orders("./CargoHub/data/testdb/test_")


def setup_data_provider():
    data_provider.init() 


def add_order():
    obj.data = []
    obj.add_order(order1)

def test_get_order_with_id():
    add_order()
    assert obj.get_order(9876) == order1

def test_get_order_not_in_db():
    add_order()
    assert obj.get_order(0) == None 

def test_get_items_in_order():
    add_order()
    assert obj.get_items_in_order(9876) == items1

def test_get_items_in_order_not_in_db():
    add_order()
    assert obj.get_items_in_order(0) == None

def test_get_order_in_shipment(): # Returns the id in a list?
    add_order()
    assert obj.get_orders_in_shipment(1) == order1

def test_get_order_in_shipment_not_in_db(): # Returns an empty list instead of None
    add_order()
    assert obj.get_orders_in_shipment(0) == None

def test_get_orders_for_clients():
    add_order()
    assert len(obj.get_orders_for_client(1)) == 1

def test_get_orders_for_clients1():
    add_order()
    assert len(obj.get_orders_for_client(3)) == 1

def test_get_orders_for_clients_not_in_db():
    add_order()
    assert len(obj.get_orders_for_client(2)) == 0

def test_add_order():
    # First, clear existing data
    obj.data = []
    obj.add_order(order1)
    assert len(obj.data) == 1

def test_add_order_wrong1():
    # Adds wrong order.
    obj.data = []
    assert obj.add_order(incomplete_order) is None
    assert len(obj.data) == 0

def test_add_empty_order():
    # Adds wrong order.
    obj.data = []
    assert obj.add_order(empty_order) is None
    assert len(obj.data) == 0


def test_update_order():
    obj.data = []
    obj.add_order(order1)
    obj.update_order(9876, order2)  # Update the order
    
    assert obj.data[0]["source_id"] == 12
    assert obj.data[0]["id"] == 9876  # ID should remain the same
    assert obj.data[0]["updated_at"] is not None  # Updated timestamp should be set


def test_update_order_empty():
    obj.data = []
    obj.add_order(order1)

    obj.update_order(9876, empty_order)

    assert obj.data[0] != empty_order  #updated while its empty 


def test_update_existing_items():
    obj.data = []
    obj.add_order(order1)

    obj.update_items_in_order(9876, items1)
    
    updated_order = obj.get_order(9876)
    assert updated_order["items"][0]["amount"] == 30, "Item P007435 should have been updated to 30"
    assert updated_order["items"][1]["amount"] == 2, "Item P009557 should have been updated to 2"
    assert updated_order["items"][2]["amount"] == 50, "Item P009553 should stay 50"
    assert len(updated_order["items"]) == 21, "The number of items in the order should remain the same"


def test_update_items_with_nonexistent_item():
    obj.data = []
    obj.add_order(order1)

    obj.update_items_in_order(9876, item_nonexistent)

    # Mocking the inventory pool
    mock_inventory_pool = MagicMock()
    mock_inventory_pool.get_inventories_for_item.return_value = [{"total_allocated": 10, "id": 1}]
    data_provider.fetch_inventory_pool = MagicMock(return_value=mock_inventory_pool)
    
    updated_order = obj.get_order(9876)
    assert updated_order["items"][0]["amount"] == 30, "Item P007435 should have been updated to 30"
    assert updated_order["items"][1]["amount"] == 2, "Item P009557 should have been updated to 2"


def test_update_items_without_changes():
    obj.data = []
    obj.add_order(order1)

    items_to_update = [
        {"item_id": "P007435", "amount": 23},
        {"item_id": "P009557", "amount": 1},
        {"item_id": "P009553", "amount": 50},
        {"item_id": "P010015", "amount": 16},
        {"item_id": "P002084", "amount": 33},
        {"item_id": "P009663", "amount": 18},
        {"item_id": "P010125", "amount": 18},
        {"item_id": "P005768", "amount": 26},
        {"item_id": "P004051", "amount": 1},
        {"item_id": "P005026", "amount": 29},
        {"item_id": "P000726", "amount": 22},
        {"item_id": "P008107", "amount": 47},
        {"item_id": "P001598", "amount": 32},
        {"item_id": "P002855", "amount": 20},
        {"item_id": "P010404", "amount": 30},
        {"item_id": "P010446", "amount": 6},
        {"item_id": "P001517", "amount": 9},
        {"item_id": "P009265", "amount": 2},
        {"item_id": "P001108", "amount": 20},
        {"item_id": "P009110", "amount": 18},
        {"item_id": "P009686", "amount": 13}
    ]

    obj.update_items_in_order(9876, items_to_update)

    updated_order = obj.get_order(9876)
    assert updated_order["items"] == items_to_update, "Items should remain unchanged since there were no updates."
    assert len(updated_order["items"]) == len(items_to_update), "The number of items in the order should remain the same."


def test_remove_orders_from_shipment():
    obj.data = []
    obj.add_order(order1)
    obj.add_order(order2)
    
    obj.update_orders_in_shipment(1, [9876])
    
    updated_order = obj.get_order(9876)
    assert updated_order["shipment_id"] == 1
    assert updated_order["order_status"] == "Packed"


def test_add_orders_to_shipment():
    obj.data = []
    order2["shipment_id"] = -1
    order2["order_status"] = "Scheduled"
    obj.add_order(order1)
    obj.add_order(order2)

    obj.update_orders_in_shipment(1, [9876])
    
    updated_order = obj.get_order(9876)
    assert updated_order["shipment_id"] == 1
    assert updated_order["order_status"] == "Packed"


def test_no_change_in_shipment():
    obj.data = []
    obj.add_order(order1)
    
    obj.update_orders_in_shipment(1, [9876])
    
    updated_order = obj.get_order(9876)
    assert updated_order["shipment_id"] == 1
    assert updated_order["order_status"] == "Packed"


def test_remove_existing_order():
    obj.data = []
    obj.add_order(order1)

    obj.remove_order(9876)

    assert len(obj.data) == 0, "Order should be removed from the list"

def test_remove_non_existing_order():
    obj.data = []
    obj.add_order(order1)
    obj.add_order(order2)

    obj.remove_order(9999)

    assert len(obj.data) == 2, "No order should be removed"
    assert obj.data[0]["id"] == 9876, "Order with ID 9876 should still exist"
    assert obj.data[1]["id"] == 9876, "Order with ID 9876 should still exist"
