async function loadBar(divId, apiUrl, title){
    const res = await fetch(apiUrl);
    const data = await res.json();

    Plotly.newPlot(divId, [{
        x: data.labels,
        y: data.values,
        type: "bar"
    }], {title});
}

async function loadPie(divId, apiUrl, title){
    const res = await fetch(apiUrl);
    const data = await res.json();

    Plotly.newPlot(divId, [{
        labels: data.labels,
        values: data.values,
        type: "pie"
    }], {title});
}

async function drawLine(divId, url, title){
    const res = await fetch(url);
    const data = await res.json();

    Plotly.newPlot(divId, [{
       x: data.labels,
       y: data.values,
        type: "scatter",
        mode: "lines+markers"
  }], { title });
}


loadBar("bar1", "/charts/bar-monthly-sales", "Monthly Sales");
loadPie("pie1", "/charts/pie-traffic-sources", "Traffic Sources");

loadBar("bar2", "/charts/bar-weekly-temperature", "Weekly Temperature");
loadPie("pie2", "/charts/pie-product-stock", "Product Stock");

drawLine("lineUsd", "/rates/usd", "USD (last 20 quotes)");
drawLine("lineChf", "/rates/chf", "CHF (last 20 quotes)");

