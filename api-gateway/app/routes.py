from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
import httpx
from app.config import SERVICE_MAP

router = APIRouter()

@router.api_route("/{service}", methods=["GET", "POST", "PUT", "DELETE"])
@router.api_route("/{service}/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def gateway(service: str, request: Request, path: str = ""):
    if service not in SERVICE_MAP:
        return JSONResponse(status_code=404, content={"detail": "Service not found"})

    target_url = SERVICE_MAP[service]
    if path:
        target_url += f"/{path}"

    async with httpx.AsyncClient() as client:
        try:
            if request.method == "GET":
                response = await client.get(target_url, params=dict(request.query_params))
            elif request.method == "POST":
                body = await request.body()
                response = await client.post(
                    target_url,
                    content=body,
                    headers={"Content-Type": request.headers.get("content-type", "application/json")},
                )
            elif request.method == "PUT":
                body = await request.body()
                response = await client.put(
                    target_url,
                    content=body,
                    headers={"Content-Type": request.headers.get("content-type", "application/json")},
                )
            elif request.method == "DELETE":
                response = await client.delete(target_url)
            else:
                return JSONResponse(status_code=405, content={"detail": "Method not allowed"})

            return JSONResponse(status_code=response.status_code, content=response.json())

        except httpx.RequestError:
            return JSONResponse(status_code=502, content={"detail": "Service unavailable"})