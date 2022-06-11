import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        app='v1.main:app',
        host='127.0.0.1',
        port=8000,
        log_level='info',
        debug=True,
    )
