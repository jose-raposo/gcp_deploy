# Deploy de API Flask no Google Cloud Platform com App Engine e Postman
![google gloud](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/Google_Cloud_Covered.png)

> Esse repositório faz parte de um [artigo escrito no Medium](https://medium.com/@jraposoneto60/deploy-de-api-flask-na-gcp-com-app-engine-e-postman-do-mkdir-%C3%A0-n%C3%BAvem-46958da0f933) onde demonstro passo a passo como realizar o Deploy de uma API em Flask no serviço PaaS App Engine da Google Cloud Platform.
### Etapas
- Criação do diretório principal `gcp_deploy`.
- Criação das subpastas `/data`, `/model` e `/app` dentro do diretório principal.
- Colocação do dataset na pasta `/data`.
- Criação do script _train_model.py_, onde defino a função _train_model()_ que registra as métricas de validação em um arquivo _metricas_.txt e gera um pipeline treinado com nome _model.pkl_.
- Criação do arquivo _app.yaml_ dentro da pasta `/app`.
- Criação do script main.py no diretório `/app` que contém a API em Flask.
- Runtime em localhost e verificação da integridade da API com o [Postman](https://www.postman.com/).
- Commit do conteúdo da pasta `gcp_deploy` para repositório do GitHub.
- Criação da conta no [Google Cloud Platform](https://www.cloud.google.com).
- Criação de instância no serviço **App Engine**.
- Abrir o shell terminal no browser.
- `git clone <MEU-REPOSITORIO>`. Aqui faremos um clone do repositório criado no GitHub contendo os arquivos para o serviço do App Engine.
- `cd <NOME-REPOSITÓRIO>/<app/>`.
- Basta seguir os comandos para realizar o deploy. `gcloud init`, fornecendo 1 como resposta às perguntas do shell.
- Por fim, `gcloud app deploy` para construir a API. Após concluído, será disponibilizado um link que será novamente testado utilizando o Postman.

Caso haja alguma dúvida, sugiro a leitura do artigo do Medium disponibilizado aqui: [Artigo](https://medium.com/@jraposoneto60/deploy-de-api-flask-na-gcp-com-app-engine-e-postman-do-mkdir-%C3%A0-n%C3%BAvem-46958da0f933).
