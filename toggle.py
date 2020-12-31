import requests


# Set this to the IP address of your McLighting controller.
lights_ip = 'http://192.168.0.2'

mode = None
endpoint = lights_ip + '/status'
r = requests.get(endpoint)
if r.status_code == 200:
    print(r.content)
    mode = r.json()['mode']
    # Note that this does not match the mode in the API doc.
    # Am I on an old version?

if mode is not None:
    if mode == 1:
        # turn the lights off
        # payload = {'m': '2', 'rgb': 'ff00bb'}
        endpoint = lights_ip + '/off'
        r = requests.get(endpoint)

    elif mode == 2:
        # turn the lights on
        payload = {'m': '0', 'rgb': '8900FF'}
        endpoint = lights_ip + '/set_mode'
        r = requests.get(endpoint, params=payload)

    else:
        # nothing
        pass