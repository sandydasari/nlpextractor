# nlptools
HOW TO EXTRACT DETAILS USING MEDCAT AND SPACY(NLP)TOOLS 
1. Create a virtual environment and pyenv for python 3.8.0
2. After activating the virtual environment, install the requirements.txt
pip install -r requirements.txt
3. Load the medcat model: !wget https://medcat.rosalind.kcl.ac.uk/media/medmen_wstatus_2021_oct.zip -P ./data/
4. Install the spacy model: python -m spacy download en_core_web_md
5. Input the required text files into files directory
6. Run python extract_details.py

# Testing the details
Here it's customized for Bahmni covid reports and to run, use python test_extract_details.py 
