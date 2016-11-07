#3_3

def lang_genoeg(lengte):
    if int(lengte) > 119:
        status = 'Je bent lang genoeg!'
    else:
        status = 'Sorry, je bent te klein'
    return status

print(lang_genoeg(121))
