const setsInputFields = document.querySelectorAll('.get-sets');
for (const setInputField of setsInputFields) {
  setInputField.addEventListener('submit', (event) => {
    event.preventDefault();

    const form = event.target;
    const workoutMovement = form.dataset.id;

    const numSets = form.querySelector('select[name="num_sets"]').value;
    form.querySelector('.btn-primary').value = "Updated";

    fetch(`/api/select_sets_reps?workout_movement=${workoutMovement}&num_sets=${numSets}`)
  })
};   

const repsInputFields = document.querySelectorAll('.get-reps');
for (const repInputField of repsInputFields) {
  repInputField.addEventListener('submit', (event) => {
    event.preventDefault();

    const form = event.target;
    const workoutMovement = form.dataset.id;

    const numReps = form.querySelector('select[name="num_reps"]').value;
    form.querySelector('.btn-primary').value = "Updated";

    fetch(`/api/select_sets_reps?workout_movement=${workoutMovement}&num_reps=${numReps}`)
  })
}; 


    