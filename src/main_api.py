from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from uvicorn import run
from commons.config import system_conf
from api.crawler_api import insert_router

API_HEADERS = '/cykl_crawlab'

app = FastAPI(title='CYKL Crawlab API', openapi_url=f'{API_HEADERS}/openapi.json')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


app.include_router(insert_router, prefix=API_HEADERS)

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=system_conf.API_PORT)
