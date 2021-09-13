#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to linked list
 * Return: void
 */

void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
/**
  * is_palindrome - checks for a palindrome in linked lists
  * @head:pointer to list
  * Return: 1 if palindrome 0 otherwise
  */
int is_palindrome(listint_t **head)
{
	listint_t *this, *that, *tmp, *dup = NULL;
	this = that = tmp = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		that = that->next->next;
		if (!that)
		{
			dup = this->next;
			break;
		}
		if (!that->next)
		{
			dup = this->next->next;
			break;
		}
		this = this->next;
	}
	reverse_listint(&dup);

	while (dup && tmp)
	{
		if (tmp->n == dup->n)
		{
			dup = dup->next;
			tmp = tmp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}


