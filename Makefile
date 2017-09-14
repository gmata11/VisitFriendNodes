
test:
	for i in `seq 5 20`; do \
	   echo Testing graph $$i; \
	   python create-connected-graph.py $$i 0.50 > test.gr; \
	   python2 ignota.py test.gr > sol.txt; \
	   python checker.py test.gr sol.txt; \
	done

clean :
	$(RM) test.gr sol1.txt sol2.txt
