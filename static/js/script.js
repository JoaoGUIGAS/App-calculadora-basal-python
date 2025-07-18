document.getElementById('calculadoraForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const dados = {
        peso: parseFloat(document.getElementById('peso').value),
        altura: parseFloat(document.getElementById('altura').value),
        idade: parseInt(document.getElementById('idade').value),
        genero: document.getElementById('genero').value,
        nivel_atividade: document.getElementById('nivel_atividade').value,
        objetivo: document.getElementById('objetivo').value
    };

    try {
        const response = await fetch('/calcular', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dados)
        });

        const resultado = await response.json();

        if (resultado.sucesso) {
            document.getElementById('resultados').classList.remove('d-none');
            
            // Atualiza TMB e calorias
            document.getElementById('tmb').textContent = `${resultado.tmb} kcal`;
            document.getElementById('calorias').textContent = `${resultado.calorias} kcal`;
            
            // Atualiza macronutrientes
            document.getElementById('proteinas').textContent = `${resultado.macros.proteina}g`;
            document.getElementById('carboidratos').textContent = `${resultado.macros.carboidratos}g`;
            document.getElementById('gorduras').textContent = `${resultado.macros.gorduras}g`;
            
            // Atualiza percentuais
            document.getElementById('proteinas_pct').textContent = `${resultado.macros.proteina_pct}% das calorias`;
            document.getElementById('carboidratos_pct').textContent = `${resultado.macros.carboidratos_pct}% das calorias`;
            document.getElementById('gorduras_pct').textContent = `${resultado.macros.gorduras_pct}% das calorias`;

            // Anima os resultados
            document.getElementById('resultados').classList.remove('animate__fadeIn');
            void document.getElementById('resultados').offsetWidth;
            document.getElementById('resultados').classList.add('animate__fadeIn');
        } else {
            alert('Erro ao calcular: ' + resultado.erro);
        }
    } catch (error) {
        alert('Erro ao processar a requisição');
        console.error(error);
    }
}); 