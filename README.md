# ChatDot
A simple chatbot AI

# Setup
Currently setup is confusing so I simplified it with a Shell script.
You will need brew to run the script properly (homebrew is availible here "https://brew.sh/")

# Versions and platforms
  Supported Platforms
  - MacOS 12
  - MacOS 13
  - Rocky Linux 9

  Unsupported Platforms
  - Windows 11
  - Windows 10*
  - Windows 7

* if you are planning to attempt windows compatibilty i recommend starting with the library "spacy" as it has known issues with this program when running on windows.

# Data

The AI does not currently come with a trained dataset. if you would like to provide training data please open an issue. data can come as active interaction or a file containing valid conversations formatted as 

{("Query1",!, "Response1");; ("Query2",!, "Response2");; ("Query3",!, "Response3")}
&&
{("Query1",!, "Response1");; ("Query2",!, "Response2");; ("Query3",!, "Response3")}

where each conversation is a new line seperated by "&&"

# Features

the program can be interacted with via speech or text.
