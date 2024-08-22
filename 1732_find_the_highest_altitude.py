def altitudeGrab(gain):
    peak = 0
    altitude = peak
    for x in gain:
        altitude += x
        peak = max(peak, altitude)
    return peak


gain = [-5,1,5,0,-7]


print(altitudeGrab(gain))