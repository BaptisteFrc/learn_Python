from enchant import Dict
import string
from time import time 

start_time = time()


dictionnary_english = Dict("en_US")

list_alphabet_lowercase = list(string.ascii_lowercase)
list_alphabet_uppercase = list(string.ascii_uppercase)
set_alphabet_lowercase = set(list_alphabet_lowercase)
set_alphabet_uppercase = set(list_alphabet_uppercase)



text = "Ew1aaevxrp9eertj9wvv|$mya9xjmck}dgmxkw1k1kwt$vw$(dh|c#j1ivbp9rautfkpp|u$ipt|cw51&]t$jditxw9bakxakdi9cazxtk~gxcqt3$B^j9el|1wl|w9~b9bakxaj1k1v|rmickzphjL>9X$qpr|1v|raweh`1bvdj}=$hdmmt$laaaazea)))51ew1autcxp9t|icajbmv$~v9el|1awemkt$jdi9~b9elpb$jtvptw9 $2156%$2156($2156 29:$|eg7=$nymzy$}tt|`j1kw1pqt$hde}cemdv|1k1pqt$zxvz}a51wv1pqpp9xb9el|1pkda9bqt1k1pqxw9bakxaj1mj1k(eepa()=$ckt1mm1em1kwra9el|1ulp`kpplca9~b9el|1gpcgut$~hu~sj?$Wpi|(-51M9yeot$~qwu$myem1pqt$jdi9~b9elpb$jtvptw9xw9p$jx|my$ipvm1k1pqt$j`qxca9~b9el|1t|cmttp|c$vw$mya9rmkrh|1sq~w|1`ppi|eak1mj15(1kk1f`1tleppc9el|1wl|$vw$mymj1w|cm|b$|`qx}$m~$j=$pe$qpw9el|1vxemv1whcp1_-9|quemi}m|u${h$j1pv159~b9el|1t|cmttp|c$m~$mya9umx|amtv71M9fmu}$j~kw1wq~s9elxe$mya9bqt1k1pqxw9bakxaj1pv1f|1eiavvimtpp|}}9 */%0 ]0)'2!%6+'0*'0_1ewu$ckt1il}ppah`xj~1pqxw9qtsak1f`1wpi(9pj}1pqtj9eerxj~1pqt$j`qxca9ckve(9el|1jl|f|c$*?5- 1 #2,-1!(3 (6*)$pb$p`|t`9avvuqzt`51sqxgq1aaav|bw|b$mya9aakxi|eak1k1e9rmkrh|1sq~w|1`ppi|eak1mj1571Bv}hvfmwv$xvep$mya9bett$jeaib${h$nymzy$P1lxu$xcvpga}1em1pqxw9bqt=$P1lxga9umjrkotv|u$myem1pqt$jdi9~b9el|1w|cm|b$(1/9 +(-$2156)59:$(>6,($2156+6,1/9tpz?$x}wv1`|aawuw9~j9el|1ulp`kpplca9~b9el|1gpcgut*9_etth`=$mya9bqt1k1pqxw9|quemi}m|u${h$ !$~xr|b$mya9smhde}cemt$1wklcpq1tvfak8$vw$mya9rmkrqtwaktjzt$vw$mya9aakxi|eak1k1e9rmkrh|1sq~w|1`ppi|eak1mj1571Ewu${h$jxip}ek1v|pwvmwv$P1lxga9}mrtspba9sa|$xsh|1pv1`|eak|mwt$mya9bqtb$vw$mya9bq{bahdawe$jtvptw9xj9flprl9el|1aaakwtjmb$xca9tr|$wdi{tvj?"

#"If we found this letter, we will be very happy."

new_special_index = -1
word_counter = 0

#for _ in range(26**3):
for index in range(len(text)):

    if text[index] not in set_alphabet_lowercase and text[index] not in set_alphabet_uppercase:
        old_special_index = new_special_index
        new_special_index = index    
        #new_special_charactere = text[index]
        word = text[old_special_index + 1:new_special_index]
        if len(word)==0 :
            print(text[index], end = "")
        else: 
            if dictionnary_english.check(word):
                print("{}{}".format(word, text[index]), end = "")

solution = 0         
for element in text:
    solution += ord(element)                    

print()
print(solution)
print(time() - start_time)  