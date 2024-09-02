document.getElementById('file-input').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        Papa.parse(file, {
            header: true,
            dynamicTyping: true,
            complete: function(results) {
                const data = results.data;
                performEDA(data);
            }
        });
    }
});

function performEDA(data) {
    const outputDiv = document.getElementById('output');

    // Display the first few rows of the dataset
    const preview = data.slice(0, 5);
    let html = "<h2>Dataset Preview (First 5 Rows):</h2>";
    html += "<table border='1'><thead><tr>";
    
    Object.keys(preview[0]).forEach(key => {
        html += `<th>${key}</th>`;
    });

    html += "</tr></thead><tbody>";
    
    preview.forEach(row => {
        html += "<tr>";
        Object.values(row).forEach(value => {
            html += `<td>${value}</td>`;
        });
        html += "</tr>";
    });

    html += "</tbody></table>";
    outputDiv.innerHTML = html;

    // Calculate some basic statistics
    let numRows = data.length;
    let numCols = Object.keys(data[0]).length;

    outputDiv.innerHTML += `<h2>Basic Statistics</h2>`;
    outputDiv.innerHTML += `<p>Number of Rows: ${numRows}</p>`;
    outputDiv.innerHTML += `<p>Number of Columns: ${numCols}</p>`;
}
