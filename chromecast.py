import time
import pychromecast

services, browser = pychromecast.discovery.discover_chromecasts()
pychromecast.discovery.stop_discovery(browser)
print(f"browsers = {services}")
chromecast_devs, browser = pychromecast.get_listed_chromecasts(friendly_names=["Family room TV"])
print([cc.cast_info.friendly_name for cc in chromecast_devs])


cast = chromecast_devs[0]
# Start worker thread and wait for cast device to be ready
cast.wait()
print(cast.cast_info)
print(cast.status)


mc = cast.media_controller
mc.play_media('http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', 'video/mp4')
mc.block_until_active()
print(mc.status)
mc.pause()
time.sleep(5)
mc.play()

# Shut down discovery
pychromecast.discovery.stop_discovery(browser)

