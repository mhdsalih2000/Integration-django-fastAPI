from typing import List
from fastapi import APIRouter , HTTPException ,status
from .models import KeyValue
from .sceemas import KeyValueDTO


router = APIRouter()

# endpoint for retrieve data using key - done
@router.get("/key-values/{key}", response_model=KeyValueDTO)
def get_key_value(key: str):
    try:
        key_value = KeyValue.objects.get(key=key)
    except KeyValue.DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Item with key '{key}' does not exist")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return key_value
    




# endpoint for create new key-value data -done
@router.post("/key-Values/create")
def create_keyValues(item: KeyValueDTO):
    if KeyValue.objects.filter(key=item.key).exists():
        raise HTTPException(status_code=400 , detail="Key already exists")  
    try: 
        KeyValue.objects.create(key=item.key, value=item.value) 
        return item 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

# endpoint for update value using key -done
@router.post("/key-Values/update")
async def update_keyValues(item: KeyValueDTO):
    try:
        key_value = KeyValue.objects.filter(key=item.key).first()
        if key_value:
            key_value.value = item.value
            key_value.save()
            return {"message": "KeyValue updated successfully"}
        else:
            raise HTTPException(status_code=404, detail=f"Item with key '{item.key}' does not exist")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        


@router.delete("/key-values/delete/{key}")
def delete_key_value(key: str):
    try:
        key_value_data = KeyValue.objects.filter(key=key).first()
        if key_value_data:
            key_value_data.delete()
            return {"message": "KeyValue deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail=f"Item with key '{key}' does not exist")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
        

