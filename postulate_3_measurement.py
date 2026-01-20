from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import numpy as np

def demonstrate_measurement_proof():
    print("--- Postulado 3: Medição (Prova Matemática) ---")
    
    # --- Passo 1: Estado antes da medição ---
    print("\n[Passo 1] Estado de Superposição")
    # Estado |+> = 1/sqrt(2) (|0> + |1>)
    psi = (1/np.sqrt(2)) * np.array([[1], [1]])
    print(f"Vetor de Estado |psi>:\n{psi}")
    
    # --- Passo 2: Cálculo Teórico da Probabilidade ---
    print("\n[Passo 2] Cálculo Teórico P(m) = |<m|psi>|^2")
    
    # Projetor para |0>
    # <0|psi>
    bra_0 = np.array([[1, 0]])
    inner_prod_0 = np.dot(bra_0, psi) # Escalar complexo
    prob_0 = np.abs(inner_prod_0)**2
    print(f"Amplitude <0|psi>: {inner_prod_0[0,0]:.4f}")
    print(f"Probabilidade P(0): {prob_0[0,0]:.4f} (Teórico)")
    
    # --- Passo 3: Experimento Monte Carlo (Qiskit) ---
    print("\n[Passo 3] Validação Experimental (1000 shots)")
    qc = QuantumCircuit(1)
    qc.h(0)
    qc.measure_all(inplace=True)
    
    simulator = AerSimulator()
    job = simulator.run(transpile(qc, simulator), shots=1000)
    counts = job.result().get_counts()
    
    p_0_experimental = counts.get('0', 0) / 1000.0
    print(f"Contagens: {counts}")
    print(f"P(0) Experimental: {p_0_experimental}")
    
    # Comparação
    erro = abs(p_0_experimental - prob_0[0,0])
    print(f"\nErro absoluto: {erro:.4f}")
    if erro < 0.05: # Margem de erro de 5% aceitável para 1000 shots
        print(">> SUCESSO: Resultado experimental converge para o teórico.")
    else:
        print(">> AVISO: Flutuação estatística normal, ou verificar shots.")

    # --- Passo 4: Plotar Circuito ---
    print("\n[Passo 4] Gerando imagem do circuito...")
    fig = qc.draw(output='mpl')
    fig.suptitle("Postulado 3: Medição (Colapso)")
    fig.savefig('circuit_postulate_3.png')
    print("Salvo em: circuit_postulate_3.png")

if __name__ == "__main__":
    demonstrate_measurement_proof()
