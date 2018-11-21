from aiohttp import web


async def hello(request):
    return web.Response(body=u'Hello world!')


def create_app(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', hello)
    return app