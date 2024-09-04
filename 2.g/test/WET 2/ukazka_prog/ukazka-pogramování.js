let gotoKNP = document.querySelector("#goto-knp");
let gotoHadej = document.querySelector("#goto-hadej");
let contKNP = document.querySelector("#knp");
let contHadej = document.querySelector("#hadej");

let textHadej = document.querySelector("#text-hadej");
let tlacitkoHadej = document.querySelector("#tlacitko-hadej");
let vstupHadej = document.querySelector("#input-hadej");
let textKNP = document.querySelector("#text-knp");
let tlacitkoKamen = document.querySelector("#tlacitko-kamen");
let tlacitkoNuzky = document.querySelector("#tlacitko-nuzky");
let tlacitkoPapir = document.querySelector("#tlacitko-papir");

console.log(localStorage.getItem("page"));
checkPage();

gotoKNP.addEventListener("click", function() {
    localStorage.setItem("page", 2)
    checkPage();
});

gotoHadej.addEventListener("click", function() {
    localStorage.setItem("page", 1)
    checkPage();
});


function checkPage() {
    if (localStorage.getItem("page") === "1") {
        contKNP.style.display = "none";
        contHadej.style.display = "flex";
    } else {
        contHadej.style.display = "none";
        contKNP.style.display = "flex";
    }
}


tlacitkoHadej.addEventListener("click", hadejCislo);
vstupHadej.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        tlacitkoHadej.click();
    }
});
tlacitkoKamen.addEventListener("click", zvolenKamen);
tlacitkoNuzky.addEventListener("click", zvolenyNuzky);
tlacitkoPapir.addEventListener("click", zvolenPapir);



// ---------------------------------------------------------------------------
// ---------------------------------------------------------------------------
// ---------------------------------------------------------------------------







// ############
// Hádej číslo 
// ############



// zvolím tajné, hádané číslo                                       pro náhodné číslo od 0 do 10: Math.floor(Math.random() * 11);
//                ↓
let tajneCislo = Math.floor(Math.random() * 101);
//                ↑


function hadejCislo() {
    let vysledek = "";
    let odpoved = parseInt(vstupHadej.value);
    console.log(tajneCislo);

    // ---------------------------------------
    // Zde upravujeme logiku hry Hádej číslo ↓

    if (odpoved === tajneCislo) {
        vysledek = "Dobře Boris.";
    } else if (odpoved < tajneCislo) {
        vysledek = "Víc Boris";
    } else if (odpoved > tajneCislo) {
        vysledek = "Míň Boris";
    } else {
        vysledek = "Číslo Boris";
    }
    

    // Zde upravujeme logiku hry Hádej číslo ↑
    // ---------------------------------------

    textHadej.innerHTML = vysledek;
    vstupHadej.value = "";
}






// ####################
// Kámen, nůžky, papír 
// ####################

function pocitaceVoliKNP() {
    let volbaPocitace = Math.floor(Math.random() * 3) + 1;
    if (volbaPocitace === 1) {
        volbaPocitace = "kámen";
    } else if (volbaPocitace === 2) {
        volbaPocitace = "nůžky";
    } else {
        volbaPocitace = "papír";
    }
    return volbaPocitace;
}



function zvolenKamen() {
    let vysledek = "";
    let volbaPocitace = pocitaceVoliKNP(); // počítač zvolí náhodně buď kámen, nůžky nebo papír

    
    // ----------------------------------------------
    // Zde upravujeme logiku, pokud je zvolen kámen ↓

    if (volbaPocitace === "kámen") {
        vysledek = "Remíza";
    } else if (volbaPocitace === "nůžky") {
        vysledek = "Výhrál/a jsi";
    } else if (volbaPocitace === "papír") {
        vysledek = "Prohrál/a jsi";
    }






    
    // Zde upravujeme logiku, pokud je zvolen kámen ↑
    // ----------------------------------------------


    textKNP.innerHTML = "Zvolil jsi: kámen" + "<br>" + "<br>" +"Počítač zvolil: "  + volbaPocitace  + "<br>" + "<br>" + "<strong>" + vysledek.toUpperCase() + "</strong>" + "<br>" + "<br>" + "Chceš hrát znovu?";
}   



function zvolenyNuzky() {
    let vysledek = "";
    let volbaPocitace = pocitaceVoliKNP(); // počítač zvolí náhodně buď kámen, nůžky nebo papír

    
    // -------------------------------------------------
    // Zde upravujeme logiku, pokud jsou zvoleny nůžky ↓


    if (volbaPocitace === "kámen") {
        vysledek = "Prohrál/a jsi";
    } else if (volbaPocitace === "nůžky") {
        vysledek = "Remíza";
    } else if (volbaPocitace === "papír") {
        vysledek = "Vyhrál/a jsi";
    }

    






    // Zde upravujeme logiku, pokud jsou zvoleny nůžky ↑
    // -------------------------------------------------


    textKNP.innerHTML = "Zvolil jsi: nůžky" + "<br>" + "<br>" +"Počítač zvolil: "  + volbaPocitace  + "<br>" + "<br>" + "<strong>" + vysledek.toUpperCase() + "</strong>" + "<br>" + "<br>" + "Chceš hrát znovu?";
}   


function zvolenPapir() {
    let vysledek = "";
    let volbaPocitace = pocitaceVoliKNP(); // počítač zvolí náhodně buď kámen, nůžky nebo papír

    
    // ----------------------------------------------
    // Zde upravujeme logiku, pokud je zvolen papír ↓

    if (volbaPocitace === "kámen") {
        vysledek = "Vyhrál/a jsi";
    } else if (volbaPocitace === "nůžky") {
        vysledek = "Prohrál/a jsi";
    } else if (volbaPocitace === "papír") {
        vysledek = "Remíza";
    }






    
    // Zde upravujeme logiku, pokud je zvolen papír ↑
    // ----------------------------------------------


    textKNP.innerHTML = "Zvolil jsi: papír" + "<br>" + "<br>" +"Počítač zvolil: "  + volbaPocitace  + "<br>" + "<br>" + "<strong>" + vysledek.toUpperCase() + "</strong>" + "<br>" + "<br>" + "Chceš hrát znovu?";
} 


















