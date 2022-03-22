# dio-pyspark-dataproc

Código criado para utilização junto a plataforma da Digital Innovation One

<p align="center"><img src="./DIO.png" width="500"></p>

### Resumo desafio PySpark

#### [1. Desafio GCP Dataproc](#desafio-gcp-dataproc)

#### [2. Como executar o desafio sem GCP](#como-executar-o-desafio-sem-gcp)


### Ferramentas utilizadas

- VSCode
- Anaconda 3
- Jupyter notebook
- Spyder IDE
- GCP (Google Cloud Platform)


## Desafio GCP Dataproc

O desafio faz parte do curso na plataforma da Digital Innovation One:

__*Criando um ecossitema Hadoop totalmente gerenciado com Google Cloud Platform*__

O desafio consiste em efetuar um processamento de dados utilizando o produto Dataproc do GCP. Esse processamento irá efetuar a contagem das palavras de um livro e informar quantas vezes cada palavra aparece no mesmo.

---

### Etapas do Desafio

1. Criar um bucket no Cloud Storage
1. Atualizar o arquivo ```bin/counter-dataproc.py``` com o nome do Bucket criado nas linhas que contém ```{SEU_BUCKET}```.
1. Fazer o upload dos arquivos ```bin/counter-dataproc.py``` e ```book.txt``` para o bucket criado (instruções abaixo)
    - https://cloud.google.com/storage/docs/uploading-objects

1. Utilizar o código em um cluster Dataproc, executando um Job do tipo PySpark chamando ```gs://{SEU_BUCKET}/bin/counter-dataproc.py```
1. O Job irá gerar uma pasta no bucket chamada ```./results```. Dentro dessa pasta o arquivo ```part-00000``` irá conter a lista de palavras e quantas vezes ela é repetida em todo o livro.

### Entrega do Resultado

1. Criar um repositório no GitHub.
2. Criar um arquivo chamado ```result.txt```. Dentro desse arquivo, colocar as 10 palavras que mais são usadas no livro, de acordo com o resultado do Job.
3. Inserir os arquivo ```result.txt``` e ```part-00000``` no repositório e informar na plataforma da Digital Innovation One.

---

### Considerações Finais

NOTA: Se o Job mostrar um WARN de Interrupt, basta ignorar. Existe um bug no Hadoop que é conhecido. Isso não impacta no processamento.

Qualquer outra dúvida, informação ou sugestão, fique a vontade para entrar em contato. 
marcelo@smarques.com

---

## Como executar o desafio sem GCP

Código otimizado por: [Francis Rodrigues](https://github.com/francisrod01)

Decidi criar o script `workd-counter.py` com **SparkSession**, onde recebe o arquivo **book-asset.txt** e, em memória, transforma, formata e agrupa os dados antes de realizar a contagem das palavras.

Convertido para DataFrame, a visualização dos dados torna-se simples.

Também foi adicionado um Jupyter notebook, onde você poderá em tempo de execução cada etapa.

## License

MIT
