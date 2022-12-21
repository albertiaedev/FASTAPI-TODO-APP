from fastapi import FastAPI

app=FastAPI()

@app.get('/',tags=['ROOT'])
async def root() -> dict:
    return{
    "Hello":"World"
    }

#@get (read)
@app.get('/get',tags=['GET'])
async def get_todo() -> dict:
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

#@put (update)

#@delete (delete)
