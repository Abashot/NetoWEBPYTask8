import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        response = await session.post('http://127.0.0.1:8080/user',
                                      json={
                                          'username': 'user3',
                                          'email': 'user3@mail.com',
                                          'password': '12345',
                                      }
                                      )
        print(response.status)
        print(await response.json())

    async with aiohttp.ClientSession() as session:
        response = await session.get('http://127.0.0.1:8080/user/11')
        print(response.status)
        print(await response.json())

    async with aiohttp.ClientSession() as session:
        response = await session.patch('http://127.0.0.1:8080/user/6',
                                       json={
                                           'username': 'user101',
                                       }
                                       )
        print(response.status)
        print(await response.json())

    async with aiohttp.ClientSession() as session:
        response = await session.delete('http://127.0.0.1:8080/user/2')
        print(response.status)
        print(await response.json())

    async with aiohttp.ClientSession() as session:
        response = await session.post('http://127.0.0.1:8080/advertisement',
                                      json={
                                          "header": "Samsung Galaxy S20",
                                          "description": "Продам Samsung Galaxy S20. Состояние: хорошее. Цена: $300",
                                          "owner": "6"
                                      }
                                      )
        print(response.status)
        print(await response.json())

    async with aiohttp.ClientSession() as session:
        response = await session.get('http://127.0.0.1:8080/advertisement/3')
        print(response.status)
        print(await response.json())

    async with aiohttp.ClientSession() as session:
        response = await session.patch('http://127.0.0.1:8080/advertisement/1',
                                       json={
                                           "header": "Iphone 10"
                                       })
        print(response.status)
        print(await response.json())

    async with aiohttp.ClientSession() as session:
        response = await session.delete('http://127.0.0.1:8080/advertisement/3')
        print(response.status)
        print(await response.json())


asyncio.run(main())
