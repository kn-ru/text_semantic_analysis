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

def ru_token(string):
    """russian tokenize based on nltk.word_tokenize. only russian letter remaind."""
    return [i for i in word_tokenize(string) if re.match(r'[\u0400-\u04ffа́]+$', i)]

with open('tfidf.pickle', 'rb') as f:
    tfidf = pickle.load(f)

with open('softmax.pickle', 'rb') as f:
    softmax = pickle.load(f)

def get_emotion(news):
    text = [news]
    sample = tfidf.transform(text)
    result = softmax.predict(sample)[0]
    return result