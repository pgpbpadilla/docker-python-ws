from demo_service import service


async def test_create_app(aiohttp_client):
    client = await aiohttp_client(service.create_app)

    assert client is not None

    response = await client.get('/')

    assert response.status == 200
    assert 'Hello' in await response.text()