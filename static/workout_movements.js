function handleInput() {
  // Declare variables
  const input = document.getElementById('userInput');
  const filter = input.value.toUpperCase();
  const ul = document.getElementById("myUL");
  const li = ul.getElementsByTagName('li');

  // Loop through all list items, and hide those who don't match the search query
  for (i = 0; i < li.length; i++) {
    p = li[i].getElementsByTagName("p")[0];
    txtValue = p.innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
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
    


