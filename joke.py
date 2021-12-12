import  requests as rq
def joke():
    url="https://icanhazdadjoke.com/"
    head={'Accept':'text/plain'}
    res=rq.get(url,headers=head)
    return res.text
