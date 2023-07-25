from threading import local

_thread_locals = local()


def get_api_current_user():
    return getattr(_thread_locals, 'user_id', None)
