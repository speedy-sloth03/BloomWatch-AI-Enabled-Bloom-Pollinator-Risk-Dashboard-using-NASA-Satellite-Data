from fastapi import APIRouter
from typing import List
from app.models.regions import Region

router = APIRouter()

# Bangladesh divisions and BBoxes — hardcoded for demo
DIVISIONS = [
    {
        "id": "Dhaka", "name_en": "Dhaka", "name_bn": "ঢাকা", "bbox": [22.0, 88.0, 24.5, 91.0]
    },
    {
        "id": "Chattogram", "name_en": "Chattogram", "name_bn": "চট্টগ্রাম", "bbox": [20.5, 91.5, 23.5, 92.8]
    },
    {
        "id": "Khulna", "name_en": "Khulna", "name_bn": "খুলনা", "bbox": [21.2, 88.0, 23.0, 90.5]
    },
    {
        "id": "Rajshahi", "name_en": "Rajshahi", "name_bn": "রাজশাহী", "bbox": [24.0, 88.0, 26.5, 89.8]
    },
    {
        "id": "Barishal", "name_en": "Barishal", "name_bn": "বরিশাল", "bbox": [21.0, 89.5, 22.5, 90.9]
    },
    {
        "id": "Sylhet", "name_en": "Sylhet", "name_bn": "সিলেট", "bbox": [24.3, 91.5, 26.0, 92.9]
    },
    {
        "id": "Rangpur", "name_en": "Rangpur", "name_bn": "রংপুর", "bbox": [24.0, 88.0, 26.0, 89.7]
    },
    {
        "id": "Mymensingh", "name_en": "Mymensingh", "name_bn": "ময়মনসিংহ", "bbox": [24.0, 89.5, 25.5, 90.8]
    }
]

@router.get("/regions", response_model=List[Region], tags=["Regions"])
async def get_regions():
    return DIVISIONS