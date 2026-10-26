# LAB — rezerwacja stanowisk (projekt syntetyczny)

Repozytorium testowe POC **PM Agent**. Wszystkie osoby, zadania, daty i wymagania są
fikcyjne; projekt nie ma użytkowników ani wdrożenia. PM Agent czyta to repozytorium tylko
do odczytu (gałęzie, commity, pull requesty i wyniki CI), żeby porównać faktyczny stan kodu
z planem w OpenProject i wymaganiami w BookStack.

Zakres pierwszego etapu (DEC-001): jednorazowe rezerwacje bez kolizji (REQ-001) oraz
anulowanie własnej rezerwacji i dostępność stanowisk (REQ-002). Rezerwacje cykliczne nie są
przyjęte.

```bash
python -m pip install pytest==8.3.3
python -m pytest -q
```
