pikachu_roll = 4500
otaku_roll= 5000
pulpu_venenoso_roll=5200
aniguila_electrica_roll=4800
pikachu_roll_total=0
otaku_roll_total=0
pulpu_venenoso_roll_total=0
aniguila_electrica_roll_total=0


while True:
    print("bienvenido a la compra de sushi por delivery, que desea llevar")
    print(f"1. pikachu roll por: ${pikachu_roll} c/u ")
    print(f"2. otaku roll por: ${otaku_roll} c/u ")
    print(f"3. pulpu venenoso roll por: ${pulpu_venenoso_roll} c/u ")
    print(f"4. anguila electrica roll por: ${aniguila_electrica_roll} c/u ")

    opcion=input("seleccione una opcion del (1-4)")

    if opcion=="1":
        cantidad_de_pikachu_roll=float(input("ingrese la contidad de roll: "))
        if cantidad_de_pikachu_roll <= pikachu_roll:
        
         pikachu_roll*cantidad_de_pikachu_roll
       
         print(f"su total de pikachu roll es: ${pikachu_roll_total}")
   
    elif opcion=="2":
        cantidad_de_otaku_roll=float(input("ingrese la contidad de roll: "))
        if cantidad_de_otaku_roll <= otaku_roll:
        
         otaku_roll*cantidad_de_otaku_roll
         
         print(f"su total de pikachu roll es: ${otaku_roll_total}")
 
    elif opcion=="1":
        cantidad_de_pulpo_roll=float(input("ingrese la contidad de roll: "))
        if cantidad_de_pulpo_roll <= pulpu_venenoso_roll:
        
         pulpu_venenoso_roll*cantidad_de_pulpo_roll
       
         print(f"su total de pikachu roll es: ${pulpu_venenoso_roll_total}")
   
    elif opcion=="1":
        cantidad_de_angila_roll=float(input("ingrese la contidad de roll: "))
        if cantidad_de_angila_roll <= aniguila_electrica_roll:
        
         aniguila_electrica_roll*cantidad_de_angila_roll
       
         print(f"su total de pikachu roll es: ${pulpu_venenoso_roll_total}")
    break

print("desea agregar algo mas")  




 
