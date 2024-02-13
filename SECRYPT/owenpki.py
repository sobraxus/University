# Gareth Owen, University of Portsmouth
# RSA / Public Key utility functions
# revised by David Williams, david.m.williams@port.ac.uk, University of Portsmouth

import random

# fermat - probably prime - false positive less than 2^-60
def is_prime(p, a=2):
    if(p==2): return True
    if(not(p&1)): return False
    return pow(a,p-1,p)==1

# get prime +/- 1 bit of desired bits
def get_prime(x):
    global rnd
    while True:
        # uses os.urandom() - should be cryptographically secure
        rnd = random.SystemRandom().getrandbits(x+1)
        if rnd < 2**(x-1): #avoid numbers too small
            continue
        if rnd & 1 == 0:  # if not odd, let's make it odd
            rnd += 1
        if is_prime(rnd):  #got a potential prime
            fail = False
            for i in range(10):   # check with different bases
                a = random.randint(2,rnd-1)
                if not is_prime(rnd, a):
                    fail = True
                    print("[note] Candidate Prime (",rnd,") failed second safety check (a=",a,") - searching for a new prime")
                    break
            if fail:
                continue
            return rnd #probably a prime

def find_primes(x):
  return filter(is_prime, xrange(2,x))

# extended Euclidean Algorithm
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

# modular inverse, find ? such that a*?=1 mod bkm .jgh
def modinv(a, b):
    g, x, y = egcd(a, b)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % b

# generate, test and output an RSA key
def gen_key(x):
    p = get_prime(x)
    q = p
    while q==p:
        q = get_prime(x)

    n = p*q
    phin = (p-1)*(q-1)
    e=65537
    d=modinv(e, phin)

    print("p=",p)
    print("q=",q)
    print("n=",n)
    print("phin=",phin)
    print("e=",e)
    print("d=",d)
    for i in range(2,min(500,n-1)):
        testEncDec = pow(i, e*d, n)
        if testEncDec != i:
            print("Checked encryption / decryption [FAILED***]: ",i)
            break

def rsa_int_to_ascii(i):
    return bytes.fromhex(hex(i)[2:]).decode('utf-8')
