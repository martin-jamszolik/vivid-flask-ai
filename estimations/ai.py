from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI, VectorDBQA
from langchain.document_loaders import DirectoryLoader



class ProposalAIService:
    loader = DirectoryLoader('../downloads/estimations/', glob='**/*.txt')
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    

    def __init__(self, config):
        embeddings = OpenAIEmbeddings(openai_api_key= config['OPENAI_API_KEY'] )
        texts = self.text_splitter.split_documents(self.documents)
        docsearch = Chroma.from_documents(texts, embeddings)
        self.qa = VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="stuff", vectorstore=docsearch)

    def ask_question( self, query ):
        return self.qa.run(query)
         