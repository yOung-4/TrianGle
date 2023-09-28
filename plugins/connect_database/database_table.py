from pony import orm
from plugins.connect_database import db


class progress(db.Entity):
    user_name = orm.Required(str)
    progress_code = orm.Required(str)
    hp = orm.Required(int)
    train_high = orm.Required(int)


db.generate_mapping(create_tables=True)