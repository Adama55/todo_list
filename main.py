from fastapi import FastAPI

# Documentation
from documentations.descriptions import api_description
from documentations.tags import tags_metadata

#import router
import routers.router_todoList

app = FastAPI(
    title="To do List",
    description=api_description,
    openapi_tags= tags_metadata
)

app.include_router(routers.router_todoList.router)

