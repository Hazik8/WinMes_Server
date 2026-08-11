from uuid import uuid4


def generate_message_id():

    return str(uuid4())


def success(data=None):

    return {

        "status": "ok",

        "data": data

    }


def error(message):

    return {

        "status": "error",

        "message": message

    }