
// Task 1
console.log(capitalize("alice"));

function capitalize (str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}
// Task 2
function capitalizeSentence (str) {
    return str.split(" ").map(capitalize).join(" ");
}
console.log(capitalizeSentence("alice"));
console.log(capitalizeSentence("alice in wonderland"));

// Task 3

const ids = new Set();

const generateId = () => {
        let id = 0;

        do {
            id++;
        } while (ids.has(id));

        ids.add(id)
        return id;

};

const ids2 = [];

const generateId2 = () => {
    let id = 0;

    do {
        id++;
    } while (ids2.includes(id));

    ids2.push(id);
    return id;
};


console.time("myGen");

for (let i = 0; i < 3000; i++) {
    generateId();
}

console.timeEnd("myGen");
console.time("defaultGen");

for (let i = 0; i < 3000; i++) {
    generateId2()
}

console.timeEnd("defaultGen");
// Task 4

function compareObjects(a, b) {
    if (a === b) return true;
    const keysA = Object.keys(a);
    const keysB = Object.keys(b);

    if (keysA.length !== keysB.length) return false;

    for (let key of keysA) {
        if (!keysB.includes(key)) return false;
        if (!compareObjects(a[key], b[key])) return false;
    }

    return true;
}

const obj1 = {
    name: "Alice",
    age: 25,
    address: {
        city: "Wonderland",
        country: "Fantasy",
    },
};

const obj2 = {
    name: "Alice",
    age: 25,
    address: {
        city: "Wonderland",
        country: "Fantasy",
    },
};

const obj3 = {
    age: 25,
    address: {
        city: "Wonderland",
        country: "Fantasy",
    },
    name: "Alice",
};

const obj4 = {
    name: "Alice",
    age: 25,
    address: {
        city: "Not Wonderland",
        country: "Fantasy",
    },
};

const obj5 = {
    name: "Alice",
};

console.log("Should be True:", compareObjects(obj1, obj2));
console.log("Should be True:", compareObjects(obj1, obj3));
console.log("Should be False:", compareObjects(obj1, obj4));
console.log("Should be True:", compareObjects(obj2, obj3));
console.log("Should be False:", compareObjects(obj2, obj4));
console.log("Should be False:", compareObjects(obj3, obj4));
console.log("Should be False:", compareObjects(obj1, obj5));
console.log("Should be False:", compareObjects(obj5, obj1));

// Task 5

function validateTitleOrAuthor(titleOrAuthor) {
    if (!titleOrAuthor || typeof titleOrAuthor !== "string") {
        throw new Error("Tittle or author must by not empty string");
    }
    return true;
}

function validatePages(pages){
    if (!pages || typeof pages !== "number" || pages <= 0) {
        throw new Error("Pages must be positive number");
    }
    return true;
}
function validateIsAvailable(isAvailable){
    if (typeof isAvailable !== "boolean") {
        throw new Error("isAvailable must be boolean");
    }
    return true;
}

function validateRatings(ratings){
    for (const key in ratings) {
        const rating = ratings[key];
        if (typeof rating !== "number" || rating < 0 || rating > 5) {
            throw new Error("All ratings must be numbers between 0 and 5");
        }
    }
    return true;
}
function validateInput(title, author, pages, isAvailable, ratings) {
    validateTitleOrAuthor(title);
    validateTitleOrAuthor(author);
    validatePages(pages);
    validateIsAvailable(isAvailable);
    validateRatings(ratings);
}
let library = [];

const addBookToLibrary = (title, author, pages, isAvailable, ratings) => {
    validateInput(title, author, pages, isAvailable, ratings);

    library.push({
        title,
        author,
        pages,
        available: isAvailable,
        ratings,
    });
};
// task 6
function testAddBookToLibrary() {
    const testCases = [
        { testCase: ["", "Author", 200, true, []], shouldFail: true },
        { testCase: ["Title", "", 200, true, []], shouldFail: true },
        { testCase: ["Title", "Author", -1, true, []], shouldFail: true },
        { testCase: ["Title", "Author", 200, "yes", []], shouldFail: true },
        { testCase: ["Title", "Author", 200, true, [1, 2, 3, 6]], shouldFail: true },
        { testCase: ["Title", "Author", 200, true, [1, 2, 3, "yes"]], shouldFail: true },
        { testCase: ["Title", "Author", 200, true, [1, 2, 3, {}]], shouldFail: true },
        { testCase: ["Title", "Author", 200, true, []], shouldFail: false },
        { testCase: ["Title", "Author", 200, true, [1, 2, 3]], shouldFail: false },
        { testCase: ["Title", "Author", 200, true, [1, 2, 3, 4]], shouldFail: false },
        { testCase: ["Title", "Author", 200, true, [1, 2, 3, 4, 5]], shouldFail: false },
        { testCase: ["Title", "Author", 200, true, [1, 2, 3, 4, 5]], shouldFail: false },
    ];

    for (const caseData of testCases) {
        const { testCase: args, shouldFail } = caseData;
        const [title, author, pages, isAvailable, ratings] = args;

        console.log("Test Begin -------------------------");

        try {

            addBookToLibrary(title, author, pages, isAvailable, ratings);
            if (shouldFail) {
                console.error(`Test failed (expected failure, but it passed): ${JSON.stringify(args)}`);
            } else {
                console.log(`Test passed (as expected): ${JSON.stringify(args)}`);
            }
        } catch (error) {
            if (shouldFail) {
                console.log(`Test passed (expected failure): ${JSON.stringify(args)}`);
            } else {
                console.error(`Test failed (unexpected error): ${JSON.stringify(args)}`);
                console.error(error.message);
            }
        }
        console.log("Test End ---------------------------");
    }
}


testAddBookToLibrary();
// task 7

function addBooksToLibrary(books) {
    for (const book of books) {
        const [title, author, pages, isAvailable, ratings] = book;
        try {
            validateInput(title, author, pages, isAvailable, ratings);
        } catch (error) {
            console.error(`Validation failed for book: ${title}`);
            console.error(error.message);
            console.log("Skipping this book.");
            continue;
        }
        addBookToLibrary(title, author, pages, isAvailable, ratings);
    }
}

const books2 = [
    ["Alice in Wonderland", "Lewis Carroll", 200, true, [1, 2, 3]],
    ["1984", "George Orwell", 300, true, [4, 5]],
    ["The Great Gatsby", "F. Scott Fitzgerald", 150, true, [3, 4]],
    ["To Kill a Mockingbird", "Harper Lee", 250, true, [2, 3]],
    ["The Catcher in the Rye", "J.D. Salinger", 200, true, [1, 2]],
    ["The Hobbit", "J.R.R. Tolkien", 300, true, [4, 5]],
    ["Fahrenheit 451", "Ray Bradbury", 200, true, [3, 4]],
    ["Brave New World", "Aldous Huxley", 250, true, [2, 3]],
    ["The Alchemist", "Paulo Coelho", 200, true, [1, 2]],
    ["The Picture of Dorian Gray", "Oscar Wilde", 300, true, [4, 5]],
];
addBooksToLibrary(books2);
console.log(library);