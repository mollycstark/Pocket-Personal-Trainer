const images = document.querySelectorAll('img');
for (const image of images) {
  image.addEventListener('click', (event) => {
    const movement = event.target;
    const movementName = movement.alt;

    fetch(`/api/select_movements?movement_name=${movementName}`)
  })
};    
    


