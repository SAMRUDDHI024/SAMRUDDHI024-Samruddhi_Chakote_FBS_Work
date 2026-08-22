 # 3. Convert distant given in feet and inches into meter and centimeter

# take  input 
f = int(input('enter the distant in feet :'))
i = int(input('enter the distant in inches :'))

# perform opration
m = f * 0.3048
cm = i * 2.54

# display result
print(f'with input feet :{f} and inches :{i}, the diatance in meter :{m}m and centimeter : {cm}cm .')