# Base64-Encoder-Decoder
This is a simple program that encode and decode Base64 strings.

python src.py -h
usage: src.py [-h] echo

positional arguments:
  echo        Enter an encoded or decoded Base64 string.
  
python src.py "Hello, World!"
SGVsbG8sIFdvcmxkIQ==

python src.py SGVsbG8sIFdvcmxkIQ==
Hello, World!
