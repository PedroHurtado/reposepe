function logger(name:string){
    return function (target: any, propertyKey: string, descriptor: PropertyDescriptor) {
      const oldFunction = descriptor.value
      descriptor.value = function(...args:[]){
       console.log(name)
       console.log("before")
       const result = oldFunction.apply(this,args)
       console.log("after")
      }
   };
 }
 
 class Foo{
    @logger("Hello")
    write(){
       console.log("write")
    }
 }
 
 new Foo().write()