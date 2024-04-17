function internal(){
    console.log("foo default")
}
export function sum(a,b){
    return a+b
}
export function resta(a,b){
    return a-b
}
export function multiplicar(a,b){
    return a*b
}
export function dividir(a,b){
    return a/b
}
//solo un default
export default function foo(){
    internal();
}