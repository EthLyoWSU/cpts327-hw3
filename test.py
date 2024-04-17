import time

SECRET_PIN = b"0000000000"

pin_guess = b"0000000000"

for i , digit in enumerate ( pin_guess ) :
    if i < len ( SECRET_PIN ) and digit == SECRET_PIN [ i ]:
        time.sleep(0.3)
        print ( " Verifying :... " )
        time.sleep(0.3)
        print ( " Verifying :... " )
    else :
        for j in range (i , len ( pin_guess ) ) :
            time.sleep(0.1)
            print ( " Verifying :... " )
            time.sleep(0.1)
            print ( " Verifying :... " )
            print ( " [ * * * ] ERROR : Verification failed ! " )

pin_guess = b"1111111111"

print("\n\n")

for i , digit in enumerate ( pin_guess ) :
    if i < len ( SECRET_PIN ) and digit == SECRET_PIN [ i ]:
        time.sleep(0.3)
        print ( " Verifying :... " )
        time.sleep(0.3)
        print ( " Verifying :... " )
    else :
        for j in range (i , len ( pin_guess ) ) :
            time.sleep(0.1)
            print ( " Verifying :... " )
            time.sleep(0.1)
            print ( " Verifying :... " )
        print ( " [ * * * ] ERROR : Verification failed ! " )
        break