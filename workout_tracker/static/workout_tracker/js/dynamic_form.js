// Dynamically create a form that allows the 
// user to add as many exercises as they like

// Listen for events in the form on log exercise buttons
$('#workout-sets').on('click', '.log-exercise', function () {
    let numberOfSets = $(this).parent().prevUntil().find('.set-count').val();
    // ensure the correct number is attached to element attributes
    // when inserted into DOM
    let exerciseNumber = $(this).parent().parent().find('.set-count').attr("id");
    let x = parseInt(exerciseNumber.slice(9, 10));
    // delete any sets to ensure no extra sets added on further pushes of button
    let clearToPreventExtra = $(this).parent().parent().siblings(`.weight-reps-rpe-${x}`);
    clearToPreventExtra.remove();
    // add the desired number of sets
    for (i = 0; i < numberOfSets; i++) {
        $(this).parent().parent().after(
            `<div class="form-row weight-reps-rpe-${x}">
                <div class="form-group col-6">
                    <label class="sr-only" for="weight-${i + 1}-exercise-${x}">Weight</label>
                    <input type="number" step="0.5" name="weight-${i + 1}-exercise-${x}" placeholder="Weight lifted" min="1" max="1200" class="form-control" required>
                </div>
                <div class="form-group col-2">
                    <label class="sr-only" for="reps-${i + 1}-exercise-${x}">Reps</label>
                    <input type="number" name="reps-${i + 1}-exercise-${x}" placeholder="Reps" min="0" max="250" class="form-control" required>
                </div>
                <div class="form-group col-2">
                    <label class="sr-only" for="rpe-${i + 1}-exercise-${x}">RPE</label>
                    <input type="number" step="0.5" name="rpe-${i + 1}-exercise-${x}" placeholder="RPE" min="1" max="10" class="form-control" required>
                </div>
                <div class="form-group col-2">
                    <label class="sr-only" for="delete-set-${i}">Delete set</label>
                    <button class="btn btn-outline-secondary w-100 form-control delete-set" name="delete-set-${i}" type="button"><i class="fas fa-trash"></i></button>                
                </div>              
            </div>`);
        // $(this).prop("disabled", true)
    }
});

// listen for clicks on the add exericse button
$('#add-exercise').click(function () {
    // ensure no duplicates in numbering/naming of element attributes
    let exerciseNumber = $('.exercise-name').last().attr('id');
    let x = parseInt(exerciseNumber.slice(9, 10)) + 1;
    // insert another row into the DOM
    $('#form-separator').before(`
                        <hr id="exercise-seperator-${x}" class="mt-1 mb-1 w-100">
                        <div class="form-row exercise-row">
                          <div class="form-group col-sm-4">
                              <label for="exercise-${x}-name">Exercise</label>
                              <input type="text" id="exercise-${x}-name" class="exercise-name form-control" minlength="2" maxlength="32" name="exercise-${x}-name" required>
                          </div>
                          <div class="form-group col-3 col-sm-2">
                              <label for="exercise-${x}-sets">Sets</label>
                              <input id="exercise-${x}-sets" class="set-count form-control" type="number" min="1" max="50" name="exercise-${x}-sets" required>
                          </div>
                          <div class="form-group col-3 col-sm-2">
                              <label for="exercise-${x}-reps">Reps</label>
                              <input id="exercise-${x}-reps" class="form-control" type="number" min="0" max="250" name="exercise-${x}-reps" required>
                          </div>
                          <div class="form-group col-3 col-sm-2">
                              <label for="log-exercise-${x}">&nbsp;</label>
                              <button id="log-${x}" class="btn btn-outline-secondary w-100 form-control log-exercise" name="log-exercise-${x}" type="button"><i class="fas fa-check"></i></button>                
                          </div>
                          <div class="form-group col-sm-2 col-3">
                              <label for="delete-exercise-${x}">&nbsp;</label>
                              <button id="delete-exercise-${x}" class="btn btn-outline-secondary w-100 form-control delete-exercise" name="delete-exercise-${x}" type="button"><i class="fas fa-trash"></i></button>                
                          </div>
                      </div>`)
});

// delete elements from the form, allowing the user to
// drop exercises and their sets
$('#workout-sets').on('click', '.delete-exercise', function () {
    let exerciseNumber = $(this).attr('id');
    let exerciseToDelete = $(this).parent().parent();
    let x = parseInt(exerciseNumber.slice(16, 17));
    let setsToDelete = exerciseToDelete.siblings(`.weight-reps-rpe-${x}`);
    let hrToDelete = $(`#exercise-seperator-${x}`);
    setsToDelete.fadeOut(750, function () {
        setsToDelete.remove()
    });
    exerciseToDelete.fadeOut(750, function () {
        exerciseToDelete.remove()
    });
    hrToDelete.fadeOut(750, function () {
        hrToDelete.remove();
    });
});

$('#workout-sets').on('click', '.delete-set', function () {
    let numberOfSets = $(this).parent().parent().prevAll('.exercise-row').first().find('.set-count');
    let setNumber = numberOfSets.val();
    // let logButton = $(this).parent().parent().prev().find('.log-exercise');
    $(this).closest('.form-row').fadeOut(750, function () {
        $(this).closest('.form-row').remove();
        numberOfSets.val(setNumber - 1);
    });
});

