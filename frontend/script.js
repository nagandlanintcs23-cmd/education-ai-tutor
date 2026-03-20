async function ask() {

let q = document.getElementById("question").value

let res = await fetch("https://education-ai-tutor.onrender.com/ask")

let data = await res.json()

document.getElementById("answer").innerText = data.answer

}
