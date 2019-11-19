// Object -> String
const jsonData = JSON.stringify({
    도현 : '합기도',
    혁진 : '감자',
})
console.log(jsonData)           // {"도현":"합기도","혁진":"감자"}
console.log(typeof jsonData)    // string

// String -> Object
const parseData = JSON.parse(jsonData)
console.log(parseData)          // { '도현': '합기도', '혁진': '감자' }
console.log(typeof parseData)   // object


/*
    [Object vs JSON 간단정리]
    - Object : JavaScript의 Key-Vaule 페어의 자료구조
    - JSON : 데이터를 표현하기 위하 단순 문자열(string)
*/

