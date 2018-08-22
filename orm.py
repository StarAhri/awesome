

#一旦决定使用异步，则系统每一层都必须是异步，“开弓没有回头箭”。


import logging

import aiomysql
import asyncio

@asyncio.coroutine
def create_pool(loop,**kwargs):
    logging.info('create database connection pool...')
    global __pool
    __pool=yield from aiomysql.create_pool(
        host=kwargs.get('host','localhost'),
        port=kwargs.get('port',3306),
        user=kwargs['user'],
        password=kwargs['password'],
        db=kwargs['db'],
        charset=kwargs.get('charset','utf8'),
        autocommit=kwargs.get('maxsize',10),
        minsize=kwargs.get('minsize',1),
        loop=loop

    )


@asyncio.coroutine
def select (sql,args,size=None):
    log(sql,args)