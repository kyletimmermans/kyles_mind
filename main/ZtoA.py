'''
I Love Lance & Janice (Google FooBar Challenge)
===============================================

In the test cases, every lowercase letter [a..z] is replaced with the
corresponding one in [z..a], while every other character 
(including uppercase letters and punctuation) is left untouched. 
That is, 'a' becomes 'z', 'b' becomes 'y', 'c' becomes 'x', etc.
For instance, the word "vmxibkgrlm", when decoded, would become 
"encryption".

Write a function called solution(s) which takes in a string and 
returns the deciphered string.

Note: Not my solution, but helpful to have

The cipher is just reversing the positions of all the letters


Why ord() and chr()?
--------------------

We use ord() as the computer uses the ASCII numbering system
to help it know the order of the letters in the alphabet. And chr()
just turns that numbering system back into actual characters.


How does it work?
-=-=-=-=-=-=-=-=-

ord('z') - (ord(char) - ord('a'))

The first part "(ord(char) - ord('a')" gets the distance between
'a' and the cipher character in the normal alphabet. This
is important because we will need to apply that same distance to
the ciphered text (reversed order). Since we start at 'z' in the
cipher alphabet, we apply the same distance to 'z', which reveals
what the letter should be in the normal alphabet.

We have undone the reversal process of the cipher, by going the same
distance from the normal start to the ciphered letter and applying
that to the cipher alphabet, giving us the equivalent letter in the normal
alphabet. 


For example: cipher 'k' translates to normal 'p'.

'k' is 10 from the start ('a') in the normal alphabet
'p' is 10 from the start ('z') in the cipher alphabet



            1st: ord(char) - ord('a')                         2nd: ord('z') - ()
         -------------------------------                -------------------------------
Plain:  [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, [p], q, r, s, t, u, v, w, x, y, z]
                                                       
                2nd: ord('z') - ()                         1st: ord(char) - ord('a')
         -------------------------------                -------------------------------                  
Cipher: [z, y, x, w, v, u, t, s, r, q, p, o, n, m, l, [k], j, i, h, g, f, e, d, c, b, a]
                                                      
'''


def solution(s):
    decrypted_text = ""
    
    for char in s:
        # Only lowercase letters
        if 'a' <= char <= 'z':

            # Calculate the corresponding reversed lowercase letter
            # Go from z-a to a-z
            decrypted_text += chr( ord('z') - (ord(char) - ord('a')) )
        else:
            # Don't shift symbols, spaces, or uppercase letters
            decrypted_text += char
    
    return decrypted_text


# Driver
print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")) 
