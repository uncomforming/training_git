
from fastapi import APIrouter

router=APIrouter(
    prefix="items",
    tags=["items"]
)

@router.get("/")
async def list_item():
    pass

@router.post("/")
async def create_items():
    pass

@router.patch("/")
async def update_items():
    pass

@router.delete("/")
async def delete_items():
    pass


