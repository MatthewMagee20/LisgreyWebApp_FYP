$(document).ready(function(){
    $('input.timepicker').timepicker({
        timeFormat: 'h:mm p',
        interval: 60,
        minTime: '12',
        maxTime: '9:00pm',
        defaultTime: '12',
        startTime: '10:00',
        dynamic: false,
        dropdown: true,
        scrollbar: true
    });
    $('#id_date').datepicker({
        dateFormat: 'dd-mm-yy',
        beforeShow: function (input, inst) {
        setTimeout(function(){
            inst.div.outerWidth($(input).outerWidth());
        },0);
    },
    })
});
