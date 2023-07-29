const btn = document.querySelector('button')
const cont = document.querySelector('#cont')
const main = document.querySelector('#main')


btn.addEventListener('click',()=>{
  cont.classList.toggle('active')
  // ul.classList.toggle('active')
  main.classList.toggle('half')

})