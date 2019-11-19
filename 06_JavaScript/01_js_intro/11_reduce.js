const tests = [90, 85, 77, 13, 58]

// const sum = tests.reduce(function(total, score) {
//     return total += score
// })

const sum = tests.reduce( (total, score) => total += score )

console.log(sum)