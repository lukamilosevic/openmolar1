# -*- coding: utf-8 -*-
# Copyright (c) 2009 Neil Wallace. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. See the GNU General Public License for
# more details.

import sys
from openmolar.connect import connect
from openmolar.settings import localsettings

headers=["topic","user","comment","submitted"]

class post():
    def __init__(self):
        self.ix=None
        self.parent_ix=None
        self.inits=""
        self.date=None
        self.topic=""
        self.comment=""
        self.briefcomment=""
        self.open=True

def getPosts(table="forum"):
    '''
    gets all active rows from a forum table
    '''

    db=connect()
    cursor=db.cursor()
    query='''select
    ix, parent_ix,topic,inits,fdate,comment from %s where open'''%table

    if localsettings.logqueries:
        print query
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    #db.close()
    retarg=[]
    for row in rows:
        newpost=post()
        newpost.ix=row[0]
        newpost.parent_ix=row[1]
        newpost.topic=row[2]
        newpost.inits=row[3]
        newpost.date=row[4]
        newpost.comment=row[5]
        newpost.briefcomment=row[5][:30]
        if newpost.comment!=newpost.briefcomment:
            newpost.briefcomment+="...."
        retarg.append(newpost)
    return retarg

if __name__ == "__main__":
    posts = getPosts()
    for post in posts:
        print post
