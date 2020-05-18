# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
db.define_table('email',
                Field('nome', 'string'),
                Field('email','string'),
               )
db.email.nome.requires = IS_NOT_EMPTY()
db.email.email.requires = IS_NOT_EMPTY()
db.email.email.requires = IS_EMAIL()
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------
auth.enable_record_versioning(db)
