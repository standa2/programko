let tlacitko = document.querySelector("#tlacitko")
let input1 = document.querySelector("#input1")
let input2 = document.querySelector("#input2")
let nadpis = document.getElementById("nadpis")
tlacitko.addEventListener("click", zmenNadpis)

function zmenNadpis() {
    let textInputu1 = input1.value
    let textInputu2 = input2.value
    textInputu2 = parseInt(textInputu2)
    if (textInputu1 === "C") {
        nadpis.innerText = prevod1(textInputu2)
    } else if (textInputu1 === "F") {
        nadpis.innerText = prevod2(textInputu2)
    }
}

function prevod1(c) {
    let farenheit = c * 33.8
    return farenheit
}

function prevod2(farenheit) {
    let c = (farenheit - 32) / 1.8
    return c
}
