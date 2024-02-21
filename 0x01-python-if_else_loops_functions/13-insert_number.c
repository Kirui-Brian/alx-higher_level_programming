#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Insert a number into a sorted singly linked list.
 * @head: Pointer to pointer to the head node of the list.
 * @number: the number to insert.
 *
 * Return: Address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	/* Allocate memory for new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return NULL;

	/* Initialize new node */
	new_node->n = number;
	new_node->next = NULL;

	/* If the list is empty or the new ode should be inserted at the beginning */
	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return new_node;
	}

	/* Traverse the list to find the correct position to insert the new node */
	current = *head;
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}

	/* Insert the new node */
	new_node->next = current->next;
	current->next = new_node;

	return new_node;
}
