const setsInputFields = document.querySelectorAll('.get-sets');
for (const setInputField of setsInputFields) {
  setInputField.addEventListener('submit', (event) => {
    event.preventDefault();
    alert("Sets updated");

    const form = event.target;
    const workoutMovement = form.dataset.id;

    const numSets = document.querySelector('select[name="num_sets"]').value;

    fetch(`/api/select_sets_reps?workout_movement=${workoutMovement}&num_sets=${numSets}`)
  })
};   

const repsInputFields = document.querySelectorAll('.get-reps');
for (const repInputField of repsInputFields) {
  repInputField.addEventListener('submit', (event) => {
    event.preventDefault();
    alert("Reps updated");

    const form = event.target;
    const workoutMovement = form.dataset.id;

    const numReps = document.querySelector('select[name="num_reps"]').value;

    fetch(`/api/select_sets_reps?workout_movement=${workoutMovement}&num_reps=${numReps}`)
  })
}; 


    