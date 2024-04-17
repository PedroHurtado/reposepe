class CustomerService{
    static async get(id){
        if(id===1){
            return {id}
        }
        throw "El cliente no existe"
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

async function main(id){
   try{
    const {id} = await CustomerService.get(id)
    const invoices = await InvoiceService.get(id)
    console.log(invoices)
   }
   catch(err){
    console.log(err)
   }
   finally{
    console.log("finally")
   }
}
main(id)