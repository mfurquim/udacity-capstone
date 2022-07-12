CC=pandoc
FLAGS=--filter pandoc-eqnos --filter pandoc-tablenos --filter pandoc-include --from=markdown-smart --to=latex --indented-code-classes=numberLines --highlight-style=zenburn --listings --ascii --number-sections

tex:
	@echo "MD -> TEX"
	iconv -t utf-8 proposal.md | $(CC) $(FLAGS) --output=mid.tex
	@cat beg.tex > tmp.tex
	@cat mid.tex >> tmp.tex
	@cat end.tex >> tmp.tex
	@mv tmp.tex ../proposal.tex
