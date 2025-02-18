from fastapi import APIRouter
from starlette.requests import Request
from starlette.templating import Jinja2Templates

router = APIRouter(tags=["Frontend"])
templates = Jinja2Templates(directory="templates")


@router.get("/home_page")
def get_home_page(request: Request):
    return templates.TemplateResponse(
        name="home_page.html", context={"request": request}
    )


@router.get("/home_page/films")
def get_films_page(request: Request):
    return templates.TemplateResponse(name="films.html", context={"request": request})


@router.get("/home_page/characters")
def get_characters_page(request: Request):
    return templates.TemplateResponse(
        name="characters.html", context={"request": request}
    )


@router.get("/home_page/planets")
def get_planets_page(request: Request):
    return templates.TemplateResponse(name="planets.html", context={"request": request})


@router.get("/home_page/starships")
def get_starships_page(request: Request):
    return templates.TemplateResponse(
        name="starships.html", context={"request": request}
    )
