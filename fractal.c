#include <stdio.h>
#include <stdlib.h>
#include <complex.h>

void get_color(int iter, int max_iter, int* r, int* g, int* b) {
    if (iter == max_iter) {
        *r = *g = *b = 0; // black
    } else {
        double t = (double) iter / max_iter;
        *r = (int)(9 * (1 - t) * t * t * t * 255);
        *g = (int)(15 * (1 - t) * (1 - t) * t * t * 255);
        *b = (int)(8.5 * (1 - t) * (1 - t) * (1 - t) * t * 255);
    }
}

void write_ppm(const char* filename, int width, int height, int** image) {
    int max_val = 255;
    FILE *fp = fopen(filename, "wb");
    if (fp == NULL) {
        fprintf(stderr, "Failed to open file for writing\n");
        exit(1);
    }
    
    fprintf(fp, "P3\n%d %d\n%d\n", width, height, max_val);

    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            int r = image[y][x*3+0];
            int g = image[y][x*3+1];
            int b = image[y][x*3+2];
            fprintf(fp, "%d %d %d ", r, g, b);
        }
        fprintf(fp, "\n");
    }

    fclose(fp);
}

int mandelbrot(double complex c, int max_iter) {
    double complex z = 0;
    int n = 0;

    while (cabs(z) <= 2 && n < max_iter) {
        z = z*z + c;
        n++;
    }

    return n;
}

int generate_fractal(int WIDTH, int HEIGHT, int MAX_ITER) {
    printf("WIDTH = %d, HEIGHT = %d, MAX_ITER = %d\n", WIDTH, HEIGHT, MAX_ITER);

    int** image = (int**) malloc(HEIGHT * sizeof(int*));
    if (image == NULL) {
        fprintf(stderr, "Failed to allocate memory for image rows\n");
        return 1;
    }

    for (int i = 0; i < HEIGHT; i++) {
        image[i] = (int*) malloc(WIDTH * 3 * sizeof(int));
        if (image[i] == NULL) {
            fprintf(stderr, "Failed to allocate memory for image columns\n");
            return 1;
        }
    }

    double x_min = -2.0, x_max = 1.0;
    double y_min = -1.5, y_max = 1.5;

    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++) {
            double real = x_min + (x_max - x_min) * x / (WIDTH - 1);
            double imag = y_min + (y_max - y_min) * y / (HEIGHT - 1);
            double complex c = real + imag * I;

            int iter = mandelbrot(c, MAX_ITER);
            int r, g, b;

            get_color(iter, MAX_ITER, &r, &g, &b);

            image[y][x*3+0] = r;
            image[y][x*3+1] = g;
            image[y][x*3+2] = b;
        }
    }

    write_ppm("mandelbrot.ppm", WIDTH, HEIGHT, image);

    for (int i = 0; i < HEIGHT; i++) {
        free(image[i]);
    }
    free(image);

    return 0;
}

int main(int argc, char *argv[]) {
    if (argc != 4) {
        fprintf(stderr, "Usage: %s <WIDTH> <HEIGHT> <MAX_ITER>\n", argv[0]);
        return 1;
    }

    int WIDTH = atoi(argv[1]);
    int HEIGHT = atoi(argv[2]);
    int MAX_ITER = atoi(argv[3]);

    return generate_fractal(WIDTH, HEIGHT, MAX_ITER);
}
