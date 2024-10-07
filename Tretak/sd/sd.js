const wrapper = document.querySelector(".wrapper")

for (let i = 0; i < 6000; i++) {
    let newDiv = document.createElement("div")
    newDiv.classList.add("square")
    let r = Math.floor(Math.random() * 255)
    let g = Math.floor(Math.random() * 255)
    let b = Math.floor(Math.random() * 255)
    newDiv.style.backgroundColor = `rgb(${r}, ${g}, ${b})`
    wrapper.appendChild(newDiv)
}
