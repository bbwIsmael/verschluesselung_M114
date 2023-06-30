const input = document.getElementById("caesar-input")
const inputShift = document.getElementById("caesar-inputShift")
const encryptButton = document.getElementById("caesar-encryptButton")
const encoded = document.getElementById("caesar-encoded")
const decryptShift = document.getElementById("caesar-decryptShift")
const decryptButton = document.getElementById("caesar-decryptButton")
const decoded = document.getElementById("caesar-decoded")
const caesarCounter = document.getElementById("caesar-counter")
// const totalCounter = document.getElementById("total-counter")

// Encrypt
encryptButton.addEventListener("click", function (event) {
    const urlData = {
        "text": input.value,
        "shift": inputShift.value
    }
    const urlParams = "?" + new URLSearchParams(urlData).toString()

    fetch("/caesar/encrypt" + urlParams, {
        method: "GET",
    })
        .then(res => res.text())
        .then(data => {
            encoded.value = data
            caesarCounter.textContent = parseInt(caesarCounter.textContent) + 1
            totalCounter.textContent = parseInt(totalCounter.textContent) + 1
        })
})

// Decrypt
decryptButton.addEventListener("click", function (event) {
    const urlData = {
        "text": encoded.value,
        "shift": decryptShift.value
    }
    const urlParams = "?" + new URLSearchParams(urlData).toString()

    fetch("/caesar/decrypt" + urlParams, {
        method: "GET",
    })
        .then(res => res.text())
        .then(data => {
            decoded.value = data
            caesarCounter.textContent = parseInt(caesarCounter.textContent) + 1
            totalCounter.textContent = parseInt(totalCounter.textContent) + 1
        })
})

// Sync all shift value inputs
inputShift.addEventListener("change", function (event) {
    decryptShift.value = event.target.value
})

decryptShift.addEventListener("change", function (event) {
    inputShift.value = event.target.value
})