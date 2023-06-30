const totalCounter = document.getElementById("total-counter")

const functions = ["caesar", "hash", "xor"]
const hiddenClass = "wrapper-hidden"

const selectElement = document.getElementById("encryptionMethod")

selectElement.addEventListener("change", function (event) {
    const value = event.target.value

    for(let i = 0; i < functions.length; i++) {
        const element = document.getElementById(functions[i] + "-wrapper")
        if(functions[i] === value) {
            element.classList.remove(hiddenClass)
        } else {
            element.classList.add(hiddenClass)
        }
    }
})