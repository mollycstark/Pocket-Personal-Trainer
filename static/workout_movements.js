function handleInput() {
  // Declare variables
  const input = document.getElementById('userInput');
  const filter = input.value.toUpperCase();
  // const ul = document.getElementById("myUL");
  // const li = ul.getElementsByTagName('li');
  const row = document.querySelectorAll('.col');

  // Loop through all row items, and hide those who don't match the search query
  for (i = 0; i < row.length; i++) {
    p = row[i].getElementsByTagName("h3")[0];
    txtValue = p.innerText;
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

    alert("Movement saved");

    fetch(`/api/select_workout_movements?movement_name=${movementName}`)
  })
};    
    


