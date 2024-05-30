from fastapi import APIRouter
from app.services.copy_file_service import list_pod_all_namespace

router = APIRouter()


@router.get("/pods")
async def list_pods():
    try:
        response = list_pod_all_namespace()
        return {"pods": response}
    except Exception as e:
        return {"error": str(e)}
