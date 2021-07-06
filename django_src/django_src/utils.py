from loguru import logger
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


logger.add('logs/errors.log', level='DEBUG', rotation='10 MB', retention='10 days')


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    logger.warning(exc)
    logger.warning(context)
    if response:
        response.data['status'] = 'error'
    else:
        response = Response({'status': 'error'},
                            status=status.HTTP_400_BAD_REQUEST)
    return response
