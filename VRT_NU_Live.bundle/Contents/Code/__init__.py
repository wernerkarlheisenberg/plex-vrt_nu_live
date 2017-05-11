import requests
import json
channels = SharedCodeService.channels

####################################################################################################
PREFIX = "/video/vrt_nu_live"
NAME = "VRT NU"
ICON = "vrt_nu.png"
####################################################################################################

def Start():
    Dict.Reset()
    ObjectContainer.title1 = NAME

@handler(PREFIX, NAME, thumb=ICON, art=ICON)
def MainMenu():

    oc = ObjectContainer()
    for channel in channels.channelList:
        do_channel = VideoClipObject(
            url= StreamURL(channel.url_name.replace('_','')),
            title = channel.name,
            thumb = channel.logo_name
        )
        oc.add(do_channel)

    return oc

def StreamURL(channel):

    live_video_resp = requests.get('http://services.vrt.be/videoplayer/r/live.json')
    live_video_resp_json = json.loads(live_video_resp.content.replace('parseLiveJson(','').replace(')',''))
    return  live_video_resp_json[channel]['hls']
