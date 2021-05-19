a = int(input('Enter the Temperature in °'))

b = input('Enter the Temperature Scale \n(C for Celsius and F for Fahrenheit)\n')

# Formula For Converting Celsius to Fahrenheit
ctf = ((int(a)/5)*9)+32

#  Formula for Converting Fahrenheit to Celsius
ftc = ((int(a)-32)*5)/9



if b == 'C':
    print(str(a) + '° Celsius is ' + str(ctf) + '° Fahrenheit')
elif b == 'F':
    print(str(a) + '° Fahrenheit is ' + str(ftc) + '° Celsius')

input('Press Enter to Exit!')
