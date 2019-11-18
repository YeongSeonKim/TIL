# JavaScript Syntax basics

## 0. 사전준비

### 0.1 `Node.js`설치

- Node.js 발표와 동시에 JavaScript가 브라우저 종속적인 언어가 아니라 서버 구축까지 가능해지며서  핫한 언어로 급부상.
- Express.js(서버), React.js(프론트), Vue.js(프론트) 등 JavaScript 기반의 수 많은 프레임워크, 라이브러리들이 현대 웹 개발 트렌드를 주도하고 있음.

- [node.js 공식 홈페이지](https://nodejs.org/ko/)
  - **LTS** Version(안정적)
  - **Windows Installer (.msi) 64bit**

![1574044567790](assets/1574044567790.png)

- 설치 확인

```bash
$ node -v
v12.13.0
```

![1574048392577](assets/1574048392577.png)

### 0.2 VScode Python & JavaScript 인덴팅 설정

settings.json

```json
{
    ...
    "editor.tabSize": 2,
    "[python]" : {
        "editor.tabSize" : 4,
    },
	...
}
```

### 0.3 Naming convention

- `lowerCamelCase`

  - 단봉낙타표기법

  ![1574044582085](assets/1574044582085.png)

  - JavaScrip의 기본 표기법

- `UpperCamelCase`
  
  - 쌍봉낙타표기법
- `snake_case`
- `kebob_case`

### 0.4 Extensions (추천)

- `auto close tag`
- `rainbow brackets`
- `indent-rainbow`



## 1. Variable

00_variable.js

```js
// 00_variable.js
// var 사용하면 안된다. ex6이전에 사용되던 방식
// hoisting(끌어올림)
// 기본적으로 밑에 둘만 사용
let
const
```

### 1.1 let (변수)

- 값을 재할당 할 수 있는 변수를 선언하는 키워드

- 변수 선언은 한 번만 할 수 있다.

  - 하지만 할당은 여러번 할수 있다.

  ```js
  // 00_variable.js
  
  // let(변수)
  let x = 1
  x = 3       // 재할당 가능
  console.log(x)
  ```

  ![1574046556306](assets/1574046556306.png)

- 블록 유효 범위 (`Block Scope`) 를 갖는 지역변수

  ```js
  // 00_variable.js
  
  // let(변수)
  let x = 1
  if(x === 1){
      // if문 만큼의 유효범위르 가지고 있다.
      // 벗어나면 접근 불가능
      let x = 2
      console.log(x)  // 2
  }   
  console.log(x)      // 1
  ```

  ![1574046769863](assets/1574046769863.png)

### 1.2 const (상수)

- 값이 변하지 않는 상수를 선언하는 키워드

  - 상수의 값은 재할당을 통해 바뀔 수 없고, 재선언도 불가능하다.

- let과 동일하게 `Block Scope` 를 가진다.

- 웬만하면 모든 선언에서 상수를 써야 한다.

  - 일단 상수를 사용하고, 값이 바뀌는게 자연스러운 상황이면 그때 변수(let)로 바꿔서 사용하는 것을 권장한다.

  ```js
  // 00_variable.js
  
  // const(상수)
  // 초기값을 생략하면 Error
  // const MY_FAV
  // MY_FAV를 상수로 정의하고 그 값을 7로 함.
  const MY_FAV = 7
  console.log('My Favorite number is ....' + MY_FAV)
  ```

  ![1574046640546](assets/1574046640546.png)

- 초기값을 생략하면 **ERROR** 발생

- 변수와 상수는 어디에 써야 할까?
  - 어디에 변수를 쓰고, 어디에는 상수를 쓰고 하는 등의 결절은 프로그래머의 몫
  - **파이 근삿값**과 같은 값은 상수가 적절 (변할 일이 없는 값)
- `var` **vs** `let` **vs** `const`
  - `var` : 할당 및 선언 자유, 함수 스코프
  - `let` :  할당 자유, 선언은 한번만, 블록 스코프
  - `const` : 할당 한번만, 선언도 한번만, 블록 스코프
- var 은 호이스팅과 같은 여러 문제를 야기하기 때문에, 앞으로 let 과 const를 사용해서 개발을 진행하자.



## 2. 조건문

### 2.1 `if`문

- 파이썬의 if문과 흡사!! `elif` 만 `else if`로 바꾸면 됨
- console
  - ctrl + r :새로고침
  - shift + enter : 줄바꿈

```js
// 01_if.js
const userName = prompt('니 이름은 뭐니?')
let message = ``
if ( userName === '도현'){
    message = `<h1>유단자... 까불지 마요...</h1>`
} else if (userName === '혁진'){
    message = `<h1>감자... 감자합니다...</h1>`
} else {
    message = `<h1>${userName}...누구??</h1>`
}
document.write(message)
```

![1574052895091](assets/1574052895091.png)

![1574052919084](assets/1574052919084.png)

## 3. 반복문

### 3.1 while

```js
// 02_loop.js
// while loop
// while 키워드 뒤에 나오는 조건이 true인 경우 반복

let i = 0
while (i < 6){
    console.log(i)
    i++
}
```

![1574052971234](assets/1574052971234.png)

### 3.2 for

````js
// 02_loop.js
// for loop
// JavaScript 가장 기본적인 반복문. for문에서 사용할 변수를 하나 정의하고 ,
// 그 변수가 특정조건에 false 값이 될 때까지 계속 연산-반복

for (let j = 0; j < 6; j++) {
    console.log(j)
}
````

![1574053031262](assets/1574053031262.png)

### 3.3 Python for in 문법처럼 비슷하게 사용

```js
// 02_loop.js
// Python의 for in 문법과 비슷하게 사용 가능!
const numbers = [1, 2, 3, 4, 5]
for (let number of numbers) {
    console.log(number)
}
for (let number of [1, 2, 3, 4, 5]) {
    console.log(number)
}
// number값 재할당 필요없으면 상수 사용 가능
for (const number of [1, 2, 3, 4, 5]) {
    console.log(number)
}
```

![1574053155176](assets/1574053155176.png)



## 4. 함수

> 함수 선언식 (statement) : 코드가 실행되기 전에 로드됨.
>
> 함수 표현식(expression) : 인터프리터가 해당 코드에 도다 했을 때 로드됨

### 4.1 선언식

````js
// 03_function.js
// 선언식
function add(num1, num2){
    return num1 + num2
}
console.log(add(1, 2))
````

### 4.2 표현식

```js
// 03_function.js
// 표현식
const sub = function(num1, num2){
    return num1 - num2
}
console.log(sub(2, 1))
```

- 타입화인

```js
// 03_function.js
// 타입 확인하면 둘다 function으로 동일!
console.log(typeof add)
console.log(typeof sub)
```



### 5. 화살표 함수(Arrow function)

- ES6 이후
- **function과 중괄호 숫자를 줄이려고 고안된 문법**
  - function 키워드 생략 가능
  - 함수에 매개변수 하나 -> `()`생략 가능
  - 함수 바디에 표현식 하나 -> `{}`, `return` 생략가능
- 화살표 함수의 경우 function 키워드로 정의한 함수와 100% 동일하지 않다. 
- 화살표 함수는 항상 **익명 함수**

```js
// 03_function.js
// 화살표 함수 (Arrow function)
const iot1 = function(name) {
    return `hello ${name}!!`
}

// 1. function 키워드 삭제
const iot1 = (name) => { return `hello! ${name}` }
// 2. () 생략 (함수 매개변수 하나일 경우)
const iot1 = name => { return `hello! ${name}` }
// 3. {}, return 생략 (바디에 표현식 1개)
const iot1 = name => `hello! ${name}`
```



실습

```js
// 03_function.js
// [실습] 3단계에 걸쳐 화살표 함수로 바꿔보기
let square = function(num) {
    return num ** 2
}

// 1. function 키워드 삭제
square = (num) => { return num ** 2 }
// 2. () 생략 (함수 매개변수 하나일 경우)
square = num => { return num ** 2 }
// 3. {}, return 생략 (바디에 표현식 1개)
square = num => num ** 2
// console.log(square(2))
```

![1574053560476](assets/1574053560476.png)







## 5. 익명 / 1회용 함수 (Anonymous function)

> JavaScript에서는 1회용으로 사용하는 함수는 이름을 짓지 않을 수 있다.
>
> 일반적으로는 함수를 정의, 변수에 함수르 저장하는 과정 등을 거쳐서 실행한다. 하지만 즉시실행함수는 함수가 선언되자마자 즉시 실행된다.
>
> 사용 이유?
>
> **초기화**에 사용한다
>
> - 즉시실행함수는 선언되자마자 실행되기 때문에, 같은 함수를 다시 호출할 수는 없다. 그래서 초기화 부분에 주로 사용된다.

```js
// JS에서는 1회용으로 사용할 함수는 이름을 짓지 않을 수 있다.
// function 키워드를 활용해서 함수를 선언할 때는, 이름을 지정하지 않으면 에러가 난다.
function (num) { return num ** 3 }

// 1. 기명함수로 만들기(변수, 상수에 할당)
const cube = function (num) { return num ** 3 }
// 화살표 함수는 기본적으로 익명 함수지만, 변수 및 상수에 할당해서 기명함수처럼 사용 가능
const squareRoot = num => num ** 0.5

// 2. 익명함수 바로 실행시키기
console.log((function (num) { return num ** 3})(2))
console.log((num => num ** 0.5)(4))
```

## 6. 배열(Arr)

```js
// 04_array.js

const numbers = [1, 2, 3, 4, 5]

numbers[0]      // 1
numbers[-1]     // undefined -> 정확한 양의 정수만 가능
numbers.length  // 5


// 원본 파괴!
numbers.reverse()       // [5, 4, 3, 2, 1]
console.log(numbers)    // [5, 4, 3, 2, 1]
numbers.reverse()       // [1, 2, 3, 4, 5]
console.log(numbers)    // [1, 2, 3, 4, 5]

// push - 배열 길이 return
numbers.push('a')       // 6
console.log(numbers)    // [1, 2, 3, 4, 5, "a"]

// pop - 배열 가장 마지막 요소 제거 후 return
numbers.pop()           // "a"
console.log(numbers)    // [1, 2, 3, 4, 5]

// unshift - 배열 가장 앞에 요소 추가
numbers.unshift('a')        // 6 ( 배열의 새로운 length )
console.log(numbers)        // ["a", 1, 2, 3, 4, 5]

// shift - 배열의 가장 첫번째 요소 제거후 return
numbers.shift()         // "a"
console.log(numbers)    // [1, 2, 3, 4, 5]

(((())))
{{{{}}}}
// extensions -> rainbow brackets & indent Brackets

numbers.push('a','b')        
console.log(numbers)        // [1, 2, 3, 4, 5, "a", "b"]
numbers.unshift('a')
console.log(numbers)        // ["a", 1, 2, 3, 4, 5, "a", "b"]

// 중복된 요소가 존재하는 경우 처음 찾은 요소의 index return
numbers.indexOf('a')        // 0
numbers.indexOf('b')        // 8
numbers.indexOf('c')        // 찾는 요소가 없으면 -1

/*
    join
    배열의 요소를 join 함수 인자를 기준으로 묶어서 문자열로 return
*/
numbers.join()      // "a,1,2,3,4,5,a,b" (기본값은 ',')
numbers.join('-')   // "a-1-2-3-4-5-a-b"
numbers.join('')    // "a12345ab"
```

## 7. 객체(Object)

```js
// 05_object.js

const me = {
    name : '영선',   // key가 한 단어일 때
    'phone number' : '01051807243',     // key가 여러 단어일 때
    appleProducts: {
        iphone:'8',
        watch:'series5',
        macbook:'pro2019'
    }
}

me.name         // "영선"
me['name']      // "영선"
// key가 여러단어 일때 []로 접근!
me['phone number']      // "01051807243"
me.appleProducts        // {iphone: "8", watch: "series5", macbook: "pro2019"}
me.appleProducts.iphone // "8"
```

