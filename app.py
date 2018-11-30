def application(environ, start_response):
    response_body = 'hello world'
    # HTTP response code and message
    status = '200 OK'
    # 应答的头部是一个列表，每对键值都必须是一个 tuple。
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(response_body)))]
    # 调用服务器程序提供的 start_response，填入两个参数
    start_response(status, response_headers)
    # 返回必须是 iterable
    return [bytes(response_body, 'utf8')]
