#a and b are object far away at certain dist if b start moving with certian speed then what should
# be speed of a to catch b at 1/3 of dist
#speed = dist/time

def catch(in_dist,mov_speed):
    onethr = in_dist*0.3
    mov_time = onethr/mov_speed
    new_dist = in_dist+onethr
    speed = new_dist/mov_time
    return speed
try:
    a = float(input("Your distance from object( in KM ) "))
    b = float(input("Speed of object( in KMPH ) "))
except:
    print("Enter an number")
    exit()
else:
    print("to catch the object under " + str(a * 0.3) + " KM")
    try:
        print("Your speed should be " + str(catch(a, b)) + ' KMPH')

    except:
        print("Your speed or distance cannot be zero")




