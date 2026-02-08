import qrcode as qr
img=qr.make("https://www.youtube.com/watch?v=cY3REsLgfz8&list=RDcY3REsLgfz8&start_radio=1")
img.save("song.png")