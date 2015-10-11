# using it

    >>> import requests_async
    >>> loop = asyncio.get_event_loop()
    >>> f = loop.run_until_complete(asyncio.gather(requests_async.get('http://www.google.com')))
    >>> f
    [<Response [200]>]
    >>> f = loop.run_until_complete(requests_async.get('http://www.google.com'))
    >>> f
    <Response [200]>
    >>> f = loop.run_until_complete(asyncio.gather(map(requests_async.get, ['http://www.google.com', 'http://www.twitter.com', 'http://imgur.com')))
      File "<stdin>", line 1
        f = loop.run_until_complete(asyncio.gather(map(requests_async.get, ['http://www.google.com', 'http://www.twitter.com', 'http://imgur.com')))
                                                                                                                                                 ^
    SyntaxError: invalid syntax
    >>> f = loop.run_until_complete(asyncio.gather(map(requests_async.get, ['http://www.google.com', 'http://www.twitter.com', 'http://imgur.com'])))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/usr/lib/python3.5/asyncio/tasks.py", line 582, in gather
        fut = ensure_future(arg, loop=loop)
      File "/usr/lib/python3.5/asyncio/tasks.py", line 531, in ensure_future
        raise TypeError('A Future or coroutine is required')
    TypeError: A Future or coroutine is required
    >>> f = loop.run_until_complete(asyncio.gather(*map(requests_async.get, ['http://www.google.com', 'http://www.twitter.com', 'http://imgur.com'])))
    >>> f
    [<Response [200]>, <Response [200]>, <Response [200]>]
    >>> 

