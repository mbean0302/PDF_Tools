# Imports
import os
import sys
import time
import PyPDF2

# GLOBAL VARIABLES
original_folder = 'Original_PDF_Files/'
merged_folder = 'Merged_PDF_Files/'
merged_file = str()

# MERGE FUNCTION


def pdf_combiner():  # Function for merging files
    merger = PyPDF2.PdfFileMerger(strict=False)  # Merger class object
    # For loop to merge all files that were input into Command Line.
    for pdf in os.listdir(original_folder):
        merger.append(f'{original_folder}{pdf}')
    merger.write(merged_file)  # This is the new file created with merged content
    os.rename(merged_file, f'{merged_folder}{merged_file}')


# CHECK / CREATE DIRECTORIES
try:
    if not os.path.exists(original_folder):
        os.mkdir(original_folder)
    if not os.path.exists(merged_folder):
        os.mkdir(merged_folder)
except FileNotFoundError as err:
    print(f'Check for {original_folder} and {merged_folder} in current directory. Create, if necessary')
    print(f'File Not Found. {err}')

# DRAG AND DROP PDF FILES
print(f'Place the .PDF files you want to merge into the {original_folder[0:-1]} folder...')
time.sleep(.850)
os.startfile('Original_PDF_Files')

# MERGE CONFIRM
try:
    input('Press [ENTER] to merge files.')
except SyntaxError as syntax_err:
    print(f'Syntax Error: {syntax_err}')

# MOVE MERGED FILE INTO MERGED DIRECTORY

merged_file = str(input('Enter a filename for the merged file:  '))
while os.path.exists(f'{merged_folder}{merged_file}'):
    if os.path.exists(f'{merged_folder}{merged_file}'):
        print('Filename already exists. Please choose a different filename...')
        time.sleep(.850)
        merged_file = str(input('Enter a filename for the merged file:  '))
    else:
        break

# MERGE FILES

pdf_combiner()

# SHOW NEW MERGED FILE
try:
    input('Press [ENTER] to display merged file.')
except SyntaxError as syntax_err:
    print(f'Syntax Error: {syntax_err}')
os.startfile('Merged_PDF_Files')
time.sleep(.850)

# OPTION TO DELETE ORIGINAL JPG FILES
check_delete = str.upper(input('Do you want to delete original PDF files? [Y/N]:  '))
if check_delete == 'Y':
    for pdf_file in os.listdir(original_folder):
        file_path = os.path.join(original_folder, pdf_file)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as except_err:
            print('Failed to delete %s. Reason: %s' % (file_path, except_err))
    input('Files deleted. Press [ENTER] to close program.')
    sys.exit()
if check_delete == 'N':
    time.sleep(.650)
    input('Press [ENTER] to close program.')
    sys.exit()
# END PROGRAM
