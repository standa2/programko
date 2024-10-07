let tlacitko = document.querySelector("#tlacitko")
let nadpisa = document.getElementById("nadpisa")
let random = Math.floor(Math.random() * 6)
tlacitko.addEventListener("click", zmenNadpis)

function zmenNadpis() {
    if (random === 1) {
        nadpisa.innerText =
            "zemřeš za  7...6....5....4...3...2...1..........................................."
    } else if (random === 2) {
        nadpisa.innerText = "budeš pjevít"
    } else if (random === 3) {
        nadpisa.innerText =
            "budeš mít mony mony mony ...... must be funy ..... in a ritch mans warld."
    } else if (random === 4) {
        nadpisa.innerText = "pamatuj Víc je Míň a Míň je Víc"
    } else if (random === 5) {
        nadpisa.innerText = "spadneš jak dvojčata"
    }
}
