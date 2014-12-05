#ifndef SYNTAX_TREE_H
#define SYNTAX_TREE_H

enum token_type {
    TOKEN_PLUS,
    TOKEN_MINUS,
    TOKEN_MUL,
    TOKEN_DIV
};

typedef struct {
    enum token_type type;
    const char *value;
} token_t;

typedef struct {
    token_t token;
    token_t *next_token;
} token_iter_t;


token_iter_t *token_list_new(token_t token)
{
    token_iter_t *token_iter = (token_iter_t*)malloc(sizeof(token_iter_t));
    if (token_iter == NULL) {
        fprintf(stderr, "token_iter_t memory allocation is failed.");
    }
    return token_iter;
}

void *token_iter_push(token_iter_t *token_iter, token_t token)
{
    while (true) {
        if (token_iter->next_token == NULL) {
            token_iter->next_token = &token;
            break;
        }
        token_iter = token_iter->next_token;
    }
    return token_list;
}

token_list_t *token_list = token_list_new()

#endif
