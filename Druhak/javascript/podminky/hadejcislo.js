let tlacitko = document.querySelector("#tlacitko")
let nadpis = document.getElementById("nadpis")

let input = document.querySelector("#input")

tlacitko.addEventListener("click", zmenNadpis)

Math.floor(Math.random() * 101)

function zmenNadpis() {
    let textInputu = input.value
        textInputu = parseInt(textInputu)
    if(textInputu === Math.floor(Math.random() * 101)){
        nadpis.innerText = "hezkyy"
     }else if(textInputu < Math.floor(Math.random() * 101)){
        nadpis.innerText = "Málo"
     }else{
        nadpis.innerText = "Moc"
     }
}