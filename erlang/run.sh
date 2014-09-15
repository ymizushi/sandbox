#!/bin/sh
erlc hello.erl
erl -noshell -run hello start -s init stop
