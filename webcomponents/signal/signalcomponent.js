import { signal } from "./signal.js"

//https://developer.chrome.com/docs/css-ui/declarative-shadow-dom?hl=es-419

class SignalComponent extends HTMLElement{
    counter = signal(0)
    constructor(){
        super();
        const shadow = this.attachShadow({mode:'open'})
        const button = document.createElement('button')
        this.counter.subscribe(()=>button.textContent = `Count:${this.counter()}`)
        shadow.appendChild(button)
    }
    handlerClick(ev){
        ev.stopPropagation();
        this.counter.set(this.counter()+1)
    }
    connectedCallback(){
        this.addEventListener('click', this.handlerClick)
    }
    disconnectedCallback(){
        this.removeEventListener('click',this.handlerClick)
    }
}
customElements.define('tel-signal',SignalComponent)