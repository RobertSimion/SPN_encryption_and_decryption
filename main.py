import SPN
import random

def main():

    # Getting clear-text from console ,consists in 4 bytes.

    clearText = input("Enter cleartext made of 4 bytes:").split()

    # Transforming it in a list of 4 bytes.

    clearText = SPN.prepareClearText(clearText)
    print("The clear-text is:",clearText)

    # We have independent keys for each round.

    allKeys = []

    # Generate sBox-256 bytes used for substitution block.

    sBox = SPN.prepareSBox()
    print("The sBox is:",sBox)

    # Generate permutation structure for permutation block .

    permutation = SPN.preparePermutation()
    print(permutation)

    # I choose 10 Rounds for SPN algorithm.

    nrRounds = 10

    # Iterate Encryption phase of Algth. each round from 0 to 9
    # Print output of each Round for testing purpose only
    # Generate independent,random key each Round and
    # stack them into a list for decryption phase of Algth.

    for i in range(nrRounds):
        key = SPN.prepareKey()
        allKeys.append(key)
        encryptedText = SPN.encryptSPN(clearText,key,sBox,
                                       permutation)
        print("Encryption Output of round " + str(i) ,encryptedText)
        clearText = encryptedText


    # Verify each key generated during each Round.

    print("The generated keys are:",allKeys)

    # Generating inverse XOR operation, inverse Permutation
    # structure and invers sBox operation
    # for decrypting using the keys in reverse order
    # Print output of each Decryption Round for testing purpose
    # only.

    for i in range(nrRounds):
        decryptedText = SPN.decryptSPN(encryptedText,
                                       allKeys[nrRounds - i - 1],
                                       sBox,
                                       permutation)
        print("Decryption Output from round " + str(i),
              decryptedText)
        encryptedText = decryptedText









main()
