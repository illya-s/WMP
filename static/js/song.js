const select = document.getElementById('select')
const select_defolt = select.getAttribute("data-key")

var keys = [
		{name: 'Ab', value: 0, type: 'F'},
		{name: 'A', value: 1, type: 'N'},
		{name: 'A#', value: 2, type: 'S'},
		{name: 'Bb', value: 2, type: 'F'},
		{name: 'H', value: 3, type: 'N'},
		{name: 'C', value: 4, type: 'N'},
		{name: 'C#', value: 5, type: 'S'},
		{name: 'Db', value: 5, type: 'F'},
		{name: 'D', value: 6, type: 'N'},
		{name: 'D#', value: 7, type: 'S'},
		{name: 'Eb', value: 7, type: 'F'},
		{name: 'E', value: 8, type: 'N'},
		{name: 'F', value: 9, type: 'N'},
		{name: 'F#', value: 10, type: 'S'},
		{name: 'Gb', value: 10, type: 'F'},
		{name: 'G', value: 11, type: 'N'},
		{name: 'G#', value: 0, type: 'S'}
];

let block = '<select name="key" id="key">'

for (l in keys) {
	if (keys[l].name == select_defolt) {
		block += `<option selected="selected" value="` + keys[l].name + `">` + keys[l].name + ` (Original)</option>`
	} else {
		block += `<option value="` + keys[l].name + `">` + keys[l].name + `</option>`
	}
}
block += '</select>'
select.innerHTML = block


const song_block = document.getElementById("song_block");
const text = song_block.getAttribute("data-text");
var tx = text.replace(/\n/g, "<br>");

function splitSongText(text) {
	var blocks = text.split(/\[(.*?)\]/);
	var inText = '';

	for (var i = 1; i < blocks.length; i += 2) {
		var type = blocks[i].toLowerCase();
		var content = blocks[i + 1].trim();
		inText += `<div class="block">
			<p class="block_type">${type}</p>
			<p class="block_text">${content}</p>
		</div>`
	}
	song_block.innerHTML = inText
}

splitSongText(tx);