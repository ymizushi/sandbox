#ifndef FIGURE_H
#define FIGURE_H

typedef struct {
    int x;
    int y;
} point_t;

typedef struct {
    int width;
    int height;
} size_t;

typedef struct {
    point_t point;
    size_t size;
} figure_t;

typedef struct {
    figure_t figure
    figure_t *next_figure
} figure_iter_t;

int figure_iter_next() {

}



#endif
