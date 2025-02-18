from fastapi import APIRouter
import requests

from utils import Utils

router = APIRouter(tags=["info"])


@router.get("/home_page/starships/starship_info/{num}")
def get_starships_info(num: int):
    data = requests.get(f"https://swapi.dev/api/starships/{num}").json()
    return f"""
    <div>
        <p>Name: {data["name"]}</p>
        <p>Model: {data["model"]}</p>
        <p>Manufacturer: {data["manufacturer"]}</p>
        <p>Cost in credits: {data["cost_in_credits"]}</p>
        <p>Length: {data["length"]}</p>
        <p>Max atmosphering speed: {data["max_atmosphering_speed"]}</p>
        <p>Crew: {data["crew"]}</p>
        <p>Passengers: {data["passengers"]}</p>
        <p>Cargo capacity: {data["cargo_capacity"]}</p>
        <p>Consumables: {data["consumables"]}</p>
        <p>Hyperdrive rating: {data["hyperdrive_rating"]}</p>
        <p>MGLT: {data["MGLT"]}</p>
        <p>Starship class: {data["starship_class"]}</p>
        <button class="close_btn">&times;</button>
    </div>
    """


@router.get("/home_page/planets/planet_info/{num}")
def get_palnet_info(num: int):
    data = requests.get(f"https://swapi.dev/api/planets/{num}").json()
    return f"""
    <div>
        <p>Name: {data["name"]}</p>
        <p>Rotation period: {data["rotation_period"]}</p>
        <p>Orbital period: {data["orbital_period"]}</p>
        <p>Diameter: {data["diameter"]}</p>
        <p>Climate: {data["climate"]}</p>
        <p>Gravity: {data["gravity"]}</p>
        <p>Terrain: {data["terrain"]}</p>
        <p>Population: {data["population"]}</p>
        <button class="close_btn">&times;</button>
    </div>
    """


@router.get("/home_page/characters/character_info/{num}")
def get_character_info(num: int):
    data = requests.get(f"https://swapi.dev/api/people/{num}").json()
    planet = requests.get(data["homeworld"]).json()["name"]
    starships = []
    vehicles = []
    for i in data["starships"]:
        starship = requests.get(i).json()
        starships.append(starship["model"])
    for i in data["vehicles"]:
        vehicle = requests.get(i).json()
        vehicles.append(vehicle["model"])
    return f"""
    <div>
        <p>Name: {data["name"]}</p>
        <p>Height: {data["height"]}</p>
        <p>Mass: {data["mass"]}</p>
        <p>Gender: {data["gender"]}</p>
        <p>Birth year: {data["birth_year"]}</p>
        <p>Homeworld: {planet}</p>
        {Utils.chek_starships(starships)}
        {Utils.chek_vehicles(vehicles)}
        <button class="close_btn">&times;</button>
    </div>
    """


@router.get("/home_page/films/episode_info/{num}")
def get_ep_one_info(num: int):
    data = requests.get(f"https://swapi.dev/api/films/{num}/").json()
    return f"""
    <div>
        <p>Title: {data["title"]}</p>
        <p>Director: {data["director"]}</p>
        <p>Producer: {data["producer"]}</p>
        <p>Release date: {data["release_date"]}</p>
        <p>Opening crawl: {data["opening_crawl"]}</p>
        <button class="close_btn">&times;</button>  
    </div>
    """
