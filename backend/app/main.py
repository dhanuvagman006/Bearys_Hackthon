from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

from app.api import auth, backup, vault, recovery, simulation, analytics, health
from app.core.config import settings
from app.core.logging import configure_logging
from app.ws.manager import manager

configure_logging()
app = FastAPI(title=settings.app_name, version='1.0.0', openapi_url=f"{settings.api_prefix}/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

REQUEST_COUNTER = Counter('api_requests_total', 'Total API requests', ['endpoint'])

app.include_router(health.router, prefix=settings.api_prefix)
app.include_router(auth.router, prefix=settings.api_prefix)
app.include_router(backup.router, prefix=settings.api_prefix)
app.include_router(vault.router, prefix=settings.api_prefix)
app.include_router(recovery.router, prefix=settings.api_prefix)
app.include_router(simulation.router, prefix=settings.api_prefix)
app.include_router(analytics.router, prefix=settings.api_prefix)


@app.middleware('http')
async def metrics_middleware(request, call_next):
    REQUEST_COUNTER.labels(endpoint=request.url.path).inc()
    return await call_next(request)


@app.get('/metrics')
async def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.websocket('/ws/live')
async def live_updates(ws: WebSocket):
    await manager.connect(ws)
    try:
        while True:
            data = await ws.receive_text()
            await manager.broadcast(f'event:{data}')
    except WebSocketDisconnect:
        manager.disconnect(ws)
