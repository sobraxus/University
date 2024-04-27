def generate_DH_values(number):
    if len(number)!=3 or number.isnumeric()!=True:
        return 'ERROR: Input must be a string of 3 numeric digits'
    digitz = [int(x) for x in number]
    print('The public generator g is: 3')
    print('The public modulus p is: 23')
    print('Alices private number is:', digitz[1]+5)
    print('Bobs private number is:', digitz[2]+15)


def generate_ECDH_values(number):
    if len(number)!=3 or number.isnumeric()!=True:
        return 'ERROR: Input must be a string of 3 numeric digits'
    digitz = [int(x) for x in number]
    print('The public Elliptic Curve constant a is: -7')
    print('The public Elliptic Curve constant b is: 10')
    print('The public field value p: 1009')
    print('The public generator point P is: (1,2)')
    print('Alices private number is:', int(number[:1]+'3'))
    print('Bobs private number is:', int(number[1:] + '7'))

msgA = ['{ Ki,Ni }pk(R)','{ I,Ki,Ni }pk(R)','{ I,R,Ki,Ni }pk(R)']
msgB = ['{ I,R }Ki, { Kr,Nr }pk(I)','{ I,R,Ni }Ki, { Kr,Nr }pk(I)','{ I,R,Ni,Nr }Ki, { Kr,Nr }pk(I)']
msgC = ['{ I,R }Kr','{ I,R,Ni }Kr','{ I,R,Ni,Nr }Kr']

def generate_protocol_two(number):
    if len(number)!=3 or number.isnumeric()!=True:
        return 'ERROR: Input must be a string of 3 numeric digits'
    digitz = [int(x)%3 for x in number]
    print('Protocol specification for PROTOCOL_TWO (in common syntax)')
    print(' ')
    print('I, R :  	Principal')
    print('Ki, Kr :  	Key')
    print('Ni, Nr :  	Nonce')
    print('pk :    	Principal -> Key')
    print(' ')
    print('1. I->R: ', msgA[digitz[0]])
    print('2. R->I: ', msgB[digitz[1]])
    print('3. I->R: ', msgC[digitz[2]])

msgX = ['Kir,Ni','I,Kir,Ni','I,R,Kir,Ni']
msgY = ['Ni','I,Ni','I,R,Ni']

def generate_protocol_five(number):
    if len(number)!=3 or number.isnumeric()!=True:
        return 'ERROR: Input must be a string of 3 numeric digits'
    digitz = [int(x)%3 for x in number]
    print('Protocol specification for PROTOCOL_FIVE (in common syntax)')
    print(' ')
    print('I, R, S :  	Principal')
    print('Kir     :  	Key')
    print('Ni      :  	Nonce')
    print('k       :  	(Principal, Principal) -> key')
    print(' ')
    print('1. I->S: { I,R,Ni }k(I,S)')
    print('2. S->I: {', msgX[digitz[0]],', {', msgX[digitz[1]], '}k(R,S) }k(I,S)',)
    print('3. I->R: { Ni }Kir, {', msgX[digitz[1]], '}k(R,S)')
    print('4. R->I: {', msgY[digitz[2]], '}Kir')
