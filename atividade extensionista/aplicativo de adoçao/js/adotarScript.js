document.getElementById("adoption-form").addEventListener("submit", function(event) {
    event.preventDefault();
  
    const formData = new FormData(this);
    const data = {};
    formData.forEach(function(value, key) {
      data[key] = value;
    });
  
    // Envia os dados do formulário para o servidor
    axios.post('URL_DO_SERVIDOR', data)
      .then(function (response) {
        console.log("Resposta do servidor:", response);
        alert("Formulário enviado com sucesso!");
      })
      .catch(function (error) {
        console.error("Erro ao enviar o formulário:", error);
        alert("Ocorreu um erro ao enviar o formulário. Por favor, tente novamente mais tarde.");
      });
  });
  