import random


'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''
def gcd(a, b):
        while b != 0:
                a, b = b, a % b
        return a

'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
def multiplicative_inverse(e, phi):
        d = 0
        x1 = 0
        x2 = 1
        y1 = 1
        temp_phi = phi
    
        while e > 0:
                temp1 = temp_phi/e
                temp2 = temp_phi - temp1 * e
                temp_phi = e
                e = temp2
                
                x = x2- temp1* x1
                y = d - temp1 * y1
                
                x2 = x1
                x1 = x
                d = y1
                y1 = y
    
        if temp_phi == 1:
                return d + phi


def prime_return():
        # return tuple of random prime numbers
        prime_list_1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        prime_list_2 =  [53, 59, 61, 67, 71, 73, 79, 83, 89,97]
        prime_num_1 = random.choice(prime_list_1)
        prime_num_2 = random.choice(prime_list_2) 
        return (prime_num_1,prime_num_2)

def generate_keypair(p, q):
        #n = pq
        n = p * q

        #Phi is the totient of n
        phi = (p-1) * (q-1)

        #Choose an integer e such that e and phi(n) are coprime
        e = random.randrange(1, phi)

        #Use Euclid's Algorithm to verify that e and phi(n) are comprime
        g = gcd(e, phi)
        while g != 1:
                e = random.randrange(1, phi)
                g = gcd(e, phi)

        #Use Extended Euclid's Algorithm to generate the private key
        d = multiplicative_inverse(e, phi)
        
        #Return public and private keypair
        #Public key is (e, n) and private key is (d, n)
        return ((e, n), (d, n))

def encrypt(pk, plaintext):
        #Unpack the key into it's components
        key, n = pk
        #Convert each letter in the plaintext to numbers based on the character using a^b mod m
        cipher = [(ord(char) ** key) % n for char in plaintext]
        #Return the array of bytes
        return cipher

def decrypt(pk, ciphertext):
        #Unpack the key into its components
        key, n = pk
        #Generate the plaintext based on the ciphertext and key using a^b mod m
        plain = [chr((char ** key) % n) for char in ciphertext]
        #Return the array of bytes as a string
        return ''.join(plain)
        

def RSA_encryption(message):
        """
        Method to convert message to encrypted code with private and public keys.
        
        Args: 
            message (str): message send by the client to the server
        
        Returns: 
            list: encrypted list of numbers in which public key is attached
        """
        print("RSA Encrypter/ Decrypter")
        prime1 , prime2 = prime_return()
        public, private = generate_keypair(prime1, prime2)
        encrypted_msg = encrypt(private,message)
        encrypted_msg.append((public))
        return encrypted_msg 

def RSA_decryption(encrypted_msg):
        """
        Method to convert encrypted message to client's message using the public key.
        
        Args: 
            encrypted_msg (list): encrypted list of numbers in which public key is attached
        
        Returns: 
            str: message decrypted to the string and send it to the client
        """
        public = encrypted_msg.pop()
        return decrypt(public, encrypted_msg)
