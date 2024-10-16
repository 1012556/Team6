import json

from Services.base import Base

WAREHOUSES = []


class ServiceWarehouses(Base):
    def __init__(self, root_path, is_debug=False):
        self.data_path = root_path + "warehouses.json"
        self.load(is_debug)

    def get_warehouses(self):
        return self.data

    def get_warehouse(self, warehouse_id):
        for x in self.data:
            if x["id"] == warehouse_id:
                return x
        return None

    def add_warehouse(self, warehouse):
        warehouse_data = warehouse.dict()
        warehouse_data["created_at"] = self.get_timestamp()
        warehouse_data["updated_at"] = self.get_timestamp()
        self.data.append(warehouse_data)

    def update_warehouse(self, warehouse_id, warehouse):
        warehouse_data = warehouse.dict()
        warehouse_data["updated_at"] = self.get_timestamp()
        warehouse_data["id"] = warehouse_id
        for i in range(len(self.data)):
            if self.data[i]["id"] == warehouse_id:
                self.data[i] = warehouse_data
                break

    def remove_warehouse(self, warehouse_id):
        for x in self.data:
            if x["id"] == warehouse_id:
                self.data.remove(x)

    def load(self, is_debug):
        if is_debug:
            self.data = WAREHOUSES
        else:
            f = open(self.data_path, "r")
            self.data = json.load(f)
            f.close()

    def save(self):
        f = open(self.data_path, "w")
        json.dump(self.data, f)
        f.close()
