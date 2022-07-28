import requests
# import extractor
from auth import Authenticator

class urls:
    def _build_tile_url(pano_id, face, zoom):
        url = f"https://gspe72-ssl.ls.apple.com/mnn_us/0665/1337/7579/4483/3546/{pano_id}/t/{face}/{zoom}"
        return url

    def _build_pano_url(lat, lon):
        url = f"https://example.com/?pano&lat={lat}&lng={lon}"
        return url

    def _build_metadata_url(pano_id):
        url = f"https://example.com/?pano={pano_id}"
        return url

#     def _build_short_url(pano_id) -> str:
#         raise extractor.ServiceNotSupported

# class misc:
#     def get_pano_from_url(url):
#         raise extractor.ServiceNotSupported

#     def short_url(pano_id):
#         raise extractor.ServiceNotSupported

# class metadata:
#     def get_date(pano_id) -> str:
#         raise extractor.ServiceNotSupported

#     def get_metadata(pano_id) -> str:
#         raise extractor.ServiceNotSupported

#     def get_coords(pano_id) -> float:
#         raise extractor.ServiceNotSupported

#     def get_gen(pano_id):
#         raise extractor.ServiceNotSupported

# def get_pano_id(lat, lon):
#     raise extractor.ServiceNotSupported

# def get_max_zoom(pano_id):
#     raise extractor.ServiceNotSupported

# last tow funcs are bit universal-ish,
# so they could work with any service
def _build_tile_arr(pano_id, zoom=0):
    auth = Authenticator()
    arr = []
    i = 0
    while True:
        url = auth.authenticate_url(urls._build_tile_url(pano_id, i, zoom))
        resp = requests.get(url)
        if resp.status_code == 200:
            i += 1
            arr.append(url)
        else: break
    return arr

if __name__ == "__main__":
    print(_build_tile_arr(1095101453))
#    pano_id = get_pano_id(39.900139527145846, 116.3958936511099)
#    zoom = _get_max_zoom(pano_id)
#    axis = _find_max_axis(pano_id, zoom)
#    tile_arr = _build_tile_arr(pano_id, zoom, axis)
#    print(tile_arr)