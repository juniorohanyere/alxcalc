# makefile for alxcalc

BIN_PATH = /usr/bin

DIR = $(HOME)/.alxcalc

SRCS = alxcalc.py alxcalc.sh base.py month.py project.py task.py

DEPS = month_0/month_0 month_0/month_0.orig

JSON = month_0/month_0.json

TARGET = $(BIN_PATH)/alxcalc

all: $(TARGET)

$(TARGET): $(SRCS) $(DEPS) $(JSON)
	sudo cp alxcalc.sh $(BIN_PATH)/alxcalc
	mkdir -p $(DIR)
	cp -r * $(DIR)
