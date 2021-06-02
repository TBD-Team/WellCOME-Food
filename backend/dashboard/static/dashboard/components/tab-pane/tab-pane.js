function autoresizeploty() {
    var doc = $(".tab-pane.active .plotly-graph-div");
    for (var i = 0; i < doc.length; i++) {
        Plotly.relayout(doc[i], { autosize: true });
    }
}

$(document).on('shown.bs.tab', function (event) {
    autoresizeploty()
})

$('.tab-pane-select').on('change', function (e) {
    $(this).parent().find('.tab-pane').removeClass('active in')
    $('#' + $(e.currentTarget).val()).addClass("active in");
    autoresizeploty()
})