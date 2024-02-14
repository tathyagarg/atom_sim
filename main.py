import space
import quark
import supplements as sup

spc = space.Space(3, 3).use_in_quarks()

qrk = quark.Quark(1, 1, 1, 1, 2).place()
spc.display(sup.SPACE_ARRAY_IDX.MASS)
sup.print_divider()
spc.display(sup.SPACE_ARRAY_IDX.ENERGY)
sup.print_divider()
spc.display(sup.SPACE_ARRAY_IDX.OBJECTS)
