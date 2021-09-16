# cryptopals
## What is Cryptopals
Cryptopals is a website that hosts sets of crypography problems designed to teach you cryptography.  It is hosted at https://cryptopals.com/.
## How I wrote my solutions
Broadly I wrote my code in the following way.  Each set has either one or a few unit tests that attempt to execute the solution to the problem.  These are located under tests/unit_tests/<set>/<challenge>.  Any code that actually does something or is used in multiple problems is located at <set>/<challenge>.  This format was chosen both to make the solutions easily demonstratable but also to ensure that if I re-work some of the code to make it more efficent for use in later problems that it still works as intended.
## Current Progress
#### Set 1
  - Challenge 1: Convert hex to base64.                   Completed
  - Challenge 2: Fixed XOR                                Completed
  - Challenge 3: Single-byte XOR cipher                   Completed
  - Challenge 4: Detect single-character XOR              Completed
  - Challenge 5: Implement repeating-key XOR              Completed
  - Challenge 6: Break repeating-key XOR                  Completed
  - Challenge 7: AES in ECB mode                          Completed
  - Challenge 8: Detect AES in ECB mode                   Completed
#### Set 2
  - Challenge 9: Implement PKCS#7 padding                 Completed
  - Challnege 10: Implement CBC mode                      Completed
  - Challenge 11: An ECB/CBC detection oracle             Completed
  - Challenge 12: Byte-at-a-time ECB decryption (Simple)  In Progress
  - Challenge 13: ECB cut-and-paste
  - Challenge 14: Byte-at-a-time ECB decryption (Harder)
  - Challenge 15: PKCS#7 padding validation
  - Challenge 16: CBC bitflipping attacks
