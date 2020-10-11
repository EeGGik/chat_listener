from werkzeug import exceptions
from exeptions import ServiceError
from loguru import logger
from http import HTTPStatus


def json_checker(request):
    try:
        message_info = request.get_json()
        logger.info(message_info)
        if message_info is None:
            raise exceptions.BadRequest
    except exceptions.BadRequest:
        return ServiceError(userMessage=f"request should be JSON format! request = {request.data}",
                            errorCode=400, status=HTTPStatus.BAD_REQUEST)
    return message_info


def bed_word_finder(message: dict):
    stop_list = ['bomb', 'terrorist', 'work']
    unswer = {'detected': False, 'bad_words': ''}
    if "message" not in message:
        return ServiceError(userMessage='request should contains message',
                            errorCode=400,
                            status=HTTPStatus.BAD_REQUEST)
    for i in stop_list:
        if i in message['message']:
            unswer['detected'] = True
            unswer['bad_words'] += f'{i} '
    unswer['bad_words'] = " ".join(unswer['bad_words'].split())
    logger.info(unswer)
    return unswer


def checker(request):
    logger.info(request.data)
    message = json_checker(request)
    if type(message) is ServiceError:
        logger.error(f"{message.status.value} {message.info()}")
        return message.info(), message.status

    message = bed_word_finder(message)
    if type(message) is ServiceError:
        logger.error(f"{message.status.value} {message.info()}")
        return message.info(), message.status

    return message, HTTPStatus.OK
