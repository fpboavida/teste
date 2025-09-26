# Solução: Cinemática de Partículas - Gráficos de Posição vs Tempo e Velocidade vs Tempo

## Problema
A partir dos gráficos de posição versus tempo (A, B, C, D) apresentados, desenhar os correspondentes gráficos de velocidade versus tempo.

<img>

## Fundamentação Teórica

### Relação entre Posição e Velocidade
A velocidade é definida como a derivada da posição em relação ao tempo:

```
v = dx/dt
```

Graficamente, isso significa que:
- **A velocidade em qualquer instante é igual à inclinação (declive) da recta tangente ao gráfico posição-tempo nesse ponto**
- Para gráficos lineares, a inclinação é constante, logo a velocidade é constante
- Para gráficos horizontais, a inclinação é zero, logo a velocidade é zero
- Para gráficos com mudanças abruptas de posição, há velocidades infinitas (fisicamente impossível, mas matematicamente representado por impulsos)

### Método de Análise
1. Identificar os diferentes segmentos do gráfico posição-tempo
2. Calcular a inclinação de cada segmento
3. A inclinação corresponde à velocidade nesse intervalo de tempo
4. Desenhar o gráfico velocidade-tempo correspondente

## Análise Detalhada dos Gráficos

### Gráfico A: Decréscimo Linear
**Características do gráfico posição-tempo:**
- Linha recta com inclinação negativa
- A posição diminui linearmente de um valor positivo para um valor negativo
- Inclinação constante e negativa

**Análise matemática:**
- Se x(t) = x₀ + v·t, onde v < 0
- Então v = dx/dt = constante negativa
- A velocidade é constante e negativa durante todo o intervalo

**Gráfico velocidade-tempo resultante:**
- Linha horizontal abaixo do eixo do tempo
- Velocidade constante e negativa
- Valor: v = Δx/Δt = (x_final - x_inicial)/(t_final - t_inicial) < 0

### Gráfico B: Acréscimo Linear
**Características do gráfico posição-tempo:**
- Linha recta com inclinação positiva
- A posição aumenta linearmente de um valor negativo para um valor positivo
- Inclinação constante e positiva

**Análise matemática:**
- Se x(t) = x₀ + v·t, onde v > 0
- Então v = dx/dt = constante positiva
- A velocidade é constante e positiva durante todo o intervalo

**Gráfico velocidade-tempo resultante:**
- Linha horizontal acima do eixo do tempo
- Velocidade constante e positiva
- Valor: v = Δx/Δt = (x_final - x_inicial)/(t_final - t_inicial) > 0

### Gráfico C: Repouso Seguido de Movimento
**Características do gráfico posição-tempo:**
- Primeira parte: linha horizontal (posição constante)
- Segunda parte: linha recta com inclinação positiva
- Transição abrupta entre os dois comportamentos

**Análise matemática:**
- **Primeira fase:** x(t) = constante → v = dx/dt = 0
- **Segunda fase:** x(t) = x₀ + v·t, onde v > 0 → v = dx/dt = constante positiva
- Mudança instantânea de velocidade no ponto de transição

**Gráfico velocidade-tempo resultante:**
- Primeira parte: linha horizontal no zero (velocidade nula)
- Segunda parte: linha horizontal acima do eixo (velocidade positiva constante)
- Transição vertical instantânea entre as duas fases

### Gráfico D: Movimento por Degraus
**Características do gráfico posição-tempo:**
- Segmentos horizontais (posição constante)
- Mudanças abruptas e verticais de posição
- Alternância entre repouso e "saltos" instantâneos

**Análise matemática:**
- **Durante os segmentos horizontais:** x(t) = constante → v = dx/dt = 0
- **Durante as mudanças verticais:** Δx ≠ 0 mas Δt = 0 → v = Δx/Δt → ±∞
- Na prática, estas transições representam mudanças muito rápidas (impulsos)

**Gráfico velocidade-tempo resultante:**
- Linhas horizontais no zero durante os períodos de repouso
- Impulsos (picos infinitos) nos instantes das mudanças de posição
- A direcção dos impulsos (positiva ou negativa) depende do sentido da mudança de posição

## Gráficos Velocidade-Tempo Resultantes

### Resumo dos Resultados:

**Gráfico A → Velocidade A:**
```
v |
  |
  |________________
  |                \
  |                 \______ t
  |________________________
  0
```
Velocidade constante negativa

**Gráfico B → Velocidade B:**
```
v |     ________________
  |    /
  |   /
  |__/______________________ t
  0
```
Velocidade constante positiva

**Gráfico C → Velocidade C:**
```
v |        ________________
  |       |
  |       |
  |_______|________________ t
  0
```
Zero seguido de velocidade constante positiva

**Gráfico D → Velocidade D:**
```
v |   ↑       ↑       ↓
  |   |       |       |
  |___|_______|_______|____ t
  0
```
Impulsos alternados com períodos de repouso

## Conceitos Importantes

### 1. Interpretação Física
- **Velocidade positiva:** movimento no sentido positivo do eixo
- **Velocidade negativa:** movimento no sentido negativo do eixo
- **Velocidade zero:** partícula em repouso
- **Mudanças abruptas:** acelerações infinitas (não físicas, mas matematicamente válidas)

### 2. Continuidade e Derivabilidade
- A posição pode ser contínua mas não derivável (como no gráfico C)
- Quando a posição não é derivável, a velocidade apresenta descontinuidades
- As mudanças verticais instantâneas (gráfico D) representam situações idealizadas

### 3. Aplicações Práticas
- **Gráfico A:** Movimento rectilíneo uniforme retardado
- **Gráfico B:** Movimento rectilíneo uniforme acelerado
- **Gráfico C:** Início de movimento a partir do repouso
- **Gráfico D:** Sistemas com impulsos ou choques

## Conclusão

A análise dos gráficos posição-tempo e a construção dos correspondentes gráficos velocidade-tempo demonstra a relação fundamental entre estas duas grandezas cinemáticas. A velocidade, como derivada da posição, representa geometricamente a inclinação da curva posição-tempo, permitindo uma interpretação visual directa do movimento da partícula.

Este exercício ilustra conceitos fundamentais da cinemática e prepara para o estudo de situações mais complexas envolvendo aceleração e movimento não-uniforme.