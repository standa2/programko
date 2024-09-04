    let tlacitko = document.querySelector("#tlacitko")
    let nadpis = document.getElementById("nadpis")
    
    let input = document.querySelector("#input")

    tlacitko.addEventListener("click", zmenNadpis)

    function zmenNadpis() {
        let textInputu = input.value
        nadpis.style.color = "red"
        nadpis.style.fontSize = "50px"
        if(textInputu === "otázka"){
            nadpis.innerText = "42"
         }else{
            innerText === textInputu
         }
    }