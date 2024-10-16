from fastapi import APIRouter, Body
from fastapi import FastAPI, Request

from models.Models import Location, Warehouse
from Services.base import Base
from Services.Service_warehouses import ServiceWarehouses
from Controllers.Controller import Controller
from providers import auth_provider, data_provider



class WarehouseController(Controller):
    warehouse_router = APIRouter()
    warehouse = data_provider.fetch_warehouse_pool()

    # http://localhost:3000/api/v1/warehouses
    @warehouse_router.get("", tags= ["warehouses"])
    def request_get_warehouses(request: Request):
        WarehouseController.authorization(request.headers.get('API_KEY'), request.url.path, request.method)

        warehouses = data_provider.fetch_warehouse_pool().get_warehouses()
        return warehouses

    @warehouse_router.get("/{warehouse_id}", tags= ["warehouses"])
    def request_get_warehouse(request: Request, warehouse_id: int):
        WarehouseController.authorization(request.headers.get('API_KEY'), request.url.path, request.method)
        warehouse = data_provider.fetch_warehouse_pool().get_warehouse(warehouse_id)

        if warehouse is None:
            return warehouse, 401
        return warehouse, 200
    
    @warehouse_router.post("")
    def request_add_warehouse(request: Request, payload: Warehouse = Body(...)):
        WarehouseController.authorization(request.headers.get('API_KEY'), request.url.path, request.method)

        data_provider.fetch_warehouse_pool().add_warehouse(payload)
        return payload, 200
    
    @warehouse_router.put("/{id}", response_model=Warehouse)
    def request_update_warehouse(request: Request, id: int, payload: Warehouse = Body(...)):
        WarehouseController.authorization(request.headers.get('API_KEY'), request.url.path, request.method)

        data_provider.fetch_warehouse_pool().update_warehouse(id, payload)
        return payload
    
    @warehouse_router.delete("/{id}", response_model=dict)
    def delete_warehouse(request: Request, id: int):
        WarehouseController.authorization(request.headers.get('API_KEY'), request.url.path, request.method)

        data_provider.fetch_warehouse_pool().remove_warehouse(id)        
        return {"Message" : "Succedfully deleted"  }  
    
    @warehouse_router.get("/{id}/locations", response_model=list) 
    def location_in_warehouse(request: Request, id: int):
        WarehouseController.authorization(request.headers.get('API_KEY'), request.url.path, request.method)

        data = data_provider.fetch_location_pool().get_locations_in_warehouse(id)
        return data
    
