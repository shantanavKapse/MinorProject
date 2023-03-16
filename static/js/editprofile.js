function addNewSkills() {
    const skill = document.querySelector('.skill-box');
    const ul = document.querySelector('.scrollbar');
    const skillLevel =  document.querySelector('.level');
    const li = document.createElement("li");

    let options = {
        method: 'POST',
        headers: {
            'Content-Type': 
                'application/json'
        },
        body: JSON.stringify({"skill_name": skill.value, "skill_level": skillLevel.value})
    }
    let fetchRes = fetch("/add_skill", options);
    fetchRes.then(res => res.json()).then(d => {
            if (d.status == 200){
                $('#skillbox').load(' #skillbox > *')
                //li.appendChild(document.createTextNode(`${skill.value} (${skillLevel.value})`));
                //ul.appendChild(li);
                //skill.value = '';
                //skillLevel.value = 'Beginner';

                //ul.scrollTop = ul.scrollHeight;


//                li.appendChild(document.createTextNode(`${skill.value} (${skillLevel.value})`));
//                let button = li.appendChild(document.createElement("button"));
//                button.setAttribute("type", "button");
//                button.setAttribute("data-skillid", d.skill.skill_id);
//                button.setAttribute("data-userid", d.skill.username);
//                li.lastElementChild.classList.add("delete-skill", "bi", "bi-trash");
//                //div.lastElementChild.setAttribute("skill", d.skill_id);
//                //li.appendChild(div);
//                ul.appendChild(li);
//                skill.value = '';
//                skillLevel.value = 'Beginner';
//                ul.scrollTop = ul.scrollHeight;
            }
        
        })
}

function showProfileImage() {
    const img = document.querySelector(".profile-img");
    const imgDiv = document.querySelector("#input-newPhoto");
    const reader = new FileReader();
    reader.readAsDataURL(imgDiv.files[0]);

    reader.addEventListener('load', () => {
        localStorage.setItem("recent-img", reader.result);
        const recentImageUrl = localStorage.getItem("recent-img");
        img.src = recentImageUrl;
    })
}


const skillsList = document.querySelector('.ul-newSkills');
skillsList.addEventListener('click', (event) => {
  if (event.target.classList.contains('delete-skill')) {
    const skillItem = event.target.parentNode;
    const skillid = event.target.dataset.skillid;
    const userid = event.target.dataset.userid;
    console.log(skillid, userid);

    let options = {
        method: 'POST',
        headers: {
            'Content-Type': 
                'application/json'
        },
        body: JSON.stringify({"skill_id": skillid, "username": userid})
    }
    let fetchRes = fetch("/remove_skill", options);
    fetchRes.then(res => res.json()).then(d => {
            if (d.status == 200){
                skillItem.parentNode.removeChild(skillItem);
            }
        })
  }
});
