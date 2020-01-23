# Uruchomienie
## Ładowanie embeddingów
 * Do katalogu ```core/embedding``` należy skopiować plik z modelem dystrubucyjnym embeddingu.
 * W pliku ```config.py``` należy zmodyfikować zmienne: 
    * ```embedding_path``` - ścieżka do pliku modelu
    * ```embedding_shape``` - rozmiar wektora
    
## Uruchomienie aplikacji
Przygotowane zostały obrazy Dockera wraz z skryptem ```docker-compose.yml```.
W katalogu głównym projektu należy wykonać:
```
docker-compose -f docker/docker-compose.yml up
```
Aplikacja działa na porcie 80.