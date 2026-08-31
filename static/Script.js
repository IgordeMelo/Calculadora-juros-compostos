async function calcular() {
    const principal = parseFloat(document.getElementById("principal").value);
    const taxaPercentual = parseFloat(document.getElementById("taxa").value);
    const meses = parseInt(document.getElementById("meses").value);
    const aporte = parseFloat(document.getElementById("aporte").value) || 0;

    const taxaMensal = taxaPercentual / 100;

    const resposta = await fetch("/calcular", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            principal: principal,
            taxa_mensal: taxaMensal,
            meses: meses,
            aporte_mensal: aporte
        })
    });

    const dados = await resposta.json();

    document.getElementById("resultado").innerHTML = `
        <p><strong>Montante final:</strong> R$ ${dados.montante_final}</p>
        <p><strong>Total investido:</strong> R$ ${dados.total_investido}</p>
        <p><strong>Total em juros:</strong> R$ ${dados.total_juros}</p>
    `;
}
