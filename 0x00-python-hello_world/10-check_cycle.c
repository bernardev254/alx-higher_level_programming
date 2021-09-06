#include "lists.h"

/**
 * check_cylce - a function that checks if a singly linked list has a
 * cycle in it
 * @list: the list to check
 *
 * Return: 1, if a cycle is present or 0, if otherwise
 */
int check_cycle(listint_t *list)
{
        listint_t *hd = list;
        listint_t *tl = list;

        while (tl && hd && hd->next)
        {
                tl = tl->next;
                hd = hd->next->next;

                if (hd == tl)
                        return (1);
        }

        return (0);
}

