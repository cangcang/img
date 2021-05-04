#!/usr/bin/python3.8
import requests
import asyncio
import aioredis
import time
import chardet

#https://aioredis.readthedocs.io/en/v1.3.1/index.html


#url = 'https://scontent-hkt1-1.cdninstagram.com/v/t51.2885-19/s320x320/119381356_363756831450146_3008355575418576013_n.jpg?tp=1&_nc_ht=scontent-hkt1-1.cdninstagram.com&_nc_ohc=DjREcz_DkfkAX9A6hIG&edm=ABfd0MgBAAAA&ccb=7-4&oh=60b3c39c24b245b3b910f79eaa7064ca&oe=60B1FD8E&_nc_sid=7bff83'

#r = requests.get(url=url)
#with open('bd_logo1.jpg', 'wb') as f:
#    f.write(r.content)
#    print('OK')
prefixPath = '/home/gen/nginx_file/img/instagram/' 

async def main():
    redis = await aioredis.create_redis_pool('redis://127.0.0.1:6379')

    while 1< 2:
        time.sleep(0.5)
        keyLen = await redis.llen('imgUrl')
        #print(keyLen)
        conList =  await redis.lrange('imgUrl',0,keyLen)
        #print(conList)
        #print(type(conList))

        for i in range(len(conList)):
            #print(conList[i])
            #print(type(conList[i]))
            ret = chardet.detect(conList[i])
            #print(ret)
            #print(str(conList[i],encoding = "utf-8"))
            newCon = str(conList[i],encoding = "utf-8")
            firstCon = newCon[0:newCon.index('?')]
            realName = firstCon[firstCon.rfind('/')+1:]
            #print(prefixPath+realName)
            rcon = requests.get(url=conList[i])
            with open(prefixPath+realName,'wb') as f:
                f.write(rcon.content)
            
            await redis.lrem('imgUrl',0,conList[i])



asyncio.run(main())


#while 1<2:
#    asyncio.run(main())
