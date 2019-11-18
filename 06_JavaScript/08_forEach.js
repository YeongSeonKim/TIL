// // ES5 for loop
// var iot1 = ['도현','혁진','은애']
// for (var i = 0; i < iot1.length; i++) {
//     console.log(iot1[i])
// }

// // ES6+
// const IOT1 = ['수연', '승찬', '한석', '경희', '영선']
// IOT1.forEach(function(student) {
//     console.log(student)
// })

// // 한줄로 리팩토링 가능!
// IOT1.forEach( student => console.log(student) )

// const result = IOT1.forEach( 
//     student => console.log(student) 
// )
// console.log(result) // undefined


// // [실습] for 를 forEach로 바꾸기!
// function handleStudents() {
//     const students = [
//         { id:1, name:'오은애', status:'응애?'},
//         { id:15, name:'서혁진', status:'기염듕이...'},
//         { id:28, name:'김영선', status:'너무쉽네..JS'},
//     ]
//     // for
//     for (let i = 0; i < students.length; i++) {
//         console.log(students[i])
//         console.log(students[i].name)
//         console.log(students[i].status)
//     }
//     // forEach
//     students.forEach(function(student) {
//         console.log(student)
//         console.log(student.name)
//         console.log(student.status)
//     })
//     console.log()
// }
// handleStudents()

// [실습] images 배열 안에 있는 정보를 곱해 넓이를 구하여 areas 배열에 저장하세요.
const images = [
    { height : 30, width : 55 },
    { height : 50, width : 178 },
    { height : 81, width : 35 },
]
const areas = []

// 정답코드 (forEach 활용)
images.forEach(function(image) {
    areas.push(image.height * image.width)
})

console.log(areas)