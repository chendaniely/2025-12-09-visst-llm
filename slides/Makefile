.PHONY: render
render:
	rm -rf ../_site ../docs
	quarto render index.qmd

.PHONY: preview
preview:
	quarto preview index.qmd --port 54321

.PHONY: setup
setup:
	quarto add emilhvitfeldt/quarto-revealjs-editable
	quarto add gadenbuie/countdown/quarto
