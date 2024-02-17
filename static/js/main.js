$(document).ready(function() {
	$('#pagination').on('click', '.page-link', function(e) {
		e.preventDefault();
		var page = $(this).data('page');

		$.ajax({
			type: 'GET',
			url: '/songs/',
			data: {'page': page},
			success: function(data) {
				$('#song_list').html(data.songs_html);
				$('#pagination').html(data.pagination_html);
				window.history.pushState("", "", `?page=`+page);
			},
			error: function() {alert('Ошибка при загрузке данных.')}
		});
	});
});

$(document).ready(function () {
	$('#searchInput').on('input', function () {
			var query = $(this).val().trim();
			$.ajax({
					url: '/songs/search/',
					type: 'GET',
					data: {q: query},
					success: function (data) {
							$('#song_list').html(data.songs_html);
							$('#pagination').html(data.pagination_html);
					},
					error: function (error) {
							console.log('Ошибка AJAX-запроса');
					}
			});
	});
});