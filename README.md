# odkazove_prilezitosti

Skript na hledání příležitostí k získání odkazů na určitá klíčová slova na určitých doménách. 
Typickým příkladem využití je, když je k dispozici seznam domén, na kterých je možné zakoupit vytvoření odkazu v textu.

Skript funguje následovně:
- Na vstupu jsou klíčová slova a domény a skript projde všechna klíčová slova vs domény. 
- Na výstup vrátí ty URL, které na klíčové slovo ve spojení se site operátorem a doménou vypíše SERP Google.

Ve skriptu je třeba vyplnit tyto proměnné:
- URLs -> umístění CSV souboru, kde je seznam domén, na kterých hledat
- KWs -> umstění CSV souboru, kde je seznam klíčových slova, která na doménách hledáme
- FILE -> výstupní soubor
