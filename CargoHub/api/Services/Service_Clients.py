import json

from Services.base import Base

CLIENTS = []


class ServiceClients(Base):
    def __init__(self, root_path, is_debug=False):
        self.data_path = root_path + "clients.json"
        self.load(is_debug)

    def get_clients(self):
        return self.data
# for x in .... loops in een functie zetten scheelt ruimte.
    def get_client(self, client_id):
        for x in self.data:
            if x["id"] == client_id:
                return x
        return None

    def add_client(self, client):
        client["created_at"] = self.get_timestamp()
        client["updated_at"] = self.get_timestamp()
        self.data.append(client)

    def update_client(self, client_id, client):
        client["updated_at"] = self.get_timestamp()
        for i in range(len(self.data)):
            if self.data[i]["id"] == client_id:
                self.data[i] = client
                break

    def remove_client(self, client_id):
        for x in self.data:
            if x["id"] == client_id:
                self.data.remove(x)
# kijk of er meerdere json functies zijn en dan apart in een bestand zetten!
    # is_debug slechte naam!!!!
    def load(self, is_debug):
        if is_debug:
            self.data = CLIENTS
        else:
            f = open(self.data_path, "r")
            self.data = json.load(f)
            f.close()

    def save(self):
        f = open(self.data_path, "w")
        json.dump(self.data, f)
        f.close()
