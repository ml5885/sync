const colors = [
	"#f1f0e7",
	"#4870a9",
	"#736334",
	"#58878C",
	"#BF6B04",
	"#8C1E14",
	"#314F64",
];

function getRandomColor() {
	const randomIndex = Math.floor(Math.random() * colors.length);
	let color = colors[randomIndex];
	return color;
}

$(function () {
	var color = getRandomColor();
	console.log(color);

	document.documentElement.style.setProperty("--highlight-color", color);
	document.documentElement.style.setProperty("--font-color", "#f1f0e7");
	if (color === "#f1f0e7") {
		document.documentElement.style.setProperty("--font-color", "#333333");
		info = $("div.info");
		info.css("background-color", "var(--font-color)");
		info.css("color", "var(--highlight-color)");
	}
});
