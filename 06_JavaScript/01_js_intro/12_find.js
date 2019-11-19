// for loop
var students = [
    { name : '서혁진' , age : 26 },
    { name : '오은애' , age : 26 },
    { name : '공선아' , age : 25 },
    { name : '이도현' , age : 26 },
    { name : '최주현' , age : 27 },
]

// ES5
for ( var i = 0; i < students.length; i++ ) {
    if ( students[i].age === 27 ){
        student = students[i]
        break       // 원하는 조건 도달하면 loop 탈출
    }
}

console.log(student)


// find Helpler
const STUDENTS = [
    { name : '서혁진' , age : 26 },
    { name : '오은애' , age : 26 },
    { name : '공선아' , age : 25 },
    { name : '이도현' , age : 26 },
    { name : '최주현' , age : 27 },
]

// const student = STUDENTS.find(function(student) {
//     return students.age === 27
// })

// 화살표함수
const student = STUDENTS.find( student => students.age === 27 )

console.log(student)