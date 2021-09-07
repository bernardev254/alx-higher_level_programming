#include "lists.h"
#include <stdlib.h>
#include <unistd.h>

/**
 * insert_node - inserts a number in an ordered linked list
 * @head: double pointer to the linked list
 * @number: number to insert in the new node
 *
 * Return: address of the new node, or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *newNode;

	current = *head;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);

	if (head == NULL)
		return (NULL);

	newNode->n = number;
	newNode->next = NULL;

	if (*head == NULL)
	{
		*head = newNode;
		return (*head);
	}
	if (number < current->n)
	{
		*head = newNode;
		newNode->next = current;
		return (*head);
	}

	while (current->next->n < number && current->next->next)
	{
		current = current->next;
	}
	if (current->next->next)
	{
		newNode->next = current->next;
		current->next = newNode;
	}
	else
		current->next->next = newNode;

	return (newNode);
}

