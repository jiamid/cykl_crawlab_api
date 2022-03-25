from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from uvicorn import run
from commons.config import system_conf
from api.crawler_api import insert_router
from api.gs_api import gs_router
from api.test_api import test_router

API_HEADERS = '/winte_olympics_api'

app = FastAPI(title='Winter Olympics Api', openapi_url=f'{API_HEADERS}/openapi.json')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

if system_conf.CRAWLER_API_STATUS == 'true':
    app.include_router(insert_router, prefix=API_HEADERS)
if system_conf.GS_API_STATUS == 'true':
    app.include_router(gs_router, prefix=API_HEADERS)

if system_conf.TEST_API_STATUS == 'true':
    app.include_router(test_router)

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=system_conf.API_PORT)
