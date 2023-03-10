document.querySelector('img').addEventListener('click', (event) => {
    event.preventDefault();
  
    const humanId = document.querySelector('select[name="human_id"]').value;
    fetch(`/api/humans?human_id=${humanId}`)
      .then((response) => response.json())
      .then((jsonResponse) => {
        showHuman(jsonResponse);
      });
  });