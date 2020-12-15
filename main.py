import library as func

def main():
    print("Anggap ini remote AC :")
    while True:
        print("1. Power ON/OFF")
        print("2. Temperatur Up")
        print("3. Temperatur Down")
        print("4. FanSpeed Increase")
        print("5. Display Status")
        
        pilihan = int(input("Pilihan : "))
        print("")    

        if pilihan == 1:
            func.turnOnOff()
            initialState = func.checkOnOff()
            if not initialState:
                print("AC Mati")
            else:
                print("AC Hidup")
        elif pilihan == 2:
            func.tempUp()
        elif pilihan == 3:
            func.tempDown()
        elif pilihan == 4:
            func.fanSpeed()
        elif pilihan == 5:
            func.display()
        print("")    
        
if __name__ == "__main__":
    main()

