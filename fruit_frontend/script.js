function onload() {
  fetchFruits();
}

async function fetchFruits() {
  const url = "http://127.0.0.1:8000/fruits/";
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const result = await response.json();
    displayFruits(result);
    console.log(result);
  } catch (error) {
    console.error(error.message);
  }
}

function displayFruits(fruits) {
  const tableBody = document.getElementById("fruit-table-rows");
  fruits.forEach((fruit) => {
    const row = document.createElement("tr");
    row.innerHTML = `
            <td>${fruit.name}</td>
            <td>${fruit.color}</td>
            <td>${fruit.weight}</td>
        `;
    tableBody.appendChild(row);
  });
}
