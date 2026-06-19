from pypdf import PdfReader

# folder_path = r"C:\Users\Sumed\Desktop\rag_assistant\data\*pdf"

def pdf_loader(folder_path):
    pdf_files = glob.glob(folder_path)

    if not pdf_files:
            raise Exception('No document(s) found')
    else:
        print(f'{len(pdf_files)} document(s) found')

    for i in pdf_files:
        print(i)
    
    page_counter = 0
    total_words = 0
    words_per_page = []
    average_words_per_page = 0

    for i in pdf_files:
        print('processing file : ', i)
        reader = PdfReader(i)
        max_words_per_page = 0

        for _,j in enumerate(reader.pages):
            current_page = j.extract_text()
            total_words_in_page = current_page.split()
            
            if max_words_per_page < len(total_words_in_page):
                max_words_per_page = len(total_words_in_page)
            words_per_page.append(len(total_words_in_page))

        print('max words in a page :',max_words_per_page) 
        print('total words in the PDF :',sum(words_per_page))
        print('average number of words per page: ', round(np.divide( sum(words_per_page),len(words_per_page) ),0) )
        print('\n')