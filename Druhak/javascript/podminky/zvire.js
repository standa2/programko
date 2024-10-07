let tlacitko = document.querySelector("#tlacitko")
let nadpis = document.getElementById("nadpis")
let body = document.querySelector ("body")
let input = document.querySelector("#input")
let nadpisa = document.getElementById("nadpisa")
tlacitko.addEventListener("click", zmenNadpis)

function zmenNadpis () {
    let textInputu = input.value
    if (textInputu === "želva") { 
        nadpis.innerText = "donny 🐸"
        body.style.backgroundColor = "green"
    }else if(textInputu === "žralok") { 
        nadpis.innerText = "megladong 🦈"
        body.style.backgroundColor = "blue"
    }else if(textInputu === "žirafa") { 
        nadpis.innerText = "klud 🦒"
        body.style.backgroundColor = "yellow"
    }else {
        nadpis.innerText = "neznaaaaam ❌"
        body.style.backgroundColor = "black"
        nadpis.style.color = "white"
        nadpisa.style.color = "white"
    }
}





