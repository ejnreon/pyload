# -*- coding: utf-8 -*-

import re

from urlparse import urljoin

from pyload.plugin.internal.SimpleCrypter import SimpleCrypter


class Go4UpCom(SimpleCrypter):
    __name    = "Go4UpCom"
    __type    = "crypter"
    __version = "0.11"

    __pattern = r'http://go4up\.com/(dl/\w{12}|rd/\w{12}/\d+)'

    __description = """Go4Up.com decrypter plugin"""
    __license     = "GPLv3"
    __authors     = [("rlindner81", "rlindner81@gmail.com"),
                       ("Walter Purcaro", "vuolter@gmail.com")]


    LINK_PATTERN = r'(http://go4up\.com/rd/.+?)<'

    NAME_PATTERN = r'<title>Download (.+?)<'

    OFFLINE_PATTERN = r'>\s*(404 Page Not Found|File not Found|Mirror does not exist)'


    def getLinks(self
        links = []

        m = re.search(r'(/download/gethosts/.+?)"')
        if m:
            self.html = self.load(urljoin("http://go4up.com/", m.group(1)))
            pages = [self.load(url) for url in re.findall(self.LINK_PATTERN, self.html)]
        else:
            pages = [self.html]

        for html in pages:
            try:
                links.append(re.search(r'<b><a href="(.+?)"', html).group(1))
            except Exception:
                continue

        return links
