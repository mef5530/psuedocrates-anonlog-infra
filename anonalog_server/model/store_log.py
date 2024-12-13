import json

from anonalog_server.model.schema import LogEntry
from anonalog_server.model import Session

def store_log(endpoint, data):
    with Session() as session:
        entry = LogEntry(endpoint=endpoint, payload=data)
        session.add(entry)
        session.commit()