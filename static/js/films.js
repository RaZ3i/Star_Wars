const films = document.querySelectorAll('.films_card')
const main_content = document.querySelector('.main_content')
const backBtn = document.querySelector('.back_btn')

backBtn.addEventListener("click", function() {
    window.location.href = "http://127.0.0.1:8001/home_page"            
})

for (const element of films) {

    element.addEventListener("mouseover", e=>{
        e.target.style.scale = 1.1
    })
    element.addEventListener("mouseout", e=>{
        e.target.style.scale = 1.0
    })

    element.addEventListener('click', async e=>{
        const invisiblock = document.createElement("div");
        invisiblock.classList.add("invisible");
        document.body.appendChild(invisiblock);
        main_content.classList.remove("body_no_opacity");
        main_content.classList.add("body_opacity");
    try {
        let response = await fetch(`http://127.0.0.1:8001/home_page/films/episode_info/${e.target.id}`, {
            method: "GET",
            }
        );
        if (response) {
            const json = await response.json();
            const info = document.createElement("div");
            info.innerHTML = json;
            info.classList.add("film_info");
            e.target.classList.add("chosen_film");
            document.body.appendChild(info);
            
        }


            }
        catch (error) {
            document.body.removeChild(document.querySelector(".invisible"));
            main_content.classList.remove("body_opacity");
            main_content.classList.add("body_no_opacity");
            }   
        } 
 
    )
    
}

document.addEventListener("click", e=>{
    if (e.target.classList.contains("close_btn")) {
      document.body.removeChild(document.querySelector(".film_info"));
      document.body.removeChild(document.querySelector(".invisible"));
      main_content.classList.remove("body_opacity");
      main_content.classList.add("body_no_opacity");
      for (const element of films) {
        if (element.classList.contains("chosen_film")){
            element.classList.remove("chosen_film");
            
                }
            }
        }
    }
)