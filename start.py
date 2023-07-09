from os import environ

import uvicorn

if __name__ == "__main__":
    reload = environ.get("RELOAD", "false") == "true"
    debug = environ.get("DEBUG", "false") == "true"
    host = "0.0.0.0"
    port = int(environ.get("PORT", "5000"))
    uvicorn.run("main:app", host=host, port=port, reload=reload)
