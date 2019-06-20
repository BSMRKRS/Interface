/usr/src/mjpg-streamer/mjpg-streamer-experimental/mjpg_streamer -i "input_uvc.so -r 640x480 -d /dev/video0 -n" -o "output_http.so -w /usr/src/mjpg-streamer/mjpg-streamer-experimental/www -p 8080"

# start with /home/student/startcam.sh
# view at http://192.168.21.xxx:8080/stream.html
# xxx being the sd card number
# this is meant for the usb cams
