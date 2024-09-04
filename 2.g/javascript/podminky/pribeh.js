let tlacitko = document.querySelector("#tlacitko")
let nadpis = document.getElementById("nadpis")
let input = document.querySelector("#input")
let nadpisa = document.getElementById("nadpisa")
tlacitko.addEventListener("click", zmenNadpis)

function zmenNadpis() {
    let textInputu1 = input.value
    let textInputu2 = input.value
    let textInputu3 = input.value

    if (textInputu) {
        input.value = ""
    }
    if (textInputu2) {
        input.value = ""
    }
    if (textInputu3) {
        input.value = ""
        nadpisa.innerText = textInputu1 + textInputu2 + textInputu3
    }
}
