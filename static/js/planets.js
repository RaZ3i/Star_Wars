const planet = document.querySelectorAll('.planet_card');
const main_content = document.querySelector('.main_content');
const backBtn = document.querySelector('.back_btn');

backBtn.addEventListener("click", function() {
    window.location.href = "http://127.0.0.1:8001/home_page"            
})


for (const element of planet) {

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
        let response = await fetch(`http://127.0.0.1:8001/home_page/planets/planet_info/${e.target.id}`, {
            method: "GET",
            }
        );
        if (response) {
            const json = await response.json();
            const info = document.createElement("div");
            info.innerHTML = json;
            info.classList.add("info");
            e.target.classList.add("chosen_target");
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
      document.body.removeChild(document.querySelector(".info"));
      document.body.removeChild(document.querySelector(".invisible"));
      main_content.classList.remove("body_opacity");
      main_content.classList.add("body_no_opacity");
      for (const element of planet) {
        if (element.classList.contains("chosen_target")){
            element.classList.remove("chosen_target");
            
                }
            }
        }
    }
)