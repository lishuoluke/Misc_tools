
import Pycrypto


def CBCMacWithStates(message, iv):
    """Computes the CBC-MAC of a message given the IV.

    Returns a tuple with the hash and a list of tuples; the first
    element is the block index and the second is the intermediate state
    associated with that block, as a byte string.

    It is expected that this returns the same hash as CBC-MAC above
    given the same inputs.
    """
    M_states = []

    paddedMessage = Pycrypto.padPKCS7(message)
    intermediateMessage = b''
    currentState = iv

    for bIndex in range(GetNumBlocks(paddedMessage)):
        intermediateMessage = GetBlock(paddedMessage, bIndex)

        cipher = AES.new(b'YELLOW SUBMARINE', AES.MODE_CBC, currentState)
        currentState = cipher.encrypt(intermediateMessage)
        currentState = currentState[-AES.block_size:]
        M_states.append( ( bIndex, currentState ) )

    return currentState, M_states