// Dynamically create a form that allows the 
// user to add as many exercises as they like

$('#start').click(function(e) {
    let workoutSets = $("#workout-sets");
    let numberOfSets = workoutSets.children('.set-count').last().val()
    console.log(numberOfSets)    
    let exerciseNumber = $('#exercise-1-sets').attr("id")
    let x = parseInt(exerciseNumber.slice(9, 10))
    for (i = 0; i < numberOfSets; i++) {
        workoutSets.append(`<input type="number" 
        name="weight-${i}-exercise-${x}" placeholder="weight">
        <input type="number" name="reps-${i}-exercise-${x}" placeholder="reps">
        <input type="number" name="rpe-${i}-exercise-${x}" placeholder="rpe"><br>`);
}});

$('#add-exercise').click(function(e) {
    let workoutSets = $("#workout-sets");
    let exerciseNumber = workoutSets.children('.exercise-name').last().attr("id")
    let x = parseInt(exerciseNumber.slice(9, 10)) + 1
    workoutSets.append(`<input type="text" id="exercise-${x}-name" 
    class="exercise-name" name="exercise-${x}-name" placeholder="exercise_name">
    <input id="exercise-${x}-sets" class="set-count" type="number" name="exercise-${x}-sets" placeholder="sets">
    <input id="exercise-${x}-sets" type="number" name="exercise-${x}-reps" placeholder="reps">
    <br>`)
});