$(document).ready(function () {
    setField();

    /**
      * This functions will prevent from inspectin elements on whole app
      */
    $('body').bind('contextmenu', function () {
        xdialog.alert("Right Click is disabled!");
        return false;
    });
    $(document).keydown(function (e) {
        if (e.which === 123) {
            xdialog.alert("Inspecet Element is disabled!");
            return false;
        }
    });

    /**
     * This function will show the 'go to the top' button
     * and scroll smoothly to the top of the page when button is clicked
     */
    $(document).scroll(function () {
        var y = $(this).scrollTop();
        if (y > 50) {
            $('.go-to-the-top').addClass('show');
        } else {
            $('.go-to-the-top').removeClass('show');
        }
    });
    $('#rocket').click(function () {
        $('html, body').animate({ scrollTop: 0 }, 'slow');
        return false;
    });

    /**
    * This function will display toasts
    */
    $('.toast').toast('show');
})

/**
 * This function will change color of select
 * box in Contact Form when offer is selected
 */

function setField() {
    let countrySelected = $('#id_offer').val();
    if (!countrySelected) {
        $('#id_offer').css('color', '#999999');
    }
    $('#id_offer').change(function () {
        countrySelected = $(this).val();
        if (!countrySelected) {
            $(this).css('color', '#999999');
        } else {
            $(this).css('color', '#212529');
        }
    });
}