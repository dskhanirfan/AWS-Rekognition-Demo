import boto3
from pprint import pprint
import image_helpers

client = boto3.client('rekognition')

#imgurl = 'https://www.parrots.org/images/uploads/dreamstime_C_47716185.jpg'
#imgurl = 'http://www.idothat.us/images/idothat-img/features/pool-patio-lanai/ft-pool-patio-lanai-2.jpg'
imgurl = 'https://www.glenstone.org/wp-content/uploads/prod/2018/07/AV_Landscape-Hero-Contour-2993-1276x800.jpg'
# grab the image from online
imgbytes = image_helpers.get_image_from_url(imgurl)

rekresp = client.detect_labels(Image={'Bytes': imgbytes},
                               MinConfidence=80)
pprint(rekresp['Labels'])