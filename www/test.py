import asyncio
import orm
from models import User, Blog, Comment

def test(loop):
    yield from orm.create_pool(user='root', password='password', db='awesome',loop=loop)
    u = User(name='Test6', email='long@example.com', passwd='1234567890', image='about:blank')
    yield from u.save()
loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))