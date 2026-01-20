# Postulados da Mecânica Quântica

Este documento define os quatro postulados fundamentais da mecânica quântica que serão demonstrados através de circuitos quânticos neste projeto.

## Postulado 1: Espaço de Estados
O estado de um sistema físico isolado é descrito por um vetor unitário em um espaço vetorial complexo com produto interno, conhecido como espaço de Hilbert.
- **Representação**: O estado é frequentemente denotado como $|\psi\rangle$ (notação bra-ket).
- **Superposição**: Se $|0\rangle$ e $|1\rangle$ são estados possíveis, então qualquer combinação linear $\alpha|0\rangle + \beta|1\rangle$ também é um estado válido, desde que $|\alpha|^2 + |\beta|^2 = 1$.

## Postulado 2: Evolução Unitária
A evolução temporal de um sistema quântico fechado é descrita por uma transformação unitária.
- **Equação**: $|\psi(t_2)\rangle = U(t_1, t_2)|\psi(t_1)\rangle$.
- **Propriedade**: A matriz $U$ deve ser unitária, ou seja, $U^\dagger U = I$. Isso garante que a norma do vetor de estado (e a probabilidade total) seja conservada.

## Postulado 3: Medição
A medição de uma observável quântica resulta em um dos autovalores dessa observável, e o estado do sistema colapsa para o autoestado correspondente.
- **Probabilidade**: A probabilidade de obter o resultado $m$ é dada por $P(m) = \langle \psi | M_m^\dagger M_m | \psi \rangle$, onde $M_m$ são os operadores de medição.
- **Colapso**: Imediatamente após a medição, o estado torna-se $\frac{M_m |\psi\rangle}{\sqrt{P(m)}}$.

## Postulado 4: Sistemas Compostos
O espaço de estados de um sistema físico composto é o produto tensorial dos espaços de estados dos sistemas componentes.
- **Matemática**: Se o sistema A está no estado $|\psi_A\rangle$ e o sistema B está no estado $|\psi_B\rangle$, o estado conjunto é $|\psi_A\rangle \otimes |\psi_B\rangle$.
- **Emaranhamento**: Nem todos os estados no espaço composto podem ser escritos como produto de estados individuais (ex: estado de Bell $\frac{|00\rangle + |11\rangle}{\sqrt{2}}$), o que leva ao fenômeno do emaranhamento.
