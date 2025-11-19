let DADOS = null; // variável global

async function carregarDados() {
  try {
    const resposta = await fetch('./dados.json'); // mesma pasta
    DADOS = await resposta.json();

    console.log("JSON carregado:", DADOS);

    exibirDadosNaTela();
  } 
  catch (erro) {
    console.error("Erro ao carregar JSON:", erro);
  }
}

function exibirDadosNaTela() {
  const div = document.getElementById("conteudo");

  div.innerHTML = `
    <strong>Nome:</strong> ${DADOS.nome}<br>
    <strong>Idade:</strong> ${DADOS.idade}<br>
    <strong>Cidade:</strong> ${DADOS.cidade}<br>
    <strong>Produtos:</strong> ${DADOS.produtos.join(", ")}<br>
  `;
}

carregarDados(); // inicia tudo

