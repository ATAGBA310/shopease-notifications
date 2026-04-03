# Shopease Notifications

## Objectif
Concevoir un système de notification multi-canal pour une plateforme e-commerce.

## Problème
Les notifications étaient codées en dur, ce qui rendait le système difficile à faire évoluer.

## Design patterns utilisés

### Observer
Le pattern Observer permet de déclencher plusieurs notifications en réaction à un événement métier, comme la création d’une commande, un paiement refusé ou une expédition.

### Strategy
Le pattern Strategy permet d’encapsuler les différents canaux de notification (email, SMS, notification interne) derrière une même interface.

## Architecture
- `EventManager` gère les abonnements et la diffusion des événements
- `NotificationListener` relie un événement à un canal et à un message
- `EcommercePlatform` déclenche les événements métier
- les channels gèrent l’envoi selon le type de notification
