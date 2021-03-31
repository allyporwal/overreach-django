// Dynamically create a form that allows the 
// user to add as many exercises as they like

// Listen for events in the form on log exercise buttons
$('#workout-sets').on('click', '.log-exercise', function() {
    let numberOfSets = $('.set-count').last().val();
    // ensure the correct number is attached to element attributes
    // when inserted into DOM
    let exerciseNumber = $('.set-count').last().attr("id");
    let x = parseInt(exerciseNumber.slice(9, 10));
    // add the desired number of sets
    for (i = 0; i < numberOfSets; i++) {
        $('#form-separator').before(
            `<div class="form-row">
                <div class="form-group col-6">
                    <label class="sr-only" for="weight-${i+1}-exercise-${x}">Weight</label>
                    <input type="number" step="0.5" name="weight-${i+1}-exercise-${x}" placeholder="Weight lifted" class="form-control" required>
                </div>
                <div class="form-group col-2">
                    <label class="sr-only" for="reps-${i+1}-exercise-${x}">Reps</label>
                    <input type="number" name="reps-${i+1}-exercise-${x}" placeholder="Reps" class="form-control" required>
                </div>
                <div class="form-group col-2">
                    <label class="sr-only" for="rpe-${i+1}-exercise-${x}">RPE</label>
                    <input type="number" step="0.5" name="rpe-${i+1}-exercise-${x}" placeholder="RPE" class="form-control" required>
                </div>
                <div class="form-group col-2">
                    <label class="sr-only" for="delete-set-${x}">Delete set</label>
                    <button class="btn btn-outline-secondary w-100 form-control" name="delete-set-${x}" type="button"><i class="fas fa-trash"></i></button>                
                </div>              
            </div>`);
}});



$('#add-exercise').click(function() {
    let workoutSets = $("#workout-sets");
    let exerciseNumber = $('.exercise-name').last().attr("id");
    let x = parseInt(exerciseNumber.slice(9, 10)) + 1;
    $('#form-separator').before(`
                        <hr class="mt-1 w-50">
                        <div class="form-row exercise-row">
                          <div class="form-group col-4">
                              <label for="exercise-${x}-name">Exercise ${x}</label>
                              <input type="text" id="exercise-${x}-name" class="exercise-name form-control" name="exercise-${x}-name">
                          </div>
                          <div class="form-group col-2">
                              <label for="exercise-${x}-sets">Sets</label>
                              <input id="exercise-${x}-sets" class="set-count form-control" type="number" name="exercise-${x}-sets">
                          </div>
                          <div class="form-group col-2">
                              <label for="exercise-${x}-reps">Reps</label>
                              <input id="exercise-${x}-reps" class="form-control" type="number" name="exercise-${x}-reps">
                          </div>
                          <div class="form-group col-2">
                              <label for="log-exercise-${x}">&nbsp;</label>
                              <button id="log-${x}" class="btn btn-outline-secondary w-100 form-control log-exercise" name="log-exercise-${x}" type="button"><i class="fas fa-check"></i></button>                
                          </div>
                          <div class="form-group col-2">
                              <label for="delete-exercise-${x}">&nbsp;</label>
                              <button id="delete-exercise-${x}" class="btn btn-outline-secondary w-100 form-control delete-exercise" name="delete-exercise-${x}" type="button"><i class="fas fa-trash"></i></button>                
                          </div>
                      </div>`)
});
