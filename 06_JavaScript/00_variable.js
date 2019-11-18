// let(변수)
// let x = 1
// x = 3       // 재할당 가능
// console.log(x)

// let x = 1
// if(x === 1){
//     // if문 만큼의 유효범위르 가지고 있다.
//     // 벗어나면 접근 불가능
//     let x = 2
//     console.log(x)  // 2
// }   
// console.log(x)      // 1

// const(상수)
// 초기값을 생략하면 Error
// const MY_FAV
// MY_FAV를 상수로 정의하고 그 값을 7로 함.
const MY_FAV = 7
console.log('My Favorite number is ....' + MY_FAV)
// 상수 재할당 -> 에러 -> Assignment
// MY_FAV = 10

// 상수를 재선언 -> 에러
const MY_FAV = 20
let MY_FAV = 11

if(MY_FAV === 7){
    const MY_FAV = 11
    console.log(MY_FAV)
}
console.log(MY_FAV)