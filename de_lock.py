def asahi(fff):
    import ctypes 
    import io
    import hashlib
    Highttest = ctypes.cdll.LoadLibrary("./KISA_HIGHT_ECB.dll")
    Highttest.HIGHT_Decrypt.restype = ctypes.c_byte
    zerodata11=bytes(136)
    zerodata1=bytes(8)
    keydata=bytes(16)
    #keydata=b'%gTy^OZ$'+bytes(8)
    #keydata=b'\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xAA\xBB\xCC\xDD\xEE\xFF'
    hightfunc1 = Highttest.HIGHT_KeySched(keydata, 16, zerodata11)
    fff_out = b''
    c=0
    a=1
    b=1
    d=0
    zzokzzokyaong=io.BytesIO(fff)
    while True:
        fileobj=zzokzzokyaong.seek(0+c)
        eht=fileobj=zzokzzokyaong.read(8)
        if eht == b'' :
            break
        outdata = eht
        hightfunc2 = Highttest.HIGHT_Decrypt(zerodata11, outdata)     
        fff_out = fff_out+outdata
        c=c+8
        a=a+1
    return fff_out