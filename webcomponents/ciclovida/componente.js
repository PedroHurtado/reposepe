const template = document.getElementById('tel-title')

class Componente extends HTMLElement{
    static observedAttributes = ["date"];
    constructor(){
        super()
        const shadow = this.attachShadow({mode:'closed'})
        shadow.appendChild(template.content.cloneNode(true))
        

        /*
         open->shadowRoot
         closed->null
         */
        //shadow.innerHTML = '<slot></slot>'
        //https://developer.mozilla.org/es/docs/Web/HTML/Element/slot

        /*
            <slot name="toolbar"></slot>
            <slot name="menu"></slot>
            <slot name="content"></slot>
            <slot></slot>
            <div slot="toolbar">
            <div slot="menu">
            <div slot="content">
        */
        console.log("constructor")
    }
    connectedCallback(){
        console.log("connected callback")
    }
    set data(value){
        console.log(value)
    }
    disconnectedCallback(){
        console.log("disconected callback")
    }
    /*
        no puedo pasar object
    */
    attributeChangedCallback(name,oldValue,newValue){
        console.log(`${name} ${oldValue} ${newValue}`)
    }
}

/*nombre valido
    prefix-name
*/

/*nombre invalidos
    name
    prefix_name
*/

/* 
https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_custom_elements
*/
customElements.define('tel-title', Componente)
