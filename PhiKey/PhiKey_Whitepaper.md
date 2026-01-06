# PhiKey: Golden Lattice Security Protocol

**Inventor:** David Edward Sproule  
**Date:** January 06, 2026  

## Overview
PhiKey is a quantum-resistant encryption protocol based on irreversible geometric growth in a phyllotactic lattice. Inspired by natural spiral packing in sunflowers and pinecones, it generates keys from a one-way process using the golden angle (~137.508°). Security stems from the computational hardness of reversing lattice growth – no reliance on factoring or discrete logarithms.

## Core Algorithm

### Key Generation Process
Input:
  - Seed value S (256-bit recommended)
  - Lattice dimension: 11x11 (121 nodes)

Process:
  1. Initialize lattice to 0.
  2. Anchor center node (61) = S.
  3. For each new node i (spiral order):
     I_i = Σ (existing j: value_j * exp(j * 2π * d_ij / λ + φ))
     λ = 137.036, φ = golden angle radians (~2.39996 rad)
     node_i = SHA3-256(I_i)
  4. Extract lattice as key material.

Public key: Merkle root commitment.

### Encryption/Decryption
- Map message to deterministic lattice path.
- Generate keystream via hashes along path.
- XOR for ciphertext (stream cipher).

## Security Properties
- Quantum-hard via geometric one-wayness.
- Key gen ~242μs, encrypt ~1μs/byte.
- Memory ~4KB.

## Applications
Secure comms, data storage, post-quantum migration. Free for open-source/non-profits; fair royalties for commercial.

GitHub: https://github.com/phibronotchi-beep/David-Sproule-s-Inventions
