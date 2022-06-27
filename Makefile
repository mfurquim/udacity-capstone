all:
	$(MAKE) -C tex all

clean:
	$(MAKE) -C tex clean
	@rm -vf proposal.pdf


