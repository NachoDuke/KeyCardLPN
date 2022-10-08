# KeyCardLPN

## What is this?
This is a rough design of a security system that can be implemented in hotels or other applications. It works using the non-linear Hopper-Blum cryptographic Protocol implementing random Bernoulli Noise for added security. It uses a vector of binary digits as a secret key and each lock uses a number of challenges, each of which is based on the scalar multiplication of the key vector with another random binary vector to obtain a single binary digit. Based on the percentage of passed challenges, the lock is either opened or left closed.

## Why does this work?
Suppose my Bernoulli parameter is 'p'. That means that the probability of choosing 1 is p and the probability of choosing 0 is 1-p. Now, after obtaining the scalar product, I have to choose a random bernoulli draw. Now, once I apply the XOR operation between the result of the scalar multiplication and the random digit, I get the same digit with probability 1-p and the flipped digit with probability p.

All that's left is to check whether the fraction of passed challenges is close enough to '1-p'.

