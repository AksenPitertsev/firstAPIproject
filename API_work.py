import io
import pygame
import requests


class APIWork:
    # def get_map(place, zoom):
    # def get_map(place):
    def get_map():

        geocoder_request = "https://geocode-maps.yandex.ru/1.x"

        data = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "format": "json",
            "geocode": "Череповец",
            # "geocode": place,
        }

        # try:
        res = requests.get(geocoder_request, data).json()
        center = (
            res.get("response")
            .get("GeoObjectCollection")
            .get("featureMember")[0]
            .get("GeoObject")
            .get("Point")
            .get("pos")
        )

        maps_request = "https://static-maps.yandex.ru/1.x"

        size = 650, 450
        data = {
            "l": "map",
            "z": 10,
            #"z": zoom,
            "size": ",".join(map(str, size)),
            "ll": center.replace(" ", ","),
        }

        res = requests.get(maps_request, data).content
        res = io.BytesIO(res)

        return res


if __name__ == "__main__":
    pygame.init()
    img = pygame.image.load(APIWork.get_map())
    screen = pygame.display.set_mode((700, 400))
    screen.blit(img, (0, 0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
