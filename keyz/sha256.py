# Python 3 code to demonstrate 
# SHA hash algorithms. 

import hashlib 

# initializing string 
str = """FROM: https://www.ibm.com/support/knowledgecenter/SSYKE2_8.0.0/com.ibm.java.security.component.80.doc/security-component/jsse2Docs/publickeycertificates.html

A public key certificate provides a safe way for an entity to pass on its public key to be used in asymmetric cryptography. The public key certificate avoids the following situation: if Charlie creates his own public key and private key, he can claim that he is Alice and send his public key to Bob. Bob will be able to communicate with Charlie, but Bob will think that he is sending his data to Alice.

A public key certificate can be thought of as the digital equivalent of a passport. It is issued by a trusted organization and provides identification for the bearer. A trusted organization that issues public key certificates is known as a certificate authority (CA). The CA can be likened to a notary public. To obtain a certificate from a CA, one must provide proof of identity. When the CA is confident that the applicant represents the organization it says it represents, the CA signs the certificate attesting to the validity of the information contained within the certificate.

A public key certificate contains several fields, including:
Issuer - The issuer is the CA that issued the certificate. If a user trusts the CA that issues a certificate, and if the certificate is valid, the user can trust the certificate.
Period of validity - A certificate has an expiration date, and this date is one piece of information that should be checked when verifying the validity of a certificate.
Subject - The subject field includes information about the entity that the certificate represents.
Subject's public key - The primary piece of information that the certificate provides is the subject's public key. All the other fields are provided to ensure the validity of this key.
Signature - The certificate is digitally signed by the CA that issued the certificate. The signature is created using the CA's private key and ensures the validity of the certificate. Because only the certificate is signed, not the data sent in the SSL transaction, SSL does not provide for non-repudiation.
If Bob only accepts Alice's public key as valid when she sends it in a public key certificate, Bob will not be fooled into sending secret information to Charlie when Charlie masquerades as Alice.

Multiple certificates may be linked in a certificate chain. When a certificate chain is used, the first certificate is always that of the sender. The next is the certificate of the entity that issued the sender's certificate. If there are more certificates in the chain, each is that of the authority that issued the previous certificate. The final certificate in the chain is the certificate for a root CA. A root CA is a public certificate authority that is widely trusted. Information for several root CAs is typically stored in the client's Internet browser. This information includes the CA's public key. Well-known CAs include VeriSign, Entrust, and GTE CyberTrust."""

# encoding GeeksforGeeks using encode() 
# then sending to SHA256() 
result = hashlib.sha256(str.encode()) 

# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA256 is : ") 
print(result.hexdigest()) 

print ("\r") 

