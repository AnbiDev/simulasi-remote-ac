import variabel as var

def checkOnOff():
    '''untuk cek status AC mati atau nyala'''
    '''jika True -> Hidup jika False -> Mati'''
    return var.status

def turnOnOff():
    '''mengubah status AC untuk nyala dan mati'''
    var.status = True if not var.status else False

def tempUp():
    '''menaikkan  suhu AC'''
    initialState = checkOnOff() 
    # jika AC hidup maka eksekusi kode dibawahnya
    if initialState: 
        if var.temp < 28:
            var.temp += 1

def tempDown():
    '''menurunkan suhu AC'''
    initialState = checkOnOff() 
    # jika AC hidup maka eksekusi kode dibawahnya
    if initialState: 
        if var.temp > 18:
            var.temp -= 1

def fanSpeed():
    '''menaikkan kecepatan kipas AC'''
    initialState = checkOnOff() 
    # jika AC hidup maka eksekusi kode dibawahnya
    if initialState: 
        var.fan = var.fan + 1 if var.fan < 4 else 1
    
def powerChill():
    ''' set nilai temperatur paling rendah dan fan paling tinggi '''
    initialState = checkOnOff()
    # jika AC hidup maka eksekusi kode dibawahnya
    if initialState:
        var.temp = 18
        var.fan = 4

def display():
    ''' display status fan dan temp '''
    initialState = checkOnOff()
    # jika AC hidup maka eksekusi kode dibawahnya
    if initialState:
        print("Temperatur Suhu : ", var.temp)
        print("Level Kipas : ", var.fan)
