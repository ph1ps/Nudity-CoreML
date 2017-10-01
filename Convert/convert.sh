wget https://github.com/yahoo/open_nsfw/raw/master/nsfw_model/resnet_50_1by2_nsfw.caffemodel
wget https://github.com/yahoo/open_nsfw/raw/master/nsfw_model/deploy.prototxt
virtualenv -p /usr/bin/python2.7 env
source env/bin/activate
pip install coremltools
python nudity.py
deactivate
