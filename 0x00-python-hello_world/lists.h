#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * Structure representing a node, in a linked list.
 * @n; integer value stored in the node.
 * @next; pointer to the node in the list.
 *
 * This structure defines the properties of a linked list node.
 */
typedef struct listint_s
{
  int n;
  struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
