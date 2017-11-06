#include <stdio.h>

#define HASH_SIZE 20

struct HashEntry {
    int key;
    int value;
};

struct HashTable {
    struct HashEntry **entries;
};

int HashTable_hash(struct HashTable *table, int key) {
    int hash = key % HASH_SIZE;
    for(;hash<HASH_SIZE;hash++) {
        if (table->entries[hash]->key == key || table->entries[hash] == NULL) {
            return hash;
        } 
    }
    return -1;
}

int HashTable_set(struct HashTable *table, int key, int value) {
    int hash = HashTable_hash(table, key);
    if (hash == -1) {
        return -1;
    } else {
      struct HashEntry *entry = & (struct HashEntry){key, value};
      table->entries[hash] = entry;
      return 0;
    }
}

struct HashEntry* HashTable_get(struct HashTable *table, int key) {
    int hash = HashTable_hash(table, key);
    if (hash == -1) {
        return NULL;
    } else {
      return table->entries[hash];
    }
}

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

