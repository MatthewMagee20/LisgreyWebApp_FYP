$(document).ready(function(){
    $('input.timepicker').timepicker({
        timeFormat: 'H:mm p',
        interval: 60,
        minTime: '12',
        maxTime: '21:00pm',
        startTime: '10:00',
        dynamic: false,
        dropdown: true,
        scrollbar: true
    });
    $('#id_date').datepicker({
    })
});
