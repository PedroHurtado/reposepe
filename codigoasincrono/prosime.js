class CustomerService{
    static get(id){
        return new Promise((resolve /*ok */,reject /*error */)=>{
            if(id===1){
                resolve({id})
            }
            else{
                reject("el cliente no existe")
            }
        })
    }
}
class InvoiceService{
    static get(clientId){
        return new Promise((resolve,reject)=>{
            if(clientId===1){
                resolve({clientId,invoices:[]})
            }
            else{
                reject("el cliente no tiene facturas")
            }
        })
    }
}

//resolve->then(n)
//reject->catch(1)

function main(id){
    CustomerService.get(id)
        .then(customer=>InvoiceService.get(customer.id))
        .then(invoices=>console.log(invoices))
        .catch(err=>console.log(err))
}
main(id)