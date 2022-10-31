document.querySelector('.question').classList.add('active');

const questions = Array.from(document.querySelectorAll('.question'));
const next_btns = document.querySelectorAll('.next-btn');
const form = document.querySelector('form');

next_btns.forEach((button)=>{
    button.addEventListener('click', ()=>{
        changeQuestion();
    });
});

/*form.addEventListener("submit", (e) => {
  e.preventDefault();
  const inputs = [];
  form.querySelectorAll("input").forEach((input) => {
    const { name, value } = input;
    inputs.push({ name, value });
  });
  console.log(inputs);
  form.reset();
});*/

function changeQuestion(){
    let index = 0;
    const active = document.querySelector('.active');
    index = questions.indexOf(active);
    questions[index].classList.remove('active');
    index++;
    questions[index].classList.add('active');
}