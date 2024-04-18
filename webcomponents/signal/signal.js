export function signal(initialValue){
    
    let value = initialValue
    let suscriptors = new Set();
    
    const fn = ()=>value   //gettter

    fn.set = (v)=>{  //setter
        if(!Object.is(value,v)){
            value=v
            for(const fn of suscriptors){
                fn();
            }
        }        
    }
    fn.subscribe = (fn)=>{ //suscription
        fn();
        suscriptors.add(fn)
    }
    return fn
}