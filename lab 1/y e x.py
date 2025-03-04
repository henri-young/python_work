x = float(input("Dê-me um número: ")) #qualquer coisa
if x<1:
    y=x
    if x==1:
        y=0
else:
    y=x**2
print(f"y = {y:.3f} and x = {x:.3f}")