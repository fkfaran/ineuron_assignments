// 1. Declare variables and check data types
let firstName = "John";
let lastName = "Doe";
let country = "USA";
let city = "New York";
let age = 30;
let isMarried = false;
let year = 2025;

console.log(typeof firstName); // string
console.log(typeof lastName);  // string
console.log(typeof country);   // string
console.log(typeof city);      // string
console.log(typeof age);       // number
console.log(typeof isMarried); // boolean
console.log(typeof year);      // number

// 2. Boolean values
// a. Truthy statements
console.log(5 > 3);     // true
console.log("Hello");   // true
console.log([]);        // true

// b. Falsy statements
console.log(0);         // false
console.log("");        // false
console.log(null);      // false

// 3. Evaluate expressions
console.log(4 > 3 && 10 < 12);    // true
console.log(4 > 3 && 10 > 12);    // false
console.log(4 > 3 || 10 < 12);    // true
console.log(4 > 3 || 10 > 12);    // true
console.log(!(4 > 3));            // false
console.log(!(4 < 3));            // true
console.log(!false);              // true
console.log(!(4 > 3 && 10 < 12)); // false
console.log(!(4 > 3 && 10 > 12)); // true
console.log(!(4 === '4'));         // true

// 4. Check if a number is even
function isEven(number) {
    return number % 2 === 0;
}
console.log(isEven(10)); // true
console.log(isEven(7));  // false

// 5. Student grades
function getGrade(score) {
    if (score >= 80 && score <= 100) return 'A';
    else if (score >= 70 && score <= 79) return 'B';
    else if (score >= 60 && score <= 69) return 'C';
    else if (score >= 50 && score <= 59) return 'D';
    else return 'F';
}

console.log(getGrade(85)); // A
console.log(getGrade(72)); // B
console.log(getGrade(65)); // C
console.log(getGrade(55)); // D
console.log(getGrade(40)); // F

// 6. Number of days in a month
function getDaysInMonth(month, year) {
    return new Date(year, month, 0).getDate();
}
console.log(getDaysInMonth(2, 2024)); // 29 (leap year)
console.log(getDaysInMonth(2, 2023)); // 28
console.log(getDaysInMonth(4, 2025)); // 30

// 7. Human-readable time formats
let now = new Date();

function pad(n){ return n<10 ? '0'+n : n; }

let yyyy = now.getFullYear();
let mm = pad(now.getMonth()+1);
let dd = pad(now.getDate());
let hh = pad(now.getHours());
let min = pad(now.getMinutes());

console.log(`${yyyy}-${mm}-${dd} ${hh}:${min}`); // YYYY-MM-DD HH:mm
console.log(`${dd}-${mm}-${yyyy} ${hh}:${min}`); // DD-MM-YYYY HH:mm
console.log(`${dd}/${mm}/${yyyy} ${hh}:${min}`); // DD/MM/YYYY HH:mm

// 8. Dollar to rupees
let dollar = 10;
let rate = 82.23;
let rupees = dollar * rate;
console.log(`${dollar} USD = ${rupees} INR`);

// 9. Unit digit of a number
let number = 6693;
let unitDigit = number % 10;
console.log(`Unit digit of ${number} is ${unitDigit}`);

// 10. Area of circle
let radius = 5;
let area = Math.PI * radius * radius;
console.log(`Area of circle is ${area.toFixed(2)} having the radius ${radius}`);
