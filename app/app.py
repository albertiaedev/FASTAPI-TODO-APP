from fastapi import FastAPI

app=FastAPI()

@app.get('/',tags=['ROOT'])
async def root() -> dict:
    return{
    "Hello":"World"
    }

#@get (read)
@app.get('/tasks',tags=['TASK'])
async def get_task() -> dict:
    return{'data':tasks}

tasks = [
    {
    'ID':'01',
    'Task':'Wakeup at 07:00 AM'
    },
    {
    'ID':'02',
    'Task':'Exercise in the morning'
    },
    {
    'ID':'03',
    'Task':'Get ready for work'
    },
    {
    'ID':'04',
    'Task':'Go to your first meeting today'
    }
]


#@post (create)
@app.post('/tasks',tags=['TASK'])
async def add_task(task:dict) -> dict:
    tasks.append(task)
    return {
        'data':'A new task has been created'
    }


#@put (update)
@app.put('/tasks/{ID}',tags=['TASK'])
async def update_task(ID:int,body:dict) -> dict:
    for task in tasks:
        if int((task['ID'])) == ID:
            task['Task']=body['Task']
            return {
                'data':f'Task #{ID} has been updated'
            }
    return {
        'data':f'Task #{ID} does not exist'
    }


#@delete (delete)
