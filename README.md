# Aplicativo de Análise Selic

Faça simulações e precificações da SELIC em tempo real, verificando qual o melhor banco (ou investimento) de acordo com seu perfil de investidor.

###### Dê uma ⭐ se você gostar do repositório!
###### Faça um fork e contribua para um aplicativo mais robusto! 💪🏻

Para clonar o repositório:
> git clone https://github.com/felp99/selic_app_analise.git

## Rodando localmente:
Instale as dependências necessárias:
> pip install -r requirements.txt

Rode o comando no diretório raiz:
> streamlit run app.py

Recomendo rodar dentro de um .env

## Funcionamento do App:

### Selecione uma página na <i>sidebar</i>:

Aqui você pode selecionar diferentes features do aplicativo sem sobrecarga do Streamlit. 

![image](https://user-images.githubusercontent.com/76445505/170893825-91c9d0ea-6fe6-4379-91da-40207dff52ab.png)

#### 1. Simulação de retorno

Faça uma comparação entre Nubank e PicPay, verificando a taxa Selic atual, as taxas da plataforma escolhida, considerando a mordida do leão e o ROI estimado. Essa simualção contará com seu investimento inicial, e, no caso do Nubank, com a quantidade de tempo que você quer deixar o dinheiro guardado (o imposto varia).

<img src="https://user-images.githubusercontent.com/76445505/170893933-fc989ecf-2d1a-45e2-9e1a-f051d47722d3.png" width="633" height="516.5" />

#### 1. Comparação entre plataformas

Como dito acima, o valor investido e o tempo modificam o valor futuro do seu investimento. Sendo assim, veja o crescimento do seu dinheiro aportando em uma conta remunerada (Picpay) ou em um CDB que responde ao imposto regressivo e IOF de maneira convencional. (Nubank)

<img src="https://user-images.githubusercontent.com/76445505/170893982-1ef6b3cf-cf1a-4d81-bf20-0effe152c746.png" width="633" height="516.5" />

##### New features comming soon...
