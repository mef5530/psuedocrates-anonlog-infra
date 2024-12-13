from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from anonalog_server.model.schema import db_init

constr = 'sqlite:///sqlite.db'
engine = create_engine(constr)
db_init(engine)

Session = sessionmaker(engine)