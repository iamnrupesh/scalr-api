# coding=utf-8
import os
import base64
import datetime
import hashlib
import hmac
import pytz
import requests
from urllib import parse

from scalr.utils import get_default_logger

log = get_default_logger(__name__)


class ScalrRestAPI(object):
    def __init__(self, url, key_id, secret_key, account_id=None, env_id=None):
        self.url = url
        self.key_id = key_id
        self.secret_key = secret_key
        self.account_id = account_id
        self.env_id = env_id
        self.session = ScalrRestAPISession(self)

    def list(self, path, **kwargs):
        data = []
        while path is not None:
            body = self.session.get(path, **kwargs).json()
            data.extend(body["data"])
            path = body["pagination"]["next"]
        return data

    def create(self, *args, **kwargs):
        return self.session.post(*args, **kwargs).json().get("data")

    def fetch(self, *args, **kwargs):
        return self.session.get(*args, **kwargs).json()["data"]

    def delete(self, *args, **kwargs):
        self.session.delete(*args, **kwargs)

    def post(self, *args, **kwargs):
        return self.session.post(*args, **kwargs).json()["data"]

    def patch(self, *args, **kwargs):
        return self.session.patch(*args, **kwargs).json()["data"]


class ScalrRestAPISession(requests.Session):
    def __init__(self, client):
        self.client = client
        super(ScalrRestAPISession, self).__init__()

    def prepare_request(self, request):
        if not request.url.startswith(self.client.url):
            request.url = "".join([self.client.url, request.url])
        request = super(ScalrRestAPISession, self).prepare_request(request)

        now = datetime.datetime.now(tz=pytz.timezone(os.environ.get("TZ", "UTC")))
        date_header = now.isoformat()

        url = parse.urlparse(request.url)

        if url.query:
            pairs = parse.parse_qsl(url.query, keep_blank_values=True, strict_parsing=True)
            pairs = [list(map(parse.quote, pair)) for pair in pairs]
            pairs.sort(key=lambda pair: pair[0])
            canon_qs = "&".join("=".join(pair) for pair in pairs)
        else:
            canon_qs = ""

        request_body = request.body if request.body is not None else ""
        request_body = bytes(request_body, "utf-8") if isinstance(request_body, str) else request_body

        sts = b"\n".join([
            bytes(request.method, 'utf-8'),
            bytes(date_header, 'utf-8'),
            bytes(url.path, 'utf-8'),
            bytes(canon_qs, 'utf-8'),
            request_body
        ])

        auth_hash = hmac.new(bytes(self.client.secret_key, 'utf-8'), sts, hashlib.sha256)
        auth_hash.hexdigest()

        sig = b" ".join([
            b"V1-HMAC-SHA256",
            base64.b64encode(auth_hash.digest())
        ])

        request.headers.update({
            "X-Scalr-Key-Id": self.client.key_id,
            "X-Scalr-Signature": sig,
            "X-Scalr-Date": date_header
        })

        return request

    def request(self, *args, **kwargs):
        res = super(ScalrRestAPISession, self).request(*args, **kwargs)
        log.debug("%s - %s", " ".join(args), res.status_code)
        if not res.ok:
            try:
                errors = res.json().get("errors", None)
                if errors is not None:
                    for error in errors:
                        log.warning("API Error (%s): %s", error["code"], error["message"])
            except ValueError:
                log.error("Received non-JSON response from API!")
        res.raise_for_status()
        log.debug("Received response: %s", res.text)
        return res
