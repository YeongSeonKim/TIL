// // for loop 활용
// var students = [
//     { name : '서혁진', type : 'male' },
//     { name : '공선아', type : 'female' },
//     { name : '남찬우', type : 'male' },
//     { name : '이도현', type : 'female' },
// ]

// var strongStudents = []
// // students 라는 배열의 객체들 중 type이 female인 요소들만 뽑기!
// // students 원본 자체를 바꾸고 싶은게 아니라, 원하는 조건에 맞는
// // 데이터들만 골라서 새로운 배열 만들기.
// // ES5
// for (var i = 0; i < students.length; i++) {
//     if ( students[i].type === 'female' ) {
//         strongStudents.push(students[i])
//     }
// }

// console.log(students)               // 원본 유지
// console.log(strongStudents)         // 새로운 배열
// console.log(students[1].name)       // 객체 내 속성 접근하기


// // filter Helper 활용
// const STUDENTS = [
//     { name : '서혁진', type : 'male' },
//     { name : '공선아', type : 'female' },
//     { name : '남찬우', type : 'male' },
//     { name : '이도현', type : 'female' },
// ]

// // const STRONG_STUDENTS = STUDENT.filter(function(student) {
// //     return student.type === 'female'
// // })

// // 한 줄로 바꾸기
// const STRONG_STUDENTS = STUDENTS.filter( student => student.type === 'female')

// console.log(STRONG_STUDENTS)        // 새로운 배열
// console.log(STUDENTS)               // 원본 유지


// filter Helpler를 사용해서 numbers 배열 중 50보다 큰 값만 필터링해서 새로운 배열에 저장하기

const numbers = [15, 35, 13, 36, 69, 3, 61, 55, 99, 5]
const newNumbers = numbers.filter(function(number) {
    return number > 50
})

// const newNumbers = numbers.filter( number => number > 50 )

console.log(numbers)
console.log(newNumbers)