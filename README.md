# Scanneur de ports TCP
Un scanneur de ports réseau multi-threads écrit en Python.

## Fonctionnalités

- Scan d'une plage de ports donnée par l'utilisateur
- Multi-threadings (parallélisation) pour des scans rapide
- Identification du nom du service associée au port ouvert
- Interface en ligne de commandes

## Utilisation
Aucune dépendance nécessaire, Python 3 suffit

Lancement typique : python scanner.py 127.0.0.1 -s 1 -e 1000 -n 100