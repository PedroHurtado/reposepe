import styles from "./day.css" assert { type: "css" };
export class Day extends HTMLElement{    
    constructor(){
        super()
        this.shadow = this.attachShadow({mode:'open'})
        this.shadow.adoptedStyleSheets = [styles]
    }
    set day(value){
        this.shadow.textContent = value
    }
}
customElements.define('tel-day', Day)
