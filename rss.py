#!/usr/bin/env python3
'''Python Script for generating a rss.xml for the A9LH Guide Plailect wrote. Requires bencodepy from pypy.'''

import os
import hashlib

import bencodepy

dir = os.getcwd()
rss = os.path.join(dir, "rss.xml")
gio = "https://plailect.github.io/Guide"

with open(rss, "w") as xml:
    xml.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
    xml.write("<rss version=\"2.0\">\n")
    xml.write("\t<channel>\n")
    xml.write("\t\t<title>Plailect Guide Feed</title>\n")
    xml.write("\t\t<link>https://github.com/Plailect/Guide/wiki</link>\n")

    for filename in os.listdir(dir):
        if filename.endswith(".torrent"):
            path = os.path.join(dir, filename)
            sfile = filename.rsplit(".", 1)[0]
            sha1 = hashlib.sha1()

            with open(path, "rb") as a:
                file = a.read()
                length = len(file)
                torstruct = bencodepy.decode(file)
                if b'info' in torstruct:
                    infohash = hashlib.sha1(bencodepy.encode(torstruct[b'info'])).hexdigest()
                else:
                    infohash = "{0}/{1}.torrent".format(gio, sfile)
                sha1.update(file)

            uri = "{0}/{1}.torrent".format(gio, sfile)
            xml.write("\t\t<item>\n")
            xml.write("\t\t\t<title>{0}</description>\n".format(sfile))
            xml.write("\t\t\t<description>{0}</description>\n".format(sfile))
            xml.write("\t\t\t<guid>{0}</guid>\n".format(infohash))
            xml.write("\t\t\t<link>{0}</link>\n".format(uri))
            xml.write("\t\t\t<enclosure url=\"{0}\" length=\"{1}\" type=\"application/x-bittorent\" />\n".format(uri, length))
            xml.write("\t\t\t<media:content url=\"{0}\" fileSize=\"{1}\"/>\n".format(uri, length))
            xml.write("\t\t\t<media:hash algo=\"sha1\"><{0}/media:hash>\n".format(sha1.hexdigest()))
            xml.write("\t\t</item>\n")
    xml.write("\t</channel>\n")
    xml.write("</rss>")
