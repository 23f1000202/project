from fastapi import FastAPI, HTTPException
from tasksA import *

app = FastAPI()

@app.post("/run")
async def run_task(task: str):
    try:
        if "datagen.py" in task:
            task_a1("your_email@example.com")
        elif "format.md" in task:
            task_a2()
        elif "dates.txt" in task:
            task_a3()
        elif "contacts.json" in task:
            task_a4()
        elif "logs" in task:
            task_a5()
        elif "docs" in task:
            task_a6()
        elif "email.txt" in task:
            task_a7()
        elif "credit-card.png" in task:
            task_a8()
        elif "comments.txt" in task:
            task_a9()
        elif "ticket-sales.db" in task:
            task_a10()
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/read")
async def read_file(path: str):
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found")
    with open(path, "r") as file:
        content = file.read()
    return {"content": content}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)