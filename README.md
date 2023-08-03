This fork is an expanded and updated version of the original [py-tengwar-tex](https://github.com/bernardinelli/py-tengwar-tex). I am currently working on contacting the original maintainer for license clarification.  

Each *language*.py will transcribe latin alphabet letters to LaTeX commands that correspond to the [TengwarScript](https://www.ctan.org/tex-archive/macros/latex/contrib/tengwarscript) LaTeX package. Because different languages utilize different uses of the tengwa, it is the goal to get each language fully transcribable to the TengwarScript commands.

Current updates involve incorporating the Mode files from [Tecendil](https://github.com/arnog/tecendil-js) for ease of transcription.  The TecendilJSONasPydict.txt file is under maintenance to convert the JSON to a usable format with python. I understand there is probably a way to directly use the JSON file, I am not smart enough for that right now.  The converted JSON to python dictionary file is not usable and has many unfixed typos. If it comes down to a complete re-write of the transcription program, that will be way down the road.

Currently, Quenya.py corresponds directly to the original transcriber.py in the original repository.  Sindarin and beleriand are also direct copies of the original transcriber file, but will be updated in the future. English.py is updated, but not fully and therefore issues surrounding TH, CH, C, etc. are still an issue (see above re: using Mode files from Tecendil). 

Because of current limitations of the TengwarScript LaTeX package, English still has a lot of post-processing issues to deal with, especially since tehta are placed on the following tengwar rather than the preceding one. [Other efforts are underway](https://www.github.com/BardenB/TengwarScript) to fix this issue, where there will be little to no post-processing necessary. 

**Usage**: Save a .txt file with the text you would like to be transcribed to TengwarScript LaTeX commands. For example, if you are transcribing English into the Tengwar script, run English.py. The program will prompt for an input file and an output file. The output file will contain the transcribed LaTeX commands that can be input into any LaTex document using the correct packages. 

