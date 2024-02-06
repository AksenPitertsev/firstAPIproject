import io
import pygame
import requests


class APIWork:
    def get_center(place):
        geocoder_request = "https://geocode-maps.yandex.ru/1.x"

        data = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "format": "json",
            "geocode": place,
        }

        res = requests.get(geocoder_request, data).json()
        center = (
            res.get("response")
            .get("GeoObjectCollection")
            .get("featureMember")[0]
            .get("GeoObject")
            .get("Point")
            .get("pos")
        )

        return place

    def get_map(center, zoom, x, y):
        geocoder_request = "https://geocode-maps.yandex.ru/1.x"

        data = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "format": "json",
            "geocode": "Череповец",
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
            "z": zoom,
            "size": ",".join(map(str, size)),
            "ll": f"{center[0] + x}{center[1] + y}",
        }

        res = requests.get(maps_request, data).content
        res = io.BytesIO(res)

        return res


if __name__ == "__main__":
    pygame.init()
    img = pygame.image.load(APIWork.get_map(12))
    screen = pygame.display.set_mode((650, 450))
    screen.blit(img, (0, 0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
