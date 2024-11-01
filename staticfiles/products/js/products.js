$('.btt-link').click(function(e) {
    window.scrollTo(0,0)
})


$('.btn-delete').on('click', function(e) {
    e.preventDefault(); // Prevent the default link action
    var productId = $(this).data('product-id'); // Get the product ID from the data attribute
    $('#deleteModal-' + productId).modal('show'); // Show the corresponding modal
});

// jQuery to trigger the modal when the delete button is clicked
$('.btn-delete').on('click', function(e) {
    e.preventDefault(); // Prevent the default link action
    var productId = $(this).data('product-id'); // Get the product ID from the data attribute
    $('#deleteModal-' + productId).modal('show'); // Show the corresponding modal
});

$('#sort-selector').change(function() {
    var selector = $(this);
    var currentUrl = new URL(window.location);

    var selectedVal = selector.val();
    if(selectedVal != "reset"){
        var sort = selectedVal.split("_")[0];
        var direction = selectedVal.split("_")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
})