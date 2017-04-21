import random, inflect, twitter, time, datetime
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
api = twitter.Api(consumer_key='SECRET',
                  consumer_secret='SECRET',
                  access_token_key='SECRET',
                  access_token_secret='SECRET')
p = inflect.engine()
print("Political shitposts are a go")
while True:
    now = datetime.datetime.now()
    if str(now.second) == '0':
        if str(now.minute) == '0':
            if (random.randint(0, 100) == 1):
                brexit = "mcbrexit"
            else:
                brexit = "brexit"
            with open("intro.txt") as f:
                intro = [x.strip('\r\n') for x in f.readlines()]
            with open("adj.txt") as f:
                adjective = [x.strip('\r\n') for x in f.readlines()]
            with open("noun.txt") as f:
                noun = [x.strip('\r\n') for x in f.readlines()]
            with open("suffix.txt") as f:
                suffix = [x.strip('\r\n') for x in f.readlines()]
            count = random.randint(0,3)
            type = random.randint(0, 3)

            if(type <= 1):
                result = random.choice(intro)
                firstAdj = random.choice(adjective)
                result = result + p.a(firstAdj)
                while count > 1:
                    if count == 3:
                        result = result + ', '
                    if count == 2:
                        result = result + ' and '
                    result = result + random.choice(adjective)
                    count -= 1
                result = result + " " + brexit
                if random.randint(1, 24) == 1:
                    result = result + ' ' + random.choice(suffix)
            elif (type == 2):
                word = random.choice(noun)
                result = (word + ' means ' + word)
            elif (type == 3):
                result= brexit + ' ' + random.choice(suffix)
            print result
            api.PostUpdate(result)
            time.sleep(1)