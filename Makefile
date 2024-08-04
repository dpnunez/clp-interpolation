all:
	gcc -o mandelbrot.out fractal.c -lm
	gcc -shared -o fractal.so -fPIC fractal.c
	pyinstaller --onefile --add-data 'fractal.so:.' main.py
	./dist/main