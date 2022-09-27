from fastapi import FastAPI, File, UploadFile, Request, Body
from fastapi.responses import Response, JSONResponse
from starlette.concurrency import run_in_threadpool
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseSettings
from fastapi.openapi.utils import get_openapi
from typing import Optional
import os
import sys
import uuid
from nltk import word_tokenize
import numpy as np
import re
import pickle

from utils import get_emotion

app = FastAPI(middleware=[Middleware(CORSMiddleware, allow_origins=["*"])], redoc_url="/documentation")

@app.post("/recognize")

############
## recognize
############
    
async def recognize(request: Request):



    #### ШАБЛОН ОТВЕТА
    result = {
        "operation_status": "",
        "result": "",
        }

    try:
        form_data = await request.form()
        text = form_data.getlist('text')[0]
    except Exception as e:
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        result["operation_status"] = 'failed'
        result["result"] = 'text not in request'
        return result


    try:
        #### РАСПОЗНАВАНИЕ ТЕКСТА
        res = get_emotion(text)
        result["operation_status"] = 'ok'
        result["result"] = res

    except Exception as e:
        result["operation_status"] = 'failed'
        result["message"] = 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e
                
    return result