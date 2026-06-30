"""Quantum computing inference algorithms, and hybrid AI models.

This package provides quantum-classical hybrid inference tools including:
- Quantum kernel methods via PennyLane
- Variational quantum circuits for ML
- Qiskit-based quantum simulation wrappers
"""
__version__ = "0.1.0"


def check_backends():
    """Check which quantum backends are available."""
    backends = {}
    try:
        import qiskit
        backends["qiskit"] = qiskit.__version__
    except ImportError:
        backends["qiskit"] = None
    try:
        import pennylane
        backends["pennylane"] = pennylane.__version__
    except ImportError:
        backends["pennylane"] = None
    try:
        import cirq
        backends["cirq"] = cirq.__version__
    except ImportError:
        backends["cirq"] = None
    return backends


def list_algorithms():
    """Return available quantum inference algorithms."""
    return [
        "quantum_kernel",
        "variational_classifier",
        "quantum_annealing_hybrid",
        "vqe_regression",
    ]
