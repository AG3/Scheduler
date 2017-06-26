import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from . import mputil as util


class MP_Viewer:
    session = requests.Session()
    username = ""
    password = ""
    url = ""
    cookies = requests.cookies.RequestsCookieJar()
    rawText = ""

    def __init__(self, username, password):
        """Provide identify information."""
        self.username = username
        self.password = password

    def Login(self):
        """Login to Myportal's home page."""
        r = self.session.get(util.URL_LOGIN)
        ts_index = r.text.find(util.MARK_SERVERTIME)
        local_timestamp = int(round(time.time() * 1000))
        server_timestamp = int(r.text[ts_index + 49:ts_index + 62])
        clientServerDelta = local_timestamp - server_timestamp
        uuid = int(round(time.time() * 1000)) - clientServerDelta
        payload = {"proxysso": "true",
                   "ssouser": self.username,
                   "ssocredential": self.password}
        r = self.session.get(util.URL_LOGIN, params=payload)
        IdpResponse = r.text
        IdpResponse = IdpResponse.replace("\x00","").replace("\n"," ").replace("\t"," ")
        IdpResponse = IdpResponse.strip().split(" ")

        self.session.cookies.set(IdpResponse[5], IdpResponse[6], domain=IdpResponse[0], path=IdpResponse[2])
        self.session.cookies.set(IdpResponse[12], IdpResponse[13], domain=IdpResponse[7], path=IdpResponse[9])
        form = {"user": self.username, "pass": self.password, "uuid": uuid}
        r = self.session.post(util.URL_POST_LOGIN, data=form)
        r = self.session.get(util.URL_LOGINOK)
        r = self.session.get(util.URL_LOGINNEXT)
        self.url = r.url
        self.rawText = r.text

    def Click(self, linkName):
        """Click a link in current page."""
        soup = BeautifulSoup(self.rawText, "html.parser")
        target_obj = soup.find("a", string=linkName)

        target_link = util.getLegalUrl(target_obj.attrs["href"])
        r = self.session.get(target_link, headers={'referer': self.url})
        self.url = r.url
        self.rawText = r.text

        soup = BeautifulSoup(r.text, "html.parser")
        content_frame = soup.find("frame", attrs={"name": "content"})

        if content_frame is not None:
            print("Page contains frame.")
            content_link = util.getLegalUrl(content_frame.attrs["src"])

            r = self.session.get(content_link, headers={'referer': self.url})
            self.url = r.url
            self.rawText = r.text
            # print("GET:", content_link)

    def goto(self, url):
        """Send a GET request to given url"""
        url = util.getLegalUrl(url)
        r = self.session.get(url)
        self.url = r.url
        self.rawText = r.text

    def PostForm(self, action, data):
        """
        Post given form, due to there're lots of forms in a same page,
        the action parameter should be given.
        """
        parsed_uri = urlparse(self.url)
        form_domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
        target_url = form_domain + action
        r = self.session.post(target_url, data, headers={'referer': self.url})
        self.url = r.url
        self.rawText = r.text

    def Logout(self):
        self.session.get(util.URL_LOGOUT)
