$(document).ready(function() {
    //FOR ADD ITEMS AND DISPLAY IN TABLE
    $('#additems').click(function() {
        var itemname = $('#name').val();
        var unitnum = $('#unit').val();
        var quanum = $('#quantity').val();


        var dataE = "<tr><td>" + itemname + "</td><td>" + unitnum + "</td><td>" + quanum + "</td><td>" + " <button class='btn btn-danger'> Delete </button>" + "</td><td>";
        $('#additemsTable').append(dataE);
        $('#name').val('');
        $('#unit').val('');
        $('#quantity').val('');

        console.log(itemname);
        console.log(unitnum);
        console.log(quanum);

    })

})