# Simple Python Blockchain

A basic blockchain implementation demonstrating core concepts like blocks, proof-of-work mining, and chain validation.

## Block Structure

Each block contains:
- `index`: Position in the chain (0 = genesis block)
- `timestamp`: When the block was created
- `data`: Information stored in the block
- `prev_hash`: Fingerprint of the previous block
- `nonce`: Number used for mining
- `hash`: Digital fingerprint of the current block


## Validation Logic

The blockchain checks:
1. **Genesis Block**:
   - Must have index 0
   - "Previous Hash" must be all zeros
   - Must contain "Genesis Block" as data

2. **All Other Blocks**:
   - Each block's hash must match its recalculated hash
   - A block's "Previous Hash" must equal the actual hash of the prior block
   - Block indices must be in perfect sequence (0, 1, 2,...)

## Proof-of-Work Approach

The mining process:
1. Finds a hash starting with "00" (simple difficulty)
2. Keeps changing the `nonce` value until the hash meets this requirement
3. Measures how long mining takes
4. Example mining output:
