// Dynamically create a form that allows the 
// user to add as many exercises as they like

// $('#start').click(function(e) {
//     let workoutSets = $("#workout-sets");
//     let numberOfSets = workoutSets.children('.set-count').last().val()   
//     let exerciseNumber = workoutSets.children('.set-count').last().attr("id")
//     let x = parseInt(exerciseNumber.slice(9, 10))
//     for (i = 0; i < numberOfSets; i++) {
//         $('#save').before(`<input type="number" step="0.5"
//             name="weight-${i+1}-exercise-${x}" placeholder="weight">
//             <input type="number" name="reps-${i+1}-exercise-${x}" placeholder="reps">
//             <input type="number" step="0.5" name="rpe-${i+1}-exercise-${x}" 
//             placeholder="rpe"><br>`);
// }});

// $('#add-exercise').click(function(e) {
//     let workoutSets = $("#workout-sets");
//     let exerciseNumber = workoutSets.children('.exercise-name').last().attr("id")
//     let x = parseInt(exerciseNumber.slice(9, 10)) + 1
//     $('#save').before(`<input type="text" id="exercise-${x}-name" 
//         class="exercise-name" name="exercise-${x}-name" placeholder="exercise_name">
//         <input id="exercise-${x}-sets" class="set-count" type="number" 
//         name="exercise-${x}-sets" placeholder="sets">
//         <input id="exercise-${x}-sets" type="number" name="exercise-${x}-reps" 
//         placeholder="reps"><br>`)
// });

$('.log-exercise').click(function(e) {
    let workoutSets = $("#workout-sets");
    let numberOfSets = $('.set-count').last().val()
    console.log(numberOfSets)    
    let exerciseNumber = $('.set-count').last().attr("id")
    let x = parseInt(exerciseNumber.slice(9, 10))
    for (i = 0; i < numberOfSets; i++) {
        $('#save').before(
            `<div class="row input-group d-inline-flex justify-content-center">
                    <div class="col-1"></div>
                    <input type="number" step="0.5" name="weight-${i+1}-exercise-${x}" placeholder="weight" class="col-4">
                    <input type="number" name="reps-${i+1}-exercise-${x}" placeholder="reps" class="col-2">
                    <input type="number" step="0.5" name="rpe-${i+1}-exercise-${x}" placeholder="rpe" class="col-2">
                    <div class="input-group-append col-2 p-0">
                        <button class="btn btn-outline-secondary w-100" type="button" id="delete-set-${i+1}">X</button>
                    </div>
                    <div class="col-1"></div>
                </div>
                <br>`);
}});

$('#add-exercise').click(function(e) {
    let workoutSets = $("#workout-sets");
    let exerciseNumber = workoutSets.children('.exercise-name').last().attr("id")
    let x = parseInt(exerciseNumber.slice(9, 10)) + 1
    $('#save').before(`<input type="text" id="exercise-${x}-name" 
        class="exercise-name" name="exercise-${x}-name" placeholder="exercise_name">
        <input id="exercise-${x}-sets" class="set-count" type="number" 
        name="exercise-${x}-sets" placeholder="sets">
        <input id="exercise-${x}-sets" type="number" name="exercise-${x}-reps" 
        placeholder="reps"><br>`)
});
