from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from paramiko import SSHClient, AutoAddPolicy

app = FastAPI()

# Templates setup
templates = Jinja2Templates(directory="templates")

ssh_client = None  # To store the SSH client instance

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index1.html", {"request": request})

@app.post("/connect/")
async def connect(
    request: Request,
    host: str = Form(...),
    port: int = Form(...),
    username: str = Form(...),
    password: str = Form(...),
):
    global ssh_client
    ssh_client = SSHClient()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())

    try:
        ssh_client.connect(host, port, username, password)
        return templates.TemplateResponse("terminal.html", {"request": request})
    except Exception as e:
        return {"error": f"SSH Connection Failed: {str(e)}"}

@app.post("/run_command/")
async def run_command(request: Request, command: str = Form(...)):
    try:
        stdin, stdout, stderr = ssh_client.exec_command(command)
        output = stdout.read().decode()
        if str(output) is "undefined":
            return ""
        else:
    
            return {"output": output}
    except Exception as e:
        return {"error": f"Command execution failed: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
