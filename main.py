from fastapi import FastAPI, Request

app = FastAPI()

fake_db = [
    {"name": "Pedro", "status": "Habilitado"},
    {"name": "Joao", "status": "Habilitado"},
    {"name": "Paulo", "status": "Desabilitado"},
    {"name": "Giovani", "status": "Habilitado"},
    {"name": "Leonardo", "status": "Desabilitado"},
    {"name": "Alexandre", "status": "Inativo"},
    {"name": "Arthur", "status": "Desabilitado"}
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
@app.get("/api/v1/health")
@app.get("/api/health")
async def health(request: Request):
    result = {}
    result['url_original'] = str(request.url)
    result['url_path'] = str(request.url.path)
    result['message'] = "App is alive"    
    return result

@app.get("/name/{name}")
async def name(name, request: Request):
    result = {}
    result['url_original'] = str(request.url)
    result['url_path'] = str(request.url.path)
    result['name'] = name
    return result

@app.get("/users")
async def user(request: Request, status: str | None = None):
    result = {}
    result['url_original'] = str(request.url)
    result['url_path'] = str(request.url.path)
    users = [user for user in fake_db]
    if status:
        users = [user for user in fake_db if user['status'] == status]
    result['users'] = users
    return result

