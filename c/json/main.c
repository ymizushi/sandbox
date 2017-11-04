#include <stdio.h>


enum JsonValueType {
    Number,
    String,
    Boolean
};

struct JsonValue {
    enum JsonValueType type;
    void* value;
};

void print_json_value(struct JsonValue *v) {
    if (v->type == Number) {
        printf("%d", (int)v->value);
    } else if (v->type == String) {
        printf("%s", (char*)v->value);
    } else if (v->type == Boolean) {
        printf("%d", (int)v->value);
    } else {

    }
}

int main(int argc, char const* argv[])
{
    struct JsonValue js_value = {String, "hoge"};
    print_json_value(&js_value);
    return 1;
}

