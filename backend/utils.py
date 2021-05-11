import json
from urllib.parse import urlparse, ParseResult
from urllib.request import urlopen, Request
from tempfile import _TemporaryFileWrapper
from backend.config import Config


def download_catalog(url: str, fd: _TemporaryFileWrapper) -> None:
    response = urlopen(url)
    while True:
        chunk: bytes = response.read(1024)
        if not chunk:
            break
        fd.write(chunk)


def download_baserow_api(url: str) -> list:
    req: Request = Request(url)
    req.add_header('Authorization', f'Token {Config.BASEROW_API_TOKEN}')

    raw_content: bytes = urlopen(req).read()
    json_content: dict = json.loads(raw_content.decode('utf-8'))

    next: str = json_content['next']
    res_list: list = []
    if next:
        parsed_uri: ParseResult = urlparse(next)
        content: list = download_baserow_api(
            f"https://{parsed_uri.netloc}{parsed_uri.path}?{parsed_uri.query}")
        res_list: list = res_list + content

    return res_list + json_content['results']
