def coroutine(func):
    def go(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return go


class BlaException(Exception):
    pass

# @coroutine
def subgen():
    while True:
        try:
            message = yield
        except BlaException:
            print('Hi!')
        else:
            print('.....', message)

@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaException as e:
    #         g.throw(e)
    yield from g
