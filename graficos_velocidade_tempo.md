# Gráficos Velocidade vs Tempo - Representação Detalhada

## Gráfico A: Velocidade Constante Negativa

```
Posição vs Tempo (A)          →          Velocidade vs Tempo (A)
                                         
x |                                      v |
  |\                                       |
  | \                                      |
  |  \                                     |________________________
  |   \                                    |                        
  |    \                                   |                        
  |     \                                  |                        
  |______\_________________ t              |________________________ t
  0       \                                0                        
           \                               
            \                              v = constante < 0
```

**Explicação:**
- Inclinação negativa constante → velocidade negativa constante
- v = Δx/Δt = (x₂-x₁)/(t₂-t₁) < 0

## Gráfico B: Velocidade Constante Positiva

```
Posição vs Tempo (B)          →          Velocidade vs Tempo (B)
                                         
x |      /                               v | ________________________
  |     /                                  |/                        
  |    /                                   |                         
  |   /                                    |                         
  |  /                                     |                         
  | /                                      |                         
  |/                                       |                         
  |________________________ t             |________________________ t
  0                                        0                        
                                           
                                           v = constante > 0
```

**Explicação:**
- Inclinação positiva constante → velocidade positiva constante
- v = Δx/Δt = (x₂-x₁)/(t₂-t₁) > 0

## Gráfico C: Repouso + Movimento Uniforme

```
Posição vs Tempo (C)          →          Velocidade vs Tempo (C)
                                         
x |        /‾‾‾‾‾‾‾‾‾‾                   v |        ________________
  |       /                                |       |                
  |      /                                 |       |                
  |     /                                  |       |                
  |    /                                   |       |                
  |___/                                    |_______|                
  |________________________ t             |________________________ t
  0                                        0       t₁               
                                           
                                           Fase 1: v = 0
                                           Fase 2: v = constante > 0
```

**Explicação:**
- **Fase 1:** Linha horizontal → inclinação = 0 → velocidade = 0
- **Fase 2:** Inclinação positiva constante → velocidade positiva constante
- **Transição:** Mudança instantânea de velocidade

## Gráfico D: Movimento por Impulsos

```
Posição vs Tempo (D)          →          Velocidade vs Tempo (D)
                                         
x | ‾|   ‾‾|     |‾‾                     v |  ↑    ↑     ↓     
  |  |     |     |                        | ∞|   ∞|    -∞|    
  |  |     |     |                        |  |    |     |     
  |__|_____|_____|____                     |__|____|_____|____ 
  |________________________ t             |________________________ t
  0                                        0                        
                                           
                                           Impulsos: v = ±∞ (teoricamente)
                                           Repouso: v = 0
```

**Explicação:**
- **Segmentos horizontais:** Inclinação = 0 → velocidade = 0
- **Mudanças verticais:** Δx ≠ 0, Δt = 0 → velocidade = ±∞ (impulsos)
- **Interpretação física:** Mudanças muito rápidas de posição

## Análise Quantitativa

### Para o Gráfico A:
Se x₁ = 4m (t=0s) e x₂ = -2m (t=6s):
```
v = Δx/Δt = (-2-4)/(6-0) = -6/6 = -1 m/s
```

### Para o Gráfico B:
Se x₁ = -3m (t=0s) e x₂ = 3m (t=6s):
```
v = Δx/Δt = (3-(-3))/(6-0) = 6/6 = +1 m/s
```

### Para o Gráfico C:
- **Primeira fase (0 ≤ t ≤ t₁):** v = 0 m/s
- **Segunda fase (t > t₁):** v = constante > 0

### Para o Gráfico D:
- **Entre mudanças:** v = 0 m/s
- **Durante mudanças:** v → ±∞ (impulsos de Dirac)

## Propriedades Matemáticas

### Continuidade da Velocidade
- **Gráficos A e B:** Velocidade contínua (função constante)
- **Gráfico C:** Descontinuidade no ponto de transição
- **Gráfico D:** Múltiplas descontinuidades (impulsos)

### Integração (Área sob a curva v-t)
A área sob o gráfico velocidade-tempo representa o deslocamento:

```
Δx = ∫v(t)dt
```

- **Gráfico A:** Área negativa → deslocamento negativo
- **Gráfico B:** Área positiva → deslocamento positivo
- **Gráfico C:** Área parcialmente positiva
- **Gráfico D:** Áreas dos impulsos → mudanças instantâneas de posição

## Aplicações Físicas

### Exemplos Reais:

**Gráfico A:** 
- Carro travando com desaceleração constante
- Objecto lançado verticalmente para cima (fase descendente)

**Gráfico B:**
- Carro acelerando uniformemente
- Queda livre (ignorando resistência do ar)

**Gráfico C:**
- Semáforo: parado → arranque súbito → velocidade constante
- Elevador: repouso → movimento uniforme

**Gráfico D:**
- Colisões perfeitamente elásticas
- Sistemas com molas muito rígidas
- Modelos idealizados com forças impulsivas

## Nota Importante sobre Impulsos

Os impulsos no gráfico D representam situações físicas idealizadas. Na realidade:
- As mudanças de velocidade levam sempre algum tempo
- Acelerações infinitas não existem fisicamente
- Os impulsos são úteis para modelar mudanças muito rápidas

```
Situação Real vs Modelo Idealizado:

Real:     v |    /‾‾\     Modelo:    v |  ↑
            |   /    \                 |  |
            |  /      \                |  |
            |_/________\___             |__|____
            
            Transição suave            Impulso instantâneo
```