import asyncio
import functools
import requests


async def request(method, url, **kwargs):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        None,
        functools.partial(requests.request, method, url, **kwargs)
    )


async def head(url, **kwargs):
    return await request('HEAD', url, **kwargs)


async def get(url, **kwargs):
    return await request('GET', url, **kwargs)


async def post(url, data=None, **kwargs):
    return await request('POST', url, data=data, **kwargs)


async def put(url, data=None, **kwargs):
    return await request('PUT', url, data=data, **kwargs)


async def patch(url, data=None, **kwargs):
    return await request('PATCH', url, data=data, **kwargs)


async def delete(url, **kwargs):
    return await request('DELETE', url, **kwargs)
