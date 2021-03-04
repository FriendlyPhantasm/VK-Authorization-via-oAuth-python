from aiohttp import web

routes = web.RouteTableDef()
code = {'code': ''}

#получаем параметр code с callback url авторизации
@routes.get('/')
async def hello(request: web.Request) -> web.Request:
    global code
    code = {'code': request.raw_path.split("=")[1]}
    return web.Response(text="Working...")


#возврат параметра code
@routes.get('/code')
async def hello(request: web.Request):
    global code
    return web.json_response(code)

#инициализация aiohttp
async def init_app() -> web.Application:
    app = web.Application()
    app.add_routes(routes)
    return app

#запуск приложения
web.run_app(init_app(), host='127.0.0.1', port=8080)
