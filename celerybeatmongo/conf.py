from celery import current_app


def get_db_alias():
    if hasattr(current_app.conf, "mongodb_scheduler_connection_alias"):
        alias = current_app.conf.get('mongodb_scheduler_connection_alias')
    elif hasattr(current_app.conf, "CELERY_MONGODB_SCHEDULER_CONNECTION_ALIAS"):
        alias = current_app.conf.CELERY_MONGODB_SCHEDULER_CONNECTION_ALIAS
    else:
        alias = "default"
    return alias


def get_periodic_task_collection():
    if hasattr(current_app.conf, "mongodb_scheduler_collection"):
        return current_app.conf.get("mongodb_scheduler_collection")
    elif hasattr(current_app.conf, "CELERY_MONGODB_SCHEDULER_COLLECTION"):
        return current_app.conf.CELERY_MONGODB_SCHEDULER_COLLECTION
    return "schedules"


def get_db_name():
    if hasattr(current_app.conf, "mongodb_scheduler_db"):
        db = current_app.conf.get("mongodb_scheduler_db")
    elif hasattr(current_app.conf, "CELERY_MONGODB_SCHEDULER_DB"):
        db = current_app.conf.CELERY_MONGODB_SCHEDULER_DB
    else:
        db = "celery"
    return db


def get_host():
    if hasattr(current_app.conf, "mongodb_scheduler_url"):
        host = current_app.conf.get('mongodb_scheduler_url')
    elif hasattr(current_app.conf, "CELERY_MONGODB_SCHEDULER_URL"):
        host = current_app.conf.CELERY_MONGODB_SCHEDULER_URL
    else:
        host = None
    return host
