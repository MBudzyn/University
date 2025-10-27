function doThings() {
    return Promise.resolve("ok");
}

doThings()
    .then(res => {
        console.log(res);
    })


//to samo co
async function doThings() {
    return "ok";
}

doThings()
    .then(res => {
        console.log("elo elo" + res); //"ok"
    });