from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from controllers import ProjectController, FirebaseController
from models import ResponseSignal
from helpers import get_settings, Settings
import json
import aiofiles
import os
import logging

logger = logging.getLogger('uvicorn.error')

firebase_router = APIRouter(
    prefix="/api/v1/get/firebase/data",
    tags=["api_v1", "getfirebasedata"]
)

@firebase_router.get("/")
async def trastain_destination_documents(app_settings: Settings = Depends(get_settings)):
    try:
        
        data = FirebaseController().get_firebase_data()
        formatted_data = json.dumps(data, indent=max(2, len(data) // 10))

        destination_dir_path = ProjectController().get_destination_path(project_id="1")
        destination_data_path = os.path.join(destination_dir_path, "json_data")

        async with aiofiles.open(destination_data_path, "wb") as f:

            await f.write(formatted_data.encode('utf-8'))

        #     while chunk := await formatted_data.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
        #         await f.write(chunk)

        return JSONResponse(
            content={"signal": ResponseSignal.DATA_SAVED_SUCCESS.value}
        )
    except Exception as e:
        logger.error(f"Error while uploading file: {e}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"signal": ResponseSignal.DATA_SAVED_FAILED.value}
        )
