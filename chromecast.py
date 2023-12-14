import time
import pychromecast

services, browser = pychromecast.discovery.discover_chromecasts()
pychromecast.discovery.stop_discovery(browser)
print(f"browsers = {services}")
chromecast_devs, browser = pychromecast.get_listed_chromecasts(friendly_names=["Family room TV"])
print([cc.cast_info.friendly_name for cc in chromecast_devs])


cast = chromecasts[0]
>> # Start worker thread and wait for cast device to be ready
>> cast.wait()
>> print(cast.cast_info)
CastInfo(services={ServiceInfo(type='mdns', data='Chromecast-Audio-42feced1d94238232fba92623e2682f3._googlecast._tcp.local.')}, uuid=UUID('42feced1-d942-3823-2fba-92623e2682f3'), model_name='Chromecast Audio', friendly_name='Living room', host='192.168.0.189', port=8009, cast_type='audio', manufacturer='Google Inc.')

>> print(cast.status)
CastStatus(is_active_input=True, is_stand_by=False, volume_level=1.0, volume_muted=False, app_id='CC1AD845', display_name='Default Media Receiver', namespaces=['urn:x-cast:com.google.cast.player.message', 'urn:x-cast:com.google.cast.media'], session_id='CCA39713-9A4F-34A6-A8BF-5D97BE7ECA5C', transport_id='web-9', status_text='')

>> mc = cast.media_controller
>> mc.play_media('http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', 'video/mp4')
>> mc.block_until_active()
>> print(mc.status)
MediaStatus(current_time=42.458322, content_id='http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', content_type='video/mp4', duration=596.474195, stream_type='BUFFERED', idle_reason=None, media_session_id=1, playback_rate=1, player_state='PLAYING', supported_media_commands=15, volume_level=1, volume_muted=False)

>> mc.pause()
>> time.sleep(5)
>> mc.play()

>> # Shut down discovery
>> pychromecast.discovery.stop_discovery(browser)

