from langchain_openai import ChatOpenAI

llm = ChatOpenAI(api_key="your-api-key")
response = llm.invoke("What is a Hello World in the software development world?")

print("")
print( response.content )
print("")