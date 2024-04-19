def signal(initialValue):
    state=initialValue
    suscriptors = []
    fn=lambda:state

    def set(v):        
        nonlocal state       
        if(v!=state):
            state=v       
            for cb in suscriptors:
                cb()

    fn.set = set
    
    def suscribe(cb):
        cb()
        suscriptors.append(cb)
    fn.suscribe = suscribe
    return fn

result = signal(10)
result.suscribe(lambda:print(result()))
result.set(100)
