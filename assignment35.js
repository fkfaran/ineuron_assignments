// 1. Shopping cart operations
let shoppingCart = ['Milk', 'Coffee', 'Tea', 'Honey'];

// a. Add 'Meat' to beginning if not exists
if (!shoppingCart.includes('Meat')) shoppingCart.unshift('Meat');

// b. Add 'Sugar' to end if not exists
if (!shoppingCart.includes('Sugar')) shoppingCart.push('Sugar');

// c. Remove 'Honey' if allergic
let allergicToHoney = true;
if (allergicToHoney) {
    shoppingCart = shoppingCart.filter(item => item !== 'Honey');
}

// d. Modify 'Tea' to 'Green Tea'
let teaIndex = shoppingCart.indexOf('Tea');
if (teaIndex !== -1) shoppingCart[teaIndex] = 'Green Tea';

console.log('Updated Shopping Cart:', shoppingCart);

// 2. Check for Sass in webTechs array
let webTechs = ['HTML', 'CSS', 'JS', 'React', 'Node'];
if (webTechs.includes('Sass')) {
    console.log('Sass is a CSS preprocess');
} else {
    webTechs.push('Sass');
    console.log('Updated WebTechs:', webTechs);
}

// 3. Students ages
const ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24];
ages.sort((a,b) => a-b);
console.log('Sorted ages:', ages);

let minAge = ages[0];
let maxAge = ages[ages.length-1];
console.log('Min Age:', minAge);
console.log('Max Age:', maxAge);

// Median
let median;
let mid = Math.floor(ages.length/2);
if (ages.length % 2 === 0) {
    median = (ages[mid-1] + ages[mid])/2;
} else {
    median = ages[mid];
}
console.log('Median Age:', median);

// Average
let sum = ages.reduce((acc, val) => acc + val, 0);
let average = sum / ages.length;
console.log('Average Age:', average);

// Range
let range = maxAge - minAge;
console.log('Range of ages:', range);

// Compare |min-average| and |max-average|
console.log('Abs(min-average):', Math.abs(minAge - average));
console.log('Abs(max-average):', Math.abs(maxAge - average));

// 4. Print array as sentence
const itCompanies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM','Oracle', 'Amazon'];
console.log(`${itCompanies.join(', ')} are big IT companies.`);

// 5. Uppercase each company name
itCompanies.forEach(company => console.log(company.toUpperCase()));

// 6. Generate random ID of any length
function generateId(length) {
    let chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let id = '';
    for (let i=0; i<length; i++) {
        id += chars.charAt(Math.floor(Math.random()*chars.length));
    }
    return id;
}
console.log('Random ID (10 chars):', generateId(10));

// 7. Generate random hexadecimal number
function generateHex(length) {
    let hex = '';
    let chars = '0123456789ABCDEF';
    for (let i=0; i<length; i++) {
        hex += chars.charAt(Math.floor(Math.random()*16));
    }
    return '0x'+hex;
}
console.log('Random Hex:', generateHex(6));

// 8. Reverse fruit array using loop
let fruits = ['banana', 'orange', 'mango', 'lemon'];
let reversedFruits = [];
for (let i=fruits.length-1; i>=0; i--) {
    reversedFruits.push(fruits[i]);
}
console.log('Reversed Fruits:', reversedFruits);

// 9. Iterate through web technologies
const webTechList = ["HTML", "CSS", "JS", "React", "Redux", "Node", "Express", "MongoDB"];
for (let tech of webTechList) {
    console.log(tech);
}

// 10. Human readable time format
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
