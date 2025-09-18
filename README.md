# Confidentially 

How my solution upholds confidentiality is that the message is encrypted using AES with a randomly generated 256-bit key. Making  sure  only someone with the key can read it. 

# Integrity 
How my solution upholds integrity is that the SHA-256 has ensures that the decrypted message is identical to the original. If alerted, the hashes will never match.


# Availability
How my solution upholds availability is that the process can be easily run again on any system with Python . Making sure data can always be accessed and, of course, verified.  

# Entropy & Key Generation

Entropy refers to the randomness collected from  a system, which is essential for producing secure cryptographic values. In  this project, the entropy is harnessed using os.urandom(), which provides unpredictable values from the operating system's cryptographic random number generator. These values are then used to generate both the AES key and the initialization vector. The AES key is 256 bits long,making it extremely resistant to brute force attacks ,while the random initialization vector ensures that even if the same message is encrypted multiple times, the ciphertext will always differ. Together, entropy and secure key generation provide the foundation for strong encryption and reliable data protection. 
