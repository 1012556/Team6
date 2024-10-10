from fastapi import APIRouter
from fastapi import FastAPI, Request

from models.warehouses import Warehouses
from Controllers.Controller import Controller
from providers import auth_provider, data_provider



class WarehouseController(Controller):
    warehouse_router = APIRouter()
    warehouse = data_provider.fetch_warehouse_pool()

    # http://localhost:3000/api/v1/warehouses
    @warehouse_router.get("warehouses")
    def request_get_warehouses(request: Request):
        WarehouseController.authorization(request.headers.get('API_KEY'), request.url.path, request.method)

        warehouses = data_provider.fetch_warehouse_pool().get_warehouses()
        return warehouses

    @warehouse_router.get("warehouses/{warehouse_id}")
    def request_get_warehouse(request: Request, warehouse_id: int):
        WarehouseController.authorization(request.headers.get('API_KEY'), request.url.path, request.method)
        warehouse = data_provider.fetch_warehouse_pool().get_warehouse(warehouse_id)

        if warehouse is None:
            return warehouse, 401
        return warehouse, 200
    
    @warehouse_router.post("warehouses")
    def request_add_warehouse(request: Request, warehouse: Warehouses):
        WarehouseController.authorization(request.headers.get('API_KEY'), request.url.path, request.method)

        data_provider.fetch_warehouse_pool().add_warehouse(warehouse)
        return warehouse, 200