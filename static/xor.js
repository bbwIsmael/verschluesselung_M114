const xorInput = document.getElementById("xor-input")
const xorInputKey = document.getElementById("xor-inputKey")
const xorEncryptButton = document.getElementById("xor-encryptButton")
const xorEncoded = document.getElementById("xor-encoded")
const xorDecryptKey = document.getElementById("xor-decryptKey")
const xorDecryptButton = document.getElementById("xor-decryptButton")
const xorDecoded = document.getElementById("xor-decoded")
const xorCounter = document.getElementById("xor-counter")
// const totalCounter = document.getElementById("total-counter")

// Encrypt
xorEncryptButton.addEventListener("click", function (event) {
    const urlData = {
        "text": xorInput.value,
        "key": xorInputKey.value
    }
    const urlParams = "?" + new URLSearchParams(urlData).toString()

    fetch("/xor" + urlParams, {
        method: "GET",
    })
        .then(res => res.text())
        .then(data => {
            xorEncoded.value = data
            xorCounter.textContent = parseInt(xorCounter.textContent) + 1
            totalCounter.textContent = parseInt(totalCounter.textContent) + 1
        })
})

// Decrypt
xorDecryptButton.addEventListener("click", function (event) {
    const urlData = {
        "text": xorEncoded.value,
        "key": xorDecryptKey.value
    }
    const urlParams = "?" + new URLSearchParams(urlData).toString()

    fetch("/xor" + urlParams, {
        method: "GET",
    })
        .then(res => res.text())
        .then(data => {
            xorDecoded.value = data
            xorCounter.textContent = parseInt(xorCounter.textContent) + 1
            totalCounter.textContent = parseInt(totalCounter.textContent) + 1
        })
})

// Sync all shift value inputs
xorInputKey.addEventListener("input", function (event) {
    xorDecryptKey.value = event.target.value
})

xorDecryptKey.addEventListener("input", function (event) {
    xorInputKey.value = event.target.value
})