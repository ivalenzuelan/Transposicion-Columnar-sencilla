# **Simple Transposition Cipher Breaker**

## **Introduction**

The **Simple Transposition Cipher** is a type of encryption where the order of the characters in the message is rearranged according to a specific system. In this script, we attempt to break a Simple Transposition Cipher by trying different column permutations to reveal the original message.

## **Code Overview**

The provided Python script reads a ciphered text from the file "transColText.txt" and attempts to break the cipher using column permutations. The script then compares the deciphered text with a list of the 1000 most common English words from the file "1-1000.txt" to identify potential solutions.

### **Usage**

The script takes the number of columns (`numCol`) as an argument. The range of columns to explore is set between 2 and 6, as these are commonly observed in Simple Transposition Ciphers.

```bash
python script.py

Code Efficiency

The script efficiently generates column permutations and evaluates potential solutions by considering the frequency of English words in the deciphered text. It outputs the possible solutions, including the original message and the column permutation used.
Dependencies

The script utilizes the numpy library for array manipulation and requires two input files: "transColText.txt" (ciphered text) and "1-1000.txt" (common English words).
Instructions

    Ensure you have the necessary dependencies installed:

bash

pip install numpy

    Place your ciphered text in the file "transColText.txt" and the list of common English words in "1-1000.txt".

    Run the script:

bash

python script.py

    Review the output for potential solutions, including the original message and the column permutation used.

Note: The efficiency of finding the correct solution may depend on the length and complexity of the ciphered text.

Feel free to experiment with different values for the number of columns (numCol) and adapt the script to your specific use case.
