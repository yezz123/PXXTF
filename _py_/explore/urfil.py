#!/usr/bin/env python


class sansor():
    def __init__(self):
        pass

    def pransor(self, url):
        from urllib.parse import unquote
        import socket
        import re
        http_match = re.search(r"^.*://", url)
        www_match = re.search(r"(w{3}|w3)\.", url)
        end_match = re.search(r"([\w\d\-]$)", url)
        ip_match = re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", url)
        if ip_match:
            try:
                result = socket.gethostbyaddr(url)
            except socket.herror as e:
                pass
            else:
                url = result[0]

        if www_match:
            url = url.replace(www_match.group(), "")
        if http_match:
            pass
        else:
            url = "http://" + url
        if end_match:
            url = url + "/"
        else:
            pass
        return unquote(url)

    def cransor(self, url):
        from urllib.request import urlopen
        try:
            ch = urlopen(url)
            status = True
        except BaseException:
            status = False
        return status
