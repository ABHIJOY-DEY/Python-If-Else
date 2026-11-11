temp = int(input())
if temp>=0:
    if temp>=10:
        if temp>=20:
            if temp>=30:
                if temp>=40:
                    print("It's very hot")
                else:
                    print("It's hot")
            else:
                print("Normal in temperature")
        else:
            print("Cold weather")
    else:
        print("Very cold weather")
else:
    print("Freezing weather")
            