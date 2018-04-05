SHELL := /bin/bash

.PHONY: all
all:
	@echo "No longer necessary. Use python setup.py install."

hungarian: hungarian/hungarian.so

hungarian/hungarian.so:
	cd hungarian && \
	TF_INC=$$(python -c 'import tensorflow as tf; print(tf.sysconfig.get_include())') && \
	if [ `uname` == Darwin ];\
	then g++-5 -std=c++11 -shared hungarian.cc -o hungarian.so -D_GLIBCXX_USE_CXX11_ABI=0 -fPIC -I $$TF_INC -undefined dynamic_lookup;\
	else g++-5 -std=c++11 -shared hungarian.cc -o hungarian.so -D_GLIBCXX_USE_CXX11_ABI=0 -fPIC -I  $$TF_INC; fi
