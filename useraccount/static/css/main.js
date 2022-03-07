

const followBtn = [...document.getElementsByClassName("follow-btn")]
followBtn.forEach(btn => btn.addEventListener('click', ()=>{
  btn.textContent = "following"
  btn.style.color = 'blue'
  btn.style.background = "white"
}))