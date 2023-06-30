const hashInput = document.getElementById("hash-input")
const hashButton = document.getElementById("hash-hashButton")
const hashed = document.getElementById("hash-hashed")
const hashCounter = document.getElementById("hash-counter")
// const totalCounter = document.getElementById("total-counter")

hashButton.addEventListener("click", function (event) {
    const urlData = {
        "text": hashInput.value,
    }
    const urlParams = "?" + new URLSearchParams(urlData).toString()

    fetch("/hash" + urlParams, {
        method: "GET",
    })
        .then(res => res.text())
        .then(data => {
            hashed.value = data
            hashCounter.textContent = parseInt(hashCounter.textContent) + 1
            totalCounter.textContent = parseInt(totalCounter.textContent) + 1
        })
})