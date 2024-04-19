class Foo {
    #x;
    constructor(x) {
        this.#x = x;
    }
    get x() {
        return this.#x;
    }
}

const foo = new Foo(30)
console.log(foo.x)
foo.#x=20
console.log(foo.#x)