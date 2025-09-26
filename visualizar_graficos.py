#!/usr/bin/env python3
"""
Visualização dos Gráficos de Cinemática - Posição vs Tempo e Velocidade vs Tempo

Este script cria visualizações dos quatro casos analisados na solução:
- Gráfico A: Movimento com velocidade constante negativa
- Gráfico B: Movimento com velocidade constante positiva  
- Gráfico C: Repouso seguido de movimento uniforme
- Gráfico D: Movimento por impulsos

Uso:
    python visualizar_graficos.py
"""

import matplotlib.pyplot as plt
import numpy as np

def criar_graficos():
    """Cria e exibe os gráficos de posição e velocidade para os 4 casos."""
    
    # Configuração do tempo
    t = np.linspace(0, 6, 1000)
    
    # Criar figura com subplots
    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    fig.suptitle('Análise de Gráficos: Posição vs Tempo → Velocidade vs Tempo', fontsize=16)
    
    # Gráfico A: Movimento com velocidade constante negativa
    # Posição: x(t) = 4 - t (linha decrescente)
    x_A = 4 - t
    v_A = np.full_like(t, -1)  # Velocidade constante = -1 m/s
    
    axes[0, 0].plot(t, x_A, 'b-', linewidth=2)
    axes[0, 0].set_title('Gráfico A: Posição vs Tempo')
    axes[0, 0].set_xlabel('Tempo (s)')
    axes[0, 0].set_ylabel('Posição (m)')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].axhline(y=0, color='k', linestyle='-', alpha=0.3)
    
    axes[1, 0].plot(t, v_A, 'r-', linewidth=2)
    axes[1, 0].set_title('Velocidade vs Tempo')
    axes[1, 0].set_xlabel('Tempo (s)')
    axes[1, 0].set_ylabel('Velocidade (m/s)')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].axhline(y=0, color='k', linestyle='-', alpha=0.3)
    axes[1, 0].set_ylim(-2, 2)
    
    # Gráfico B: Movimento com velocidade constante positiva
    # Posição: x(t) = -3 + t (linha crescente)
    x_B = -3 + t
    v_B = np.full_like(t, 1)  # Velocidade constante = +1 m/s
    
    axes[0, 1].plot(t, x_B, 'b-', linewidth=2)
    axes[0, 1].set_title('Gráfico B: Posição vs Tempo')
    axes[0, 1].set_xlabel('Tempo (s)')
    axes[0, 1].set_ylabel('Posição (m)')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].axhline(y=0, color='k', linestyle='-', alpha=0.3)
    
    axes[1, 1].plot(t, v_B, 'r-', linewidth=2)
    axes[1, 1].set_title('Velocidade vs Tempo')
    axes[1, 1].set_xlabel('Tempo (s)')
    axes[1, 1].set_ylabel('Velocidade (m/s)')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].axhline(y=0, color='k', linestyle='-', alpha=0.3)
    axes[1, 1].set_ylim(-2, 2)
    
    # Gráfico C: Repouso seguido de movimento uniforme
    t_transicao = 2.0
    x_C = np.where(t <= t_transicao, 1, 1 + 1.5*(t - t_transicao))
    v_C = np.where(t <= t_transicao, 0, 1.5)
    
    axes[0, 2].plot(t, x_C, 'b-', linewidth=2)
    axes[0, 2].set_title('Gráfico C: Posição vs Tempo')
    axes[0, 2].set_xlabel('Tempo (s)')
    axes[0, 2].set_ylabel('Posição (m)')
    axes[0, 2].grid(True, alpha=0.3)
    axes[0, 2].axhline(y=0, color='k', linestyle='-', alpha=0.3)
    axes[0, 2].axvline(x=t_transicao, color='g', linestyle='--', alpha=0.5, label='Transição')
    
    axes[1, 2].plot(t, v_C, 'r-', linewidth=2)
    axes[1, 2].set_title('Velocidade vs Tempo')
    axes[1, 2].set_xlabel('Tempo (s)')
    axes[1, 2].set_ylabel('Velocidade (m/s)')
    axes[1, 2].grid(True, alpha=0.3)
    axes[1, 2].axhline(y=0, color='k', linestyle='-', alpha=0.3)
    axes[1, 2].axvline(x=t_transicao, color='g', linestyle='--', alpha=0.5)
    axes[1, 2].set_ylim(-0.5, 2)
    
    # Gráfico D: Movimento por impulsos (simplificado)
    # Posições constantes com mudanças abruptas
    t_mudancas = [1, 3, 5]
    posicoes = [0, 2, 2, 4, 4, 1]
    
    # Criar função degrau para posição
    x_D = np.zeros_like(t)
    for i, tempo in enumerate(t):
        if tempo < t_mudancas[0]:
            x_D[i] = posicoes[0]
        elif tempo < t_mudancas[1]:
            x_D[i] = posicoes[1]
        elif tempo < t_mudancas[2]:
            x_D[i] = posicoes[3]
        else:
            x_D[i] = posicoes[5]
    
    axes[0, 3].plot(t, x_D, 'b-', linewidth=2)
    axes[0, 3].set_title('Gráfico D: Posição vs Tempo')
    axes[0, 3].set_xlabel('Tempo (s)')
    axes[0, 3].set_ylabel('Posição (m)')
    axes[0, 3].grid(True, alpha=0.3)
    axes[0, 3].axhline(y=0, color='k', linestyle='-', alpha=0.3)
    for t_mud in t_mudancas:
        axes[0, 3].axvline(x=t_mud, color='g', linestyle='--', alpha=0.5)
    
    # Para as velocidades, mostrar impulsos como setas
    axes[1, 3].axhline(y=0, color='r', linewidth=2)
    for t_mud in t_mudancas:
        if t_mud == t_mudancas[0] or t_mud == t_mudancas[1]:  # Impulsos positivos
            axes[1, 3].arrow(t_mud, 0, 0, 3, head_width=0.1, head_length=0.2, 
                           fc='red', ec='red', linewidth=2)
            axes[1, 3].text(t_mud, 3.5, '↑ Impulso +', ha='center', fontsize=8)
        else:  # Impulso negativo
            axes[1, 3].arrow(t_mud, 0, 0, -3, head_width=0.1, head_length=0.2, 
                           fc='red', ec='red', linewidth=2)
            axes[1, 3].text(t_mud, -3.5, '↓ Impulso -', ha='center', fontsize=8)
    
    axes[1, 3].set_title('Velocidade vs Tempo')
    axes[1, 3].set_xlabel('Tempo (s)')
    axes[1, 3].set_ylabel('Velocidade (m/s)')
    axes[1, 3].grid(True, alpha=0.3)
    axes[1, 3].set_ylim(-4, 4)
    
    # Ajustar layout
    plt.tight_layout()
    
    # Adicionar texto explicativo
    fig.text(0.02, 0.02, 
             'A: Velocidade constante negativa | B: Velocidade constante positiva | ' +
             'C: Repouso → Movimento | D: Impulsos (mudanças instantâneas)',
             fontsize=10, ha='left')
    
    return fig

def main():
    """Função principal - cria e salva os gráficos."""
    
    print("Criando visualizações dos gráficos de cinemática...")
    
    # Configurar matplotlib para português
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.grid'] = True
    
    # Criar os gráficos
    fig = criar_graficos()
    
    # Salvar a figura
    plt.savefig('/home/runner/work/teste/teste/graficos_cinematica.png', 
                dpi=300, bbox_inches='tight')
    print("Gráficos salvos como 'graficos_cinematica.png'")
    
    # Mostrar os gráficos (se em ambiente interativo)
    try:
        plt.show()
    except:
        print("Ambiente não-interativo - gráficos salvos apenas como arquivo.")
    
    print("\nAnálise completa:")
    print("- Gráfico A: Movimento rectilíneo uniforme com v = -1 m/s")
    print("- Gráfico B: Movimento rectilíneo uniforme com v = +1 m/s") 
    print("- Gráfico C: Repouso (v=0) seguido de movimento uniforme (v=1.5 m/s)")
    print("- Gráfico D: Impulsos representando mudanças instantâneas de posição")

if __name__ == "__main__":
    main()