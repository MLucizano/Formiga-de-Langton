# 🐜 Formiga de Langton - Simulação Interativa em Python

Este projeto implementa a **Formiga de Langton**, um autômato celular bidimensional que segue regras extremamente simples, mas que gera padrões complexos e imprevisíveis ao longo do tempo.  

A implementação foi feita em **Python**, combinando **programação orientada a objetos**, **representação esparsa de matrizes**, **renderização gráfica em tempo real** e **expansão dinâmica de grid**.

---

## 🚀 Tecnologias e Bibliotecas
- **Python 3.12+**
- **Matplotlib** → visualização interativa com suporte a eventos de teclado e mouse.
- **NumPy** → manipulação eficiente de arrays e vetores.
- **SciPy (sparse.lil_matrix)** → representação esparsa do grid, garantindo eficiência em memória.

---

## 🧠 Técnicas e Abordagens Utilizadas

### 1. **Programação Orientada a Objetos (POO)**
O código foi estruturado em duas classes principais:
- `Formiga`: encapsula a posição, direção e comportamento da formiga (virar, andar e interagir com o mundo).
- `Mundo`: gerencia o grid, expansão dinâmica da matriz e renderização gráfica.

Essa separação melhora a **coesão**, facilita manutenção e permite **reuso** da lógica em outras simulações.

---

### 2. **Sparse Representation (Matriz Esparsa)**
O grid é armazenado como uma **`lil_matrix`** (SciPy), que mantém apenas os elementos **ativos** (células pretas).  
Essa abordagem é fundamental para simulações de longo prazo, já que:
- A memória cresce apenas com células realmente alteradas.
- É possível simular dezenas de milhares de passos sem sobrecarga excessiva.

---

### 3. **Expansão Dinâmica do Grid**
O mundo não tem tamanho fixo:  
- Quando a formiga atinge a borda, a matriz é expandida automaticamente em +2 unidades.  
- O conteúdo anterior é copiado para o centro da nova matriz.  
- Existe ainda um **mecanismo de "wrap-around"** (quando atinge o limite máximo), fazendo a formiga reaparecer no lado oposto.

---

### 4. **Eventos Interativos**
- Pressionar **ESC** interrompe a execução.  
- Fechar a janela também finaliza a simulação.  
- Isso é feito via `matplotlib.mpl_connect`, conectando eventos do teclado e do fechamento da janela ao loop principal.

---

### 5. **Renderização Gráfica em Tempo Real**
- Uso de `plt.ion()` (modo interativo) para atualizar a cada passo.  
- `plt.imshow()` para renderizar o grid em escala de cinza.  
- `plt.scatter()` para exibir a formiga com o marcador correspondente à sua orientação (`^`, `>`, `v`, `<`).  

---

### 6. **Lógica Algorítmica (Formiga de Langton)**
A regra segue o modelo clássico:
- Se a célula atual for **preta** → vira **à direita** e pinta de branco.  
- Se a célula atual for **branca** → vira **à esquerda** e pinta de preto.  
- Move-se uma unidade na direção atual.  

Esse algoritmo, apesar de simples, leva a padrões altamente não triviais após milhares de iterações — incluindo o surgimento de um “highway” (estrada infinita).

---
## Animação da execução

Aqui está a animação , mostrando milhares de passos e a formação da famosa "estrada" (highway) da formiga:

![Formiga de Langton - GIF ](/formiga_langton_longo.gif)

> **Dica:** para ver a simulação completa, você também pode executar o script Python que gera o GIF.


## ▶️ Como Executar

Clone o repositório:
```bash
git clone https://github.com/MLucizano/formiga-langton.git
cd formiga-langton
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

Execute a simulação:
```bash
python src/formiga_langton.py
```

---

## 📚 Conceitos relacionados
- Autômatos Celulares
- Programação Orientada a Objetos
- Sparse Representation
- Padrões emergentes
- Sistemas complexos
---

✨ Desenvolvido por Matheus Pereira Lucizano graduado em Analise e Desenvolvimento de Sistemas, e entusiasta de algoritmos, otimização e simulações computacionais.

