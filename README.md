# xml-to-text-converter
A script for converting base64-encoded strings contained in an XML file into a text file:

* The script detects an XML file contained in the same directory and takes it as an input. 
  It will process only one file at a time.
* When the script is run, the user is prompted to input the name of the XML element containing a base-64 encoded string.
* The string will be decoded and saved in the same directory as "decoded_text.txt".

Base64 and xml.etree.ElementTree are used for decoding and for processing of XML elements.
