# coding=utf-8

from pyquery import PyQuery as pq

uktop40 = pq('http://www.181.fm/recent/181-uktop40/')
bbcradio1 = pq('https://www.bbc.co.uk/radio1')
capitalfm = pq('http://www.capitalfm.com/london/radio/last-played-songs/')

song = uktop40('font').eq(4).text()
title, artist = song.split(' - ')
print('uktop40: ', artist, '-', title)

song = bbcradio1('div.on-air__track-now-playing__title').eq(0).text() \
       + ' - ' \
       + bbcradio1('div.on-air__track-now-playing__artist').eq(0).text()

print('bbcradio1:', song)

song = capitalfm('span.track').eq(0).text() \
       + ' - ' \
       + capitalfm('span.artist').eq(0).text()

print('capitalfm:', song)
