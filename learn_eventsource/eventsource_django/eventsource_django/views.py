# coding:utf-8

import time

from django.http import HttpResponse, StreamingHttpResponse
from django.utils.timezone import now


def eventsource(request):
    time.sleep(10)
    response = StreamingHttpResponse(stream_generator(), content_type="text/event-stream")
    response['Cache-Control'] = 'no-cache'
    return response


def stream_generator():
    while True:
        # 发送事件数据
        # yield 'event: date\ndata: %s\n\n' % str(now())

        # 发送数据
        yield u'data: %s\n\n' % str(now())
        time.sleep(4)


def ajax(request):
    time.sleep(2)
    return HttpResponse('ajax')
