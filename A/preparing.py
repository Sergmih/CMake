#!/usr/bin/python3

f = open('index.h', 'w')
f.write("#ifndef A_index\n")
f.write("#define A_index\n")
f.write("#include <iostream>\n")
f.write("void A_index_check()\n")
f.write("{\n")
f.write("std::cout << \"A_index added!\";\n")
f.write("return;\n")
f.write("}\n")
f.write("#endif")
f.close()
