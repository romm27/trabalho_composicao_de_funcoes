f = eval("lambda x: " + input("f(x): ").replace('^', '**'))
g = eval("lambda x: " +  input("g(x): ").replace('^', '**'))
value = float(input("x: "))

print("(f∘g)({}) =".format(value), (lambda x: f(g(x)))(value))
print("(f∘f)({}) =".format(value), (lambda x: f(f(x)))(value))
print("(g∘f)({}) =".format(value), (lambda x: g(f(x)))(value))
print("(g∘g)({}) =".format(value), (lambda x: g(g(x)))(value))