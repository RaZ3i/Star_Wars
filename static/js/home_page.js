const filmsBtn = document.querySelector(".films_all");
const heroesBtn = document.querySelector(".heroes_all");
const planetsBtn = document.querySelector(".planets");
const starshipsBtn = document.querySelector(".starships");



filmsBtn.addEventListener("click", function() {
    window.location.href = "http://127.0.0.1:8001/home_page/films"            
})


heroesBtn.addEventListener("click", function() {
    window.location.href = "http://127.0.0.1:8001/home_page/characters"            
})


planetsBtn.addEventListener("click", function() {
    window.location.href = "http://127.0.0.1:8001/home_page/planets"            
})


starshipsBtn.addEventListener("click", function() {
    window.location.href = "http://127.0.0.1:8001/home_page/starships"            
})

