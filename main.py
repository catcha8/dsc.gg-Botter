import requests, threading, random, user_agent

code    = input('>> code :: ')
proxys  = open('proxies.txt', 'r').read().splitlines(); proxy   = random.choice(proxys); proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
view    = 0

def __bot():
 try:
    global view
    with requests.Session() as session:
        res      = session.get(
         f'https://dsc.gg/{code}?ref=homepage',
         headers = {'user-agent': user_agent.generate_user_agent()},
         proxies = proxies

        )

        if res.status_code == 200:
            view +=1; print('>> {} sent!'.format(view))
        
        else:
            pass

 except Exception:
    pass
        
    

while True:
    threading.Thread(target=__bot).start()
