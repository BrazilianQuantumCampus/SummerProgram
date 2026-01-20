from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

def demonstrate_unitary_proof():
    print("--- Postulado 2: Evolução Unitária (Prova Matemática) ---")
    
    # --- Passo 1: Verificar se a matriz é unitária ---
    print("\n[Passo 1] Verificação de Unitaridade (U'U = I)")
    # Matriz X (Pauli-X)
    X_gate = np.array([[0, 1], [1, 0]])
    print(f"Matriz X:\n{X_gate}")
    
    # Cálculo de U Dagger (Transposta Conjugada) - para reais é apenas transposta
    X_dagger = X_gate.conj().T
    
    # Multiplicação U' * U
    Identity_check = np.dot(X_dagger, X_gate)
    print(f"X' * X:\n{Identity_check}")
    
    if np.allclose(Identity_check, np.eye(2)):
        print(">> PROVA: A matriz é Unitária.")
    
    # --- Passo 2: Evolução Temporal ---
    print("\n[Passo 2] Evolução do Estado")
    ket_0 = np.array([[1], [0]])
    print(f"Estado Inicial |0>:\n{ket_0}")
    
    # Evolução 1: X|0>
    state_1_math = np.dot(X_gate, ket_0)
    print(f"Após aplicar X (Manual): \n{state_1_math}")
    
    # Evolução 2: X(X|0>)
    state_final_math = np.dot(X_gate, state_1_math)
    print(f"Após aplicar X novamente (Manual): \n{state_final_math}")
    
    # --- Passo 3: Comparação com Qiskit ---
    print("\n[Passo 3] Verificação com Qiskit")
    qc = QuantumCircuit(1)
    qc.x(0)
    qc.x(0)
    state_qiskit = Statevector.from_instruction(qc).data.reshape(2,1)
    
    if np.allclose(state_final_math, state_qiskit):
         print(">> SUCESSO: A evolução manual coincide com a simulação.")

    # --- Passo 4: Plotar Circuito ---
    print("\n[Passo 4] Gerando imagem do circuito...")
    # Adicionando medição para visualização final
    qc.measure_all(inplace=True)
    # Para visualizar melhor, vamos desenhar o circuito que foi executado
    fig = qc.draw(output='mpl')
    fig.suptitle("Postulado 2: Evolução Unitária (X -> X -> Medição)")
    fig.savefig('circuit_postulate_2.png')
    print("Salvo em: circuit_postulate_2.png")

if __name__ == "__main__":
    demonstrate_unitary_proof()
