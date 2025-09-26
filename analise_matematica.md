# Análise Matemática Formal - Gráficos de Cinemática

## Fundamentos Matemáticos

### Definição da Velocidade
A velocidade instantânea é definida como a derivada da posição em relação ao tempo:

```
v(t) = dx/dt = lim[Δt→0] (x(t+Δt) - x(t))/Δt
```

### Interpretação Geométrica
Geometricamente, a velocidade num instante t corresponde ao declive da recta tangente à curva x(t) nesse ponto.

## Análise Matemática de Cada Gráfico

### Gráfico A: Função Linear Decrescente

**Função posição:**
```
x(t) = x₀ - at, onde a > 0
```

**Cálculo da velocidade:**
```
v(t) = dx/dt = d/dt(x₀ - at) = -a = constante < 0
```

**Exemplo numérico:**
Se x(t) = 4 - t, então:
- x₀ = 4 m
- a = 1 m/s
- v(t) = -1 m/s ∀t

**Verificação:**
- t = 0: x(0) = 4 m
- t = 6: x(6) = -2 m
- v = Δx/Δt = (-2-4)/(6-0) = -1 m/s ✓

### Gráfico B: Função Linear Crescente

**Função posição:**
```
x(t) = x₀ + bt, onde b > 0
```

**Cálculo da velocidade:**
```
v(t) = dx/dt = d/dt(x₀ + bt) = b = constante > 0
```

**Exemplo numérico:**
Se x(t) = -3 + t, então:
- x₀ = -3 m
- b = 1 m/s
- v(t) = +1 m/s ∀t

**Verificação:**
- t = 0: x(0) = -3 m
- t = 6: x(6) = 3 m
- v = Δx/Δt = (3-(-3))/(6-0) = 1 m/s ✓

### Gráfico C: Função por Partes

**Função posição:**
```
x(t) = {
  x₀,           para 0 ≤ t ≤ t₁
  x₀ + c(t-t₁), para t > t₁
}
onde c > 0
```

**Cálculo da velocidade:**
```
v(t) = {
  0,  para 0 ≤ t ≤ t₁
  c,  para t > t₁
}
```

**Propriedades matemáticas:**
- A função x(t) é contínua em t = t₁
- A função x(t) **não é derivável** em t = t₁
- A função v(t) tem uma **descontinuidade de salto** em t = t₁

**Exemplo numérico:**
Se t₁ = 2s, x₀ = 1m, c = 1.5 m/s:
```
x(t) = {
  1,              para 0 ≤ t ≤ 2
  1 + 1.5(t-2),   para t > 2
}

v(t) = {
  0,     para 0 ≤ t ≤ 2
  1.5,   para t > 2
}
```

### Gráfico D: Função Degrau com Descontinuidades

**Função posição (exemplo):**
```
x(t) = {
  x₁,  para 0 ≤ t < t₁
  x₂,  para t₁ ≤ t < t₂
  x₃,  para t₂ ≤ t < t₃
  x₄,  para t ≥ t₃
}
```

**Análise da velocidade:**
- **Nos intervalos contínuos:** v(t) = 0 (derivada de constante)
- **Nos pontos de descontinuidade:** v(t) não está definida

**Representação usando distribuições:**
```
v(t) = (x₂-x₁)δ(t-t₁) + (x₃-x₂)δ(t-t₂) + (x₄-x₃)δ(t-t₃)
```
onde δ(t) é a função delta de Dirac.

## Propriedades Matemáticas Avançadas

### Continuidade e Derivabilidade

| Gráfico | x(t) Contínua? | x(t) Derivável? | v(t) Contínua? |
|---------|----------------|-----------------|----------------|
| A       | ✓              | ✓               | ✓              |
| B       | ✓              | ✓               | ✓              |
| C       | ✓              | ✗ (em t₁)       | ✗ (em t₁)      |
| D       | ✗              | ✗               | ✗              |

### Teorema do Valor Médio

Para os gráficos A e B (funções deriváveis), o Teorema do Valor Médio garante que:
```
∃c ∈ [a,b] : f'(c) = (f(b) - f(a))/(b - a)
```

Como x(t) é linear, temos f'(c) = constante, logo o teorema é trivialmente satisfeito.

### Integração: Área sob o Gráfico v-t

A área sob o gráfico velocidade-tempo representa o deslocamento:
```
Δx = ∫[t₁ to t₂] v(t) dt
```

**Gráfico A:**
```
Δx = ∫[0 to T] (-a) dt = -aT
```

**Gráfico B:**
```
Δx = ∫[0 to T] b dt = bT
```

**Gráfico C:**
```
Δx = ∫[0 to t₁] 0 dt + ∫[t₁ to T] c dt = c(T - t₁)
```

**Gráfico D:**
```
Δx = ∑ᵢ (xᵢ₊₁ - xᵢ) = diferença total de posição
```

## Aplicações do Cálculo Diferencial

### Relação Fundamental da Cinemática

```
Posição → Velocidade → Aceleração
x(t)   →   v(t)     →   a(t)
       dx/dt       dv/dt = d²x/dt²
```

### Operações Inversas

```
Aceleração → Velocidade → Posição
a(t)      →   v(t)    →   x(t)
          ∫a dt       ∫v dt
```

## Exercícios de Aplicação

### Exercício 1: Análise Quantitativa
Dado x(t) = 2t² - 3t + 1, determine:
1. v(t) = ?
2. Quando v(t) = 0?
3. Posição no instante v = 0?

**Solução:**
1. v(t) = dx/dt = 4t - 3
2. v(t) = 0 ⟹ 4t - 3 = 0 ⟹ t = 3/4 s
3. x(3/4) = 2(3/4)² - 3(3/4) + 1 = -1/8 m

### Exercício 2: Movimento Composto
Uma partícula move-se segundo:
```
x(t) = {
  t²,        para 0 ≤ t ≤ 2
  4 + 2(t-2), para t > 2
}
```

Determine v(t) e analise a continuidade.

**Solução:**
```
v(t) = {
  2t,  para 0 ≤ t < 2
  2,   para t > 2
}
```

- Em t = 2⁻: v = 4 m/s
- Em t = 2⁺: v = 2 m/s
- Descontinuidade de salto em t = 2

## Conclusões Matemáticas

1. **A derivação gráfica** é uma ferramenta poderosa para analisar movimento
2. **Descontinuidades na posição** levam a impulsos na velocidade
3. **A continuidade da posição não garante a continuidade da velocidade**
4. **Funções por partes** requerem análise cuidadosa nos pontos de transição
5. **A interpretação física** deve acompanhar sempre a análise matemática

### Nota sobre Realismo Físico

Os impulsos (velocidades infinitas) são **matematicamente válidos** mas **fisicamente impossíveis**. Na realidade:
- Transições levam tempo finito
- Forças têm magnitude limitada  
- Acelerações são finitas

Os modelos com impulsos são úteis para:
- Simplificar análises complexas
- Estudar limites de processos rápidos
- Compreender comportamentos idealizados