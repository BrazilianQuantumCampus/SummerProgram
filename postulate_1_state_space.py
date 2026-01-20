from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

def demonstrate_state_space_proof():
    print("||| Postulado 1: Espaço de Estados (Prova Matemática) |||")
    
    # ||| Parte 1: Definição Teórica |||
    print("\n[Passo 1] Definição Teórica")
    print("O estado é um vetor coluna unitário.")
    # Vetor |0>
    ket_0 = np.array([[1], [0]])
    print(f"Estado |0> (Numpy):\n{ket_0}")
    
    # ||| Porta Hadamard (Matriz de Mudança de Base) |||
    H_gate = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]])
    print(f"\nMatriz Hadamard (H):\n{H_gate}")
    
    # ||| Parte 2: Cálculo Algebrico |||
    print("\n[Passo 2] Cálculo Algébrico (Matriz x Vetor)")
    # H * |0>
    final_state_math = np.dot(H_gate, ket_0)
    print(f"H |0> Calculado:\n{final_state_math}")
    
    # ||| Parte 3: Simulação Qiskit |||
    print("\n[Passo 3] Simulação usando qiskit.quantum_info.")
    qc = QuantumCircuit(1)
    qc.h(0)
    state_qiskit = Statevector.from_instruction(qc).data.reshape(2,1)
    print(f"Estado Qiskit:\n{state_qiskit}")
    
    # ||| Parte 4: Comparação/Prova |||
    print("\n[Passo 4] Prova da Equivalência")
    # Comparar (usando allclose para tolerância de ponto flutuante)
    if np.allclose(final_state_math, state_qiskit):
        print(">> SUCESSO: O cálculo manual (Álgebra Linear) coincide com a simulação quântica.")
    else:
        print(">> FALHA: Divergência encontrada.")
        
    # ||| Passo 5: Plotar Circuito |||
    print("\n[Passo 5] Gerando imagem do circuito...")
    
    # Captura a figura para adicionar título
    fig = qc.draw(output='mpl')
    fig.suptitle("Postulado 1: Espaço de Estados (Superposição)")
    fig.savefig('circuit_postulate_1.png')
    print("Salvo em: circuit_postulate_1.png")

if __name__ == "__main__":
    demonstrate_state_space_proof()

