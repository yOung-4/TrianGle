from pony import orm

db = orm.Database()
db.bind(provider="splite", filename="database.selite", create_db=True)

orm.set_sql_debug(True)
