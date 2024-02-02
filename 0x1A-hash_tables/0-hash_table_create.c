#include <stdlib.h>
#include "hash_table.h"  // Assuming you have a header file for the hash table structure

/**
 * hash_table_create - Creates a hash table
 * @size: Size of the array
 *
 * Returns: A pointer to the newly created hash table
 *          or NULL if allocation fails
 */
hash_table_t *hash_table_create(unsigned long int size)
{
    // Allocate memory for the hash table
    hash_table_t *hash_table = (hash_table_t *)malloc(sizeof(hash_table_t));
    if (hash_table == NULL)
    {
        // Allocation failed
        return NULL;
    }

    // Allocate memory for the array of pointers to linked lists
    hash_table->array = (hash_node_t **)calloc(size, sizeof(hash_node_t *));
    if (hash_table->array == NULL)
    {
        // Allocation failed
        free(hash_table);
        return NULL;
    }

    // Set the size of the hash table
    hash_table->size = size;

    return hash_table;
}
