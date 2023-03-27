
function calculate() {
    let from = document.getElementById("from").value;
    let weightInput = document.getElementById("weightInput").value;

    let parent = document.getElementById("newCalcs");

    let valCode = validateInput(from, weightInput);
    let newD = document.createElement('div');
    let newP = document.createElement('p');

    if (valCode === -1) {
        newD.classList = "stuff-box sun"
        newD.onclick = function() { deleteRecord(parent, newD) }

        newP.textContent = "Error: invalid input"
        newP.style.textAlign = "center"
    } else {
        newD.classList = "stuff-box purple"
        newD.onclick = function() { deleteRecord(parent, newD) }

        //TODO: convert weight to Troy Oz
        //TODO: multiply by price of gold

        newP.textContent = weightInput + " " + from + " of gold is worth $____"
        newP.style.textAlign = "center"
    }

    newD.appendChild(newP);
    parent.prepend(newD);
}

function deleteRecord(parent, toDelete) {
    parent.removeChild(toDelete);
}

function validateInput(from, weightInput) {

    let validUnits = ["T", "g", "t_oz", "kg", "lb", "oz"];
    if (!validUnits.includes(from)) {
        return -1;
    }
    if (weightInput === "") {
        return -1;
    }
    let toFloat = Number.parseFloat(weightInput);

    if (Number.isNaN(toFloat) || Math.sign(toFloat) === -1) {
        return -1;
    }

    return toFloat;
}

function getPrice() {
    let url = "https://data.nasdaq.com/api/v3/datasets/LBMA/GOLD/data.json?api_key=afHh9D4FGtELuouNAZ26&rows=1";
    fetch(url)
        .then( response => response.json() )
        .then( json => {
            let theData = json;
            price = theData.dataset_data.data[0][1];
            let priceDisplay = document.getElementById("priceDisplay");
            priceDisplay.innerHTML = "The current price of gold is " + price + " USD per Troy Oz"
        })
}

let price = -1;
getPrice()

