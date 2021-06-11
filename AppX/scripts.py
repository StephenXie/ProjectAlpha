from quotes import Quotes
import random
my_quote = Quotes()
def get_quotes():
    return my_quote.random()[1]

def get_video():
    arr = ["..\static\\admin\img\Pexels%20Videos%201409899.mp4", "https://player.vimeo.com/external/269971860.hd.mp4?s=eae965838585cc8342bb5d5253d06a52b2415570&profile_id=175&oauth2_token_id=57447761", "https://player.vimeo.com/video/473655823?title=0&portrait=0&byline=0&autoplay=1", "https://player.vimeo.com/video/299108946?title=0&portrait=0&byline=0&autoplay=1", "https://player.vimeo.com/video/269983448?title=0&portrait=0&byline=0&autoplay=1"]
    return arr[0]
    