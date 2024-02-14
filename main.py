import space
import quark

spc = space.Space(3, 3)
quark.Quark.use_space(spc)

qrk = quark.Quark(1, 1, 1, 1)
print(qrk.checksum)
