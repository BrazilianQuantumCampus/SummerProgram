from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

def demonstrate_composite_proof():
    print("--- Postulado 4: Sistemas Compostos (Prova Matemática) ---")
    
    # ||| Passo 1: Produto Tensorial |||
    print("\n[Passo 1] Construção do Estado Produto |+> sum |0>")
    # Qubit 0: |+> = 1/sqrt(2) [1, 1]
    q0 = (1/np.sqrt(2)) * np.array([[1], [1]])
    # Qubit 1: |0> = [1, 0]
    q1 = np.array([[1], [0]])
    
    print("Qubit 0 (|+>):\n", q0)
    print("Qubit 1 (|0>):\n", q1)
    
    # Tensor Product: kron (Kronecker product)
    # Estado conjunto inicial = |+> (x) |0>
    psi_initial = np.kron(q1, q0) # Nota: Qiskit usa ordem q1 (x) q0 (little-endian) para vetor [00, 01, 10, 11]
    # Qiskit ordena qubits como q_n ... q_0. 
    # Vou usar a convenção matemática padrão (q0 tensor q1) e ajustar a comparação se necessário.
    # Mas Qiskit visualiza Statevector como q_n...q_0. Entao Statevector([1,0,0,0]) é 00.
    # Vamos seguir a álgebra linear padrão aqui e comparar valores.
    
    # Vou calcular q0 (x) q1 manualmente para o usuário ver
    psi_math_initial = np.kron(q0, q1)
    print(f"\nProduto Tensorial Manual (q0 (x) q1):\n{psi_math_initial}")
    print("Interpretado como coeficientes de: |00>, |01>, |10>, |11>")
    
    # ||| Passo 2: Aplicação da CNOT |||
    print("\n[Passo 2] Aplicação da Matriz CNOT")
    # Matriz CNOT padrão (controle q0, alvo q1)
    # |00> -> |00>
    # |01> -> |01>
    # |10> -> |11>
    # |11> -> |10>
    CNOT_matrix = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ])
    print(f"Matriz CNOT:\n{CNOT_matrix}")
    
    psi_final_math = np.dot(CNOT_matrix, psi_math_initial)
    print(f"\nEstado Final Calculado (Bell State):\n{psi_final_math}")
    
    # ||| Passo 3: Verificação Qiskit |||
    print("\n[Passo 3] Simulação Qiskit")
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1) # Control 0, Target 1
    
    # O Qiskit usa little-endian (q1...q0). 
    # Meu cálculo manual foi q0 (x) q1 (big-endian).
    # O estado de Bell ideal (|00> + |11>) é simétrico, então os vetores devem ser iguais visualmente:
    # [1/rt2, 0, 0, 1/rt2]
    
    state_qiskit = Statevector.from_instruction(qc).data
    print(f"Vetor Qiskit:\n{state_qiskit}")
    
    # Comparar apenas os valores absolutos para evitar confusão de fase global ou ordenação simples neste caso simétrico
    if np.allclose(np.abs(psi_final_math.flatten()), np.abs(state_qiskit)):
        print(">> SUCESSO: O cálculo tensorial manual corresponde ao estado emaranhado gerado.")
    else:
        print(">> AVISO: Verificar convenção de endianness. (Mas para estado de BellPhi+, são iguais).")

    # ||| Passo 4: Plotar Circuito |||
    print("\n[Passo 4] Gerando imagem do circuito...")
    qc.measure_all(inplace=True)
    fig = qc.draw(output='mpl')
    fig.suptitle("Postulado 4: Sistemas Compostos (Emaranhamento)")
    fig.savefig('circuit_postulate_4.png')
    print("Salvo em: circuit_postulate_4.png")

if __name__ == "__main__":
    demonstrate_composite_proof()

