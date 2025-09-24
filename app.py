import streamlit as st
import datetime

st.set_page_config(layout="wide")

st.title("Gerenciador de Aluguel de Filmes/Jogos")

# Lista de filmes ou jogos
produtos = [
    "O Senhor dos Anéis: A Sociedade do Anel",
    "The Witcher 3: Wild Hunt",
    "Duna: Parte Dois",
    "Cyberpunk 2077",
    "A Origem",
    "Red Dead Redemption 2"
]

# Interface do usuário
st.header("Registrar Novo Aluguel")

# Seleção do produto
produto_selecionado = st.selectbox("Selecione um filme ou jogo:", produtos)

# Seleção das datas
data_retirada = st.date_input("Data de Retirada:", datetime.date.today())
data_devolucao = st.date_input("Data de Devolução:", datetime.date.today() + datetime.timedelta(days=7))

# Botão para registrar o aluguel
if st.button("Registrar Aluguel"):
    # Lógica de cálculo de prazo e mensagens
    hoje = datetime.date.today()
    dias_restantes = (data_devolucao - hoje).days

    mensagem_prazo = ""
    if dias_restantes > 0:
        mensagem_prazo = f"Faltam {dias_restantes} dias para a devolução."
    elif dias_restantes == 0:
        mensagem_prazo = "A devolução é hoje!"
    else:
        mensagem_prazo = f"O prazo já passou! A devolução deveria ter sido há {-dias_restantes} dias."

    # Exibição das informações
    st.subheader("Informações do Aluguel:")
    st.write(f"**Produto:** {produto_selecionado}")
    st.write(f"**Data de Retirada:** {data_retirada.strftime('%d/%m/%Y')}")
    st.write(f"**Data de Devolução:** {data_devolucao.strftime('%d/%m/%Y')}")
    st.info(mensagem_prazo)


