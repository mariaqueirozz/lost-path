# Testes

Esta pasta contem testes automatizados do projeto.

## Arquivos

- `test_logica.py`: testa regras básicas do jogo.
- `test_mapa.py`: verifica funções relacionadas ao mapa.

## Como executar

```bash
python -m pytest
```
Os testes garantem o funcionamento das principais regras implementadas durante o desenvolvimento do projeto.

## Boas praticas

- Crie testes para toda regra de pontuacao, vidas e condicoes de fim de jogo.
- Prefira funcoes pequenas e testaveis no modulo `src/funcoes.py`.
