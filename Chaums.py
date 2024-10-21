from math import gcd

def RSA(p: int, q: int):
    n = p * q
    phi = (p - 1) * (q - 1)
    # public key, e
    for i in range(2, phi):
        if gcd(i, phi) == 1:
            e = i
            break

    # private key, d
    j = 0
    while True:
        if (j * e) % phi == 1:
            d = j
            break
        j += 1
    return e, d ,n

def ChaumBlindSignature(p: int, q: int, message: int, blinding_factor: int):

    # Generate public and private key
    e, d ,n = RSA(p, q)
    print("Public key : %d\nPrivate key : %d\n"%(e,d))

    # Blind the message
    blinded_message = (message * (blinding_factor ** e)) % n
    print('blinded_message : ',blinded_message)
    # Sign the blinded message
    blinded_signature = (blinded_message ** d) % n

    # Unblind the signature
    unblinded_signature = (blinded_signature * (blinding_factor ** -e)) % n

    # Verify the signature
    verified_message = (unblinded_signature ** e) % n

    # return verified_message == message

    return blinded_message, blinded_signature, unblinded_signature , verified_message

# Example usage
p = 3
q = 17
message = 12
blinding_factor = 7

blinded_message, blinded_signature, unblinded_signature ,verified_message= ChaumBlindSignature(p, q, message, blinding_factor)

print("Blinded message:", blinded_message)
print("Blinded signature:", blinded_signature)
print("Unblinded signature:", unblinded_signature)
print("Verified message:", verified_message)