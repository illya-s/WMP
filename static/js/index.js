var future = false
var switch_btn = document.getElementById("switch_btn")

switch_btn.addEventListener("click", function(e) {
	if (future == false) {
		switch_btn.textContent = "Предстоящие"
		future = true
	} else {
		switch_btn.textContent = "Прошедшие"
		future = false
	}
})

$(document).ready(function() {
	$('#switch_btn').click(function(e) {
		e.preventDefaul;
		$.ajax({
			type: 'GET',
			url: '/ministrys/',
			data: {'future': future},
			success: function(data) {
				$('#ministrys').html(data.ministrys_html);
			},
			error: function(xhr, status, error) {
				console.error('Ошибка при выполнении запроса');
			}
		});
	});
});