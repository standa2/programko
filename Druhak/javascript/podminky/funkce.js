function ukazka(pozdrav) {
    console.log(pozdrav)
    console.log("Čégo")
}

ukazka("dobrý den")
ukazka("ahoj")

function scitani(cisloA, cisloB) {
    let vysledek = cisloA + cisloB
    console.log(vysledek)
}

scitani(3, 8)

function prevod(km) {
    let mile = km * 0.621371192
    return mile
}

prevod(10)
console.log(prevod(50))
let vysledekPrevodu = prevod(30)
console.log(vysledekPrevodu)

let textvHTML = document.querySelector("#text")
textvHTML.innerText = prevod(50)
