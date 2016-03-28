#!/bin/sh

if ! nosetests --with-coverage --cover-package=elapsed --cover-min-percentage=99; then
    exit 1
fi

if ! flake8 .; then
    exit 1
fi
