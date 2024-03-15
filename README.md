Softwares needed
1. Pycharm community edition IDE
2. Python 3.11.18
3. Docker desktop : To install Docker CLI library.

Core components : Create the below resources in Azure Portal
- Azure Storage account & blob : Used to store uploaded files 
- Azure AI Search : Used for querying uploaded documents
- Azure Container Registry : Registry for containers
- Azure App Service : Hosting the application using docker
- Azure OpenAI service :  Using GPT turbo & Embedding LLM models

Design decisions: 
1. For better compatibility, we have opted for Azure services instead of other alternatives. 
Examples are Azure AI Search & Azure OpenAI service
2. We are using Docker for hosting Python code & Docker desktop to build & push image to container registry. 
3. LangChain is a developer platform that connects to any source of data or knowledge and supports building reliable GenAI apps.. Langchain works with Python so opted to develop solution using Python.
4. Pycharm community edition IDE : Utilising this free edition IDE to work with Python code. 


Models: 
1. gpt-35-turbo : Used with Chat Completion API
2. text-embedding-ada-002 : Langchain embedding to generate vector data

Accuracy is 90%-95%

How to setup locally -
1. Open the LangChainAzureSearch Folder in Pycharm.
2. Select Base interpreter as 3.11.8 when you receive a prompt. It would include Virtual environment creation as well.
3. Activate the virtual environment -  Pycharm Terminal run command: .venv\scripts\activate
4. Run command: pip install -r requirements.txt
5. Update configurations in .env file 

After the setup is complete, run below command in the terminal
- streamlit run .\application.py

Deploy docker
- docker ps
- docker login yourcontainerregistryname.azurecr.io --username <yourusername> --password <yourpassword>
- docker build -t yourcontainerregistryname.azurecr.io/app:v1 .
- docker push yourcontainerregistryname.azurecr.io/app:v1
- docker images

Note - Rename env.json to .env file for it to work
environment.json file content would be used to update the configuration settings in Azure App Service

startup command - python -m streamlit run application.py --server.port 8000 --server.address 0.0.0.0
