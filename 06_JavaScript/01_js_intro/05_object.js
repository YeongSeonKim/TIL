const me = {
    name : '영선',   // key가 한 단어일 때
    'phone number' : '01051807243',     // key가 여러 단어일 때
    appleProducts: {
        iphone:'8',
        watch:'series5',
        macbook:'pro2019'
    }
}

/*
me.name         // "영선"
me['name']      // "영선"
// key가 여러단어 일때 []로 접근!
me['phone number']      // "01051807243"
me.appleProducts        // {iphone: "8", watch: "series5", macbook: "pro2019"}
me.appleProducts.iphone // "8"
*/

console.log(me.appleProducts)
console.log(me.appleProducts.iphone)