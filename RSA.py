import random
import math

# set of a bunch of primes to bs used for P and Q
primes = set()

public_key = None
private_key = None
n = None

# Sieve Of Eratosthenes method for finding prime numbers
def primer():

    global primes

    # get the prime numbers < 10000
    n = 10000
    prime = [True for i in range(n+1)]
    p = 2
    while(p*p <= n):
        #check for unmarked number
        if(prime[p]==True):
            for i in range(p*p, n+1, p):
                prime[i] = False #marks the multiples of p off
        p+=1
    
    for p in range(2, n+1):
        if prime[p]:
            primes.add(p)

def pickRandPrime():
    global primes

    k = random.randint(0, len(primes) - 1)
    it = iter(primes)
    for _ in range(k):
        next(it)
    
    ret = next(it)
    primes.remove(ret) #removes the taken prime from the primes set because p!=q
    return ret

def setKeys():
    global public_key, private_key, n
    P = pickRandPrime()
    Q = pickRandPrime()

    print("Primes we're working with for keys:")
    print("P:", P, " Q:", Q)

    n = P*Q
    fi = (P-1)*(Q-1) # totient

    #determine public key (e cannot be a factor of Φ(n))
    e, Found = 2, False
    while not Found:
        if math.gcd(e, fi) == 1:
            Found = True
        else:
            e+=1
    public_key = e

    #determine private key (d = (k*Φ(n) + 1) / e for some integer k)
    d, Found = 2, False
    while not Found:
        if (d*e)%fi==1:               
            Found = True
        else:
            d+=1
    private_key = d

def encrypt(msg):
    global public_key, n
    e = public_key
    encrypted_text = 1
    # c^e % n broken up using math laws (c^e is wayyyy too large)
    while e > 0:
        encrypted_text *= msg
        encrypted_text %= n
        e-=1
    return encrypted_text

def decrypt(e_msg):
    global private_key, n
    d = private_key
    decrypted_text = 1
    while d > 0:
        decrypted_text *= e_msg
        decrypted_text %= n
        d-=1
    return decrypted_text

#this is where all the ASCII jazz goes down
def encoder(message):
    encoded = []
    # encrypt each letter using the encrypt function
    for ch in message:
        encoded.append(encrypt(ord(ch))) #sends the ascii value to encrypt; the encrypt function assumes the integer message is being passed in
    return encoded

def decoder(e_message):
    s = '' # string concatenation for the decrypted message as a string
    for number in e_message: # e_message is a list of integers that represent characters
        s += chr(decrypt(number))
    return s
    
def main():
    print("Enter a message to be encrypted:")
    msg = input()
    coded_msg = encoder(msg)
    decoded_msg = decoder(coded_msg)
    print("The original message:", msg)
    print("The encrypted message:", ''.join(str(ch) for ch in coded_msg))
    print("I'd usually ask for your private key here to decode the message, but I'm feeling generous...")
    print("The decoded message:", ''.join(str(ch) for ch in decoded_msg))
    

if __name__ == "__main__":
    primer() # init set of primes less than 10k
    setKeys() # init public and private keys and n
    main() # calls main to query the user for a message