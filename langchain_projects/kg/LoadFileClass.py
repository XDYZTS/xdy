from langchain_community.document_loaders import PyPDFLoader
file_path = (r"C:\Users\Windows\Desktop\xdy\langchain_projects\kg\input_data\乙炔气瓶充装规定.pdf")
loader = PyPDFLoader(file_path)
pages = loader.load_and_split()
print(pages[0].page_content)