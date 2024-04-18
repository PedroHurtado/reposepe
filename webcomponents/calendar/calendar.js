import styles from "./calendar.css" with { type: "css" };
import {Day} from './day.js'

function* getDays(){
    for(let i=0;i<31;i++){
        yield i+1
    }
}

class Calendar extends HTMLElement{
    constructor(){
        super();
        const shadow = this.attachShadow({mode:'open'})
        shadow.adoptedStyleSheets = [styles]
        for(const day of getDays()){
            const dayDom = new Day();
            dayDom.setAttribute('data-day', day)
            dayDom.day = day
            shadow.appendChild(dayDom)
        }
    }
    handlerClick(ev){
        ev.stopPropagation();
        const node = ev.composedPath().find(n=>n.dataset && 'day' in n.dataset)
        if(node){
            const {day} = node.dataset
            console.log(day)            
        }
    }
    connectedCallback(){
        this.addEventListener('click', this.handlerClick)
    }
    disconnectedCallback(){
        this.removeEventListener('click',this.handlerClick)
    }
}
customElements.define('tel-calendar', Calendar)