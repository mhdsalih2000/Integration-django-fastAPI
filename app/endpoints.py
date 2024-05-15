from typing import List
from fastapi import APIRouter , HTTPException ,status
from .models import KeyValue
from .sceemas import KeyValueDTO

router = APIRouter()

@router.get("/key-Values", response_model=List[KeyValueDTO])
async def get_keyValues():
    try:
        key_values = await KeyValue.objects.all()
        return key_values
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))



@router.post("/key-Values")
async def post_keyValues(key: str, value: str):
    try:
        if KeyValue.objects.filter(key=key).exists():
            raise HTTPException(status_code=400, detail="Key already exists")    
        KeyValue.objects.create(key=key, value=value) 
        raise HTTPException(status_code=201, detail="Created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/key-Values" ,status_code=status.HTTP_201_CREATED)
def update():
    pass




