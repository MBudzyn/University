

/**
 * @typedef {Object} Product
 * @property {string} name - The name of the product
 * @property {number} id - The id of the product
 * @property {number} count - The count of the product to be bought
 * @property {Date} date - The last possible date of the product to be bought
 * @property {boolean} isBought - The status of the product
 * @property {number} [price] - The price of the product (optional)
 */

/** @type {Product[]} */
let product_list = [];

/**
 * Class representing a product.
 */
class Product {
    constructor(name, id, count, date, isBought, price) {
        this.name = name;
        this.id = id;
        this.count = count;
        this.date = date;
        this.isBought = isBought;
        this.price = price;
    }
}

/**
 * Adds a product to the list.
 * @param {string} name - Product name
 * @param {number} count - Product count
 * @param {string} date - Purchase date (string)
 * @param {boolean} isBought - Purchase status
 * @param {number} [price] - Product price (optional)
 */
function addProduct(name, count, date, isBought, price) {
    const id = Math.floor(Math.random() * 1000000);
    const dateObj = new Date(date);
    const product = new Product(name, id, count, dateObj, isBought, price);
    product_list.push(product);
}

/**
 * Removes product by ID.
 * @param {number} id - Product ID
 */
function removeProduct(id) {
    product_list = product_list.filter(product => product.id !== id);
}

/**
 * Finds product by ID.
 * @param {number} id - Product ID
 * @returns {Product|null}
 */
function getProduct(id) {
    const product = product_list.find(product => product.id === id);
    return product || null;
}

/**
 * Edits product name.
 * @param {number} id - Product ID
 * @param {string} name - New name
 */
function editProductName(id, name) {
    let product = getProduct(id);
    if (product) product.name = name;
}

/**
 * Edits product count.
 * @param {number} id - Product ID
 * @param {number} count - New count
 */
function editProductCount(id, count) {
    let product = getProduct(id);
    if (product) product.count = count;
}

/**
 * Edits product date.
 * @param {number} id - Product ID
 * @param {string} date - New date
 */
function editProductDate(id, date) {
    let product = getProduct(id);
    if (product) product.date = new Date(date);
}

/**
 * Edits product status.
 * @param {number} id - Product ID
 * @param {boolean} isBought - New status
 */
function editProductIsBought(id, isBought) {
    let product = getProduct(id);
    if (product) product.isBought = isBought;
    if (!isBought) editProductPrice(id, null);
}

/**
 * Edits product price.
 * @param {number} id - Product ID
 * @param {number} price - New price
 */
function editProductPrice(id, price) {
    let product = getProduct(id);
    if (product) product.price = price;
}

/**
 * Edits whole product.
 * @param {number} id - Product ID
 * @param {string} name
 * @param {number} count
 * @param {string} date
 * @param {boolean} isBought
 * @param {number} price
 */
function editProduct(id, name, count, date, isBought, price) {
    let product = getProduct(id);
    if (product) {
        editProductName(id, name);
        editProductCount(id, count);
        editProductDate(id, date);
        editProductIsBought(id, isBought);
        editProductPrice(id, price);
    }
}

/**
 * Moves product down in list.
 * @param {number} index - Product index
 */
function moveDown(index) {
    if (index > 0) {
        [product_list[index - 1], product_list[index]] = [product_list[index], product_list[index - 1]];
    }
}

/**
 * Moves product up in list.
 * @param {number} index - Product index
 */
function moveUp(index) {
    if (index < product_list.length - 1) {
        [product_list[index + 1], product_list[index]] = [product_list[index], product_list[index + 1]];
    }
}

/**
 * Changes product order.
 * @param {number} index - Product index
 * @param {boolean} isUp - Direction
 */
function changeOrder(index, isUp) {
    if (isUp) {
        moveUp(index);
    } else {
        moveDown(index);
    }
}

/**
 * Gets products that should be bought today.
 * @returns {Product[]}
 */
function getTodayNotBoughtProducts() {
    const today = new Date();
    return product_list.filter(product => {
        const productDate = new Date(product.date);
        return (
            productDate.getFullYear() === today.getFullYear() &&
            productDate.getMonth() === today.getMonth() &&
            productDate.getDate() === today.getDate() &&
            !product.isBought
        );
    });
}

/**
 * Adds price to bought product.
 * @param {number} id - Product ID
 * @param {number} price - Price
 */
function addPriceIfBought(id, price) {
    let product = getProduct(id);
    if (product && product.isBought) {
        product.price = price;
    }
}

/**
 * Sums price of today's bought products.
 * @param {string} dateString - Date in string format
 * @returns {number}
 */
function sumPriceOfBoughtProductsByDate(dateString) {
    const date = new Date(dateString);
    return product_list.reduce((sum, product) => {
        const productDate = new Date(product.date);
        if (
            product.isBought &&
            productDate.getFullYear() === date.getFullYear() &&
            productDate.getMonth() === date.getMonth() &&
            productDate.getDate() === date.getDate() &&
            product.price
        ) {
            return sum + product.price;
        }
        return sum;
    }, 0);
}

/**
 * apply to modify function to selected products.
 * @param {number[]} ids - List of product IDs
 * @param {(product: Product) => void} modifyFunction - Function to apply
 */
function modifyProducts(ids, modifyFunction) {
    ids.forEach(id => {
        let product = getProduct(id);
        if (product) {
            modifyFunction(product);
        }
    });
}

console.log("=== Dodawanie produktów ===");
addProduct("Chleb", 2, "2025-03-28", false, 4.5);
addProduct("Mleko", 1, "2025-03-28", true, 3);
addProduct("Masło", 1, "2025-03-29", false, 7);
console.log("Po dodaniu produktów:", product_list);

console.log("\n=== Edycja nazwy produktu ===");
console.log("Przed edycją:", product_list[0]);
editProductName(product_list[0].id, "Chleb razowy");
console.log("Po edycji:", product_list[0]);

console.log("\n=== Usuwanie produktu ===");
console.log("Lista przed usunięciem:", product_list.map(p => p.name));
removeProduct(product_list[2].id);
console.log("Lista po usunięciu (usunięto Masło):", product_list.map(p => p.name));

console.log("\n=== Zmiana statusu produktu na 'kupiony' ===");
console.log("Status przed:", product_list[0].isBought);
editProductIsBought(product_list[0].id, true);
console.log("Status po:", product_list[0].isBought);

console.log("\n=== Dodawanie ceny do kupionego produktu ===");
console.log("Cena przed:", product_list[0].price);
addPriceIfBought(product_list[0].id, 5);
console.log("Cena po:", product_list[0].price);

console.log("\n=== Zmiana kolejności produktów (przesunięcie w górę) ===");
console.log("Kolejność przed:", product_list.map(p => p.name));
changeOrder(0, true);
console.log("Kolejność po:", product_list.map(p => p.name));

console.log("\n=== Pobieranie produktów do kupienia dzisiaj ===");
console.log("Produkty do kupienia dziś:", getTodayNotBoughtProducts());

console.log("\n=== Sumowanie kosztu zakupionych produktów z datą 2025-03-28 ===");
const suma = sumPriceOfBoughtProductsByDate("2025-03-28");
console.log("Suma kosztów zakupionych produktów:", suma);

console.log("\n=== Masowa modyfikacja produktów (przewalutowanie ceny x4.5) ===");
console.log("Ceny przed:", product_list.map(p => p.price));
modifyProducts(
    product_list.map(p => p.id),
    (product) => {
        if (product.price) product.price = product.price * 4.5;
    }
);
console.log("Ceny po:", product_list.map(p => p.price));

