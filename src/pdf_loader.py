from pypdf import PdfReader


def pdf_loader():
    page_counter = 0
    total_words = 0
    words_per_page = []
    average_words_per_page = 0
    max_words_per_page = 0

    for i,j in enumerate(reader.pages):
        current_page = j.extract_text()
        
        total_words_in_page = current_page.split()
        
        if max_words_per_page < len(total_words_in_page):
            max_words_per_page = len(total_words_in_page)
        
        words_per_page.append(len(total_words_in_page))

    print('max words in a page :',max_words_per_page) 
    print('total words in the PDF :',sum(words_per_page))
    print('average number of words per page: ', round(sum(words_per_page)/len(words_per_page),0))