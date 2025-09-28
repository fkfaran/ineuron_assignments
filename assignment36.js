// 1. Sum of all numbers from 0 to 100
let sumAll = 0;
for (let i = 0; i <= 100; i++) {
    sumAll += i;
}
console.log("Sum of numbers 0 to 100:", sumAll);

// 2. Sum of evens and odds from 0 to 100
let sumEvens = 0;
let sumOdds = 0;
for (let i = 0; i <= 100; i++) {
    if (i % 2 === 0) sumEvens += i;
    else sumOdds += i;
}
console.log("Sum of evens and odds:", [sumEvens, sumOdds]);

// 3. Generate random ID of any length
function generateRandomId(length) {
    let chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let id = '';
    for (let i = 0; i < length; i++) {
        id += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return id;
}
console.log("Random ID (12 chars):", generateRandomId(12));

// 4. Check countries containing 'and'
const countries = ['Finland', 'Sweden', 'Norway', 'Thailand', 'Denmark', 'Canada'];
let countriesWithAnd = countries.filter(c => c.toLowerCase().includes('and'));
if (countriesWithAnd.length > 0) console.log("Countries containing 'and':", countriesWithAnd);
else console.log("All these countries are without and");

// 5. Reverse fruit array using loop
const fruits = ['banana', 'orange', 'mango', 'lemon'];
let reversedFruits = [];
for (let i = fruits.length - 1; i >= 0; i--) {
    reversedFruits.push(fruits[i]);
}
console.log("Reversed Fruits:", reversedFruits);

// 6. Capitalize array function
function capitalizeArray(arr) {
    return arr.map(item => typeof item === 'string' ? item.toUpperCase() : item);
}
console.log(capitalizeArray(['apple','banana','mango']));

// 7. Sum of array items with type check
function sumOfArrayItems(arr) {
    if (!arr.every(item => typeof item === 'number')) return "Array contains non-number items!";
    return arr.reduce((sum, item) => sum + item, 0);
}
console.log(sumOfArrayItems([1,2,3,4])); // 10
console.log(sumOfArrayItems([1,2,'3',4])); // Error message

// 8. Modify fifth item in array
function modifyArray(arr, newValue) {
    if (arr.length < 5) return 'Item not found';
    arr[4] = newValue;
    return arr;
}
console.log(modifyArray([1,2,3,4,5,6], 'Modified'));
console.log(modifyArray([1,2,3], 'Modified'));

// 9. Check if all items in array are same data type
function isSameDataType(arr) {
    if (arr.length === 0) return true;
    const type = typeof arr[0];
    return arr.every(item => typeof item === type);
}
console.log(isSameDataType([1,2,3,4])); // true
console.log(isSameDataType([1,'2',3])); // false

// 10. Validate variable name
function isValidVariable(name) {
    const validPattern = /^[a-zA-Z_$][a-zA-Z0-9_$]*$/;
    return validPattern.test(name);
}
console.log(isValidVariable("myVar"));   // true
console.log(isValidVariable("_var1"));   // true
console.log(isValidVariable("$var2"));   // true
console.log(isValidVariable("2var"));    // false
console.log(isValidVariable("var-name")); // false
