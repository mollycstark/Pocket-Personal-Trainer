function handleInput() {
  // Declare variables
  const input = document.getElementById('userInput');
  const filter = input.value.toUpperCase();
  // const ul = document.getElementById("myUL");
  const row = document.querySelectorAll('.movement');

  // Loop through all list items, and hide those who don't match the search query
  for (i = 0; i < row.length; i++) {
    text = row[i].getElementsByTagName("text")[0];
    txtValue = text.innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      row[i].style.display = "";
    } else {
      row[i].style.display = "none";
    }
  }
}


const images = document.querySelectorAll('img');
for (const image of images) {
  image.addEventListener('click', (event) => {
    const movement = event.target;
    const movementName = movement.alt;

    alert("Movement logged");

    fetch(`/api/select_completed_movements?movement_name=${movementName}`)
  })
};    
    