CC=riscv64-linux-gnu-gcc

FILE?=

build: setup 
	docker build -t fas .

all: copy notebook

copy: compile
	cat temp/O0.s > temp/O0.txt
	cat temp/O2.s > temp/O2.txt

compile: 
	$(CC) temp/input.c -S -O0 -o temp/O0.s 
	$(CC) temp/input.c -S -O2 -o temp/O2.s 
	@echo "Compilation complete."

setup: clean 
	@if [ ! -f "$(FILE)" ]; then \
		echo "File not found: $(FILE)"; \
		exit 1; \
	fi
	cp $(FILE) temp/input.c
	@echo "Ready: $(FILE) → temp/input.c"

clean:
	rm -f temp/*.s
	rm -f temp/*.txt
	rm -f temp/*.c

notebook: 
	cd output && jupyter notebook --allow-root --ip=0.0.0.0 --port=8888 
