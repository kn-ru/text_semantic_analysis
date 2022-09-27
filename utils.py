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
import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
transformer = TfidfTransformer()
loaded_vec = TfidfVectorizer(decode_error="replace",vocabulary=json.load(open("./vocabulary.json", "r")))


with open('./softmax.pickle', 'rb') as f:
    softmax = pickle.load(f)

def get_emotion(text):
    sample = transformer.fit_transform(loaded_vec.fit_transform([text]))
    result = softmax.predict(sample)[0]
    return result