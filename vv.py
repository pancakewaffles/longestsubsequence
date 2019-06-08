ss = 'GENR EYPT RERZ DIPT KMVR NKST NVTR XDKP IGNT ETEK RZSR KITZ WVKD XIEZ MKVX VXGX HZWR ZSTM ZUUN SFXR RKVV TZVE XMKY MKVZ PMRK VNSR ZSRP MMKS TIMZ FMXD VVTZ ITEK HXMK XUVZ RMKY NTKY GNTE TEKR MKXT NZSZ WXSZ ITND XUXU FZMN TEDW ZMVZ ULNS FTEK VNSF UKVZ PMRK VEZM TKVT IXTE IMZO UKDX VGKU UXVO KNSF XSKX MUHI MZIZ SKST ZWVT MPRT PMKY IMZF MXDD NSFV TZIF NLKT EKNM VPMS XDKV TZIX'

# most common 1gram
onegram = {}
b = list(ss)
for a in b:
    if a not in onegram.keys():
        onegram[a] = 1
    else:
        onegram[a] += 1
del onegram[' ']
print(onegram)
# most common 2gram

# most common 3gram

# most common 4gram
