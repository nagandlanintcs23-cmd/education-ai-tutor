async function ask() {

let q = document.getElementById("question").value

let res = await fetch(`http://127.0.0.1:8000/ask?question=${q}`)

let data = await res.json()

document.getElementById("answer").innerText = data.answer

}